# Panduan Praktik 4: Mengambil Data Bluesky lewat API Resmi

Mata kuliah Social Media Analytics, 3 SKS. Pengampu: Dr. Halim Maulana, S.T., M.Kom.

Praktik ini dikerjakan sendiri-sendiri di HP masing-masing. Semua perintah di bawah sudah diuji jalan di Termux pada 11 November 2026, jadi kalau hasilmu berbeda, penyebabnya biasanya ada di langkah yang terlewat, bukan di panduan.

Waktu praktik: 150 menit. Keluaran: satu berkas CSV, satu berkas log, satu berkas checksum, dan satu paragraf temuan.

---

## 1. Yang perlu disiapkan

| Bahan | Cara menyiapkan |
|---|---|
| Termux dan Python | Sudah ada di HP kalau Termux terpasang. Cek dengan `python3 --version` |
| Koneksi internet | Wifi kampus atau data seluler |
| Folder kerja | `mkdir -p ~/praktik-bsky` lalu `cd ~/praktik-bsky` |
| Skrip kolektor | Salin `blsky_collect.py` ke folder kerja |

Catatan penting tempat membuka berkas. Kartu SD di Android kadang menolak berkas skrip dijalankan langsung dari sana. Simpan skrip di folder dalam HP (Folder Termux), bukan di kartu SD. Kalau sudah tersimpan di SD, salin dulu: `cp /sdcard/path/blsky_collect.py ~/praktik-bsky/`.

Endpoint yang akan kita pakai bersifat **publik**, artinya tidak perlu login. Tidak ada kata sandi yang akan diminta di praktik ini.

---

## 2. Melihat JSON dengan mata sendiri (15 menit)

Sebelum memakai skrip, lihat dulu bentuk datanya. Tempel perintah ini:

```bash
curl -sS "https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed?actor=bsky.app&limit=2" | python3 -m json.tool
```

Yang akan kamu lihat: sebuah objek berisi daftar `feed`. Setiap isinya punya `post`, dan di dalam `post` ada `uri`, `record`, `author`, serta angka `likeCount`, `replyCount`, dan `repostCount`.

Titik periksa 1: kamu melihat tulisan `at://did:plc:.../app.bsky.feed.post/...` di bagian `uri`. Kalau muncul, langkah ini berhasil.

Catatan yang penting untuk dicatat di buku: endpoint lain **tidak** semuanya terbuka. Pada hari uji coba, `app.bsky.feed.searchPosts` menolak permintaan tanpa login dengan kode 403, dan `app.bsky.feed.getTimeline` menolak dengan kode 401. Jadi kalau nanti kamu ingin mencari berdasarkan kata kunci, siapkan dulu jalur yang pakai login. Praktik hari ini sengaja memakai endpoint yang pasti terbuka.

---

## 3. Membaca lima field utama (15 menit)

Dari JSON di atas, kenali lima hal ini. Tulis artinya di catatanmu sendiri:

| Field | Arti singkat |
|---|---|
| `uri` | Alamat tetap post, formatnya `at://did:plc:.../app.bsky.feed.post/...` |
| `record.createdAt` | Waktu post dibuat, format UTC |
| `record.text` | Isi tulisan |
| `likeCount` | Jumlah suka saat data diambil |
| `reason` | Muncul hanya kalau post itu reshare, bertipe `reasonRepost` |

Perhatikan yang terakhir. Kalau satu akun membagikan tulisan orang lain, `post` yang muncul tetap milik penulis asli, sedangkan `reason` memberitahu siapa yang membagikan. Di data nyata ini sangat sering terjadi, dan kalau tidak diperhatikan, satu tulisan bisa terhitung berkali-kali. Inilah bentuk duplikat dekat yang dibahas di Materi 6.

---

## 4. Menjalankan kolektor (40 menit)

Letakkan skrip `blsky_collect.py` di folder kerja, lalu jalankan:

```bash
python3 bsky_collect.py --actor bsky.app --limit 150 --outdir hasil
```

Apa yang dilakukan skrip, urut:

1. Meminta 100 post terbaru dari akun, memakai parameter `actor` dan `limit`.
2. Menyimpan setiap post ke `hasil/raw.jsonl` (berkas mentah, satu baris satu post).
3. Kalau masih kurang dari 150 baris, memakai `cursor` sebagai penanda lanjutan.
4. Berhenti kalau cursor sudah kosong.
5. Jeda 1,5 detik antar permintaan agar tidak membebani server.
6. Menulis `hasil/clean.csv`, `hasil/collection_log.md`, dan `hasil/sha256.txt`.

Titik periksa 2: muncul tiga baris keluaran berisi jumlah baris, jumlah halaman, dan tiga nama berkas. Hasil uji kami: 150 baris dari 2 halaman.

Kalau muncul galat, buka tabel di bagian 8.

---

## 5. Membaca hasil dan menemukan sesuatu (30 menit)

Buka isi `hasil/clean.csv`. Kolomnya: `uri`, `created_at`, `text`, `like_count`, `reply_count`, `repost_count`, `author_handle`, `is_reshare`, `reshared_by`, `captured_at`.

Hitung cepat dengan tiga perintah:

```bash
wc -l hasil/clean.csv
cut -d',' -f8 hasil/clean.csv | sort | uniq -c
cut -d',' -f7 hasil/clean.csv | sort | uniq -c | sort -rn | head -5
```

Hasil uji kami pada akun `bsky.app`, limit 150: 150 baris, 68 baris bertanda `iya` (reshare) dan 82 baris tulisan asli. Penulis aslinya beragam, 57 nama berbeda.

Nah, inilah latihan berpikir. Tulis satu paragraf jawaban untuk pertanyaan ini: **kalau kamu mau mengetahui "apa yang sedang dibicarakan Bluesky hari ini", apakah 150 baris dari satu akun ini cukup? Mengapa, dan apa batas jujur yang harus kamu sebut di laporan?**

Jawaban yang baik menyebut setidaknya: satu akun bukan komunitas, sebagian besar konten adalah reshare, jadi tulisan asli yang baru hanya 82 baris, dan periodenya hanya selang sehari.

---

## 6. Bermain dengan potongan diam-diam (20 menit)

Sekarang coba akun yang lamanya tidak aktif:

```bash
python3 bsky_collect.py --actor detikcom.bsky.social --limit 150 --outdir hasil-detik
```

Hasil uji kami: hanya **2 baris** dari 1 halaman, tanpa cursor. Artinya feed akun itu sudah habis, dan kolektor berhenti dengan benar.

Bandingkan dengan `collection_log.md` di kedua folder. Di `hasil`, halaman terakhir berisi 99 item. Di `hasil-detik`, halaman terakhir berisi 2 item. Inilah sinyal **potongan diam-diam**: bila halaman terakhir jauh lebih sedikit dari 100 padahal seharusnya masih ada lanjutan, berarti ada yang terpotong. Mengetahuinya membuat caramu menulis laporan jauh lebih jujur.

Titik periksa 3: kamu bisa menyebutkan beda kedua log itu dengan satu kalimat.

---

## 7. Mengerjakan log dan checksum (20 menit)

Buka `hasil/collection_log.md` dan `hasil/sha256.txt`. Kamu akan melihat isinya sudah terisi otomatis: endpoint, aktor, waktu selesai dalam UTC, jumlah halaman, jumlah baris, jeda permintaan, rincian tiap halaman, dan dua hash SHA-256.

Tugasmu sekarang: lengkapi log itu dengan dua baris tulisan tanganmu sendiri:

1. Satu kalimat batasan: apa yang data ini tidak bisa jawab.
2. Satu kalimat keputusan: apakah 150 baris ini cukup untuk pertanyaanmu, atau perlu dilanjutkan besok.

Titik periksa 4: logmu memuat angka halaman, angka baris, dua hash, dan dua kalimat tulisannya. Format ini dipakai lagi di tugas mandiri.

---

## 8. Tabel galat yang mungkin muncul

| Galat | Arti | Yang dilakukan |
|---|---|---|
| HTTP 400 dari getAuthorFeed | Handle akun salah atau akun tidak ada | Periksa ejaan handle setelah `@` di profil |
| HTTP 403 dari searchPosts | Endpoint itu butuh login | Pakai endpoint publik lain, atau siapkan jalur login |
| HTTP 401 dari getTimeline | Endpoint itu khusus pengguna login | Sama seperti di atas |
| HTTP 429 | Kecepatan permintaan terlalu tinggi | Skrip menunggu lebih lama otomatis; tetap jalankan |
| Tidak bisa membuka berkas skrip di SD | Android menolak jalankan dari kartu SD | Salin skrip ke folder HP dulu |
| Baris `text` kosong | Post berupa gambar atau tautan saja | Biarkan, lalu tandai di laporan |

---

## 9. Aturan yang tidak boleh dilanggar

1. **Hanya data publik.** Akun dan daftar yang terkunci tidak disentuh.
2. **Tidak menyamar.** Tidak perlu login di praktik ini, jadi tidak ada alasan memakai akun orang lain.
3. **Ramah ke server.** Jeda antara permintaan dibiarkan ada. Jangan dihapus agar "lebih cepat".
4. **Berkas mentah tidak diubah.** Semua perbaikan ditulis ke berkas baru.
5. **Log ditulis saat masih ingat, bukan minggu depan.**

---

## 10. Tugas setelah praktik

Untuk mata kuliah ini, kamu akan memakai alat yang sama pada tugas mandiri.

| Waktu | Tugas |
|---|---|
| Minggu ini | Ulangi praktik untuk tiga akun yang berkaitan dengan topikmu, masing-masing 150 baris |
| Pekan depan | Gabungkan ketiganya, buang baris reshare, lalu tulis tiga temuan dengan bukti angka |
| Saat UTS | Log praktik ini menjadi contoh kalau ada soal tentang jalan data |

Titipan kecil dari pengalaman praktik hari ini: yang membuat laporan terasa dewasa bukan jumlah barisnya, tapi kalimat yang menyebutkan apa yang datanya **tidak** bisa jawab.

---

## 11. Tugas tambahan bagi yang sudah selesai lebih cepat

Untuk melihat data mengalir secara nyaris tanpa saringan, ada Jetstream, aliran resmi Bluesky dalam bentuk websocket. Jalankan:

```bash
pip install websocket-client
python3 - << "PYEOF"
import json, websocket
ws = websocket.create_connection(
    "wss://jetstream1.us-east.bsky.network/subscribe?wantedCollections=app.bsky.feed.post")
n = 0
while n < 5:
    data = json.loads(ws.recv())
    print(data.get("did"), "|", data.get("kind"), "|",
          data.get("commit", {}).get("record", {}).get("text", "")[:40])
    n += 1
ws.close()
PYEOF
```

Urutan perintah di atas sudah diuji balasannya pada hari uji coba. Kalimat yang muncul adalah isi post pengguna yang tadi dibuat di seluruh dunia.

Peringatan ukuran: Jetstream sangat deras. Untuk praktik kelas, batasi dengan `limit` atau hentikan setelah beberapa ratus baris. Kegunaannya di mata kuliah ini adalah memahami maksud "firehose terbuka", bukan untuk mengumpulkan sebanyak mungkin.

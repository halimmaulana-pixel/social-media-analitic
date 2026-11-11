# RPS Action-Oriented — Social Media Analytics (14 Pertemuan)

**Prinsip desain:** kerjakan dulu, teori menyusul. Setiap pertemuan dibuka dengan satu artefak nyata (post, dataset, dashboard), mahasiswa mengerjakan di lab, konsep dibangun di atas hasil kerja (flipped/inquiry). Cakupan CPMK & bobot penilaian sama dengan RPS standar (`rps-14-pertemuan.md`), hanya urutan pengalaman belajar yang dibalik.

## Peta 14 Pertemuan — versi Action & Contoh

| Mg | Judul aksi | Contoh kasus (Indonesia) | Aksi lab utama | Luaran dinilai |
|----|------------|--------------------------|----------------|----------------|
| 1 | "3 juta view itu bagus atau buruk?" | Video viral UMKM snack di TikTok | Bedah 1 dashboard vs 1 data mentah; tulis rencana analisis untuk 1 isu asli | Rencana analisis 2 hal. |
| 2 | Ambil topik yang sama dari 3 platform | Isu kenaikan harga BBM / tagar tren #Pemilu2024 | Kumpulkan 1.000 post di X (atau Bluesky), Reddit, YouTube → tabel field tersedia | Memo komparabilitas 1 hal. |
| 3 | Bongkar 1 objek data | 1 post X + 1 video TikTok + 1 komentar YouTube | Inspeksi JSON mentah, daftar semua field + arti + missingness | Kamus field platform |
| 4 | Bangun collector kecil | Arsip topik banjir Jakarta 7 hari | Coding 3 API: pagination, rate limit, query operator, checksum | Dataset + collection log |
| 5 | "Budget nol, butuh data" | Analisis komentar IG brand UMKM; kebutuhan data Meta/X | Tulis feasibility memo: jalur akses, biaya, ToS, UU PDP | Feasibility/legal-ethics memo |
| 6 | Bersihkan data bagian sendiri | Komentar code-mixing Jawa–Indonesia, emoji, slang "bjb/gws" | Pipeline cleaning + lapor before/after; filter bot; deteksi bahasa | Dataset bersih + laporan |
| 7 | **UTS action** | Pasang laporan analis fiktif yang salah (5 kesalahan diselipkan) | Temukan & tulis koreksi tiap kesalahan; jawab kasus singkat | Ujian terstruktur |
| 8 | Bake-off word metrics | Komentar TikTok produk skincare lokal | TF-IDF/RAKE/lexicon InSet; tabel metrik; pilih baseline | Notebook baseline |
| 9 | Sentimen vs emosi | Brand minuman viral terkontroversi di X vs TikTok | Latih 3 model (lexicon→SVM→BERT); ABSA rasa/harga; error analysis | Laporan metrik + kesalahan |
| 10 | Silang-uji model Indonesia | Slang Jakarta, Jawa, code-mixing; dataset SmSA | IndoBERT vs multilingual; error analysis 50 sampel | Laporan error analysis |
| 11 | Peta topik diskursus | Isu RUU kontroversial / tagar solidaritas internasional | LDA vs BERTopic, coherence, validasi manual 30 dokumen | Topik tervalidasi |
| 12 | Siapa jembatan antar-kubu | Reply/mention di konflik opini politik 2024 | Graf networkx, centrality, Louvain; interpretasi substantif | Graf + interpretasi |
| 13 | Label otom yang harus dibuktikan | Berita kesehatan/hoaks; kelas "hoax vs valid" | Codebook→prompt LLM; gold set 200; κ gate; demo agent harian + audit; retention curve video pendek | Gold set + laporan κ + demo |
| 14 | **UAS + capstone** | Satu isu nyata dipilih tim: pemilu, hoax, brand, short-video campaign | Presentasi end-to-end + dashboard 2 view (jaringan + temporal) + ethics note | UAS 30% + capstone 35% + ethics 10% |

## Pola menit per pertemuan (150 menit)

- **Opening artifact (20')** — tampilkan artefak nyata (post viral, dashboard, dataset rusak); mahasiswa mendiagnosis sebelum teori.
- **Aksi lab (90')** — kerjakan di lab dengan template starter (script/colab/notebook).
- **Debrief konsep (30')** — dosen menamai konsep yang muncul dari hasil kerja; hubungkan ke literatur.
- **Bridge tugas (10')** — tugas mingguan menuntaskan apa yang belum selesai di lab.

## Jejak capstone (jaringan tugas terhubung)

Data P2→P4 → bersih P6 → baseline P8 → model P9–P11 → analisis jaringan P12 → label LLM tervalidasi P13 → dashboard & presentasi P14. Setiap luaran mingguan adalah komponen capstone; tidak ada tugas sekali-pakai.

## Catatan risiko desain action-first

1. Konsep formal (sampling bias, κ, distribusi) datang lebih lambat — mit: debrief konsep wajib; pre-read teks 2 halaman tiap minggu.
2. Ketergantungan akses API siaga saat lab — mit: arsip dataset cadangan lokal tiap topik (studi kasus tetap jalan tanpa jaringan).
3. Kelompok lambat tertinggal — mit: rubrik ketuntasan minimum per lab + pasangan peer-review.

## Penilaian (tidak berubah dari RPS standar)

| Komponen | Bobot |
|---|---|
| UTS (P7, berbentuk studi kasus) | 20% |
| UAS tertulis (P14) | 30% |
| Tugas/lab mingguan (12 tugas) | 35% |
| Capstone (presentasi P14) | 15% |

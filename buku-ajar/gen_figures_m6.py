# Generator 7 ilustrasi untuk Buku Ajar Materi 6 (Preprocessing).
# Gaya visual sama dengan materi 1-5: SVG ringan, teks Indonesia, tanpa em dash.
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)

INK = "#1e293b"
BLUE = "#2563eb"
BLUE_L = "#dbeafe"
GREEN = "#059669"
GREEN_L = "#d1fae5"
RED = "#dc2626"
RED_L = "#fee2e2"
AMBER = "#d97706"
AMBER_L = "#fef3c7"
GRID = "#cbd5e1"
PAPER = "#ffffff"


def svg(w, h, body, label):
    return ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' "
            "width='%d' height='%d' role='img' aria-label='%s'>%s</svg>"
            % (w, h, w, h, label, body))


def rect(x, y, w, h, fill, stroke, rx=8, sw=1.2, dash=""):
    d = " stroke-dasharray='%s'" % dash if dash else ""
    return ("<rect x='%d' y='%d' width='%d' height='%d' rx='%d' fill='%s' "
            "stroke='%s' stroke-width='%.1f'%s/>" % (x, y, w, h, rx, fill, stroke, sw, d))


def text(x, y, s, size=14, fill=INK, anchor="start", weight="normal", family="Georgia, serif"):
    return ("<text x='%d' y='%d' font-family='%s' font-size='%d' fill='%s' "
            "text-anchor='%s' font-weight='%s'>%s</text>"
            % (x, y, family, size, fill, anchor, weight, esc(s)))


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def arrow(x1, y1, x2, y2, color=GRID, sw=1.6, dash=""):
    d = " stroke-dasharray='5,4'" % () if dash else ""
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    L = 9
    p1 = (x2 - L * math.cos(ang - 0.42), y2 - L * math.sin(ang - 0.42))
    p2 = (x2 - L * math.cos(ang + 0.42), y2 - L * math.sin(ang + 0.42))
    return ("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='%.1f'%s/>"
            "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' fill='%s'/>"
            % (x1, y1, x2, y2, color, sw, d, x2, y2, p1[0], p1[1], p2[0], p2[1], color))


def save(name, s):
    open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8").write(s)
    print("written", name + ".svg", len(s), "bytes")


# ---------------------------------------------------------------- fig 1 pipeline
def fig_pipeline():
    W, H = 980, 250
    b = [rect(0, 0, W, H, PAPER, GRID, 0)]
    stages = [
        ("1. Cek integritas", "parse JSON, hitung baris, field hilang", "lolos kalau parse error 0"),
        ("2. Deduplikasi", "MinHash + rantai reshare", "tandai, jangan hapus opini baru"),
        ("3. Saring bot", "6 heuristik, skor 0-1", "di bawah 0.5 lanjut, sisanya audit"),
        ("4. Normalisasi", "slang, emoji, huruf panjang", "negasi dan entitas jangan hilang"),
        ("5. Deteksi bahasa", "fastText/CLD per kalimat", "campur kode tetap diproses"),
        ("6. Tokenisasi", "kata dasar, hashtag dipecah", "token mewakili unit makna"),
        ("7. Quality gate", "cek ulang sampel 5 persen", "catat angka sebelum/sesudah"),
    ]
    x = 18
    bw, gap = 128, 12
    for i, (t, d, g) in enumerate(stages):
        fill = BLUE_L if i % 2 == 0 else "#eff6ff"
        b.append(rect(x, 60, bw, 74, fill, BLUE))
        b.append(text(x + bw / 2, 82, t, 12.5, INK, "middle", "bold"))
        words = d.split()
        line = ""
        y = 98
        for w in words:
            if len(line) + len(w) > 18:
                b.append(text(x + bw / 2, y, line, 10.5, "#475569", "middle"))
                line = w
                y += 13
            else:
                line = (line + " " + w).strip()
        if line:
            b.append(text(x + bw / 2, y, line, 10.5, "#475569", "middle"))
        b.append(text(x + bw / 2, 148, g, 9.5, GREEN, "middle"))
        if i < len(stages) - 1:
            b.append(arrow(x + bw + 1, 97, x + bw + gap - 2, 97, BLUE))
        x += bw + gap
    b.append(text(W / 2, 28, "Peta jalan preprocessing: tujuh tahap berurutan, tiap tahap punya gate", 15, INK, "middle", "bold"))
    b.append(text(W / 2, 46, "Urutan penting: normalisasi teks dijalankan setelah data bersih dari duplikat dan akun bot", 11, "#475569", "middle"))
    b.append(text(18, 190, "Bacaan: setiap kotak menyatakan satu tahap. Baris hijau adalah syarat lanjut sebelum tahap berikutnya dijalankan.", 11, "#475569"))
    b.append(text(18, 208, "Prinsip: semua keputusan tahap ini dicatat dalam cleaning log, lengkap dengan angka sebelum dan sesudah.", 11, "#475569"))
    save("figm6-pipeline", svg(W, H, "".join(b), "Peta jalan preprocessing tujuh tahap dengan gate"))


# ---------------------------------------------------------------- fig 2 minhash
def fig_minhash():
    W, H = 980, 330
    b = [rect(0, 0, W, H, PAPER, GRID, 0)]
    b.append(text(W / 2, 26, "Dedup dekat: dua tweet yang mirip 71 persen, apakah opini yang sama?", 15, INK, "middle", "bold"))
    b.append(text(30, 58, "Tweet A (asli):", 12, BLUE, "start", "bold"))
    b.append(text(140, 58, "Pemda lamban tangani banjir, warga sampai mengungsi ke masjid", 12.5, INK))
    b.append(text(30, 84, "Tweet B (reshare):", 12, BLUE, "start", "bold"))
    b.append(text(140, 84, "Pemda lamban tangani banjir, warga terpaksa mengungsi ke masjid Agung", 12.5, INK))
    b.append(text(30, 112, "Shingle 3 kata:", 12, "#475569", "start", "bold"))
    sh_a = ["pemda lamban tangani", "lamban tangani banjir", "tangani banjir warga", "banjir warga sampai",
            "warga sampai mengungsi", "sampai mengungsi ke", "mengungsi ke masjid"]
    sh_b = ["pemda lamban tangani", "lamban tangani banjir", "tangani banjir warga", "banjir warga terpaksa",
            "warga terpaksa mengungsi", "terpaksa mengungsi ke", "mengungsi ke masjid agung"]
    y = 138
    for i in range(7):
        same = sh_a[i] == sh_b[i]
        col = GREEN_L if same else RED_L
        st = GREEN if same else RED
        b.append(rect(30, y - 13, 300, 20, col, st, 4))
        b.append(text(38, y + 1, sh_a[i], 10.5, INK))
        b.append(rect(350, y - 13, 330, 20, col, st, 4))
        b.append(text(358, y + 1, sh_b[i], 10.5, INK))
        b.append(text(700, y + 1, "sama" if same else "beda", 10.5, st, "start", "bold"))
        y += 24
    b.append(text(30, y + 12, "MinHash memperkirakan kemiripan dari potongan 3 kata yang bertumpang tindih.", 11, "#475569"))
    b.append(text(30, y + 30, "LSH mencari pasangan yang layak diperiksa, sehingga 500 ribu tweet tidak perlu dibandingkan satu per satu.", 11, "#475569"))
    b.append(rect(30, y + 48, 900, 58, AMBER_L, AMBER, 6))
    b.append(text(44, y + 68, "Keputusan: 5 dari 7 potongan sama, skor 0,71 di atas ambang 0,60, keduanya ditandai duplikat.", 11.5, INK))
    b.append(text(44, y + 92, "Catatan: jika Tweet B menambahkan klaim baru (video, lokasi baru), ia bukan duplikat. Tanda, lalu periksa isi sebelum membuang.", 11, "#475569"))
    save("figm6-minhash", svg(W, H, "".join(b), "Contoh dedup dekat dengan shingle tiga kata dan skor kemiripan"))


# ---------------------------------------------------------------- fig 3 bot
def fig_bot():
    W, H = 980, 300
    b = [rect(0, 0, W, H, PAPER, GRID, 0)]
    b.append(text(W / 2, 26, "Enam heuristik bot, disatukan menjadi satu skor contoh", 15, INK, "middle", "bold"))
    rows = [
        ("Frekuensi post per hari", "rata-rata akun organik 3-8", "akun A 412"),
        ("Rasio like per post", "akun organik punya variasi", "akun A selalu 0"),
        ("Usia akun saat aktif pertama", "akun tua lalu diam, lalu ramai lagi", "akun A lahir 2 minggu lalu"),
        ("Pola jam post", "manusia punya jam tidur", "akun A post 24 jam nonstop"),
        ("Kemiripan teks antar post", "manusia menulis berbeda", "akun A 96 persen salinan"),
        ("Perilaku jaringan", "mengikuti banyak akun serentak", "akun A ikut 1.200 akun sehari"),
    ]
    y = 62
    for name, human, akun in rows:
        b.append(rect(30, y - 18, 340, 26, "#f1f5f9", GRID, 6))
        b.append(text(42, y, name, 11.5, INK, "start", "bold"))
        b.append(rect(390, y - 18, 250, 26, GREEN_L, GREEN, 6))
        b.append(text(400, y, human, 10.5, INK))
        b.append(rect(660, y - 18, 270, 26, RED_L, RED, 6))
        b.append(text(670, y, akun, 10.5, INK))
        y += 34
    b.append(text(390, y - 40, "pola manusia", 10, GREEN, "start", "bold"))
    b.append(text(660, y - 40, "contoh akun A", 10, RED, "start", "bold"))
    b.append(rect(30, y + 6, 440, 54, BLUE_L, BLUE, 8))
    b.append(text(44, y + 30, "Skor akun A = 0,82 (enam heuristik bobot sama)", 12.5, INK, "start", "bold"))
    b.append(text(44, y + 50, "di atas ambang 0,50: disaring dari analisis sentimen", 11, "#475569"))
    b.append(rect(510, y + 6, 420, 54, GREEN_L, GREEN, 8))
    b.append(text(524, y + 30, "Skor akun B = 0,21", 12.5, INK, "start", "bold"))
    b.append(text(524, y + 50, "di bawah ambang: dipakai, kontennya dibaca biasanya", 11, "#475569"))
    b.append(text(30, y + 82, "Ambang 0,50 adalah contoh kelas, bukan baku industri. Setiap riset wajib kalibrasi dan mengaudit 5 persen sampel manual.", 10.5, "#475569"))
    save("figm6-bot", svg(W, H, "".join(b), "Enam heuristik bot dan contoh perhitungan skor dua akun"))


# ---------------------------------------------------------------- fig 4 normalize
def fig_normalize():
    W, H = 980, 400
    b = [rect(0, 0, W, H, PAPER, GRID, 0)]
    b.append(text(W / 2, 26, "Contoh nyata: satu baris komentar marketplace, enam langkah jadi token bersih", 15, INK, "middle", "bold"))
    b.append(text(30, 56, "Mentah: barangnya bagus bjrr, pengiriman cepat, tapi packing'e abis bangkeett 💔 Recommended deh!! @TokoA #belanjakan #murah", 12, INK, "start", "italic"))
    steps = [
        ("1. Pisah elemen non-teks", "hapus @mention, pisahkan #tagar, emoji ditandai token EMI_PLOSI", "barangnya bagus bjr pengiriman cepat tapi packinge abis bangkeett EMI_PLOSI Recommended deh TAGAR_BELANJAKAN TAGAR_MURAH"),
        ("2. Rapikan huruf panjang", "bangkeett menjadi banget (aturan: huruf berulang lebih dari dua kali dipangkas)", "barangnya bagus bjrr pengiriman cepat tapi packinge abis banget EMI_PLOSI Recommended deh ..."),
        ("3. Ganti slang lewat kamus", "bjb jadi bagus, bjrr jadi bagus banget, deh jadi partikel, tuh dipertahankan bila menunjuk", "barangnya bagus bagus banget pengiriman cepat tapi packing china abis banget ..."),
        ("4. Pecah tagar majemuk", "#belanjakan menjadi belanja akan, #murah tetap murah", "TAGAR_BELANJAKAN -> token belanja, akan"),
        ("5. Beri tanda negasi", "tapi membuka klausa negatif, packinge abis dikontraskan dengan bagus", "flag NEGASI aktif sampai tanda baca berikutnya"),
        ("6. Simpan bentuk asli", "kolom teks_mentah tak pernah dihapus, hanya kolom teks_bersih yang berubah", "audit dapat dibuka kembali kapan saja"),
    ]
    y = 84
    for t, d, out in steps:
        b.append(rect(30, y - 16, 250, 46, BLUE_L, BLUE, 6))
        b.append(text(42, y, t, 11, INK, "start", "bold"))
        b.append(rect(292, y - 16, 250, 46, "#f1f5f9", GRID, 6))
        words = d.split()
        line = ""
        yy = y
        for w in words:
            if len(line) + len(w) > 30:
                b.append(text(302, yy, line, 9.8, "#475569"))
                line = w
                yy += 12
            else:
                line = (line + " " + w).strip()
        if line:
            b.append(text(302, yy, line, 9.8, "#475569"))
        b.append(rect(556, y - 16, 394, 46, GREEN_L, GREEN, 6))
        words = out.split()
        line = ""
        yy = y
        for w in words:
            if len(line) + len(w) > 46:
                b.append(text(566, yy, line, 9.8, INK))
                line = w
                yy += 12
            else:
                line = (line + " " + w).strip()
        if line:
            b.append(text(566, yy, line, 9.8, INK))
        arrow(20, y + 7, 27, y + 7, BLUE)
        y += 52
    b.append(text(30, y + 8, "Hasil akhir: [barangnya] [bagus] [bagus] [banget] [pengiriman] [cepat] [NEGASI] [packing] [china] [abis] [banget] [EMI_PLOSI] [TAGAR_BELANJAKAN]", 10.5, INK))
    b.append(text(30, y + 26, "Tanda NEGASI penting untuk langkah selanjutnya. Model sentimen di pertemuan 9 membaca penanda ini agar tidak salah simpul.", 10.5, "#475569"))
    save("figm6-normalize", svg(W, H, "".join(b), "Worked example normalisasi komentar marketplace enam langkah"))


# ---------------------------------------------------------------- fig 5 overclean
def fig_overclean():
    W, H = 980, 300
    b = [rect(0, 0, W, H, PAPER, GRID, 0)]
    b.append(text(W / 2, 26, "Jebakan membersihkan berlebihan: stopword naif membalik makna", 15, INK, "middle", "bold"))
    b.append(text(30, 60, "Kalimat asli:", 12, "#475569", "start", "bold"))
    b.append(text(140, 60, "Kualitas tidak bagus untuk harga segitu", 12.5, INK))
    b.append(text(30, 92, "Jalur salah (stopword umum Indonesia memuat kata 'tidak'):", 11.5, RED, "start", "bold"))
    b.append(rect(30, 104, 430, 100, RED_L, RED, 8))
    b.append(text(44, 128, "tidak dihapus -> tersisa: kualitas bagus untuk harga segitu", 11, INK))
    b.append(text(44, 148, "pembaca mesin menyimpulkan POSITIF", 11, RED, "start", "bold"))
    b.append(text(44, 168, "padahal ulasan asli NEGATIF", 11, RED))
    b.append(text(44, 192, "kesalahan ini lolos karena tidak ada manusia memeriksa sampel", 10.5, "#475569"))
    b.append(text(510, 92, "Jalur benar:", 11.5, GREEN, "start", "bold"))
    b.append(rect(510, 104, 440, 100, GREEN_L, GREEN, 8))
    b.append(text(524, 128, "kata negasi dipakai ulang sebagai penanda NEGASI", 11, INK))
    b.append(text(524, 148, "tersisa: kualitas NEGASI bagus untuk harga segitu", 11, INK))
    b.append(text(524, 168, "model membaca: ulasan NEGATIF", 11, GREEN, "start", "bold"))
    b.append(text(524, 192, "stopword khusus analisis dikompilasi, bukan kamus serbaguna", 10.5, "#475569"))
    b.append(rect(30, 224, 920, 56, AMBER_L, AMBER, 8))
    b.append(text(44, 246, "Aturan praktis: sebelum menghapus kata apa pun dari daftar, tanyakan apakah kata itu mengubah arah kalimat.", 11, INK))
    b.append(text(44, 268, "Yang mengubah arah (tidak, belum, jarang, malah) disimpan. Yang hanya mengganjal (yang, di, ke) boleh dihapus.", 11, "#475569"))
    save("figm6-overclean", svg(W, H, "".join(b), "Contoh over-cleaning pada kalimat negatif dan jalur perbaikan"))


# ---------------------------------------------------------------- fig 6 window
def fig_window():
    W, H = 980, 300
    b = [rect(0, 0, W, H, PAPER, GRID, 0)]
    b.append(text(W / 2, 26, "Satu pertanyaan, dua jendela waktu, dua cerita berbeda", 15, INK, "middle", "bold"))
    b.append(text(30, 58, "Pertanyaan: seberapa ramai warga membicarakan banjir pada minggu pertama Januari?", 11.5, "#475569"))
    for j, (label, desc, bars, col, note) in enumerate([
        ("Jendela A: exactly 7 hari sesuai parameter", "pagination dihentikan saat cursor habis",
         [40, 55, 90, 130, 120, 60, 45], BLUE, "cacat: siklus harian terputus bila halaman terakhir habis"),
        ("Jendela B: 24 jam pertama + sampling 10 persen", "kuota habis di tengah, sampling dipakai",
         [80, 30, 20, 15, 10, 8, 6], AMBER, "cacat: memotong puncak membicarakan, volume tampak kecil"),
    ]):
        x0 = 30 + j * 470
        b.append(text(x0, 92, label, 11.5, INK, "start", "bold"))
        b.append(text(x0, 110, desc, 10.5, "#475569"))
        by = 250
        bw = 42
        for i, v in enumerate(bars):
            h = v * 1.1
            b.append(rect(x0 + 20 + i * (bw + 10), by - h, bw, h, col, col))
            b.append(text(x0 + 20 + i * (bw + 10) + bw / 2, by - h - 5, str(v), 9.5, INK, "middle"))
        for i in range(7):
            b.append(text(x0 + 20 + i * (bw + 10) + bw / 2, 268, "H%d" % (i + 1), 9.5, "#475569", "middle"))
        b.append(rect(x0, 282, 440, 1, GRID, GRID))
        b.append(text(x0, 296, note, 10, "#475569"))
    b.append(text(30, 22, "Volume per hari untuk tagar yang sama", 11, "#475569"))
    save("figm6-window", svg(W, H, "".join(b), "Perbandingan dua jendela waktu API dan efek volume"))


# ---------------------------------------------------------------- fig 7 funnel
def fig_funnel():
    W, H = 980, 340
    b = [rect(0, 0, W, H, PAPER, GRID, 0)]
    b.append(text(W / 2, 26, "Funnel lab: 500 baris mentah menjadi 300 baris layak analisis", 15, INK, "middle", "bold"))
    rows = [
        ("Mentah dari kolektor (log lengkap)", 500, "#e2e8f0"),
        ("Cek integritas: 10 baris JSON rusak dibuang", 490, "#eff6ff"),
        ("Dedup dekat: 29 baris tumpang tindih ditandai", 461, "#dbeafe"),
        ("Saring bot: 30 akun skor tinggi dihilangkan", 431, "#bfdbfe"),
        ("Normalisasi: tidak membuang baris, hanya mengubah bentuk", 431, "#93c5fd"),
        ("Quality gate: 19 baris kosong atau teks < 3 token disingkirkan", 412, "#60a5fa"),
        ("Audit manual sampel 5 persen: 14 baris ditandai ragu", 398, "#3b82f6"),
        ("Tahap akhir setelah keputusan ragu dibuka", 300, BLUE),
    ]
    y = 58
    maxw = 720
    for label, n, col in rows:
        w = int(maxw * n / 500)
        b.append(rect(30, y - 14, w, 22, col, BLUE, 4))
        b.append(text(30 + w + 10, y + 2, str(n), 11.5, INK, "start", "bold"))
        b.append(text(30 + maxw + 90, y + 2, label, 10.5, "#475569"))
        y += 32
    b.append(rect(30, y + 8, 920, 54, AMBER_L, AMBER, 8))
    b.append(text(44, y + 30, "Pelajaran angka: setiap tahap menyisakan jejak. Laporan cleaning wajib memuat deret 500, 490, 461, 431, 412, 398, 300", 11, INK))
    b.append(text(44, y + 50, "beserta alasan tiap selisih. Tanpa deret itu, analisis tidak bisa direproduksi oleh peneliti lain.", 11, "#475569"))
    save("figm6-funnel", svg(W, H, "".join(b), "Funnel lab dari 500 baris mentah menjadi 300 baris layak analisis"))


if __name__ == "__main__":
    fig_pipeline()
    fig_minhash()
    fig_bot()
    fig_normalize()
    fig_overclean()
    fig_window()
    fig_funnel()
    print("tujuh figur selesai")

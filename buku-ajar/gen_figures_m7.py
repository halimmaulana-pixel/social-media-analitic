# Generator 2 ilustrasi untuk Buku Ajar Materi 7 (Rangkuman dan Kisi-Kisi UTS).
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)
INK = "#1e293b"; BLUE = "#2563eb"; BLUE_L = "#dbeafe"; GREEN = "#059669"
GREEN_L = "#d1fae5"; RED = "#dc2626"; RED_L = "#fee2e2"; AMBER = "#d97706"
AMBER_L = "#fef3c7"; GRID = "#cbd5e1"; PAPER = "#ffffff"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg(w, h, body, label):
    return ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' "
            "width='%d' height='%d' role='img' aria-label='%s'>%s</svg>"
            % (w, h, w, h, label, body))


def rect(x, y, w, h, fill, stroke, rx=8, sw=1.2):
    return ("<rect x='%d' y='%d' width='%d' height='%d' rx='%d' fill='%s' "
            "stroke='%s' stroke-width='%.1f'/>" % (x, y, w, h, rx, fill, stroke, sw))


def text(x, y, s, size=14, fill=INK, anchor="start", weight="normal"):
    return ("<text x='%d' y='%d' font-family='Georgia, serif' font-size='%d' "
            "fill='%s' text-anchor='%s' font-weight='%s'>%s</text>"
            % (x, y, size, fill, anchor, weight, esc(s)))


def arrow(x1, y1, x2, y2, color=GRID, sw=1.5):
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    L = 9
    p1 = (x2 - L * math.cos(ang - 0.42), y2 - L * math.sin(ang - 0.42))
    p2 = (x2 - L * math.cos(ang + 0.42), y2 - L * math.sin(ang + 0.42))
    return ("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='%.1f'/>"
            "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' fill='%s'/>"
            % (x1, y1, x2, y2, color, sw, x2, y2, p1[0], p1[1], p2[0], p2[1], color))


def save(name, s):
    open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8").write(s)
    print("written", name + ".svg", len(s), "bytes")


def fig_conceptmap():
    W, H = 980, 420
    b = [rect(0, 0, W, H, PAPER, GRID, 0)]
    b.append(text(W / 2, 28, "Peta hubungan enam materi sebelum UTS", 16, INK, "middle", "bold"))
    b.append(text(W / 2, 48, "Bacaan dari kiri atas ke kanan bawah: fondasi, lalu akses, lalu kualitas data", 11.5, "#475569", "middle"))
    nodes = [
        (60, 80, "Materi 1\nFondasi SMA", "siklus data,\nmaturitas analitik,\nunit analisis", BLUE_L, BLUE),
        (300, 80, "Materi 2\nEkosistem", "affordance, feed =\nsampling frame, tangga\nakses 2026", BLUE_L, BLUE),
        (540, 80, "Materi 3\nJenis data", "5 keluarga data,\nfield dictionary,\ngranularitas", BLUE_L, BLUE),
        (540, 210, "Materi 4\nAkuisisi API", "pagination, rate limit,\nchecksum, collection\nlog", GREEN_L, GREEN),
        (300, 210, "Materi 5\nAkses & legalitas", "gated access, scraping,\nUU PDP, GDPR,\nfeasibility memo", GREEN_L, GREEN),
        (60, 210, "Materi 6\nPreprocessing", "dedup, bot heuristik,\nnormalisasi, cleaning\nlog", AMBER_L, AMBER),
        (300, 340, "CPMK-2 teruji: koleksi bersih,\nlapor terdokumentasi, keputusan\njalur data bisa dipertanggungjawabkan", "", "#f1f5f9", GRID),
    ]
    for x, y, title, body, fill, stroke in nodes:
        b.append(rect(x, y, 380, 100, fill, stroke, 10))
        lines = title.split("\n")
        yy = y + 26
        for ln in lines:
            b.append(text(x + 14, yy, ln, 12.5, INK, "start", "bold"))
            yy += 17
        yy += 4
        for ln in body.split("\n"):
            b.append(text(x + 14, yy, ln, 10.5, "#475569"))
            yy += 14
    for (x1, y1, x2, y2) in [(440, 130, 540, 130), (710, 130, 710, 210),
                             (540, 260, 440, 260), (300, 260, 200, 260),
                             (190, 310, 370, 340)]:
        b.append(arrow(x1, y1, x2, y2, BLUE))
    b.append(text(510, 118, "lanjut", 10, BLUE, "middle", "bold"))
    b.append(text(722, 175, "data mentah", 10, BLUE, "start"))
    b.append(text(530, 275, "keputusan jalur", 10, GREEN, "middle", "bold"))
    b.append(text(290, 275, "bersihkan dahulu", 10, AMBER, "middle", "bold"))
    b.append(text(60, 380, "Setiap kotak adalah satu pertemuan. Tiap panah adalah ketergantungan: Materi 4 memakai kamus field dari Materi 3,", 11, "#475569"))
    b.append(text(60, 398, "Materi 6 memakai collection log dari Materi 4, dan Materi 5 menjadi filter sebelum keduanya dijalankan.", 11, "#475569"))
    save("figm7-map", svg(W, H, "".join(b), "Peta hubungan enam materi sebelum UTS"))


def fig_worked():
    W, H = 980, 430
    b = [rect(0, 0, W, H, PAPER, GRID, 0)]
    b.append(text(W / 2, 28, "Contoh soal diagnosis: potongan laporan dengan lima cacat", 15.5, INK, "middle", "bold"))
    snippet = [
        "Bukti: Analisis sentimen atas 12.000 komentar tagar #isudesa dari platform X, diambil",
        "1-7 Januari. Karena seluruh komentar bersifat publik, pengumpulan dinilai etis tanpa",
        "persetujuan tambahan. Angka engagement digabungkan dari tiga metrik platform yang",
        "equivalen. Deduplikasi dilakukan dengan menghapus semua baris bernilai kemiripan",
        "di atas 0,60, dan bot disaring memakai ambang 0,30 agar hasil bersih sempurna.",
    ]
    y = 62
    for ln in snippet:
        b.append("<text x='30' y='%d' font-family='DejaVu Sans Mono, monospace' font-size='12' fill='%s'>%s</text>" % (y, INK, esc(ln)))
        y += 20
    notes = [
        ("Cacat 1 (Materi 2)", "\"opini publik\" dari 12.000 komentar tagar: tagar adalah sampling frame, bukan populasi.", RED_L, RED),
        ("Cacat 2 (Materi 5)", "\"publik berarti etis tanpa persetujuan\": identifikasi data pribadi menurut UU PDP tetap berlaku.", RED_L, RED),
        ("Cacat 3 (Materi 2)", "\"tiga metrik yang dianggap setara\": definisi engagement beda antar platform, wajib normalisasi.", RED_L, RED),
        ("Cacat 4 (Materi 6)", "\"hapus semua di atas 0,60\": duplikat dekat bisa membawa klaim baru, wajib dibaca.", RED_L, RED),
        ("Cacat 5 (Materi 6)", "\"ambang 0,30\": terlalu ketat, akun manusia aktif tersaring, hasil condong netral.", RED_L, RED),
    ]
    y = 178
    for t, d, fill, stroke in notes:
        b.append(rect(30, y - 16, 920, 34, fill, stroke, 6))
        b.append(text(42, y, t, 11, stroke, "start", "bold"))
        b.append(text(190, y, d, 10.5, INK))
        y += 40
    b.append(rect(30, y + 6, 920, 52, AMBER_L, AMBER, 8))
    b.append(text(44, y + 28, "Cara menjawab: tulis nomor cacat, sebut materi asalnya, lalu satu kalimat koreksi.", 11.5, INK))
    b.append(text(44, y + 48, "Contoh jawaban lengkap: \"Cacat 1 dari Materi 2. Tagar adalah sampling frame; klaim tentang opini publik tidak sah.\"", 11, "#475569"))
    save("figm7-worked", svg(W, H, "".join(b), "Contoh soal diagnosis dengan lima cacat bertanda materi asal"))


if __name__ == "__main__":
    fig_conceptmap()
    fig_worked()
    print("dua figur selesai")

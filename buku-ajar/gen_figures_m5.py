#!/usr/bin/env python3
"""Buku Ajar SMA — figur Materi 5 (akses gated, scraping, legalitas)."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "figures")
os.makedirs(OUT, exist_ok=True)

W, H = 940, 430

HEAD = ('<defs>\n'
        '<marker id="ar" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">'
        '<path d="M0,0 L8,4.5 L0,9 Z" fill="#4a5568"/></marker>\n'
        '<marker id="arg" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">'
        '<path d="M0,0 L8,4.5 L0,9 Z" fill="#2f855a"/></marker>\n'
        '<marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">'
        '<path d="M0,0 L8,4.5 L0,9 Z" fill="#c53030"/></marker>\n'
        '</defs>\n'
        '<style>'
        '.t{font-size:16px;fill:#1a202c}'
        '.ts{font-size:13px;fill:#2d3748}'
        '.tx{font-size:11.5px;fill:#4a5568}'
        '.th{font-size:15px;fill:#fff}'
        '</style>\n')


def box(x, y, w, h, fill, stroke=None, rx=8):
    s = stroke if stroke else fill
    return '<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s" stroke="%s" stroke-width="1.4"/>\n' % (x, y, w, h, rx, fill, s)


def title(t, sub):
    return '<text x="30" y="34" class="t" font-weight="700" font-size="19">%s</text>\n' % t \
        + '<text x="30" y="56" class="tx">%s</text>\n' % sub


def arrow(x1, y1, x2, y2, color="#4a5568", marker="ar"):
    return '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.8" marker-end="url(#%s)"/>\n' % (x1, y1, x2, y2, color, marker)


def txt(x, y, s, cls="ts", anchor="start", bold=False, fill=None):
    w = ' font-weight="700"' if bold else ""
    f = ' fill="%s"' % fill if fill else ""
    return '<text x="%d" y="%d" class="%s" text-anchor="%s"%s%s>%s</text>\n' % (x, y, cls, anchor, w, f, s)


def multi(x, y, lines, cls="ts", lh=18, anchor="start", fill=None):
    return "\n".join('<text x="%d" y="%d" class="%s" text-anchor="%s"%s>%s</text>' % (x, y + i * lh, cls, anchor, (' fill="%s"' % fill) if fill else "", s) for i, s in enumerate(lines)) + "\n"


def save(name, body, label):
    doc = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 430" font-family="Segoe UI, Roboto, Helvetica, Arial, sans-serif" role="img" aria-label="%s">\n' % label \
        + HEAD + body + "</svg>\n"
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(doc)
    print("wrote", name, len(doc), "bytes")


def close_note(b, note):
    return b + '<text x="30" y="415" class="tx">%s</text>\n' % note


# ---------------------------------------------------------------- 1. tangga akses
def fig_ladder():
    # urutan atas ke bawah = tertinggi ke terbuka
    steps = [
        ("4", "Enclave berbayar", "Meta Content Library — approval lembaga; biaya kelembagaan (verifikasi per 2026)", "#9b2c2c"),
        ("3", "Research API terdaftar", "TikTok Research API, dsb. — proposal + waktu tunggu; kuota dikendalikan platform", "#c05621"),
        ("2", "API resmi berkuota", "X v2 tier rendah · YouTube Data API v3 · Reddit — registrasi + batas kuota harian", "#2b6cb0"),
        ("1", "Kanal terbuka", "Bluesky (AT Protocol) firehose · data terbuka pemerintah — biaya nol, cakupan terbatas", "#2f855a"),
    ]
    b = title("Tangga akses data media sosial (2026)",
              "Tidack: pendaftaran makin ketat, kuota makin longgar — namun biaya dan tuntutan tahap opsi besar makin tinggi.")
    for n, (num, hd, sub, col) in enumerate(steps):
        y = 96 + n * 80
        x = 60 + (4 - int(num) - 1) * 26  # step 4 paling atas digeser sedikit ke kanan? — gunakan offset tunggal
        b += '<rect x="%d" y="%d" width="78" height="66" fill="%s" rx="6"/>\n' % (x, y, col)
        b += '<text x="%d" y="%d" class="th" font-size="22" text-anchor="middle">%s</text>\n' % (x + 39, y + 40, num)
        b += box(x + 92, y, 520, 66, "#f7fafc", col) \
            + txt(x + 106, y + 27, hd, cls="t", bold=True) \
            + txt(x + 106, y + 47, sub, cls="tx")
    b += box(700, 96, 210, 266, "#fff5f5", "#c53030") \
        + multi(714, 126, ["Semuanya kanal", "RESMI.", "Scraping halaman", "publik bukan anak", "tangga kelima —", "melainkan jalan", "samping dengan", "risiko hukum", "sendiri (Bag. 5)."],
                cls="ts", lh=29)
    b = close_note(b, "Kuota dan biaya bersifat indikatif — verifikasi ulang tiap semester di halaman resmi platform.")
    b = b.replace("Tidack: pendaftaran makin ketat", "Semakin tinggi anak tangga: hak akses lebih luas")
    save("figm5-ladder.svg", b, "figm5 ladder")


# ---------------------------------------------------------------- 2. timeline kebijakan
def fig_timeline():
    b = title("Timeline kebijakan akses akademik 2021–2026",
              "Peta perubahan besar; peristiwa makin baru makin cepat berubah — semua angka wajib diverifikasi ulang.")
    b += '<line x1="60" y1="240" x2="880" y2="240" stroke="#4a5568" stroke-width="2.4" marker-end="url(#ar)"/>\n'
    events = [
        (120, "2021", ["Era API longgar:", "tier akademik gratis", "masih tersedia"], "#2f855a", 1),
        (300, "2023", ["X menghentikan tier", "gratis; Reddit menetapkan", "harga Data API"], "#c05621", -1),
        (490, "2024", ["Meta Content Library", "diumumkan pengganti", "CrowdTangle"], "#c05621", 1),
        (670, "2025-26", ["Biaya enclave dilaporkan", "publik; DSA memata", "keras transparansi Eropa"], "#9b2c2c", -1),
        (828, "2026", ["Peta akses berubah", "zio — cek sumber resmi", "tiap semester"], "#9b2c2c", 1),
    ]
    for x, yr, lines, col, side in events:
        b += '<circle cx="%d" cy="240" r="8" fill="%s"/>\n' % (x, col)
        b += txt(x, 272, yr, cls="t", bold=True, anchor="middle")
        ys = 150 if side > 0 else 88
        for i, line in enumerate(lines):
            b += txt(x, ys + i * 17, line, cls="tx", anchor="middle")
        b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.4"/>\n' % (x, ys + 3 * 17 - 6 if side > 0 else ys + 3 * 17 - 6, x, 234 if side > 0 else 172, col)
    b = close_note(b, "Sumber: dokumentasi resmi tiap platform dan laporan komunitas riset 2021–2026 (indikatif).")
    b = b.replace("memata\nkeras transparansi Eropa", "mendorong transparansi Eropa")
    b = b.replace("zio — cek sumber resmi", "terus — cek sumber resmi")
    save("figm5-timeline.svg", b, "figm5 timeline")


# ---------------------------------------------------------------- 3. pohon keputusan scraping
def fig_scraping():
    b = title("Pohon keputusan: boleh scraping atau tidak?",
              "Empat pertanyaan berurutan — 'terlihat publik' bukan lisensi otomatis.")
    b += box(370, 74, 200, 46, "#2b6cb0") \
        + txt(470, 102, "Data tidak tersedia via API", cls="th", anchor="middle")
    b += arrow(470, 120, 470, 142)

    # Q1 robots.txt
    b += box(360, 142, 220, 44, "#edf2f7", "#4a5568") \
        + txt(470, 169, "1. robots.txt memperbolehkan?", cls="ts", anchor="middle")
    b += arrow(580, 164, 646, 164, "#2f855a", "arg") + txt(606, 156, "ya", cls="ts", anchor="middle", fill="#2f855a")
    b += arrow(360, 164, 296, 164, "#c53030", "arr") + txt(326, 156, "tidak", cls="ts", anchor="middle", fill="#c53030")
    b += box(648, 142, 120, 44, "#f0fff4", "#2f855a") + txt(708, 169, "lanjut cek ToS", cls="ts", anchor="middle", fill="#2f855a")
    b += box(200, 142, 94, 44, "#fff5f5", "#c53030") + txt(247, 169, "BERHENTI", cls="th", anchor="middle", fill="#c53030").replace('class="th"', 'class="ts"')

    # Q2 ToS
    b += arrow(470, 186, 470, 208)
    b += box(360, 208, 220, 44, "#edf2f7", "#4a5568") \
        + txt(470, 235, "2. Ketentuan Layanan mengizinkan?", cls="ts", anchor="middle")
    b += arrow(580, 230, 646, 230, "#2f855a", "arg") + txt(606, 222, "ya", cls="ts", anchor="middle", fill="#2f855a")
    b += arrow(360, 230, 296, 230, "#c53030", "arr") + txt(326, 222, "tidak", cls="ts", anchor="middle", fill="#c53030")
    b += box(648, 208, 120, 44, "#f0fff4", "#2f855a") + txt(708, 235, "cek data pribadi", cls="ts", anchor="middle", fill="#2f855a")
    b += box(200, 208, 94, 44, "#fff5f5", "#c53030") + txt(247, 235, "BERHENTI", cls="ts", anchor="middle", fill="#c53030", bold=True)

    # Q3 data pribadi
    b += arrow(470, 252, 470, 274)
    b += box(360, 274, 220, 44, "#edf2f7", "#4a5568") \
        + txt(470, 301, "3. Isinya bebas data pribadi?", cls="ts", anchor="middle")
    b += arrow(580, 296, 646, 296, "#2f855a", "arg") + txt(606, 288, "ya", cls="ts", anchor="middle", fill="#2f855a")
    b += arrow(360, 296, 296, 296, "#c53030", "arr") + txt(326, 288, "tidak", cls="ts", anchor="middle", fill="#c53030")
    b += box(648, 274, 120, 44, "#f0fff4", "#2f855a") + txt(708, 301, "cek beban situs", cls="ts", anchor="middle", fill="#2f855a")
    b += box(200, 274, 94, 44, "#fff5f5", "#c53030") + txt(247, 301, "Jalur Bag. 6", cls="ts", anchor="middle", fill="#c53030", bold=True)

    # Q4 beban situs
    b += arrow(470, 318, 470, 340)
    b += box(360, 340, 220, 48, "#edf2f7", "#4a5568") \
        + txt(470, 362, "4. Tidak membebani situs?", cls="ts", anchor="middle") \
        + txt(470, 380, "jeda antar request, jam mati, tanpa retry agresif", cls="tx", anchor="middle")
    b += arrow(580, 364, 646, 364, "#2f855a", "arg") + txt(606, 356, "ya", cls="ts", anchor="middle", fill="#2f855a")
    b += arrow(360, 364, 296, 364, "#c53030", "arr") + txt(326, 356, "tidak", cls="ts", anchor="middle", fill="#c53030")
    b += box(648, 340, 120, 48, "#f0fff4", "#2f855a") + txt(708, 366, "BOLEH;", cls="ts", anchor="middle", fill="#2f855a", bold=True) \
        + txt(708, 381, "catat di log", cls="tx", anchor="middle", fill="#2f855a")
    b += box(200, 340, 94, 48, "#fff5f5", "#c53030") + txt(247, 367, "BERHENTI", cls="ts", anchor="middle", fill="#c53030", bold=True)

    b = close_note(b, "Empat 'ya' menjadi satu keputusan: scraping yang boleh; satu saja 'tidak' menghentikan jalurnya.")
    save("figm5-scraping.svg", b, "figm5 scraping")


# ---------------------------------------------------------------- 4. PDP: satu post dua wajah
def fig_pdp():
    b = title("Satu post, dua klaster field — pelindungan data pribadi (UU PDP 27/2022)",
              "Pembeda utamanya adalah 'dapat diidentifikasi', bukan status privasi akun.")
    b += box(30, 84, 430, 296, "#f0fdf4", "#2f855a") \
        + txt(52, 112, "Aman dianalisis & disajikan", cls="t", bold=True, fill="#2f855a")
    rows_a = ["isi teks post (dipublikasikan akun sendiri)", "id post / id media (tanpa identitas akun)",
              "metrik agregat: jumlah suka, replikasi", "waktu posting (UTC)", "label bahasa dari platform",
              "jenis konten: teks / gambar / video"]
    for i, r in enumerate(rows_a):
        yy = 132 + i * 41
        b += box(52, yy, 386, 34, "#ffffff", "#c6f6d5", 6) + txt(66, yy + 22, r, cls="ts")
    b += box(480, 84, 430, 296, "#fff5f5", "#c53030") \
        + txt(502, 112, "Perlu mitigasi / tidak dibagikan", cls="t", bold=True, fill="#c53030")
    rows_b = ["nama tampilan + user_id akun", "foto profil wajah (data biometrik)",
              "bio: pekerjaan, kota presisi, sekolah", "kontak yang dipaparkan di bio",
              "jaringan follower/following yang memetakan", "ka-29 karakteristik minoritas lainnya"]
    for i, r in enumerate(rows_b):
        yy = 132 + i * 41
        b += box(502, yy, 386, 34, "#ffffff", "#fed7d7", 6) + txt(516, yy + 22, r, cls="ts")
    b = close_note(b, "Anonimisasi bukan menghapus nama saja: kombinasi field kecil pun dapat mengembalikan identitas (re-identification).")
    b = b.replace("ka-29 karakteristik minoritas lainnya", "label kategori sensitif lainnya")
    save("figm5-pdp.svg", b, "figm5 pdp")


# ---------------------------------------------------------------- 5. publik != boleh
def fig_ethics():
    b = title("Publik \u2260 boleh — tiga lingkar izin yang mengecil",
              "Terlihat publik, boleh dianalisis, boleh dibagikan: tiga persetujuan berbeda dengan syarat masing-masing.")
    cx = 480
    b += '<circle cx="%d" cy="228" r="150" fill="#eff6ff" stroke="#2b6cb0" stroke-width="2"/>\n' % cx
    b += '<circle cx="%d" cy="252" r="104" fill="#fefcbf" stroke="#b7791f" stroke-width="2"/>\n' % cx
    b += '<circle cx="%d" cy="276" r="58" fill="#e6fffa" stroke="#2c7a7b" stroke-width="2"/>\n' % cx
    b += txt(cx, 96, "TERLIHAT PUBLIK", cls="t", bold=True, anchor="middle", fill="#2b6cb0") \
        + txt(cx, 114, "semua yang bisa dibaca siapa pun di halaman terbuka", cls="tx", anchor="middle", fill="#2b6cb0") \
        + txt(cx, 196, "BOLEH DIANALISIS", cls="t", bold=True, anchor="middle", fill="#b7791f") \
        + txt(cx, 214, "persetujuan etik + penghargaan post yang telah dihapus", cls="tx", anchor="middle", fill="#b7791f") \
        + txt(cx, 282, "BOLEH DIBAGIKAN", cls="t", bold=True, anchor="middle", fill="#2c7a7b") \
        + txt(cx, 300, "anonimisasi agresif; dataset dibagikan dengan rubrik", cls="tx", anchor="middle", fill="#2c7a7b")
    b += box(30, 360, 880, 40, "#fff5f5", "#c53030") \
        + txt(52, 385, "Melanggar lingkar: menganalisis dari data publik lalu membagikannya utuh beserta identitas akun — pelanggaran hukum dan etika sekaligus.", cls="ts", fill="#c53030")
    b = close_note(b, "Izin analisis dan izin publikasi adalah dua surat yang berbeda.")
    save("figm5-ethics.svg", b, "figm5 ethics")


# ---------------------------------------------------------------- 6. memo 6 blok
def fig_memo():
    b = title("Feasibility memo: enam blok keputusan",
              "Memo satu halaman; urutan blok memaksa pertimbangan yang tidak terlewat.")
    blocks = [
        ("1", "Pertanyaan riset & unit analisis", "topik apa, forum apa, unitnya post / akun / forum", "#2b6cb0"),
        ("2", "Kandidat jalur data (minimal 3)", "API kuota · Research API · enclave · scraping terbuka · dataset publik", "#c05621"),
        ("3", "Keputusan & alasan", "jalur utama yang dipilih; jalur cadangan yang ditunda beserta alasannya", "#2b6cb0"),
        ("4", "Biaya & risiko", "kuota harian, harga tier, waktu tunggu approval", "#c05621"),
        ("5", "Mitigasi & jadwal", "buffer 25%, fallback Buffer Block, jam cadangan di lab", "#2b6cb0"),
        ("6", "Rujukan hukum & etik", "kebijakan platform, UU PDP, ToS, dan ethika akademik kampus", "#c05621"),
    ]
    for i, (n, hd, sub, col) in enumerate(blocks):
        yy = 84 + i * 52
        b += box(60, yy, 820, 42, "#f7fafc", col) \
            + '<rect x="60" y="%d" width="46" height="42" fill="%s" rx="6"/>\n' % (yy, col) \
            + txt(83, yy + 29, n, cls="th", anchor="middle", bold=True) \
            + txt(118, yy + 18, hd, cls="t", bold=True) \
            + txt(118, yy + 37, sub, cls="tx")
    b = close_note(b, "Memo ditulis sebelum koleksi berjalan — bukan catatan mundur-mundur setelah data terkumpul.")
    b = b.replace("fallback Buffer Block, jam cadangan di lab", "jalur cadangan, jadwal approval, jam cadangan lab")
    b = b.replace("ethika akademik kampus", "pedoman etik akademik kampus")
    save("figm5-memo.svg", b, "figm5 memo")


# ---------------------------------------------------------------- 7. alur MCL
def fig_mcl():
    b = title("Jalur riset lewat Meta Content Library: dari proposal hingga enclave",
              "Contoh konkret kanal ter-gating: tiap panah adalah waktu tunggu, syarat, atau biaya.")
    boxes = [
        (40, "Tim riset", ["dosen penanggung", "jawab + proposal"], "#edf2f7"),
        (270, "Pendaftaran lembaga", ["verifikasi institusi", "+ tujuan riset"], "#fefcbf"),
        (490, "Approval", ["waktu tunggu;", "berlaku utk lembaga"], "#fed7d7"),
        (710, "Enclave berbayar", ["query didalam;", "eksport terbatas"], "#fed7d7"),
    ]
    for x, hd, sub, col in boxes:
        b += box(x, 96, 190, 78, col, "#4a5568") \
            + txt(x + 12, 120, hd, cls="t", bold=True) \
            + multi(x + 12, 142, sub, cls="tx", lh=17)
    for x1 in (230, 460, 680):
        b += arrow(x1, 135, x1 + 40, 135)
    lessons = [
        "1. Approval milik LEMBAGA, bukan pribadi — usulkan pendaftaran di minggu pertama semester.",
        "2. Enclave: data tidak boleh keluar; hasil yang bisa dibawa umumnya hanya agregat.",
        "3. Biaya kelembagaan yang dilaporkan publik 2026 sekitar USD 371 per tim per bulan (verifikasi!).",
        "4. Tanpa approval? triangulasi kanal terbuka (Bluesky) dan platform berkuota — dan jujur di memo tentang cakupannya.",
    ]
    b += multi(46, 210, ["Tiga pelajaran dari satu jalur:"], cls="ts", lh=22) \
        + multi(46, 234, lessons, cls="ts", lh=24)
    b = close_note(b, "Sumber: laporan publik akses riset Meta 2024–2026 (indikatif; verifikasi sebelum dikutip).")
    b = b.replace("query didalam;", "query di dalam;")
    b = b.replace("eksport terbatas", "ekspor terbatas")
    save("figm5-mcl.svg", b, "figm5 contentlibrary")


if __name__ == "__main__":
    fig_ladder()
    fig_timeline()
    fig_scraping()
    fig_pdp()
    fig_ethics()
    fig_memo()
    fig_mcl()
    print("selesai: figur materi 5 (7 file)")

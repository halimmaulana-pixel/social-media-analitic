# -*- coding: utf-8 -*-
"""7 SVG figures for Buku Ajar Materi 4 (style matches gen_figures_m23.py)."""
import os, textwrap

BASE = os.path.dirname(os.path.abspath(__file__))
W = 1000
INK, MUT, LINE = "#141414", "#5A5A5A", "#D9D9D9"
BLUE, GREEN, AMBER, ORANGE, PLUM, RED = ("#0072B2", "#009E73", "#E69F00",
                                         "#D55E00", "#7A4FA0", "#9B2C2C")
SOFTB, SOFTG, SOFTA, SOFTO, SOFTP, SOFTR = ("#F2F8FD", "#F1FAF5", "#FEF6E7",
                                           "#FDF1EA", "#F7F2FC", "#FBE9E9")
GREY, WHITE = "#F6F6F8", "#FFFFFF"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def wrap_(txt, n):
    return textwrap.wrap(txt, n)

def text(x, y, s, size=14, fill=INK, w=None, bold=False, anchor="start"):
    fw = ' font-weight="bold"' if bold else ""
    if w:
        out = []
        for i, ln in enumerate(wrap_(s, w)):
            out.append('<text x="%d" y="%d" font-size="%s" fill="%s"%s text-anchor="%s">%s</text>'
                       % (x, y + i * int(size + 4), size, fill, fw, anchor, esc(ln)))
        return "\n".join(out)
    return ('<text x="%d" y="%d" font-size="%s" fill="%s"%s text-anchor="%s">%s</text>'
            % (x, y, size, fill, fw, anchor, esc(s)))

def rect(x, y, w, h, fill, stroke=LINE, rx=8, sw=1.2, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<rect x="%d" y="%d" width="%d" height="%d" rx="%s" fill="%s" '
            'stroke="%s" stroke-width="%s"%s/>' % (x, y, w, h, rx, fill, stroke, sw, d))

def line_(x1, y1, x2, y2, stroke=MUT, sw=1.4, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="%s"%s/>' % (
        x1, y1, x2, y2, stroke, sw, d)

def arrow(x1, y1, x2, y2, color=BLUE, sw=2):
    return ('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="%s" '
            'marker-end="url(#ahb)"/>' % (x1, y1, x2, y2, color, sw))

def defs():
    return ('<defs><marker id="ahb" markerWidth="10" markerHeight="8" refX="9" refY="4" '
            'orient="auto"><path d="M0,0 L9,4 L0,8 z" fill="%s"/></marker></defs>' % INK)

def save(name, body, h):
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
           'role="img" aria-label="%s" font-family="Helvetica, Arial, sans-serif">\n%s\n%s\n</svg>'
           % (W, h, W, h, esc(name.replace("-", " ")), defs(), "\n".join(body)))
    open(os.path.join(BASE, name + ".svg"), "w", encoding="utf-8").write(svg)
    print(name, "bytes:", len(svg))



# --------------------------------------------------------------- 1. pipeline
def m4_pipeline():
    H = 430
    b = []
    b.append(text(22, 30, "Alur akuisisi data: dari pertanyaan riset ke arsip yang bisa direproduksi", 15, BLUE, bold=True))
    steps1 = [("1", "PERTANYAAN RISET", BLUE, SOFTB,
               "Satu kalimat yang bisa\ndiuji; batas populasi\npost & waktu ditulis"),
              ("2", "PLATFORM & JALUR", GREEN, SOFTG,
               "API resmi / firehose /\narsip terbuka; kuota\ndan biaya dicatat"),
              ("3", "KOLEKTOR", AMBER, SOFTA,
               "query + pagination +\nrate limit + quota\nbudget ala desain"),
              ("4", "RAW JSONL", ORANGE, SOFTO,
               "disimpan apa adanya,\nsebelum dibersihkan\n(raw first)")]
    x0, bw, gap, y1 = 30, 215, 18, 78
    for i, (nu, tit, col, bg, desc) in enumerate(steps1):
        x = x0 + i * (bw + gap)
        b.append(rect(x, y1, bw, 116, bg, stroke=col, sw=1.6))
        b.append(text(x + 12, y1 + 26, nu + ". " + tit, 13.5, col, bold=True))
        for j, ln in enumerate(desc.split("\n")):
            b.append(text(x + 12, y1 + 48 + j * 19, ln, 12.5, INK))
        if i < 3:
            b.append(arrow(x + bw + 2, y1 + 58, x + bw + gap - 2, y1 + 58))
    b.append(line_(x0 + 3 * (bw + gap) + bw / 2, y1 + 116, x0 + 3 * (bw + gap) + bw / 2, y1 + 144))
    steps2 = [("5", "CHECKSUM", GREEN, SOFTG,
               "SHA-256 tiap file;\nrusak/terpotong langsung\nketahuan"),
              ("6", "CLEANING & KAMUS", PLUM, SOFTP,
               "dedup, filter bot, kamus\nfield dari Materi 3;\nlog sebelum-sesudah"),
              ("7", "ANALISIS & PRESERVE", BLUE, SOFTB,
               "dataset + collection log\n+ kode; siap dipakai\nulang orang lain")]
    x2, y2 = 30, 156
    for i, (nu, tit, col, bg, desc) in enumerate(steps2):
        x = x2 + i * (bw + gap)
        b.append(rect(x, y2, bw, 116, bg, stroke=col, sw=1.6))
        b.append(text(x + 12, y2 + 26, nu + ". " + tit, 13.5, col, bold=True))
        for j, ln in enumerate(desc.split("\n")):
            b.append(text(x + 12, y2 + 48 + j * 19, ln, 12.5, INK))
        if i < 2:
            b.append(arrow(x + bw + 2, y2 + 58, x + bw + gap - 2, y2 + 58))
    b.append(arrow(x2 + 2 * (bw + gap) + bw / 2, y1 + 116, x2 + 2 * (bw + gap) + bw / 2, y2 - 2))
    b.append(rect(30, 296, W - 60, 92, WHITE, stroke=GREEN, sw=1.4))
    b.append(text(46, 320, "Prinsip yang diuji di lab pertemuan ini", 13, GREEN, bold=True))
    rules = ["Setiap kotak mengeluarkan artefak nyata: file raw, checksum, collection log.",
             "Langkah yang tidak tercatat = keputusan yang tidak bisa dipertahankan saat review."]
    for i, ln in enumerate(rules):
        b.append(text(46, 344 + i * 24, "•  " + ln, 13, INK))
    return b, H


# ------------------------------------------------------------------- 2. auth
def m4_auth():
    H = 470
    b = []
    b.append(text(22, 30, "Tiga pola autentikasi API — siapa yang membawa identitas", 15, BLUE, bold=True))
    panels = [
        ("A. BEARER TOKEN (APP-ONLY)", BLUE, SOFTB,
         ["Aplikasi riset", "↓ header: Authorization: Bearer", "Endpoint API platform"],
         "Mudah untuk data publik; kuota paling tipis; tidak membawa akun user.",
         "contoh: X API v2 app-only"),
        ("B. OAUTH 2.0 (USER CONTEXT)", ORANGE, SOFTO,
         ["Aplikasi riset", "↓ login + consent user", "Access token (+ refresh)"],
         "Aksi atas nama user; scope diberikan setipis mungkin.",
         "contoh: YouTube Data API v3"),
        ("C. APP PASSWORD (AT PROTOCOL)", PLUM, SOFTP,
         ["Aplikasi riset", "↓ app-password khusus riset", "PDC server / firehose"],
         "User tetap memegang kendali; bisa dicabut kapan saja.",
         "contoh: Bluesky AT Protocol"),
    ]
    pw, gap, y0 = 296, 22, 64
    for i, (tit, col, bg, rows, note, ex) in enumerate(panels):
        x = 30 + i * (pw + gap)
        b.append(rect(x, y0, pw, 300, bg, stroke=col, sw=1.6, rx=10))
        for j, ln in enumerate(wrap_(tit, 44)):
            b.append(text(x + 14, y0 + 26 + j * 18, ln, 12.5, col, bold=True))
        yy = y0 + 70
        for k, ln in enumerate(rows):
            b.append(rect(x + 16, yy, pw - 32, 30, WHITE, stroke=LINE, rx=6))
            b.append(text(x + pw / 2, yy + 20, ln, 12, INK, anchor="middle"))
            if k < len(rows) - 1:
                b.append(arrow(x + pw / 2, yy + 30, x + pw / 2, yy + 48, col, 1.6))
            yy += 52
        for j, ln in enumerate(wrap_(note, 46)):
            b.append(text(x + 14, yy + 14 + j * 18, ln, 11.5, MUT))
        b.append(text(x + 14, yy + 44 + 18 * len(wrap_(note, 46)) - 18, ex, 11.5, col, bold=True))
    b.append(rect(30, 382, W - 60, 62, WHITE, stroke=GREEN, sw=1.4))
    b.append(text(46, 404, "Aturan kredensial yang dipakai di lab", 12.5, GREEN, bold=True))
    b.append(text(46, 426, "•  Kredensial di file .env (di-gitignore); scope minimum; versi API dicantumkan di collection log.", 12.5, INK))
    b.append(text(46, 444, "•  Secret pernah bocor = asumsi bocor: regenerate, jangan hanya menghapus dari repo.", 12.5, INK))
    return b, H


# ------------------------------------------------------------- 3. pagination
def m4_pagination():
    H = 470
    b = []
    b.append(text(22, 30, "Dua mekanisme halaman: cursor pagination vs potongan waktu", 15, BLUE, bold=True))
    # lane A
    b.append(rect(30, 58, W - 60, 170, SOFTB, stroke=BLUE, sw=1.3, rx=10))
    b.append(text(46, 82, "A. CURSOR PAGINATION — API deserahkan token 'lanjut dari sini'", 13, BLUE, bold=True))
    box = [(46, "request#1"), (300, "page 1\nnext_token = c1"), (560, "request#2\n(next_token=c1)"), (820, "page 2 …")]
    for x, t in box:
        ln = t.split("\n")
        b.append(rect(x, 96, 130 if x == 46 else 200, 62, WHITE, stroke=LINE, rx=6))
        for j, s in enumerate(ln):
            b.append(text(x + (65 if x == 46 else 100), 116 + j * 18, s, 12, INK, anchor="middle"))
    b.append(arrow(178, 127, 298, 127))
    b.append(arrow(502, 127, 558, 127))
    b.append(arrow(762, 127, 818, 127))
    b.append(text(46, 188, "selama next_token masih dikirim → terus; token habis → berputar dari token null. cursor membuat trek tak bisa loncat.", 12, MUT, w=110))
    b.append(text(46, 218, "Dedup tetap wajib: retweet/konten editan bisa muncul dobel antar halaman.", 12, RED))
    # lane B
    b.append(rect(30, 240, W - 60, 150, SOFTO, stroke=ORANGE, sw=1.3, rx=10))
    b.append(text(46, 264, "B. POTONGAN WAKTU — kuota kecil? bagi rentang tanggal menjadi jendela", 13, ORANGE, bold=True))
    wins = [("11–17 Mar", 46), ("18–24 Mar", 276), ("25–31 Mar", 506), ("1–7 Apr", 736)]
    for t, x in wins:
        b.append(rect(x, 280, 190, 56, WHITE, stroke=LINE, rx=6))
        b.append(text(x + 95, 306, "jendela " + t, 12, INK, anchor="middle"))
        b.append(text(x + 95, 326, "max_results fase per jendela", 11, MUT, anchor="middle"))
    for x in (238, 468, 698):
        b.append(arrow(x, 308, x + 36, 308, ORANGE, 1.6))
    b.append(text(46, 366, "Hati-hati dobel di tepi jendela: dedup by post_id + cap waktu eksklusif (batas kiri termasuk, batas kanan tidak).", 12, RED))
    # bottom
    b.append(rect(30, 404, W - 60, 48, WHITE, stroke=GREEN, sw=1.4))
    b.append(text(46, 432, "Angka halaman yang selalu sama persis (mis. 200 tiap run) = tanda query terpotong diam-diam (silent truncation). Catat!", 12.5, GREEN))
    return b, H


# ------------------------------------------------------------ 4. rate limit
def m4_ratelimit():
    H = 440
    b = []
    b.append(text(22, 30, "Rate limit & kuota: anggaran yang dijadwalkan sejak hari pertama", 15, BLUE, bold=True))
    # bucket
    b.append(rect(30, 58, 430, 250, SOFTB, stroke=BLUE, sw=1.4, rx=10))
    b.append(text(50, 84, "BUCKET PER 15 MENIT (contoh satu tier)", 13, BLUE, bold=True))
    flask_x, flask_y, flask_w, flask_h = 70, 110, 90, 170
    b.append(rect(flask_x, flask_y, flask_w, flask_h, WHITE, stroke=LINE, rx=8))
    b.append(rect(flask_x, flask_y + 70, flask_w, flask_h - 70, "#C8E3F5", stroke="none", rx=0))
    b.append(text(flask_x + flask_w / 2, flask_y + 130, "terpakai", 11.5, BLUE, anchor="middle"))
    b.append(text(flask_x + flask_w / 2, flask_y + 148, "di jendela ini", 11.5, MUT, anchor="middle"))
    b.append(text(flask_x + flask_w + 24, flask_y + 24, "rekon: hitung request, bukan post", 12, INK, w=50))
    b.append(text(flask_x + flask_w + 24, flask_y + 92, "backoff: kalau 429, tunggu header reset; jangan terus ngebut", 12, RED, w=50))
    b.append(text(50, 296, "kuota per endpoint berbeda dari kuota per jendela — dua kalender, dua neraca.", 11.5, MUT, w=62))
    # budget panel
    b.append(rect(480, 58, 490, 250, SOFTG, stroke=GREEN, sw=1.4, rx=10))
    b.append(text(498, 84, "ANGGARAN KUOTA (contoh perencanaan, bukan angka resmi)", 12.5, GREEN, bold=True))
    rows = ["Kuota yg dialokasikan utk riset: 20.000 post/hari (fase maksimal satu tier)",
            "Target korpus: 150.000 post (satu topik, 30 hari)",
            "Buffer eksperimen: 25% (query uji cobacoba di sini, bukan di produksi)",
            "Estimasi durasi koleksi: 9–10 hari kerja (kurva nonlinier saat weekend)",
            "Strategi: pagi berjalan sejahtera; kalau jendela habis, jadwal lain dipakai"]
    yy = 110
    for ln in rows:
        for j, s in enumerate(wrap_("• " + ln, 82)):
            b.append(text(498, yy + j * 17, s, 11.5, INK))
        yy += 38
    b.append(rect(30, 326, W - 60, 88, WHITE, stroke=AMBER, sw=1.4))
    b.append(text(46, 350, "Aturan anggaran yang dipakai di lab", 12.5, AMBER, bold=True))
    rules = ["Query uji dikerjakan di budget eksperimen; pemborosan kuota = desain yang buruk, bukan pekerjaan rajin.",
             "Setiap run dicatat: jumlah request, jumlah post, sisa kuota — kalau run gagal, catatan menyelamatkan sesi berikut."]
    for i, ln in enumerate(rules):
        for j, s in enumerate(wrap_("• " + ln, 118)):
            b.append(text(46, 374 + i * 22 + j * 17, s, 11.5, INK))
    return b, H


# ------------------------------------------------------------ 5. checkpoint
def m4_checkpoint():
    H = 430
    b = []
    b.append(text(22, 30, "Checkpoint & checksum: koleksi yang selamat dari crash dan koneksi", 15, BLUE, bold=True))
    loop = [("fetch\nhalaman", BLUE), ("tulis hanya-append\nraw_history.jsonl", GREEN),
            ("hash SHA-256\nfile baru", AMBER), ("update checkpoint.json", ORANGE)]
    x0, bw, gap, y0 = 40, 200, 34, 84
    for i, (lbl, col) in enumerate(loop):
        x = x0 + i * (bw + gap)
        ln = lbl.split("\n")
        b.append(rect(x, y0, bw, 66, WHITE, stroke=col, sw=1.5, rx=8))
        for j, s in enumerate(ln):
            b.append(text(x + bw / 2, y0 + 26 + j * 18, s, 12.5, col, anchor="middle"))
        if i < 3:
            b.append(arrow(x + bw + 2, y0 + 33, x + bw + gap - 2, y0 + 33))
    # loop back arrow
    b.append(line_(x0 + bw / 2, y0 + 66, x0 + bw / 2, y0 + 92, ORANGE, 1.6))
    b.append(arrow(x0 + bw / 2, y0 + 92, x0 + 3 * (bw + gap) + bw / 2, y0 + 92, ORANGE, 1.6))
    b.append(text(x0 + bw / 2, y0 + 112, "kembali ke awal sampai next_token habis / kuota habis / target tercapai", 12, ORANGE, anchor="middle"))
    crash = [rect(40, 160, 900, 96, SOFTR, stroke=RED, sw=1.4, rx=10),
             text(58, 186, "SAAT RUN TERPUTUS (listrik, timeout, rate limit keras)", 13, RED, bold=True),
             text(58, 208, "•  raw app-only: file yang terlanjur terulis aman — tidak ada yang dikorbankan.", 12, INK),
             text(58, 226, "•  checkpoint.json bilang: run_id, waktu, file terakhir, halaman terakhir → resume dari sini.", 12, INK),
             text(58, 244, "•  kolektor NEMPARKAN jendela waktu sisa; jangan mulai dari nol seperti orang panik.", 12, RED)]
    for c in crash:
        b.append(c)
    # checksum panel
    b.append(rect(40, 272, 440, 130, GREY, stroke=LINE, rx=10))
    b.append(text(56, 296, "nilai SHA-256 satu file (contoh)", 12.5, MUT, bold=True))
    hx = "3f9a12c4…  raw_w03_part01.jsonl"
    b.append(text(56, 320, hx, 12.5, INK))
    b.append(text(56, 344, "checksum = sidik jari file.", 12, MUT, w=46))
    b.append(text(56, 366, "file rusak/terpotong → hash beda → ditolak masuk analisis.", 12, INK, w=46))
    b.append(rect(500, 272, 440, 130, GREY, stroke=LINE, rx=10))
    b.append(text(516, 296, "jendela waktu sisa di checkpoint (contoh)", 12.5, MUT, bold=True))
    b.append(text(516, 320, '"window": "2026-11-03 → 2026-11-07",', 12, INK))
    b.append(text(516, 344, '"page": "halaman 23", "run_id": "run03",', 12, INK))
    b.append(text(516, 368, 'resume = mulai run03 dari halaman 23', 12, MUT))
    return b, H


# -------------------------------------------------------- 6. collection log
def m4_collectionlog():
    H = 470
    b = []
    b.append(text(22, 30, "Collection log — bukti koleksi, bukan laporan akhir", 15, BLUE, bold=True))
    b.append(text(22, 52, "Fungsi: membebaskan memori; menegakkan konsistensi antar run; mata-mata atas silent truncation.", 12.5, MUT))
    rows = [
        ("run_id", "run02", "identitas run; idempoten (ulang run menimpa id sama)"),
        ("platform + endpoint", "X API v2 · /2/tweets/search/recent", "versi API dicantumkan — docs berubah per bulan"),
        ("auth mode", "app-only bearer", "bearer / oauth2 / app-password"),
        ("sampling frame", "keyword (#BapakKantor OR kata kunci tokoh) window 7 hari", "query string utuh + rentang waktu UTC"),
        ("mulai–selesai (UTC+WIB)", "2026-11-03 00:00Z ↔ 07:00 WIB", "dua zona berdampingan — tidak boleh dicampur diam-diam"),
        ("pages / post", "45 halaman · 3.120 post mentah", "jika bulat selerusnya (200/200/…) → curiga truncation"),
        ("filter aktif", "exclude retweet; exclude tombol query promosi", "setiap filter platform dicantumkan — ia ikut membentuk sampel"),
        ("dedup & jendela", "by post_id; kap waktu kiri-inklusif", "dedup across window; tepi jendela tak dobel"),
        ("file + checksum", "raw_w03_part00.jsonl …  shasum256s 4 file", "file raw di arsip; hash disimpan berdekatan"),
        ("kuota", "19.4k/20.000 post terpakai", "run berikutnya harus tahu sisa anggaran"),
    ]
    y0, rh = 76, 37
    x1, x2, w1 = 250, 660, 240
    b.append(rect(30, y0 - 22, W - 60, 26, "#E9EEF4", stroke=LINE, rx=4))
    b.append(text(44, y0 - 4, "Field", 12.5, BLUE, bold=True))
    b.append(text(x1 + 10, y0 - 4, "Contoh isi (run nyata di lab)", 12.5, BLUE, bold=True))
    b.append(text(x2 + 12, y0 - 4, "Fungsi", 12.5, BLUE, bold=True))
    for i, (f, v, fu) in enumerate(rows):
        y = y0 + i * rh
        col = WHITE if i % 2 == 0 else "#FAFBFC"
        b.append(rect(30, y, W - 60, rh, col, stroke=LINE, sw=1))
        b.append(text(44, y + 23, f, 12.5, PLUM))
        for j, s in enumerate(wrap_(v, 36)):
            b.append(text(x1 + 10, y + 15 + j * 16, s, 12, INK))
        for j, s in enumerate(wrap_(fu, 44)):
            b.append(text(x2 + 12, y + 15 + j * 16, s, 11.5, MUT))
    b.append(text(30, y0 + len(rows) * rh + 26,
                  "Reviewer menilai collection log dulu, baru dataset: log yang baik membuat dataset bisa direproduksi tanpa bertanya.", 12.5, GREEN))
    return b, H


# ------------------------------------------------------------ 7. sampling
def m4_sampling():
    H = 520
    b = []
    b.append(text(22, 30, "Empat sampling frame — dan bias yang menyertai masing-masing", 15, BLUE, bold=True))
    cells = [
        ("KEYWORD SEARCH", BLUE, SOFTB,
         "Sampel = post yang memuat query (hashtag/kata).",
         "Kuat: relevan langsung dgn topik.",
         "Bahaya: query sempit = rantai kecil; platform bisa memotong query diam-diam."),
        ("TIMELINE (PER AKUN)", GREEN, SOFTG,
         "Sampel = seluruh aktivitas akun yang dipilih.",
         "Kuat: konteks akun utuh, kronologis.",
         "Bahaya: representatifnya akun, bukan pop; kurasi hidup manusia (bias kurator)."),
        ("SNOWBALL (REPLY/MENTION)", ORANGE, SOFTO,
         "Sampel = perluasan via tautan dari sampel awal.",
         "Kuat: menemukan komunitas tersembunyi.",
         "Bahaya: terjebak di satu kubu — lingkaran yang menutup diri."),
        ("RANDOM (FIREHOSE SAMPLE)", PLUM, SOFTP,
         "Sampel = cuplikan acak dari stream/firehose.",
         "Kuat: tak dibentuk algoritma recommendation per-halaman.",
         "Bahaya: banyak tak relevan; users kecil terwakili, justifikasi window harus ditulis."),
    ]
    pw, ph, gap = 462, 178, 24
    for i, (tit, col, bg, s, ku, ba) in enumerate(cells):
        x = 30 + (i % 2) * (pw + gap)
        y = 58 + (i // 2) * (ph + gap)
        b.append(rect(x, y, pw, ph, bg, stroke=col, sw=1.5, rx=10))
        b.append(text(x + 16, y + 26, tit, 13, col, bold=True))
        yy = y + 48
        for j, s2 in enumerate(wrap_(s, 70)):
            b.append(text(x + 16, yy + j * 17, s2, 12, INK))
        yy += (17 * len(wrap_(s, 70))) + 6
        b.append(text(x + 16, yy, "↗ " + ku, 11.5, GREEN, w=62))
        yy += 18 * len(wrap_(ku, 62))
        b.append(text(x + 16, yy, "✕ " + ba, 11.5, RED, w=62))
    b.append(rect(30, 446, W - 60, 56, WHITE, stroke=AMBER, sw=1.4))
    b.append(text(46, 468, "Pilih frame yang menjawab pertanyaan riset — bukan yang paling mudah. Kuota & akses" , 12.5, AMBER))
    b.append(text(46, 488, "adalah bagian dari desain: backbone frame yang lemah tidak diselamatkan oleh jumlah halaman yang besar.", 12.5, AMBER))
    return b, H


def cleanup(obj):
    return [x for x in obj if x]


FIGS = [
    ("figm4-pipeline", m4_pipeline),
    ("figm4-auth", m4_auth),
    ("figm4-pagination", m4_pagination),
    ("figm4-ratelimit", m4_ratelimit),
    ("figm4-checkpoint", m4_checkpoint),
    ("figm4-collectionlog", m4_collectionlog),
    ("figm4-sampling", m4_sampling),
]

for name, fn in FIGS:
    body, h = fn()
    save(name, cleanup(body), h)
print("done")

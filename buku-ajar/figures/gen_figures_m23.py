# -*- coding: utf-8 -*-
"""11 SVG figures for Buku Ajar Materi 2 & 3 (style matches fig1-fig6)."""
import os, textwrap

BASE = os.path.dirname(os.path.abspath(__file__))
W = 1000
INK, MUT, LINE, BG = "#141414", "#5A5A5A", "#D9D9D9", "#FFFFFF"
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


# -------------------------------------------------------------- 1. ecosystem
def m2_ecosystem():
    H = 560
    b = [rect(10, 46, W - 20, H - 66, GREY, rx=14)]
    b.append(text(22, 30, "Lima kawasan ekosistem media sosial (2026)", 15, BLUE, bold=True))
    panels = [
        ("KAWASAN MIKROBLOG / TEKS", BLUE, SOFTB,
         ["X - API berbayar sejak 2023", "Threads - feed, API riset terbatas",
          "Bluesky - firehose terbuka (AT Protocol)"],
         "Ciri data: teks pendek + reply/follow"),
        ("KAWASAN SHORT-VIDEO", ORANGE, SOFTO,
         ["TikTok - Research API (terdaftar)", "Instagram Reels - gated via Meta",
          "YouTube Shorts - data via Data API"],
         "Ciri data: watch time & completion"),
        ("KAWASAN VIDEO PANJANG", ORANGE, SOFTO,
         ["YouTube - Data API berkuota", "Live stream - chat burst"],
         "Ciri data: hitaman view + komentar"),
        ("KAWASAN KOMUNITAS / FORUM", GREEN, SOFTG,
         ["Reddit - API berkuota", "Forum & grup HTML/Telegram",
          "Diskusi thread terstruktur"],
         "Ciri data: kedalaman percakapan"),
        ("KAWASAN PROTOKOL TERBUKA", GREEN, SOFTG,
         ["AT Protocol - Jetstream repat", "ActivityPub - Mastodon dkk.",
          "Graf sosial pengguna terpublikasi"],
         "Ciri data: reproducible & andal"),
        ("KAWASAN META (GATED)", PLUM, SOFTP,
         ["Facebook & Instagram - MCL", "Threads - via Meta riset",
          "Enclave SOMAR (eksekusi terbatas)"],
         "Ciri data: arsip besar, akses dijaga"),
    ]
    for i, (name, stroke, fill, items, note) in enumerate(panels):
        x = 22 + (i % 3) * 320
        y = 66 + (i // 3) * 250
        b.append(rect(x, y, 300, 226, fill, stroke=stroke, sw=1.8))
        b.append(text(x + 14, y + 26, name, 13, stroke, bold=True, w=34))
        for j, it in enumerate(items):
            b.append(text(x + 14, y + 56 + j * 26, "- " + it, 12, w=38))
        b.append(line_(x + 14, y + 152, x + 284, y + 152, stroke=LINE))
        b.append(text(x + 14, y + 180, note, 12, MUT, w=36))
    return b, H


# ------------------------------------------------------------- 2. affordance
def m2_affordance():
    H = 620
    rows_ = ["X", "TikTok", "Instagram", "YouTube", "Reddit", "Bluesky", "Threads"]
    cols_ = ["teks", "media", "engagement", "graf", "firehose", "retrospektif"]
    access = {"X": ("berbayar", RED), "TikTok": ("terdaftar", AMBER),
              "Instagram": ("gated", PLUM), "YouTube": ("berkuota", BLUE),
              "Reddit": ("berkuota", BLUE), "Bluesky": ("TERBUKA", GREEN),
              "Threads": ("tertutup", MUT)}
    full = {"X": ["teks", "retrospektif"], "TikTok": ["media", "engagement"],
            "Instagram": ["media", "engagement"], "YouTube": ["media", "engagement", "retrospektif"],
            "Reddit": ["teks", "engagement", "graf", "retrospektif"],
            "Bluesky": ["teks", "graf", "firehose", "retrospektif"], "Threads": ["teks", "engagement"]}
    half = {"X": ["media", "graf", "engagement"], "TikTok": ["teks"], "Instagram": ["teks"],
            "YouTube": ["teks"], "Reddit": ["media"], "Bluesky": ["media"],
            "Threads": ["retrospektif"]}
    x0, y0, cw, ch, lw = 210, 108, 124, 46, 150
    b = [rect(10, 46, W - 20, H - 66, WHITE, rx=14)]
    b.append(text(24, 30, "Matriks affordance: apa yang bisa diambil dari tiap platform", 15, BLUE, bold=True))
    for ci, c in enumerate(cols_):
        b.append(text(x0 + cw * ci + cw / 2, 30 + y0 - 34, c, 12.5, INK, bold=True, anchor="middle"))
    b.append(text(x0 + cw * 6 + cw / 2, 30 + y0 - 34, "STATUS AKSES", 12.5, INK, bold=True, anchor="middle"))
    for i, r in enumerate(rows_):
        yy = y0 + i * ch
        b.append(rect(28, yy - 18, lw, 34, GREY, stroke=LINE, rx=6))
        b.append(text(42, yy + 4, r, 14, INK, bold=True))
        for ci in range(7):
            cx = x0 + cw * ci
            if ci == 6:
                lab, col = access[r]
                fillc = SOFTG if col == GREEN else SOFTA
                if col == MUT:
                    fillc = GREY
                b.append(rect(cx + 8, yy - 15, cw - 22, 28, fillc, stroke=col, sw=1.4, rx=5))
                b.append(text(cx + cw / 2 - 3, yy + 4, lab, 11.5, col if col != MUT else MUT,
                              bold=True, anchor="middle"))
                continue
            val = "F" if c in full.get(r, []) else ("H" if c in half.get(r, []) else "N")
            if val == "F":
                b.append(rect(cx + 16, yy - 13, cw - 34, 26, BLUE, rx=4))
            elif val == "H":
                b.append(rect(cx + 16, yy - 13, cw - 34, 26, WHITE, stroke=BLUE, sw=1.4, rx=4))
                b.append(rect(cx + 16, yy - 13, (cw - 34) / 2, 26, BLUE, rx=4))
            else:
                b.append(rect(cx + 16, yy - 13, cw - 34, 26, WHITE, stroke=LINE, sw=1.2, rx=4))
    meaning = {"teks": "post/caption utama", "media": "gambar/video terekap",
               "engagement": "like/simpan/tonton", "graf": "reply/follow/mention",
               "firehose": "stream realtime", "retrospektif": "unduh data lama"}
    for ci, c in enumerate(cols_):
        b.append(text(x0 + cw * ci + cw / 2, y0 + ch * 7 + 24, meaning[c], 10.5, MUT, anchor="middle"))
    b.append(rect(28, y0 + ch * 7 + 52, 946, 74, SOFTB, stroke=LINE))
    b.append(text(44, y0 + ch * 7 + 78, "Kotak biru penuh = tersedia penuh  ·  setengah biru = tersedia sebagian  ·  putih = tidak tersedia", 12.5))
    b.append(text(44, y0 + ch * 7 + 104, "Indikasi per 2026 - tier, kuota, dan field API berubah-ubah: selalu cek ulang tiap semester.", 12.5, MUT))
    return b, H


# ------------------------------------------------------------------ 3. feed
def m2_feed():
    H = 470
    b = [rect(10, 46, W - 20, H - 66, WHITE, rx=14)]
    b.append(text(22, 30, "Tiga logika feed - dan sampel data yang dihasilkannya", 15, BLUE, bold=True))
    cards = [
        ("KRONOLOGIS", GREEN, SOFTG, "Post mengikuti urutan waktu murni",
         "Sampel: apa saja yang tayang dalam jendela waktu; waktu ukur yang jujur.",
         "Cocok untuk: kecepatan sebaran per jam"),
        ("FOLLOW-GRAPH", PLUM, SOFTP, "Post terbatas pada jaringan follow pengguna",
         "Sampel: kubu yang saling follow - bukan kubu yang jauh.",
         "Cocok untuk: analisis tautan relasi"),
        ("REKOMENDASI", ORANGE, SOFTO, "Ranking model memilih apa yang tampil",
         "Sampel: yang direkomendasikan, bukan yang tayang semuanya.",
         "Cocok untuk: analisis virality - hati-hati bias"),
    ]
    for i, (name, stroke, fill, def_, samp, cocok) in enumerate(cards):
        x = 28 + i * 322
        b.append(rect(x, 66, 296, 230, fill, stroke=stroke, sw=1.8))
        b.append(text(x + 16, 92, name, 14, stroke, bold=True, w=34))
        b.append(text(x + 16, 122, def_, 12.5, w=38))
        b.append(line_(x + 16, 150, x + 278, 150, stroke=LINE))
        b.append(text(x + 16, 176, samp, 12, INK, w=38))
        b.append(text(x + 16, 240, "Pakai untuk:", 11.5, MUT))
        b.append(text(x + 16, 262, cocok, 12, stroke, bold=True, w=38))
    b.append(text(22, 332, "Konsekuensi metodologis (yang sering tidak disebut)", 13, INK, bold=True))
    warns = [
        "Feed rekomendasi menghapus waktu asli tayang dari og: jangan baca timestamp sampel rekomendasi sebagai jam jual.",
        "Hasil di feed kronologis tidak berlaku di feed rekomendasi tanpa pengkajian ulang.",
        "Kombinasi nominal: 'engager' di feed kronologis = siapa saja yang melihat; di rekomendasi = siapa saja yang algoritma pilih.",
    ]
    for i, wl in enumerate(warns):
        y = 350 + i * 40
        b.append(rect(28, y, 944, 34, SOFTA, stroke=AMBER, rx=6))
        b.append(text(44, y + 22, wl, 12, w=140))
    return b, H


# -------------------------------------------------------------- 4. openness
def m2_openness():
    H = 600
    b = [rect(10, 46, W - 20, H - 66, WHITE, rx=14)]
    b.append(text(22, 30, "Tangga keterbukaan akses riset data platform (2026)", 15, BLUE, bold=True))
    tiers = [
        ("1. API / FIREHOSE TERBUKA", GREEN, SOFTG, "Bluesky Jetstream - Mastodon",
         "Gratis, tanpa penjajakan - riset graf skala besar & reproducible"),
        ("2. API BERKUOTA", BLUE, SOFTB, "YouTube Data API - Reddit API",
         "Gratis, kuota harian: kuota harian dibagi membagi antar tim"),
        ("3. API TERDAFTAR", AMBER, SOFTO, "TikTok Research API",
         "Wajib daftar + klarifikasi riset; field & kuota di kasernya"),
        ("4. GATED AKADEMIK", PLUM, SOFTP, "Meta Content Library (+ Threads riset)",
         "Gratis untuk kampus yang lolos; eksekusi di enclave, ekspor terbatas"),
        ("5. API BERBAYAR", RED, SOFTR, "X API v2 (tier berbayar)",
         "Akses riset gratis dicabut 2023; anggaran wajib masuk rencana studi"),
    ]
    for i, (name, stroke, fill, plats, note) in enumerate(tiers):
        y = 72 + i * 96
        indent = 24 + i * 22
        b.append(rect(indent, y, 480, 82, fill, stroke=stroke, sw=1.8))
        b.append(text(indent + 14, y + 26, name, 13.5, stroke, bold=True))
        b.append(text(indent + 14, y + 48, plats, 12.5, INK, w=78))
        b.append(rect(indent + 496, y, 928 - indent - 496, 82, WHITE, stroke=LINE, rx=8))
        b.append(text(indent + 510, y + 30, note, 12, MUT, w=68))
        if i < 4:
            b.append(arrow(indent + 232, y + 96 - 14, indent + 232, y + 96, color=stroke, sw=2))
    b.append(line_(24, 560, 950, 560, stroke=MUT, sw=1.2, dash="5 4"))
    b.append(text(24, 584, "Membaca tangga dari kiri-atas ke kanan-bawah: makin ke bawah, makin mahal dan makin ribet perizinannya.", 12, MUT))
    b.append(text(24, 604, "Seluruhnya legal bagi riset; keputusannya adalah desain studi memilih anak tangga mana yang menopang pertanyaan.", 12, MUT))
    return b, H


# --------------------------------------------------------------- 5. timeline
def m2_timeline():
    H = 400
    b = [rect(10, 46, W - 20, H - 66, WHITE, rx=14)]
    b.append(text(22, 30, "Timeline kebijakan akses data riset 2021-2026", 15, BLUE, bold=True))
    ay = 250
    b.append(line_(60, ay, 950, ay, stroke=MUT, sw=2))
    events = [
        (2021.8, "TikTok Research API mulai berlaku (2021-22)", ORANGE),
        (2023.1, "X: akses riset gratis dicabut (Feb-Apr 2023)", RED),
        (2023.45, "Reddit: API membayar (Jun 2023)", AMBER),
        (2024.2, "Meta Content Library dibuka (2024)", PLUM),
        (2024.6, "AT Protocol & Jetstream matang (2024)", GREEN),
        (2026.05, "Enclave riset mulai berbayar (Jan 2026)", RED),
    ]
    for t, label, col in events:
        x = 60 + (950 - 60) * (t - 2021) / 5.0
        b.append('<circle cx="%d" cy="%d" r="6" fill="%s"/>' % (int(x), ay, col))
        up = label.find("X:") >= 0 or label.find("Enclave") >= 0
        ychat = ay - 56 if up else ay + 44
        b.append(line_(int(x), ay, int(x), ay - 40 if up else ay + 28, stroke=col, sw=1.4))
        b.append(text(max(int(x) - 8, 28), ychat, label, 11.5, col, bold=True, w=24))
    for yr in range(2021, 2027):
        x = 60 + (950 - 60) * (yr - 2021) / 5.0
        b.append(text(int(x), ay + 76, str(yr), 12.5, INK, anchor="middle", bold=True))
    b.append(text(24, 368, "Pesan utama: akses riset condong menyempit sejak 2023 - desain studi mesti pilih platform", 12.5, w=120))
    b.append(text(24, 388, "yang aksesnya masih jelas tanggal kebijakannya, bukan dipilih setelah pengeluaran biaya naik.", 12.5, w=120))
    return b, H


# --------------------------------------------------------------- 6. metrics
def m2_metrics():
    H = 480
    b = [rect(10, 46, W - 20, H - 66, WHITE, rx=14)]
    b.append(text(22, 30, "Satu kata 'engagement' - empat definisi beda", 15, BLUE, bold=True))
    plates = [
        ("X", BLUE, SOFTB, ["like (suka)", "repost (re-post)", "reply (jawab)", "quote + impression"]),
        ("TikTok", ORANGE, SOFTO, ["like (suka)", "komentar", "share (bagikan)", "save + watch time"]),
        ("YouTube", PLUM, SOFTP, ["view (tonton)", "watch time total", "like (suka)", "komentar + share"]),
        ("Instagram", GREEN, SOFTG, ["like (suka)", "komentar", "save (simpan)", "share (bagikan)"]),
    ]
    for i, (name, stroke, fill, items) in enumerate(plates):
        x = 30 + i * 244
        b.append(rect(x, 66, 216, 190, fill, stroke=stroke, sw=1.8))
        b.append(text(x + 14, 92, name, 14, stroke, bold=True))
        for j, it in enumerate(items):
            b.append(text(x + 14, 122 + j * 28, "- " + it, 12.5, w=26))
    b.append(text(22, 292, "Ambang perbandingan yang masih sah:", 13, INK, bold=True))
    rules = [
        "1. Normalisasi: per 1.000 pengikut atau per 1.000 penonton - jangan raw count mentah.",
        "2. Damai komponen: hanya banding like vs like, save vs save - bukan engagement berleo.",
        "3. Nyatakan definisi: laporan musti cantumkan versi definisi yang dipakai.",
        "4. Watch time & save: dua metrik paling iyak & paling beda antar platform; lankan biasa.",
    ]
    for i, r in enumerate(rules):
        y = 306 + i * 40
        b.append(rect(28, y, 944, 34, SOFTB, stroke=LINE, rx=6))
        b.append(text(44, y + 22, r, 12, w=150))
    return b, H


# ----------------------------------------------------------- 7. taxonomy m3
def m3_taxonomy():
    H = 600
    b = [rect(10, 46, W - 20, H - 66, WHITE, rx=14)]
    b.append(text(22, 30, "Taksonomi unit data media sosial - lima keluarganya", 15, BLUE, bold=True))
    b.append(rect(418, 62, 164, 40, BLUE, rx=10))
    b.append(text(500, 88, "SATU POST", 14, "#FFFFFF", bold=True, anchor="middle"))
    group = [
        ("TEKS", BLUE, SOFTB, ["isi post & caption", "hashtag & mention", "sarkasme & emoji"]),
        ("MEDIA", ORANGE, SOFTO, ["frame video utama", "teks on-screen (OCR)", "audio (transkrip)"]),
        ("INTERAKSI", GREEN, SOFTG, ["like / suka", "komentar / reply", "share / save"]),
        ("METADATA", PLUM, SOFTP, ["timestamp UTC & lokal", "lokasi (bila ada)", "bahasa & perangkat"]),
        ("LOG ENGAGEMENT", RED, SOFTR, ["watch time & completion", "urutan frame ditonton", "klik notifikasi"]),
    ]
    for i, (name, stroke, fill, items) in enumerate(group):
        x = 24 + i * 196
        cx = x + 90
        b.append(line_(500, 102, cx, 148, stroke=stroke, sw=1.4))
        b.append(rect(x, 148, 180, 224, fill, stroke=stroke, sw=1.8))
        b.append(text(x + 12, 174, name, 13, stroke, bold=True, w=22))
        for j, it in enumerate(items):
            b.append(text(x + 12, 202 + j * 32, "- " + it, 11.5, w=24))
        b.append(line_(500, 102, cx, 148, stroke=stroke, sw=1.4))
    b.append(rect(24, 404, 944, 108, SOFTB, stroke=LINE))
    b.append(text(40, 432, "Moral: lima keluarga data hadir dalam SATU objek post. Analisis multimodal = menggabungkan", 12.5, w=100))
    b.append(text(40, 454, "semua keluarga atas berdasarkan post ID yang sama - bukan lima tabel yang biak tanpa tautan.", 12.5, w=100))
    b.append(text(40, 476, "Praktik juga aman: simpan mentah JSON utuh (audit), lalu ekstrak field di kamus field (efisien).", 12.5, w=100))
    b.append(text(24, 560, "Aliran data post = input beberapa kelompok metode (NLP untuk teks, CV untuk frame, timeseries untuk watch time)", 12, MUT))
    b.append(text(24, 580, "karena post yang sama bisa ditanya beragam pertanyaan.", 12, MUT))
    return b, H


# ------------------------------------------------------------- 8. anatomy m3
def m3_anatomy():
    H = 560
    b = [rect(10, 46, W - 20, H - 66, WHITE, rx=14)]
    b.append(text(22, 30, "Anatomi satu objek post (JSON dari API)", 15, BLUE, bold=True))
    b.append(rect(46, 60, 470, 440, "#1E1E2E", rx=10))
    code = [
        ("{", MUT), ('  "id": "post_1892...",', BLUE), ('  "text": "...om telolet om...",', "#C7E5FA"),
        ('  "created_at": "2026-10-25T08:14:05Z",', "#C7E5FA"), ('  "lang": "in",', "#C7E5FA"),
        ('  "author": {', ORANGE), ('    "id": "user_77",', ORANGE), ('    "followers": 4820,', ORANGE),
        ('    "verified": false', ORANGE), ("  },", ORANGE), ('  "metrics": {', PLUM),
        ('    "like": 312,', PLUM), ('    "reply": 44,', PLUM), ('    "share": 87,', PLUM),
        ('    "impression": 51203', PLUM), ("  },", PLUM), ('  "media": [{"type": "video",', GREEN),
        ('             "duration": 41}],', GREEN), ('  "entities": {', BLUE),
        ('    "hashtag": ["ulasan"],', BLUE), ('    "mention": ["user_x"]', BLUE), ("  }", BLUE),
        ("}", MUT),
    ]
    for i, (ln, col) in enumerate(code):
        b.append('<text x="62" y="%d" font-family="Consolas, monospace" font-size="13" fill="%s">%s</text>'
                 % (88 + i * 18, col, esc(ln)))
    anns = [
        ("IDENTITAS", RED, "id + URL post + timestamp: dasar dedup dan tautan ke artefak lain."),
        ("KEPENGARANGAN", ORANGE, "author.id, followers, verified: jangan dipakai langsung sebagai identitas pribadi."),
        ("ISI", BLUE, "text + entities (hashtag/mention): bahan pokok untuk analitik NLP teks."),
        ("METRIK", PLUM, "engagement per aksi: definisinya beda per platform - nyatakan aturan di laporan."),
        ("MEDIA", GREEN, "jenis media + durasi: pintu masuk analisis frame & transkrip audio."),
    ]
    for i, (name, col, note) in enumerate(anns):
        y = 66 + i * 90
        b.append(line_(526, y + 30, 560, y + 30, stroke=col, sw=1.6))
        b.append(rect(560, y, 396, 78, SOFTB, stroke=LINE, rx=8))
        b.append(text(576, y + 26, name, 13, col, bold=True))
        b.append(text(576, y + 50, note, 11.5, MUT, w=64))
    return b, H


# ------------------------------------------------------------ 9. spectrum m3
def m3_spectrum():
    H = 440
    b = [rect(10, 46, W - 20, H - 66, WHITE, rx=14)]
    b.append(text(22, 30, "Spektrum struktur: terstruktur - semi-terstruktur - tak terstruktur", 15, BLUE, bold=True))
    bands = [
        ("TERSTRUKTUR", GREEN, SOFTG, "engagement log, follower count, watch time, timestamp",
         "tabel SQL/pandas; dtype tetap; skala besar pilih parquet"),
        ("SEMI-TERSTRUKTUR", BLUE, SOFTB, "objek API JSON (post, comment), HTML forum, XML feed",
         "pandas/tidy + kolom entitas; simpan JSON asli untuk audit"),
        ("TAK TERSTRUKTUR", ORANGE, SOFTO, "teks bebas komentar, gambar, video, audio, live-stream",
         "NLP/CV/ASR per kasus; simpan fitur hasil ekstraksi + penunjuk file mentah"),
    ]
    for i, (name, stroke, fill, ex, note) in enumerate(bands):
        x = 30 + i * 322
        b.append(rect(x, 66, 296, 214, fill, stroke=stroke, sw=1.8))
        b.append(text(x + 16, 92, name, 13.5, stroke, bold=True, w=32))
        b.append(text(x + 16, 120, "Contoh konten:", 12, MUT))
        b.append(text(x + 16, 142, ex, 12.5, w=38))
        b.append(line_(x + 16, 168, x + 280, 168, stroke=LINE))
        b.append(text(x + 16, 192, "Implikasi tooling:", 12, MUT))
        b.append(text(x + 16, 214, note, 12, INK, w=38))
    for i in (0, 1):
        b.append(arrow(324 + i * 322, 254, 350 + i * 322, 254, color=BLUE, sw=2))
    b.append(text(22, 300, "Satu post biasa menjangkau ketiga band:", 12.5, INK, bold=True))
    b.append(text(22, 322, "metadata (JSON) + teks isi (teks bebas) + OCR on-screen (tak terstruktur).", 12.5, MUT))
    b.append(rect(28, 348, 944, 54, SOFTB, stroke=LINE))
    b.append(text(44, 370, "Bacaan arah kanan: struktur menurun, biaya analisis naik, potensi insight justru justru paling besar", 12.5, w=150))
    b.append(text(44, 392, "di band tak terstruktur - karena di band tak terstruktur: tidak terbaca oleh hitungan sederhana saja.", 12.5, w=150))
    return b, H


# --------------------------------------------------------- 10. dictionary m3
def m3_dictionary():
    H = 600
    b = [rect(10, 46, W - 20, H - 66, WHITE, rx=14)]
    b.append(text(22, 30, "Lima langkah merancang field dictionary", 15, BLUE, bold=True))
    steps = [
        ("1", "Ambil 500 objek dari API", "sampel mentah, jangan diubah dahulu"),
        ("2", "Daftar semua field yang muncul", "field bersarang pakai jalur penuh: metrics.like"),
        ("3", "Isi tipe tiap field", "text / angka / timestamp / enum / objek"),
        ("4", "Tulis arti & missingness", "apa yang terjadi bila field tidak ada?"),
        ("5", "Pilih granularity baris", "satu baris per post, atau per event engagement"),
    ]
    for i, (n, t, d) in enumerate(steps):
        y = 88 + i * 100
        b.append('<circle cx="58" cy="%d" r="18" fill="%s"/>' % (y, BLUE))
        b.append(text(58, y + 5, n, 14, "#FFFFFF", bold=True, anchor="middle"))
        b.append(rect(96, y - 24, 380, 66, SOFTB, stroke=LINE, rx=8))
        b.append(text(112, y, t, 13, INK, bold=True, w=44))
        b.append(text(112, y + 24, d, 11.5, MUT, w=50))
        if i < 4:
            b.append(arrow(58, y + 20, 58, y + 66, color=BLUE))
    b.append(rect(500, 62, 468, 474, "#FFFFFF", stroke=MUT, sw=1.4, rx=8))
    b.append(text(514, 88, "POTONGAN KAMUS FIELD (contoh post Bluesky)", 12.5, BLUE, bold=True))
    head = ["FIELD", "TIPE", "CONTOH / ARTI"]
    body = [
        ["uri", "string", "at://.../post/3l... - id unik post"],
        ["created_at", "timestamp", "2026-10-25T02:14:05Z - waktu"],
        ["reply_count", "int", "23 - jumlah balasan"],
        ["repost_count", "int", "410 - posting ulang"],
        ["quote_count", "int", "95 - quote / kutipan"],
        ["author.id", "string", "did:plc:... - id pengguna"],
        ["record.text", "text", "isi post utama"],
        ["like_count", "int|null", "null - bisa tidak tersedia"],
    ]
    wx = [90, 106, 178]
    yy = 118
    for c, cx_ in zip(head, wx):
        b.append(text(514 + cx_, yy, c, 11, PLUM, bold=True))
    yy += 24
    for row in body:
        b.append(line_(514, yy - 12, 952, yy - 12, stroke=LINE, sw=0.6))
        for j, cell in enumerate(row):
            b.append(text(514 + wx[j], yy, cell, 10.5, INK, w=16 if j == 2 else 10))
        yy += 34
    b.append(text(514, yy + 24, "Aturan: kamus harus bisa dipakai mahasiswa lain", 11.5, MUT, w=84))
    b.append(text(514, yy + 44, "tanpa membaca kode - itulah ujian keterbacaannya.", 11.5, MUT, w=84))
    return b, H


# -------------------------------------------------------- 11. missingness m3
def m3_missingness():
    H = 520
    b = [rect(10, 46, W - 20, H - 66, WHITE, rx=14)]
    b.append(text(22, 30, "Tiga jenis missing pada data social media - dan cara mencatatnya", 15, BLUE, bold=True))
    kinds = [
        ("KONTEN TERHAPUS / DIEDIT", ORANGE,
         "Post dihapus atau admin menyembunyikan sebelum snapshot - missing 'tidak acak'.",
         "Risiko: sampel melewatkan konten paling kontroversial.",
         "Mitigasi: snapshot saat tayang + laporkan jendela snapshot."),
        ("FIELD TIDAK DIJAMIN ADA", PLUM,
         "Geotag hanya muncul bila pengguna memakai lokasi - pola berpola, bukan acak.",
         "Risiko: field kosong berimbang antar kelompok pengguna.",
         "Mitigasi: lapor persentase null per field."),
        ("JENDELA METRIK TERBATAS", GREEN,
         "Engagement log sering hanya diberikan untuk window waktu terbatas.",
         "Risiko: perbandingan antar-batch dibaca sebagai perbedaan asli.",
         "Mitigasi: tulis jendela snapshot di laporan; jangan campur batch."),
    ]
    for i, (name, stroke, defi, risik, mit) in enumerate(kinds):
        y = 66 + i * 108
        b.append(rect(26, y, 944, 94, SOFTB, stroke=LINE, rx=8))
        b.append(rect(26, y, 250, 94, SOFTA, stroke=stroke, sw=1.6, rx=8))
        b.append(text(44, y + 34, name, 13, stroke, bold=True, w=28))
        b.append(text(296, y + 24, defi, 12, INK, w=104))
        b.append(text(296, y + 50, risik, 12, RED, w=104))
        b.append(text(296, y + 76, mit, 12, GREEN, w=104))
    b.append(rect(26, 398, 944, 62, SOFTG, stroke=GREEN, rx=8))
    b.append(text(44, 422, "Aturan buku ini: setiap field di kamus harus menyebut kejadian missing yang mungkin -", 12.5, w=150))
    b.append(text(44, 444, "null yang sah, field yang bisa absent, atau metrik yang hanya diberikan per window waktu.", 12.5, w=150))
    return b, H


FIGS = [
    ("figm2-ecosystem", m2_ecosystem),
    ("figm2-affordance", m2_affordance),
    ("figm2-feed", m2_feed),
    ("figm2-openness", m2_openness),
    ("figm2-timeline", m2_timeline),
    ("figm2-metrics", m2_metrics),
    ("figm3-taxonomy", m3_taxonomy),
    ("figm3-anatomy", m3_anatomy),
    ("figm3-spectrum", m3_spectrum),
    ("figm3-dictionary", m3_dictionary),
    ("figm3-missingness", m3_missingness),
]

for name, fn in FIGS:
    body, h = fn()
    save(name, body, h)
print("done")

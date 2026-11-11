# -*- coding: utf-8 -*-
"""Generate 6 vector (SVG) figures for Buku Ajar Materi 1: Fondasi & Ruang Lingkup SMA."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
OK = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"]
BLUE, ORANGE, GREEN, YELLOW, GRAY = OK[4], OK[5], OK[2], OK[3], "#4D4D4D"
FONT = "Helvetica, Arial, 'DejaVu Sans', sans-serif"


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def txt(x, y, s, size=13, color="#111111", weight="normal", anchor="start", ls=0):
    return ('<text x="%s" y="%s" font-family="%s" font-size="%s" fill="%s" '
            'font-weight="%s" text-anchor="%s" letter-spacing="%s">%s</text>'
            % (x, y, FONT, size, color, weight, anchor, ls, esc(s)))


def rect(x, y, w, h, fill="#ffffff", stroke="#8C8C8C", rx=8, sw=1.6, dash=None, op=1.0):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s opacity="%s"/>' % (x, y, w, h, rx, fill, stroke, sw, d, op))


def circle(cx, cy, r, fill, stroke, sw=1.6, op=0.22):
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s" opacity="%s"/>'
            % (cx, cy, r, fill, stroke, sw, op))


def line(x1, y1, x2, y2, stroke="#4D4D4D", sw=1.6, dash=None, marker=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    m = ' marker-end="url(#%s)"' % marker if marker else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s%s/>'
            % (x1, y1, x2, y2, stroke, sw, d, m))


def poly(points, fill="none", stroke="#4D4D4D", sw=1.6, marker=None):
    p = " ".join("%s,%s" % (a, b) for a, b in points)
    m = ' marker-end="url(#%s)"' % marker if marker else ""
    return '<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>' % (p, fill, stroke, sw, m)


def box(x, y, w, h, title, lines, fill="#FFFFFF", stroke=GRAY, tcol="#111111", lsize=11, tsize=13, pad=10):
    """Rounded box with a bold title and wrapped body lines."""
    out = [rect(x, y, w, h, fill, stroke, rx=10)]
    ty = y + 22
    out.append(txt(x + pad, ty, title, size=tsize, weight="bold", color=tcol))
    for i, ln in enumerate(lines):
        out.append(txt(x + pad, ty + 16 + i * (lsize + 4), ln, size=lsize, color="#333333"))
    return "".join(out)


def arrow(x1, y1, x2, y2, color="#4D4D4D", sw=2.0, dash=None):
    return line(x1, y1, x2, y2, stroke=color, sw=sw, dash=dash, marker="ah")


def svg_open(w, h, title):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" width="100%%" '
            'role="img" aria-label="%s" font-family="%s">\n'
            '<defs><marker id="ah" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">'
            '<path d="M0,0 L10,4 L0,8 z" fill="#4D4D4D"/></marker></defs>\n'
            '<rect x="0" y="0" width="%s" height="%s" fill="#FFFFFF"/>\n'
            % (w, h, esc(title), FONT, w, h))


# ----------------------------------------------------------------- FIGURE 1
def fig_discipline():
    W, H = 940, 470
    p = [svg_open(W, H, "Posisi Social Media Analytics dalam peta disiplin ilmu")]
    p.append(txt(470, 34, "Gambar 1. Posisi Social Media Analytics (SMA) dalam peta disiplin",
                 size=15, weight="bold", anchor="middle"))
    p.append(txt(470, 54, "SMA berada di irisan empat ruang ilmu; tiap disiplin membawa pertanyaan, teori, dan metode yang berbeda",
                 size=11.5, color="#555555", anchor="middle"))
    cx, cy = 470, 250
    p.append(circle(cx - 150, cy + 60, 150, GREEN, GREEN, op=0.13))
    p.append(circle(cx + 150, cy + 60, 150, ORANGE, ORANGE, op=0.13))
    p.append(circle(cx - 60, cy - 110, 135, BLUE, BLUE, op=0.13))
    p.append(circle(cx + 120, cy - 120, 130, YELLOW, YELLOW, op=0.13))
    # labels on the four circles
    p.append(txt(318, 190, "Ilmu Komunikasi", size=12.5, weight="bold", color="#0A5C46", anchor="middle"))
    p.append(txt(318, 208, "framing, opini publik,", size=10.5, color="#0A5C46", anchor="middle"))
    p.append(txt(318, 223, "agenda setting, efek media", size=10.5, color="#0A5C46", anchor="middle"))
    p.append(txt(690, 190, "Riset Pasar & Marketing", size=12.5, weight="bold", color="#8A3D00", anchor="middle"))
    p.append(txt(690, 208, "social listening, brand health,", size=10.5, color="#8A3D00", anchor="middle"))
    p.append(txt(690, 223, "comms planning", size=10.5, color="#8A3D00", anchor="middle"))
    p.append(txt(370, 130, "Ilmu Komputer / NLP", size=12.5, weight="bold", color="#0A4C7A", anchor="middle"))
    p.append(txt(370, 148, "klasifikasi teks, topic model,", size=10.5, color="#0A4C7A", anchor="middle"))
    p.append(txt(370, 163, "graf interaksi, LLM", size=10.5, color="#0A4C7A", anchor="middle"))
    p.append(txt(640, 130, "Statistika & Pembelajaran Mesin", size=12.5, weight="bold", color="#7A6A00", anchor="middle"))
    p.append(txt(640, 148, "inferensi, prediksi, evaluasi,", size=10.5, color="#7A6A00", anchor="middle"))
    p.append(txt(640, 163, "validitas & reliabilitas", size=10.5, color="#7A6A00", anchor="middle"))
    # centre
    p.append(rect(cx - 108, cy - 38, 216, 84, "#FFFFFF", "#111111", rx=12, sw=2.2))
    p.append(txt(cx, cy - 14, "SOCIAL MEDIA", size=15, weight="bold", anchor="middle"))
    p.append(txt(cx, cy + 8, "ANALYTICS", size=15, weight="bold", anchor="middle"))
    p.append(txt(cx, cy + 28, "data platform Bahasa Indonesia + global", size=9.5, color="#555555", anchor="middle"))
    # quadrant one-liners
    p.append(box(60, 300, 250, 120, "Yang dibawa Komunikasi",
                 ["- Apa yang sedang dibicarakan", "- Siapa pembicara & framing-nya",
                  "- Bagaimana narasi menyebar", "- Dampak opini & agenda"],
                 fill="#F3FBF6", stroke=GREEN, lsize=10.5))
    p.append(box(630, 300, 250, 120, "Yang dibawa Marketing",
                 ["- Kesehatan merek & kampiye", "- Audiens & segmen",
                  "- Efektivitas konten", "- Kebutuhan vs. suara pasar"],
                 fill="#FFF7EC", stroke=ORANGE, lsize=10.5))
    p.append(box(60, 60, 250, 96, "Yang dibawa Komputasi",
                 ["- Pipeline otomatis & reproducible", "- Model untuk teks, gambar, video",
                  "- Skala: juta post", "- Tool: Python/R, LLM"],
                 fill="#F2F8FD", stroke=BLUE, lsize=10.5))
    p.append(box(630, 60, 250, 96, "Yang dibawa Statistika",
                 ["- Sampling frame & bias", "- Uji hipotesis & prediksi",
                  "- Metrik evaluasi adil", "- Ketidakpastian"],
                 fill="#FCFBE8", stroke=YELLOW, lsize=10.5))
    open(os.path.join(OUT, "fig1-discipline.svg"), "w", encoding="utf-8").write("".join(p) + "</svg>")


# ----------------------------------------------------------------- FIGURE 2
def fig_lifecycle():
    W, H = 1000, 300
    p = [svg_open(W, H, "Siklus hidup data Social Media Analytics")]
    p.append(txt(500, 30, "Gambar 2. Siklus hidup data SMA: enam tahap, satu putaran iteratif",
                 size=15, weight="bold", anchor="middle"))
    stages = [
        ("1. Rumusan pertanyaan", ["Buat pertanyaan terukur:", "siapa, apa, kapan,", "dibandingkan dengan apa"]),
        ("2. Akses & akuisisi", ["API resmi / sumber sah", "Kuota, filter, sampling", "frame, arsip + checksum"]),
        ("3. Preprocessing", ["Normalisasi, dedup,", "bot filter, bahasa &", "code-mixing, anonimisasi"]),
        ("4. Analisis / model", ["Sentimen, topik, jaringan,", "engagement, multimodal,", "evaluasi metrik"]),
        ("5. Visualisasi", ["Graf, tren, dashboard,", "chart jujur +", "ketidakpastian"]),
        ("6. Interpretasi & preservasi", ["Insight + keterbatasan", "Publikasi & replicasi", "Data & kode disimpan"]),
    ]
    bw, bh, gap = 148, 118, 15
    x0 = 22
    y = 66
    for i, (t, ls) in enumerate(stages):
        x = x0 + i * (bw + gap)
        p.append(box(x, y, bw, bh, t, ls, fill=["#F2F8FD", "#FFF7EC", "#F3FBF6", "#FCFBE8", "#F7F2FA", "#F5F5F5"][i],
                     stroke="#8C8C8C", tsize=11.5, lsize=9.5, pad=8))
        if i < 5:
            p.append(arrow(x + bw + 1, y + bh / 2, x + bw + gap - 2, y + bh / 2))
    # feedback loop
    y2 = y + bh
    p.append(txt(500, y2 + 26, "Umpan balik: temuan baru memperbaiki rumusan pertanyaan, sampling frame, atau codebook label",
                 size=11, color="#555555", anchor="middle"))
    xs, xe = x0 + 5 * (bw + gap) + bw / 2, x0 + bw / 2
    p.append(poly([(xe + 26, y2 + 10), (xe, y2 + 34), (xe - 26, y2 + 10)], fill="none", stroke="#8C8C8C"))
    p.append(line(xs, y2 + 10, xs, y2 + 30, stroke="#8C8C8C", dash="4 4"))
    p.append(line(xs, y2 + 30, xe + 26, y2 + 30, stroke="#8C8C8C", dash="4 4"))
    p.append(line(xe + 26, y2 + 30, xe + 26, y2 + 12, stroke="#8C8C8C", dash="4 4"))
    p.append(txt(500, y2 + 58, "Tahap yang paling sering disalahartikan mahasiswa: 2 (sampling frame) dan 6 (interpretasi) — bukan tahap 4",
                 size=10.5, color="#8A3D00", anchor="middle"))
    open(os.path.join(OUT, "fig2-lifecycle.svg"), "w", encoding="utf-8").write("".join(p) + "</svg>")


# ----------------------------------------------------------------- FIGURE 3
def fig_maturity():
    W, H = 990, 400
    p = [svg_open(W, H, "Tangga maturitas analitik: deskriptif, diagnostik, prediktif, preskriptif")]
    p.append(txt(495, 30, "Gambar 3. Tangga maturitas analitik (descriptive → prescriptive)",
                 size=15, weight="bold", anchor="middle"))
    p.append(txt(495, 50, "Semakin ke kanan, nilai naik tetapi biaya data, asumsi model, dan risiko salah-tafsir juga naik",
                 size=11.5, color="#555555", anchor="middle"))
    steps = [
        ("DESKRIPTIF", "Apa yang terjadi?",
         ["Hitungan, tren, porsi,", "perbandingan antar-platform"],
         "Contoh: 62% post negatif", "Tools: API, pandas, chart", "#F2F8FD", BLUE),
        ("DIAGNOSTIK", "Mengapa terjadi?",
         ["Sub-grup, aspek, peristiwa", "pemicu (crash, kebijakan)"],
         "Contoh: lonjakan minggu 3", "Tools: ABSA, topic model", "#F3FBF6", GREEN),
        ("PREDIKTIF", "Apa yang akan terjadi?",
         ["Prediksi engagement,", "viralitas, churn, tren"],
         "Contoh: post akan trending", "Tools: ML/LLM, time series", "#FCFBE8", YELLOW),
        ("PRESKRIPTIF", "Apa yang harus dilakukan?",
         ["Rekomendasi aksi,", "alokasi anggaran konten"],
         "Contoh: geser 30% budget", "Tools: optimasi + evaluasi", "#FFF7EC", ORANGE),
    ]
    bw, bh = 228, 205
    x0, y = 30, 62
    for i, (t, q, ls, ex, tl, fill, st) in enumerate(steps):
        x = x0 + i * (bw + 13)
        yb = y + (i * 8)
        p.append(rect(x, yb, bw, bh, fill, st, rx=10, sw=1.8))
        p.append(txt(x + bw / 2, yb + 22, t, size=13.5, weight="bold", anchor="middle", color=st))
        p.append(txt(x + bw / 2, yb + 40, q, size=11, anchor="middle", color="#111111"))
        p.append(line(x + 12, yb + 50, x + bw - 12, yb + 50, stroke="#C8C8C8", sw=1))
        for j, ln in enumerate(ls):
            p.append(txt(x + 14, yb + 70 + j * 16, ln, size=10.5, color="#333333"))
        p.append(txt(x + 14, yb + 118, ex, size=10.5, color=st, weight="bold"))
        p.append(txt(x + 14, yb + 134, tl, size=10, color="#555555"))
        p.append(txt(x + 14, yb + 158, "Bukti: " + ["angka + rentang", "bandingan terkontrol", "uji out-of-sample", "uji dampak"][i],
                     size=9.8, color="#777777"))
        if i < 3:
            p.append(arrow(x + bw + 1, yb + bh / 2, x + bw + 11, yb + bh / 2 - 4))
    p.append(txt(495, H - 34, "Aturan praktik: jangan pernah naik tingkat tanpa bukti di tingkat bawah. Insight preskriptif tanpa diagnostik = opini.",
                 size=11.5, weight="bold", color="#8A3D00", anchor="middle"))
    open(os.path.join(OUT, "fig3-maturity.svg"), "w", encoding="utf-8").write("".join(p) + "</svg>")


# ----------------------------------------------------------------- FIGURE 4
def fig_units():
    W, H = 1000, 430
    p = [svg_open(W, H, "Unit analisis dalam Social Media Analytics")]
    p.append(txt(500, 30, "Gambar 4. Unit analisis menentukan pertanyaan yang bisa dijawab",
                 size=15, weight="bold", anchor="middle"))
    p.append(txt(500, 50, "Dari kelompok besar ke individu; setiap turun satu tingkat menambah kolom data tetapi menyempitkan generalisasi",
                 size=11.5, color="#555555", anchor="middle"))
    rows = [
        ("PLATFORM / EKOSISTEM", "Perbandingan lintas platform", ["Adakah perbedaan narasi antar aplikasi?", "Platform mana yang layak diaudit rutin?"], BLUE),
        ("CONVERSASI / KAMPANYE", "Thread, tagar, topik, batch", ["Bagaimana isu X berkembang 7 hari?", "Topik apa yang muncul pasca peristiwa?"], GREEN),
        ("POST / KONTEN", "Teks, gambar, video + metrik", ["Format apa yang paling disimpan?", "Hook seperti apa menahan penonton?"], YELLOW),
        ("PENGGUNA / AKUN", "Profil, riwayat, demografi terinferensi", ["Siapa pembicara teraktif & apa latarnya?", "Akun mana yang tampak otomatis?"], ORANGE),
        ("JARINGAN / KOMUNITAS", "Graf ikut-ikuti, balas, sebut, ko-unggah", ["Siapa jembatan antar kubu?", "Adakah klaster terkoordinasi?"], "#7A4FA0"),
    ]
    y = 66
    h = 62
    for i, (t, sub, qs, col) in enumerate(rows):
        x = 30 + i * 190
        p.append(rect(x, y, 176, h + 8, "#FFFFFF", col, rx=10, sw=1.8))
        p.append(txt(x + 12, y + 20, t, size=11.5, weight="bold", color=col))
        p.append(txt(x + 12, y + 36, sub, size=9.8, color="#555555"))
        for j, q in enumerate(qs):
            p.append(txt(x + 12, y + 52 + j * 13, "• " + q, size=9.2, color="#333333"))
        if i < 4:
            p.append(arrow(x + 178, y + 34, x + 188, y + 34))
    p.append(txt(500, y + h + 40, "Contoh satu unit data — satu post TikTok/X — dapat diurai menjadi komponen berikut:",
                 size=11.5, weight="bold", anchor="middle"))
    # anatomy of a post
    ax, ay, aw, ah = 40, y + h + 52, 920, 200
    p.append(rect(ax, ay, aw, ah, "#FBFBFD", "#8C8C8C", rx=10, sw=1.4))
    p.append(txt(ax + 14, ay + 22, "Anatomi satu post: empat lapis data", size=12.5, weight="bold"))
    layers = [
        ("Lapis 1 — Isi (content)", "Teks, transkrip audio, teks on-screen (OCR), objek terlihat (CLIP), label & mention", BLUE),
        ("Lapis 2 — Metadata", "Waktu, zona waktu, bahasa, lokasi, perangkat, jumlah follower, status verifikasi", GREEN),
        ("Lapis 3 — Interaksi (engagement)", "Like, komentar, share, save, watch time, completion rate, klik profil", YELLOW),
        ("Lapis 4 — Relasi", "Reply ke post siapa, mention siapa, bagian dari graf follow/co-post", ORANGE),
    ]
    for i, (t, d, col) in enumerate(layers):
        yy = ay + 44 + i * 36
        p.append(rect(ax + 16, yy - 16, 190, 26, "#FFFFFF", col, rx=6, sw=1.4))
        p.append(txt(ax + 22, yy, t, size=11, weight="bold", color=col))
        p.append(txt(ax + 218, yy, d, size=10.5, color="#333333"))
    open(os.path.join(OUT, "fig4-units.svg"), "w", encoding="utf-8").write("".join(p) + "</svg>")


# ----------------------------------------------------------------- FIGURE 5
def fig_openness():
    W, H = 1000, 400
    p = [svg_open(W, H, "Lanskap keterbukaan data platform 2026")]
    p.append(txt(500, 30, "Gambar 5. Lanskap keterbukaan data platform (indikatif, 2026)",
                 size=15, weight="bold", anchor="middle"))
    p.append(txt(500, 50, "Skor keterbukaan akses riset 0–10: open protocol/terbuka (hijau) · API resmi terbatas (biru) · gated/berbayar (oranye)",
                 size=11.5, color="#555555", anchor="middle"))
    data = [
        ("Bluesky (AT Protocol / Jetstream)", 9.0, GREEN, "Terbuka, firehose penuh, tanpa kuota akademik"),
        ("Reddit API", 7.0, GREEN, "Terbuka dengan rate limit & kebijakan 2023"),
        ("YouTube Data API", 7.0, GREEN, "Terbuka dengan kuota harian"),
        ("TikTok Research API", 5.5, BLUE, "Terbatas: pendaftaran & tujuan riset"),
        ("X / Twitter API v2", 4.0, ORANGE, "Berbayar; akses akademik gratis dihapus 2023"),
        ("Instagram / Threads (Meta)", 3.0, ORANGE, "Gated: eligibility institusi akademik"),
        ("Facebook (Meta Content Library)", 2.5, ORANGE, "Gated; enclave riset mulai berbayar 2026"),
    ]
    maxv = 10.0
    x0, y0, bh = 330, 74, 26
    for i, (name, v, col, note) in enumerate(data):
        y = y0 + i * (bh + 6)
        p.append(txt(x0 - 12, y + 17, name, size=11.5, anchor="end", color="#111111"))
        p.append(rect(x0, y, int(520 * (v / maxv)), bh, col, col, rx=4, sw=1.0, op=0.85))
        p.append(txt(x0 + 520 * (v / maxv) + 8, y + 17, "%.1f" % v, size=11, weight="bold", color=col))
        p.append(txt(x0 + 12, y0 + i * (bh + 6) + 17, note, size=9.8, color="#FFFFFF" if v > 6 else "#333333"))
    p.append(txt(500, H - 62, "Implikasi kurikulum: rancang studi yang tetap feasible saat akses tertutup — gunakan protokol terbuka,",
                 size=11.5, color="#111111", anchor="middle"))
    p.append(txt(500, H - 45, "arsip publik, metadata-first design, atau kolaborasi institusi ber-akses.", size=11.5, color="#111111", anchor="middle"))
    p.append(txt(500, H - 24, "Skor bersifat indikatif untuk tujuan pengajaran; verifikasi tier, kuota, dan biaya sebelum menyusun RPS.",
                 size=10, color="#8A3D00", anchor="middle"))
    open(os.path.join(OUT, "fig5-openness.svg"), "w", encoding="utf-8").write("".join(p) + "</svg>")


# ----------------------------------------------------------------- FIGURE 6
def fig_metrics_insight():
    W, H = 1120, 330
    p = [svg_open(W, H, "Dari data ke insight: piramida lima tingkat")]
    p.append(txt(560, 30, "Gambar 6. Dari metrik ke insight: lima tingkat, makin ke atas makin bernilai dan makin rawan",
                 size=15, weight="bold", anchor="middle"))
    p.append(txt(560, 50, "Contoh: kampanye minuman ringan di TikTok, minggu 1–4",
                 size=11.5, color="#555555", anchor="middle"))
    stages = [
        ("DATA", "12.480 post + 1.120 video", "API + scrape sah", BLUE, 150),
        ("METRIK", "3,1 juta view; 4,2% engagement", "hitung & agregasi", GREEN, 175),
        ("TEMUAN", "save/share naik 38% minggu 3", "bandingkan & uji", YELLOW, 200),
        ("INSIGHT", "konten 'cara bikin' mendorong save, bukan like", "hubungkan ke mekanisme", ORANGE, 225),
        ("REKOMENDASI", "alokasikan 60% budget ke format tutorial", "ambil keputusan + ukur dampaknya", "#8A2E5B", 250),
    ]
    x = 30
    for i, (t, ex, act, col, w) in enumerate(stages):
        y = 62
        p.append(rect(x, y, w, 96, "#FFFFFF", col, rx=10, sw=1.8))
        p.append(txt(x + w / 2, y + 22, t, size=13, weight="bold", anchor="middle", color=col))
        p.append(txt(x + w / 2, y + 44, ex, size=10, anchor="middle", color="#333333"))
        p.append(txt(x + w / 2, y + 62, act, size=9.5, anchor="middle", color="#777777"))
        if i < 4:
            p.append(arrow(x + w + 1, y + 48, x + w + 13, y + 48))
        x += w + 15
    # quality bar
    p.append(line(30, 190, 1090, 190, stroke="#CCCCCC", sw=1))
    p.append(txt(30, 208, "Kualitas naik", size=11, weight="bold", color="#0A5C46"))
    p.append(txt(1090, 208, "Risiko salah-tafsir naik", size=11, weight="bold", color="#8A3D00", anchor="end"))
    p.append(arrow(240, 186, 860, 172, color="#0A5C46", sw=1.6))
    p.append(txt(31, 240, "Jebakan umum:", size=11.5, weight="bold"))
    jebakan = [
        "Menyebut metrik sebagai insight (\"engagement naik\" = temuan, bukan insight)",
        "Naik tingkat tanpa bukti tingkat bawah (rekomendasi tanpa diagnostik)",
        "Menggeneralisasi satu platform ke seluruh platform",
        "Engagement dibaca sebagai sikap/opini tanpa validasi",
        "Tidak menyebut rentang ketidakpastian dan bias sampling",
    ]
    for i, j in enumerate(jebakan):
        p.append(txt(46, 262 + i * 16, "✗ " + j, size=10.8, color="#333333"))
    open(os.path.join(OUT, "fig6-insight.svg"), "w", encoding="utf-8").write("".join(p) + "</svg>")


for f in (fig_discipline, fig_lifecycle, fig_maturity, fig_units, fig_openness, fig_metrics_insight):
    f()
print("figures:", sorted(os.listdir(OUT)))

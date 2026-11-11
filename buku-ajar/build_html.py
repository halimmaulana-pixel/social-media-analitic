# -*- coding: utf-8 -*-
"""Build buku-ajar-materi-N.html from template + inline SVG figures (idempotent).

Usage: python3 build_html.py [N]   (default N=1)
"""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1

FIGS_M = {
    1: ["fig1-discipline", "fig2-lifecycle", "fig3-maturity",
        "fig4-units", "fig5-openness", "fig6-insight"],
    2: ["figm2-ecosystem", "figm2-affordance", "figm2-feed",
        "figm2-openness", "figm2-timeline", "figm2-metrics"],
    3: ["figm3-taxonomy", "figm3-anatomy", "figm3-spectrum",
        "figm3-dictionary", "figm3-missingness"],
    4: ["figm4-pipeline", "figm4-auth", "figm4-sampling",
        "figm4-pagination", "figm4-ratelimit", "figm4-checkpoint",
        "figm4-collectionlog"],
    5: ["figm5-ladder", "figm5-timeline", "figm5-mcl", "figm5-memo",
        "figm5-scraping", "figm5-pdp", "figm5-ethics"],
    6: ["figm6-pipeline", "figm6-minhash", "figm6-bot", "figm6-normalize",
        "figm6-overclean", "figm6-window", "figm6-funnel"],
    7: ["figm7-map", "figm7-worked"],
}

FIXES = [("td>Riset pengalaman", "<td>Riset pengalaman"),
         ("marut?", "marah?"),
         ("menjadi saturan konten utama", "menjadi satu satuan konten utama"),
         ("Konten siklik (trending)", "Isu siklikal (trending)"),
         ("tangkap kemiripan", "menangkap kemiripan"),
         ("sumbansih", "sumbangan"),
         ("satu tahap yang bocak merusak", "satu tahap yang bocor merusak"),
         ("Kualitas akhir rata-rata seluruh tahap",
          "Kualitas akhir hanya sebaik tahap terlemahnya"),
         ("salah satu kesalahan pewawancara terbesar bagi lulusan muda",
          "salah satu kesalahan yang paling sering ditemui pewawancara kerja pada lulusan muda"),
         ("sebelum mengiris klaim", "sebelum mengemukakan klaim"),
         ("Sum bangsih", "Sumbangan"),
         ("sumbansih ini", "sumbangan ini"),
         ("Conten sintetis", "Konten sintetis"),
         ("paska-2023", "pasca-2023"),
         ("Process memperoleh", "Proses memperoleh"),
         ("tandai", "tandai")]

def build(n=N):
    h = open(os.path.join(BASE, "buku-ajar-materi-%d.tmpl.html" % n), encoding="utf-8").read()
    css = open(os.path.join(BASE, "style.css"), encoding="utf-8").read()
    if "<!--STYLE-->" in h:
        h = h.replace("<!--STYLE-->", css)
    for a, b in FIXES:
        h = h.replace(a, b)
    figs = FIGS_M[n]
    for f in figs:
        svg = open(os.path.join(BASE, "figures", f + ".svg"), encoding="utf-8").read()
        svg = svg.replace('<svg ', '<svg preserveAspectRatio="xMidYMid meet" ', 1)
        ph = "<!--FIG:%s.svg-->" % f
        assert ph in h, "placeholder missing: %s" % ph
        m = re.search(re.escape(ph) + r'\s*<figcaption>.*?</figcaption>', h, re.S)
        if m:
            block = m.group(0)
            repl = "<figure>\n" + svg + "\n" + block[len(ph):].strip() + "\n</figure>"
            h = h.replace(block, repl)
        else:
            h = h.replace(ph, "<figure>\n%s\n</figure>" % svg)
    out = os.path.join(BASE, "buku-ajar-materi-%d.html" % n)
    open(out, "w", encoding="utf-8").write(h)
    return h, out

if __name__ == "__main__":
    h, out = build()
    from html.parser import HTMLParser
    VOID = {"br", "wbr", "img", "hr", "meta", "link", "input", "col"}
    stack, errs = [], []
    class P(HTMLParser):
        def handle_starttag(self, t, a):
            if t not in VOID:
                stack.append(t)
        def handle_endtag(self, t):
            if t in VOID:
                return
            if stack and stack[-1] == t:
                stack.pop()
            else:
                errs.append((t, stack[-3:]))
    P().feed(h)
    print("written:", out, "(materi %d)" % N)
    print("tables %d/%d · figures %d/%d · figcaptions %d/%d" % (
        h.count("<table"), h.count("</table>"),
        h.count("<figure"), h.count("</figure>"),
        h.count("<figcaption>"), h.count("</figcaption>")))
    print("h2 sections:", h.count("<h2>"), "· bytes:", len(h))
    print("tag errors:", errs[:6], "· unclosed:", stack[:6])

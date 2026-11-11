# -*- coding: utf-8 -*-
"""Convert buku-ajar-materi-1.html into an editable Markdown companion (v2)."""
import os, re, sys
from html.parser import HTMLParser

BASE = os.path.dirname(os.path.abspath(__file__))
VOID = {"br", "wbr", "img", "hr", "meta", "link", "input", "col"}
FIGMAP = ["fig1-discipline", "fig2-lifecycle", "fig3-maturity",
          "fig4-units", "fig5-openness", "fig6-insight",
          "figm2-ecosystem", "figm2-affordance", "figm2-feed",
          "figm2-openness", "figm2-timeline", "figm2-metrics",
          "figm3-taxonomy", "figm3-anatomy", "figm3-spectrum",
          "figm3-dictionary", "figm3-missingness",
          "figm4-pipeline", "figm4-auth", "figm4-sampling",
          "figm4-pagination", "figm4-ratelimit", "figm4-checkpoint",
          "figm4-collectionlog",
          "figm5-ladder", "figm5-timeline", "figm5-mcl", "figm5-scraping",
          "figm5-pdp", "figm5-ethics", "figm5-memo",
          "figm6-pipeline", "figm6-minhash", "figm6-bot",
          "figm6-normalize", "figm6-overclean", "figm6-window",
          "figm6-funnel", "figm7-map", "figm7-worked"]
FIGKEY_M = {
    1: {"irisan": "fig1-discipline", "siklus": "fig2-lifecycle",
        "keterbukaan": "fig5-openness", "maturitas": "fig3-maturity",
        "unit analisis": "fig4-units", "insight": "fig6-insight"},
    2: {"kawasan": "figm2-ecosystem", "matriks affordance": "figm2-affordance",
        "logika feed": "figm2-feed", "tangga": "figm2-openness",
        "timeline kebijakan": "figm2-timeline", "empat definisi": "figm2-metrics"},
    3: {"taksonomi unit data": "figm3-taxonomy", "anatomi satu objek": "figm3-anatomy",
        "spektrum struktur": "figm3-spectrum", "field dictionary": "figm3-dictionary",
        "tiga jenis missing": "figm3-missingness", "jenis missing": "figm3-missingness"},
    4: {"figm4 pipeline": "figm4-pipeline", "figm4 auth": "figm4-auth",
        "figm4 sampling": "figm4-sampling", "figm4 pagination": "figm4-pagination",
        "figm4 ratelimit": "figm4-ratelimit", "figm4 checkpoint": "figm4-checkpoint",
        "figm4 collectionlog": "figm4-collectionlog"},
    5: {"tangga": "figm5-ladder", "timeline": "figm5-timeline",
        "meta content library": "figm5-mcl", "enam blok": "figm5-memo",
        "memo kelayakan": "figm5-memo", "pohon keputusan": "figm5-scraping",
        "dua kolom": "figm5-pdp", "tiga lingkar": "figm5-ethics",
        "publik ≠ boleh": "figm5-ethics"},
    6: {"peta jalan preprocessing": "figm6-pipeline", "pipeline": "figm6-pipeline",
        "dedup dekat": "figm6-minhash", "minhash": "figm6-minhash",
        "enam heuristik": "figm6-bot", "bot": "figm6-bot",
        "enam langkah": "figm6-normalize", "normalisasi": "figm6-normalize",
        "membersihkan berlebihan": "figm6-overclean", "stopword": "figm6-overclean",
        "jendela waktu": "figm6-window", "funnel": "figm6-funnel"},
    7: {"peta hubungan": "figm7-map", "contoh soal diagnosis": "figm7-worked",
        "lima cacat": "figm7-worked"},
}
MAT = int(sys.argv[1]) if len(sys.argv) > 1 else 1
FIGKEY = FIGKEY_M[MAT]


class Node:
    def __init__(self, tag, attrs=None):
        self.tag, self.attrs, self.children = tag, dict(attrs or []), []
    def cls(self):
        return self.attrs.get("class", "")


class Build(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("body")
        self.stack = [self.root]
    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs)
        self.stack[-1].children.append(n)
        if tag not in VOID:
            self.stack.append(n)
    def handle_endtag(self, tag):
        if tag in VOID:
            return
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break
    def handle_data(self, data):
        d = re.sub(r"\s+", " ", data)
        if d.strip():
            lead = " " if d[:1] == " " else ""
            trail = " " if d[-1:] == " " else ""
            self.stack[-1].children.append(lead + d.strip() + trail)


def kids(node):
    """Inline markdown of a node's subtree."""
    parts = []

    def emit(c):
        if isinstance(c, str):
            parts.append(c)
            return
        t = c.tag
        if t in ("b", "strong"):
            parts.append("**" + kids(c) + "**")
        elif t in ("i", "em"):
            parts.append("*" + kids(c) + "*")
        elif t == "code":
            parts.append("`" + kids(c) + "`")
        elif t == "br":
            parts.append("  \n")
        else:
            for x in c.children:
                emit(x)

    for c in node.children:
        emit(c)
    # join fragments with a space so formatting boundaries stay readable
    PUNCT = ".,;:!?)]}”’%("
    out = []
    for p in parts:
        if p == "  \n":
            out.append(p)
            continue
        if (out and not out[-1].endswith((" ", "\n")) and not p.startswith((" ", "\n"))
                and p[0] not in PUNCT and out[-1][-1] != "("):
            out.append(" " + p)
        else:
            out.append(p)
    return re.sub(r"\s+", " ", "".join(out)).strip()


def find(node, tag):
    for c in node.children:
        if not isinstance(c, str) and c.tag == tag:
            return c
    return None


def block(node):
    """Return list of markdown block lines for one node."""
    if isinstance(node, str):
        return [node] if node else []
    t, cls = node.tag, node.cls()
    if t in ("h1", "h2", "h3", "h4"):
        return ["", "#" * int(t[1]) + " " + kids(node), ""]
    if t == "p":
        txt = kids(node)
        return [txt, ""] if txt else []
    if t == "table":
        out = []
        cap = find(node, "caption")
        if cap:
            out += ["**" + kids(cap) + "**", ""]
        rows = []
        for sect in ("thead", "tbody"):
            s = find(node, sect)
            if s:
                for tr in [c for c in s.children if not isinstance(c, str)]:
                    rows.append([kids(c) or "—" for c in tr.children
                                 if not isinstance(c, str) and c.tag in ("th", "td")])
        if rows:
            w = max(len(r) for r in rows)
            rows = [r + [""] * (w - len(r)) for r in rows]
            out.append("| " + " | ".join(rows[0]) + " |")
            out.append("|" + "|".join([" --- "] * w) + "|")
            for r in rows[1:]:
                out.append("| " + " | ".join(r) + " |")
            out.append("")
        return out
    if t in ("ul", "ol"):
        items = [c for c in node.children if not isinstance(c, str) and c.tag == "li"]
        if not items:
            return []
        out = []
        for i, li in enumerate(items):
            txt = kids(li).replace("|", "\\|")
            nested = [x for x in li.children if not isinstance(x, str) and x.tag in ("ul", "ol")]
            if t == "ol":
                out.append("%d. %s" % (i + 1, txt))
            else:
                out.append("- " + txt)
            for nt in nested:
                for ln in block(nt):
                    out.append("    " + ln)
        out.append("")
        return out
    if t == "figure":
        cap = find(node, "figcaption")
        svg = find(node, "svg")
        alt = (svg.attrs.get("aria-label", "Gambar") if svg else "Gambar")
        n = FIGMAP[FIGIDX[0]] if FIGIDX[0] < len(FIGMAP) else "fig"
        FIGIDX[0] += 1
        # map by aria-label, because document order != filename order
        key = alt.lower()
        for kw, fn in FIGKEY.items():
            if kw in key:
                n = fn
                break
        out = ["", "![%s](figures/%s.svg)" % (alt, n), ""]
        if cap:
            out += [kids(cap), ""]
        return out
    if t in ("style", "script"):
        return []
    if "box" in cls.split():
        head, body, buf = None, [], []
        def flush():
            if buf:
                fake = Node("div")
                fake.children = list(buf)
                txt = kids(fake)
                if txt:
                    body.append(txt)
                    body.append("")
                buf.clear()
        for c in node.children:
            if isinstance(c, str):
                buf.append(c)
                continue
            if c.tag == "span" and "h" in c.cls().split():
                flush()
                head = kids(c)
                continue
            if c.tag in ("ul", "ol", "table", "p", "figure"):
                flush()
                body += block(c)
            else:
                buf.append(c)
        flush()
        lines = ["> **" + (head or "Catatan") + "**  "]
        for ln in body:
            if ln == "":
                lines.append(">")
            else:
                lines.append("> " + ln)
        lines.append("")
        return lines
    out = []
    for c in node.children:
        out += block(c)
    return out


FIGIDX = [[0, 6, 12, 17, 24, 31, 33][min(MAT, 7) - 1]]


def main():
    html = open(os.path.join(BASE, "buku-ajar-materi-%d.html" % MAT), encoding="utf-8").read()
    b = Build()
    b.feed(html)
    md = []
    for c in b.root.children:
        md += block(c)
    txt = re.sub(r"\n{3,}", "\n\n", "\n".join(md)).strip() + "\n"
    path = os.path.join(BASE, "buku-ajar-materi-%d.md" % MAT)
    open(path, "w", encoding="utf-8").write(txt)
    print("written:", path, "| bytes:", len(txt))
    print("h2:", txt.count("\n## "), "· h3:", txt.count("\n### "),
          "· table rows:", txt.count("\n|"), "· figures:", txt.count("](figures/"),
          "· boxes:", txt.count("> **"))


if __name__ == "__main__":
    main()

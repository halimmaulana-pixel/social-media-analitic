#!/usr/bin/env python3
"""md_to_html.py: konversi tugas-mandiri-m1-6.md menjadi satu berkas HTML
dengan gaya yang sama seperti buku ajar (karena markupnya dikendalikan:
h1-h3, tabel, bold, blockquote, list, kode, hr)."""
import os
import re
import sys

SRC = "tugas-mandiri-m1-6.md"
DST = "tugas-mandiri-m1-6.html"

CSS = """
body{font-family:Georgia,'Times New Roman',serif;line-height:1.65;margin:0;background:#f8fafc;color:#1e293b}
main{max-width:860px;margin:0 auto;padding:28px 20px 60px}
h1{font-size:1.65em;margin:.2em 0 .1em}
h2{font-size:1.28em;margin-top:1.8em;border-bottom:2px solid #2563eb;padding-bottom:.25em}
h3{font-size:1.08em;margin-top:1.3em}
table{border-collapse:collapse;width:100%;margin:.9em 0;font-size:.92em;background:#fff}
th,td{border:1px solid #cbd5e1;padding:7px 9px;text-align:left;vertical-align:top}
th{background:#e2e8f0}
blockquote{border-left:4px solid #2563eb;background:#eff6ff;margin:1.1em 0;padding:10px 14px;border-radius:0 8px 8px 0}
code{font-family:'DejaVu Sans Mono',monospace;font-size:.88em;background:#eef2ff;padding:1px 5px;border-radius:4px}
pre{background:#0f172a;color:#e2e8f0;padding:12px 14px;border-radius:8px;overflow-x:auto;font-size:.85em}
pre code{background:none;color:inherit;padding:0}
strong{color:#0f172a}
ol,ul{padding-left:1.4em}
li{margin:.3em 0}
hr{border:none;border-top:1px solid #cbd5e1;margin:2em 0}
@media print{body{background:#fff}main{padding:0}}
"""


def inline(s):
    s = (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def rows_of(lines):
    out = []
    for ln in lines:
        if ln.strip().startswith("|"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            out.append(cells)
    return out


def main():
    import sys
    global SRC, DST
    if len(sys.argv) > 1:
        SRC = sys.argv[1]
        DST = os.path.splitext(SRC)[0] + ".html"
    md = open(SRC, encoding="utf-8").read().split("\n")
    body = []
    i, n = 0, len(md)
    while i < n:
        ln = md[i]
        t = ln.strip()
        if t.startswith("# ") and not t.startswith("## "):
            body.append("<h1>%s</h1>" % inline(t[2:]))
            i += 1
        elif t.startswith("## "):
            body.append("<h2>%s</h2>" % inline(t[3:]))
            i += 1
        elif t.startswith("### "):
            body.append("<h3>%s</h3>" % inline(t[4:]))
            i += 1
        elif t == "---":
            body.append("<hr/>")
            i += 1
        elif t.startswith("```"):
            i += 1
            code = []
            while i < n and not md[i].strip().startswith("```"):
                code.append(md[i])
                i += 1
            i += 1
            body.append("<pre><code>%s</code></pre>" %
                        ("\n".join(code).replace("&", "&amp;")
                         .replace("<", "&lt;").replace(">", "&gt;")))
        elif t.startswith("|"):
            tbl = []
            while i < n and md[i].strip().startswith("|"):
                tbl.append(md[i])
                i += 1
            rr = rows_of(tbl)
            rr = [r for r in rr if not all(set(c) <= set("-: ") for c in r)]
            if rr:
                body.append("<table>")
                for j, r in enumerate(rr):
                    tag = "th" if j == 0 else "td"
                    body.append("<tr>" + "".join(
                        "<%s>%s</%s>" % (tag, inline(c), tag) for c in r) + "</tr>")
                body.append("</table>")
        elif t.startswith(">"):
            quote = []
            while i < n and md[i].strip().startswith(">"):
                quote.append(md[i].strip()[1:].strip())
                i += 1
            body.append("<blockquote>%s</blockquote>" % inline(" ".join(quote)))
        elif re.match(r"^\d+\.\s", t):
            items = []
            while i < n and re.match(r"^\d+\.\s", md[i].strip()):
                items.append("<li>%s</li>" % inline(re.sub(r"^\d+\.\s", "", md[i].strip())))
                i += 1
            body.append("<ol>" + "".join(items) + "</ol>")
        elif t.startswith("- "):
            items = []
            while i < n and md[i].strip().startswith("- "):
                items.append("<li>%s</li>" % inline(md[i].strip()[2:]))
                i += 1
            body.append("<ul>" + "".join(items) + "</ul>")
        elif t == "":
            i += 1
        else:
            para = [t]
            i += 1
            while i < n and md[i].strip() and not re.match(r"^(#|\||>|- |\d+\.|---)", md[i].strip()):
                para.append(md[i].strip())
                i += 1
            body.append("<p>%s</p>" % inline(" ".join(para)))
    html = ("<!DOCTYPE html><html lang='id'><head><meta charset='utf-8'/>"
            "<meta name='viewport' content='width=device-width, initial-scale=1'/>"
            "<title>Tugas Mandiri Social Media Analytics</title><style>%s</style></head>"
            "<body><main>%s</main></body></html>" % (CSS, "".join(body)))
    open(DST, "w", encoding="utf-8").write(html)
    print("written", DST, len(html), "bytes")


if __name__ == "__main__":
    main()

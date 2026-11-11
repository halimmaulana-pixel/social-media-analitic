#!/usr/bin/env python3
"""bsky_collect.py: kolektor Bluesky memakai pustaka standar Python saja.

Contoh pakai:
    python3 bsky_collect.py --actor detikcom.bsky.social --limit 50 --outdir data/bluesky

Endpoint yang dipakai: app.bsky.feed.getAuthorFeed (publik, tanpa login).
Keluaran: raw JSONL per post, CSV bersih, collection log, dan berkas SHA-256.
"""
import argparse
import csv
import hashlib
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

BASE = "https://public.api.bsky.app/xrpc/"
USER_AGENT = "sma-lab/1.0 (educational collection exercise)"
SLEEP = 1.5          # jeda sopan antar permintaan, dalam detik
MAX_PAGES = 40       # pengaman agar loop tidak berjalan tanpa akhir


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fetch_page(actor, cursor):
    params = {"actor": actor, "limit": 100, "filter": "posts_no_replies"}
    if cursor:
        params["cursor"] = cursor
    url = BASE + "app.bsky.feed.getAuthorFeed?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                               "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8")), dict(resp.headers)


def row_of(item):
    post = item.get("post", {})
    rec = post.get("record", {})
    author = post.get("author", {})
    return {
        "uri": post.get("uri", ""),
        "created_at": rec.get("createdAt", ""),
        "text": (rec.get("text") or "").replace("\n", " "),
        "like_count": post.get("likeCount", 0),
        "reply_count": post.get("replyCount", 0),
        "repost_count": post.get("repostCount", 0),
        "author_handle": author.get("handle", ""),
        "is_reshare": "iya" if "reasonRepost" in item.get("reason", {}).get("$type", "") else "tidak",
        "reshared_by": item.get("reason", {}).get("by", {}).get("handle", ""),
        "captured_at": now_iso(),
    }


def write_outputs(outdir, actor, raw_items, rows, pages_report):
    os.makedirs(outdir, exist_ok=True)
    raw_path = os.path.join(outdir, "raw.jsonl")
    csv_path = os.path.join(outdir, "clean.csv")
    log_path = os.path.join(outdir, "collection_log.md")
    sum_path = os.path.join(outdir, "sha256.txt")

    with open(raw_path, "w", encoding="utf-8") as f:
        for it in raw_items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")

    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            w.writerow(r)

    checksums = []
    for p in (raw_path, csv_path):
        h = hashlib.sha256(open(p, "rb").read()).hexdigest()
        checksums.append("%s  %s" % (h, p))
    with open(sum_path, "w", encoding="utf-8") as f:
        f.write("\n".join(checksums) + "\n")

    last = pages_report[-1] if pages_report else {}
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("# Collection log\n\n")
        f.write("- Endpoint: app.bsky.feed.getAuthorFeed (publik, tanpa login)\n")
        f.write("- Aktor: %s\n" % actor)
        f.write("- Waktu selesai (UTC): %s\n" % now_iso())
        f.write("- Halaman terbaca: %d\n" % len(pages_report))
        f.write("- Baris terkumpul: %d\n" % len(rows))
        f.write("- Jeda antar permintaan: %.1f detik\n" % SLEEP)
        f.write("- Halaman terakhir berisi %s item. Jika jauh di bawah 100, "
                "curiga potongan diam-diam dan laporkan di sini.\n" % last.get("items"))
        f.write("- Checksum SHA-256: lihat sha256.txt\n\nRincian halaman:\n\n")
        for p in pages_report:
            f.write("- halaman %d: %d item, sisa kuota %s\n"
                    % (p["page"], p["items"], p["ratelimit_remaining"]))

    return raw_path, csv_path, log_path, sum_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--actor", required=True,
                    help="contoh: detikcom.bsky.social atau did:plc:...")
    ap.add_argument("--limit", type=int, default=500)
    ap.add_argument("--outdir", default="data/bluesky")
    args = ap.parse_args()

    rows, raw_items, pages_report = [], [], []
    cursor, page = None, 0
    failed = 0
    while len(rows) < args.limit and page < MAX_PAGES:
        try:
            data, headers = fetch_page(args.actor, cursor)
        except urllib.error.HTTPError as e:
            failed += 1
            pages_report.append({"page": page, "items": 0,
                                 "ratelimit_remaining": "HTTP %s" % e.code})
            if e.code in (429, 500, 502, 503):
                wait = 5 * failed
                print("ditolak %s, menunggu %d detik" % (e.code, wait))
                time.sleep(wait)
                if failed >= 3:
                    break
                continue
            print("galat permanen: %s. Aktor atau endpoint bermasalah." % e.code)
            break
        items = data.get("feed", [])
        pages_report.append({"page": page, "items": len(items),
                             "ratelimit_remaining": headers.get("x-ratelimit-remaining")})
        for it in items:
            raw_items.append(it)
            rows.append(row_of(it))
        cursor = data.get("cursor")
        page += 1
        if not cursor:
            break
        time.sleep(SLEEP)

    rows = rows[:args.limit]
    if not rows:
        print("tidak ada baris. Periksa handle, jaringan, dan endpoint.")
        return
    raw_path, csv_path, log_path, sum_path = write_outputs(
        args.outdir, args.actor, raw_items[:len(rows)], rows, pages_report)
    print("baris: %d | halaman: %d" % (len(rows), len(pages_report)))
    print("raw:", raw_path)
    print("csv:", csv_path)
    print("log:", log_path)
    print("checksum:", sum_path)


if __name__ == "__main__":
    main()

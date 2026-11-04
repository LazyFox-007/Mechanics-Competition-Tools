# -*- coding: utf-8 -*-
"""抓 OpenStax 教材网页正文 → markdown（绕过 PDF 的 403）
用法: python fetch_openstax.py [book_url] [outdir]
"""
import re, sys, time, urllib.request, html
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
BOOK = sys.argv[1] if len(sys.argv) > 1 else "https://openstax.org/books/university-physics-volume-1/pages/1-introduction"
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else r"D:\math\mechnicsCOMP\AIMechanicSpace\mechanics-competition-tools\kb\raw\openstax")
OUT.mkdir(parents=True, exist_ok=True)


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "ignore")


def strip(h):
    h = re.sub(r"(?is)<(script|style|nav|header|footer|aside)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>", "\n", h)
    h = re.sub(r"(?i)</(p|div|li|h[1-6]|tr|section)>", "\n", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    h = html.unescape(h)
    h = re.sub(r"[ \t\u00a0]+", " ", h)
    h = re.sub(r"\n\s*\n+", "\n\n", h)
    return h.strip()


def main():
    first = get(BOOK)
    base = re.match(r"(https://openstax\.org/books/[^/]+/)", BOOK).group(1)
    slugs = sorted(set(re.findall(re.escape(base) + r"pages/([0-9]+-[a-z0-9\-]+)", first)))
    print(f"发现 {len(slugs)} 个章节页")
    total = 0
    for i, s in enumerate(slugs, 1):
        p = OUT / f"{s}.md"
        if p.exists() and p.stat().st_size > 500:
            continue
        try:
            body = strip(get(base + "pages/" + s))
            p.write_text(f"# {s}\n\n{body}", encoding="utf-8")
            total += len(body)
            print(f"  [{i}/{len(slugs)}] {s}  {len(body)} 字符")
        except Exception as e:  # noqa: BLE001
            print(f"  [{i}] FAIL {s}: {e}")
        time.sleep(0.3)
    print(f"完成，累计 {total/1048576:.2f} MB 文本")


if __name__ == "__main__":
    main()

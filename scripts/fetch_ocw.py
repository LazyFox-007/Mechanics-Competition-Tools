# -*- coding: utf-8 -*-
"""抓 MIT OCW 3.11 Mechanics of Materials（CC BY-NC-SA）全部 PDF
用法: python fetch_ocw.py [课程根URL] [输出目录]
"""
import re, sys, time, urllib.request, urllib.parse
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
ROOT = sys.argv[1] if len(sys.argv) > 1 else "https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/"
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else r"D:\math\mechnicsCOMP\AIMechanicSpace\mechanics-competition-tools\kb\raw\ocw311")
OUT.mkdir(parents=True, exist_ok=True)

PAGES = ["pages/lecture-notes/", "pages/assignments/", "pages/exams/",
         "pages/recitations/", "pages/readings/", "pages/syllabus/", "pages/tools/"]


def get(url, timeout=40):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def main():
    links = set()
    for p in PAGES:
        try:
            html = get(urllib.parse.urljoin(ROOT, p)).decode("utf-8", "ignore")
        except Exception as e:  # noqa: BLE001
            print(f"  [page] {p}: {e}")
            continue
        found = re.findall(r'href="([^"]+\.pdf)"', html)
        found += re.findall(r'href="(/courses/[^"]+/resources/[^"]+)"', html)
        for f in found:
            links.add(urllib.parse.urljoin(ROOT, f))
        print(f"  [page] {p}: +{len(found)}")

    # 解码 /resources/<slug>/ 页面，取其中的 pdf 直链
    direct = {u for u in links if u.lower().endswith(".pdf")}
    pages = {u for u in links if "/resources/" in u and not u.lower().endswith(".pdf")}
    for u in list(pages)[:0]:   # 直链优先：/resources/ 逐页解析太慢，实测会卡住
        try:
            html = get(u).decode("utf-8", "ignore")
            for f in re.findall(r'href="([^"]+\.pdf)"', html):
                direct.add(urllib.parse.urljoin(u, f))
        except Exception:  # noqa: BLE001
            pass
    print(f"发现 PDF {len(direct)} 个")

    tot, ok = 0, 0
    for u in sorted(direct):
        name = urllib.parse.unquote(u.rsplit("/", 1)[-1])
        p = OUT / name
        if p.exists() and p.stat().st_size > 10_000:
            tot += p.stat().st_size
            ok += 1
            continue
        try:
            data = get(u, 60)
            if len(data) < 5_000 or data[:4] != b"%PDF":
                continue
            p.write_bytes(data)
            tot += len(data)
            ok += 1
            if ok % 10 == 0:
                print(f"  ... {ok} 篇 {tot/1048576:.1f} MB")
        except Exception as e:  # noqa: BLE001
            print(f"  fail {name}: {type(e).__name__}")
        time.sleep(0.15)
    print(f"完成：{ok} 篇，{tot/1048576:.1f} MB → {OUT}")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""批量抓 NIST Legacy/NSRDS 公开 PDF（公有领域）。
NSRDS 是 NIST 的标准参考数据丛书，编号连续，已知 nbsnsrds44 可下（2.93MB）。
用法: python fetch_nist.py [开始] [结束]
"""
import sys, time, urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
OUT = Path(r"D:\math\mechnicsCOMP\AIMechanicSpace\mechanics-competition-tools\kb\raw\nist")
OUT.mkdir(parents=True, exist_ok=True)
TMPL = "https://nvlpubs.nist.gov/nistpubs/Legacy/NSRDS/nbsnsrds{n}.pdf"

lo = int(sys.argv[1]) if len(sys.argv) > 1 else 1
hi = int(sys.argv[2]) if len(sys.argv) > 2 else 60
tot = 0
ok = 0
for n in range(lo, hi + 1):
    p = OUT / f"nbsnsrds{n}.pdf"
    if p.exists() and p.stat().st_size > 100_000:
        tot += p.stat().st_size
        ok += 1
        continue
    url = TMPL.format(n=n)
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=45) as r:
            data = r.read()
        if len(data) < 100_000 or not data[:4] == b"%PDF":
            print(f"  [{n}] skip ({len(data)} bytes)")
            continue
        p.write_bytes(data)
        tot += len(data)
        ok += 1
        print(f"  [{n}] OK {len(data)/1048576:.2f} MB  {p.name}")
    except Exception as e:  # noqa: BLE001
        print(f"  [{n}] fail {type(e).__name__} {getattr(getattr(e,'response',None),'status',None) or ''}")
    time.sleep(0.2)

print(f"完成：{ok} 篇，共 {tot/1048576:.1f} MB → {OUT}")

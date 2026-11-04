#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""kb_index.py —— 力学竞赛知识库全文索引（离线、无第三方依赖除 PyMuPDF）

用法：
    python kb_index.py build   [--kb D:\\...\\kb]     # 建索引 kb/index.jsonl
    python kb_index.py search "压杆 柔度"  [--top 5]  # 检索，打印片段
    python kb_index.py stat                            # 看索引规模

设计：纯词频 + 子串命中打分，不依赖 embedding，赛时零网络、零模型。
索引单位 = 一个"块"（PDF 一页 / markdown 一节），chunk 带文件、页码，便于溯源。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

CHUNK = 900          # 每块目标字符数（PDF 页内再切）
OVERLAP = 120


def _norm(s: str) -> str:
    s = s.replace("\u3000", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def _chunks(text: str, size: int = CHUNK, overlap: int = OVERLAP):
    text = _norm(text)
    if not text:
        return
    i = 0
    while i < len(text):
        yield text[i:i + size]
        i += size - overlap


def iter_pdf(p: Path):
    import pymupdf  # PyMuPDF
    with pymupdf.open(p) as doc:
        for no, page in enumerate(doc, 1):
            for c in _chunks(page.get_text("text")):
                yield {"file": p.name, "page": no, "text": c}


def iter_text(p: Path):
    raw = p.read_text(encoding="utf-8", errors="ignore")
    # markdown 按二级标题切
    parts = re.split(r"(?m)^##\s+", raw)
    for i, part in enumerate(parts):
        if not part.strip():
            continue
        head = part.splitlines()[0][:60] if part.splitlines() else ""
        for c in _chunks(part):
            yield {"file": p.name, "section": head, "text": c}


def build(kb: Path) -> int:
    out = kb / "index.jsonl"
    n = 0
    with out.open("w", encoding="utf-8") as f:
        for p in sorted(kb.rglob("*")):
            if p.is_dir() or p.name.startswith(".") or p.suffix.lower() not in {".pdf", ".md", ".txt"}:
                continue
            if p.parent.name == "raw" and p.suffix.lower() == ".md":
                continue
            try:
                it = iter_pdf(p) if p.suffix.lower() == ".pdf" else iter_text(p)
                for rec in it:
                    if len(rec["text"]) < 40:      # 丢掉目录页/空白页
                        continue
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    n += 1
            except Exception as e:  # noqa: BLE001
                print(f"  [skip] {p.name}: {e}", file=sys.stderr)
    print(f"索引完成：{n} 块 → {out}  ({out.stat().st_size/1048576:.2f} MB)")
    return n


def load(kb: Path):
    idx = kb / "index.jsonl"
    if not idx.exists():
        sys.exit(f"没有索引，先跑：python {Path(__file__).name} build")
    with idx.open(encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)


def search(kb: Path, query: str, top: int = 5):
    terms = [t for t in re.split(r"\s+", query.strip()) if t]
    if not terms:
        sys.exit("查询为空")
    scored = []
    for rec in load(kb):
        text = rec["text"]
        low = text.lower()
        hit = [t for t in terms if t.lower() in low]
        if not hit:
            continue
        # 打分：命中词数 * 100 + 出现次数；短块略加权
        cnt = sum(low.count(t.lower()) for t in hit)
        score = len(hit) * 100 + min(cnt, 50) + 300 / max(len(text), 1) * 10
        scored.append((score, rec, hit))
    scored.sort(key=lambda x: -x[0])
    if not scored:
        print("无命中")
        return
    for score, rec, hit in scored[:top]:
        loc = f"{rec['file']}" + (f" p.{rec['page']}" if "page" in rec else f" §{rec.get('section','')}")
        print(f"\n=== [{score:.0f}] {loc}   命中:{','.join(hit)}")
        t = rec["text"].replace("\n", " ")
        print("   " + t[:400] + ("…" if len(t) > 400 else ""))
    print(f"\n共 {len(scored)} 块命中，显示前 {min(top, len(scored))} 条。")


def stat(kb: Path):
    idx = kb / "index.jsonl"
    if not idx.exists():
        sys.exit("无索引")
    files, chars, n = Counter(), 0, 0
    for rec in load(kb):
        files[rec["file"]] += 1
        chars += len(rec["text"])
        n += 1
    print(f"块数 {n}，字符 {chars:,}，索引 {idx.stat().st_size/1048576:.2f} MB")
    for f, c in files.most_common():
        print(f"  {f}: {c} 块")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "search", "stat"])
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("--kb", default=str(Path(__file__).resolve().parent.parent / "kb"))
    ap.add_argument("--top", type=int, default=5)
    a = ap.parse_args()
    kb = Path(a.kb)
    if not kb.is_dir():
        sys.exit(f"知识库目录不存在：{kb}")
    {"build": lambda: build(kb),
     "stat": lambda: stat(kb),
     "search": lambda: search(kb, a.query, a.top)}[a.cmd]()


if __name__ == "__main__":
    main()

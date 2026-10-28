# -*- coding: utf-8 -*-
"""
给技能库生成检索索引 index.json。

为什么需要：mechanics-map 有 17 章、约 45 万字符，模型没法整本读进上下文；
先查索引拿到「文件 + 行号」，再只读那几十行，token 才可控。

索引结构（每章一条，章节内记录各级标题的行号）：
{
  "generated": "2026-10-28T17:40:00",
  "sources": [
    {"skill": "mechanics-map", "file": "modules/01-newtonian-basics.md",
     "title": "1. Newtonian Basics", "lines": 812,
     "sections": [{"level": 2, "title": "1.1 ...", "line": 34}, ...]}
  ]
}

跑法：python skills/mechanics-map/build_index.py
"""
import io
import json
import os
import re
import time

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.basename(HERE)

HEAD = re.compile(r"^(#{1,4})\s+(.*\S)\s*$")


def scan(path):
    with io.open(path, encoding="utf-8", errors="replace") as f:
        lines = f.read().splitlines()
    title = None
    sections = []
    for i, ln in enumerate(lines, start=1):
        m = HEAD.match(ln)
        if not m:
            continue
        level = len(m.group(1))
        text = m.group(2).strip()
        if title is None:
            # 优先用 H1；很多模块直接从 H2 起（如 "1: Basics of Newtonian Mechanics"），
            # 此时用第一个标题当章名，别退化成文件名
            title = text
        sections.append({"level": level, "title": text, "line": i})
    return {"title": title or os.path.basename(path), "lines": len(lines), "sections": sections}


def main():
    sources = []
    mod_dir = os.path.join(HERE, "modules")
    files = []
    if os.path.isdir(mod_dir):
        files += [os.path.join(mod_dir, f) for f in sorted(os.listdir(mod_dir)) if f.endswith(".md")]
    files += [os.path.join(HERE, "SKILL.md")]

    for fp in files:
        if not os.path.isfile(fp):
            continue
        rel = os.path.relpath(fp, HERE).replace("\\", "/")
        rec = scan(fp)
        rec.update({"skill": SKILL, "file": rel})
        sources.append(rec)

    payload = {
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "skill": SKILL,
        "note": "先查本索引定位「文件 + 行号」，再只读那几十行；不要整本读。",
        "sources": sources,
    }
    out = os.path.join(HERE, "index.json")
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)

    total_sections = sum(len(s["sections"]) for s in sources)
    print(f"wrote {out}")
    print(f"  文件 {len(sources)} 个，标题 {total_sections} 条，总行数 {sum(s['lines'] for s in sources)}")
    for s in sources[:3]:
        print(f"  - {s['file']}: {s['title']}（{len(s['sections'])} 节）")


if __name__ == "__main__":
    main()

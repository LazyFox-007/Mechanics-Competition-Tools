#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""换环境预检 —— 在目标机上跑一遍，确认整套东西真的能起来。

为什么需要它：
  本仓库在开发机上跑通不代表换机器跑通。最常见的四类坑：
    1. .ps1 丢了 UTF-8 BOM（PS5.1 会按 ANSI 解，中文全乱、语法报错）
    2. 行尾被 git 改掉（CRLF ↔ LF）
    3. 文件里写死了开发机的绝对路径（D:\\anaconda\\..., D:/math/...）
    4. 解释器太老 / 缺标准库

  本脚本只做静态检查与自检，不依赖 sympy / numpy，纯标准库即可运行：
      python scripts/preflight.py

  全部 OK 才返回 0。
"""

import io
import glob
import json
import os
import re
import subprocess
import sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASS, FAIL, WARN = 0, 0, 0


def ok(msg):
    global PASS
    PASS += 1
    print("  [OK  ] %s" % msg)


def bad(msg):
    global FAIL
    FAIL += 1
    print("  [FAIL] %s" % msg)


def warn(msg):
    global WARN
    WARN += 1
    print("  [WARN] %s" % msg)


def walk(exts, skip=(".git", ".out", "__pycache__", "vendor")):
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in skip]
        for fn in filenames:
            if any(fn.endswith(e) for e in exts):
                yield os.path.join(dirpath, fn)


def rel(p):
    return os.path.relpath(p, ROOT).replace("\\", "/")


# ───────────────────────── 1. Python 版本 ─────────────────────────
print("=== 1. 解释器 ===")
if sys.version_info < (3, 8):
    bad("Python %s < 3.8（f-string / := 等语法会失败）" % sys.version.split()[0])
else:
    ok("Python %s (%s)" % (sys.version.split()[0], sys.executable))

# ───────────────────────── 2. .ps1 必须 UTF-8 BOM + CRLF ─────────────────────────
print("\n=== 2. .ps1 编码（PS5.1 无 BOM 会按 ANSI 解，中文必乱）===")
ps1s = list(walk([".ps1"]))
if not ps1s:
    warn("没找到 .ps1")
for p in ps1s:
    b = open(p, "rb").read()
    has_bom = b[:3] == b"\xef\xbb\xbf"
    body = b[3:] if has_bom else b
    crlf = body.count(b"\r\n")
    lf = body.count(b"\n") - crlf
    if not has_bom:
        bad("%s 缺 UTF-8 BOM" % rel(p))
    elif lf:
        bad("%s 有 %d 处裸 LF（应为全 CRLF）" % (rel(p), lf))
    else:
        ok("%s  BOM+CRLF  %d 行" % (rel(p), crlf))

# ───────────────────────── 3. 文本文件可 UTF-8 解码 ─────────────────────────
print("\n=== 3. 文本编码 ===")
bad_enc = []
n = 0
for p in walk([".py", ".json", ".md", ".yml", ".yaml", ".cmd"]):
    n += 1
    try:
        with io.open(p, encoding="utf-8") as f:
            f.read()
    except UnicodeDecodeError as e:
        bad_enc.append("%s (%s)" % (rel(p), e.reason))
if bad_enc:
    for x in bad_enc:
        bad("非 UTF-8: " + x)
else:
    ok("%d 个文本文件全部可 UTF-8 解码" % n)

# ───────────────────────── 4. Python 语法编译 ─────────────────────────
print("\n=== 4. Python 语法 ===")
bad_py = []
pys = list(walk([".py"]))
for p in pys:
    try:
        # 用内存 compile 而不是 py_compile：后者在 Windows 上把 cfile 指到
        # os.devnull（"nul"）会报 "nul is a non-regular file"
        with io.open(p, encoding="utf-8") as f:
            compile(f.read(), p, "exec")
    except Exception as e:  # noqa: BLE001
        bad_py.append("%s: %s" % (rel(p), str(e)[:90]))
if bad_py:
    for x in bad_py:
        bad(x)
else:
    ok("%d 个 .py 编译通过" % len(pys))

# ───────────────────────── 5. JSON 可解析 ─────────────────────────
print("\n=== 5. JSON ===")
bad_json = []
jsons = list(walk([".json"]))
for p in jsons:
    try:
        with io.open(p, encoding="utf-8") as f:
            json.load(f)
    except Exception as e:  # noqa: BLE001
        bad_json.append("%s: %s" % (rel(p), str(e)[:60]))
if bad_json:
    for x in bad_json:
        bad(x)
else:
    ok("%d 个 .json 解析通过" % len(jsons))

# ───────────────────────── 6. 绝对路径硬编码 ─────────────────────────
print("\n=== 6. 绝对路径硬编码（换机器就废）===")
PAT = re.compile(r"[A-Za-z]:[\\/](?:[^\\/\s\"'`]+[\\/])*[^\\/\s\"'`]*")
ALLOW_DIRS = ("D:/math", "D:\\math")            # 文档里的『本机快照』允许
hits = []
for p in walk([".py", ".json", ".md"]):
    r = rel(p)
    if r.startswith("kb/") or r.startswith("docs/工具审计") or r == "docs/建模决策卡.md":
        continue                                  # 审计/复盘文档允许写开发机路径
    with io.open(p, encoding="utf-8", errors="replace") as f:
        for i, line in enumerate(f, 1):
            if "REPO" in line or "${" in line or "%s" in line or "repoPosix" in line:
                continue
            for m in PAT.finditer(line):
                s = m.group(0)
                if len(s) < 6 or s.startswith(("http", "https")):
                    continue
                hits.append("%s:%d  %s" % (r, i, s))
if hits:
    for h in hits[:25]:
        warn("疑似硬编码: " + h)
    if len(hits) > 25:
        warn("...另有 %d 处" % (len(hits) - 25))
    print("       （WARN 不计失败：多为候选清单/示例，人看一眼即可）")
else:
    ok("未发现绝对路径硬编码")

# ───────────────────────── 7. 建模决策卡 schema ─────────────────────────
print("\n=== 7. 建模决策卡 cards.json ===")
cards = os.path.join(ROOT, "mcp", "mech-model", "cards.json")
try:
    with io.open(cards, encoding="utf-8") as f:
        d = json.load(f)
    assert "_common" in d and "cards" in d, "缺 _common / cards"
    need = {"id", "question", "options"}
    for pid, c in d["cards"].items():
        assert "name" in c and "axes" in c, "%s 缺 name/axes" % pid
        for a in c["axes"]:
            miss = need - set(a)
            assert not miss, "%s.%s 缺字段 %s" % (pid, a.get("id", "?"), miss)
            assert len(a["options"]) >= 2, "%s.%s 选项少于 2" % (pid, a["id"])
        for cf in c.get("conflicts", []):
            assert "when" in cf and "message" in cf, "%s conflicts 字段不全" % pid
    n_ax = sum(len(c["axes"]) for c in d["cards"].values())
    ok("%d 张卡 / %d 条题型轴 / %d 条通用轴"
       % (len(d["cards"]), n_ax, len(d["_common"]["axes"])))

    # 防泄漏：卡里不许出现具体答案数值（赛规：严禁夹带赛题答案）
    leak_re = re.compile(r"\d+\.\d{3,}")          # 三位以上小数，几乎必是某个答案
    KNOWN = ["5.54", "48.05", "0.043", "166.2", "298.7", "36517", "82163",
             "13584", "23528", "1.707", "2.165", "1.371", "12.775"]
    leaks = []

    def walk_json(node, path):
        if isinstance(node, dict):
            for k, v in node.items():
                walk_json(v, path + "." + str(k))
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk_json(v, path + "[%d]" % i)
        elif isinstance(node, str):
            for m in leak_re.findall(node):
                leaks.append("%s  %s" % (path, m))
            for k in KNOWN:
                if k in node:
                    leaks.append("%s  %s" % (path, k))

    walk_json(d["_common"], "_common")
    for pid, c in d["cards"].items():
        walk_json(c, pid)
    if leaks:
        for x in leaks:
            bad("cards.json 疑似泄漏答案数值: " + x)
    else:
        ok("cards.json 无泄漏（无 3 位以上小数、无已知答案数值）")
except Exception as e:  # noqa: BLE001
    bad("cards.json 校验失败: %s" % e)

# ───────────────────────── 9. 可选插件 ─────────────────────────
print("\n=== 9. 可选插件 dsh-mech-workbench（读图工具链）===")
home = os.path.expanduser("~")
_cfg_path = os.path.join(home, ".dsh", "cordis.patch.yml")
cands = []
for pat in ("plugins/*mech-workbench*", "plugins/*/*mech-workbench*"):
    cands += glob.glob(os.path.join(home, ".dsh", pat))
in_cfg = False
if os.path.isfile(_cfg_path):
    with io.open(_cfg_path, encoding="utf-8", errors="replace") as f:
        for ln in f:
            s = ln.strip()
            if not s or s.startswith("#"):
                continue          # 注释里提到不算已装（踩过：mech-kit 的注释含该字样导致误报）
            if "mech-workbench" in s:
                in_cfg = True
                break
if cands or in_cfg:
    ok("已装（%s）" % (cands[0] if cands else "cordis.patch.yml 里有非注释条目"))
    print("        注：本仓库另有 mcp/mech-kit/ 直接调同一批脚本，不装插件也能用读图/内力图")
else:
    warn("插件未装 —— 只能用 mcp/mech-kit 的 4 个离线 op（足够覆盖读图与静定分析）")
    print("        插件额外给的（都要联网或额外装）：second_reader 二次转写、viz_check 语义评审、")
    print("        render_math 公式排版。赛规禁联网，这三项本来也用不了，可不装。")
    print("        若要装（需创造模式）：")
    print("          plugin_manager → action: install_bundle")
    print("                       → target: %s" % os.path.join(ROOT, "plugins", "dsh-mech-workbench"))

# ───────────────────────── 8. 真跑自检 ─────────────────────────
print("\n=== 8. 跑自检（这些会起真进程）===")
SELFTESTS = [
    ("mech-model/selftest", os.path.join(ROOT, "mcp", "mech-model", "test", "selftest.py")),
    ("mech-model/handshake", os.path.join(ROOT, "mcp", "mech-model", "test", "handshake.py")),
    ("mech-kit/selftest", os.path.join(ROOT, "mcp", "mech-kit", "test", "selftest.py")),
]
for label, sp in SELFTESTS:
    if not os.path.isfile(sp):
        bad("缺 %s" % label)
        continue
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    p = subprocess.run([sys.executable, sp], cwd=ROOT,
                       capture_output=True, timeout=300, env=env)
    tail = [l for l in p.stdout.decode("utf-8", "replace").splitlines() if l.strip()][-1:]
    if p.returncode == 0:
        ok("%s -> %s" % (label, tail[0] if tail else "ok"))
    else:
        bad("%s 退出码 %d | %s" % (label, p.returncode,
                                   (tail[0] if tail else p.stderr.decode('utf-8', 'replace')[-160:])))

# ───────────────────────── 汇总 ─────────────────────────
print("\n" + "=" * 46)
print("PASS %d  WARN %d  FAIL %d" % (PASS, WARN, FAIL))
if FAIL == 0:
    print("换环境预检通过：可以打包带走。")
else:
    print("有 FAIL 项，别急着换机器。")
sys.exit(0 if FAIL == 0 else 1)

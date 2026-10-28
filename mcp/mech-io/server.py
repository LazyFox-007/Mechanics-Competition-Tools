#!/usr/bin/env python3
"""
mech-io MCP —— 竞赛现场的「环境 / 读图 / 校核 / 交付」四类边界工具

为什么单独一个服务：
  比赛时真正浪费时间的不是解方程，而是四类边界——
    1) 跑 Python 要穿过 shell：中文弯引号、GBK 控制台、argv 转义，一碰就炸；
    2) 图像区域操作：预览图与原图像素比例不同，按像素裁必然错位；
    3) 图形自检：缺字形、文字溢出/重叠、图被压扁，只能靠人眼看；
    4) 交付打包：命名规范、清单哈希、MD/HTML 转 PDF，全靠手搓。

工具（10 个）：
    io_info           自检：哪些可选依赖可用
    py_run            跑 Python（脚本或代码），UTF-8、argv 数组、不经 shell
    img_crop          按「分数坐标」裁剪/放大图片
    pdf_page_crop     直接从 PDF 页取局部高清图（不经过整页渲染再裁）
    fig_lint          图片级检查：尺寸/DPI/是否空白/是否触边/是否重复
    plot_audit        跑绘图脚本并审计：缺字形、文字越界、文字重叠、图尺寸
    scan_extremum     表达式在给定区域上做密扫描找极值（含边界判定）
    numeric_compare   两个表达式在网格上比数值一致度（闭式 vs 一般式）
    html_to_pdf       用 Edge/Chrome 无头打印 HTML→PDF
    submission_pack   按赛规命名建提交骨架 + 生成带 SHA-256 的清单

设计原则（与 sympy-physics 一致）：
  - 只依赖标准库；Pillow / PyMuPDF / matplotlib / numpy / sympy 均为可选，缺了要说清楚
  - stdout 只走协议，任何杂散输出压到 stderr
  - 任何工具失败都返回 {"ok": false, "error": ...}，不崩进程
"""

import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import traceback

# ── stdout 保护：真 stdout 留给协议，fd 1 指向 stderr ──────────────
_real_stdout_fd = os.dup(1)
os.dup2(2, 1)
_OUT = os.fdopen(_real_stdout_fd, "w", encoding="utf-8", buffering=1)

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8")

SERVER_NAME = "mech-io"
VERSION = "0.1.0"

# ── 可选依赖探测 ─────────────────────────────────────────────────
try:
    from PIL import Image  # noqa: F401
    HAS_PIL = True
except Exception:  # noqa: BLE001
    HAS_PIL = False

try:
    import fitz  # PyMuPDF
    HAS_FITZ = True
except Exception:  # noqa: BLE001
    HAS_FITZ = False

try:
    import numpy as np
    HAS_NUMPY = True
except Exception:  # noqa: BLE001
    HAS_NUMPY = False

try:
    import sympy as sp
    HAS_SYMPY = True
except Exception:  # noqa: BLE001
    HAS_SYMPY = False


# ════════════════════════════════════════════════════════════════
# 工具定义
# ════════════════════════════════════════════════════════════════
TOOLS = [
    {
        "name": "io_info",
        "description": "自检：解释器版本 + Pillow/PyMuPDF/numpy/sympy/matplotlib/browser 是否可用。开局先跑一次。",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "py_run",
        "description": (
            "跑一段 Python（脚本文件或内联代码），UTF-8 输入输出、argv 数组、不经过 shell。"
            "用来绕开 Windows 下中文引号/路径被 PowerShell 拆坏、控制台 GBK 报 UnicodeEncodeError 的问题。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "脚本绝对路径；与 code 二选一"},
                "code": {"type": "string", "description": "内联代码；与 path 二选一"},
                "args": {"type": "array", "items": {"type": "string"}, "description": "传给脚本的参数（数组，不经转义）"},
                "cwd": {"type": "string", "description": "工作目录，默认脚本所在目录"},
                "python": {"type": "string", "description": "指定解释器，默认本服务所用解释器"},
                "timeout": {"type": "number", "description": "超时秒数，默认 300"},
                "max_chars": {"type": "number", "description": "stdout/stderr 各保留多少字符，默认 20000"},
            },
        },
    },
    {
        "name": "img_crop",
        "description": (
            "按「分数坐标」裁剪（或放大）图片：box=[x0,y0,x1,y1]，取值 0~1，与图片实际像素无关。"
            "解决“预览图被缩放、按像素裁一定错位”的问题。scale>1 时 LANCZOS 放大，适合读小号公式。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "源图片路径"},
                "box": {"type": "array", "items": {"type": "number"},
                        "description": "[x0,y0,x1,y1]，默认分数（0~1）"},
                "box_units": {"type": "string", "enum": ["frac", "px"], "description": "默认 frac"},
                "scale": {"type": "number", "description": "放大倍数，默认 1"},
                "out": {"type": "string", "description": "输出路径，默认同目录 *_crop.png"},
            },
            "required": ["path", "box"],
        },
    },
    {
        "name": "pdf_page_crop",
        "description": (
            "直接从 PDF 某一页取局部高清图（分数坐标，默认 300 dpi），不经过整页渲染再裁。"
            "读公式下标、图注、表格数字时用它，比 pdf_render 整页再裁更准更小。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "PDF 路径"},
                "page": {"type": "number", "description": "页码，1 起"},
                "box": {"type": "array", "items": {"type": "number"},
                        "description": "[x0,y0,x1,y1]，0~1 分数坐标；省略则整页"},
                "dpi": {"type": "number", "description": "默认 300"},
                "out": {"type": "string", "description": "输出 PNG 路径"},
            },
            "required": ["path", "page"],
        },
    },
    {
        "name": "fig_lint",
        "description": (
            "图片级体检：尺寸、DPI、是否近乎空白、内容是否触边（可能被裁）、多张图是否重复。"
            "语义问题（坐标轴方向反了、层次被压扁）它查不出来，那要靠 viz_check 或人眼看。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "paths": {"type": "array", "items": {"type": "string"}, "description": "一张或多张图片"},
            },
            "required": ["paths"],
        },
    },
    {
        "name": "plot_audit",
        "description": (
            "跑一个 matplotlib 绘图脚本，并在每张图保存前审计：缺字形（tofu）、文字越出画布、"
            "标题/轴标签/注记互相重叠、画布尺寸与 DPI。比事后看图更早发现问题。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "script": {"type": "string", "description": "绘图脚本绝对路径"},
                "timeout": {"type": "number", "description": "默认 300 秒"},
                "overlap_ratio": {"type": "number", "description": "重叠面积占比阈值，默认 0.25"},
            },
            "required": ["script"],
        },
    },
    {
        "name": "scan_extremum",
        "description": (
            "把表达式在给定变量区间上做密集网格扫描，返回极值、位置、是否落在边界、以及网格分辨率误差。"
            "用于“危险点在哪”“极值是否随参数切换”这类判断（解析解写完后用它独立复核）。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "expr": {"type": "string", "description": "表达式，如 '3*q*l**2/(4*b*h**2)' 或含 x,y"},
                "vars": {"type": "array", "description": "[[名, 下界, 上界], ...]，1~3 个",
                         "items": {"type": "array"}},
                "params": {"type": "object", "description": "其余符号的取值，如 {'q':'1e3','l':'5'}"},
                "find": {"type": "string", "enum": ["max", "min"], "description": "默认 max"},
                "samples": {"type": "number", "description": "每维采样数，默认 401"},
            },
            "required": ["expr", "vars"],
        },
    },
    {
        "name": "numeric_compare",
        "description": (
            "两个表达式在网格上逐点比较，返回最大相对误差与出现位置。"
            "用于“闭式推导 vs 一般式”“解析解 vs 数值积分”的一致性复核。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "expr_a": {"type": "string"},
                "expr_b": {"type": "string"},
                "vars": {"type": "array", "description": "[[名, 下界, 上界], ...] 网格变量"},
                "params": {"type": "object", "description": "其余符号的取值，如 {'q':'1e3','l':'5'}"},
                "samples": {"type": "number", "description": "每维采样数，默认 41"},
                "tol": {"type": "number", "description": "相对误差阈值，默认 1e-9"},
            },
            "required": ["expr_a", "expr_b", "vars"],
        },
    },
    {
        "name": "html_to_pdf",
        "description": "用本机 Edge/Chrome 无头打印把 HTML 转成 PDF（A4、无页眉页脚）。技术报告、答案文件的排版出口。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "html": {"type": "string", "description": "HTML 绝对路径"},
                "pdf": {"type": "string", "description": "输出 PDF 路径，默认同名 .pdf"},
                "browser": {"type": "string", "description": "浏览器可执行文件，默认自动查找 Edge/Chrome"},
            },
            "required": ["html"],
        },
    },
    {
        "name": "submission_pack",
        "description": (
            "提交材料流水线。action=init 按赛规建 <编号>-命题式赛题1-<队名> 目录骨架；"
            "action=manifest 递归生成带 SHA-256 的 manifest.json（复现包的“知识库清单与哈希”）。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": ["init", "manifest"]},
                "root": {"type": "string", "description": "init 用：放提交目录的父目录；manifest 用：要扫描的目录"},
                "team": {"type": "string", "description": "团队编号，如 AIC-2026-00000000"},
                "name": {"type": "string", "description": "团队名称"},
                "problem": {"type": "string", "description": "默认“命题式赛题1”"},
            },
            "required": ["action", "root"],
        },
    },
]


# ════════════════════════════════════════════════════════════════
# 通用小工具
# ════════════════════════════════════════════════════════════════
def _clip(s, n):
    s = s or ""
    return s if len(s) <= n else s[:n] + f"\n…[截断，原长 {len(s)}]"


def _which_browser(explicit=None):
    cands = []
    if explicit:
        cands.append(explicit)
    if os.environ.get("MECH_BROWSER"):
        cands.append(os.environ["MECH_BROWSER"])
    for env in ("PROGRAMFILES(X86)", "PROGRAMFILES", "LOCALAPPDATA"):
        base = os.environ.get(env)
        if not base:
            continue
        for rel in (r"Microsoft\Edge\Application\msedge.exe",
                    r"Google\Chrome\Application\chrome.exe"):
            cands.append(os.path.join(base, rel))
    for c in cands:
        if c and os.path.isfile(c):
            return c
    for exe in ("msedge", "chrome", "chromium", "google-chrome"):
        p = shutil.which(exe)
        if p:
            return p
    return None


def _sha256(path, chunk=1 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


# ════════════════════════════════════════════════════════════════
# 工具实现
# ════════════════════════════════════════════════════════════════
def t_io_info(_args):
    info = {
        "ok": True,
        "server": SERVER_NAME,
        "version": VERSION,
        "python": sys.version.split()[0],
        "executable": sys.executable,
        "platform": platform.platform(),
        "optional": {
            "Pillow": HAS_PIL,
            "PyMuPDF(fitz)": HAS_FITZ,
            "numpy": HAS_NUMPY,
            "sympy": HAS_SYMPY,
        },
        "browser": _which_browser(),
    }
    if not HAS_PIL:
        info.setdefault("hints", []).append("缺 Pillow：img_crop / fig_lint 不可用 → pip install pillow")
    if not HAS_FITZ:
        info.setdefault("hints", []).append("缺 PyMuPDF：pdf_page_crop 不可用 → pip install pymupdf")
    if not HAS_NUMPY:
        info.setdefault("hints", []).append("缺 numpy：scan_extremum / numeric_compare 不可用")
    if not HAS_SYMPY:
        info.setdefault("hints", []).append("缺 sympy：表达式解析不可用 → pip install sympy")
    if not info["browser"]:
        info.setdefault("hints", []).append("没找到 Edge/Chrome：html_to_pdf 不可用")
    return info


def t_py_run(args):
    code = args.get("code")
    path = args.get("path")
    if not code and not path:
        return {"ok": False, "error": "path 与 code 至少要给一个"}
    if code and path:
        return {"ok": False, "error": "path 与 code 只能给一个"}

    python = args.get("python") or sys.executable
    extra = [str(a) for a in (args.get("args") or [])]
    timeout = float(args.get("timeout") or 300)
    max_chars = int(args.get("max_chars") or 20000)

    if path:
        if not os.path.isfile(path):
            return {"ok": False, "error": f"脚本不存在: {path}"}
        cmd = [python, path] + extra
        cwd = args.get("cwd") or os.path.dirname(os.path.abspath(path))
    else:
        cmd = [python, "-c", code] + extra
        cwd = args.get("cwd") or os.getcwd()

    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    env.pop("PYTHONSTARTUP", None)

    try:
        p = subprocess.run(cmd, cwd=cwd, env=env, timeout=timeout,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"超时 {timeout}s", "cmd": cmd}

    out = p.stdout.decode("utf-8", "replace")
    err = p.stderr.decode("utf-8", "replace")
    return {
        "ok": p.returncode == 0,
        "returncode": p.returncode,
        "cwd": cwd,
        "stdout": _clip(out, max_chars),
        "stderr": _clip(err, max_chars),
    }


def t_img_crop(args):
    if not HAS_PIL:
        return {"ok": False, "error": "缺 Pillow，先 pip install pillow"}
    src = args["path"]
    box = [float(v) for v in args["box"]]
    if len(box) != 4:
        return {"ok": False, "error": "box 需要 4 个数 [x0,y0,x1,y1]"}
    scale = float(args.get("scale") or 1)
    units = (args.get("box_units") or "frac").lower()

    im = Image.open(src)
    w, h = im.size
    if units == "frac":
        px = (box[0] * w, box[1] * h, box[2] * w, box[3] * h)
    else:
        px = tuple(box)
    px = (max(0, int(round(px[0]))), max(0, int(round(px[1]))),
          min(w, int(round(px[2]))), min(h, int(round(px[3]))))
    if px[2] <= px[0] or px[3] <= px[1]:
        return {"ok": False, "error": f"裁剪框为空: {px}（源图 {w}x{h}）"}

    crop = im.crop(px)
    if scale != 1:
        crop = crop.resize((int(crop.width * scale), int(crop.height * scale)), Image.LANCZOS)

    out = args.get("out") or (os.path.splitext(src)[0] + "_crop.png")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    crop.save(out)
    return {"ok": True, "out": out, "source_size": [w, h], "box_px": list(px),
            "out_size": [crop.width, crop.height], "scale": scale}


def t_pdf_page_crop(args):
    if not HAS_FITZ:
        return {"ok": False, "error": "缺 PyMuPDF，先 pip install pymupdf（或改用 document MCP 的 pdf_render）"}
    path = args["path"]
    page_no = int(args["page"])
    dpi = int(args.get("dpi") or 300)   # PyMuPDF 的 xres/yres 要 int，给 float 会 TypeError
    box = args.get("box") or [0, 0, 1, 1]
    box = [float(v) for v in box]

    doc = fitz.open(path)
    if not (1 <= page_no <= doc.page_count):
        return {"ok": False, "error": f"页码越界：{page_no} / 共 {doc.page_count} 页"}
    page = doc[page_no - 1]
    r = page.rect
    clip = fitz.Rect(r.x0 + box[0] * r.width, r.y0 + box[1] * r.height,
                     r.x0 + box[2] * r.width, r.y0 + box[3] * r.height)
    pix = page.get_pixmap(clip=clip, dpi=dpi)

    out = args.get("out") or (
        os.path.splitext(path)[0] + f"_p{page_no}_crop.png")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    pix.save(out)
    return {"ok": True, "out": out, "page": page_no, "pages_total": doc.page_count,
            "size": [pix.width, pix.height], "dpi": dpi, "box_frac": box}


def t_fig_lint(args):
    if not HAS_PIL:
        return {"ok": False, "error": "缺 Pillow，先 pip install pillow"}
    paths = args["paths"]
    if isinstance(paths, str):
        paths = [paths]
    rows, digests = [], {}
    for p in paths:
        if not os.path.isfile(p):
            rows.append({"path": p, "error": "文件不存在"})
            continue
        im = Image.open(p)
        w, h = im.size
        dpi_info = None
        try:
            dpi_info = list(im.info.get("dpi") or [])
        except Exception:  # noqa: BLE001
            pass
        g = im.convert("L")
        try:
            from PIL import ImageStat
            stat = ImageStat.Stat(g)
            mean = float(stat.mean[0])
            std = float(stat.stddev[0])
        except Exception:  # noqa: BLE001
            px = list(g.getdata())
            n = max(1, len(px))
            mean = sum(px) / n
            std = (sum((v - mean) ** 2 for v in px) / n) ** 0.5
        # 触边：四条边像素与全图均值差异大 → 内容可能被裁
        edge_vals = []
        ww, hh = g.size
        for x in range(0, ww, max(1, ww // 50)):
            edge_vals.append(g.getpixel((x, 0)))
            edge_vals.append(g.getpixel((x, hh - 1)))
        for y in range(0, hh, max(1, hh // 50)):
            edge_vals.append(g.getpixel((0, y)))
            edge_vals.append(g.getpixel((ww - 1, y)))
        edge_dev = max(abs(v - mean) for v in edge_vals) if edge_vals else 0

        dg = _sha256(p)
        dup = digests.get(dg)
        digests.setdefault(dg, p)
        rows.append({
            "path": p, "size": [w, h], "mode": im.mode, "dpi": dpi_info,
            "mean_gray": round(mean, 1), "std_gray": round(std, 1),
            "blank": std < 2.0,
            "content_touches_edge": edge_dev > 60,
            "sha256_16": dg[:16],
            "duplicate_of": dup if dup else None,
        })
    return {"ok": True, "count": len(rows), "figures": rows,
            "note": "blank=True 多半是画布没画上；touches_edge=True 检查是否被裁；duplicate_of 非空说明重复出图"}


_AUDIT_RUNNER = r'''
import json, os, sys, warnings, runpy

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

SCRIPT = sys.argv[1]
OUTJSON = sys.argv[2]
RATIO = float(sys.argv[3]) if len(sys.argv) > 3 else 0.25

records = []
_orig_savefig = Figure.savefig
_done = set()

def _bbox(t, renderer):
    try:
        return t.get_window_extent(renderer=renderer)
    except Exception:
        return None

def audit(fig, fname):
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    fbox = fig.bbox
    issues = []
    texts = []
    for ax in fig.axes:
        for t in [ax.title, ax.xaxis.label, ax.yaxis.label] + list(ax.texts):
            if t.get_text().strip():
                texts.append((t.get_text()[:40], _bbox(t, renderer)))

    for label, bb in texts:
        if bb is None:
            continue
        if bb.x0 < fbox.x0 - 1 or bb.y0 < fbox.y0 - 1 or bb.x1 > fbox.x1 + 1 or bb.y1 > fbox.y1 + 1:
            issues.append({"kind": "out_of_canvas", "text": label,
                           "bbox": [round(v, 1) for v in (bb.x0, bb.y0, bb.x1, bb.y1)]})

    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            a, b = texts[i][1], texts[j][1]
            if a is None or b is None:
                continue
            x0, y0 = max(a.x0, b.x0), max(a.y0, b.y0)
            x1, y1 = min(a.x1, b.x1), min(a.y1, b.y1)
            if x1 <= x0 or y1 <= y0:
                continue
            inter = (x1 - x0) * (y1 - y0)
            smaller = min((a.x1 - a.x0) * (a.y1 - a.y0), (b.x1 - b.x0) * (b.y1 - b.y0))
            if smaller > 0 and inter / smaller > RATIO:
                issues.append({"kind": "text_overlap",
                               "a": texts[i][0], "b": texts[j][0],
                               "ratio": round(inter / smaller, 2)})

    records.append({
        "file": os.path.basename(fname),
        "size_inches": [round(v, 2) for v in fig.get_size_inches()],
        "dpi": fig.dpi,
        "axes": len(fig.axes),
        "issues": issues,
    })

def patched(self, fname, *a, **kw):
    key = id(self)
    if key not in _done:
        _done.add(key)
        try:
            audit(self, str(fname))
        except Exception as e:
            records.append({"file": str(fname), "audit_error": f"{type(e).__name__}: {e}"})
    return _orig_savefig(self, fname, *a, **kw)

Figure.savefig = patched

with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    try:
        runpy.run_path(SCRIPT, run_name="__main__")
        err = None
    except SystemExit:
        err = None
    except Exception as e:
        import traceback as tb
        err = {"error": f"{type(e).__name__}: {e}", "trace": tb.format_exc(limit=4)}
    glyph = []
    for w in caught:
        msg = str(w.message)
        if "missing from font" in msg or "Glyph" in msg:
            glyph.append(msg)

payload = {"ok": True, "figures": records, "missing_glyph_warnings": glyph[:20],
           "run_error": err}
with open(OUTJSON, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=1)
'''


def t_plot_audit(args):
    script = args["script"]
    if not os.path.isfile(script):
        return {"ok": False, "error": f"脚本不存在: {script}"}
    timeout = float(args.get("timeout") or 300)
    ratio = float(args.get("overlap_ratio") or 0.25)

    tmpdir = tempfile.mkdtemp(prefix="mechio_audit_")
    runner = os.path.join(tmpdir, "_audit_runner.py")
    outjson = os.path.join(tmpdir, "_audit.json")
    with open(runner, "w", encoding="utf-8") as f:
        f.write(_AUDIT_RUNNER)

    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["MPLBACKEND"] = "Agg"
    try:
        p = subprocess.run([sys.executable, runner, script, outjson, str(ratio)],
                           cwd=os.path.dirname(os.path.abspath(script)),
                           env=env, timeout=timeout,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"超时 {timeout}s"}

    if not os.path.isfile(outjson):
        return {"ok": False,
                "error": "审计没产出结果（多半是脚本在 import 阶段就挂了）",
                "returncode": p.returncode,
                "stderr": _clip(p.stderr.decode("utf-8", "replace"), 4000)}
    with open(outjson, encoding="utf-8") as f:
        payload = json.load(f)

    payload["script"] = script
    payload["returncode"] = p.returncode
    payload["stderr"] = _clip(p.stderr.decode("utf-8", "replace"), 2000)
    total_issues = sum(len(fig.get("issues") or []) for fig in payload.get("figures") or [])
    payload["summary"] = {
        "figures": len(payload.get("figures") or []),
        "issues": total_issues,
        "missing_glyphs": len(payload.get("missing_glyph_warnings") or []),
        "clean": total_issues == 0 and not payload.get("missing_glyph_warnings")
                 and payload.get("run_error") is None,
    }
    return payload


def _lambdify(expr_str, names, params=None):
    locals_map = {n: sp.Symbol(n, real=True) for n in names}
    if params:
        for k, v in params.items():
            locals_map.setdefault(k, sp.Symbol(k, real=True))
    expr = sp.sympify(expr_str, locals=locals_map)
    syms = [locals_map[n] for n in names]
    fn = sp.lambdify(syms, expr, "numpy")
    return expr, syms, fn


def t_scan_extremum(args):
    if not (HAS_NUMPY and HAS_SYMPY):
        return {"ok": False, "error": "需要 numpy + sympy"}
    varlist = args["vars"]
    names = [v[0] for v in varlist]
    n = int(args.get("samples") or 401)
    find = (args.get("find") or "max").lower()
    params = args.get("params") or {}

    expr, syms, _ = _lambdify(args["expr"], names, params)
    if params:
        expr = expr.subs({sp.Symbol(k, real=True): sp.sympify(v) for k, v in params.items()})
    free = expr.free_symbols - set(syms)
    if free:
        return {"ok": False,
                "error": f"表达式里还有未给值的符号: {sorted(str(s) for s in free)}",
                "hint": "用 params 传值，或把变量写进 vars"}
    fn = sp.lambdify(syms, expr, "numpy")

    grids = [np.linspace(float(v[1]), float(v[2]), n) for v in varlist]
    mesh = np.meshgrid(*grids, indexing="ij")
    vals = fn(*mesh)
    vals = np.asarray(vals, dtype=float)
    if vals.ndim == 0:
        vals = np.broadcast_to(vals, mesh[0].shape)
    if find == "max":
        idx = np.unravel_index(np.nanargmax(vals), vals.shape)
    else:
        idx = np.unravel_index(np.nanargmin(vals), vals.shape)

    coords = {names[k]: float(mesh[k][idx]) for k in range(len(names))}
    on_edge = {}
    for k, nm in enumerate(names):
        lo, hi = float(varlist[k][1]), float(varlist[k][2])
        v = coords[nm]
        on_edge[nm] = bool(abs(v - lo) < 1e-12 * max(1, abs(lo)) or abs(v - hi) < 1e-12 * max(1, abs(hi)))

    steps = {names[k]: (float(varlist[k][2]) - float(varlist[k][1])) / (n - 1) for k in range(len(names))}
    return {"ok": True, "expr": str(expr), "find": find,
            "value": float(vals[idx]), "at": coords,
            "on_boundary": on_edge, "grid_step": steps,
            "note": "on_boundary=True 说明极值落在扫描边界上，应当扩大区间再扫；极值精度受 grid_step 限制"}


def t_numeric_compare(args):
    if not (HAS_NUMPY and HAS_SYMPY):
        return {"ok": False, "error": "需要 numpy + sympy"}
    names = [v[0] for v in args["vars"]]
    n = int(args.get("samples") or 41)
    tol = float(args.get("tol") or 1e-9)
    params = args.get("params") or {}

    ea, _, fa = _lambdify(args["expr_a"], names, params)
    eb, _, fb = _lambdify(args["expr_b"], names, params)
    sub = {sp.Symbol(k, real=True): sp.sympify(v) for k, v in params.items()}
    ea, eb = ea.subs(sub), eb.subs(sub)

    grids = [np.linspace(float(v[1]), float(v[2]), n) for v in args["vars"]]
    mesh = np.meshgrid(*grids, indexing="ij")
    # 代入参数后重新 lambdify，避免自由符号残留
    fa = sp.lambdify([sp.Symbol(s, real=True) for s in names], ea, "numpy")
    fb = sp.lambdify([sp.Symbol(s, real=True) for s in names], eb, "numpy")
    va = np.asarray(fa(*mesh), dtype=float)
    vb = np.asarray(fb(*mesh), dtype=float)
    shape = mesh[0].shape
    # 常数表达式（如 expr_b='1'）会是 0 维，先广播到网格形状再逐点比
    va = np.broadcast_to(va, shape)
    vb = np.broadcast_to(vb, shape)
    denom = np.maximum(np.abs(va), 1e-12)
    rel = np.abs(va - vb) / denom
    idx = np.unravel_index(np.nanargmax(rel), rel.shape)
    worst = {names[k]: float(mesh[k][idx]) for k in range(len(names))}
    max_rel = float(rel[idx])
    return {"ok": True, "max_rel_err": max_rel, "at": worst,
            "tol": tol, "pass": bool(max_rel <= tol),
            "a_at_worst": float(va[idx]), "b_at_worst": float(vb[idx])}


def t_html_to_pdf(args):
    html = args["html"]
    if not os.path.isfile(html):
        return {"ok": False, "error": f"HTML 不存在: {html}"}
    pdf = args.get("pdf") or (os.path.splitext(html)[0] + ".pdf")
    browser = _which_browser(args.get("browser"))
    if not browser:
        return {"ok": False, "error": "没找到 Edge/Chrome，可用 browser 参数显式指定"}

    profile = os.path.join(tempfile.gettempdir(), "mechio_pdf_profile")
    if os.path.exists(pdf):
        os.remove(pdf)
    cmd = [browser, "--headless=new", "--disable-gpu", "--no-first-run",
           "--no-default-browser-check", f"--user-data-dir={profile}",
           "--no-pdf-header-footer", "--print-to-pdf-no-header",
           f"--print-to-pdf={pdf}",
           "file:///" + os.path.abspath(html).replace("\\", "/").lstrip("/")]
    try:
        p = subprocess.run(cmd, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, timeout=240)
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "浏览器打印超时"}
    if not os.path.isfile(pdf):
        return {"ok": False, "error": "PDF 未生成", "returncode": p.returncode, "browser": browser}
    return {"ok": True, "pdf": pdf, "size": os.path.getsize(pdf),
            "browser": browser, "returncode": p.returncode}


def t_submission_pack(args):
    action = args["action"]
    root = args["root"]

    if action == "init":
        team = args.get("team") or "AIC-2026-00000000"
        name = args.get("name") or "演练队"
        problem = args.get("problem") or "命题式赛题1"
        folder = f"{team}-{problem}-{name}"
        base = os.path.join(root, folder)
        ids = [f"{team}-{problem}"]
        dirs = [base,
                os.path.join(base, "图"),
                os.path.join(base, ids[0] + "-复现包"),
                os.path.join(base, ids[0] + "-复现包", "scripts"),
                os.path.join(base, ids[0] + "-复现包", "report")]
        for d in dirs:
            os.makedirs(d, exist_ok=True)
        files = {
            os.path.join(base, ids[0] + "-答案文件.md"): "# 答案文件\n\n> 待填写\n",
            os.path.join(base, ids[0] + "-过程日志.md"): "# 过程日志\n\n| 阶段 | 动作 | 结果 |\n|---|---|---|\n",
        }
        created = []
        for f, content in files.items():
            if not os.path.exists(f):
                with open(f, "w", encoding="utf-8") as fh:
                    fh.write(content)
                created.append(f)
        return {"ok": True, "folder": base, "dirs": dirs, "files_created": created,
                "note": "文件名已按 <编号>-<命题>-<材料> 规范；技术报告 PDF 用 html_to_pdf 生成"}

    if action == "manifest":
        if not os.path.isdir(root):
            return {"ok": False, "error": f"目录不存在: {root}"}
        items = []
        total = 0
        for dirpath, _, filenames in os.walk(root):
            for fn in filenames:
                fp = os.path.join(dirpath, fn)
                rel = os.path.relpath(fp, root).replace("\\", "/")
                size = os.path.getsize(fp)
                total += size
                items.append({"path": rel, "size": size, "sha256": _sha256(fp)})
        out = os.path.join(root, "manifest.json")
        payload = {"root": root, "count": len(items), "total_bytes": total,
                   "files": sorted(items, key=lambda x: x["path"])}
        with open(out, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=1)
        return {"ok": True, "manifest": out, "count": len(items),
                "total_bytes": total, "total_mb": round(total / 1024 / 1024, 2)}

    return {"ok": False, "error": f"未知 action: {action}"}


HANDLERS = {
    "io_info": t_io_info,
    "py_run": t_py_run,
    "img_crop": t_img_crop,
    "pdf_page_crop": t_pdf_page_crop,
    "fig_lint": t_fig_lint,
    "plot_audit": t_plot_audit,
    "scan_extremum": t_scan_extremum,
    "numeric_compare": t_numeric_compare,
    "html_to_pdf": t_html_to_pdf,
    "submission_pack": t_submission_pack,
}


def call_tool(name, args):
    fn = HANDLERS.get(name)
    if fn is None:
        return {"ok": False, "error": f"未知工具: {name}"}
    try:
        return fn(args or {})
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "error": f"{type(e).__name__}: {e}",
                "trace": traceback.format_exc(limit=3)}


def send(payload):
    _OUT.write(json.dumps(payload, ensure_ascii=False) + "\n")
    _OUT.flush()


def main():
    sys.stderr.write(f"[{SERVER_NAME}] 启动，python {sys.version.split()[0]}\n")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except Exception as e:  # noqa: BLE001
            sys.stderr.write(f"[{SERVER_NAME}] 非法 JSON: {e}\n")
            continue

        mid = msg.get("id")
        method = msg.get("method")

        if method == "initialize":
            send({"jsonrpc": "2.0", "id": mid, "result": {
                "protocolVersion": msg.get("params", {}).get("protocolVersion", "2024-11-05"),
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": SERVER_NAME, "version": VERSION},
            }})
        elif method == "notifications/initialized":
            continue
        elif method == "tools/list":
            send({"jsonrpc": "2.0", "id": mid, "result": {"tools": TOOLS}})
        elif method == "tools/call":
            p = msg.get("params") or {}
            res = call_tool(p.get("name"), p.get("arguments"))
            send({"jsonrpc": "2.0", "id": mid, "result": {
                "content": [{"type": "text", "text": json.dumps(res, ensure_ascii=False, indent=1)}],
                "isError": not res.get("ok", False),
            }})
        elif mid is not None:
            send({"jsonrpc": "2.0", "id": mid,
                  "error": {"code": -32601, "message": f"不支持的方法: {method}"}})


if __name__ == "__main__":
    main()

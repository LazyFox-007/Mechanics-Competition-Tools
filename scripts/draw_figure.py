# -*- coding: utf-8 -*-
"""draw_figure.py —— 按 JSON 描述画力学示意图（现场 B 方案）

用途：纸质赛题不能拍照时，用户用文字描述图形，
      本脚本把描述画成干净示意图，用户肉眼比对纸面图后指出差异。
      即"我复述 → 你核对"的可视化版本。

用法：
    python draw_figure.py --spec spec.json --out fig.png
    python draw_figure.py --json '{"elements":[...]}' --out fig.png

spec 结构：
{
  "title": "第3题 组合梁（可省）",
  "size": [10, 5],                      # 画布英寸，可省
  "xlim": [0, 10], "ylim": [-1, 5],     # 可省，默认按元素自动
  "elements": [ {...}, ... ]
}

元素类型：
  ground   {x1,x2,y}                       地面/基线（带斜线阴影）
  beam     {p1,p2,width?}                  杆/梁
  curved   {center,r,a1,a2}                圆弧杆
  support  {kind,at,angle?}                kind: fixed|pin|roller|spring|free
  node     {at,label}                      节点小圆 + 字母
  force    {at,dir,label?,value?}          集中力箭头
  dist     {p1,p2,dir,label?,kind?}        分布载荷 kind: uniform(默认)|triangle
  moment   {at,label,cw?}                  力偶（弧箭头）
  dim      {p1,p2,offset,label}            尺寸线
  block    {at,w,h,angle?,label?}          物块/矩形
  circle   {at,r,label?,dashed?}           圆轮/滑轮
  hatch    {p1,p2}                         固定端斜线
  text     {at,s,size?}                    注记
  angle    {at,r,a1,a2,label}              角度标注

约定：x 向右、y 向上；坐标单位任意（等比绘制）。
"""
import argparse
import io
import json
import math
import os
import re
import sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Polygon, Rectangle, Wedge

# ── 中文字体 ──────────────────────────────────────────────
_CJK_CANDIDATES = [
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\msyhbd.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
    r"C:\Windows\Fonts\simsun.ttc",
]


def _setup_font():
    from matplotlib import font_manager
    for p in _CJK_CANDIDATES:
        if os.path.isfile(p):
            try:
                font_manager.fontManager.addfont(p)
                name = font_manager.FontProperties(fname=p).get_name()
                plt.rcParams["font.sans-serif"] = [name] + plt.rcParams["font.sans-serif"]
                plt.rcParams["axes.unicode_minus"] = False
                return name
            except Exception:  # noqa: BLE001
                continue
    return None


FONT = _setup_font()

LW = 1.8
CLR = "black"


def _arrow(ax, p0, p1, color=CLR, lw=LW, style="-|>", ms=14, shrink=0, ls="-"):
    a = FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=ms,
                        lw=lw, color=color, shrinkA=shrink, shrinkB=shrink,
                        linestyle=ls, zorder=5)
    ax.add_patch(a)


# ── 文字：unicode 上下标自动转 mathtext ──────────────────
_SUB = dict(zip("\u2080\u2081\u2082\u2083\u2084\u2085\u2086\u2087\u2088\u2089", "0123456789"))
_SUP = dict(zip("\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079", "0123456789"))


_CJK_RE = re.compile(r"[\u3400-\u9fff\u3000-\u303f\uff00-\uffef]")


def fix_text(s):
    """把 q\u2082 / P\u00b2 这类 unicode 上下标转成 mathtext。

    只对**不含汉字**的词包 $...$：mathtext 没有 CJK 字形，
    整串包进去反而会把中文吃掉（实测过）。
    """
    if not isinstance(s, str) or "$" in s:
        return s
    if not any(c in _SUB or c in _SUP for c in s):
        return s

    def conv(tok):
        return "".join(("_{%s}" % _SUB[c]) if c in _SUB
                       else ("^{%s}" % _SUP[c]) if c in _SUP else c
                       for c in tok)

    out = []
    for tok in re.split(r"(\s+)", s):
        if tok and any(c in _SUB or c in _SUP for c in tok) and not _CJK_RE.search(tok):
            out.append("$%s$" % conv(tok))
        else:
            out.append(tok)
    return "".join(out)


def _txt(ax, x, y, s, **kw):
    return ax.text(x, y, fix_text(s), **kw)


def _unit(v):
    n = math.hypot(v[0], v[1])
    if n < 1e-12:
        return (0.0, -1.0)
    return (v[0] / n, v[1] / n)


# ── 各元素绘制 ────────────────────────────────────────────
def e_ground(ax, el):
    x1, x2, y = el.get("x1", 0), el["x2"], el.get("y", 0)
    ax.plot([x1, x2], [y, y], color=CLR, lw=LW, zorder=3)
    step = (x2 - x1) / max(2, int(abs(x2 - x1) / 0.45))
    h = 0.16 * max(1.0, abs(x2 - x1) / 10)
    for x in np.arange(x1, x2 + 1e-9, step):
        ax.plot([x, x - h], [y, y - h], color=CLR, lw=1.0, zorder=3)


def e_beam(ax, el):
    p1, p2 = el["p1"], el["p2"]
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=CLR,
            lw=el.get("width", 3.2), solid_capstyle="round", zorder=4)


def e_curved(ax, el):
    c, r = el["center"], el["r"]
    ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=el.get("a1", 0),
                     theta2=el.get("a2", 180), lw=3.2, color=CLR, zorder=4))


def e_support(ax, el):
    kind = el.get("kind", "pin")
    x, y = el["at"]
    s = el.get("scale", 1.0)
    w, hh = 0.30 * s, 0.34 * s
    if kind == "fixed":
        ax.plot([x, x], [y - hh, y + hh], color=CLR, lw=3.4, zorder=6)
        for yy in np.linspace(y - hh * 0.9, y + hh * 0.9, 6):
            ax.plot([x, x - w * 0.9], [yy, yy - w * 0.55], color=CLR, lw=1.1, zorder=5)
    elif kind in ("pin", "roller"):
        tri = Polygon([[x, y], [x - w, y - hh], [x + w, y - hh]],
                      closed=True, fill=False, lw=LW, ec=CLR, zorder=6)
        ax.add_patch(tri)
        if kind == "pin":
            ax.plot([x - w * 1.3, x + w * 1.3], [y - hh, y - hh], color=CLR, lw=LW, zorder=5)
            for xx in np.linspace(x - w * 1.2, x + w * 1.2, 5):
                ax.plot([xx, xx - w * 0.4], [y - hh, y - hh - w * 0.42], color=CLR, lw=1.0, zorder=5)
        else:
            for dx in (-w * 0.55, w * 0.55):
                ax.add_patch(Circle((x + dx, y - hh - w * 0.28), w * 0.26,
                                    fill=False, lw=1.4, ec=CLR, zorder=6))
            ax.plot([x - w * 1.5, x + w * 1.5], [y - hh - w * 0.56, y - hh - w * 0.56],
                    color=CLR, lw=LW, zorder=5)
    elif kind == "spring":
        n, amp = 6, 0.13 * s
        ys = np.linspace(y - 0.9 * s, y, n * 2 + 1)
        xs = [x] + [x + (amp if i % 2 else -amp) for i in range(1, len(ys) - 1)] + [x]
        ax.plot(xs, ys, color=CLR, lw=1.5, zorder=6)
        ax.plot([x - 0.3 * s, x + 0.3 * s], [y - 0.9 * s, y - 0.9 * s], color=CLR, lw=LW, zorder=5)


def e_node(ax, el):
    x, y = el["at"]
    ax.add_patch(Circle((x, y), el.get("r", 0.072), fill=False, lw=1.6, ec=CLR, zorder=7))
    lb = el.get("label")
    if lb:
        off = el.get("label_off", [0.11, 0.13])
        _txt(ax, x + off[0], y + off[1], lb, fontsize=14, zorder=8, ha="left", va="bottom")


def e_force(ax, el):
    x, y = el["at"]
    d = _unit(el.get("dir", [0, 1]))
    ln = el.get("len", 1.0)
    tip = (x + d[0] * ln, y + d[1] * ln)
    _arrow(ax, (x, y), tip)
    lb = el.get("label")
    val = el.get("value")
    txt = " ".join([t for t in (lb, val) if t])
    if txt:
        _txt(ax, tip[0] + d[0] * 0.12, tip[1] + d[1] * 0.12, txt,
                fontsize=13, ha="center", va="center", zorder=9)


def e_dist(ax, el):
    p1, p2 = np.array(el["p1"], float), np.array(el["p2"], float)
    d = np.array(_unit(el.get("dir", [0, -1])))
    n = el.get("n", 7)
    hmax = el.get("len", 1.0)
    tri = el.get("kind", "uniform") == "triangle"
    rows = []
    for t in np.linspace(0, 1, n):
        p = p1 + (p2 - p1) * t
        h = hmax * ((1 - t) if tri else 1.0)
        tip = p + d * h
        rows.append((p, tip, h))
        if h > 1e-9:
            _arrow(ax, tuple(p), tuple(tip), lw=1.4, ms=10)
    # 三角形载荷画斜边；均布默认不画线（梁本身就是基线），el["line"]=true 才画
    if tri or el.get("line"):
        ax.plot([r[1][0] for r in rows], [r[1][1] for r in rows],
                color=CLR, lw=1.5, zorder=4)
    lb = el.get("label")
    if lb:
        mid = rows[len(rows) // 2][1]
        _txt(ax, mid[0] + d[0] * 0.20, mid[1] + d[1] * 0.20, lb,
                fontsize=13, ha="center", va="center", zorder=9)


def e_moment(ax, el):
    x, y = el["at"]
    r = el.get("r", 0.38)
    cw = el.get("cw", False)
    # 270° 圆弧：CCW 从 130° 扫到 400°，CW 反之（用连续角参数，避免 Arc 取模问题）
    a1, a2 = (130.0, 400.0) if not cw else (400.0, 130.0)
    th = np.radians(np.linspace(a1, a2, 90))
    xs, ys = x + r * np.cos(th), y + r * np.sin(th)
    ax.plot(xs, ys, color=CLR, lw=1.8, zorder=7)
    # 箭头沿着圆弧前进方向
    t0 = th[-1]
    tx, ty = -math.sin(t0), math.cos(t0)
    if cw:
        tx, ty = -tx, -ty
    _arrow(ax, (xs[-1] - tx * r * 0.5, ys[-1] - ty * r * 0.5), (xs[-1], ys[-1]),
           ms=13, lw=1.4)
    lb = el.get("label")
    if lb:
        am = (a1 + a2) / 2.0
        _txt(ax, x + (r + 0.26) * math.cos(math.radians(am)),
                y + (r + 0.26) * math.sin(math.radians(am)),
                lb, fontsize=13, ha="center", va="center", zorder=9)


def e_taper(ax, el):
    """圆台/锥台（侧视）。at=底心，h=高，r1=底半宽，r2=顶半宽；angle=轴线方向(默认90=竖直向上)"""
    x, y = el["at"]
    h = el.get("h", 3.0)
    r1 = el.get("r1", 1.0)
    r2 = el.get("r2", 0.5)
    ang = math.radians(el.get("angle", 90))
    ux, uy = math.cos(ang), math.sin(ang)          # 轴向单位矢
    px, py = -uy, ux                               # 横向单位矢
    bx1 = (x + px * r1, y + py * r1)
    bx2 = (x - px * r1, y - py * r1)
    tx1 = (x + ux * h + px * r2, y + uy * h + py * r2)
    tx2 = (x + ux * h - px * r2, y + uy * h - py * r2)
    poly = Polygon([bx1, bx2, tx2, tx1], closed=True,
                   fill=bool(el.get("fill")), fc=el.get("fill") or "none",
                   alpha=el.get("alpha", 0.28), lw=el.get("lw", LW),
                   ec=CLR, zorder=4)
    ax.add_patch(poly)
    if el.get("label"):
        _txt(ax, x + ux * h * 0.5 + px * (max(r1, r2) + 0.25),
             y + uy * h * 0.5 + py * (max(r1, r2) + 0.25),
             el["label"], fontsize=12, ha="left", va="center", zorder=9)


def e_rope(ax, el):
    p1, p2 = el["p1"], el["p2"]
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=CLR, lw=1.4,
            ls="--" if el.get("dashed") else "-", zorder=4)
    if el.get("label"):
        _txt(ax, (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 + 0.18, el["label"],
                fontsize=12, ha="center", va="bottom", zorder=9)


def e_incline(ax, el):
    p1, p2 = np.array(el["p1"], float), np.array(el["p2"], float)
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=CLR, lw=3.0, zorder=4)
    # 斜面下方斜线阴影
    v = p2 - p1
    nrm = np.array([v[1], -v[0]], float)
    nrm = nrm / (np.linalg.norm(nrm) + 1e-12) * 0.16
    for t in np.linspace(0.04, 0.96, el.get("n", 9)):
        p = p1 + v * t
        ax.plot([p[0], p[0] - nrm[0]], [p[1], p[1] - nrm[1]],
                color=CLR, lw=1.0, zorder=3)


def e_dim(ax, el):
    p1, p2 = np.array(el["p1"], float), np.array(el["p2"], float)
    off = el.get("offset", 0.6)
    v = p2 - p1
    n = np.array([-v[1], v[0]])
    nn = n / (np.linalg.norm(n) + 1e-12) * off
    a, b = p1 + nn, p2 + nn
    ax.plot([a[0], b[0]], [a[1], b[1]], color=CLR, lw=1.1, zorder=6)
    _arrow(ax, tuple(a), tuple(b), style="<|-|>", ms=10, lw=1.0)
    for p, q in ((p1, a), (p2, b)):
        ax.plot([p[0], q[0] + nn[0] * 0.18], [p[1], q[1] + nn[1] * 0.18],
                color=CLR, lw=0.9, ls=(0, (3, 3)), zorder=5)
    mid = (a + b) / 2 + nn / (np.linalg.norm(nn) + 1e-12) * 0.22
    _txt(ax, mid[0], mid[1], el.get("label", ""), fontsize=13, ha="center", va="center", zorder=9)


def e_block(ax, el):
    x, y = el["at"]
    w, h = el.get("w", 1.0), el.get("h", 0.6)
    ang = el.get("angle", 0)
    fill = el.get("fill")
    box = Rectangle((x - w / 2, y - h / 2), w, h,
                    fill=bool(fill), fc=fill or "none",
                    alpha=el.get("alpha", 0.35 if fill else 1.0),
                    lw=el.get("lw", LW), ec=el.get("ec", CLR),
                    ls=el.get("ls", "-"))
    tr = matplotlib.transforms.Affine2D().rotate_deg_around(x, y, ang) + ax.transData
    box.set_transform(tr)
    ax.add_patch(box)
    lb = el.get("label")
    if lb:
        _txt(ax, x, y, lb, fontsize=13, ha="center", va="center", zorder=9)


def e_circle(ax, el):
    x, y = el["at"]
    r = el.get("r", 0.5)
    ax.add_patch(Circle((x, y), r, fill=False, lw=LW, ec=CLR,
                        ls="--" if el.get("dashed") else "-", zorder=6))
    if el.get("label"):
        _txt(ax, x, y, el["label"], fontsize=13, ha="center", va="center", zorder=9)
    if el.get("radius_line"):
        _arrow(ax, (x, y), (x + r, y), ms=10, lw=1.0)


def e_hatch(ax, el):
    p1, p2 = el["p1"], el["p2"]
    n = el.get("n", 6)
    for t in np.linspace(0, 1, n):
        p = (p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t)
        ax.plot([p[0], p[0] - 0.22], [p[1], p[1] - 0.22], color=CLR, lw=1.0, zorder=5)


def e_text(ax, el):
    _txt(ax, el["at"][0], el["at"][1], el.get("s", ""),
            fontsize=el.get("size", 13), ha=el.get("ha", "left"),
            va=el.get("va", "center"), zorder=9)


def e_angle(ax, el):
    c, r = el["at"], el.get("r", 0.6)
    ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=el.get("a1", 0), theta2=el.get("a2", 45),
                     lw=1.3, color=CLR, zorder=6))
    am = math.radians((el.get("a1", 0) + el.get("a2", 45)) / 2)
    _txt(ax, c[0] + (r + 0.18) * math.cos(am), c[1] + (r + 0.18) * math.sin(am),
            el.get("label", ""), fontsize=12, ha="center", va="center", zorder=9)


DISPATCH = {
    "ground": e_ground, "beam": e_beam, "curved": e_curved, "support": e_support,
    "node": e_node, "force": e_force, "dist": e_dist, "moment": e_moment,
    "dim": e_dim, "block": e_block, "circle": e_circle, "hatch": e_hatch,
    "text": e_text, "angle": e_angle, "rope": e_rope, "incline": e_incline,
    "taper": e_taper,
}


def check_layout(fig, ax):
    """渲染后自检：标签互相重叠 / 超出画布 / 缺字形。返回警告列表。"""
    from matplotlib.transforms import Bbox as _BB
    fig.canvas.draw()
    try:
        ren = fig.canvas.get_renderer()
    except Exception:  # noqa: BLE001
        return []
    items = []
    for t_ in ax.texts:
        s = (t_.get_text() or "").strip()
        if not s or s.startswith("$") is False and not s:
            continue
        try:
            bb = t_.get_window_extent(renderer=ren)
        except Exception:  # noqa: BLE001
            continue
        if bb.width <= 0 or bb.height <= 0:
            continue
        items.append((s, bb))
    warns = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            s1, b1 = items[i]
            s2, b2 = items[j]
            inter = _BB.intersection(b1, b2)
            if inter is None:
                continue
            ai = max(0.0, inter.width) * max(0.0, inter.height)
            small = min(b1.width * b1.height, b2.width * b2.height)
            if small > 0 and ai / small > 0.12:
                warns.append("标签重叠 %2d%%  「%s」×「%s」"
                             % (round(ai / small * 100), s1[:18], s2[:18]))
    try:
        fx = fig.get_window_extent(ren)
        for s, bb in items:
            if bb.x0 < fx.x0 - 2 or bb.x1 > fx.x1 + 2 or bb.y0 < fx.y0 - 2 or bb.y1 > fx.y1 + 2:
                warns.append("超出画布  「%s」" % s[:24])
    except Exception:  # noqa: BLE001
        pass
    return warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", help="spec JSON 文件路径")
    ap.add_argument("--json", help="spec JSON 字符串")
    ap.add_argument("--out", required=True, help="输出 PNG")
    ap.add_argument("--dpi", type=int, default=160)
    a = ap.parse_args()

    if a.spec:
        spec = json.loads(io.open(a.spec, encoding="utf-8").read())
    elif a.json:
        spec = json.loads(a.json)
    else:
        print("错误: 需要 --spec 或 --json")
        return 2

    els = spec.get("elements", [])
    if not els:
        print("错误: elements 为空")
        return 2

    unknown = [e.get("type") for e in els if e.get("type") not in DISPATCH]
    if unknown:
        print("警告: 未知元素类型 %s（已跳过）" % sorted(set(unknown)))

    w, h = spec.get("size", [11, 5.6])
    fig, ax = plt.subplots(figsize=(w, h))
    for el in els:
        fn = DISPATCH.get(el.get("type"))
        if fn:
            try:
                fn(ax, el)
            except Exception as exc:  # noqa: BLE001
                print("元素绘制失败 %r: %r" % (el.get("type"), exc))

    xs, ys = [], []
    for el in els:
        for k in ("p1", "p2", "at", "center"):
            if k in el:
                v = el[k]
                if isinstance(v, (list, tuple)) and len(v) == 2:
                    xs.append(v[0]); ys.append(v[1])
        for k in ("x1", "x2"):
            if k in el:
                xs.append(el[k])
        if "y" in el:
            ys.append(el["y"])
    if spec.get("xlim"):
        ax.set_xlim(*spec["xlim"])
    elif xs:
        ax.set_xlim(min(xs) - 1.2, max(xs) + 1.2)
    if spec.get("ylim"):
        ax.set_ylim(*spec["ylim"])
    elif ys:
        ax.set_ylim(min(ys) - 1.0, max(ys) + 1.4)

    ax.set_aspect("equal", adjustable="datalim")
    ax.axis("off")
    if spec.get("title"):
        ax.set_title(spec["title"], fontsize=15, pad=12)

    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    fig.tight_layout()
    warns = check_layout(fig, ax)
    import warnings as _w
    with _w.catch_warnings(record=True) as caught:
        _w.simplefilter("always")
        fig.savefig(a.out, dpi=a.dpi, bbox_inches="tight", facecolor="white")
    glyph = [str(c.message) for c in caught
             if "missing from current font" in str(c.message) or "Glyph" in str(c.message)]
    plt.close(fig)
    print("已出图: %s  (%dx%d)" % (a.out, *[int(v * a.dpi) for v in fig.get_size_inches()]))
    print("字体: %s" % (FONT or "未找到中文字体，中文可能显示为方块"))
    print("元素 %d 个，类型: %s" % (len(els), sorted({e.get('type') for e in els})))
    if glyph:
        print("缺字形警告 %d 条（会渲染成方块）:" % len(glyph))
        for g in sorted(set(glyph))[:6]:
            print("   ", g[:110])
    if warns:
        print("版式警告 %d 条:" % len(warns))
        for w in warns[:12]:
            print("   ", w)
    else:
        print("版式自检: 无标签重叠、无出界 ✓")
    return 0


if __name__ == "__main__":
    sys.exit(main())

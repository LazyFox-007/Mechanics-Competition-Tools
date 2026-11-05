# -*- coding: utf-8 -*-
"""mech-model 回归测试。

靶子是第十四、十五届两次实测里**真实犯过的错**，不是编的用例。
判据：这 4 个错必须全部 block；正确声明必须全部 pass（不许误报）。
"""
import json
import os
import sys

# 换环境时控制台可能是 GBK，中文输出会 UnicodeEncodeError
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))          # -> mcp/mech-model
import core  # noqa: E402

PASS, FAIL = 0, 0


def t(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("  PASS  %s" % name)
    else:
        FAIL += 1
        print("  FAIL  %s   %s" % (name, detail))


def chk(pid, dec):
    return core.dispatch({"action": "check", "problem_class": pid, "decisions": dec})


def codes(r):
    return [v["code"] for v in r["violations"]]


def axes_of(pid):
    return [a["id"] for a in core._merged_axes(pid)]


def baseline(pid, overrides=None):
    """把每条轴填成它的第一个选项 + evidence=derived，再按需覆盖。"""
    d = {}
    for a in core._merged_axes(pid):
        d[a["id"]] = {"value": a["options"][0], "evidence": "derived"}
    for k, v in (overrides or {}).items():
        d[k] = v
    return d


# ────────────────────────── 0. 规模 ──────────────────────────
print("=== 0. 卡库规模 ===")
idx = core.dispatch({"action": "index"})
with open(os.path.join(os.path.dirname(HERE), "cards.json"), encoding="utf-8") as _f:
    N_CARDS = len(json.load(_f)["cards"])
print("  版本 %s | 卡片 %d 张 | 通用轴 %d 条"
      % (idx["version"], len(idx["cards"]), len(idx["common_axes"])))
for c in idx["cards"]:
    print("    %-24s %s" % (c["id"], c["name"]))
t("卡片数与 cards.json 一致", len(idx["cards"]) == N_CARDS, (len(idx["cards"]), N_CARDS))
t("卡片数 >= 30（题型覆盖未退化）", N_CARDS >= 30, N_CARDS)
t("通用轴 = 5", len(idx["common_axes"]) == 5, idx["common_axes"])

# ────────────────────────── 1. probe ──────────────────────────
print("\n=== 1. probe 命中 ===")
probes = [
    ("rail_vehicle", "列车轮对由两个刚性轮和一根刚性轴固结而成，车轮简化为顶角为2α的锥面体，"
                     "轨道相距2b，轮对侧移y与转角ψ，蠕滑力，滚动半径"),
    ("floating_stability", "运载火箭和海上回收平台简化为两个叠放共轴均质圆柱，漂浮于海水中，"
                           "排水体积，吃水，竖直平衡状态稳定，稳心，微幅运动"),
    ("sliding_block_on_beam", "梁AB的A端放置重量为G的滑块，滑块与梁之间滑动摩擦因数μ，"
                              "刚好滑到梁的中点静止，滑出B端时速度"),
    ("column_buckling", "杆BD为细长杆，恰好使滑块开始下滑且杆BD没有失稳，求弯曲刚度应满足的条件"),
]
for want, text in probes:
    pr = core.dispatch({"action": "probe", "text": text})
    top = pr["candidates"][0]["id"] if pr["candidates"] else None
    print("  %-24s -> %s" % (want, top))
    t("probe 命中 %s" % want, top == want, pr["candidates"])

# ────────────────────────── 2. 真实错题必须 block ──────────────────────────
print("\n=== 2. 第十四届第6题：我当时的两条沉默默认 ===")
d14 = baseline("rail_vehicle", {
    "figure_transcribed": {"value": "只看过整页", "evidence": "assumed"},
    "cone_taper": {"value": "半径向外侧增大", "evidence": "assumed"},
    "axle_tilt": {"value": "假定轴线始终水平", "evidence": "assumed"},
})
r = chk("rail_vehicle", d14)
print("  verdict=%s err=%d" % (r["verdict"], r["n_error"]))
for v in r["violations"]:
    print("    [%-18s] %s" % (v["code"], v["message"][:66]))
t("14届6 判 block", r["verdict"] == "block")
t("14届6 报出锥度未论证", any(v.get("axis") == "cone_taper" and v["code"] == "UNARGUED" for v in r["violations"]))
t("14届6 报出轴线未论证", any(v.get("axis") == "axle_tilt" and v["code"] == "UNARGUED" for v in r["violations"]))
t("14届6 报出读图未确认", any(v.get("axis") == "figure_transcribed" and v["code"] == "UNARGUED" for v in r["violations"]))

print("\n=== 3. 第十五届第6题：三条建模轴 ===")
d15 = baseline("sliding_block_on_beam", {
    "stop_criterion": {"value": "准静态：局部斜率降到摩擦角即停", "evidence": "assumed"},
    "inertia_scope": {"value": "连动能也丢掉", "evidence": "assumed"},
    "staged_condition": {"value": "默认消失", "evidence": "assumed"},
})
r = chk("sliding_block_on_beam", d15)
print("  verdict=%s err=%d" % (r["verdict"], r["n_error"]))
for v in r["violations"]:
    print("    [%-18s] %s" % (v["code"], v["message"][:66]))
t("15届6 判 block", r["verdict"] == "block")
t("15届6 报出『准静态 vs 能量法』", any(v["code"] == "CONFLICT" and "能量条件" in v["message"] for v in r["violations"]))
t("15届6 报出『动能不能丢』", any(v["code"] == "CONFLICT" and "动能" in v["message"] for v in r["violations"]))
t("15届6 报出条件继承未论证", any(v.get("axis") == "staged_condition" and v["code"] == "UNARGUED" for v in r["violations"]))

print("\n=== 4. 第十五届第6题：压杆把铰支读成固支 ===")
dmu = baseline("column_buckling", {
    "end_condition": {"value": "一端固支一端铰", "evidence": "figure"},
    "figure_transcribed": {"value": "只看过整页", "evidence": "assumed"},
})
r = chk("column_buckling", dmu)
print("  verdict=%s err=%d" % (r["verdict"], r["n_error"]))
for v in r["violations"]:
    print("    [%-18s] %s" % (v["code"], v["message"][:78]))
t("压杆 μ 判 block", r["verdict"] == "block")
t("压杆 报出『空心圆=铰支』",
  any(v["code"] == "CONFLICT" and "空心圆" in v["message"] for v in r["violations"]))

print("\n=== 5. 第十五届第5题：浮体质心取界面 ===")
df = baseline("floating_stability", {
    "cg_from_parts": {"value": "取两段界面", "evidence": "assumed"},
    "waterplane_inertia": {"value": "排水体", "evidence": "derived"},
})
r = chk("floating_stability", df)
print("  verdict=%s err=%d" % (r["verdict"], r["n_error"]))
for v in r["violations"]:
    print("    [%-18s] %s" % (v["code"], v["message"][:66]))
t("浮体 判 block", r["verdict"] == "block")
t("浮体 报出 BM 的 I 取错", any(v["code"] == "CONFLICT" and "水线面" in v["message"] for v in r["violations"]))

# ────────────────────────── 6. 正确声明必须 pass ──────────────────────────
print("\n=== 6. 正确声明必须 pass（不许误报）===")
FIX = {
    # 卡片语义上要求覆盖默认值的地方
    "curved_member_impact": {"point_stress": {"value": "弯+扭(平面应力)", "evidence": "derived"}},
    "large_deflection": {"small_deflection": {"value": "large", "evidence": "derived"}},
    "rail_vehicle": {
        "figure_transcribed": {"value": "已逐项转写并放大确认", "evidence": "figure"},
        "cone_taper": {"value": "半径向辋内(法兰侧)增大", "evidence": "figure"},
        "axle_tilt": {"value": "允许倾斜,且与侧移满足几何关系", "evidence": "derived"},
    },
    "floating_stability": {
        "figure_transcribed": {"value": "已逐项转写并放大确认", "evidence": "figure"},
        "cg_from_parts": {"value": "已加权算出并写成坐标", "evidence": "derived"},
        "waterplane_inertia": {"value": "水线面 πr⁴/4(半径取水线处)", "evidence": "textbook"},
        "gm_criterion": {"value": "初稳性 GM=BM−BG>0", "evidence": "textbook"},
        "dof_coupling": {"value": "轴对称⇒一阶解耦", "evidence": "derived"},
        "roll_inertia_point": {"value": "绕总质心的水平轴", "evidence": "derived"},
    },
    "sliding_block_on_beam": {
        "figure_transcribed": {"value": "已逐项转写并放大确认", "evidence": "figure"},
        "stop_criterion": {"value": "能量法：到该处速度为零", "evidence": "statement"},
        "inertia_scope": {"value": "只忽略静力平衡中的惯性项，动能保留", "evidence": "derived"},
        "load_position": {"value": "位置随滑块移动，逐点列弯矩", "evidence": "derived"},
        "support_stiffness": {"value": "已折算 k=EA/a，且判定为静定(反力与 k 无关)", "evidence": "derived"},
        "friction_work": {"value": "∫μN ds，且 N 随滑块位置变", "evidence": "derived"},
    },
    "column_buckling": {
        "figure_transcribed": {"value": "已逐项转写并放大确认", "evidence": "figure"},
        "end_condition": {"value": "两端铰", "evidence": "figure"},
        "member_scope": {"value": "二力杆(仅轴力)", "evidence": "derived"},
        "mu_vs_sigma": {"value": "临界力/临界应力(稳定问题)", "evidence": "statement"},
        "slenderness": {"value": "已核 λ ≥ λp(大柔度,用欧拉)", "evidence": "derived"},
    },
}
for pid in core.load_cards()["cards"].keys():
    dec = baseline(pid, FIX.get(pid, {}))
    rr = chk(pid, dec)
    errs = [v for v in rr["violations"] if v["level"] == "error"]
    print("  %-24s verdict=%-5s err=%d %s" % (pid, rr["verdict"], rr["n_error"],
                                             [v["message"][:38] for v in errs]))
    t("%s 正确声明 pass" % pid, rr["verdict"] == "pass", errs)

# ────────────────────────── 7. 漏轴 / 非法值 / 未知题型 ──────────────────────────
print("\n=== 7. 边界输入 ===")
short = {"cone_taper": {"value": "半径向辋内(法兰侧)增大", "evidence": "figure"}}
r = chk("rail_vehicle", short)
n_missing = sum(1 for v in r["violations"] if v["code"] == "MISSING")
n_all = len(axes_of("rail_vehicle"))
print("  MISSING=%d / 总轴 %d" % (n_missing, n_all))
t("漏轴全部报 MISSING", n_missing == n_all - 1, n_missing)
t("未知题型报错", core.dispatch({"action": "list", "problem_class": "nope"})["ok"] is False)
t("非法取值报 BAD_VALUE",
  "BAD_VALUE" in codes(chk("rail_vehicle", {"cone_taper": {"value": "乱填", "evidence": "derived"}})))
t("缺 problem_class 报错", core.dispatch({"action": "check", "decisions": {}})["ok"] is False)
t("空 decisions 全报 MISSING",
  sum(1 for v in chk("rail_vehicle", {})["violations"] if v["code"] == "MISSING") == n_all)

print("\n" + "=" * 46)
print("PASS %d / FAIL %d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)

# -*- coding: utf-8 -*-
"""mech-model 回归测试 —— 拿第十四届第 6 题（本次实测最大失分）做靶"""
import json
import os
import sys

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


print("=== 0. index ===")
idx = core.dispatch({"action": "index"})
print("  卡片数 = %d | 通用轴 = %s" % (len(idx["cards"]), idx["common_axes"]))
t("index 返回 6 张卡", len(idx["cards"]) == 6, idx)

print("\n=== 1. probe：第6题题干关键词 ===")
stem = ("列车轮对由两个刚性轮和一根刚性轴固结而成，车轮简化为顶角为2α的锥面体，"
        "轨道简化为相距2b的两条平行线，车轮与轨道为点接触。轮对会发生微小侧向移位y，"
        "和绕通过质心的铅垂轴的微小转角ψ。求滚动半径、侧向恢复力、蠕滑力与运动微分方程。")
pr = core.dispatch({"action": "probe", "text": stem})
print("  候选:", [(c["id"], c["score"]) for c in pr["candidates"]])
t("probe 首选 rail_vehicle",
  pr["candidates"] and pr["candidates"][0]["id"] == "rail_vehicle", pr["candidates"])

print("\n=== 2. 我的真实错误态（两条轴都 assumed）===")
bad = {
    "sign_convention": {"value": "已声明", "evidence": "derived"},
    "small_deflection": {"value": "small", "evidence": "statement"},
    "load_type": {"value": "dead", "evidence": "derived"},
    "cone_taper": {"value": "半径向外侧增大", "evidence": "assumed"},
    "axle_tilt": {"value": "假定轴线始终水平", "evidence": "assumed"},
    "creep_law": {"value": "线性(F=−f·v/vc)", "evidence": "statement"},
    "spin_creep": {"value": "忽略", "evidence": "derived"},
    "frame": {"value": "随质心平动系 + 相对定轴转动系", "evidence": "derived"},
}
r = core.dispatch({"action": "check", "problem_class": "rail_vehicle", "decisions": bad})
print("  verdict=%s  err=%d warn=%d" % (r["verdict"], r["n_error"], r["n_warn"]))
for v in r["violations"]:
    print("    [%s] %-18s %s" % (v["code"], v.get("axis", str(v.get("axes"))), v["message"][:70]))
t("错误态判 block", r["verdict"] == "block")
codes = [v["code"] for v in r["violations"]]
t("报出 cone_taper 未论证", any(v.get("axis") == "cone_taper" and v["code"] == "UNARGUED" for v in r["violations"]))
t("报出 axle_tilt 未论证", any(v.get("axis") == "axle_tilt" and v["code"] == "UNARGUED" for v in r["violations"]))
t("报出锥度方向冲突", "CONFLICT" in codes)
t("总错误 >= 3", r["n_error"] >= 3, r["n_error"])

print("\n=== 3. 半错：锥度对了但轴线仍假定水平 ===")
half = dict(bad)
half["cone_taper"] = {"value": "半径向辋内(法兰侧)增大", "evidence": "figure"}
half["axle_tilt"] = {"value": "假定轴线始终水平", "evidence": "derived"}
r3 = core.dispatch({"action": "check", "problem_class": "rail_vehicle", "decisions": half})
print("  verdict=%s  err=%d" % (r3["verdict"], r3["n_error"]))
for v in r3["violations"]:
    print("    [%s] %s" % (v["code"], v["message"][:80]))
t("半错仍判 block", r3["verdict"] == "block")
t("报出『轴线必然倾斜』", any(v["code"] == "CONFLICT" and "轴线必然倾斜" in v["message"] for v in r3["violations"]))

print("\n=== 4. 正确态应 pass ===")
good = dict(bad)
good["cone_taper"] = {"value": "半径向辋内(法兰侧)增大", "evidence": "figure"}
good["axle_tilt"] = {"value": "允许倾斜,且与侧移满足几何关系", "evidence": "derived"}
r4 = core.dispatch({"action": "check", "problem_class": "rail_vehicle", "decisions": good})
print("  verdict=%s err=%d warn=%d" % (r4["verdict"], r4["n_error"], r4["n_warn"]))
for v in r4["violations"]:
    print("    [%s] %s" % (v["code"], v["message"][:80]))
t("正确态 pass", r4["verdict"] == "pass")
t("filled 含 8 条轴", len(r4["filled"]) == 8, len(r4["filled"]))

print("\n=== 5. 漏轴检查 ===")
short = {"cone_taper": {"value": "半径向辋内(法兰侧)增大", "evidence": "figure"}}
r5 = core.dispatch({"action": "check", "problem_class": "rail_vehicle", "decisions": short})
n_missing = sum(1 for v in r5["violations"] if v["code"] == "MISSING")
print("  MISSING = %d" % n_missing)
t("漏 7 条轴全部报 MISSING", n_missing == 7, n_missing)

print("\n=== 6. 其余 5 张卡不误报（正常填法应 pass）===")
cases = {
    "statics_friction": {
        "sign_convention": {"value": "已声明", "evidence": "derived"},
        "small_deflection": {"value": "small", "evidence": "statement"},
        "load_type": {"value": "dead", "evidence": "derived"},
        "critical_states": {"value": "滑动2种+翻转2种 共4种", "evidence": "derived"},
        "moment_point": {"value": "接触面端点", "evidence": "derived"},
        "joint_type": {"value": "内铰(M=0,不提供反力)", "evidence": "statement"},
    },
    "multibody_lagrange": {
        "sign_convention": {"value": "已声明", "evidence": "derived"},
        "small_deflection": {"value": "small", "evidence": "statement"},
        "load_type": {"value": "dead", "evidence": "derived"},
        "dof_count": {"value": "已消去,自由度=剩余广义坐标数", "evidence": "derived"},
        "inertia_reference": {"value": "定轴转动→对轴心", "evidence": "textbook"},
        "extra_mass": {"value": "两者都计入", "evidence": "derived"},
        "potential_sign": {"value": "V=−mg·h(向下为正高)", "evidence": "statement"},
    },
    "beam_strength": {
        "sign_convention": {"value": "已声明", "evidence": "derived"},
        "small_deflection": {"value": "small", "evidence": "statement"},
        "load_type": {"value": "dead", "evidence": "derived"},
        "section_region": {"value": "已按图示换算成 y 区间", "evidence": "figure"},
        "danger_candidate": {"value": "同时考虑边缘纯弯与中性轴纯剪", "evidence": "textbook"},
        "theory": {"value": "第三(最大切应力)", "evidence": "statement"},
    },
    "curved_member_impact": {
        "sign_convention": {"value": "已声明", "evidence": "derived"},
        "small_deflection": {"value": "small", "evidence": "statement"},
        "load_type": {"value": "dead", "evidence": "derived"},
        "point_stress": {"value": "弯+扭(平面应力)", "evidence": "derived"},
        "gauge_transform": {"value": "完整(εx,εy,γ → ε_θ)", "evidence": "derived"},
        "gap_closed": {"value": "已算位移并与间隙比较", "evidence": "derived"},
        "stiffness_known": {"value": "部分缺失→改用能量/实验量反求", "evidence": "statement"},
        "mu": {"value": "铰-铰 1.0", "evidence": "statement"},
    },
    "large_deflection": {
        "sign_convention": {"value": "已声明", "evidence": "derived"},
        "small_deflection": {"value": "large", "evidence": "derived"},
        "load_type": {"value": "dead", "evidence": "derived"},
        "moment_arm": {"value": "到载荷作用线的垂直距离(死载)", "evidence": "derived"},
        "segmentation": {"value": "已分段,段间 φ 连续、M 连续", "evidence": "derived"},
        "solve_route": {"value": "两者互验", "evidence": "derived"},
        "initial_guess": {"value": "BVP+打靶互验", "evidence": "derived"},
    },
}
for pid, dec in cases.items():
    rr = core.dispatch({"action": "check", "problem_class": pid, "decisions": dec})
    nop = [v for v in rr["violations"] if v["level"] == "error"]
    print("  %-22s verdict=%-5s err=%d %s" % (pid, rr["verdict"], rr["n_error"],
                                              [v["message"][:40] for v in nop]))
    t("%s 正常填法 pass" % pid, rr["verdict"] == "pass", nop)

print("\n=== 7. 非法输入 ===")
t("未知题型报错", core.dispatch({"action": "list", "problem_class": "nope"})["ok"] is False)
t("非法取值报 BAD_VALUE",
  "BAD_VALUE" in [v["code"] for v in core.dispatch(
      {"action": "check", "problem_class": "rail_vehicle",
       "decisions": {"cone_taper": {"value": "乱填", "evidence": "derived"}}})["violations"]])
t("缺 problem_class 报错", core.dispatch({"action": "check", "decisions": {}})["ok"] is False)

print("\n================================")
print("PASS %d / FAIL %d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)

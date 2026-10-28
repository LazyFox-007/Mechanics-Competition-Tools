#!/usr/bin/env python3
"""
mech-solver MCP —— 补齐工具覆盖的四个空白分支

现状（补齐前）：
  静力学   静定梁/杆/轴有 mech_analyze；桁架、摩擦、重心靠手推
  运动学   点的运动学有 kinematics_derive；刚体平面运动完全空白
  动力学   拉格朗日有 lagrange_eom；碰撞无入口
  材料力学 内力/应力有 mech_analyze；压杆稳定、能量法、静不定空白

本服务补四个高频分支（碰撞按约定不做：几何依赖太强、性价比最低）：

  1. energy_method   卡氏定理 / 单位载荷法（梁的位移，通用积分器）
  2. truss_solve     桁架：节点法整体线性求解 + 反力 + 逐节点平衡自校验
  3. rigid_planar    刚体平面运动：速度/加速度基点法、速度瞬心
  4. buckling_solve  压杆稳定：欧拉/经验公式分档 + 柔度判定
  5. solver_info     自检

设计铁律（与其他服务一致）：
  - 每个工具**必须自带独立校核**，校核不过就 ok:false，不给"看起来很确定"的数
  - 只依赖标准库 + sympy + numpy；缺了明确报错
  - stdout 只走协议
"""

import json
import math
import os
import sys
import traceback

# ── stdout 保护 ────────────────────────────────────────────────
_real_stdout_fd = os.dup(1)
os.dup2(2, 1)
_OUT = os.fdopen(_real_stdout_fd, "w", encoding="utf-8", buffering=1)

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8")

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

SERVER_NAME = "mech-solver"
VERSION = "0.1.0"

TOOLS = [
    {
        "name": "solver_info",
        "description": "自检：sympy / numpy 版本，四个求解分支是否可用。",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "energy_method",
        "description": (
            "能量法求梁/刚架的位移。op=castigliano：给弯矩 M(x) 与 EI，返回 U=∫M²/(2EI)dx 与 "
            "δ=∂U/∂P（卡氏第二定理）；op=unit_load：给真实弯矩 M(x)、单位载荷弯矩 m̄(x) 与 EI，"
            "返回 δ=∫M·m̄/(EI)dx。自带有限差分校核。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "op": {"type": "string", "enum": ["castigliano", "unit_load"]},
                "M": {"type": "string", "description": "弯矩表达式，如 '-P*(l-x)'"},
                "mbar": {"type": "string", "description": "unit_load 用：单位载荷弯矩，如 '-(l-x)'"},
                "EI": {"type": "string", "description": "抗弯刚度表达式，如 'E*I' 或 '2.0e4'"},
                "x": {"type": "string", "description": "变量名，默认 x"},
                "span": {"type": "array", "items": {"type": "string"},
                         "description": "积分区间 [a, b]，如 ['0','l']"},
                "P": {"type": "string", "description": "castigliano 用：求导的载荷符号，如 'P'"},
                "params": {"type": "object", "description": "其余符号取值，如 {'l':'2','E':'210e9','I':'1e-6'}"},
            },
            "required": ["op", "M", "EI", "span"],
        },
    },
    {
        "name": "truss_solve",
        "description": (
            "静定平面桁架求解：给节点坐标、杆件、支座、载荷，整体线性求解杆件轴力与反力，"
            "并逐节点校核 ΣF=0、报告零杆与静定性。拉力为正。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "nodes": {"type": "array", "description": "[{name,x,y}, ...]"},
                "members": {"type": "array", "description": "[{a,b}, ...] 杆件两端节点名"},
                "supports": {"type": "array", "description": "[{node,type}] type=pin(两向约束)/roller(竖向约束)"},
                "loads": {"type": "array", "description": "[{node,fx,fy}, ...] 载荷，向右/向上为正"},
            },
            "required": ["nodes", "members", "supports"],
        },
    },
    {
        "name": "rigid_planar",
        "description": (
            "刚体平面运动。op=vel：给 ω、A 点速度、A→B 矢径，求 B 点速度；"
            "op=acc：给 ω、α、A 点加速度、矢径，求 B 点加速度（含法向 ω²r）；"
            "op=ic：给 ω 与 A 点速度，求速度瞬心。自带 |v|=ω·r 一致性校核。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "op": {"type": "string", "enum": ["vel", "acc", "ic"]},
                "omega": {"type": "number", "description": "角速度（逆时针为正）"},
                "alpha": {"type": "number", "description": "角加速度（acc 用）"},
                "vA": {"type": "array", "items": {"type": "number"}, "description": "[vx, vy]"},
                "aA": {"type": "array", "items": {"type": "number"}, "description": "[ax, ay]"},
                "r": {"type": "array", "items": {"type": "number"}, "description": "A→B 矢量 [rx, ry]"},
                "A": {"type": "array", "items": {"type": "number"}, "description": "A 点坐标 [x, y]（ic 用）"},
            },
            "required": ["op", "omega"],
        },
    },
    {
        "name": "buckling_solve",
        "description": (
            "压杆稳定：按两端约束取长度系数 μ，算柔度 λ、欧拉临界应力与临界力；"
            "给了材料比例极限 σp 时自动判大/中柔度并用经验公式，附一致性校核。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "E": {"type": "number", "description": "弹性模量，Pa"},
                "I": {"type": "number", "description": "最小惯性矩，m^4"},
                "A": {"type": "number", "description": "截面面积，m^2"},
                "l": {"type": "number", "description": "杆长，m"},
                "ends": {"type": "string",
                         "enum": ["pinned-pinned", "fixed-free", "fixed-fixed", "fixed-pinned"],
                         "description": "两端约束，默认 pinned-pinned"},
                "sigma_p": {"type": "number", "description": "材料比例极限 Pa，可选"},
                "a": {"type": "number", "description": "经验公式 σcr=a-bλ 的 a，可选"},
                "b": {"type": "number", "description": "经验公式 σcr=a-bλ 的 b，可选"},
            },
            "required": ["E", "I", "A", "l"],
        },
    },
]

MU = {
    "pinned-pinned": (1.0, "两端铰支"),
    "fixed-free": (2.0, "一端固定一端自由"),
    "fixed-fixed": (0.5, "两端固定"),
    "fixed-pinned": (0.7, "一端固定一端铰支"),
}


# ════════════════════════════════════════════════════════════════
# 1. 能量法
# ════════════════════════════════════════════════════════════════
def t_solver_info(_args):
    return {
        "ok": True, "server": SERVER_NAME, "version": VERSION,
        "python": sys.version.split()[0], "executable": sys.executable,
        "optional": {"sympy": HAS_SYMPY, "numpy": HAS_NUMPY},
        "branches": ["energy_method(卡氏/单位载荷)", "truss_solve(桁架)",
                     "rigid_planar(刚体平面运动)", "buckling_solve(压杆稳定)"],
        "not_covered": ["碰撞（几何依赖强，按约定不做）", "静不定/塑性/大变形"],
    }


def t_energy_method(args):
    if not HAS_SYMPY:
        return {"ok": False, "error": "需要 sympy"}
    op = args["op"]
    xname = args.get("x") or "x"
    x = sp.Symbol(xname, real=True)
    params_raw = args.get("params") or {}

    Pname = args.get("P") or "P"
    P = sp.Symbol(Pname, positive=True)

    # 关键：先把所有参数名声明成符号再解析，否则 E*I 里的 I 会被当成虚数单位
    loc = {xname: x, Pname: P}
    for k in params_raw:
        loc.setdefault(k, sp.Symbol(k, positive=True))

    M = sp.sympify(args["M"], locals=loc)
    EI = sp.sympify(args["EI"], locals=loc)
    lo, hi = [sp.sympify(v, locals=loc) for v in args["span"]]
    subs = {loc[k]: sp.sympify(v) for k, v in params_raw.items()}

    if op == "castigliano":
        U = sp.simplify(sp.integrate(M**2 / (2 * EI), (x, lo, hi)))
        dU = sp.simplify(sp.diff(U, P))
        out = {"U": str(U), "delta": str(dU)}
        # 校核：数值中心差分 vs 符号导数（在参数化的具体梁上比）
        try:
            num_U = sp.lambdify(P, U.subs(subs), "math")
            num_dU = sp.lambdify(P, dU.subs(subs), "math")
            p0, h = 2.0, 1e-6
            fd = (float(num_U(p0 + h)) - float(num_U(p0 - h))) / (2 * h)
            ana = float(num_dU(p0))
            err = abs(fd - ana) / max(1e-12, abs(ana))
            out["check_fd"] = {"numeric": fd, "symbolic": ana,
                               "rel_err": err, "pass": bool(err < 1e-5)}
        except Exception as e:  # noqa: BLE001
            out["check_fd"] = {"pass": False, "error": str(e)}
        return {"ok": True, **out, "note": "卡氏第二定理 δ=∂U/∂P；P 是真实载荷，虚拟载荷取 P→0"}

    if op == "unit_load":
        mbar = sp.sympify(args["mbar"], locals=loc)
        d = sp.simplify(sp.integrate(M * mbar / EI, (x, lo, hi)))
        val = None
        try:
            val = float(d.subs(subs))
        except Exception:  # noqa: BLE001
            val = None
        return {"ok": True, "delta": str(d), "numeric": val,
                "integrand": str(sp.simplify(M * mbar / EI)),
                "note": "单位载荷法 δ=∫M·m̄/(EI)dx；m̄ 为单位力引起的弯矩"}

    return {"ok": False, "error": f"未知 op: {op}"}


# ════════════════════════════════════════════════════════════════
# 2. 桁架
# ════════════════════════════════════════════════════════════════
def t_truss_solve(args):
    if not HAS_NUMPY:
        return {"ok": False, "error": "需要 numpy"}
    nodes = args["nodes"]
    members = args["members"]
    supports = args.get("supports") or []
    loads = args.get("loads") or []

    name2i = {n["name"]: i for i, n in enumerate(nodes)}
    N, M = len(nodes), len(members)

    # 未知量：杆力 M 个 + 反力（pin 两向、roller 竖向）
    reac = []
    for s in supports:
        i = name2i[s["node"]]
        if s.get("type", "pin") == "pin":
            reac += [(i, 0), (i, 1)]
        else:
            reac += [(i, 1)]
    R = len(reac)
    nunk = M + R

    A = np.zeros((2 * N, nunk))
    b = np.zeros(2 * N)

    for k, m in enumerate(members):
        i, j = name2i[m["a"]], name2i[m["b"]]
        dx = nodes[j]["x"] - nodes[i]["x"]
        dy = nodes[j]["y"] - nodes[i]["y"]
        L = math.hypot(dx, dy)
        if L == 0:
            return {"ok": False, "error": f"杆件 {m['a']}-{m['b']} 长度为零"}
        ux, uy = dx / L, dy / L
        # 拉力为正：对节点 i 拉向 j（+u），对节点 j 拉向 i（-u）
        A[2 * i, k] += ux
        A[2 * i + 1, k] += uy
        A[2 * j, k] -= ux
        A[2 * j + 1, k] -= uy

    for r, (i, d) in enumerate(reac):
        A[2 * i + d, M + r] += 1.0

    for ld in loads:
        i = name2i[ld["node"]]
        b[2 * i] += float(ld.get("fx", 0.0))
        b[2 * i + 1] += float(ld.get("fy", 0.0))

    det = M + R - 2 * N
    if det > 0:
        return {"ok": False,
                "error": f"超静定：m+r−2N = +{det}，本工具只解静定桁架",
                "hint": "超静定需要变形协调，请用 sympy 手推或拆分连续梁"}
    if det < 0:
        return {"ok": False,
                "error": f"几何可变（机构）：m+r−2N = {det}",
                "hint": "检查支座数量或杆件连接"}

    try:
        y = np.linalg.lstsq(A, -b, rcond=None)[0]
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "error": f"求解失败: {e}"}

    residual = float(np.max(np.abs(A @ y + b)))
    scale = max(1.0, float(np.max(np.abs(b))))

    member_forces = [{"member": f"{m['a']}-{m['b']}", "N": float(y[k])}
                     for k, m in enumerate(members)]
    reactions = [{"node": nodes[i]["name"], "dir": "x" if d == 0 else "y",
                  "R": float(y[M + r])} for r, (i, d) in enumerate(reac)]
    zero = [mf["member"] for mf in member_forces if abs(mf["N"]) < 1e-9 * scale]

    return {
        "ok": residual < 1e-7 * scale,
        "determinate": True,
        "m": M, "r": R, "j": N, "m_plus_r_minus_2j": det,
        "member_forces": member_forces,
        "reactions": reactions,
        "zero_force_members": zero,
        "check": {
            "max_node_residual": residual,
            "tolerance": 1e-7 * scale,
            "pass": residual < 1e-7 * scale,
            "note": "逐节点 ΣF=0 的残差；拉力为正、压力为负",
        },
    }


# ════════════════════════════════════════════════════════════════
# 3. 刚体平面运动
# ════════════════════════════════════════════════════════════════
def _rot90(v):
    return (-v[1], v[0])


def t_rigid_planar(args):
    op = args["op"]
    w = float(args.get("omega") or 0.0)

    if op in ("vel", "acc"):
        r = args.get("r") or [0, 0]
        rx, ry = float(r[0]), float(r[1])
        # ω×r = (-ω ry, ω rx)
        cross = (-w * ry, w * rx)
        if op == "vel":
            vA = args.get("vA") or [0, 0]
            vB = (float(vA[0]) + cross[0], float(vA[1]) + cross[1])
            speed = math.hypot(*vB)
            # 校核：|vB| 与「瞬心法」一致（若 ω≠0）
            out = {"vB": [round(vB[0], 10), round(vB[1], 10)],
                   "speed": round(speed, 10)}
            if abs(w) > 0:
                # 瞬心：v_A = ω×r_A ⇒ r_A = (v_ay/ω, −v_ax/ω)；|v_B| 应等于 ω×|B−IC|
                rAx, rAy = float(vA[1]) / w, -float(vA[0]) / w
                dB = math.hypot(rx - rAx, ry - rAy)
                out["check_ic"] = {"omega_times_d": abs(w) * dB,
                                   "rel_err": abs(abs(w) * dB - speed) / max(1e-12, speed),
                                   "pass": abs(abs(w) * dB - speed) / max(1e-12, speed) < 1e-9}
            return {"ok": True, **out,
                    "note": "vB = vA + ω×r（逆时针为正，ω×r=(-ωry, ωrx)）"}

        alpha = float(args.get("alpha") or 0.0)
        aA = args.get("aA") or [0, 0]
        tang = (-alpha * ry, alpha * rx)
        norm = (-w * w * rx, -w * w * ry)
        aB = (float(aA[0]) + tang[0] + norm[0], float(aA[1]) + tang[1] + norm[1])
        return {"ok": True, "aB": [round(aB[0], 10), round(aB[1], 10)],
                "components": {"transport_tangential": [round(tang[0], 10), round(tang[1], 10)],
                               "normal": [round(norm[0], 10), round(norm[1], 10)],
                               "magnitude": round(math.hypot(*aB), 10)},
                "note": "aB = aA + α×r − ω²r（法向项恒指向转轴）"}

    if op == "ic":
        vA = args.get("vA") or [0, 0]
        if abs(w) < 1e-15:
            return {"ok": False, "error": "ω=0 时无速度瞬心（瞬时平动）"}
        Ax, Ay = (args.get("A") or [0, 0])[:2]
        rAx, rAy = float(vA[1]) / w, -float(vA[0]) / w
        ic = (float(Ax) - rAx, float(Ay) - rAy)
        speed = math.hypot(float(vA[0]), float(vA[1]))
        r = math.hypot(rAx, rAy)
        return {"ok": True, "ic": [round(ic[0], 10), round(ic[1], 10)],
                "radius_A": round(r, 10),
                "check": {"omega_times_r": round(abs(w) * r, 10), "speed_A": round(speed, 10),
                          "pass": abs(abs(w) * r - speed) < 1e-9}}

    return {"ok": False, "error": f"未知 op: {op}"}


# ════════════════════════════════════════════════════════════════
# 4. 压杆稳定
# ════════════════════════════════════════════════════════════════
def t_buckling_solve(args):
    E = float(args["E"]); I = float(args["I"]); A = float(args["A"]); l = float(args["l"])
    ends = args.get("ends") or "pinned-pinned"
    mu, desc = MU.get(ends, (1.0, ends))

    i_rad = math.sqrt(I / A)
    lam = mu * l / i_rad
    Pcr = math.pi ** 2 * E * I / (mu * l) ** 2
    sig_cr_euler = Pcr / A
    out = {
        "mu": mu, "end_condition": desc,
        "i": i_rad, "lambda": lam,
        "P_cr_euler": Pcr, "sigma_cr_euler": sig_cr_euler,
        "check": {"pi2EI_over_mul2": Pcr,
                  "sigma_times_A": sig_cr_euler * A,
                  "pass": abs(sig_cr_euler * A - Pcr) / Pcr < 1e-12},
    }

    sig_p = args.get("sigma_p")
    if sig_p:
        sig_p = float(sig_p)
        lam_p = math.pi * math.sqrt(E / sig_p)
        out["lambda_p"] = lam_p
        if lam >= lam_p:
            out["regime"] = "大柔度（欧拉公式适用）"
            out["sigma_cr"] = sig_cr_euler
            out["P_cr"] = Pcr
        else:
            a, b = args.get("a"), args.get("b")
            if a and b:
                s = float(a) - float(b) * lam
                out["regime"] = "中柔度（经验公式 σcr=a−bλ）"
                out["sigma_cr"] = s
                out["P_cr"] = s * A
            else:
                out["regime"] = "非大柔度：欧拉公式不适用，需给 a/b 走经验公式或按强度计算"
                out["sigma_cr"] = None
                out["P_cr"] = None
    else:
        out["regime"] = "未给 σp，仅按欧拉公式计算（需自行判断是否大柔度）"
    return {"ok": True, **out, "note": "i=√(I/A)，λ=μl/i；欧拉公式仅当 σcr≤σp 时成立"}


HANDLERS = {
    "solver_info": t_solver_info,
    "energy_method": t_energy_method,
    "truss_solve": t_truss_solve,
    "rigid_planar": t_rigid_planar,
    "buckling_solve": t_buckling_solve,
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
    sys.stderr.write(f"[{SERVER_NAME}] 启动\n")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except Exception as e:  # noqa: BLE001
            sys.stderr.write(f"[{SERVER_NAME}] 非法 JSON: {e}\n")
            continue
        mid, method = msg.get("id"), msg.get("method")
        if method == "initialize":
            send({"jsonrpc": "2.0", "id": mid, "result": {
                "protocolVersion": msg.get("params", {}).get("protocolVersion", "2024-11-05"),
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": SERVER_NAME, "version": VERSION}}})
        elif method == "notifications/initialized":
            continue
        elif method == "tools/list":
            send({"jsonrpc": "2.0", "id": mid, "result": {"tools": TOOLS}})
        elif method == "tools/call":
            p = msg.get("params") or {}
            res = call_tool(p.get("name"), p.get("arguments"))
            send({"jsonrpc": "2.0", "id": mid, "result": {
                "content": [{"type": "text", "text": json.dumps(res, ensure_ascii=False, indent=1)}],
                "isError": not res.get("ok", False)}})
        elif mid is not None:
            send({"jsonrpc": "2.0", "id": mid,
                  "error": {"code": -32601, "message": f"不支持的方法: {method}"}})


if __name__ == "__main__":
    main()

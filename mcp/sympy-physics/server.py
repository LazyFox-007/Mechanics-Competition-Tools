#!/usr/bin/env python3
"""
sympy-physics MCP —— 把 sympy.physics 的四个模块包成任务级工具

覆盖：
  sympy.physics.mechanics            动力学方程（拉格朗日 / Kane）
  sympy.physics.vector               运动学（参考系、点的速度/加速度）
  sympy.physics.continuum_mechanics  梁 / 桁架（反力、内力、转角、挠度）
  sympy.physics.units                量纲检查与单位换算

设计原则：
  - 只依赖 sympy + 标准库（sympy 已装在带 mcp 的解释器里即可）
  - stdout 是 MCP 的 JSON-RPC 通道，任何库的杂散打印都要挡在 stderr
  - 每个工具返回 JSON，出错返回 {"ok": false, "error": ...} 而不是崩掉

传输：stdio，一行一个 JSON-RPC 2.0 消息。
"""

import json
import os
import sys
import traceback

# ── stdout 保护：真 stdout 留给协议，fd 1 指向 stderr ──────────────
_real_stdout_fd = os.dup(1)
os.dup2(2, 1)
_OUT = os.fdopen(_real_stdout_fd, "w", encoding="utf-8", buffering=1)

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8")

import sympy  # noqa: E402
from sympy import Matrix, cos, exp, latex, pi, simplify, sin, sqrt, symbols, sympify  # noqa: E402
from sympy.physics.mechanics import LagrangesMethod, dynamicsymbols  # noqa: E402

SERVER_NAME = "sympy-physics"
VERSION = "0.1.0"

TOOLS = [
    {
        "name": "mech_info",
        "description": "自检：sympy 版本 + 四个 physics 模块是否可用 + 各自符号数。",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "lagrange_eom",
        "description": (
            "用拉格朗日方法建立动力学方程。给拉格朗日量 L（用 q1..qn 与 qd1..qdn 表示广义坐标与速度）"
            "和广义坐标列表，返回运动方程（含 q̈ 项）。适用于多自由度系统、含转动刚体的动力学题。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "L": {"type": "string", "description": "拉格朗日量表达式，如 'm*l**2*qd1**2/2 + m*g*l*cos(q1)'"},
                "coords": {"type": "array", "items": {"type": "string"},
                           "description": "广义坐标名列表，如 ['q1'] 或 ['x','theta']"},
                "params": {"type": "object", "description": "常数取值的字典，可选，如 {'m':'1','l':'1','g':'9.8'}"},
                "latex": {"type": "boolean", "description": "是否同时返回 LaTeX，默认 false"},
            },
            "required": ["L", "coords"],
        },
    },
    {
        "name": "kinematics_derive",
        "description": (
            "给位置向量表达式（关于 t 的表达式逐分量写出），自动求速度与加速度。"
            "用于运动学：直角坐标下点的运动、轨迹分析。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "pos": {"type": "array", "items": {"type": "string"},
                        "description": "位置分量，如 ['R*cos(omega*t)','R*sin(omega*t)','0']"},
                "params": {"type": "object", "description": "常数取值，可选"},
                "eval_at": {"type": "object", "description": "代入求值，如 {'t':'0.5'}，可选"},
            },
            "required": ["pos"],
        },
    },
    {
        "name": "relative_motion",
        "description": (
            "点的合成运动：由牵连速度/加速度与相对速度/加速度求绝对量，自动计算科氏加速度 a_C = 2ω×v_r。"
            "动系平动时把 omega 设为 [0,0,0]。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "v_e": {"type": "array", "items": {"type": "string"}, "description": "牵连速度 [vx,vy,vz]"},
                "v_r": {"type": "array", "items": {"type": "string"}, "description": "相对速度 [vx,vy,vz]"},
                "a_e": {"type": "array", "items": {"type": "string"}, "description": "牵连加速度，可选"},
                "a_r": {"type": "array", "items": {"type": "string"}, "description": "相对加速度，可选"},
                "omega": {"type": "array", "items": {"type": "string"},
                          "description": "动系角速度 [wx,wy,wz]，可选（默认零）"},
            },
            "required": ["v_e", "v_r"],
        },
    },
    {
        "name": "beam_solve",
        "description": (
            "欧拉-伯努利梁求解：给梁长、EI、支座与载荷，返回支反力、剪力、弯矩、转角、挠度表达式，"
            "并可在指定点求值。支座类型 pin/roller/fixed。载荷类型 point（集中力）/dist（均布）/moment（集中力偶）。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "length": {"type": "number", "description": "梁长（米）"},
                "EI": {"type": "string", "description": "抗弯刚度表达式，如 'E*I' 或数值字符串"},
                "supports": {"type": "array", "description": "支座列表",
                             "items": {"type": "object",
                                       "properties": {"at": {"type": "number"},
                                                      "type": {"type": "string", "enum": ["pin", "roller", "fixed"]}},
                                       "required": ["at", "type"]}},
                "loads": {"type": "array", "description": "载荷列表",
                          "items": {"type": "object",
                                    "properties": {
                                        "type": {"type": "string", "enum": ["point", "dist", "moment"]},
                                        "at": {"type": "number", "description": "作用位置；dist 时为起点"},
                                        "value": {"type": "number", "description": "集中力/均布集度/力偶（向下为负）"},
                                        "span": {"type": "number", "description": "dist 的分布长度，默认到梁端"}},
                                    "required": ["type", "at", "value"]}},
                "eval_points": {"type": "array", "items": {"type": "number"},
                                "description": "在这些 x 处求数值，可选"},
            },
            "required": ["length", "EI", "supports", "loads"],
        },
    },
    {
        "name": "unit_check",
        "description": (
            "量纲检查：给一个用物理量符号组成的表达式，返回其量纲与 SI 单位，用于校验公式量纲一致性。"
            "如 expr='F*L', units={'F':'newton','L':'meter'} → 力矩。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "expr": {"type": "string", "description": "表达式，如 'F*L/(E*I)'"},
                "units": {"type": "object", "description": "符号到单位的映射，如 {'F':'newton','L':'meter','E':'pascal','I':'meter**4'}"},
            },
            "required": ["expr", "units"],
        },
    },
    {
        "name": "unit_convert",
        "description": "单位换算：把带数值的表达式换算到目标单位。如 1 kN·m → N·mm。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "value": {"type": "string", "description": "带单位的表达式，如 '5*kilometer'"},
                "to": {"type": "array", "items": {"type": "string"},
                       "description": "目标单位列表，如 ['meter'] 或 ['newton','meter']"},
            },
            "required": ["value", "to"],
        },
    },
]


def _ns(params):
    """把 params 注入为符号，转成 sympy 对象。"""
    ns = {}
    if params:
        for k, v in params.items():
            ns[k] = sympify(v, locals=ns) if isinstance(v, str) else sympify(v)
    return ns


def _num_or_expr(e, evaldict=None):
    try:
        if evaldict:
            v = e.subs(evaldict)
            f = complex(v.evalf())
            if abs(f.imag) < 1e-12:
                return round(f.real, 10)
    except Exception:
        pass
    return str(e)


# ────────────────────────── 工具实现 ──────────────────────────

def t_mech_info(args):
    mods = {}
    for mod in ("sympy.physics.mechanics", "sympy.physics.vector",
                "sympy.physics.continuum_mechanics", "sympy.physics.units"):
        try:
            m = __import__(mod, fromlist=["*"])
            mods[mod] = len([n for n in dir(m) if not n.startswith("_")])
        except Exception as e:  # noqa: BLE001
            mods[mod] = f"不可用: {e}"
    return {"ok": True, "sympy": sympy.__version__, "modules": mods}


def t_lagrange_eom(args):
    coords = args["coords"]
    ns = _ns(args.get("params"))
    # 必须用 dynamicsymbols 内部那个 t，否则 symbols('t', real=True) 是两个不同对象，
    # q.diff(t) 会返回 0，动能项整块丢失（踩过）。
    t = dynamicsymbols._t
    qs = dynamicsymbols(" ".join(coords))   # 直接用实际坐标名，输出更自然
    if len(coords) == 1:
        qs = [qs]
    qds = [q.diff(t) for q in qs]

    # 把 q1..qn / qd1..qdn 映射到实际坐标名
    sub = {}
    for i, _name in enumerate(coords):
        sub[symbols(f"q{i+1}")] = qs[i]
        sub[symbols(f"qd{i+1}")] = qds[i]

    Lex = sympify(args["L"], locals=ns).subs(sub)
    LM = LagrangesMethod(Lex, qs)
    eom = LM.form_lagranges_equations()
    out = {
        "ok": True,
        "coords": coords,
        "equations": [str(simplify(e)) for e in eom],
        "count": len(eom),
    }
    if args.get("latex"):
        out["latex"] = [latex(simplify(e)) for e in eom]
    return out


def t_kinematics_derive(args):
    ns = _ns(args.get("params"))
    t = symbols("t", real=True)
    ns["t"] = t
    pos = [sympify(p, locals=ns) for p in args["pos"]]
    vel = [simplify(p.diff(t)) for p in pos]
    acc = [simplify(v.diff(t)) for v in vel]

    ev = None
    if args.get("eval_at"):
        ev = {sympify(k): sympify(v) for k, v in args["eval_at"].items()}

    return {
        "ok": True,
        "position": [str(p) for p in pos],
        "velocity": [str(v) for v in vel],
        "acceleration": [str(a) for a in acc],
        "evaluated": None if not ev else {
            "at": args["eval_at"],
            "position": [_num_or_expr(p, ev) for p in pos],
            "velocity": [_num_or_expr(v, ev) for v in vel],
            "acceleration": [_num_or_expr(a, ev) for a in acc],
        },
    }


def t_relative_motion(args):
    ns = _ns(args.get("params"))
    zero = ["0", "0", "0"]
    ve = Matrix([sympify(x, locals=ns) for x in args["v_e"]])
    vr = Matrix([sympify(x, locals=ns) for x in args["v_r"]])
    w = Matrix([sympify(x, locals=ns) for x in (args.get("omega") or zero)])
    ae = Matrix([sympify(x, locals=ns) for x in (args.get("a_e") or zero)])
    ar = Matrix([sympify(x, locals=ns) for x in (args.get("a_r") or zero)])

    vabs = simplify(ve + vr)
    # a_C = 2 ω × v_r
    a_c = simplify(2 * w.cross(vr))
    aabs = simplify(ae + ar + a_c)

    return {
        "ok": True,
        "v_absolute": [str(simplify(x)) for x in vabs],
        "v_absolute_magnitude": str(simplify(sqrt(vabs.dot(vabs)))),
        "a_coriolis": [str(x) for x in a_c],
        "a_absolute": [str(x) for x in aabs],
        "a_absolute_magnitude": str(simplify(sqrt(aabs.dot(aabs)))),
        "note": "动系平动时 ω=0，科氏加速度为零" if w == Matrix(zero) else "",
    }


def t_beam_solve(args):
    from sympy.physics.continuum_mechanics.beam import Beam  # noqa: PLC0415

    ns = {}
    E, I = symbols("E I", positive=True)
    EI_expr = sympify(args["EI"], locals=ns)
    # 支持 'E*I' 或 '200000*8000000' 形式
    eq = symbols("EI", positive=True)
    L = args["length"]
    b = Beam(L, E, I)

    r_syms = []
    for s in args["supports"]:
        r = b.apply_support(s["at"], s["type"])
        if isinstance(r, (list, tuple)):
            r_syms.extend(r)
        else:
            r_syms.append(r)

    for ld in args["loads"]:
        v = ld["value"]
        if ld["type"] == "point":
            b.apply_load(v, ld["at"], -1)
        elif ld["type"] == "dist":
            span = ld.get("span", L - ld["at"])
            b.apply_load(v, ld["at"], 0, end=ld["at"] + span)
        elif ld["type"] == "moment":
            b.apply_load(v, ld["at"], -2)

    if r_syms:
        b.solve_for_reaction_loads(*r_syms)

    x = symbols("x")
    shear = simplify(b.shear_force())
    moment = simplify(b.bending_moment())
    slope = simplify(b.slope())
    defl = simplify(b.deflection())

    out = {
        "ok": True,
        "length": L,
        "reactions": {str(k): str(v) for k, v in b.reaction_loads.items()},
        "shear_force": str(shear),
        "bending_moment": str(moment),
        "slope": str(slope),
        "deflection": str(defl),
        "EI": str(EI_expr),
    }

    if args.get("eval_points"):
        pts = args["eval_points"]
        out["evaluated"] = []
        for p in pts:
            rec = {"x": p}
            for label, expr in (("shear", shear), ("moment", moment),
                                ("slope", slope), ("deflection", defl)):
                try:
                    rec[label] = str(simplify(expr.subs(x, p)))
                except Exception:  # noqa: BLE001
                    rec[label] = None
            out["evaluated"].append(rec)

    return out


def _units_ns():
    """单位命名空间：让 sympify('newton') 解析成真正的物理量，而不是普通符号。"""
    import sympy.physics.units as U  # noqa: PLC0415
    return {k: v for k, v in vars(U).items() if not k.startswith("_")}


def t_unit_check(args):
    import sympy.physics.units as U  # noqa: F401, PLC0415
    from sympy.physics.units.systems.si import SI  # noqa: PLC0415

    ns = _units_ns()
    for k, v in (args.get("units") or {}).items():
        ns[k] = sympify(v, locals=ns)   # 必须用单位命名空间解析，否则退化成符号
    expr = sympify(args["expr"], locals=ns)
    try:
        dim = str(SI.get_dimensional_expr(expr))
    except Exception as e:  # noqa: BLE001
        dim = f"无法解析: {e}"
    return {
        "ok": True,
        "expr": str(expr),
        "dimension": dim,
        "note": "量纲用 SI 基本量表示；若返回 1 说明表达式里没有可识别的物理量",
    }


def t_unit_convert(args):
    from sympy.physics.units import convert_to  # noqa: PLC0415
    from sympy.physics.units.util import quantity_simplify  # noqa: PLC0415

    ns = _units_ns()
    val = sympify(args["value"], locals=ns)
    target = [sympify(u, locals=ns) for u in args["to"]]
    conv = convert_to(val, target)
    simp = quantity_simplify(conv)
    try:
        coeff = simplify(simp.as_coeff_Mul()[0])
        num = str(coeff) if coeff.is_number else None
    except Exception:  # noqa: BLE001
        num = None
    return {
        "ok": True,
        "input": str(val),
        "converted": str(conv),
        "simplified": str(simp),
        "numeric": num,
    }


HANDLERS = {
    "mech_info": t_mech_info,
    "lagrange_eom": t_lagrange_eom,
    "kinematics_derive": t_kinematics_derive,
    "relative_motion": t_relative_motion,
    "beam_solve": t_beam_solve,
    "unit_check": t_unit_check,
    "unit_convert": t_unit_convert,
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
    sys.stderr.write(f"[{SERVER_NAME}] 启动，sympy {sympy.__version__}\n")
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

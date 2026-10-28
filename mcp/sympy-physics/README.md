# sympy-physics MCP

把 `sympy.physics` 的四个模块包成任务级工具。**纯本地、免联网**，只依赖 sympy。

## 为什么做这个

`sympy` 1.14 里已经装了完整的力学库，但现有 `sympy-mcp` 只暴露了通用代数/微积分/矩阵，
这四块一个都没有露出来：

| 模块 | 符号数 | 能解决什么 |
|---|---|---|
| `sympy.physics.mechanics` | 90 | 动力学方程：`KanesMethod`、`LagrangesMethod`、`RigidBody`、`inertia` |
| `sympy.physics.vector` | 34 | 运动学：`ReferenceFrame`、`Point`、旋转坐标系 |
| `sympy.physics.continuum_mechanics` | 8 | 材料力学：`Beam`(50 方法)、`Arch`、`Cable`、`Truss` |
| `sympy.physics.units` | 369 | 量纲检查、单位换算 |

## 工具（7 个）

| 工具 | 作用 |
|---|---|
| `mech_info` | 自检：sympy 版本 + 四模块可用性与符号数 |
| `lagrange_eom` | **拉格朗日方程**：给 L（用 `q1..qn`/`qd1..qdn`）与广义坐标，返回运动方程 |
| `kinematics_derive` | **运动学**：给位置表达式分量，自动求速度、加速度 |
| `relative_motion` | **合成运动**：v_abs = v_e + v_r，a_abs = a_e + a_r + **2ω×v_r**（自动算科氏） |
| `beam_solve` | **梁**：支反力、剪力、弯矩、转角、挠度；支持 pin/roller/fixed 与 point/dist/moment 载荷 |
| `unit_check` | **量纲检查**：表达式 → SI 基本量组合 |
| `unit_convert` | **单位换算**：如 `5*kilometer` → `5000*meter` |

## 实测（都是教科书算例，可复现）

**拉格朗日 · 单摆**
```json
{"L": "m*l**2*qd1**2/2 + m*g*l*cos(q1)", "coords": ["theta"],
 "params": {"m":"1","l":"1","g":"9.8"}}
```
→ `9.8*sin(theta(t)) + Derivative(theta(t), (t, 2))` ✅

**运动学 · 圆周运动** `pos = [R*cos(ωt), R*sin(ωt), 0]`，R=2, ω=3
→ v = `[-6sin3t, 6cos3t, 0]`，a = `[-18cos3t, -18sin3t, 0]`（a = ω²R = 18 ✅）

**合成运动** `v_e=[1,0,0]`, `v_r=[0,2,0]`, `ω=[0,0,3]`
→ v_abs = `[1,2,0]`，**a_C = `[-12,0,0]`**（手算 2ω×v_r = -12 ✅）

**简支梁** 跨 10 m，跨中 −5 kN
→ 反力 `5/2` 与 `5/2`，跨中挠度 `-625/(6EI)` = **PL³/48EI = 104.17/EI** ✅

**量纲** `F*L`，F=newton, L=meter → `force*length` ✅

**换算** `5*kilometer` → `5000*meter`（numeric 5000）✅

## 踩过的三个坑

1. **`dynamicsymbols` 的 t 不能用 `symbols('t', real=True)` 代替**
   两者是不同对象，`q.diff(t)` 直接返回 `0`，动能项整块丢失，方程只剩势能项。
   必须用 `dynamicsymbols._t`。

2. **`sympify('newton')` 不会解析成单位**
   需要在 `locals` 里注入 `sympy.physics.units` 的命名空间，否则退化成普通符号，量纲恒为 1。

3. **`Beam.solve_for_reaction_loads` 要传 `apply_support` 的返回值**
   自己 `symbols('R_0')` 造名字会抛 `IndexError: tuple index out of range`。

另外 `SI` 与 `quantity_simplify` 不在 `sympy.physics.units` 顶层：
```python
from sympy.physics.units.systems.si import SI
from sympy.physics.units.util import quantity_simplify
```

## 启动

```bash
<装有 sympy 的 python> mcp/sympy-physics/server.py
```

stdout 是 MCP 的 JSON-RPC 通道；服务启动时用 `os.dup2` 把 fd 1 指向 stderr，
所以 sympy 的任何杂散打印都不会污染协议。

## 边界

- 只做**符号/精确解**，不做数值积分（ODE 求数值解请用 `sympy.dsolve` 出通解后自行代入）
- `beam_solve` 是欧拉-伯努利梁，不含剪切变形（Timoshenko）
- `continuum_mechanics` 的 `Arch`/`Cable`/`Truss` 本版未封装，需要时再补

---
name: mechanics-map
description: "开放教材《Mechanics Map》(Moore et al., CC BY-SA 4.0) 的逐章提炼，覆盖静力学、运动学、动力学、单自由度振动与惯性矩积分。当理论力学题需要标准解法、公式出处、坐标系选择或概念辨析时查阅；也用于核对「这一步该用什么定理」。"
---

# Mechanics Map（理论力学系统参考）

开放教材逐章提炼，**英文原文 + 公式 + 例题**，按章节切成独立模块，按需只读需要的那一章。

- 原书：[Mechanics Map (Moore et al.)](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Mechanics_Map_%28Moore_et_al.%29)
- 作者：Jacob Moore and Contributors
- 许可：**CC BY-SA 4.0** —— 引用/派生须署名并沿用同协议，见 `LICENSE-NOTICE.md`

---

## 什么时候用这个 skill

| 情形 | 用它做什么 |
|---|---|
| 不确定该用哪个定理（牛顿 / 动能 / 动量矩） | 查第 8–14 章的「选型」段落 |
| 运动学不会建立速度/加速度关系 | 第 7 章（质点）、第 11 章（刚体，含**旋转坐标系**） |
| 需要标准解题流程和例题 | 各章 `## Example` 段 |
| 摩擦、桁架、重心、惯性矩 | 第 6 章、第 5 章、第 17 章 |
| 单自由度振动（固有频率、阻尼） | 第 15 章 |

**不适合**：具体数值计算（交给 `mcp__sympy__*`）、静定内力图（交给插件 `mech_analyze` / `mech_diagram`）。

---

## 章节索引

| 模块 | 内容 | 对应考点 |
|---|---|---|
| `01-newtonian-basics` | 牛顿力学基础、单位、矢量 | 概念辨析、量纲 |
| `02-static-concurrent-forces` | 汇交力系平衡 | 静力学基础 |
| `03-static-rigid-bodies` | 刚体平衡、支座反力 | 受力分析（高频） |
| `04-statically-equivalent-systems` | 等效力系、力系简化 | 主矢主矩、力螺旋 |
| `05-engineering-structures` | 桁架、框架、绳索 | 桁架零杆判断 |
| `06-friction` | 摩擦、摩擦角、自锁 | 摩擦平衡（易错） |
| `07-particle-kinematics` | 质点运动学、三种坐标系 | **运动学**（直角/法向/极坐标） |
| `08-newton-second-law-particles` | 质点牛顿第二定律 | 动力学基本方程 |
| `09-work-energy-particles` | 质点动能定理、势能 | 能量法 |
| `10-impulse-momentum-particles` | 质点动量定理、碰撞 | 冲击、动量守恒 |
| `11-rigid-body-kinematics` | **刚体运动学**：定轴转动、传动、绝对运动、相对运动、**旋转坐标系** | **运动学最难的点在这** |
| `12-newton-second-law-rigid-bodies` | 刚体牛顿-欧拉方程 | 平面运动动力学 |
| `13-work-energy-rigid-bodies` | 刚体动能定理 | 含转动惯量的能量法 |
| `14-impulse-momentum-rigid-bodies` | 刚体动量矩定理 | 碰撞、突然约束 |
| `15-vibrations-one-dof` | 单自由度振动 | 固有频率、阻尼比 |
| `16-vector-matrix-math` | 矢量与矩阵运算 | 空间力系、方向余弦 |
| `17-moment-integrals` | 惯性矩积分、平行轴定理 | 组合截面 |

---

## 用法

1. **先定位**：按上表找到章节，只读那一章，别通读
2. **查三样东西**：概念定义 → 公式 → `## Example` 的标准流程
3. **回到工具**：把公式抄进 `mcp__sympy__*` 做符号推导，避免手算错

> Token 提示：单章 10–50 KB，只读需要的一章。整本读完 ~390 KB，赛时没必要。

---

## 与其它工具的分工

| 环节 | 工具 |
|---|---|
| 概念、定理选择、标准流程、例题 | **本 skill** |
| 符号推导、解方程、积分、特征值 | `mcp__sympy__*` |
| 静定反力、内力图、截面几何、莫尔圆 | 插件 `mech_analyze` / `mech_diagram` |
| 梁的挠度/转角（欧拉-伯努利） | `sympy.physics.continuum_mechanics.Beam` |
| 动力学方程自动建立（Kane/拉格朗日） | `sympy.physics.mechanics` |
| 中文术语对照、符号约定、题型决策表 | **`mechanics-zh` skill**（自研） |

---

## 说明

- 本 skill 正文为英文原文（CC BY-SA 4.0），引用须署名并沿用同协议，见 `LICENSE-NOTICE.md`
- 中文部分单独放在 `mechanics-zh` skill 里 —— 那是自研整理，不含任何第三方教材原文
- 网上能搜到的中文《理论力学》讲义仓库绝大多数**没有声明许可**（默认版权保留），不能打包分发，因此没有收录

# mechanics-competition-tools

「国产AI大模型辅助理论力学与材料力学解题」赛题的**工具与配置仓库**。

目标很简单：换一台机器，`git clone` + 跑一个脚本，把力学/数学求解能力装回来。

> 命题编号 AI-MECH-2026-001 · 江苏省力学学会
> 本仓库**只有工具，不含任何赛题、答案或测试标签**（赛规明令禁止）。

---

## 快速开始（新机器）

```powershell
git clone https://gitee.com/haveink/mechanics-competition-tools.git
cd mechanics-competition-tools
pwsh -File setup.ps1
```

脚本会做四件事：复制技能到 `~/.dsh/skills` → 把两个 MCP 写进 `~/.dsh/cordis.patch.yml`
→ 检查 Python 依赖 → 打印还差什么。**改配置前会备份**。

装完重启 DSH。

---

## 仓库里有什么

| 目录 | 内容 | 干什么用 |
|---|---|---|
| `skills/undergrad-physics-skill/` | 本科物理与力学推导技能 | 六步流程 + **8 种验算方法**（F 量纲 / B 回代 / L 极限 / C 守恒 / D 定义域 / E 抽样 / I 独立方法 / J 一致性），FAIL 就回溯 |
| `skills/undergrad-physics-skill/modules/material-mechanics.md` | 材料力学模块 | 补静不定、压杆稳定、能量法、动载荷——原版没有，这是自加的 |
| `skills/math-skill/` | 数学推理技能 | 通用数学推导与验证 |
| **`skills/mechanics-map/`** | **《Mechanics Map》全教材 17 章**（CC BY-SA 4.0） | 静力学、**运动学**、**动力学**、单自由度振动、惯性矩——查标准解法与例题 |
| **`skills/mechanics-zh/`** | **中文速查**（自研） | 术语对照、符号约定、题型决策表、三类高频题骨架、量纲清单、答案模板 |
| `plugins/dsh-mech-workbench/` | DSH 插件（9 工具） | 读题图、静定反力与 N/Q/M/T 图、截面几何、莫尔圆、出图自检、题目卡片 |
| `mcp/sympy/` | sympy-mcp（Apache-2.0） | 32 个符号数学工具：解方程/方程组、ODE/PDE、积分、微分、矩阵特征值、LaTeX 输出 |
| **`mcp/sympy-physics/`** | **自建（7 工具）** | **`sympy.physics` 四模块封装**：拉格朗日方程、运动学求导、合成运动（含科氏）、梁（反力/内力/转角/挠度）、量纲检查、单位换算 |
| `mcp/lean4/` | lean-mcp 单文件 | Lean 4 形式化：类型检查、运行、query |
| `docs/` | 赛规摘要、工具映射 | 赛前对表用 |

**总大小约 5.0 MB** —— 远低于赛规 200 MB 的知识库上限。

> `mechanics-map` 是英文原书（CC BY-SA 4.0，署名 Jacob Moore and Contributors）；
> 中文部分在 `mechanics-zh`，为自研整理。两套都**不含任何网络题解或赛题答案**。

---

## 配套的外部工具（不在本仓库）

| 工具 | 用途 | 在哪 |
|---|---|---|
| `document` MCP | 读 PDF/Word/Excel（读赛题 PDF 必需） | [ai-agent-tools](https://gitee.com/haveink/ai-agent-tools) `mcp/document` |
| Python 3.10+ | 跑 `sympy` / `lean4` / 插件脚本 | anaconda 或 Python311 |
| `sympy` + `mcp` 库 | sympy-mcp 的运行时 | `pip install sympy mcp` |

---

## 赛前必做（合规检查）

赛规里有几条**直接决定成绩有效性**：

1. **关掉所有联网 MCP** —— `browser`、`context7` 在赛时属于「联网检索」，违规。
   在 `~/.dsh/cordis.patch.yml` 给它们加 `disabled: true`。
2. **确认知识库 ≤ 200 MB** —— 以解压后含索引、配置、元数据的总量计。
3. **不含赛题/答案** —— 仓库和知识库里都不能有当次赛题、答案、测试标签。
4. **留痕** —— 保存模型信息、部署配置、prompt 模板、检索注入片段、推理日志。
5. **Token 影响排名** —— 总分相同则 Token 少者胜。**别开一堆用不上的 MCP**，
   工具描述本身要占 context。

详见 [docs/规则摘要.md](docs/规则摘要.md)。

---

## 工具怎么选（按评分权重）

总分 = 答案正确性 **70%** + 过程与公式规范 **20%** + 表达/量纲/校核 **10%**。

| 环节 | 用什么 | 为什么 |
|---|---|---|
| 读题 | `document` 的 `pdf_text` / `pdf_render`，或直接看图 | 读错一个数整题报废 |
| 符号推导 | `mcp__sympy__*` | 32 个工具，能出 LaTeX，方便写进答案 |
| 内力图 / 静定反力 | 插件 `mech_analyze` / `mech_diagram` | 自动出图 + 8 项校核，直接当「校核」得分点 |
| 验算 | `undergrad-physics-skill` 的 F/B/L 组合 | 过程分 20% 靠这个 |
| 量纲检查 | 技能里的 F 方法 + sympy 单位 | 表达分 10% 靠这个 |

详细映射见 [docs/工具映射.md](docs/工具映射.md)。

---

## 已知边界（别指望工具兜底）

- 插件的 `mech_analyze` **只解静定**：静不定、压杆稳定、塑性、大变形明确不做
- 这四块恰好是周培源提高题的常客 → **必须靠 skill 的流程 + sympy 手推**
- `sympy` 是有状态的：`intro` → `introduce_expression` → `solve` → `reset_state`
- 插件安装需要**创造模式**（`plugin_manager`），脚本装不了，见下方

---

## 插件怎么装（脚本管不了）

```
设置 → Agent 预设 → 创造入口（cordis 预设）→ 新开会话
plugin_manager → action: install_bundle
              → target: <本仓库>/plugins/dsh-mech-workbench
装完重启 DSH
```

`plugins/dsh-mech-workbench/requirements.txt` 里写了符号计算依赖的三种补法。

---

## 许可

- 本仓库自建部分：随便用
- `mcp/sympy`：Apache-2.0（保留原 LICENSE）
- `mcp/lean4`：自建单文件
- `skills/math-skill`、`skills/undergrad-physics-skill`：MIT
- `skills/mechanics-map`：**CC BY-SA 4.0**（署名 Jacob Moore and Contributors，派生须同协议）
- `skills/mechanics-zh`：自研，随意使用
- `plugins/dsh-mech-workbench`：MIT（保留原 LICENSE）

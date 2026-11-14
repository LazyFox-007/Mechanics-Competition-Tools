# mechanics-competition-tools

> **辅助 AI 做力学。**
>
> 一套让大语言模型真正会解理论力学 / 材料力学题的工具链、知识库与强制流程。

## 它解决什么问题

大模型早就会背公式、会推式子。实测两届竞赛（第十四届 93/120、第十五届提高题 39/60）暴露的真相是：

> **失分几乎全部发生在「方程之前」——建模选错、图读错、条件继承错。
> 纯数学推导部分，六次核对全对。**

所以这个仓库不提供题库、不提供答案、不是又一个 prompt 模板。它给 AI 配三样东西：

| 能力 | 靠什么 | 目录 |
|---|---|---|
| **算得动** | 7 个 MCP 服务 + 插件 + PyNite 三维刚架 | `mcp/` `plugins/` `vendor/` |
| **查得到** | 21 MB 离线知识库：MIT OCW 材料力学 60 篇讲义、NASA 屈曲手册、教材 17 章、30+ 张判据卡 | `kb/` `skills/` |
| **错得少** | 九条硬规则 + 建模决策卡 + 8 类验算方法，全流程强制 | `skills/mechanics-zh/` `mcp/mech-model/` |

> 面向「国产AI大模型辅助理论力学与材料力学解题」赛题（AI-MECH-2026-001 · 江苏省力学学会）构建。
> **通用**：任何让 AI 做力学题的场景都能用。
>
> 仓库**只有工具与公开资料，不含任何赛题、答案或测试标签**。

**两个入口**：

- AI 现场运行 → 先读 [AGENTS.md](AGENTS.md)（强制要求与红线）
- 人看的说明 → 本文件
- 打不出希腊字母 → 查 [符号表.md](符号表.md)

---

## 快速开始（新机器）

```powershell
git clone https://gitee.com/haveink/mechanics-competition-tools.git
cd mechanics-competition-tools
.\setup.ps1 -Competition
```

GitHub 镜像：`https://github.com/LazyFox-007/Mechanics-Competition-Tools.git`

装完重启 DSH。

---

## 配置脚本

一个 `setup.ps1` 管全部环境，**改配置前自动备份**。

| 时机 | 命令 | 做什么 |
|---|---|---|
| 赛前 | `.\setup.ps1 -Competition` | 复制技能 + 注册 MCP + 关掉联网/无用 MCP（合规、省 token） |
| 装依赖 | `.\setup.ps1 -InstallDeps` | pip 装 sympy/mcp/pymupdf 等，再**离线**装 PyNite 并回锁 numpy |
| 重启后 | `.\setup.ps1 -Verify` | 真的把每个 MCP 拉起来走 `initialize`+`tools/list`，报工具数与耗时 |
| 出问题 | `.\setup.ps1 -Restore` | 回到最近一次备份（`-BackupPath` 可指定） |
| 只看不改 | `.\setup.ps1 -DryRun` | 打印将要做什么 |

其他参数：`-DshHome`（指定配置根目录）、`-PythonExe`（指定解释器）、
`-NoEverything`（连本地检索也关，最省 token）。

**内置的三道检查**：

1. **D 盘合规** —— 逐条检查 仓库 / `DSH_HOME` / Python 解释器，凡在 `C:` 的红字报警。
   `DSH_HOME` 解析顺序：`-DshHome` > 环境变量 `DSH_HOME` > `D:\dsh`（若存在）> 用户目录（兜底）。
   迁移步骤见 [docs/赛前必读-D盘要求.md](docs/赛前必读-D盘要求.md)。
2. **装包冲突** —— PyNite 声明 `numpy>=2.4`，但 matplotlib 3.9 编译于 numpy 1.x，升到 2 会 `ImportError`。
   脚本用 `--no-deps` 装本地 wheel，强制回锁 `numpy==1.26.4 / scipy==1.11.4`，装完立刻导入自检。
3. **联网工具** —— `browser` / `context7` 属赛规禁止的联网检索，无论传什么参数都强制关闭。

配套脚本：

```powershell
python scripts/preflight.py          # 上机前预检（路径/依赖/MCP/知识库），不通过别开赛
python scripts/mcp_switch.py --list  # MCP 开关一览
python scripts/verify_setup.py       # 独立自检
scripts\dsh_update.ps1               # DSH 宿主版本护栏与一键更新
```

> 插件 `dsh-mech-workbench` 是 Host-only bundle，脚本装不了，需走创造模式；
> 但 `mcp/mech-kit/` 提供**绕过插件的等价能力**，见下。

---

## 仓库里有什么

### 一、工具线（算得动）

| 目录 | 内容 | 解决什么 |
|---|---|---|
| `mcp/sympy/` | sympy-mcp（Apache-2.0，32 工具） | 解方程/ODE/PDE、积分、矩阵特征值、LaTeX 输出 |
| `mcp/sympy-physics/` | 自建 7 工具 | 拉格朗日方程、运动学求导、合成运动（科氏）、梁的转角挠度、量纲检查 |
| `mcp/mech-solver/` | 自建 5 工具 | 能量法（卡氏/单位载荷）、桁架（含逐节点平衡校验）、刚体平面运动与瞬心、压杆稳定 |
| `mcp/mech-io/` | 自建 11 工具 | 边界工具：`py_run` 跑 Python、`pdf_page_crop` 取图纸局部、`numeric_compare` 独立校核、`kb_search` 查知识库 |
| `mcp/mech-model/` | 自建 1 工具 | **建模决策卡**：按题型列出「活决策轴」（选项 / 选错的后果链 / 判别试验），检查建模声明是否有缺失、未论证、互相矛盾。专治**建模轴沉默默认**，零依赖 |
| `mcp/mech-kit/` | 自建 1 工具 / 5 op | 直接调插件脚本，**绕过插件层**：17 种图像算子、静定反力+N/Q/M/T+8 项独立校核、力学图、原图标注 |
| `mcp/lean4/` | lean-mcp 单文件 | Lean 4 形式化检查 |
| `vendor/wheels/` | **PyNiteFEA 3.2.1（MIT）离线 wheel** | 三维刚架/桁架有限元。实测复核空间刚架：$M_A=5\sqrt2/18$、$T_B=2\sqrt2/9$，与解析解一致 |
| `plugins/dsh-mech-workbench/` | DSH 插件（9 工具） | 读题图、静定反力与内力图、截面几何、莫尔圆、出图自检 |

### 二、知识线（查得到）

| 目录 | 内容 | 规模 |
|---|---|---|
| `kb/raw/ocw311/` | **MIT OCW 3.11《Mechanics of Materials》全 60 篇讲义**（CC BY-NC-SA） | 14.7 MB |
| `kb/raw/NASA-SP-8007` | 薄壁圆柱壳屈曲手册（2020 修订版，公有领域） | 109 页 |
| `kb/theory/` | 《Mechanics Map》全 17 章 + 中文技能模块 | 38 个 md |
| `kb/examples/` | 从教材抽取的例题集 | 28 道 |
| `kb/index.jsonl` | **全文索引：2416 块 / 162.9 万字符** | 1.9 MB |

检索完全离线，零模型、零网络：

```powershell
python scripts/kb_index.py build                  # 建索引
python scripts/kb_index.py search "压杆 柔度 稳定" --top 5
python scripts/kb_index.py stat
```

按来源加权：判据卡 ×2.2 > 自检清单 ×1.8 > 教材 ×1.4 > 外部 PDF ×0.5。

### 三、流程线（错得少）

| 目录 | 内容 |
|---|---|
| `skills/mechanics-zh/modules/02-解题后自检.md` | 强制流程：九条硬规则 |
| `skills/mechanics-zh/modules/03-提高题建模清单.md` | 四道错题各提炼一条判据 |
| `skills/mechanics-zh/modules/04-题型判据卡.md` | 30 张卡：识别特征 → 第一步 → 高频坑 → 校核 |
| `skills/mechanics-map/` | 《Mechanics Map》17 章（CC BY-SA 4.0） |
| `skills/undergrad-physics-skill/` | 六步流程 + 8 类验算（量纲/回代/极限/守恒/定义域/抽样/独立方法/一致性） |
| `skills/math-skill/` | 数学推理与验证 |

---

## 九条硬规则（交卷前逐条打勾）

**35 分的失分里，绝大多数发生在「求解前」这一组，而不是算错。**

### A. 求解前（不满足不许动笔）

| # | 规则 | 动作 |
|---|---|---|
| 1 | **凡图必放大 / 必复述核对** | 有电子图：`img_crop(scale=3)` 逐个放大。纸质题：用户描述 → 我**文字复述 + 必出图**（`scripts/draw_figure.py`）→ 用户逐项核对 → 改完**重画再看一遍**。**铰支常画成端部空心小圆圈**，别当成"没画"——实测把铰支读成固支，压杆 $\mu$ 从 1.0 变 0.7，临界力差 2 倍 |
| 2 | **支座类型单独列一行** | 固支 / 铰支 / 滚动 / 弹簧 / 自由，逐项写明，放建模段第一行 |
| 3 | **建模轴先声明** | `model_card(action="probe")` 选题型 → `list` 看活决策轴 → `check` 提交声明。出现 `UNARGUED` / `CONFLICT` 就停下来改 |
| 4 | **分步题条件继承** | (1)(2)(3) 每问开头写一行：本问继承什么、什么已消失。「P 是否仍作用」「间隙是否已闭合」错一个整问归零 |

### B. 交卷前

| # | 规则 | 动作 |
|---|---|---|
| 5 | **截面积分过整体量** | 验 $\int\tau\,\mathrm dA=F_S$、$\int\sigma\,\mathrm dA=N$、$\int y\sigma\,\mathrm dA=M$ |
| 6 | **分段刚度建有限元** | EI/EA 沿杆长变化时**禁止手算积分**，建 3–4 个梁单元 |
| 7 | **二力杆先跑 `truss_solve`** | 先看内力**比**，再谈临界力与配比 |

### C. 结果出来之后（最容易被跳过）

| # | 规则 | 动作 |
|---|---|---|
| 8 | **力臂取矢量差** | 任何对点取矩，力臂必须是 **(作用点 − 矩心)** 的矢量差。先写 `(P−O)×F` 展开再代值；若 P 与 O 同高，力臂应只剩竖直分量——用它做退化校核。实测：矩心在 $y=L$ 却只用了 $P_y$，**结果形式完全正常、工具不会报错** |
| 9 | **"数脏"不是证伪** | 出现大分母、怪分数时，先查 ① 能否约分 ② 与同题其他小问是否自洽。**不要因为"不像出题人会写"就去改模型**——实测正确解的外表恰恰难看 |

**一句话**：能算 ≠ 算对。每个答案都要有一条**不依赖同一套推导**的路径去核对。

---

## 赛前合规检查

| # | 要求 | 怎么做 |
|---|---|---|
| 0 | **工具与知识库装在 D 盘** | `setup.ps1` 自动检查，见 [docs/赛前必读-D盘要求.md](docs/赛前必读-D盘要求.md) |
| 1 | **关掉联网 MCP** | `setup.ps1 -Competition` 强制关闭 `browser` / `context7` |
| 2 | **知识库 ≤ 200 MB** | 当前 21 MB（含索引），见 `python scripts/kb_index.py stat` |
| 3 | **不含赛题/答案** | 仓库与知识库都不得有当次赛题、答案、测试标签 |
| 4 | **留痕** | 保存模型信息、配置、prompt、检索片段、推理日志 |
| 5 | **省 token** | 同分看 token，别开一堆用不上的 MCP |

详见 [docs/规则摘要.md](docs/规则摘要.md)。

---

## 工具怎么选（按评分权重）

总分 = 答案正确性 **70%** + 过程与公式规范 **20%** + 表达/量纲/校核 **10%**。

| 环节 | 用什么 |
|---|---|
| 读题 | `document` 的 `pdf_text` / `pdf_render`；纸质题走 [docs/现场录入协议.md](docs/现场录入协议.md) |
| 读公式下标 | `mech-io` 的 `pdf_page_crop`（300 dpi 局部） |
| 建模轴 | `mech-model` 的 `model_card` |
| 符号推导 | `mcp__sympy__*` |
| 内力图 / 静定反力 | `mech-kit` 的 `analyze` / `diagram`（8 项校核直接当得分点） |
| 验算 | `undergrad-physics-skill` 的 F/B/L + `mech-io` 的 `scan_extremum` / `numeric_compare` |
| 量纲 | 技能里的 F 方法 + `sympy-physics` 的 `unit_check` |
| 出图自检 | `mech-io` 的 `plot_audit` / `fig_lint` |
| 交付打包 | `mech-io` 的 `html_to_pdf` / `submission_pack` |

详细映射见 [docs/工具映射.md](docs/工具映射.md)。

---

## 已知边界

- `mech-kit` 的 `analyze` **只解静定**：静不定、压杆稳定、塑性、大变形明确不做 → 手推 + `sympy`
- **曲杆/圆环、缠绕薄壁容器**没有现成库 → sympy 做平面假设积分 / 半环平衡
- `sympy` 有状态：`intro` → `introduce_expression` → `solve` → `reset_state`
- 知识库**没有中文教材**（版权所限），只有 MIT OCW / NASA / Mechanics Map 等开放资料
- 受限网络下 archive.org、madhuvable.org、ntrs.nasa.gov 均不可达，可用源记在 `kb/README.md`

---

## 体积

| 项 | 数值 |
|---|---|
| 仓库总计 | **43.1 MB**（工作树 24.3 + `.git` 18.7） |
| 其中知识库 `kb/` | 21.1 MB |
| 赛规上限 | 200 MB |

---

## 插件怎么装（脚本管不了）

```
设置 → Agent 预设 → 创造入口（cordis 预设）→ 新开会话
plugin_manager → action: install_bundle
              → target: <本仓库>/plugins/dsh-mech-workbench
装完重启 DSH
```

装不了也没关系：`mcp/mech-kit/` 已能直接调用插件脚本，覆盖大部分能力。

---

## 许可与来源

| 部分 | 许可 |
|---|---|
| 本仓库自建代码与文档 | 随意使用 |
| `mcp/sympy` | Apache-2.0 |
| `vendor/wheels/pynitefea` | **MIT** |
| `skills/mechanics-map`、`kb/theory/*mechanics-map*` | **CC BY-SA 4.0**（署名 Jacob Moore and Contributors，派生须同协议） |
| `kb/raw/ocw311` | **CC BY-NC-SA**（MIT OpenCourseWare 3.11） |
| `kb/raw/NASA-SP-8007` | 美国政府作品，公有领域 |
| `skills/math-skill`、`skills/undergrad-physics-skill` | MIT |
| `skills/mechanics-zh`、`plugins/dsh-mech-workbench` | 自研 / MIT |

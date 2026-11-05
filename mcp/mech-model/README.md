# mech-model MCP —— 建模决策卡

> 自建，零第三方依赖。
> 解决的是**建模轴沉默默认**，不是算力问题。

## 为什么有这个服务

2026-11 用第十四届（120 分）实测：**93/120**（答案口径）。失分最重的第 6 题（−17 分）
不是算错，是两条建模轴走了默认：

| 建模轴 | 我的默认 | 正确 |
|---|---|---|
| 锥面滚动半径沿横向的梯度方向 | 向外增大 | 向辋内（法兰侧）增大 |
| 轮对轴线能否绕纵向轴倾斜 | 假定始终水平 | 必须倾斜（两轮半径不等） |

求解器再准也按错模型算。**缺的不是算力，是声明。**

## 工具

只有一个工具：`model_card`

| action | 入参 | 作用 |
|---|---|---|
| `index` | — | 列全部题型 + 通用轴 |
| `probe` | `text` | 按题干关键词给候选题型（只是候选，人定） |
| `list` | `problem_class` | 给该题型的活决策轴：选项 / 选错的后果链 / 判别试验 |
| `check` | `problem_class`, `decisions` | 返回 缺失 / 未论证 / 互相矛盾 |

`decisions` 格式：

```json
{"cone_taper": {"value": "半径向辋内(法兰侧)增大", "evidence": "figure"}}
```

`evidence` 只能取 `statement` / `figure` / `textbook` / `derived`；
**空值或 `assumed` 一律判 block**。

## 判定规则

| code | 触发 | 级别 |
|---|---|---|
| `MISSING` | 该轴没填 | error |
| `UNARGUED` | `evidence` 为空或 `assumed` | error |
| `BAD_VALUE` | 取值不在选项内 | error |
| `CONTRADICTS_STEM` | 与题干钉死值冲突 | error |
| `CONFLICT` | 两条声明之间物理/几何上不成立 | error 或 warn |

`check` 返回的 `filled` 即留痕里的「建模声明」，可直接写进过程日志。

## 现有题型（6 张）

| id | 覆盖 |
|---|---|
| `statics_friction` | 静力 / 摩擦 / 翻转 / 组合梁 |
| `multibody_lagrange` | 齿轮系、行星轮、曲柄连杆等 2+ 自由度系统 |
| `beam_strength` | 梁、截面应力、强度理论、危险点 |
| `curved_member_impact` | 曲杆、冲击、压缩稳定、组合受力 |
| `large_deflection` | 分段变截面构件的大变形（elastica） |
| `rail_vehicle` | 轮轨 / 锥形轮对 / 蠕滑 / 蛇行 |

每张卡另叠 3 条通用轴（符号约定 / 小变形判定 / 载荷死载或随动）。

## 加一张卡

编辑 `cards.json`：

```json
"your_type": {
  "name": "中文名",
  "triggers": ["题干里会出现的词"],
  "axes": [{
    "id": "轴id",
    "question": "一句话问题",
    "options": ["选项A", "选项B"],
    "if_wrong": "选错的后果——要写清会连锁影响哪些量",
    "test": "判别试验——怎么用图/实物/极限确认",
    "pinned": null
  }],
  "conflicts": [
    {"when": {"轴id": "选项A"}, "message": "为什么不行", "severity": "error"}
  ]
}
```

写卡的三条纪律：

1. **只写方法论与判据，不写任何赛题答案**（仓库 README 的硬约定）
2. `if_wrong` 要写成**下游影响链**（哪个符号会翻），不是"会错"
3. `test` 必须是**能用图或极限做完的操作**，不是"再想想"

## 自检

用仓库注册时的同一个解释器（`setup.ps1` 会告诉你路径）；不需要任何第三方依赖。

```powershell
# 20 项逻辑自检（含第十四届第 6 题回归）
python mcp/mech-model/test/selftest.py

# MCP 协议握手（真起进程走 initialize/tools/list/tools/call）
python mcp/mech-model/test/handshake.py
```

换机器部署前，先跑一遍全仓预检：

```powershell
python scripts/preflight.py
```

它会检查 `.ps1` 的 BOM+CRLF、文本编码、Python 语法、JSON 可解析、绝对路径硬编码、
`cards.json` schema，并真跑上面两个自检。

## 体积与 Token

| 项 | 量 |
|---|---|
| 代码 + 卡 | ~25 KB |
| 工具描述 | 244 字符（≈ 120 token/轮） |
| 第三方依赖 | 0 |

赛规 Token 计量含系统提示，所以刻意只做**一个工具 + 一个 action 枚举**，
不拆成 4 个独立工具（那样约 1000 token/轮）。

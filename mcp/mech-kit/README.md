# mech-kit MCP —— 把 dsh-mech-workbench 的脚本直接拿来用

> 自建（1 工具 / 5 个 op），零第三方依赖。
> **不走插件层**：不需要创造模式、不需要 `install_bundle`、不占 profile 配置。

## 为什么不装插件

`plugins/dsh-mech-workbench/` 里那 9 个工具，本体就是 `scripts/*.py` 里的 **8 个独立 CLI**：

```
analyze.py  annotate.py  figure.py  preprocess.py
presets.py  render_math.py  symbolic.py  vision.py
```

全部 `--spec <file>` 或 `--spec-json '<json>'` 进、JSON 出、带退出码。插件那层只是
（a）把它们注册成宿主工具（b）做无损 JSON 守卫。注册要创造模式 + 授权 + 重启 DSH，
换台机器还得再来一遍。

**包一层 MCP 就变成仓库资产**：跟着 git 走、`setup.ps1` 注册、`preflight.py` 检查。

## 工具

一个工具 `mech_kit(op, spec)`，`spec` 原样透传给脚本。

| op | 脚本 | 干什么 | 依赖 |
|---|---|---|---|
| `preprocess` | `preprocess.py` | **17 种图像算子**：`probe` 探测、`zoom` 局部放大、`deskew` 转正、`perspective` 透视校正、`binarize`、`enhance_text`、`auto_orient`、`autocontrast`、`split` 一页多题分栏… | Pillow + numpy |
| `analyze` | `analyze.py` | 静定反力、N/Q/M/T、截面几何、应力、**8 项独立校核**、**静定/静不定判别**（`determinate`） | numpy |
| `diagram` | `figure.py` | 力学标准图：轴力/剪力/弯矩/扭矩/应力分布/莫尔圆/挠曲线，多图共享 x 轴 | matplotlib（缺则降级 Pillow） |
| `annotate` | `annotate.py` | 在学生**原图**上标注：框/圈/箭头/尺寸线/文字/局部放大 | Pillow + numpy |
| `info` | — | 自检：脚本是否存在、依赖是否齐、解释器路径 | — |

**不包**（走云端 API，赛规禁用）：
`second_reader`（原 `mech_read_problem` 的二次转写）、`viz_check`、`render_math`。
它们的调用链是 `siliconflow → 智谱 GLM → DeepSeek → 商汤 → Gemini`，要从
`~/.dsh/secrets/media-tools.env` 或 `.credentials.yaml` 读 key。离线环境下如实失败，
所以不包——需要"第二意见"时用 `img_crop` 双裁双读代替。

## 为什么值得包

它补的正好是**两次实测里最贵的那类错误——读图**：

| 实测教训 | 对应 op |
|---|---|
| 把压杆端部的空心小圆圈（铰支）读成固支 → 长度系数 1.0 变 0.7 → 临界力差 2 倍 | `preprocess {op:"zoom", box:[...], factor:3}` |
| 锥面朝向读反 → 整条符号链反号 | 同上 |
| 手机拍歪 / 扫描发灰 → 小字糊 | `deskew` / `perspective` / `enhance_text` / `binarize` |
| 没画受力图丢 6 分 | `diagram` / `annotate` |
| 截面积分忘了过整体量（硬规则 5） | `analyze` 的 8 项校核里直接含 `∫σdA=N`、`∫yσdA=M` |

## 用法示例

```jsonc
// 放大图上可疑区域（box 是 0–1 归一化，与图片像素无关）
{"op":"preprocess","spec":{
   "src":"题干页.png","out":"放大.png",
   "ops":[{"op":"zoom","box":[0.52,0.45,0.75,0.62],"factor":3}]}}

// 静定梁：反力 + 内力 + 8 项校核 + 静定判别
{"op":"analyze","spec":{
   "kind":"beam","length":4,
   "supports":[{"x":0,"type":"pin"},{"x":4,"type":"roller"}],
   "loads":[{"type":"point_force","x":2,"value":-10,"dir":"transverse"}],
   "section":{"shape":"rect","params":{"b":0.1,"h":0.2},"E":200000}}}

// 在原图上圈出并标注
{"op":"annotate","spec":{
   "src":"题干页.png","out":"标注.png",
   "ops":[{"op":"box","box":[0.55,0.49,0.70,0.58],"color":"#e11","width":4},
          {"op":"text","at":[0.55,0.60],"text":"D端：空心圆=铰支","size":30}]}}
```

## 符号约定（与 `analyze` 一致）

轴力 **N 拉为正**；剪力 **Q 使微段顺时针转为正**；弯矩 **M 下侧受拉为正**；
扭矩 **T 右手螺旋 +x 为正**；横向力向上为正；集中力偶逆时针为正。
默认单位 `m / kN / kN·m / MPa`。

## 自检

```powershell
python mcp/mech-kit/test/selftest.py     # 起真进程走 MCP 协议，验 info / preprocess / analyze
python scripts/preflight.py              # 全仓预检（含本服务的脚本存在性）
```

## 已知限制

1. **`figure.py` 的测试用例里有原作者路径**（`C:\Users\丁曹扬\...`）。`test/` 不随插件发布，
   spec 里的 `out` 必须自己覆盖，否则报 `PermissionError`。
2. **`analyze` 只解静定问题**。静不定返回 `determinate: false` 并说明需变形协调，不猜结果；
   不做塑性、压杆稳定、大变形、剪切修正；截面沿 x 常量（变截面要拆成多段 spec）。
3. **`diagram` 的 spec 形状要按 `presets.py` 展开**，直接丢一个 `analyze` 的输出进去不会自动成图。

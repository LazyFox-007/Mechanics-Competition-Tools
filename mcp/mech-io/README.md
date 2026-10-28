# mech-io —— 竞赛现场的「边界工具」

> 10 个工具，专治比赛里**不产生分数、但会吃掉时间**的四类边界。
> 不是解方程的工具（那有 sympy / sympy-physics），是**让解方程这件事不被打断**的工具。

## 为什么单独一个服务

复盘一次真实演练（3 道周培源真题）时，9 次重试的分布是：

| 归因 | 次数 | 具体 |
|---|---|---|
| shell / 编码边界 | 3 | PowerShell 把中文弯引号当定界符；控制台 GBK 让 `print` 中文崩 |
| 图形自检 | 3 | 阴影区画反、两层被压成一条线、下标缺字形 |
| 读题 | 1 | PDF 文字层丢下标，`E₁=E₃=E₂/5=E` 成乱码 |
| 算术 | 1 | 落点漏了初始横坐标偏移 |

也就是说：**2/3 的摩擦与力学无关**。这 10 个工具就是把这 2/3 抹平。

## 工具

| # | 工具 | 作用 | 替代掉的做法 |
|---|---|---|---|
| 1 | `io_info` | 自检：Pillow / PyMuPDF / numpy / sympy / 浏览器 是否可用 | 逐个试 import |
| 2 | `py_run` | 跑 Python（脚本或内联），UTF-8、argv 数组、不经 shell | `pwsh -Command "python -c \"...\""` ← 引号地狱 |
| 3 | `img_crop` | 按**分数坐标**裁剪/放大图片 | 先量预览图再换算原图（必错） |
| 4 | `pdf_page_crop` | 从 PDF 某页直接取局部高清图（默认 300 dpi） | 整页 170 dpi 渲染 → 再裁 → 再放大 |
| 5 | `fig_lint` | 图片级体检：尺寸/DPI/空白/触边/重复 | 靠眼看出图是否空、是否裁掉 |
| 6 | `plot_audit` | 跑绘图脚本并审计：缺字形、文字越界、文字重叠 | 出图后逐张看，看到第三张才发现问题 |
| 7 | `scan_extremum` | 表达式在区间上密扫描找极值 + 边界判定 | 手写 meshgrid（每次都重写） |
| 8 | `numeric_compare` | 两表达式在网格上比数值一致度 | 手写残差脚本 |
| 9 | `html_to_pdf` | Edge/Chrome 无头打印 HTML→PDF（A4、无页眉页脚） | 装 Office / 手搓 LaTeX 工具链 |
| 10 | `submission_pack` | 按赛规命名建提交骨架 + 生成 SHA-256 清单 | 手建目录、手算哈希 |

## 装

和 `sympy-physics` 一样：`setup.ps1` 会把它写进 `~/.dsh/cordis.patch.yml`。

```powershell
pwsh -File setup.ps1
# 装完重启 DSH
```

手工注册见 [`dsh/cordis.patch.snippet.yml`](../../dsh/cordis.patch.snippet.yml) 的 `mech-io` 段。

## 依赖

| 工具 | 需要 | 缺了会怎样 |
|---|---|---|
| `py_run` / `submission_pack` / `html_to_pdf` | 标准库 + 浏览器 | 浏览器缺失时 `html_to_pdf` 明确报错 |
| `img_crop` / `fig_lint` | Pillow | 返回 `ok:false` 并给出 `pip install pillow` |
| `pdf_page_crop` | PyMuPDF | 建议改用 `document` MCP 的 `pdf_render` |
| `scan_extremum` / `numeric_compare` | numpy + sympy | 明确报错 |
| `plot_audit` | matplotlib（跑的是你的脚本） | 明确报错 |

**没有硬依赖**：缺哪个就只少哪个工具，服务照常起。

## 自测

```bash
python mcp/mech-io/test/selftest.py
# 带 PDF 可多测一项：python mcp/mech-io/test/selftest.py --pdf D:/exam.pdf
```

当前 **16/16 通过**（含中文 argv、中文 stdout、分数裁剪、公式页裁剪、缺字形/越界检测、极值扫描、HTML→PDF、提交清单）。

> 注意：`--pdf` 的路径若含中文弯引号 `“”`，**别从 PowerShell 直接传**——它会拆坏参数。
> 用 ASCII 路径的副本，或直接让 `py_run` 去复制（这正是工具 2 存在的理由）。

## 边界（别指望它）

1. `fig_lint` 只做**图像级**判断；坐标轴方向反了、层次比例失真这类**语义错误**它查不出——那要靠 `viz_check`（视觉模型）或人眼。
2. `plot_audit` 只审计 `Figure.savefig` 之前的状态；用 `plt.show()` 或第三方封装的保存路径抓不到。
3. `pdf_page_crop` 不做版面分析，不给“这页哪块是公式”——坐标要你自己给（配合 `pdf_text` 的页内顺序推断）。
4. `scan_extremum` 是密扫描，精度受 `grid_step` 限制；**极值落在边界时结果无效**，它会用 `on_boundary` 告诉你。
5. `html_to_pdf` 不保证和浏览器“打印预览”像素一致（页边距走 CSS `@page`）。

## 许可

自建，随意使用。

# DSH 宿主版本兼容性

> 本文件回答两件事：**从官网下载的是不是最新版**、**换到新版本会不会把仓库搞坏**。
> 登记值在 [`dsh/TESTED_DSH.json`](../dsh/TESTED_DSH.json)，`preflight.py` 第 10 节会自动比对。

---

## 一、版本现状（2026-11-06 实测）

| 项 | 值 |
|---|---|
| 本机已装 | **0.2.1-rc.5**（安装于 2026-10-29） |
| 官方最新 | **0.2.2-rc.1**（发布 2026-11-04） |
| 更新通道 | `nightly`（stable / beta / latest 三条 feed 全部 404，**只有 nightly**） |
| feed | `https://download.deepseek.com/dsh-desk/feeds/win-x64/nightly.yml` |
| 官网下载 | `https://download.deepseek.com/desktop/dsh-latest-windows-x64.exe` |

**官网下载页给的就是最新版**，已用文件指纹确认：

```
官网 dsh-latest-windows-x64.exe   size 293425336   ETag ecd1d9880f68ec91a63b4936163bfc44
nightly 0.2.2-rc.1 安装包          size 293425336   ETag ecd1d9880f68ec91a63b4936163bfc44
```

两者大小与 ETag 完全一致 ⇒ **同一个文件**。所以"从官网下载"拿到的是 0.2.2-rc.1，比本机新一版。

> 网络上能搜到 "DeepSeek Harness Desktop 5.2.0" 之类版本号，来自第三方仓库
> （`ningbainb/deepseek-harness-desktop`），**不是官方**，不要用来判断版本。
> 官方版本号形如 `0.2.x-rc.y`，发布方签名是 Hangzhou DeepSeek Artificial Intelligence Co., Ltd.。

---

## 二、仓库对宿主的依赖面（只有 3 处）

| 依赖 | 在哪 | 断了会怎样 |
|---|---|---|
| `~/.dsh/cordis.patch.yml` 里 `insert` 的 MCP 条目结构 | `setup.ps1`、`scripts/verify_setup.py`、`scripts/mcp_switch.py` | **所有 MCP 消失**，工具全没了 |
| `~/.dsh/skills/` 被扫描加载 | `setup.ps1` 复制 4 套技能 | 技能（六步流程、KB）不加载 |
| `~/.dsh/secrets/media-tools.env`、`~/.dsh/.credentials.yaml` | 云端工具读 key | 只有联网工具受影响（赛时本就禁用） |

**不受影响**：插件 bundle 接口——`mcp/mech-kit/` 直接调 `plugins/dsh-mech-workbench/scripts/*.py`，
不经过宿主注册，所以插件装不装、宿主怎么改，读图与静定分析都照跑。
profile 的 `.generations` 布局也只有装插件时才涉及。

> 换句话说：**升级 DSH 的最大风险是 `cordis.patch.yml` 的 schema 变了**，
> 其余都是文件层面的东西，换个目录也能用。

---

## 三、升级前后怎么做

### 升级前：留好回滚

更新器缓存里已经有当前版本的完整安装包，**先把它复制出来**（缓存会被自动清理）：

```
%LOCALAPPDATA%\@deepseek-aidsh-desktop-updater\pending\deepseek-harness-0.2.1-rc.5-win-x64.exe
```

复制到与仓库同级的目录（如 `D:\mechanics-competition-tools-rollback\`），
并记下文件名里的版本号。

### 装不上：`MoveFileExW` / Windows error 32

**症状**：点更新、转一圈、版本没变；更新器缓存里堆出 `installer-logs\directory-failure-*.log`。

**原因**：NSIS 安装器要先把 `Programs\DeepSeek Harness` 改名成
`DeepSeek Harness.old-{GUID}` 再铺新文件。DSH 自己开着 6 个进程（主进程 +
`--type=gpu-process` + `--type=renderer` + `--type=utility` + `--expose-internals`，
后者还挂着二三十个 MCP 子进程），目录被句柄锁死 → `error 32`，安装器重试 10 次全失败。

**和网络/权限/签名无关**：`pending\update-info.json` 里的 `sha512` 与官方 feed 一致就说明包是好的。

**一键处理**（在**独立的** PowerShell 窗口里跑，因为它会结束 DSH）：

```powershell
# 先体检，不动任何进程
pwsh -File scripts\dsh_update.ps1

# 确认无误后执行：结束进程树 -> 等解锁 -> 静默安装 -> 复核版本
pwsh -File scripts\dsh_update.ps1 -Apply
```

脚本做四件事：① 列占用进程与历史失败日志 ② 结束 DSH 整棵进程树（含 MCP 子进程）
③ 轮询到目录可独占打开（`TimeoutSec` 默认 60 秒）④ 跑安装器 `-Wait` 并比对注册表版本，
成功后自动重启 DSH。

**若仍报「目录被占用」**：注销一次 Windows 再登录（比重启快），然后重跑 `-Apply`。

> 为什么不在应用内点「重启并更新」：那条路会复用同一个安装器，而它没有先确保所有
> 子进程退干净，于是每次都卡在同一处。手动 `-Apply` 至少能把进程树杀干净再装。

### 升级后：按顺序跑这四步

| # | 动作 | 判据 |
|---|---|---|
| 1 | `python scripts\preflight.py` | 第 10 节显示版本一致；末尾 `FAIL 0` |
| 2 | `python scripts\verify_setup.py` | 它**真的 spawn 每个 MCP**；7 个全 `[OK]`，结论「全部就绪」 |
| 3 | 新开会话看工具 | `mcp__mech-model` / `mcp__mech-kit` 出现；没出现就重启 DSH |
| 4 | 跑一遍自检 | `mech-model/test/selftest.py` → `PASS 60 / FAIL 0` |

### 出问题的两条分支

- **MCP 全没出来** ⇒ 最可能是 `cordis.patch.yml` 的 `insert` 结构变了。
  备份 `~/.dsh/cordis.patch.yml` → 重跑 `setup.ps1` → 看宿主报什么 → 照报错改条目。
  对照文件：[`dsh/cordis.patch.snippet.yml`](cordis.patch.snippet.yml)。
- **改不动 / 赛场在即** ⇒ 直接用回滚包装回 0.2.1-rc.5，别在赛前硬扛。

---

## 四、什么时候升级

**不要等到赛前。** 更新器是 `nightly` 通道且 `stagingPercentage: 100`，意味着它自己会升上来；
与其让它在不合适的时候动，不如现在（还有时间改）主动升，并按上面四步验一遍。

升级完成后，把 `dsh/TESTED_DSH.json` 的 `tested` 改成新版本号，
`preflight.py` 第 10 节才会恢复「版本一致」。

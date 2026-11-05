#Requires -Version 5.1
<#
.SYNOPSIS
    力学竞赛工具一键配置
.DESCRIPTION
    把本仓库的力学/数学工具装进 DeepSeek Harness：
      1. 复制两套技能到 ~/.dsh/skills
      2. 把 sympy / lean4 两个 MCP 写进 ~/.dsh/cordis.patch.yml（附备份）
      3. 检查 Python 依赖
      4. 打印还差什么（插件要手工装、赛前要关联网工具）
    改配置前一律备份。
.PARAMETER DshHome
    DSH 配置根目录，默认 ~/.dsh
.PARAMETER PythonExe
    指定跑 sympy/lean4 的解释器；默认自动找一个装了 sympy 和 mcp 的
.PARAMETER DryRun
    只打印将要做什么，不落盘
.PARAMETER Competition
    竞赛模式：保留 document / sympy / sympy-physics / mech-io / mech-solver，
    外加本地文件检索 everything（不联网、体积小，且 ~/.dsh/AGENTS.md 的路由表依赖它）。
    其余 MCP（video/image/tools/eac/rea/…）disabled，省 token（同分看 token）。
    browser / context7 属赛规禁止的联网工具，无论 -KeepMCP 传什么都强制关闭。
.PARAMETER KeepMCP
    在默认保留清单之外额外保留的 MCP 服务名（逗号分隔）。
    例：-KeepMCP image,video。不能用于保留联网工具（会被拒绝）。
.PARAMETER NoEverything
    连 everything 一起关掉，走“最省 token”档；代价是路由表第一行（找文件）失效。
.PARAMETER Verify
    重启 DSH 之后跑：真的把每个 MCP 拉起来，走 initialize + tools/list，
    报工具数与耗时；再查技能、插件、依赖。不写任何配置。
.PARAMETER Restore
    回滚到最近一次（或用 -BackupPath 指定）的 cordis.patch.yml 备份。
.PARAMETER InstallDeps
    先 pip 装缺的依赖（sympy / mcp / pyyaml / pillow / pymupdf / numpy / matplotlib）。
.EXAMPLE
    pwsh -File setup.ps1 -Competition
.EXAMPLE
    pwsh -File setup.ps1 -Verify
.EXAMPLE
    pwsh -File setup.ps1 -Restore
#>
[CmdletBinding()]
param(
    [string]$DshHome = '',
    [string]$PythonExe = '',
    [switch]$DryRun,
    [switch]$Competition,
    [string[]]$KeepMCP = @(),
    [switch]$NoEverything,
    [switch]$Verify,
    [switch]$Restore,
    [string]$BackupPath = '',
    [switch]$InstallDeps
)

$ErrorActionPreference = 'Stop'
# PowerShell 控制台默认按 GBK 解子进程输出，Python 打中文会乱码
$env:PYTHONIOENCODING = 'utf-8'
$env:PYTHONUTF8 = '1'

function Info($m) { Write-Host $m }
function Step($m) { Write-Host "`n=== $m" -ForegroundColor Cyan }
function Ok($m)   { Write-Host "  [OK] $m" -ForegroundColor Green }
function Warn($m) { Write-Host "  [!] $m" -ForegroundColor Yellow }
function Bad($m)  { Write-Host "  [x] $m" -ForegroundColor Red }

# ---------- 路径 ----------
if ([string]::IsNullOrWhiteSpace($PSScriptRoot)) {
    $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
} else {
    $scriptDir = $PSScriptRoot
}
$RepoRoot = $scriptDir
if ([string]::IsNullOrWhiteSpace($DshHome)) {
    # 赛规：工具与知识库须在 D 盘。优先级：显式 -DshHome > 环境变量 DSH_HOME > D:\dsh（若已存在）> 用户目录（兜底，会报警）
    if ($env:DSH_HOME) { $DshHome = $env:DSH_HOME }
    elseif (Test-Path 'D:\dsh') { $DshHome = 'D:\dsh' }
    else { $DshHome = Join-Path $env:USERPROFILE '.dsh' }
}
$Cordis = Join-Path $DshHome 'cordis.patch.yml'

# ---------- 工具函数：找一个能用 pyyaml 的解释器 ----------
function Get-ToolPython {
    $cands = @()
    if ($PythonExe) { $cands += $PythonExe }
    if ($env:DSH_MECH_PYTHON) { $cands += $env:DSH_MECH_PYTHON }
    $cands += 'D:\anaconda\python.exe'
    $cands += (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python311\python.exe')
    $p = Get-Command python -ErrorAction SilentlyContinue
    if ($p) { $cands += $p.Source }
    foreach ($c in ($cands | Where-Object { $_ -and (Test-Path $_) } | Select-Object -Unique)) {
        & $c -c "import yaml" 2>$null
        if ($LASTEXITCODE -eq 0) { return $c }
    }
    return $null
}

# ---------- 早退分支：-Verify / -Restore / -InstallDeps ----------
if ($Verify) {
    $py = Get-ToolPython
    if (-not $py) { Bad '没找到带 pyyaml 的解释器（用 -PythonExe 指定）'; exit 1 }
    Write-Host "`n=== 工具链自检（真的把每个 MCP 拉起来）===" -ForegroundColor Cyan
    & $py (Join-Path $RepoRoot 'scripts\verify_setup.py')
    exit $LASTEXITCODE
}

if ($Restore) {
    $py = Get-ToolPython
    if (-not $py) { Bad '没找到带 pyyaml 的解释器（用 -PythonExe 指定）'; exit 1 }
    Write-Host "`n=== 回滚 MCP 配置 ===" -ForegroundColor Cyan
    if ($BackupPath) {
        & $py (Join-Path $RepoRoot 'scripts\mcp_switch.py') '--restore' $BackupPath
    } else {
        & $py (Join-Path $RepoRoot 'scripts\mcp_switch.py') '--restore'
    }
    exit $LASTEXITCODE
}

if ($InstallDeps) {
    $py = $PythonExe
    if (-not $py) { foreach ($c in @('D:\anaconda\python.exe', (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python311\python.exe'))) { if (Test-Path $c) { $py = $c; break } } }
    if (-not $py) { $p = Get-Command python -ErrorAction SilentlyContinue; if ($p) { $py = $p.Source } }
    if (-not $py) { Bad '没找到 Python'; exit 1 }
    Write-Host "`n=== 安装 Python 依赖（$py）===" -ForegroundColor Cyan
    & $py -m pip install --disable-pip-version-check -q sympy mcp pyyaml pillow pymupdf numpy matplotlib
    if ($LASTEXITCODE -eq 0) { Ok '基础依赖安装完成' } else { Warn 'pip 返回非 0，检查上面的输出' }

    # --- PyNite（3D 刚架/桁架，MIT，离线 wheel） ---
    # 冲突预警：PyNiteFEA 声明 numpy>=2.4，但本机 matplotlib 3.9 编译于 numpy 1.x，
    # 升到 numpy 2 会 ImportError（matplotlib._path）。实测 PyNite 3.2.1 在 numpy 1.26 下工作正常，
    # 因此用 --no-deps 装 wheel，并把 numpy/scipy 回锁到已知兼容版本。
    $wheelDir = Join-Path $RepoRoot 'vendor\wheels'
    $whl = Get-ChildItem $wheelDir -Filter 'pynitefea*.whl' -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($whl) {
        & $py -m pip install --disable-pip-version-check -q --no-deps $whl.FullName
        & $py -m pip install --disable-pip-version-check -q "numpy==1.26.4" "scipy==1.11.4"
        $probe = & $py -c "from Pynite import FEModel3D; import numpy; print(numpy.__version__)" 2>$null
        if ($LASTEXITCODE -eq 0) { Ok "PyNite 已装（离线 wheel，numpy 回锁 $probe）" }
        else { Warn 'PyNite 导入失败：检查 numpy 是否被升到 2.x（见 docs/工具映射.md）' }
    } else { Warn 'vendor\wheels 下没有 PyNiteFEA*.whl，跳过' }

    exit $LASTEXITCODE
}

Step '1/4 环境确认'
Info "仓库    : $RepoRoot"
Info "DSH_HOME: $DshHome"

# ---------- 赛规硬要求：工具与知识库必须装在 D 盘 ----------
$pathsOnC = @()
if ($DshHome -match '^[Cc]:') { $pathsOnC += "DSH_HOME = $DshHome" }
if ($RepoRoot -match '^[Cc]:') { $pathsOnC += "仓库     = $RepoRoot" }
$pyPath = $PythonExe; if (-not $pyPath) { $pyPath = (Get-Command python -ErrorAction SilentlyContinue).Source }
if ($pyPath -and ($pyPath -match '^[Cc]:')) { $pathsOnC += "Python   = $pyPath" }
if ($pathsOnC.Count -gt 0) {
    Write-Host ""
    Bad '========== 赛规不合规：以下路径在 C 盘 =========='
    $pathsOnC | ForEach-Object { Warn "  $_" }
    Warn '赛规要求：解题工具与知识库必须安装在 D 盘。请迁移后重跑本脚本。'
    Warn '迁移方法见 docs/赛前必读-D盘要求.md'
    Write-Host ""
} else {
    Ok 'D 盘要求：仓库 / DSH_HOME / Python 均在 D 盘'
}

if (-not (Test-Path (Join-Path $RepoRoot 'skills'))) { Bad '仓库结构不对，找不到 skills/'; exit 1 }
if (-not (Test-Path $DshHome)) { Warn 'DSH_HOME 不存在，请确认 DSH 已装并至少启动过一次'; }

# ---------- 找 Python ----------
Step '2/4 查找 Python 解释器'
$cands = @()
if ($PythonExe) { $cands += $PythonExe }
if ($env:DSH_MECH_PYTHON) { $cands += $env:DSH_MECH_PYTHON }
$cands += 'D:\anaconda\python.exe'
$cands += (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python311\python.exe')
$pyCmd = Get-Command python -ErrorAction SilentlyContinue
if ($pyCmd) { $cands += $pyCmd.Source }

$py = $null
$pyVer = $null
$cands = $cands | Where-Object { $_ -and (Test-Path $_) } | Select-Object -Unique
foreach ($c in $cands) {
    try {
        $out = & $c -c "import sympy, mcp; print(sympy.__version__)" 2>$null
        if ($LASTEXITCODE -eq 0 -and $out) {
            $py = $c; $pyVer = $out.Trim(); break
        }
    } catch { }
}
if ($py) {
    Ok "使用 $py （sympy $pyVer）"
} else {
    Bad '没找到同时有 sympy 和 mcp 的解释器'
    Info '  装了 anaconda 的话，确认 D:\anaconda\python.exe 存在'
    Info '  否则先跑：<python> -m pip install sympy mcp'
    Info '  或用 -PythonExe 指定'
}

# ---------- 复制技能 ----------
Step '3/4 安装技能'
$skillSrc = Join-Path $RepoRoot 'skills'
$skillDst = Join-Path $DshHome 'skills'
$installed = @()
foreach ($d in Get-ChildItem $skillSrc -Directory) {
    $target = Join-Path $skillDst $d.Name
    if (Test-Path $target) { Warn "$($d.Name) 已存在，覆盖（旧版保留 .bak）" }
    if (-not $DryRun) {
        New-Item -ItemType Directory -Force -Path $skillDst | Out-Null
        if (Test-Path $target) {
            $bak = "$target.bak-" + (Get-Date -Format 'yyyyMMdd-HHmmss')
            Move-Item $target $bak
        }
        Copy-Item $d.FullName $target -Recurse -Force
    }
    $installed += $d.Name
    Ok $d.Name
}

# ---------- 写 MCP 配置 ----------
Step '4/4 注册 MCP'
if (-not $py) {
    Warn '跳过（没有可用 Python）'
} else {
    $repoPosix = $RepoRoot -replace '\\', '/'
    # YAML 单引号内反斜杠是字面量，不能再转义，否则路径会变成双反斜杠而失效
    $pyYaml = $py

    $blkSympy = @"

- insert:
    - id: mech-sympy
      name: '@deepseek-ai/dsh-mcp-client'
      config:
        serverName: sympy
        transport: stdio
        command: '$pyYaml'
        args:
          - '$repoPosix/mcp/sympy/server.py'
"@

    $blkLean = @"
- insert:
    - id: mech-lean4
      name: '@deepseek-ai/dsh-mcp-client'
      config:
        serverName: lean4
        transport: stdio
        command: '$pyYaml'
        args:
          - '$repoPosix/mcp/lean4/server.py'
"@

    $blkPhys = @"
- insert:
    - id: mech-sympy-physics
      name: '@deepseek-ai/dsh-mcp-client'
      config:
        serverName: sympy-physics
        transport: stdio
        command: '$pyYaml'
        args:
          - '$repoPosix/mcp/sympy-physics/server.py'
"@

    $blkIo = @"
- insert:
    - id: mech-io
      name: '@deepseek-ai/dsh-mcp-client'
      config:
        serverName: mech-io
        transport: stdio
        command: '$pyYaml'
        args:
          - '$repoPosix/mcp/mech-io/server.py'
"@

    $blkSolver = @"
- insert:
    - id: mech-solver
      name: '@deepseek-ai/dsh-mcp-client'
      config:
        serverName: mech-solver
        transport: stdio
        command: '$pyYaml'
        args:
          - '$repoPosix/mcp/mech-solver/server.py'
"@

    $blkModel = @"
- insert:
    - id: mech-model
      name: '@deepseek-ai/dsh-mcp-client'
      config:
        serverName: mech-model
        transport: stdio
        command: '$pyYaml'
        args:
          - '$repoPosix/mcp/mech-model/server.py'
"@

    $existing = ''
    if (Test-Path $Cordis) { $existing = Get-Content $Cordis -Raw -Encoding UTF8 }

    # 锚定匹配：避免 sympy 命中 sympy-physics
    $want = [ordered]@{
        'sympy'         = $blkSympy
        'lean4'         = $blkLean
        'sympy-physics' = $blkPhys
        'mech-io'       = $blkIo
        'mech-solver'   = $blkSolver
        'mech-model'    = $blkModel
    }
    $missing = @()
    foreach ($name in $want.Keys) {
        $pat = '(?m)^\s*serverName:\s*' + [regex]::Escape($name) + '\s*$'
        if ($existing -notmatch $pat) { $missing += $name }
    }

    if ($missing.Count -eq 0) {
        Warn 'sympy / lean4 / sympy-physics / mech-io / mech-solver / mech-model 都已在配置里，不重复添加'
        Info '  想换成本仓库的副本，先删掉旧条目再跑一次'
    } elseif ($DryRun) {
        Info ('--- 将要追加: ' + ($missing -join ', ') + ' ---')
        foreach ($name in $missing) { Info $want[$name] }
    } else {
        $toAdd = ''
        foreach ($name in $missing) { $toAdd += $want[$name] + "`n" }
        if (Test-Path $Cordis) {
            $bak = "$Cordis.bak-mech-" + (Get-Date -Format 'yyyyMMdd-HHmmss')
            Copy-Item $Cordis $bak -Force
            Ok "已备份 $bak"
        } else {
            New-Item -ItemType Directory -Force -Path $DshHome | Out-Null
        }
        $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
        $merged = ($existing.TrimEnd() + "`n" + $toAdd)
        [System.IO.File]::WriteAllText($Cordis, $merged, $utf8NoBom)
        Ok ('已写入 ' + $Cordis + '（新增: ' + ($missing -join ', ') + '）')
    }
}

# ---------- 竞赛模式：只留必需 MCP ----------
# 保留清单是**唯一真相源**：-DryRun 的提示与实际执行都从它派生。
# 以前这里有两份独立的硬编码清单（提示一份、调用一份），已经漂移过一次
# （DryRun 说 4 个、实际调 5 个），新增 MCP 时还会被静默关掉——现在改这里一处即可。

$CompetitionKeep = @(
    'document'        # 读赛题 PDF
    'sympy'           # 符号推导
    'sympy-physics'   # 单位/量纲/运动学/梁
    'mech-io'         # 跑脚本 / 裁图 / 图检 / 打包
    'mech-solver'     # 桁架 / 刚体平面运动 / 压杆稳定 / 能量法
    'mech-model'      # 建模决策卡：建模轴显式声明与矛盾检查
)
$CompetitionKeepLocal = @(
    'everything'      # 本地文件检索，不联网、4 个工具，路由表第一行依赖它
)
# 赛规明令禁止的联网工具：即便用户用 -KeepMCP 点名，也必须拒
$CompetitionForbid = @('browser', 'context7')

if ($Competition) {
    $py = Get-ToolPython
    if (-not $py) {
        Warn '竞赛模式需要 pyyaml，已跳过（用 -PythonExe 指定解释器）'
    } else {
        $keep = @($CompetitionKeep)
        if (-not $NoEverything) { $keep += $CompetitionKeepLocal }
        if ($KeepMCP) { $keep += $KeepMCP }
        $keep = @($keep | Where-Object { $_ -and $_.Trim() } | ForEach-Object { $_.Trim() } | Select-Object -Unique)

        $violated = @($keep | Where-Object { $CompetitionForbid -contains $_ })
        if ($violated.Count -gt 0) {
            Bad ('拒绝：这些是赛规禁止的联网工具，不能保留 —— ' + ($violated -join ', '))
            Info '  （-KeepMCP 只用于本地工具；browser/context7 在竞赛模式下恒定关闭）'
            exit 1
        }

        # 把「会关掉谁」逐条列出来，不让它静默发生
        $cfgPath = Join-Path $DshHome 'cordis.patch.yml'
        $allServers = @()
        if (Test-Path $cfgPath) {
            $allServers = @(Select-String -Path $cfgPath -Pattern 'serverName:\s*(\S+)\s*$' |
                Where-Object { $_.Line -notmatch '^\s*#' } |
                ForEach-Object { $_.Matches[0].Groups[1].Value } | Select-Object -Unique)
        }
        $willOff = @($allServers | Where-Object { $keep -notcontains $_ })
        $unknown = @($KeepMCP | Where-Object { $_ -and ($allServers -notcontains $_) })

        if ($unknown.Count -gt 0) {
            Warn ('-KeepMCP 里有配置中不存在的服务名：' + ($unknown -join ', '))
        }

        if ($DryRun) {
            Info ('  [DryRun] 保留 ' + $keep.Count + ' 个：' + ($keep -join ', '))
            Info ('  [DryRun] 置为 disabled ' + $willOff.Count + ' 个（含此前已关）：' + ($willOff -join ', '))
            Info '  [DryRun] browser / context7 为赛规禁止的联网工具，强制关闭，不可用 -KeepMCP 覆盖'
            if ($NoEverything) { Warn '  [DryRun] 已指定 -NoEverything：everything 也会被关，路由表第一行将失效' }
        } else {
            Step '5/5 竞赛模式：关掉无关 MCP（合规 + 省 token）'
            Ok ('  保留 ' + $keep.Count + ' 个：' + ($keep -join ', '))
            if ($willOff.Count -gt 0) { Warn ('  置为 disabled ' + $willOff.Count + ' 个（含此前已关）：' + ($willOff -join ', ')) }
            & $py (Join-Path $RepoRoot 'scripts\mcp_switch.py') '--only' ($keep -join ',')
        }
    }
}

# ---------- 插件安装检查 ----------
# 插件是 Host-only bundle，脚本装不了；但「装没装」必须能查出来，
# 否则最容易出现的情况是：以为装好了，赛时发现 9 个工具根本不存在。
$pluginName = 'dsh-mech-workbench'
$pluginWhere = $null
$candidates = @()
$candidates += (Join-Path $DshHome "profiles\node_modules\$pluginName")
$candidates += (Join-Path $DshHome "plugins\$pluginName")
# 实际安装位在各 profile 自己的 node_modules 下（如 profiles\desktop\node_modules）
$profilesDir = Join-Path $DshHome 'profiles'
if (Test-Path $profilesDir) {
    $candidates += Get-ChildItem $profilesDir -Directory -ErrorAction SilentlyContinue |
        ForEach-Object { Join-Path $_.FullName "node_modules\$pluginName" }
}
foreach ($p in $candidates) {
    if (Test-Path $p) { $pluginWhere = $p; break }
}
if (-not $pluginWhere -and (Test-Path $Cordis)) {
    $cfgText = Get-Content $Cordis -Raw -Encoding UTF8
    if ($cfgText -match [regex]::Escape($pluginName)) { $pluginWhere = 'cordis.patch.yml 里已登记' }
}
if ($pluginWhere) {
    Ok "插件 $pluginName 已安装：$pluginWhere"
    $pluginStatus = "  1) [已装] 插件 $pluginName —— $pluginWhere`n       重启 DSH 后可用 9 个工具"
} else {
    Warn "插件 $pluginName 未安装（9 个工具目前不可用）"
    $pluginStatus = @"
  1) [未装] 插件 $pluginName（9 个工具，需创造模式）
       设置 → Agent 预设 → 创造入口（cordis 预设）→ 新开会话
       plugin_manager → action: install_bundle
                    → target: $RepoRoot\plugins\dsh-mech-workbench
       装完重启 DSH。没装也能解题，但读题图/内力图/出图自检要退回 mech-io + sympy 手推。
"@
}

# ---------- 收尾清单 ----------
Write-Host ''
Write-Host '================ 还差这些（脚本管不了）================' -ForegroundColor Cyan
Write-Host $pluginStatus
Write-Host @"
  2) 赛前切竞赛模式（合规 + 省 token）
       pwsh -File setup.ps1 -Competition
       保留 document / sympy / sympy-physics / mech-io / mech-solver / mech-model + everything（本地检索）
       其余（video/image/tools/eac/rea…）自动 disabled；
       browser / context7 属联网工具，强制关闭且不可用 -KeepMCP 覆盖
       想多留几个本地工具：-KeepMCP image,video
       最省 token（连 everything 也关）：-NoEverything
       恢复：pwsh -File setup.ps1 -Restore

  3) 边界工具 mech-io（11 个）
       已随本脚本注册。自检：
       python $RepoRoot\mcp\mech-io\test\selftest.py

  3b) 建模决策卡 mech-model（1 个）
       已随本脚本注册。自检：
       python $RepoRoot\mcp\mech-model\test\selftest.py

  4) 可选：读题工具（来自另一个仓库）
       ai-agent-tools 的 document MCP：pdf_text / pdf_render
       注：mech-io 的 pdf_page_crop 能直接取 PDF 局部，已覆盖大部分读题需求

  5) 重启 DSH 生效

  6) 自检：问一句「现在有哪些 MCP 工具」

  7) 换机器前跑一遍预检（编码 / 语法 / JSON / 硬编码路径 / 真跑自检）
       python $RepoRoot\scripts\preflight.py
"@
Write-Host '======================================================' -ForegroundColor Cyan
if ($DryRun) { Write-Host "`n（DryRun：以上均未落盘）" -ForegroundColor Yellow }

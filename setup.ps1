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
    竞赛模式：只保留 document / sympy / sympy-physics / mech-io，
    其余 MCP（browser/context7/everything/video/image/tools/eac/rea/…）全部 disabled。
    既满足“赛时不得联网”的合规要求，也省 token（同分看 token）。
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
if ([string]::IsNullOrWhiteSpace($DshHome)) { $DshHome = Join-Path $env:USERPROFILE '.dsh' }
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
    if ($LASTEXITCODE -eq 0) { Ok '依赖安装完成' } else { Warn 'pip 返回非 0，检查上面的输出' }
    exit $LASTEXITCODE
}

Step '1/4 环境确认'
Info "仓库    : $RepoRoot"
Info "DSH_HOME: $DshHome"
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

    $existing = ''
    if (Test-Path $Cordis) { $existing = Get-Content $Cordis -Raw -Encoding UTF8 }

    # 锚定匹配：避免 sympy 命中 sympy-physics
    $want = [ordered]@{
        'sympy'         = $blkSympy
        'lean4'         = $blkLean
        'sympy-physics' = $blkPhys
        'mech-io'       = $blkIo
    }
    $missing = @()
    foreach ($name in $want.Keys) {
        $pat = '(?m)^\s*serverName:\s*' + [regex]::Escape($name) + '\s*$'
        if ($existing -notmatch $pat) { $missing += $name }
    }

    if ($missing.Count -eq 0) {
        Warn 'sympy / lean4 / sympy-physics / mech-io 都已在配置里，不重复添加'
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
if ($Competition) {
    $py = Get-ToolPython
    if (-not $py) {
        Warn '竞赛模式需要 pyyaml，已跳过（用 -PythonExe 指定解释器）'
    } elseif ($DryRun) {
        Info '  [DryRun] 将只保留 document / sympy / sympy-physics / mech-io'
        Info '  [DryRun] 其余一律 disabled（browser/context7 属赛规禁止的联网工具）'
    } else {
        Step '5/5 竞赛模式：关掉无关 MCP（合规 + 省 token）'
        & $py (Join-Path $RepoRoot 'scripts\mcp_switch.py') '--only' 'document,sympy,sympy-physics,mech-io'
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
       只保留 document / sympy / sympy-physics / mech-io，
       其余（browser/context7/everything/video/image/tools/eac/rea）自动 disabled
       恢复：pwsh -File setup.ps1 -Restore

  3) 边界工具 mech-io（11 个）
       已随本脚本注册。自检：
       python $RepoRoot\mcp\mech-io\test\selftest.py

  4) 可选：读题工具（来自另一个仓库）
       ai-agent-tools 的 document MCP：pdf_text / pdf_render
       注：mech-io 的 pdf_page_crop 能直接取 PDF 局部，已覆盖大部分读题需求

  5) 重启 DSH 生效

  6) 自检：问一句「现在有哪些 MCP 工具」
"@
Write-Host '======================================================' -ForegroundColor Cyan
if ($DryRun) { Write-Host "`n（DryRun：以上均未落盘）" -ForegroundColor Yellow }

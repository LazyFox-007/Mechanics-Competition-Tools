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
.EXAMPLE
    pwsh -File setup.ps1
.EXAMPLE
    pwsh -File setup.ps1 -DryRun
#>
[CmdletBinding()]
param(
    [string]$DshHome = '',
    [string]$PythonExe = '',
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

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

    $block = @"

# ---- 力学竞赛工具（mechanics-competition-tools / setup.ps1 生成）----
- insert:
    - id: mech-sympy
      name: '@deepseek-ai/dsh-mcp-client'
      config:
        serverName: sympy
        transport: stdio
        command: '$pyYaml'
        args:
          - '$repoPosix/mcp/sympy/server.py'
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

    $existing = ''
    if (Test-Path $Cordis) { $existing = Get-Content $Cordis -Raw -Encoding UTF8 }

    $hasSympy = $existing -match 'serverName:\s*sympy'
    $hasLean = $existing -match 'serverName:\s*lean4'

    if ($hasSympy -and $hasLean) {
        Warn '配置里已有 sympy 和 lean4（多半来自 ai-agent-tools 的 community），不重复添加'
        Info '  想用本仓库的副本，先手动删掉旧条目再跑一次'
    } elseif ($DryRun) {
        Info '--- 将要追加的配置 ---'
        Info $block
    } else {
        $toAdd = $block
        if ($hasSympy -or $hasLean) {
            $toAdd = ($block -split "`n" | Where-Object { $_ -notmatch 'serverName:\s*(sympy|lean4)' }) -join "`n"
            Warn '已有一个，跳过重复的那个（另一半仍会写入）'
        }
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
        Ok "已写入 $Cordis"
    }
}

# ---------- 收尾清单 ----------
Write-Host ''
Write-Host '================ 还差这些（脚本管不了）================' -ForegroundColor Cyan
Write-Host @"
  1) 插件 mech-workbench（9 个工具，需创造模式）
       设置 → Agent 预设 → 创造入口（cordis 预设）→ 新开会话
       plugin_manager → action: install_bundle
                    → target: $RepoRoot\plugins\dsh-mech-workbench

  2) 赛前关掉联网 MCP（违规项）
       在 $Cordis 里给 browser / context7 加 disabled: true

  3) 读题工具（可选，来自另一个仓库）
       ai-agent-tools 的 document MCP：pdf_text / pdf_render

  4) 重启 DSH 生效

  5) 自检：问一句「现在有哪些 MCP 工具」
"@
Write-Host '======================================================' -ForegroundColor Cyan
if ($DryRun) { Write-Host "`n（DryRun：以上均未落盘）" -ForegroundColor Yellow }

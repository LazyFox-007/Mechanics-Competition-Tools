<#
.SYNOPSIS
    应用已下载的 DSH 更新（专治安装器 MoveFileExW / Windows error 32）。

.DESCRIPTION
    electron-updater 的 NSIS 安装器先把旧安装目录改名成 "DeepSeek Harness.old-{GUID}"，
    再铺新文件。若 DSH 仍在运行（它自己 6 个进程 + 挂着的 MCP 子进程），改名会失败：
        MoveFileExW -> Windows error 32（另一个程序正在使用此文件）
    现场症状：点更新、转一圈、版本没变；更新器缓存里出现 directory-failure-*.log。

    本脚本按顺序做：体检 -> 结束 DSH 整棵进程树 -> 等目录解锁 -> 跑安装器 -> 复核版本。

.PARAMETER Apply
    真正执行。不加只体检，不动任何进程。

.PARAMETER Interactive
    用安装器图形界面（默认 /S 静默安装）。

.PARAMETER NoRelaunch
    装完不自动启动 DSH。

.PARAMETER TimeoutSec
    等待目录解锁的上限秒数，默认 60。

.EXAMPLE
    pwsh -File scripts\dsh_update.ps1
    pwsh -File scripts\dsh_update.ps1 -Apply
    pwsh -File scripts\dsh_update.ps1 -Apply -Interactive -NoRelaunch
#>
[CmdletBinding()]
param(
    [switch]$Apply,
    [switch]$Interactive,
    [switch]$NoRelaunch,
    [int]$TimeoutSec = 60
)

$ErrorActionPreference = 'Stop'

$Inst  = Join-Path $env:LOCALAPPDATA 'Programs\DeepSeek Harness'
$Cache = Join-Path $env:LOCALAPPDATA '@deepseek-aidsh-desktop-updater'
$Pend  = Join-Path $Cache 'pending'

function Get-DshVersion {
    $keys = @(
        'HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*',
        'HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*',
        'HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*'
    )
    $e = Get-ItemProperty $keys -ErrorAction SilentlyContinue |
         Where-Object { $_.DisplayName -match 'DeepSeek Harness' } |
         Select-Object -First 1
    if ($e) { return [string]$e.DisplayVersion }
    return $null
}

function Get-DshProcs {
    Get-CimInstance Win32_Process | Where-Object {
        $_.ExecutablePath -and $_.ExecutablePath.StartsWith($Inst, [StringComparison]::OrdinalIgnoreCase)
    }
}

function Get-Descendants {
    param([int]$Root)
    $all = Get-CimInstance Win32_Process | Select-Object ProcessId, ParentProcessId
    $out = New-Object System.Collections.Generic.List[int]
    $queue = New-Object System.Collections.Queue
    $queue.Enqueue($Root)
    while ($queue.Count -gt 0) {
        $cur = [int]$queue.Dequeue()
        foreach ($p in $all) {
            if ([int]$p.ParentProcessId -eq $cur -and [int]$p.ProcessId -ne $cur) {
                if (-not $out.Contains([int]$p.ProcessId)) {
                    $out.Add([int]$p.ProcessId)
                    $queue.Enqueue([int]$p.ProcessId)
                }
            }
        }
    }
    return $out
}

function Test-Unlocked {
    # 能独占打开这几个关键文件，说明安装目录没被任何进程占着
    $cand = @(
        (Join-Path $Inst 'DeepSeek Harness.exe'),
        (Join-Path $Inst 'resources\app.asar'),
        (Join-Path $Inst 'resources.pak')
    ) | Where-Object { Test-Path $_ }
    if (-not $cand) { return $false }
    foreach ($f in $cand) {
        try {
            $fs = [System.IO.File]::Open($f, [System.IO.FileMode]::Open,
                                         [System.IO.FileAccess]::ReadWrite,
                                         [System.IO.FileShare]::None)
            $fs.Close()
            $fs.Dispose()
        } catch {
            return $false
        }
    }
    return $true
}

# ───────────────────────── 体检 ─────────────────────────
Write-Host "==== DSH 更新器体检 ====" -ForegroundColor Cyan
Write-Host ("安装目录 : {0}   (存在={1})" -f $Inst, (Test-Path $Inst))

$verNow = Get-DshVersion
Write-Host ("当前版本 : {0}" -f $(if ($verNow) { $verNow } else { '未检出' }))

$pendExe = $null
if (Test-Path $Pend) {
    $pendExe = Get-ChildItem $Pend -Filter *.exe -ErrorAction SilentlyContinue |
               Sort-Object Length -Descending | Select-Object -First 1
}
if ($pendExe) {
    Write-Host ("待装包   : {0}" -f $pendExe.Name)
    Write-Host ("            {0:N0} 字节   下载于 {1:yyyy-MM-dd HH:mm:ss}" -f $pendExe.Length, $pendExe.LastWriteTime)
} else {
    Write-Host "待装包   : 无 —— 先在应用内点一次「检查更新」让它下载" -ForegroundColor Yellow
}

$info = Join-Path $Pend 'update-info.json'
if (Test-Path $info) {
    try { $j = Get-Content $info -Raw -Encoding UTF8 | ConvertFrom-Json
          Write-Host  ("           update-info 指向: {0}" -f $j.fileName)
          Write-Host  ("           需要管理员: {0}" -f $j.isAdminRightsRequired) } catch { }
}

$fails = Get-ChildItem (Join-Path $Cache 'installer-logs') -Filter 'directory-failure-*.log' -ErrorAction SilentlyContinue |
         Sort-Object LastWriteTime -Descending
if ($fails) {
    Write-Host ("`n历史失败 : {0} 次，最近一次 {1:yyyy-MM-dd HH:mm:ss}" -f @($fails).Count, $fails[0].LastWriteTime) -ForegroundColor Yellow
    $lines = Get-Content $fails[0].FullName -Encoding UTF8 | Where-Object { $_ -match 'Windows error|Operation|Source' }
    foreach ($l in $lines) { Write-Host ("           " + $l.Trim()) }
}

$procs = @(Get-DshProcs)
Write-Host ("`n占用进程 : {0} 个" -f $procs.Count) -ForegroundColor Cyan
if ($procs.Count -gt 0) {
    $procs | Select-Object ProcessId, ParentProcessId, Name |
        Format-Table -AutoSize | Out-String | Write-Host
}

$unlocked = Test-Unlocked
if ($unlocked) {
    Write-Host "目录状态 : 可独占（没人占用）" -ForegroundColor Green
} else {
    Write-Host "目录状态 : 被占用 —— 这就是 error 32 的来源" -ForegroundColor Yellow
}

if (-not $Apply) {
    Write-Host "`n（体检模式，未做任何改动）" -ForegroundColor DarkGray
    if (-not $pendExe) { Write-Host "缺待装包，先让应用下载。" }
    elseif ($unlocked) { Write-Host "现在就可以直接跑安装器：`n  `"$($pendExe.FullName)`"" }
    else { Write-Host "执行更新：`n  pwsh -File `"$PSCommandPath`" -Apply" }
    return
}

# ───────────────────────── 执行 ─────────────────────────
if (-not $pendExe) { throw "没有待装包，先在应用内让它下载，再运行 -Apply" }

Write-Host "`n==== 1. 结束 DSH 进程树 ====" -ForegroundColor Cyan
$roots = @($procs | ForEach-Object { [int]$_.ProcessId })
$victims = New-Object System.Collections.Generic.List[int]
foreach ($r in $roots) {
    if (-not $victims.Contains($r)) { $victims.Add($r) }
    foreach ($d in (Get-Descendants -Root $r)) {
        if (-not $victims.Contains($d)) { $victims.Add($d) }
    }
}
Write-Host ("将结束 {0} 个进程（DSH 本体 + 它派生的 MCP 子进程）" -f $victims.Count)
foreach ($procId in $victims) {
    try { Stop-Process -Id $procId -Force -ErrorAction Stop } catch { }
}
Start-Sleep -Milliseconds 800

Write-Host "`n==== 2. 等目录解锁 ====" -ForegroundColor Cyan
$ok = $false
$deadline = (Get-Date).AddSeconds($TimeoutSec)
while ((Get-Date) -lt $deadline) {
    if (Test-Unlocked) { $ok = $true; break }
    Start-Sleep -Milliseconds 500
}
if (-not $ok) {
    Write-Host ("等了 {0} 秒目录仍被占用。" -f $TimeoutSec) -ForegroundColor Red
    Write-Host "建议：注销一次 Windows 再登录（比重启快），然后重跑本脚本。" -ForegroundColor Yellow
    throw "安装目录仍被锁定"
}
Write-Host "目录已解锁。" -ForegroundColor Green

Write-Host "`n==== 3. 运行安装器 ====" -ForegroundColor Cyan
if ($Interactive) {
    Write-Host "图形界面模式，按提示完成。"
    $sp = @{ FilePath = $pendExe.FullName; PassThru = $true; Wait = $true }
} else {
    Write-Host "静默模式（/S）。"
    $sp = @{ FilePath = $pendExe.FullName; ArgumentList = '/S'; PassThru = $true; Wait = $true }
}
try {
    $p = Start-Process @sp
    Write-Host ("安装器退出码: {0}" -f $p.ExitCode)
} catch {
    Write-Host ("启动安装器失败: " + $_.Exception.Message) -ForegroundColor Red
    Write-Host ("请手动双击: " + $pendExe.FullName) -ForegroundColor Yellow
    throw
}

Write-Host "`n==== 4. 复核 ====" -ForegroundColor Cyan
$verNew = Get-DshVersion
Write-Host ("升级前 : {0}" -f $(if ($verNow) { $verNow } else { '未检出' }))
Write-Host ("升级后 : {0}" -f $(if ($verNew) { $verNew } else { '未检出' }))

if ($verNew -and $verNew -ne $verNow) {
    Write-Host "`n升级成功。" -ForegroundColor Green
    $left = Get-ChildItem (Split-Path $Inst -Parent) -Directory -Filter 'DeepSeek Harness.old-*' -ErrorAction SilentlyContinue
    if ($left) { Write-Host ("遗留旧目录（确认新版能跑后可删）: {0}" -f ($left.Name -join ', ')) }
    Write-Host "`n接下来：" -ForegroundColor Cyan
    Write-Host "  1) cd <仓库>; python scripts\preflight.py      # 第 10 节会 WARN（登记的仍是旧版本）"
    Write-Host "  2) python scripts\verify_setup.py             # 最关键：7 个 MCP 是否仍被接受"
    Write-Host "  3) 把 dsh/TESTED_DSH.json 的 tested 改成 $verNew，再跑一次 preflight"
    if (-not $NoRelaunch) {
        Start-Process (Join-Path $Inst 'DeepSeek Harness.exe')
        Write-Host "`n已重新启动 DSH。" -ForegroundColor Green
    }
} else {
    Write-Host "`n版本没有变化 —— 静默安装可能不被支持。" -ForegroundColor Yellow
    Write-Host ("请手动双击安装器再试一次：`n  " + $pendExe.FullName)
    if (-not $NoRelaunch -and (Test-Path (Join-Path $Inst 'DeepSeek Harness.exe'))) {
        Start-Process (Join-Path $Inst 'DeepSeek Harness.exe')
    }
}

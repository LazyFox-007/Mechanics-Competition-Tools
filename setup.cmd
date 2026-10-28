@echo off
chcp 65001 >nul
setlocal
set HERE=%~dp0

echo ============================================================
echo   mechanics-competition-tools  -  one-click setup
echo ============================================================
echo.
echo   1  Competition mode  (keep only document/sympy/sympy-physics/mech-io)
echo   2  Install / update only  (do not change MCP switches)
echo   3  Verify            (run AFTER restarting DSH)
echo   4  Rollback MCP config to last backup
echo   5  Install Python deps (pip)
echo.
set /p choice=Select [1-5, Enter=1]: 
if "%choice%"=="" set choice=1

if "%choice%"=="1" powershell -NoProfile -ExecutionPolicy Bypass -File "%HERE%setup.ps1" -Competition
if "%choice%"=="2" powershell -NoProfile -ExecutionPolicy Bypass -File "%HERE%setup.ps1"
if "%choice%"=="3" powershell -NoProfile -ExecutionPolicy Bypass -File "%HERE%setup.ps1" -Verify
if "%choice%"=="4" powershell -NoProfile -ExecutionPolicy Bypass -File "%HERE%setup.ps1" -Restore
if "%choice%"=="5" powershell -NoProfile -ExecutionPolicy Bypass -File "%HERE%setup.ps1" -InstallDeps

echo.
echo ------------------------------------------------------------
echo  If you chose 1 or 2: restart DSH, then run this again and pick 3.
echo ------------------------------------------------------------
pause

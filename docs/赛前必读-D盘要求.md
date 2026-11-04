# 赛前必读：工具与知识库必须装在 D 盘

> 依据：组委会环境核验要求（补充通知）。**C 盘上的任何工具/知识库都不计入合规部署。**
> 本仓库的 `setup.ps1` 已内置检查：在 `Step 1/4 环境确认` 会逐条打印路径，凡是在 `C:` 的都会红字报警。

## 一、必须落在 D 盘的三样东西

| 项 | 合规位置（示例） | 当前默认 |
|---|---|---|
| 本仓库（工具 + 技能 + wheel） | `D:\mechanics-competition-tools` | ✅ 已在 D 盘 |
| DSH 配置与技能安装目录 `DSH_HOME` | `D:\dsh` | ⚠️ 默认 `C:\Users\<你>\.dsh` |
| Python 解释器 | `D:\anaconda\python.exe` | ✅ 已在 D 盘 |

## 二、自查一条命令

```powershell
pwsh -File setup.ps1 -Verify
```

看 `Step 1/4` 那三行：仓库 / DSH_HOME / Python，**全部以 `D:` 开头才算合规**；
文件末尾 `[OK] D 盘要求：仓库 / DSH_HOME / Python 均在 D 盘` 是最终判据。

## 三、把 DSH_HOME 迁到 D 盘

1. 关闭 DSH。
2. 复制（不是移动，先留备份）：`robocopy "%USERPROFILE%\.dsh" "D:\dsh" /E`
3. 设环境变量（用户级，永久）：
   ```powershell
   [Environment]::SetEnvironmentVariable('DSH_HOME','D:\dsh','User')
   ```
4. 重开终端，跑 `setup.ps1 -Competition -DshHome D:\dsh`，再 `-Verify` 确认。
5. 确认无误后再删 `%USERPROFILE%\.dsh`（**注意先备份 `sessions/` 与 `attachments/`**）。

## 四、为什么这条要求会卡人

- DSH 默认把技能装到 `~/.dsh/skills`，`~` 在 C 盘 → 技能等于没装到合规位置。
- `pip install` 默认装到 `D:\anaconda`（本项目 Python 在 D 盘，✅ 天然合规）；
  但**如果误用系统 Python（C 盘）**，包会落到 `C:\Users\...\AppData\Roaming\Python`，直接不合规。
- 所以 `setup.ps1 -InstallDeps` 一定要用 `-PythonExe D:\anaconda\python.exe` 显式指定。

## 五、交卷前打勾

```
[ ] 仓库在 D 盘
[ ] DSH_HOME 在 D 盘（技能实际安装在 D 盘）
[ ] Python 解释器在 D 盘
[ ] vendor/wheels 里的 wheel 已安装（离线可用，不联网）
[ ] setup.ps1 -Verify 输出 "D 盘要求 ... 均在 D 盘"
```

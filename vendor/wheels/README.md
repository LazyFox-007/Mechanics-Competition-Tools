# vendor/wheels —— 离线安装包

赛规禁止赛时联网（规则三.1），所有 pip 依赖必须在赛前落到本地并随仓库分发。

| wheel | 版本 | 大小 | 许可 | 用途 |
|---|---|---|---|---|
| pynitefea-3.2.1-py3-none-any.whl | 3.2.1 | 0.2 MB | MIT | 3D 刚架/桁架/连续梁有限元（校核空间刚架题） |
| prettytable-3.18.0-py3-none-any.whl | 3.18.0 | 0.04 MB | BSD-3 | PyNite 的依赖 |

## 已知冲突（重要）

`PyNiteFEA` 的 METADATA 声明 `numpy>=2.4.0`，但本机 `matplotlib 3.9.2` 编译于 numpy 1.x，
升到 numpy 2 会 `ImportError: numpy.core.multiarray failed to import`。
实测 PyNite 3.2.1 在 `numpy 1.26.4` 下功能正常（第 10 题 3D 刚架校核通过），
所以安装脚本用 `--no-deps` 装 wheel，并强制回锁 `numpy==1.26.4`、`scipy==1.11.4`。

安装命令（setup.ps1 -InstallDeps 已包含）：

```
python -m pip install --no-deps vendor/wheels/pynitefea-3.2.1-py3-none-any.whl
python -m pip install numpy==1.26.4 scipy==1.11.4
```

## 复现性

wheel 自带哈希记录在 `wheel-sha256.txt`，可用 `certutil -hashfile <wheel> SHA256` 核对。
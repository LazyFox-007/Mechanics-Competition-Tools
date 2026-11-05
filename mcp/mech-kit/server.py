#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mech-kit MCP —— 把 dsh-mech-workbench 的 Python 脚本直接拿来用，**不经插件层**。

为什么不走插件：
  那 9 个工具的本体就是 `plugins/dsh-mech-workbench/scripts/*.py` 里的 8 个独立 CLI，
  全部 `--spec-json` 进、JSON 出。插件那层只是（a）注册成宿主工具（b）做无损 JSON 守卫。
  注册要创造模式 + `install_bundle` + 重启，换机器还得再来一遍；
  包一层 MCP 就能进仓库、跟着 git 走、用 setup.ps1 注册。

只包**离线**的部分（4 个 + 自检）：
  preprocess  17 种图像预处理（zoom / probe / split / deskew / binarize …）—— 纯 Pillow
  analyze     静定反力、N/Q/M/T、截面几何、应力、8 项独立校核、**静定判别** —— 纯 numpy
  diagram     力学标准图（轴力/剪力/弯矩/扭矩/应力分布/莫尔圆/挠曲线）—— matplotlib 或 Pillow
  annotate    在学生原图上标注（框/圈/箭头/文字/局部放大）—— 纯 Pillow

**不包**（要联网，赛规禁用）：
  second_reader（mech_read_problem 的二次转写）、viz_check、render_math
  —— 它们走 siliconflow / 智谱 / DeepSeek / 商汤 / Gemini 的云端 API。

设计铁律：
  - 零第三方依赖的**协议层**；重活交给脚本自己（它们要 Pillow/numpy/matplotlib）
  - spec 走临时文件（UTF-8），不走 argv —— Windows 上中文 argv 编码不稳
  - 脚本返回什么就回什么，不二次加工、不"顺手修一下"
  - stdout 只走协议
"""

import json
import os
import subprocess
import sys
import tempfile
import traceback

# ── stdout 保护 ────────────────────────────────────────────────
_real_stdout_fd = os.dup(1)
os.dup2(2, 1)
_OUT = os.fdopen(_real_stdout_fd, "w", encoding="utf-8", buffering=1)

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8")

SERVER_NAME = "mech-kit"
VERSION = "0.1.0"

# repo/mcp/mech-kit/server.py -> repo
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPTS = os.path.join(REPO, "plugins", "dsh-mech-workbench", "scripts")

OPS = {
    "preprocess": "preprocess.py",
    "analyze": "analyze.py",
    "diagram": "figure.py",
    "annotate": "annotate.py",
}

TOOLS = [
    {
        "name": "mech_kit",
        "description": (
            "调用仓库内置的 dsh-mech-workbench 脚本（不经插件层、全离线）。"
            "op=preprocess 图像预处理17算子(zoom/probe/split 等)；"
            "analyze 静定反力+N/Q/M/T+截面几何+8项独立校核+静定判别；"
            "diagram 力学标准图；annotate 在学生原图上标注；info 自检。"
            "spec 传脚本原样的 JSON 对象。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "op": {"type": "string", "enum": ["preprocess", "analyze", "diagram", "annotate", "info"]},
                "spec": {"type": "object", "description": "脚本入参，原样透传"},
            },
            "required": ["op"],
        },
    },
]


def _missing_deps(script):
    """粗略检查脚本能不能跑：解释器 + 关键库。"""
    import importlib
    need = {
        "preprocess.py": ["PIL", "numpy"],
        "analyze.py": ["numpy"],
        "figure.py": ["PIL", "numpy"],
        "annotate.py": ["PIL", "numpy"],
    }.get(script, [])
    miss = []
    for m in need:
        try:
            importlib.import_module(m)
        except Exception:  # noqa: BLE001
            miss.append(m)
    return miss


def t_info(_spec):
    rows = []
    for op, script in OPS.items():
        path = os.path.join(SCRIPTS, script)
        exists = os.path.isfile(path)
        rows.append({
            "op": op, "script": script, "exists": exists,
            "bytes": os.path.getsize(path) if exists else None,
            "missing_deps": _missing_deps(script) if exists else ["(script missing)"],
        })
    return {"ok": all(r["exists"] for r in rows),
            "server": SERVER_NAME, "version": VERSION,
            "python": sys.version.split()[0], "executable": sys.executable,
            "scripts_dir": SCRIPTS,
            "ops": rows,
            "note": "second_reader / viz_check / render_math 走云端 API，赛规禁用，故未包。"
                    "缺 matplotlib 时 diagram 会降级到 Pillow 后端。"}


def t_call(op, spec):
    if op == "info":
        return t_info(spec)
    script = OPS.get(op)
    if script is None:
        return {"ok": False, "error": "未知 op: %s" % op, "ops": list(OPS) + ["info"]}
    path = os.path.join(SCRIPTS, script)
    if not os.path.isfile(path):
        return {"ok": False, "error": "脚本不存在: %s" % path,
                "hint": "仓库根是否为 %s ？plugins/dsh-mech-workbench/scripts 应在其中" % REPO}
    if spec is None:
        spec = {}
    if not isinstance(spec, dict):
        return {"ok": False, "error": "spec 必须是 JSON 对象"}

    fd, tmp = tempfile.mkstemp(suffix=".json", prefix="mechkit_")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(spec, f, ensure_ascii=False)
        p = subprocess.run([sys.executable, path, "--spec", tmp],
                           capture_output=True, timeout=240)
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "脚本执行超时（240 s）", "op": op}
    finally:
        try:
            os.remove(tmp)
        except OSError:
            pass

    out = p.stdout.decode("utf-8", "replace").strip()
    err = p.stderr.decode("utf-8", "replace").strip()
    if not out:
        return {"ok": False, "op": op, "exit": p.returncode,
                "error": "脚本无 stdout 输出", "stderr_tail": err[-1200:]}
    try:
        res = json.loads(out)
    except Exception:  # noqa: BLE001
        return {"ok": False, "op": op, "exit": p.returncode,
                "error": "stdout 不是合法 JSON（已原样返回尾部）",
                "raw_tail": out[-1200:], "stderr_tail": err[-600:]}
    if not isinstance(res, dict):
        res = {"value": res}
    res.setdefault("ok", p.returncode == 0)
    res["_op"] = op
    res["_exit"] = p.returncode
    if err:
        res["_stderr_tail"] = err[-600:]
    return res


def dispatch(args):
    args = args or {}
    try:
        return t_call(args.get("op") or "info", args.get("spec"))
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "error": "%s: %s" % (type(e).__name__, e),
                "trace": traceback.format_exc(limit=3)}


def send(payload):
    _OUT.write(json.dumps(payload, ensure_ascii=False) + "\n")
    _OUT.flush()


def main():
    sys.stderr.write("[%s] 启动，scripts=%s\n" % (SERVER_NAME, SCRIPTS))
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except Exception as e:  # noqa: BLE001
            sys.stderr.write("[%s] 非法 JSON: %s\n" % (SERVER_NAME, e))
            continue
        mid, method = msg.get("id"), msg.get("method")
        if method == "initialize":
            send({"jsonrpc": "2.0", "id": mid, "result": {
                "protocolVersion": msg.get("params", {}).get("protocolVersion", "2024-11-05"),
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": SERVER_NAME, "version": VERSION}}})
        elif method == "notifications/initialized":
            continue
        elif method == "tools/list":
            send({"jsonrpc": "2.0", "id": mid, "result": {"tools": TOOLS}})
        elif method == "tools/call":
            p = msg.get("params") or {}
            res = dispatch(p.get("arguments"))
            send({"jsonrpc": "2.0", "id": mid, "result": {
                "content": [{"type": "text", "text": json.dumps(res, ensure_ascii=False, indent=1)}],
                "isError": not res.get("ok", False)}})
        elif mid is not None:
            send({"jsonrpc": "2.0", "id": mid,
                  "error": {"code": -32601, "message": "不支持的方法: %s" % method}})


if __name__ == "__main__":
    main()

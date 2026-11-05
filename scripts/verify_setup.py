# -*- coding: utf-8 -*-
"""
verify_setup.py —— 重启 DSH 之后，真正验一遍工具链对不对。

不只看配置：把每个 MCP 服务**真的拉起来**，走一遍 initialize + tools/list，
报出工具数量和耗时。配置写错、解释器路径失效、依赖没装，都会在这一步现形。

另查：技能目录、插件安装位、Python 依赖。

用法：
  python scripts/verify_setup.py             # 只验竞赛必需的 4 个
  python scripts/verify_setup.py --all       # 验所有 enabled 的
  python scripts/verify_setup.py --json      # 机器可读
"""
import argparse
import io
import json
import os
import queue
import subprocess
import sys
import threading
import time

CFG = os.path.join(os.path.expanduser("~"), ".dsh", "cordis.patch.yml")
DSH = os.path.join(os.path.expanduser("~"), ".dsh")
COMPETITION = ["document", "sympy", "sympy-physics", "mech-io", "mech-solver",
               "mech-model", "mech-kit"]


def load_entries():
    import yaml
    with io.open(CFG, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    out = []
    for blk in data or []:
        for row in (blk or {}).get("insert", []) or []:
            cfg = row.get("config") or {}
            out.append({
                "id": row.get("id"),
                "name": cfg.get("serverName") or "?",
                "command": cfg.get("command"),
                "args": cfg.get("args") or [],
                "disabled": bool(row.get("disabled")),
            })
    return out


def _readline_with_timeout(proc, timeout):
    q = queue.Queue()

    def reader():
        try:
            q.put(proc.stdout.readline())
        except Exception:  # noqa: BLE001
            q.put(b"")

    t = threading.Thread(target=reader, daemon=True)
    t.start()
    try:
        return q.get(timeout=timeout)
    except queue.Empty:
        return None


def probe(entry, timeout=25):
    cmd = [entry["command"]] + [str(a) for a in entry["args"]]
    t0 = time.time()
    try:
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL, cwd=os.path.expanduser("~"))
    except Exception as e:  # noqa: BLE001
        return {"server": entry["name"], "ok": False, "error": f"启动失败: {e}", "ms": 0}

    def send(obj):
        proc.stdin.write((json.dumps(obj) + "\n").encode())
        proc.stdin.flush()

    try:
        send({"jsonrpc": "2.0", "id": 1, "method": "initialize",
              "params": {"protocolVersion": "2024-11-05"}})
        line = _readline_with_timeout(proc, timeout)
        if not line:
            raise RuntimeError("initialize 无响应")

        # MCP 握手：initialize 之后必须先发 notifications/initialized，
        # 否则有的实现（如 community launcher 代理）不会响应 tools/list
        send({"jsonrpc": "2.0", "method": "notifications/initialized"})

        send({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
        line = _readline_with_timeout(proc, timeout)
        if not line:
            raise RuntimeError("tools/list 无响应")
        tools = json.loads(line.decode("utf-8", "replace")).get("result", {}).get("tools", [])
        return {"server": entry["name"], "ok": True, "tools": len(tools),
                "names": [t.get("name") for t in tools][:3], "ms": int((time.time() - t0) * 1000)}
    except Exception as e:  # noqa: BLE001
        return {"server": entry["name"], "ok": False, "error": str(e),
                "ms": int((time.time() - t0) * 1000)}
    finally:
        try:
            proc.kill()
        except Exception:  # noqa: BLE001
            pass


def check_env():
    rows = []
    skills = os.path.join(DSH, "skills")
    for name in ("mechanics-map", "mechanics-zh", "undergrad-physics-skill", "math-skill"):
        p = os.path.join(skills, name)
        rows.append({"item": f"技能 {name}", "ok": os.path.isdir(p), "where": p if os.path.isdir(p) else "-"})

    plug = None
    prof = os.path.join(DSH, "profiles")
    if os.path.isdir(prof):
        for d in os.listdir(prof):
            cand = os.path.join(prof, d, "node_modules", "dsh-mech-workbench")
            if os.path.isdir(cand):
                plug = cand
                break
    rows.append({"item": "插件 dsh-mech-workbench", "ok": True, "optional": True,
                 "where": plug or "未装（可选；离线能力已由 mcp/mech-kit 覆盖）"})

    for mod in ("sympy", "numpy", "matplotlib", "PIL", "fitz", "Pynite"):
        try:
            m = __import__(mod)
            ver = getattr(m, "__version__", "")
            rows.append({"item": f"依赖 {mod}", "ok": True,
                         "where": f"import ok {ver}".strip()})
        except Exception:  # noqa: BLE001
            rows.append({"item": f"依赖 {mod}", "ok": False, "where": "缺"})

    # 冲突自检：PyNite 声明 numpy>=2.4，但 matplotlib<3.10 编译于 numpy 1.x，
    # numpy 2 会让 matplotlib 直接 ImportError。这里显式比对两者能否共存。
    try:
        import numpy
        import matplotlib  # noqa: F401
        major = int(str(numpy.__version__).split(".")[0])
        ok = major == 1
        rows.append({"item": "冲突 numpy(1.x)+matplotlib", "ok": ok,
                     "where": f"numpy {numpy.__version__}" + ("" if ok else " → 需回锁 1.26.4")})
    except Exception as e:  # noqa: BLE001
        rows.append({"item": "冲突 numpy(1.x)+matplotlib", "ok": False, "where": str(e)[:60]})
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    entries = load_entries()
    want = [e for e in entries if not e["disabled"] and (a.all or e["name"] in COMPETITION)]
    skipped = [e["name"] for e in entries if e["disabled"]]

    results = []
    for e in want:
        r = probe(e)
        results.append(r)
        if not a.json:
            tag = "OK  " if r["ok"] else "FAIL"
            extra = f"{r.get('tools')} 工具" if r["ok"] else r.get("error", "")
            print(f"  [{tag}] {r['server']:16} {extra}  ({r['ms']} ms)")

    env = check_env()
    if not a.json:
        print("\n  —— 环境 ——")
        for row in env:
            if row.get("optional"):
                tag = "SKIP" if "未装" in str(row["where"]) else "OK  "
            else:
                tag = "OK  " if row["ok"] else "FAIL"
            print(f"  [{tag}] {row['item']:26} {row['where']}")

    # 可选项（插件）不计入总体结论：它的离线能力已由 mcp/mech-kit 覆盖，
    # 剩下的 second_reader / viz_check / render_math 走云端 API，赛规禁用。
    ok = all(r["ok"] for r in results) and all(
        row["ok"] for row in env
        if not row["item"].startswith("依赖 fitz") and not row.get("optional"))
    if a.json:
        print(json.dumps({"servers": results, "env": env, "skipped": skipped,
                          "ok": ok}, ensure_ascii=False, indent=1))
    else:
        print(f"\n  结论：{'全部就绪' if ok else '有失败项，见上'}"
              + (f"（已禁用：{', '.join(skipped)}）" if skipped else ""))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

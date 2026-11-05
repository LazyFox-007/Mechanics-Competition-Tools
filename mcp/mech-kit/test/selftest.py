# -*- coding: utf-8 -*-
"""mech-kit 自检：起真进程走 MCP 协议，验 info / preprocess / analyze。

不依赖网络、不依赖视觉模型；只用仓库自带的脚本与一个临时 PNG。
"""
import json
import os
import subprocess
import sys
import tempfile

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
SERVER = os.path.join(os.path.dirname(HERE), "server.py")
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
PY = sys.executable

PASS, FAIL = 0, 0


def t(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("  PASS  %s" % name)
    else:
        FAIL += 1
        print("  FAIL  %s   %s" % (name, detail))


# ── 造一张测试图（避免依赖外部素材）──
tmpdir = tempfile.mkdtemp(prefix="mechkit_test_")
src = os.path.join(tmpdir, "page.png")
try:
    from PIL import Image, ImageDraw
    im = Image.new("RGB", (800, 1000), "white")
    d = ImageDraw.Draw(im)
    d.rectangle([300, 600, 500, 760], outline="black", width=3)
    d.ellipse([392, 740, 408, 756], outline="black", width=2)   # 端部空心圆（铰支标志）
    im.save(src)
    t("生成测试图", os.path.isfile(src))
except Exception as e:  # noqa: BLE001
    t("生成测试图", False, e)
    src = None

reqs = [
    {"jsonrpc": "2.0", "id": 1, "method": "initialize",
     "params": {"protocolVersion": "2024-11-05", "capabilities": {},
                "clientInfo": {"name": "selftest", "version": "0"}}},
    {"jsonrpc": "2.0", "method": "notifications/initialized"},
    {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
    {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
     "params": {"name": "mech_kit", "arguments": {"op": "info"}}},
]
if src:
    reqs.append({"jsonrpc": "2.0", "id": 4, "method": "tools/call",
                 "params": {"name": "mech_kit", "arguments": {
                     "op": "preprocess",
                     "spec": {"src": src, "out": os.path.join(tmpdir, "zoomed.png"),
                              "ops": [{"op": "probe"},
                                      {"op": "zoom", "box": [0.3, 0.55, 0.7, 0.8], "factor": 3}]}}}})
reqs.append({"jsonrpc": "2.0", "id": 5, "method": "tools/call",
             "params": {"name": "mech_kit", "arguments": {
                 "op": "analyze",
                 "spec": {"kind": "beam", "length": 4.0,
                          "supports": [{"x": 0.0, "type": "pin"}, {"x": 4.0, "type": "roller"}],
                          "loads": [{"type": "point_force", "x": 2.0, "value": -10.0,
                                     "dir": "transverse"}],
                          "section": {"shape": "rect", "params": {"b": 0.1, "h": 0.2},
                                      "E": 200000.0},
                          "stations": [0, 1, 2, 3, 4]}}}})

payload = "\n".join(json.dumps(r, ensure_ascii=False) for r in reqs) + "\n"
p = subprocess.run([PY, SERVER], input=payload.encode("utf-8"),
                   capture_output=True, timeout=300, cwd=os.path.dirname(SERVER))
out = p.stdout.decode("utf-8", "replace")
err = p.stderr.decode("utf-8", "replace")

print("\n--- 协议 ---")
ok = {"init": False, "tools": 0, "info": False, "pre": False, "ana": False}
for line in out.splitlines():
    if not line.strip():
        continue
    m = json.loads(line)
    rid, res = m.get("id"), m.get("result") or {}
    if rid == 1:
        si = res.get("serverInfo", {})
        print("  initialize -> %s %s" % (si.get("name"), si.get("version")))
        ok["init"] = si.get("name") == "mech-kit"
    elif rid == 2:
        tools = res.get("tools", [])
        ok["tools"] = len(tools)
        for tl in tools:
            print("  tools/list -> %s | desc %d 字符" % (tl["name"], len(tl["description"])))
    elif rid in (3, 4, 5):
        body = json.loads(res["content"][0]["text"])
        if rid == 3:
            print("  info        ok=%s  python=%s" % (body.get("ok"), body.get("python")))
            for r in body.get("ops", []):
                print("     %-11s exists=%-5s deps=%s" % (r["op"], r["exists"], r["missing_deps"]))
            ok["info"] = body.get("ok") is True and all(r["exists"] for r in body.get("ops", []))
        elif rid == 4:
            n_ops = len(body.get("outputs") or [])
            print("  preprocess  ok=%s  outputs=%d" % (body.get("ok"), n_ops))
            ok["pre"] = body.get("ok") is True and n_ops >= 1
        elif rid == 5:
            ext = body.get("extrema") or {}
            checks = body.get("checks") or []
            n_pass = sum(1 for c in checks if c.get("pass"))
            print("  analyze     ok=%s determinate=%s  M_max=%.4g @x=%.3g  校核 %d/%d"
                  % (body.get("ok"), body.get("determinate"),
                     (ext.get("M") or {}).get("abs_max", float("nan")),
                     (ext.get("M") or {}).get("abs_max_x", float("nan")),
                     n_pass, len(checks)))
            ok["ana"] = (body.get("ok") is True and body.get("determinate") is True
                         and n_pass == len(checks) and len(checks) >= 8
                         and abs((ext.get("M") or {}).get("abs_max", 0) - 10.0) < 1e-6)
            t("analyze 8 项校核全过", n_pass == len(checks) and len(checks) >= 8, checks)
            t("analyze M_max = 10 kN·m", abs((ext.get("M") or {}).get("abs_max", 0) - 10.0) < 1e-6, ext)

print("\n--- 断言 ---")
t("initialize 返回 mech-kit", ok["init"])
t("只暴露 1 个工具", ok["tools"] == 1, ok["tools"])
t("info 自检通过、4 个脚本齐", ok["info"])
t("preprocess zoom/probe 出图", ok["pre"] if src else True)
t("analyze 静定且结果正确", ok["ana"])
t("stderr 有启动行", "[mech-kit]" in err, err[:120])

# 清理
try:
    import shutil
    shutil.rmtree(tmpdir, ignore_errors=True)
except Exception:  # noqa: BLE001
    pass

print("\n" + "=" * 46)
print("PASS %d / FAIL %d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)

# -*- coding: utf-8 -*-
"""MCP 握手自检：真起一个进程，走 initialize → tools/list → tools/call"""
import json
import os
import subprocess
import sys

# 换环境时控制台可能是 GBK，中文输出会 UnicodeEncodeError
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
SERVER = os.path.join(os.path.dirname(HERE), "server.py")
PY = sys.executable

# 期望的卡片数从 cards.json 读，避免加卡后这里写死的数字漂移
with open(os.path.join(os.path.dirname(HERE), "cards.json"), encoding="utf-8") as _f:
    N_EXPECT = len(json.load(_f)["cards"])

reqs = [
    {"jsonrpc": "2.0", "id": 1, "method": "initialize",
     "params": {"protocolVersion": "2024-11-05",
                "capabilities": {}, "clientInfo": {"name": "selftest", "version": "0"}}},
    {"jsonrpc": "2.0", "method": "notifications/initialized"},
    {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
    {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
     "params": {"name": "model_card", "arguments": {"action": "index"}}},
    {"jsonrpc": "2.0", "id": 4, "method": "tools/call",
     "params": {"name": "model_card",
                "arguments": {"action": "probe", "text": "锥面车轮 轮对 蠕滑 蛇行"}}},
]
payload = "\n".join(json.dumps(r, ensure_ascii=False) for r in reqs) + "\n"

p = subprocess.run([PY, SERVER], input=payload.encode("utf-8"),
                   capture_output=True, timeout=60, cwd=os.path.dirname(SERVER))
out = p.stdout.decode("utf-8", "replace")
err = p.stderr.decode("utf-8", "replace")

print("exit=%d  stdout行数=%d" % (p.returncode, len([l for l in out.splitlines() if l.strip()])))
print("--- stderr ---"); print(err.strip())
print("--- stdout ---")
ok = {"init": False, "tools": 0, "call": False, "probe": False}
for line in out.splitlines():
    if not line.strip():
        continue
    m = json.loads(line)
    rid, res = m.get("id"), m.get("result") or {}
    if rid == 1:
        si = res.get("serverInfo", {})
        print("  initialize -> %s %s (protocol %s)" % (si.get("name"), si.get("version"), res.get("protocolVersion")))
        ok["init"] = si.get("name") == "mech-model"
    elif rid == 2:
        tools = res.get("tools", [])
        ok["tools"] = len(tools)
        for t in tools:
            print("  tools/list -> %s | desc %d 字符 | schema keys=%s"
                  % (t["name"], len(t["description"]), list(t["inputSchema"].get("properties", {}).keys())))
    elif rid == 3:
        body = json.loads(res["content"][0]["text"])
        print("  call index -> ok=%s, %d 张卡（期望 %d）" % (body["ok"], len(body["cards"]), N_EXPECT))
        ok["call"] = body["ok"] and len(body["cards"]) == N_EXPECT
    elif rid == 4:
        body = json.loads(res["content"][0]["text"])
        top = body["candidates"][0]["id"] if body.get("candidates") else None
        print("  call probe -> 首选 %s" % top)
        ok["probe"] = top == "rail_vehicle"

print("\n结果:", ok)
good = ok["init"] and ok["tools"] == 1 and ok["call"] and ok["probe"]
print("HANDSHAKE", "PASS" if good else "FAIL")
sys.exit(0 if good else 1)

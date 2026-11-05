#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mech-model MCP —— 只做一件事：把建模的『沉默默认』变成显式声明并检查。

为什么有这个服务（第十四届实测归因）：
  6 道题里失分最重的第 6 题（-17 分），不是算错，是两条建模轴走了默认：
  锥度方向、轮对轴线能否倾斜。求解器再准也按错模型算，所以缺的不是算力而是**声明**。

工具：model_card(action=index|probe|list|check)
  - index  列全部题型
  - probe  按题干关键词给候选题型（只是候选，人定）
  - list   给该题型的活决策轴：选项 / 选错的后果链 / 判别试验
  - check  收 decisions，返回 缺失 / 未论证(evidence=assumed) / 互相矛盾

铁律：
  - 零第三方依赖（只标准库）；卡是 JSON，赛规下算自研笔记，体积 ~10 KB
  - evidence 为空或 assumed 一律判 block，不给"看起来确定"的通过
  - 卡里不含任何赛题答案，只有判据与后果
  - stdout 只走协议
"""

import json
import os
import sys
import traceback

# ── stdout 保护 ────────────────────────────────────────────────
_real_stdout_fd = os.dup(1)
os.dup2(2, 1)
_OUT = os.fdopen(_real_stdout_fd, "w", encoding="utf-8", buffering=1)

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core  # noqa: E402

SERVER_NAME = "mech-model"
VERSION = "0.1.0"

TOOLS = [
    {
        "name": "model_card",
        "description": (
            "建模决策卡（零依赖、纯本地）。把题型的『活决策轴』摆出来并检查你的建模声明，"
            "专治沉默默认。action=index 列题型；probe 按题干关键词给候选；"
            "list 给某题型的决策轴（每轴含选项/选错后果/判别试验）；"
            "check 收 decisions={轴id:{value,evidence}}，返回缺失、未论证(evidence=assumed)、互相矛盾。"
            "evidence 只能 statement/figure/textbook/derived；assumed 判 block。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": ["index", "probe", "list", "check"]},
                "problem_class": {"type": "string",
                                  "description": "题型 id；list/check 必填，可先 probe 或 index"},
                "text": {"type": "string", "description": "probe 用：题干文本"},
                "decisions": {"type": "object",
                              "description": "check 用：{轴id: {value, evidence, note?}}"},
            },
            "required": ["action"],
        },
    },
]

HANDLERS = {"model_card": core.dispatch}


def call_tool(name, args):
    fn = HANDLERS.get(name)
    if fn is None:
        return {"ok": False, "error": f"未知工具: {name}"}
    try:
        return fn(args or {})
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "error": f"{type(e).__name__}: {e}",
                "trace": traceback.format_exc(limit=3)}


def send(payload):
    _OUT.write(json.dumps(payload, ensure_ascii=False) + "\n")
    _OUT.flush()


def main():
    sys.stderr.write(f"[{SERVER_NAME}] 启动\n")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except Exception as e:  # noqa: BLE001
            sys.stderr.write(f"[{SERVER_NAME}] 非法 JSON: {e}\n")
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
            res = call_tool(p.get("name"), p.get("arguments"))
            send({"jsonrpc": "2.0", "id": mid, "result": {
                "content": [{"type": "text", "text": json.dumps(res, ensure_ascii=False, indent=1)}],
                "isError": not res.get("ok", False)}})
        elif mid is not None:
            send({"jsonrpc": "2.0", "id": mid,
                  "error": {"code": -32601, "message": f"不支持的方法: {method}"}})


if __name__ == "__main__":
    main()

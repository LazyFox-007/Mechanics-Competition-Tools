#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""建模决策卡内核 —— 纯逻辑，无 I/O，可被测试直接 import。

设计意图（来自第十四届实测的失分归因）：
  - 失分最重的不是"算错"，是**建模轴沉默默认**（锥度方向、轴线自由度）。
  - 所以本模块不做"替你建模"，只做两件事：
      list  —— 把该题型的『活决策轴』摆出来（题干没钉死的那些选择）
      check —— 检查你的声明：漏了？没论证？两条之间矛盾？
  - 规则铁律：`evidence` 为空或写成 assumed 一律判不通过。
    卡本身不含任何赛题答案，只有判据与后果链。
"""

import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_CARDS_PATH = os.path.join(_HERE, "cards.json")

_ASSUMED = {"", None, "assumed", "默认", "猜", "guess"}

_cache = {}


def load_cards(path=_CARDS_PATH):
    """按 mtime 失效的缓存：改 cards.json 不必重启 MCP 进程。"""
    try:
        mtime = os.path.getmtime(path)
    except OSError:
        mtime = None
    hit = _cache.get(path)
    if hit is not None and hit[0] == mtime:
        return hit[1]
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    _cache[path] = (mtime, data)
    return data


def _card(pid, data=None):
    data = data or load_cards()
    return data["cards"].get(pid)


def _merged_axes(pid, data=None):
    data = data or load_cards()
    card = data["cards"][pid]
    axes = []
    for a in data["_common"]["axes"]:
        axes.append(dict(a, group="通用"))
    for a in card.get("axes", []):
        axes.append(dict(a, group=card["name"]))
    return axes


# ────────────────────────────── index ──────────────────────────────
def index():
    data = load_cards()
    rows = []
    for pid, c in data["cards"].items():
        rows.append({
            "id": pid,
            "name": c["name"],
            "axes": len(c.get("axes", [])) + len(data["_common"]["axes"]),
            "triggers": c.get("triggers", [])[:6],
        })
    return {"ok": True, "action": "index", "version": data.get("version"),
            "common_axes": [a["id"] for a in data["_common"]["axes"]],
            "cards": rows}


# ────────────────────────────── probe ──────────────────────────────
def probe(text):
    """按关键词打分，返回最可能的卡片（不替代人判断，只是给候选）。"""
    data = load_cards()
    t = text or ""
    scored = []
    for pid, c in data["cards"].items():
        hits = [k for k in c.get("triggers", []) if k and k in t]
        if hits:
            scored.append({"id": pid, "name": c["name"], "hits": hits,
                           "score": len(hits)})
    scored.sort(key=lambda r: -r["score"])
    return {"ok": True, "action": "probe",
            "candidates": scored[:3],
            "note": "只是关键词匹配，最终选题型由人定"}


# ────────────────────────────── list ──────────────────────────────
def list_card(pid):
    data = load_cards()
    card = _card(pid, data)
    if card is None:
        return {"ok": False, "error": f"未知题型: {pid}",
                "available": list(data["cards"].keys())}
    axes = [{"id": a["id"], "group": a["group"], "question": a["question"],
             "options": a["options"], "if_wrong": a.get("if_wrong", ""),
             "test": a.get("test", ""), "pinned": a.get("pinned")}
            for a in _merged_axes(pid, data)]
    return {"ok": True, "action": "list", "problem_class": pid,
            "name": card["name"], "axes": axes,
            "conflicts": card.get("conflicts", []),
            "howto": ("逐条填 decisions，每个轴给 value + evidence。"
                      "evidence 只能是 statement / figure / textbook / derived / assumed；"
                      "assumed 会被判不通过。填完调 action=check。")}


# ────────────────────────────── check ──────────────────────────────
def check(pid, decisions):
    data = load_cards()
    card = _card(pid, data)
    if card is None:
        return {"ok": False, "error": f"未知题型: {pid}",
                "available": list(data["cards"].keys())}
    if decisions is None:
        return {"ok": False, "error": "check 需要 decisions"}
    if isinstance(decisions, str):
        try:
            decisions = json.loads(decisions)
        except Exception as e:  # noqa: BLE001
            return {"ok": False, "error": f"decisions 不是合法 JSON: {e}"}

    axes = _merged_axes(pid, data)
    violations, passed, filled = [], [], {}

    for a in axes:
        aid = a["id"]
        d = decisions.get(aid)
        if d is None:
            violations.append({
                "axis": aid, "level": "error", "code": "MISSING",
                "question": a["question"],
                "message": "未声明：这是活决策轴，题干没钉死，必须显式选择并给证据",
                "options": a["options"], "if_wrong": a.get("if_wrong", "")})
            continue

        if isinstance(d, str):
            d = {"value": d}
        val = d.get("value")
        ev = d.get("evidence")

        if val not in a["options"]:
            violations.append({
                "axis": aid, "level": "error", "code": "BAD_VALUE",
                "got": val, "options": a["options"],
                "message": "取值不在选项内"})
            continue

        if ev in _ASSUMED:
            violations.append({
                "axis": aid, "level": "error", "code": "UNARGUED",
                "value": val, "evidence": ev if ev is not None else "(缺)",
                "question": a["question"],
                "message": ("未论证：evidence=%r。选错的后果 —— %s"
                            % (ev, a.get("if_wrong", ""))),
                "test": a.get("test", "")})
            continue

        if a.get("pinned") is not None and val != a["pinned"]:
            violations.append({
                "axis": aid, "level": "error", "code": "CONTRADICTS_STEM",
                "value": val, "pinned": a["pinned"],
                "message": f"与题干钉死值冲突（题干为 {a['pinned']}）"})
            continue

        filled[aid] = {"value": val, "evidence": ev,
                       "note": d.get("note", "")}
        passed.append({"axis": aid, "value": val, "evidence": ev})

    # 矛盾规则
    for cf in card.get("conflicts", []):
        when = cf.get("when", {})
        got = {}
        ok = True
        for k, v in when.items():
            d = decisions.get(k)
            gv = d.get("value") if isinstance(d, dict) else d
            if gv != v:
                ok = False
                break
            got[k] = gv
        if ok:
            violations.append({"level": cf.get("severity", "error"),
                               "code": "CONFLICT", "axes": got,
                               "message": cf.get("message", "")})

    n_err = sum(1 for v in violations if v["level"] == "error")
    n_warn = len(violations) - n_err
    return {
        "ok": True, "action": "check", "problem_class": pid,
        "verdict": "pass" if n_err == 0 else "block",
        "n_error": n_err, "n_warn": n_warn,
        "violations": violations,
        "passed": passed,
        "filled": filled,
        "note": ("verdict=block 时不许往下算；逐条改完再 check。"
                 "这份 filled 就是留痕里的『建模声明』。"),
    }


def dispatch(args):
    args = args or {}
    action = (args.get("action") or "index").lower()
    if action == "index":
        return index()
    if action == "probe":
        return probe(args.get("text") or "")
    if action == "list":
        pid = args.get("problem_class")
        if not pid:
            return {"ok": False, "error": "list 需要 problem_class；可先 action=probe 或 index",
                    "available": list(load_cards()["cards"].keys())}
        return list_card(pid)
    if action == "check":
        pid = args.get("problem_class")
        if not pid:
            return {"ok": False, "error": "check 需要 problem_class"}
        return check(pid, args.get("decisions"))
    return {"ok": False, "error": f"未知 action: {action}",
            "actions": ["index", "probe", "list", "check"]}

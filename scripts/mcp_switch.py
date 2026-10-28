# -*- coding: utf-8 -*-
"""
mcp_switch.py —— 安全地开关 ~/.dsh/cordis.patch.yml 里的 MCP 条目。

为什么不用普通 YAML 读写：这个文件里全是注释和分块 `- insert:`，
整体 dump 回去会把这些注释和顺序全毁掉。所以这里**按行**改：
只在目标条目的 `- id:` 行后面插入/删除 `disabled: true`，其余字节不动。

用法：
  python scripts/mcp_switch.py --list
  python scripts/mcp_switch.py --disable browser,context7
  python scripts/mcp_switch.py --enable lean4
  python scripts/mcp_switch.py --only document,sympy,sympy-physics,mech-io
  python scripts/mcp_switch.py --restore                # 恢复最近一次备份
  python scripts/mcp_switch.py --restore <备份路径>

所有写操作都会先备份，并在写完后用 yaml.safe_load 校验；校验失败自动回滚。
"""
import argparse
import io
import os
import shutil
import sys
import time

CFG = os.path.join(os.path.expanduser("~"), ".dsh", "cordis.patch.yml")


def read_lines(path):
    with io.open(path, encoding="utf-8", newline="") as f:
        return f.read().splitlines(keepends=True)


def write_lines(path, lines):
    with io.open(path, "w", encoding="utf-8", newline="") as f:
        f.write("".join(lines))


def blocks(lines):
    """返回 [{id, server_name, start, end, disabled, indent}]；start 是 `- id:` 行号。"""
    out = []
    cur = None
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s.startswith("- id:"):
            if cur:
                out.append(cur)
            cur = {"id": s.split(":", 1)[1].strip(), "start": i, "end": len(lines),
                   "server_name": None, "disabled": False}
        elif cur is not None:
            if s.startswith("serverName:"):
                cur["server_name"] = s.split(":", 1)[1].strip()
            if s == "disabled: true":
                cur["disabled"] = True
    if cur:
        out.append(cur)
    for k in range(len(out) - 1):
        out[k]["end"] = out[k + 1]["start"]
    for b in out:
        ln = lines[b["start"]]
        b["indent"] = ln[: len(ln) - len(ln.lstrip())]
    return out


def cmd_list():
    lines = read_lines(CFG)
    for b in blocks(lines):
        name = b["server_name"]
        if not name:          # 非 MCP 的插件行没有 serverName，不列
            continue
        print(f"  {'OFF' if b['disabled'] else 'ON ':3}  {name:16} (id={b['id']})")


def apply(disable=(), enable=(), only=None):
    lines = read_lines(CFG)
    bs = blocks(lines)
    if only:
        keep = {s.strip() for s in only}
        disable = {b["server_name"] for b in bs if b["server_name"] and b["server_name"] not in keep}
        enable = keep
    else:
        disable, enable = set(disable), set(enable)

    targets = [b for b in bs if b["server_name"] in disable or b["server_name"] in enable]
    if not targets:
        print("没有匹配的条目")
        return 0

    # 从后往前改，避免行号位移
    changed = 0
    for b in sorted(targets, key=lambda x: -x["start"]):
        want_off = b["server_name"] in disable
        if want_off and not b["disabled"]:
            lines.insert(b["start"] + 1, f"{b['indent']}  disabled: true\n")
            changed += 1
        elif (not want_off) and b["disabled"]:
            for j in range(b["start"] + 1, b["end"]):
                if lines[j].strip() == "disabled: true":
                    del lines[j]
                    changed += 1
                    break

    if not changed:
        print("状态已是目标值，无需改动")
        return 0

    bak = CFG + ".bak-switch-" + time.strftime("%Y%m%d-%H%M%S")
    shutil.copyfile(CFG, bak)

    import yaml
    try:
        write_lines(CFG, lines)
        with io.open(CFG, encoding="utf-8") as f:
            yaml.safe_load(f)
    except Exception as e:  # noqa: BLE001
        shutil.copyfile(bak, CFG)
        print(f"写回失败，已回滚：{e}", file=sys.stderr)
        return 1

    print(f"已更新 {changed} 条，备份：{bak}")
    cmd_list()
    return 0


def cmd_restore(path=None):
    if path is None:
        cands = [os.path.join(os.path.dirname(CFG), f) for f in os.listdir(os.path.dirname(CFG))
                 if f.startswith(os.path.basename(CFG) + ".bak-")]
        if not cands:
            print("没有备份可恢复", file=sys.stderr)
            return 1
        path = max(cands, key=os.path.getmtime)
    if not os.path.isfile(path):
        print(f"备份不存在：{path}", file=sys.stderr)
        return 1
    shutil.copyfile(path, CFG)
    print(f"已恢复：{path}")
    cmd_list()
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--disable")
    ap.add_argument("--enable")
    ap.add_argument("--only")
    ap.add_argument("--restore", nargs="?", const="")
    a = ap.parse_args()

    if not os.path.isfile(CFG):
        print(f"找不到 {CFG}", file=sys.stderr)
        return 1
    if a.restore is not None:
        return cmd_restore(a.restore or None)
    if a.list:
        cmd_list()
        return 0
    split = lambda s: [x.strip() for x in s.split(",") if x.strip()] if s else []
    if a.only:
        return apply(only=split(a.only))
    if a.disable or a.enable:
        return apply(disable=split(a.disable), enable=split(a.enable))
    cmd_list()
    return 0


if __name__ == "__main__":
    sys.exit(main())

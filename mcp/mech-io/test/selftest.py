# -*- coding: utf-8 -*-
"""
mech-io 自测：真的起一个 stdio 子进程，按 JSON-RPC 逐个调工具。

跑法：python mcp/mech-io/test/selftest.py
可选：python mcp/mech-io/test/selftest.py --pdf "D:/xxx/赛题.pdf"

覆盖本次比赛真实踩过的坑：
  - 中文参数经 argv 传递（不再被 PowerShell 拆坏）
  - 中文 stdout（不再 GBK 崩）
  - 分数坐标裁剪（不再被预览图缩放坑）
  - PDF 局部高清取图（公式下标）
  - 缺字形 / 文字越界 / 文字重叠
  - 密扫描找极值、双表达式比对
  - HTML→PDF、提交骨架与清单
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SERVER = os.path.join(os.path.dirname(HERE), "server.py")
ROOT = os.path.dirname(os.path.dirname(HERE))          # 仓库根

PASS, FAIL, SKIP = "[PASS]", "[FAIL]", "[SKIP]"
results = []


def rec(ok, name, detail=""):
    results.append((ok, name, detail))
    tag = PASS if ok is True else (SKIP if ok is None else FAIL)
    print(f"{tag} {name}" + (f"  {detail}" if detail else ""))


class Client:
    def __init__(self, py):
        self.p = subprocess.Popen(
            [py, SERVER],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            cwd=ROOT,
        )
        self._id = 0
        self.request("initialize", {"protocolVersion": "2024-11-05"})

    def request(self, method, params=None):
        self._id += 1
        msg = {"jsonrpc": "2.0", "id": self._id, "method": method}
        if params is not None:
            msg["params"] = params
        self.p.stdin.write((json.dumps(msg, ensure_ascii=False) + "\n").encode("utf-8"))
        self.p.stdin.flush()
        line = self.p.stdout.readline()
        if not line:
            raise RuntimeError("服务端没有响应（可能启动失败）：" + self.p.stderr.read().decode("utf-8", "replace")[-800:])
        return json.loads(line.decode("utf-8"))

    def call(self, tool, args=None):
        resp = self.request("tools/call", {"name": tool, "arguments": args or {}})
        if "error" in resp:
            raise RuntimeError(resp["error"])
        text = resp["result"]["content"][0]["text"]
        return json.loads(text)

    def close(self):
        try:
            self.p.stdin.close()
            self.p.wait(timeout=5)
        except Exception:  # noqa: BLE001
            self.p.kill()


def main():
    py = sys.executable
    pdf_arg = None
    if "--pdf" in sys.argv:
        pdf_arg = sys.argv[sys.argv.index("--pdf") + 1]

    tmp = tempfile.mkdtemp(prefix="mechio_test_")
    c = Client(py)

    # 1. tools/list
    tl = c.request("tools/list")
    names = [t["name"] for t in tl["result"]["tools"]]
    rec(len(names) == 10, "tools/list 返回 10 个工具", ",".join(names))

    # 2. io_info
    info = c.call("io_info")
    rec(info.get("ok") and info.get("optional", {}).get("Pillow"), "io_info 自检", str(info.get("optional")))

    # 3. py_run：中文 stdout（本次被 GBK 坑过）
    r = c.call("py_run", {"code": "print('中文输出 ✓ 行2')"})
    rec(r.get("ok") and "中文输出" in r.get("stdout", ""), "py_run 中文 stdout", r.get("stdout", "").strip())

    # 4. py_run：中文 argv（本次被 PowerShell 弯引号坑过）
    script = os.path.join(tmp, "argv_echo.py")
    with open(script, "w", encoding="utf-8") as f:
        f.write("import sys\nprint('|'.join(sys.argv[1:]))\n")
    trick = '“国产AI大模型” — 45°'
    r = c.call("py_run", {"path": script, "args": [trick, "第二项"]})
    rec(r.get("ok") and trick in r.get("stdout", ""), "py_run 中文/弯引号 argv 原样传递", r.get("stdout", "").strip())

    # 5. 造一张测试图（1406x1988，模拟 170dpi 卷面）
    img = os.path.join(tmp, "page.png")
    r = c.call("py_run", {"code": (
        "from PIL import Image, ImageDraw\n"
        f"im=Image.new('RGB',(1406,1988),'white')\n"
        "d=ImageDraw.Draw(im)\n"
        "for k in range(0,1406,80): d.line([(k,0),(k,1988)],fill='black',width=1)\n"
        "for k in range(0,1988,80): d.line([(0,k),(1406,k)],fill='black',width=1)\n"
        "d.ellipse([500,800,900,1200],outline='black',width=6)\n"
        f"im.save(r'{img}')\n"
        "print(im.size)\n"
    )})
    rec(r.get("ok"), "py_run 生成测试图", r.get("stdout", "").strip())

    # 6. img_crop：分数坐标不依赖像素
    out = os.path.join(tmp, "crop.png")
    r = c.call("img_crop", {"path": img, "box": [0.25, 0.25, 0.75, 0.75], "scale": 2, "out": out})
    px = r.get("box_px") or [0, 0, 0, 0]
    expect = [(px[2] - px[0]) * 2, (px[3] - px[1]) * 2]
    rec(r.get("ok") and r.get("out_size") == expect, "img_crop 分数坐标 + 放大",
        f"{r.get('out_size')} 期望 {expect}")

    # 7. pdf_page_crop（有 PDF 才测）
    if pdf_arg and os.path.isfile(pdf_arg):
        outp = os.path.join(tmp, "pdf_crop.png")
        r = c.call("pdf_page_crop", {"path": pdf_arg, "page": 11,
                                     "box": [0.25, 0.16, 1.0, 0.30], "dpi": 300, "out": outp})
        rec(r.get("ok") and os.path.isfile(outp), "pdf_page_crop 取参数行",
            f"size={r.get('size')} file={os.path.getsize(outp) if os.path.isfile(outp) else 0}")
    else:
        rec(None, "pdf_page_crop", "未提供 --pdf，跳过")

    # 8. fig_lint
    r = c.call("fig_lint", {"paths": [out]})
    rec(r.get("ok") and r["figures"][0]["blank"] is False, "fig_lint 非空白判定",
        f"std={r['figures'][0]['std_gray']}")

    # 9. plot_audit：坏脚本（长标题越界 + 缺字形）
    bad = os.path.join(tmp, "bad_fig.py")
    with open(bad, "w", encoding="utf-8") as f:
        f.write(
            "import matplotlib\nmatplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
            "fig, ax = plt.subplots(figsize=(3, 2))\n"
            "ax.plot([0, 1], [0, 1])\n"
            "ax.set_title('这是一个非常长的标题必然会超出画布并且和轴标签压在一起 yₙ')\n"
            "ax.set_xlabel('也很长很长很长很长很长很长很长很长很长的轴标签')\n"
            "fig.savefig('bad_fig.png')\n"
        )
    r = c.call("plot_audit", {"script": bad})
    ok = r.get("ok") and (r["summary"]["issues"] > 0 or r["summary"]["missing_glyphs"] > 0)
    rec(bool(ok), "plot_audit 抓到越界/缺字形",
        f"issues={r.get('summary', {}).get('issues')} glyph={r.get('summary', {}).get('missing_glyphs')}")

    # 10. plot_audit：干净脚本
    good = os.path.join(tmp, "good_fig.py")
    with open(good, "w", encoding="utf-8") as f:
        f.write(
            "import matplotlib\nmatplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
            "fig, ax = plt.subplots(figsize=(4, 3))\n"
            "ax.plot([0, 1], [0, 1])\n"
            "ax.set_title('ok')\n"
            "ax.set_xlabel('x')\n"
            "fig.tight_layout()\n"
            "fig.savefig('good_fig.png')\n"
        )
    r = c.call("plot_audit", {"script": good})
    rec(r.get("ok") and r["summary"]["clean"], "plot_audit 干净脚本判 clean",
        json.dumps(r.get("summary"), ensure_ascii=False))

    # 11. scan_extremum（带参数）
    r = c.call("scan_extremum", {"expr": "x*(l-x)", "vars": [["x", 0, 5]],
                                 "params": {"l": "5"}, "find": "max"})
    ok = r.get("ok") and abs(r["value"] - 6.25) < 1e-3 and abs(r["at"]["x"] - 2.5) < 1e-2
    rec(bool(ok), "scan_extremum 极值+参数代入", f"value={r.get('value')} at={r.get('at')}")

    # 12. scan_extremum 缺参数应报错
    r = c.call("scan_extremum", {"expr": "x*(l-x)", "vars": [["x", 0, 5]]})
    rec(r.get("ok") is False and "未给值" in r.get("error", ""), "scan_extremum 缺参数报错",
        r.get("error", ""))

    # 13. numeric_compare
    r = c.call("numeric_compare", {"expr_a": "sin(x)**2+cos(x)**2", "expr_b": "1",
                                   "vars": [["x", 0, 6.28]]})
    rec(r.get("ok") and r["pass"], "numeric_compare 恒等式", f"max_rel={r.get('max_rel_err')}")

    # 14. html_to_pdf
    html = os.path.join(tmp, "t.html")
    with open(html, "w", encoding="utf-8") as f:
        f.write("<html><meta charset='utf-8'><body style=\"font-family:'Microsoft YaHei'\">"
                "<h1>中文标题测试</h1><p>公式：σ = M·y / I</p></body></html>")
    r = c.call("html_to_pdf", {"html": html})
    rec(r.get("ok") and os.path.getsize(r["pdf"]) > 1000, "html_to_pdf", f"size={r.get('size')}")

    # 15. submission_pack init + manifest
    r = c.call("submission_pack", {"action": "init", "root": tmp,
                                   "team": "AIC-2026-00000000", "name": "自测队"})
    folder = r.get("folder", "")
    rec(r.get("ok") and os.path.isdir(folder), "submission_pack init", folder)
    r2 = c.call("submission_pack", {"action": "manifest", "root": folder})
    rec(r2.get("ok") and r2["count"] >= 2, "submission_pack manifest",
        f"count={r2.get('count')}")

    c.close()

    n_fail = sum(1 for ok, _, _ in results if ok is False)
    n_skip = sum(1 for ok, _, _ in results if ok is None)
    print(f"\n合计 {len(results)} 项：通过 {len(results) - n_fail - n_skip}，失败 {n_fail}，跳过 {n_skip}")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())

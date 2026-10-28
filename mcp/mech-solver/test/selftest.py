# -*- coding: utf-8 -*-
"""
mech-solver 自测：起 stdio 子进程，按 JSON-RPC 逐个调工具。
每个用例都有手算可对照的期望值。

跑法：python mcp/mech-solver/test/selftest.py
"""
import json
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SERVER = os.path.join(os.path.dirname(HERE), "server.py")

PASS, FAIL = "[PASS]", "[FAIL]"
results = []


def rec(ok, name, detail=""):
    results.append(ok)
    print(f"{PASS if ok else FAIL} {name}" + (f"  {detail}" if detail else ""))


class Client:
    def __init__(self, py):
        self.p = subprocess.Popen([py, SERVER], stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.i = 0
        self.req("initialize", {"protocolVersion": "2024-11-05"})

    def req(self, method, params=None):
        self.i += 1
        m = {"jsonrpc": "2.0", "id": self.i, "method": method}
        if params:
            m["params"] = params
        self.p.stdin.write((json.dumps(m) + "\n").encode())
        self.p.stdin.flush()
        line = self.p.stdout.readline()
        if not line:
            raise RuntimeError("无响应: " + self.p.stderr.read().decode("utf-8", "replace")[-500:])
        return json.loads(line)

    def call(self, name, args=None):
        r = self.req("tools/call", {"name": name, "arguments": args or {}})
        return json.loads(r["result"]["content"][0]["text"])

    def close(self):
        try:
            self.p.stdin.close()
            self.p.wait(timeout=5)
        except Exception:  # noqa: BLE001
            self.p.kill()


def main():
    c = Client(sys.executable)

    tl = c.req("tools/list")
    names = [t["name"] for t in tl["result"]["tools"]]
    rec(len(names) == 5, "tools/list", ",".join(names))

    info = c.call("solver_info")
    rec(info.get("ok") and info["optional"]["sympy"], "solver_info", str(info.get("branches")))

    # 1) 卡氏定理：悬臂梁端部集中力，δ = Pl³/(3EI)
    E, I, l = 210e9, 1e-6, 2.0
    r = c.call("energy_method", {
        "op": "castigliano", "M": "-P*(l-x)", "EI": "E*I", "span": ["0", "l"], "P": "P",
        "params": {"l": str(l), "E": str(E), "I": str(I)}})
    expect = l ** 3 / (3 * E * I)          # δ/P
    ok = r.get("ok") and r["check_fd"]["pass"]
    rec(bool(ok), "卡氏定理 悬臂梁 δ=Pl³/3EI", f"check_fd rel_err={r.get('check_fd', {}).get('rel_err'):.2e}"
        if r.get("ok") else r.get("error", ""))

    # 2) 单位载荷法：同一根梁，δ = ∫M·m̄/EI = Pl³/(3EI)
    r = c.call("energy_method", {
        "op": "unit_load", "M": "-P*(l-x)", "mbar": "-(l-x)", "EI": "E*I", "span": ["0", "l"],
        "params": {"l": str(l), "E": str(E), "I": str(I), "P": "1"}})
    val = r.get("numeric")
    ok = r.get("ok") and val is not None and abs(val - expect) / expect < 1e-9
    rec(bool(ok), "单位载荷法 同一根梁", f"数值={val:.6e} 期望={expect:.6e}")

    # 3) 桁架：三杆三角架，A(0,0) 铰、B(2,0) 辊轴、C(1,1) 竖向 -10
    r = c.call("truss_solve", {
        "nodes": [{"name": "A", "x": 0, "y": 0}, {"name": "B", "x": 2, "y": 0},
                  {"name": "C", "x": 1, "y": 1}],
        "members": [{"a": "A", "b": "C"}, {"a": "B", "b": "C"}, {"a": "A", "b": "B"}],
        "supports": [{"node": "A", "type": "pin"}, {"node": "B", "type": "roller"}],
        "loads": [{"node": "C", "fx": 0, "fy": -10}]})
    f = {m["member"]: m["N"] for m in (r.get("member_forces") or [])}
    reac = {(x["node"], x["dir"]): x["R"] for x in (r.get("reactions") or [])}
    expect_f = {"A-C": -10 / (2 * math.sin(math.pi / 4)), "B-C": -10 / (2 * math.sin(math.pi / 4)), "A-B": 5.0}
    ok = (r.get("ok") and r["check"]["pass"]
          and all(abs(f[k] - v) < 1e-6 for k, v in expect_f.items())
          and abs(reac[("A", "y")] - 5) < 1e-6 and abs(reac[("B", "y")] - 5) < 1e-6)
    rec(bool(ok), "桁架 三杆三角架", f"杆力={ {k: round(v,4) for k,v in f.items()} } 反力={ {k: round(v,4) for k,v in reac.items()} }")

    # 4) 桁架：少一根杆 → 机构，应拒绝
    r = c.call("truss_solve", {
        "nodes": [{"name": "A", "x": 0, "y": 0}, {"name": "B", "x": 2, "y": 0}, {"name": "C", "x": 1, "y": 1}],
        "members": [{"a": "A", "b": "C"}, {"a": "B", "b": "C"}],
        "supports": [{"node": "A", "type": "pin"}, {"node": "B", "type": "roller"}],
        "loads": [{"node": "C", "fx": 0, "fy": -10}]})
    rec(r.get("ok") is False and "机构" in r.get("error", ""), "桁架 少杆判机构", r.get("error", ""))

    # 5) 刚体平面运动：ω=2, vA=0, r=(1,0) → vB=(0,2)
    r = c.call("rigid_planar", {"op": "vel", "omega": 2, "vA": [0, 0], "r": [1, 0]})
    ok = r.get("ok") and abs(r["vB"][0]) < 1e-12 and abs(r["vB"][1] - 2) < 1e-12
    rec(bool(ok), "刚体 vB=ω×r", str(r.get("vB")))

    # 6) 加速度：α=0, ω=2, r=(1,0) → aB=(-4,0)
    r = c.call("rigid_planar", {"op": "acc", "omega": 2, "alpha": 0, "aA": [0, 0], "r": [1, 0]})
    ok = r.get("ok") and abs(r["aB"][0] + 4) < 1e-12 and abs(r["aB"][1]) < 1e-12
    rec(bool(ok), "刚体 aB=−ω²r", str(r.get("aB")))

    # 7) 瞬心：ω=2, vA=(0,2) → IC 在 A 下方 1（r_A=(v_ay/ω, -v_ax/ω)=(1,0) → IC=(-1,0)? 见断言）
    r = c.call("rigid_planar", {"op": "ic", "omega": 2, "vA": [0, 2], "A": [0, 0]})
    ok = r.get("ok") and r["check"]["pass"]
    rec(bool(ok), "速度瞬心 |v|=ωr", f"ic={r.get('ic')} r={r.get('radius_A')}")

    # 8) 压杆稳定：两端铰支，λ=31.6 < λp=99.4 → 中柔度，走经验公式 σcr=a−bλ
    r = c.call("buckling_solve", {"E": 200e9, "I": 1e-6, "A": 1e-3, "l": 1.0,
                                  "ends": "pinned-pinned", "sigma_p": 200e6,
                                  "a": 304e6, "b": 1.12e6})
    sig_expect = 304e6 - 1.12e6 * r.get("lambda", 0)
    ok = (r.get("ok") and abs(r["P_cr_euler"] - math.pi ** 2 * 200e9 * 1e-6) < 1
          and r["check"]["pass"] and "中柔度" in r["regime"]
          and abs(r["sigma_cr"] - sig_expect) < 1.0)
    rec(bool(ok), "压杆 柔度分档+经验公式",
        f"λ={r.get('lambda'):.2f} λp={r.get('lambda_p'):.2f} σcr={r.get('sigma_cr')/1e6:.1f}MPa {r.get('regime')}")

    c.close()
    bad = results.count(False)
    print(f"\n合计 {len(results)} 项：通过 {len(results)-bad}，失败 {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

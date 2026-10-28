# A stateless MCP server wrapping a local Lean 4 toolchain.
# Provides tools to check, evaluate and query Lean 4 code.

import os
import re
import subprocess
import tempfile

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("lean4")

LEAN_DIR = os.path.expanduser("~/.elan/bin")
MATHLIB_PROJECT = r"D:\TheSkillOfAI\lean-mathlib-project"


def _lean_bin(name: str) -> str:
    exe = name + (".exe" if os.name == "nt" else "")
    return os.path.join(LEAN_DIR, exe)


def _run(args: list, timeout: int = 120, cwd: str = None) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    env["NO_COLOR"] = "1"
    return subprocess.run(
        args,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        cwd=cwd,
        env=env,
    )


@mcp.tool()
def lean_version() -> str:
    """Returns the installed Lean 4 version and lake (build tool) version."""
    try:
        lean = _run([_lean_bin("lake"), "env", "lean", "--version"], cwd=MATHLIB_PROJECT).stdout.strip()
        lake = _run([_lean_bin("lake"), "--version"], cwd=MATHLIB_PROJECT).stdout.strip()
        return f"{lean}\n{lake}"
    except FileNotFoundError:
        return "error: lean not found in " + LEAN_DIR


@mcp.tool()
def check_lean_code(lean_code: str, imports: str = "import Mathlib\n") -> str:
    """Type-checks a complete Lean 4 snippet and returns compiler feedback.

    Args:
        lean_code: The Lean 4 code to check (a theorem, definition, etc.).
        imports: Optional import lines prepended to the code (default: Mathlib).
    """
    with tempfile.NamedTemporaryFile(mode="w", suffix=".lean", delete=False, encoding="utf-8") as f:
        f.write(imports + "\n" + lean_code)
        path = f.name
    try:
        result = _run([_lean_bin("lake"), "env", "lean", path], cwd=MATHLIB_PROJECT, timeout=180)
        output = (result.stdout + result.stderr).strip()
        if result.returncode == 0:
            return "OK: no errors."
        # Strip absolute temp path from messages
        output = output.replace(path, "<file>")
        return output
    finally:
        os.unlink(path)


@mcp.tool()
def run_lean_code(lean_code: str) -> str:
    """Runs a Lean 4 script with `lean --run` and returns its printed output.

    The code must be a full program (def main : IO Unit := ... or standalone
    top-level commands). IO output is captured.

    Args:
        lean_code: The Lean 4 code to execute.
    """
    with tempfile.NamedTemporaryFile(mode="w", suffix=".lean", delete=False, encoding="utf-8") as f:
        f.write(lean_code)
        path = f.name
    try:
        result = _run([_lean_bin("lake"), "env", "lean", "--run", path], cwd=MATHLIB_PROJECT, timeout=180)
        output = (result.stdout + result.stderr).strip()
        if result.returncode == 0:
            return output or "OK: no output."
        output = output.replace(path, "<file>")
        return "error:\n" + output
    finally:
        os.unlink(path)


@mcp.tool()
def query_lean(lean_code: str) -> str:
    """Evaluates `#check`, `#eval`, `#reduce`, `#print` queries in Lean 4 and returns the results.

    Args:
        lean_code: One or more #check / #eval / #reduce / #print commands.
    """
    with tempfile.NamedTemporaryFile(mode="w", suffix=".lean", delete=False, encoding="utf-8") as f:
        f.write("import Mathlib\n\n" + lean_code)
        path = f.name
    try:
        result = _run([_lean_bin("lake"), "env", "lean", path], cwd=MATHLIB_PROJECT, timeout=180)
        output = (result.stdout + result.stderr).strip()
        if result.returncode == 0:
            return output or "OK: no output."
        output = output.replace(path, "<file>")
        return "error:\n" + output
    finally:
        os.unlink(path)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()

"""P2 smallest viable slice smoke: Robust PowerShell Execution Tool / Sandbox.

Run:
  .\.venv\Scripts\python.exe test_p2_pwsh_smoke.py

Focus (tiny slice):
- Harden _execute_powershell (now run_robust_powershell) with truncation + explicit timeout.
- Expose via ToolRegistry ("run_robust_powershell").
- Dual: Python surface (executor/agents/registry) + ready for PS wrapper / GUI terminal.
- Live validation of success, truncation, timeout paths.
- Traceability: L2-001 / TOOL-001 in IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md + IDE_REFACTOR_PLAN §5.

Slice 2 (this run): env scoping + basic sandbox notes + PS wrapper example + smoke extension.
Next: full sandbox profile, procedure parser integration for env, richer docs, etc.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.platform.orchestration.executor import run_robust_powershell
from src.platform.tools.registry import get_registry, reset_registry_for_tests


def main() -> int:
    print("=== P2 Pwsh Smoke (smallest slice) ===")

    # 1. Direct robust call - success path
    ev = run_robust_powershell("Write-Output 'P2-SMOKE-OK'")
    print(f"success: status={ev.status}, stdout[:50]={ev.stdout[:50]!r}")
    assert ev.status == "success"
    assert "P2-SMOKE-OK" in ev.stdout
    print("  PASS: basic success")

    # 2. Truncation
    reset_registry_for_tests()
    longish = "Write-Output ('x' * 200)"
    ev_trunc = run_robust_powershell(longish, max_output=50)
    print(f"trunc: len(stdout)={len(ev_trunc.stdout)}, contains marker={'truncated' in ev_trunc.stdout}")
    assert len(ev_trunc.stdout) <= 50 + 40  # original slice + marker
    assert "truncated" in ev_trunc.stdout
    print("  PASS: output truncation")

    # 3. Timeout path (Start-Sleep is reliable on pwsh/Windows)
    ev_to = run_robust_powershell("Start-Sleep -Seconds 3", timeout=1)
    print(f"timeout: status={ev_to.status}, stderr={ev_to.stderr!r}")
    assert ev_to.status == "timeout"
    assert "Timeout" in ev_to.stderr
    print("  PASS: explicit timeout status")

    # 4. Env scoping (P2 slice 2) + basic sandbox note (env is caller-controlled)
    ev_env = run_robust_powershell('Write-Output "ENV:$env:P2_SMOKE_ENV"', env={"P2_SMOKE_ENV": "from-smoke"})
    print(f"env: status={ev_env.status}, contains from-smoke={'from-smoke' in ev_env.stdout}")
    assert ev_env.status == "success"
    assert "from-smoke" in ev_env.stdout
    print("  PASS: env support (safe merge)")

    # 5. Registry exposure (P2 tool)
    reg = get_registry()
    tools = reg.list_tools()
    print(f"registry tools contain run_robust_powershell: {'run_robust_powershell' in tools}")
    assert "run_robust_powershell" in tools
    # invoke via registry (uses the same hardened func)
    ev_via_reg = reg.invoke("run_robust_powershell", command="Write-Output 'via-registry'")
    assert ev_via_reg.status == "success"
    assert "via-registry" in ev_via_reg.stdout
    print("  PASS: registered as tool and invocable")

    # 6. PS / dual note (the surface is the Python func; PS wrapper can call it via the existing Invoke or future thin .ps1)
    print("  (Dual PS surface: existing Invoke-IdeTool.ps1 + future direct robust wrapper; GUI terminal will call the same Python entry. Env support ready for sandboxed procedures.)")

    print("\n=== P2 SMOKE COMPLETE (slice 2 passed) ===")
    print("Next: more P2 (full sandbox profile, richer PS integration, docs, integration in procedure parser), tiny anchors, matrix update.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

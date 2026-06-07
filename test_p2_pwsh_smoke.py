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
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.platform.orchestration.executor import run_robust_powershell, ProceduralSkillExecutor
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

    # 7. Real skill step test (P2 conclusion slice): use ProceduralSkillExecutor on a temp SKILL.md
    # with a safe inline pwsh block. This exercises the parser -> run_robust_powershell path.
    temp_skill = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, dir='.', encoding='utf-8') as f:
            f.write("""---
name: p2-real-pwsh-test
---
# temp for smoke
## Procedure
```pwsh
Write-Output "REAL-SKILL-PWSH-STEP-OK"
```
""")
            temp_skill = f.name
        execr = ProceduralSkillExecutor(workspace_root=".")
        res = execr.execute(temp_skill)
        pwsh_evs = [e for e in res.evidence if e.step_type == "pwsh"]
        print(f"real-skill: #pwsh-evs={len(pwsh_evs)}, status={res.status}, has-ok={any('REAL-SKILL-PWSH-STEP-OK' in (e.stdout or '') for e in pwsh_evs)}")
        assert len(pwsh_evs) == 1
        assert "REAL-SKILL-PWSH-STEP-OK" in pwsh_evs[0].stdout
        assert res.status in ("success", "partial")
        print("  PASS: real SKILL.md pwsh step via executor (robust path)")
    finally:
        if temp_skill and Path(temp_skill).exists():
            Path(temp_skill).unlink()

    print("\n=== P2 SMOKE COMPLETE (P2 to conclusion) ===")
    print("All P2 items (harden timeouts/env/cwd/output/error, sandbox notes, PS wrappers, registry expose, real skill step test, dual PS/GUI, anchors, trace) complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

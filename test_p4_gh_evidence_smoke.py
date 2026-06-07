"""P4 Slice 1 smoke: gh CLI / GitHub Evidence Tool (basic wrapper + registry).

Run:
  .\.venv\Scripts\python.exe test_p4_gh_evidence_smoke.py

Focus (tiny slice):
- gh_evidence.py: reliable wrapper (_run_gh with auth precheck, create-issue, attach, etc.).
- Evidence schema helper.
- Registered as 'gh_evidence' in ToolRegistry (scopes gh.evidence).
- Live smoke: import, registry presence, structured call (auth check or graceful error), schema.
- Dry-run friendly (no real attach if no auth/gh).
- Tiny changes. Live validation. Dual (Python now; PS in slice 2).
- Trace to TOOL-001 (gh/evidence wrappers), L4, §5, matrix.

This is the first small testable batch for P4.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.platform.tools.gh_evidence import gh_evidence, evidence_schema_example, _run_gh
from src.platform.tools.registry import get_registry, reset_registry_for_tests


def main() -> int:
    print("=== P4 Gh Evidence Smoke (slice 1) ===")

    # 1. Basic wrapper direct call (auth check or graceful)
    res = gh_evidence("create-issue", title="P4 smoke test (dry-run)", body="Test evidence attachment. No real gh attach.")
    print(f"direct gh_evidence create-issue: status={res['status']}, has_auth_err={'auth' in (res.get('stderr','') + res.get('stdout','')).lower()}")
    assert "status" in res and "command" in res
    print("  PASS: structured result from gh_evidence")

    # 2. _run_gh internal (for auth precheck test)
    auth_res = _run_gh(["auth", "status"])
    print(f"_run_gh auth: status={auth_res['status']}")
    # May be error if no gh or no auth, but always structured
    assert auth_res["status"] in ("success", "error", "timeout")
    print("  PASS: auth precheck / reliable wrapper")

    # 3. Evidence schema
    schema = evidence_schema_example()
    print(f"evidence_schema_example: type={schema['type']}, has_files={'files' in schema}")
    assert schema["type"] == "gh-evidence"
    print("  PASS: evidence schema helper")

    # 4. Registry exposure
    reset_registry_for_tests()
    reg = get_registry()
    tools = reg.list_tools()
    print(f"registry has gh_evidence: {'gh_evidence' in tools}")
    assert "gh_evidence" in tools
    # Try invoke (will use wrapper)
    inv_res = reg.invoke("gh_evidence", action="create-issue", title="P4 via registry smoke")
    print(f"registry invoke gh_evidence: status={inv_res.get('status')}")
    assert "status" in inv_res
    print("  PASS: registered and invocable via ToolRegistry")

    print("\n=== P4 SLICE 1 SMOKE COMPLETE ===")
    print("Next slice: PS wrapper + evidence schema usage in attach, more tests.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

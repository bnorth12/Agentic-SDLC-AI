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

    # Slice 2 preview (integrated for small batch): evidence schema in attach call
    attach_res = gh_evidence("attach", target="#42", files=["evidence/trace.md"], body="P4 attach sim")
    print(f"attach sim (schema/files): status={attach_res['status']}, command has attach={'attach' in attach_res.get('command','')}")
    schema = evidence_schema_example()
    assert "files" in schema and schema["type"] == "gh-evidence"
    print("  PASS: evidence schema + attach action (sim)")

    # Note: real attach would use gh release upload or pr review --comment in full; here structured.

    # Slice 3: real skill step integration test (temp SKILL with python block calling gh_evidence tool via registry)
    import tempfile
    temp_skill = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, dir='.', encoding='utf-8') as f:
            f.write("""---
name: p4-gh-skill-test
---
## Procedure
```python
from src.platform.tools.registry import get_registry
reg = get_registry()
res = reg.invoke("gh_evidence", action="create-issue", title="P4 real skill evidence", body="Dry-run via tool in SKILL step.")
print("GH-TOOL-IN-SKILL:", res.get("status"))
```
""")
            temp_skill = f.name
        from src.platform.orchestration.executor import ProceduralSkillExecutor
        execr = ProceduralSkillExecutor(workspace_root=".")
        res = execr.execute(temp_skill)
        py_evs = [e for e in res.evidence if e.step_type == "python"]
        has_gh = any("GH-TOOL-IN-SKILL" in (e.stdout or "") for e in py_evs)
        print(f"real-skill gh via tool: #py-evs={len(py_evs)}, has-gh-tool={has_gh}, status={res.status}")
        assert len(py_evs) >= 1 and has_gh
        print("  PASS: real SKILL step using gh_evidence via registry/tool call (P4 integrate)")
    finally:
        if temp_skill and Path(temp_skill).exists():
            Path(temp_skill).unlink()
    return 0


if __name__ == "__main__":
    sys.exit(main())

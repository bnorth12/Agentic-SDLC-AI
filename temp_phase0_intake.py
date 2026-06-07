#!/usr/bin/env python
"""Phase 0 Intake: Run mandatory upfront skills for PS-to-IDE Transition Plan.
This follows the plan's own rules: always start with skills for requirements, architecture, hierarchy, governance, traceability, verification, check-work.
"""
import sys
from pathlib import Path
ROOT = Path(".").resolve()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.platform.orchestration.executor import run_procedural_skill
from src.platform.tools.gate_evidence_bundler import create_gate_evidence_bundle, bundle_to_markdown

print("=== PHASE 0: GOVERNED INTAKE FOR PS-to-IDE TRANSITION PLAN ===")
print("Running required upfront skills (as per plan Phase 0 and project charter).")

skills_to_run = [
    "ide-requirements-implementation-auditor",
    "ide-architecture-design-disposition",
    "ide-hierarchy-taxonomy-steward",
    "ide-governance-policy-compiler",
    "ide-source-to-evidence-traceability",
    "ide-verification-coverage",
    "ide-check-work-commit",
]

results = []
sources = []

for sk in skills_to_run:
    print(f"\n--- Running {sk} ---")
    try:
        res = run_procedural_skill(sk, workspace_root=".")
        entry = {
            "skill": sk,
            "status": res.get("status"),
            "declared_tools": res.get("outputs", {}).get("declared_tools", []),
            "required_scopes": res.get("outputs", {}).get("required_scopes", []),
            "tool_registry_available": res.get("outputs", {}).get("tool_registry_available"),
        }
        results.append(entry)
        sources.append({"type": "phase0_skill", "id": sk, "result": res})
        print(f"Status: {entry['status']}")
        print(f"Declared tools: {entry['declared_tools']}")
        print(f"Required scopes: {entry['required_scopes']}")
    except Exception as e:
        entry = {"skill": sk, "status": "error", "error": str(e)[:200]}
        results.append(entry)
        sources.append({"type": "phase0_skill", "id": sk, "result": entry})
        print(f"Error: {str(e)[:200]}")

print("\n=== Phase 0 Summary ===")
for r in results:
    print(f"  {r['skill']}: {r['status']}")

# Create evidence bundle for this intake (G0_wave_charter or G1)
try:
    bundle = create_gate_evidence_bundle("G0_wave_charter", sources)
    md = bundle_to_markdown(bundle)
    print(f"\nP5 Evidence Bundle created for G0_wave_charter (id approx {getattr(bundle, 'bundle_id', 'N/A')[:8]})")
    print("Bundle markdown head (first 500 chars):")
    print(md[:500])
except Exception as be:
    print(f"Bundle creation note: {be}")

print("\n=== Recommendations for updates (to be applied in this micro-batch) ===")
print("1. Mark Phase 0 complete in PS_IDE_TRANSITION_PLAN.md and invocation record.")
print("2. Add tiny anchor in matrix X PS-IDE-TRANSITION-001 and invocation.")
print("3. Confirm baseline smoke still passes.")
print("4. Proceed to Phase 1 only after this evidence.")

print("=== PHASE 0 INTAKE COMPLETE ===")
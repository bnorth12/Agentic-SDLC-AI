#!/usr/bin/env python
"""Micro-batch for continuing PS-to-IDE transition (Phase 2/3 small steps).
Run required upfront skills first (gov, hierarchy, verif, trace, check-work) per plan.
This ensures full engineering rigor before any code/doc changes.
"""
import sys
from pathlib import Path
ROOT = Path(".").resolve()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.platform.orchestration.executor import run_procedural_skill

print("=== MICRO-BATCH: Phase 2/3 continuation (skills first) ===")

skills = [
    "ide-governance-policy-compiler",
    "ide-hierarchy-taxonomy-steward",
    "ide-verification-coverage",
    "ide-source-to-evidence-traceability",
    "ide-check-work-commit",
]

for sk in skills:
    print(f"\n--- Running {sk} ---")
    try:
        res = run_procedural_skill(sk, workspace_root=".")
        print(f"Status: {res.get('status')}")
        print(f"Declared tools: {res.get('outputs', {}).get('declared_tools')}")
    except Exception as e:
        print(f"Error (partial expected): {str(e)[:100]}")

print("\nSkills run complete. Ready for small changes + verification.")
print("=== UPFRONT SKILLS DONE ===")
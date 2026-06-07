#!/usr/bin/env python
"""Phase 1 Batch 1: Requirements & Functional Decomposition small batch.
Run required skills first (hierarchy, gov, verification, traceability) on the transition artifacts.
Then apply small updates to matrix (expand decomp in X PS-IDE-TRANSITION-001) and plan.
This is a tiny verifiable batch.
"""
import sys
from pathlib import Path
ROOT = Path(".").resolve()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.platform.orchestration.executor import run_procedural_skill

print("=== PHASE 1 BATCH 1: REQUIREMENTS & DECOMP (small testable batch) ===")
print("Running required upfront skills first (per plan and rules).")

skills = [
    "ide-hierarchy-taxonomy-steward",
    "ide-governance-policy-compiler",
    "ide-verification-coverage",
    "ide-source-to-evidence-traceability",
]

for sk in skills:
    print(f"\n--- {sk} (for Phase 1 decomp/reqs) ---")
    try:
        res = run_procedural_skill(sk, workspace_root=".")
        print(f"Status: {res.get('status')}")
        print(f"Declared: {res.get('outputs', {}).get('declared_tools')}")
    except Exception as e:
        print(f"Error: {str(e)[:100]}")

print("\nSkills run complete for this batch. Now applying small decomp/req updates to artifacts (in subsequent tool calls).")
print("=== BATCH SKILL PREP COMPLETE ===")
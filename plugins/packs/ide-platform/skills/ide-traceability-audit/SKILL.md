---
name: ide-traceability-audit
description: >
  Generalized skill for auditing repo-native traceability: orphan IDs, broken links, etc. for the agentic IDE platform.
  Primary for Traceability Audit. Generalizes traceability-audit-farmrtk and related assets. Audits traceability in generalized agents/skills, structure changes, and self-hosted evidence.
metadata:
  short-description: "Repo traceability audit for IDE generalized assets and structure"
  agent: ide-traceability-audit
  gates: [G1_traceability, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-traceability-audit

**Agents:** Traceability Audit (primary, from farmrtk), Source-to-Evidence Traceability Auditor, Requirements Baseline Steward, Refactoring Agent  
**Parent:** [ide-traceability-audit (to be generalized)] · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) · Structural Refactor Execution Plan

## Purpose
Audit repo-native traceability: orphan REQ/ work item IDs, broken links in docs, etc. for the IDE (generalized agents/skills, structure changes, evidence). Ensure no orphans in the new layout or generalized content.

## When to Invoke
- Quarterly or before major baselines (G5).
- After bulk changes or generalization.
- Staged for pre-commit.
- User: "traceability audit for structure", "/ide-traceability-audit".

## Inputs
- Repo scope, generalized artifacts, structure records, evidence.

## Procedure

1. Full repo scan (adapt original PS1 or script to check generalized in ide-platform, structure, living docs, legacy quarantine for orphans/broken links).
2. Staged-only supplement.
3. Fix orphan IDs or broken links in docs, plans, or generalized files.
4. Update matrices or indexes in the same "PR" (changes) as implementation.
5. Re-run until clean or documented.
6. Enforce with flag if needed.

## Outputs
- Audit findings (WARN/FAIL lines for orphans, broken links).
- Remediation for the execution plan.
- Evidence for G1, G4, G5.

## PowerShell / GitHub Native Emphasis
```powershell
# Adapted for IDE
pwsh -File tools/ci/ide-traceability-audit.ps1 -Scope "Structure-Refactor"

# Enforce
$env:IDE_ENFORCE_CHECKS = "1"
pwsh -File tools/ci/ide-traceability-audit.ps1
```

## Guardrails
- Local-only.
- Explicit fixes.

## Generalization & IDE-Specific Notes
- Removed FarmRTK-specific (REQ/TC, cad, etc.).
- Added focus on IDE: orphans in generalized agents/skills, structure docs, living plans, evidence from procedures, self-hosting.
- Supports the refactor by cleaning traceability in the new layout.

## Related
- Gates: G1, G4, G5.
- Agents: Traceability Audit + other traceability, Refactoring.
- Self-referential for the platform's traceability during generalization and structure work.
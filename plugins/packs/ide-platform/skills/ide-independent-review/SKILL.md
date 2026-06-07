---
name: ide-independent-review
description: >
  IDE platform EIRC unified review — commit, change, and milestone gate modes for
  generalized content, matrix updates, tooling changes, and self-hosting work.
  Generalizes independent-review-farmrtk. Extends prior check-work patterns.
  Use for EIRC review, milestone gate, or pre-merge check on IDE platform changes.
metadata:
  short-description: "EIRC commit/change/milestone review for IDE platform"
  agent: independent-review-committee
  gates: [G1_traceability, G4_independent_review]
  maturity: M0+
---

# ide-independent-review

**Agent:** Independent Review Committee (EIRC, generalized)  
**Parent:** [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) (Cross XGEN) · [IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](../../../docs/charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md)

## Purpose
Orchestrates independent review tiers for the IDE platform: pre-change/commit scans (hierarchy, matrix links, new tool usage), merge/pre-push enforcement (optional), and milestone gate reviews (full XGEN coverage, self-hosting hygiene, G4 evidence). Ensures changes to generalized skills, the matrix, executor/tools, and plans are reviewed for traceability and quality.

## When to Invoke
- Before committing changes to generalized SKILL.md, the matrix, §5, or new tools (via hooks or explicit).
- Pre-merge on XGEN PRs (enforce with flag for critical batches).
- At wave/milestone end (e.g., after FarmRTK batch 3) for G4 checklist scan.
- User: "EIRC review for new ide-tool", "milestone check on matrix extension".
- As part of ide-structural-refactoring Phase 5 or before G4.

## Modes

| Mode | When | Blocking |
|------|------|----------|
| `commit` / `change` | pre-commit or pre-change on generalized content/matrix/tools | No (M0–M1 default) |
| `merge` | pre-merge / PR to main on XGEN or structural | Optional (set flag) |
| `milestone` | Wave end, after batch (e.g., full FarmRTK) | Human sign-off; advisory script |

## Procedure

### Commit/Change Tier
```powershell
pwsh -File tools/ci/ide_check_independent_review.ps1 -Mode change
```

### Merge Tier (enforce optional)
```powershell
$env:IDE_ENFORCE_MERGE_CHECKS = "1"
pwsh -File tools/ci/ide_check_independent_review.ps1 -Mode merge
```

### Milestone Tier
```powershell
pwsh -File tools/ci/ide_check_independent_review.ps1 -Mode milestone -Gate M-G5
```

Gates: M-G0 to M-G5 mapped to matrix rows and wave progress (see references in matrix).

## Outputs
- Reports under evidence/ide-reviews/{commit,merge,milestone}-*.md
- Updated matrix with review findings or waivers.
- Evidence bundle for G4.

## Escalation
- FAIL at merge enforce on critical generalized item → Chief Engineer or waive.
- Milestone FAIL on traceability → Program Manager reschedules; do not advance.
- Repeated issues → update using ide-process-audit or ide-kpi-drift-analyst.

## Generalization & IDE-Specific Notes
- Stripped FarmRTK-specific (CAD, SCAD, firmware, .farmrtk/reviews paths).
- Focused on IDE platform: changes to generalized agents/skills (batch 3), matrix extensions, L2 executor + ide_core tools, self-hosting artifacts, §5 updates.
- Explicit integration with the traceability matrix (reviews feed matrix rows).
- PowerShell + gh for review reports on generalization PRs.
- Now the unified EIRC for the reboot, building on prior check-work and MATM independent-review-orchestrator.

## Related Platform Artifacts
- Gates: G1, G4.
- Tools: ide_core (hierarchy validation in reviews), the matrix.
- Complements: ide-check-work-commit (subset), ide-process-audit, ide-source-to-evidence-traceability.
- Used in pre-merge for batch 3 and future XGEN; updates IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md (Cross XGEN rows).

---
name: ide-check-work-commit
description: >
  Light pre-commit / pre-XGEN-change scan for the IDE platform: orphan requirements
  in generalized artifacts, broken links in docs/matrix, hierarchy metadata on
  new .agent.md/SKILL.md, manifest drift. Informational at early maturity;
  can be enforced. Generalizes check-work-commit-farmrtk.
metadata:
  short-description: "Light EIRC-style commit / change check for IDE generalization work"
  agent: independent-review-committee
  gates: [G1_traceability, G4_independent_review]
  maturity: M0+
---

# ide-check-work-commit

**Agent:** Independent Review Committee (EIRC, generalized)  
**Tier:** Change / Pre-Commit — informational by default (enforceable via flag)  
**Parent:** [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) (Cross XGEN) · [IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](../../../docs/charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md)

## Purpose
Perform a lightweight, fast scan before committing generalization changes, structural updates, or matrix edits. Catches orphan links in the traceability matrix, missing hierarchy on new generalized items, manifest drift in ide-platform, and broken cross-references. Non-blocking at M0-M1 unless FARMRTK_ENFORCE_CHECKS (or equivalent IDE flag) is set.

## When to Invoke
- Before `git commit` on changes to generalized SKILL.md/.agent.md, the matrix, §5, or pack manifests (via hooks or explicit).
- After using the new tools (ide_core.py) to generate or edit artifacts.
- User: "pre-change check", "EIRC scan for XGEN PR", "validate matrix before commit".
- In CI for generalization PRs.

## Inputs
- Staged or specified changes (generalized files, matrix, plans).
- Current ide-platform manifest and layer index.
- The traceability matrix itself.

## Procedure

### 1. Stage & Run (generalized)
```powershell
# From repo root, for changes related to ide-platform or matrix
pwsh -File tools/ci/ide_check_work.ps1 -Mode change -Scope "ide-platform + matrix"
```

Or for simulation:
```bash
# Git Bash equivalent
bash tools/ci/ide_check_work.sh change
```

### 2. Review Report
- Read report (e.g., evidence/ide-checks/change-*.md).
- Focus on: missing hierarchy (use validate_hierarchy_metadata tool), orphan rows in the matrix, broken links to §5 or invocation records.

### 3. Remediate (non-blocking by default)
- Fix high-confidence issues (e.g., add missing Parent links or run the hierarchy validator).
- Log warnings for trend tracking (KPI equivalent).

### 4. Optional Enforcement
- Set flag to make blocking for critical generalization PRs.

## Scope
See references in the matrix for current high-priority generalized content (Tranche 2 + new FarmRTK).

## Escalation
- Blocking issues in matrix or new generalized artifacts → Refactoring Agent before merge.
- Repeated drift → ide-process-audit + update to WAVE charter.

## Generalization & IDE-Specific Notes
- Stripped FarmRTK CAD/SCAD/PARAMS-specific checks.
- Added IDE-native: hierarchy validation on .agent.md/SKILL.md using new tools, matrix link integrity, ide-platform manifest coherence, references to L0-L8 and §5.
- PowerShell + gh friendly for PR checks.
- Supports the self-hosting model by keeping the architecture surface clean during active XGEN.

## Related Platform Artifacts
- Gates: G1, G4.
- Tools: ide_core (validate_hierarchy_metadata, read_ide_artifact).
- Complements: ide-repo-audit, ide-process-audit, the traceability matrix.
- Used in pre-merge for changes touching generalized content or the matrix.

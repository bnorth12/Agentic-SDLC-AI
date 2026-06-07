---
name: ide-risk-register
description: >
  Maintain and audit the risk register for IDE platform generalization, tooling,
  self-hosting, executor maturity, and layer work. Generalizes risk-register-farmrtk.
  Use for risk audit, mitigation planning during XGEN waves (including this FarmRTK batch),
  or before G5.
metadata:
  short-description: "Risk register audit and maintenance for IDE platform"
  agent: risk-manager
  gates: [G1_traceability, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-risk-register

**Agent:** Risk Manager (generalized)  
**Parent:** [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) (Cross XGEN / XSELF) · [IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](../../../docs/charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md)

## Purpose
Audit and maintain risks specific to the IDE platform reboot and self-hosting: generalization debt (FarmRTK/MATM batches), tooling/executor maturity (new ide_core and L2 executor), matrix traceability gaps, legacy migration, doc hygiene. Ensures risks are tracked with owners, mitigations, and links to the matrix and wave plans.

## When to Invoke
- End of XGEN tranche or after significant tooling changes (e.g., new ide_core functions, executor integration, batch 2/3).
- During WAVE-02 planning or closeout.
- Monthly or when new risks emerge from audits (e.g., from ide-process-audit or matrix review).
- User: "update IDE risk register", "audit risks for current FarmRTK batch".
- As part of ide-structural-refactoring Phase 5 or Planning Agent portfolio review.

## Inputs
- The traceability matrix, layer index, recent invocation records and audit reports.
- Generalized artifacts and new code (executor, ide_core tools).
- Previous risk passes and WAVE charter.

## Procedure

### 1. Run Risk Audit (generalized)
```powershell
pwsh -File tools/ci/ide_risk_register_audit.ps1 -Scope "XGEN + tools + self-hosting + batch-2"
```

### 2. Ensure Risk Hygiene
- Each open risk has owner, mitigation, likelihood/impact ratings.
- Link to specific matrix rows or §5 sections (e.g., "L2 executor pending full test" -> TOOL-001 row; "FarmRTK batch 2 coverage" -> specific XGEN rows).
- Feed into program metrics / ide-kpi-drift-analyst.

### 3. Escalate High-Impact Risks
- Escalate to Planning Agent for wave re-sequencing or Refactoring Agent for immediate mitigation (e.g., using new tools for faster generalization).
- Document trades via ide-decision-record.

### 4. Baseline
- Update register and matrix revision when risks are accepted or closed.

## Outputs
- Updated risk register with IDE-specific entries (including this batch).
- Linked evidence in the matrix.
- Input to G4/G5.

## Escalation
- High-impact generalization or tooling risks without mitigation → Planning Agent + Chief Engineer.
- Repeated matrix traceability risks → update audit process or tools.

## Generalization & IDE-Specific Notes
- Stripped FarmRTK project-specific risks (hardware, firmware, specific BOM).
- Focused on IDE reboot risks: XGEN progress (this FarmRTK batch 2), new L2/L4 components (executor + ide_core tools), self-hosting loops, legacy quarantine.
- Explicit integration with the traceability matrix as the primary risk visibility surface.
- PowerShell + gh for risk PRs during generalization.
- Used to track risks from using the new tools themselves during batch execution.

## Related Platform Artifacts
- Gates: G1, G4, G5.
- Tools: ide_core, program-metrics equivalents.
- Used by: ide-kpi-drift-analyst, ide-portfolio-planning, ide-structural-refactoring closeout.
- Lives in / updates the IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md (Cross rows).

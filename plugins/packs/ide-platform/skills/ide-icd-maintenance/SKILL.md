---
name: ide-icd-maintenance
description: >
  Maintain and audit interface control documents (ICD) and layer wiring for the
  IDE platform. Covers interfaces between L2 executor, L4 tools (ide_core), pack
  manifests, gate evidence formats, and the traceability matrix. Generalizes
  icd-maintenance-farmrtk.
metadata:
  short-description: "ICD and layer interface audit for IDE platform"
  agent: systems-engineer
  gates: [G1_traceability, G2_icd_interfaces, G4_independent_review]
  maturity: M0+
---

# ide-icd-maintenance

**Agent:** Systems Engineer (generalized)  
**Parent:** [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) (L2/L3/L4 + Cross) · [IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](../../../docs/charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md)

## Purpose
Audit and maintain interface definitions between IDE platform layers and components (e.g., L2 executor calling L4 ide_core tools, pack manifests for discovery, gate evidence formats, matrix structure for traceability). Ensures consistency for generalized agents/skills and new tooling. Supports self-hosting by keeping the architecture surface's "wiring" clean and traceable.

## When to Invoke
- After adding or changing generalized content that affects interfaces (e.g., new tool in ide_core, executor step formats, matrix schema updates).
- Before or during WAVE-02 execution or tranche closeout when L2/L4 contracts may change.
- When introducing new evidence formats or viewer registrations.
- User: "audit ICD for new L2 tools", "check matrix <-> executor interfaces".
- As part of ide-structural-refactoring Phase 2/3 or G2 gate.

## Inputs
- Current IDE_REFACTOR_PLAN §5, the traceability matrix, FRAMEWORK_DECOMPOSITION.
- Generalized SKILL.md/.agent.md and tool implementations (ide_core).
- Gate registry for evidence formats.

## Procedure

### 1. Run ICD Audit (generalized)
```powershell
pwsh -File tools/ci/ide_icd_audit.ps1 -Scope "L2-executor + L4-tools + matrix"
```

### 2. Fix Interface Gaps
- Ensure missing "wiring" docs or contracts are updated (e.g., tool call contracts in matrix rows, executor evidence format in §5).
- Link affected decisions via ide-decision-record.
- Pair with domain wiring if relevant, but focus on platform layers and matrix.

### 3. Traceability Update
- Update the matrix with any new interface rows or changes.
- Run validate_hierarchy_metadata on affected artifacts.
- Document trades in ADR using ide-decision-record.

### 4. Close with Evidence
- Verify all generalized items have consistent interface refs in their Parents and the matrix.

## Outputs
- Updated ICD / interface docs or matrix sections.
- Audit report with gaps and fixes.
- Evidence for G1/G2/G4.

## Escalation
- Inconsistent layer interfaces in generalized skills → Refactoring Agent + matrix update.
- Missing tool contracts after new ide_core addition → L2/L4 tooling work.

## Generalization & IDE-Specific Notes
- Removed FarmRTK-specific ICD (SYS-DOC-04, wiring diagrams for hardware/electronics).
- Focused on IDE platform interfaces: executor <-> tools (ide_core), packs <-> loader, matrix <-> generalized artifacts, L2-L4 contracts for self-hosting.
- Explicit support for documenting and auditing the new L2 executor and ide_core tools (this batch).
- PowerShell + gh for interface change PRs during generalization.
- Directly maintains the traceability matrix as the "ICD" for the architecture.

## Related Platform Artifacts
- Gates: G1, G2, G4.
- Tools: ide_core (validate for allocation, read/write for ICD artifacts).
- Used by: ide-structural-refactoring, the matrix itself, WAVE-02 charter.
- Updates IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md (L2/L4/Cross rows).

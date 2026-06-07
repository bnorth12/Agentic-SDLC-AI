---
name: ide-decision-record
description: >
  Scaffold and maintain architecture decision records (ADRs) for the IDE platform.
  Use for documenting trade studies, layer decisions, tool/executor design choices,
  generalization approaches, and self-hosting architecture. Generalizes decision-record-farmrtk.
metadata:
  short-description: "ADR scaffold for IDE platform decisions and trade studies"
  agent: systems-engineer
  gates: [G1_traceability, G2_icd_interfaces, G4_independent_review]
  maturity: M0+
  # Priority 1 tool registry declaration (for L2 executor + permission model)
  tools: [validate_hierarchy_metadata, read_ide_artifact]
  required_scopes: [ide.hierarchy, ide.fs.read]
---

# ide-decision-record

**Agent:** Systems Engineer (generalized)  
**Parent:** [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) (Cross XGEN / L2-L4) · [IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](../../../docs/charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md)

## Purpose
Provide a standardized way to document architecture decisions, trade studies, and rationale for the agentic IDE platform. Covers choices around L0-L8 decomposition, new L2 executor and ide_core tools, generalization strategies for imported assets, legacy handling, and self-hosting loops. Ensures decisions are traceable to requirements, the matrix, and layer work packages.

## When to Invoke
- When making significant structural or generalization decisions (e.g., new tool in ide_core, executor wiring, FarmRTK batch scoping, matrix extensions).
- Before or after updating the traceability matrix or layer index for a decision that affects hierarchy or interfaces.
- During WAVE chartering, tranche closeout, or G2 interface reviews.
- User: "create ADR for L2 tool integration", "document decision on custom GUI vs PowerShell-first".
- As part of ide-structural-refactoring Phase 3 (disposition) or 4 (evidence).

## Inputs
- Current state of generalized artifacts, the matrix, IDE_REFACTOR_PLAN §5, FRAMEWORK_DECOMPOSITION.
- Request from Chief Engineer, Refactoring Agent, or wave charter.
- Existing decisions or related ADRs (if any).

## Procedure

### 1. Scaffold New ADR (generalized)
```powershell
# Generalized scaffold (adapt from original Tools/ci/scaffold_adr.ps1 logic)
pwsh -File tools/ci/ide_scaffold_adr.ps1 -AdrId ADR-IDE-001 -Title "L2 executor and ide_core tools integration for self-hosting"
```

### 2. Populate Decision Record
- Link to relevant requirements (from ide-structure-requirements-baseline or matrix rows).
- Reference affected layers (e.g., L2 Orchestration, Cross XGEN) and specific matrix rows.
- Include options considered, rationale, consequences for the matrix, plans, and self-hosting.
- Update traceability: add link in the matrix row or §5 if it affects decomposition.

### 3. Reference and Trace
- Link the ADR from the relevant generalized SKILL.md (e.g., in ide-decision-record usage notes) or invocation record.
- Run `validate_hierarchy_metadata` (from ide_core tools) on the ADR if it affects layer allocation.
- Pair with `ide-source-to-evidence-traceability` to ensure the decision closes a chain.

### 4. Accept and Baseline
- Once accepted, reference from architecture docs or layer index.
- Bump matrix revision if the decision impacts XGEN rows.

## Outputs
- ADR file (e.g., docs/decisions/ADR-IDE-xxx.md) with full traceability table.
- Updated links in matrix, plans, and affected generalized artifacts.
- Evidence suitable for G1/G2/G4.

## Escalation
- Decision impacts multiple layers without clear hierarchy update → Chief Engineer + Refactoring Agent.
- Missing links in matrix after ADR → update matrix as part of the wave.

## Generalization & IDE-Specific Notes
- Stripped all FarmRTK/CAD/firmware-specific trade study examples (e.g., case selection for hardware).
- Made fully driven by IDE layers, the traceability matrix, and self-hosting needs.
- Explicit support for documenting choices around the new tools (ide_core), executor, and XGEN batches (including this FarmRTK batch 2).
- PowerShell + gh examples for creating ADRs as part of generalization PRs.
- Decisions now feed directly into the IDE_ARCHITECTURE_TRACEABILITY_MATRIX and §5.

## Related Platform Artifacts
- Gates: G1, G2, G4.
- Tools: ide_core (validate_hierarchy_metadata for decision allocation).
- Used by: ide-structural-refactoring (Phase 3), Planning Agent wave planning, matrix maintenance.
- Updates IDE_REFACTOR_PLAN §5 and the traceability matrix (Cross rows).

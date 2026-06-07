---
name: ide-test-authoring
description: >
  Scaffold and maintain test cases (TC-xxx style) and artifact directories for
  the IDE platform. Use for authoring tests for generalized skills, the L2
  executor, new tools (ide_core), matrix validation, and self-hosting features.
  Generalizes test-authoring-farmrtk.
metadata:
  short-description: "Test case scaffold for IDE platform capabilities"
  agent: test-engineer
  gates: [G1_traceability, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-test-authoring

**Agents:** System Test Engineer, Software Test Engineer (generalized)  
**Parent:** [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) (L2/L4 + Cross XGEN/XSELF) · [IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](../../../docs/charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md)

## Purpose
Provide a standardized way to author and maintain test cases for the agentic IDE platform. Covers testing generalized agents/skills (MATM/FarmRTK batches), the procedural executor, ide_core tools, traceability matrix integrity, hierarchy validation, and self-hosting scenarios. Ensures test coverage is traceable to requirements, the matrix, and layer work packages.

## When to Invoke
- When adding or changing generalized content (new FarmRTK skills, tool additions, executor updates).
- After structural changes or matrix extensions to add corresponding tests.
- Before G5 baseline or wave closeout to verify coverage.
- User: "scaffold test for new ide-tool", "author TC for executor integration".
- As part of ide-structural-refactoring Phase 5 (validation) or after using new tools.

## Inputs
- Parent requirements or work packages from the traceability matrix or IDE_REFACTOR_PLAN §5.
- Existing test templates or artifacts in tests/ or evidence/.
- The L2 executor, ide_core tools, or specific generalized SKILL.md to test against.

## Procedure

### 1. Scaffold New Test Case (generalized)
```powershell
# Generalized scaffold (adapt from original Tools/ci/scaffold_tc.ps1 logic)
pwsh -File tools/ci/ide_scaffold_tc.ps1 -TcId TC-IDE-001 -ParentReq "TOOL-001 or matrix row" -Method "Test via executor"
```

### 2. Link and Populate
- Link to parent REQ/WP (e.g., from matrix: L2 executor row, Cross XGEN).
- Create artifact dir under evidence/ or tests/ for the TC.
- Add row to relevant BACKLOG equivalent (layer index or project-plan) and verification plan.
- Author steps that exercise the feature (e.g., run executor on the skill, call validate_hierarchy_metadata, check matrix links).

### 3. Execute and Log
- Run on "bench" (local or via executor).
- Log results in execution-log.md style, with evidence bundle.
- Run related audits (e.g., ide-source-to-evidence-traceability, ide-hierarchy-taxonomy-steward).

### 4. Close with Traceability
- Update the matrix with test coverage note for the row.
- Reference in the generalized skill's "Verification" section if applicable.

## Outputs
- New TC file and artifacts dir.
- Updated BACKLOG/layer index, matrix with coverage.
- Evidence suitable for G1/G4/G5 (test results linked to matrix).

## Escalation
- Test failure on core generalized artifact or tool → Refactoring Agent + fix before next wave.
- Missing traceability in TC → update using ide-source-to-evidence-traceability.

## Generalization & IDE-Specific Notes
- Stripped all FarmRTK-specific (CAD, firmware, rover, SYS-DOC paths).
- Made fully driven by IDE layers, the matrix, executor/tools, and self-hosting.
- Explicit support for testing the new L2 executor, ide_core tools (e.g., validate_hierarchy_metadata), and Tranche 2/3 generalized content.
- PowerShell + gh examples for test PRs and evidence attachment.
- Now core to maintaining coverage in the IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md.

## Related Platform Artifacts
- Gates: G1, G4, G5.
- Tools: ide_core (validate_hierarchy_metadata can be exercised in tests), the L2 executor.
- Used by: ide-structural-refactoring (validation), ide-verification-coverage, Planning Agent wave closeout.
- Updates the IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md (adds test coverage notes to rows).

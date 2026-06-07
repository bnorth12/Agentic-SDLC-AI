---
name: ide-verification-coverage
description: >
  Generalized skill for assessing and improving requirement-to-verification coverage for the agentic IDE platform.
  Primary for Verification Coverage Planner. Generalizes verification-coverage-planner (MATM),
  validation-plan-farmrtk, test-authoring-farmrtk, and related traceability/verification assets.
  Critical early to plan verifications in parallel with generalization, structural work, and IDE surface development.
metadata:
  short-description: "Requirement-to-verification linkage and coverage for IDE layers, editors, skills, agents, and structure"
  agent: verification-coverage-planner
  gates: [G1_traceability, G3_verification_plan, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-verification-coverage

**Agents:** Verification Coverage Planner (primary), Requirements Baseline Steward, Architecture/Design Disposition Planner, Traceability Manager, Planning Agent  
**Parent:** [verification-coverage-planner.agent.md](../../../agents/ide-platform/verification-coverage-planner.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md)

## Purpose
Drive complete, auditable, and executable verification linkage for every governed requirement and capability of the agentic IDE (including its own editors, viewers, agents as artifacts, skills, layers L0-L8, repo structure, functional decomposition, and self-hosting). This skill ensures we plan and track verifications from the start of work (generalization, structural refactors, surface development) rather than as an afterthought.

## When to Invoke
- During or immediately after requirements baselining and architecture/design disposition for any IDE work.
- Before and during generalization of imported agents/skills batches.
- When planning or reviewing structural/repo changes or functional decomp.
- At wave/sprint intake and before closeout or baseline gates.
- User: "verify coverage for the IDE structure changes", "plan verifications for agent/skill editors", "/ide-verification-coverage".

## Inputs
- Requirements baselines and hierarchy metadata (from ide-requirements-baseline).
- Architecture/design workpacks and dispositions (from ide-architecture-design-disposition).
- Current work items (generalization targets, proposed structural moves, new surfaces).
- Existing tests, evidence artifacts, verification strategy references, traceability matrix.
- Gate registry (especially G3 verification plan entries).

## Procedure

### 1. Map Requirements to Verification
For each requirement or capability slice:
- Identify the linked architecture/design target.
- Map to concrete verification method (test, demonstration, inspection, analysis) and artifact (e.g., test file, evidence bundle, viewer output, compliance report).
- Confirm objective pass criteria.
- IDE-specific: Verify coverage for editors (e.g., can edit .agent.md with RRA preview?), viewers (e.g., source-to-evidence graph renders correctly?), skill execution (procedural vs ACP), pack loading, PowerShell/GitHub integration, self-hosting scenarios.

### 2. Identify Gaps and Weaknesses
- Flag requirements with no verification, weak methods (e.g., "it works on my machine"), or missing artifacts.
- Assess risk concentration (e.g., many L4 plugin host items without verification, or structural changes without tests for editor compatibility).
- Use hierarchy to roll up coverage at layer and decomposition level.

### 3. Produce Coverage Report and Backlog
- Calculate coverage ratios (overall and by layer/priority).
- Prioritize remediation actions by severity, layer impact, and dependency on other work.
- Recommend specific verification tasks that can run in parallel (e.g., "add test for generalized requirements-baseline skill in ide-platform pack").
- For repo structure work: Include verification that the new layout supports the IDE vision (e.g., agents/skills are easily editable in the future agent/skill editors, no legacy pollution in active surfaces).

### 4. Update Traceability and Gates
- Refresh the traceability matrix with new linkages.
- Propose or update G3 verification plan entries in the gate registry.
- Ensure handoff to independent review (G4) and baseline (G5).

### 5. PowerShell / GitHub Native Steps (examples)
```powershell
# Example (to be implemented as reusable skill fragment or ACP action)
pwsh -File tools/verification/coverage.ps1 -Scope "L0-Editors L4-PluginHost Cross-Structure" -Baseline docs/ide-structure-requirements-baseline.md -Output evidence/verification-coverage-$(Get-Date -Format yyyyMMdd).md

# Log findings as GitHub issue for the wave
gh issue create --title "Verification gaps for IDE repo structure" --label verification,compliance,ide-platform --body-file evidence/verification-coverage-*.md
```

### 6. Support Iteration
- As new architecture/designs or requirements emerge (common in early IDE development), re-run to update coverage and backlog.
- Tie directly to compliance (ide-governance-policy-compiler) and review processes.

## Outputs
- Verification coverage report with ratios, missing-link findings, and risk assessment.
- Prioritized remediation backlog (actionable for the Refactoring Agent, implementers, or future test authoring skills).
- Updated traceability matrix slices and gate recommendations.
- Evidence suitable for G1, G3, G4, G5.

## Escalation
- Critical unverifiable requirements or high risk concentration in foundational layers/surfaces → Planning Agent for re-sequencing + Architecture/Design Disposition Planner.
- Compliance violations in verification plans → Governance Policy Compiler + Independent Review (G4).
- Gaps that affect self-hosting or repo structure usability → Refactoring Agent for immediate remediation.

## Generalization & IDE-Specific Notes
- Removed product-specific assumptions (e.g., FarmRTK hardware verification, MATM threat model pipelines).
- Added explicit coverage for the IDE's core innovations: agents and skills as editable first-class artifacts (with editors and viewers), L0-L8 layer decomposition, pack-based delivery, hybrid orchestration, PowerShell + GitHub native, and self-hosting (verifying that the platform can govern its own development using the same tools).
- Strong support for verifying functional decomposition and structural changes (e.g., does the new repo layout make agent/skill editing natural?).

## Related Platform Artifacts
- Gates: G1 (traceability), G3 (verification plan), G4, G5.
- Agents: Verification Coverage Planner (primary), Requirements Baseline Steward, Architecture/Design agents, Compliance agents.
- Used in parallel with generalization (XGEN) and structural work in early waves. This skill is self-referential — we use it to verify coverage of the IDE's own requirements and architecture.
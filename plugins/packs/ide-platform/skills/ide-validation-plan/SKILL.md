---
name: ide-validation-plan
description: >
  Generalized skill for producing and maintaining validation & verification plans, coverage strategies,
  and evidence requirements for the agentic IDE platform (including generalization tranches and structural work).
  Generalizes validation-plan-farmrtk with full IDE layer, self-hosting, and XGEN awareness.
metadata:
  short-description: "V&V plans, coverage, and verification strategy for IDE layers, generalized agents/skills, and self-hosting"
  agent: verification-validation (composed)
  gates: [G1_traceability, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-validation-plan

**Agents:** V&V Lead (composed), Verification Coverage Planner, IDE Requirements Implementation Auditor, Refactoring Agent, Planning Agent  
**Parent:** [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) · [LAYER_WORK_PACKAGE_INDEX.md](../../../docs/charter/ide-refactor/LAYER_WORK_PACKAGE_INDEX.md) · `agents/platform/invocations/remaining-xgen-refactoring-session.md`

## Purpose
Produce and maintain validation & verification (V&V) plans, coverage strategies, and evidence requirements tailored to the agentic IDE platform. This includes verification of generalized agents and skills (the remaining XGEN set and FarmRTK batch), structural repo changes, self-hosting exercises (using the generalized items to govern the IDE's own development), layer interface contracts (G2), and overall G5 baseline readiness. The skill ensures that every tranche of IDE integration work has explicit, measurable verification hooks and evidence paths.

## When to Invoke
- After or during generalization of agents/skills (remaining XGEN tranche) to define verification for the new ide-* items and their registration.
- When updating structural execution plans or performing content moves / legacy decisions.
- Before G4 independent review of XGEN or structural work and before G5 baseline.
- When re-baselining verification coverage after self-hosted governance runs.
- User: "produce V&V plan for the remaining XGEN + FarmRTK integration", "define coverage for generalized agents/skills as first-class artifacts", "/ide-validation-plan".
- As a required input to ide-verification-coverage-planner and during ide-structural-refactoring Phase 5.

## Inputs
- Current layered architecture and work packages (IDE_REFACTOR_PLAN, LAYER_WORK_PACKAGE_INDEX, structural-refactor-execution-plan).
- Generalized artifacts (new and prior ide-* in ide-platform) and their traceability chains.
- Requirements baselines and architecture dispositions.
- Gate registry (especially G1, G2, G4, G5) and policy profiles.
- Prior verification coverage reports and evidence bundles.
- Self-hosting context (invocation records, this tranche's Phase 0 audits).

## Procedure

### 1. Scope the V&V Domain
- Identify the items under verification (the 5 pending MATM agents + skills just generalized, priority FarmRTK items, registration/manifest updates, structural plan changes in this tranche).
- Map to layers and Cross concerns (e.g., L4 Plugin Host for pack loading of the new items, Cross XGEN for generalization quality, Cross XSELF for self-hosting).

### 2. Define Verification Methods and Evidence
- For each item or work package, specify:
  - Unit / smoke (e.g., "generalized SKILL.md parses and produces expected frontmatter + procedure steps").
  - Integration (e.g., "new ide-xxx loads from ide-platform pack manifest; hierarchy metadata validated by ide-hierarchy-taxonomy-steward").
  - Self-hosting (e.g., "the item was used in this invocation to govern its own generalization").
  - Gate evidence (G1 traceability chain, G4 independent review packet, G5 baseline contribution).
- Require explicit hierarchy metadata on the verification strategy itself.

### 3. Coverage Strategy & Gaps
- Produce coverage matrix (requirements/WPs → implementation in generalized artifacts → verification methods).
- Identify gaps (e.g., "ide-kpi-drift-analyst.agent.md now exists but verification leg for its use in self-hosting metrics is weak — add smoke in next executor work").
- Recommend minimal viable verification additions (tests, re-audit commands, evidence attachments).

### 4. PowerShell / GitHub Native
```powershell
# Example
pwsh -File tools/vv/plan-ide.ps1 -Scope "Remaining-XGEN-Tranche2 + ide-platform-registration" -LayerIndex docs/charter/ide-refactor/LAYER_WORK_PACKAGE_INDEX.md -Output docs/plans/ide-validation-plan-remaining-xgen-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "V&V plan and coverage gaps for remaining XGEN" --label verification,xgen,ide-platform --body-file docs/plans/ide-validation-plan-*.md
```

### 5. Closeout & Self-Hosting
- Hand the V&V plan to ide-verification-coverage-planner and the Refactoring Agent for Phase 5.
- Re-apply the plan to the platform's own tranche artifacts.
- Update this skill with lessons.

## Outputs
- IDE-specific V&V plan with layer and XGEN scoping.
- Coverage matrix and gap analysis with file/WP references.
- Recommended verification additions and evidence requirements.
- Input suitable for G4/G5 and for the verification coverage planner.

## Generalization & IDE-Specific Notes
- Original FarmRTK validation-plan (hardware/firmware/bench focused) generalized to the agentic IDE: verification of generalized agents/skills as first-class pack content, L0-L8 + Cross decomposition, self-hosting (the V&V for the work that builds the IDE), editor/viewer contracts for the new surfaces, and GitHub-native evidence.
- Removed all product-specific bench/CAD/firmware assumptions (those stay in domain packs).
- Explicitly designed for the current context of completing the remaining set and continuing IDE integration.

## Related Platform Artifacts
- Gates: G1, G2, G4, G5.
- Works with ide-verification-coverage-planner, ide-requirements-implementation-auditor, ide-source-to-evidence-traceability.
- Primary consumer during XGEN closeout and structural execution: Refactoring Agent.
- Future: Integrated with verification viewers and coverage dashboards in the IDE.
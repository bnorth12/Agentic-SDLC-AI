---
name: ide-requirements-baseline
description: >
  Generalized IDE requirements quality, traceability, and intake readiness skill.
  Primary for Requirements Baseline Steward. Generalizes requirements-baseline-steward (MATM),
  requirements-management-farmrtk, traceability-audit-farmrtk, and related traceability assets.
  Must precede architecture/design work, implementation, and structural refactors.
metadata:
  short-description: "Validate and baseline requirements for the agentic IDE (layers, editors, skills, agents, structure)"
  agent: requirements-baseline-steward
  gates: [G0_wave_charter, G1_traceability, G2_icd_interfaces, G4_independent_review]
  maturity: M0+
---

# ide-requirements-baseline

**Agents:** Requirements Baseline Steward (primary), Traceability Manager, Architecture/Design Disposition Planner, Planning Agent  
**Parent:** [requirements-baseline-steward.agent.md](../../../agents/ide-platform/requirements-baseline-steward.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md)

## Purpose
Enforce high-quality, verifiable, traceable, and architecture-linked requirements for the full agentic IDE platform before any design, implementation, generalization, or structural work begins. This skill is the gate that ensures we build the right thing (editors for agents/skills, viewers, hybrid orchestration, packs, repo structure aligned to the IDE model, functional decomposition of L0-L8 layers, etc.).

## When to Invoke
- Start of any wave, feature, or structural refactor that touches IDE capabilities or the repo itself.
- Before architecture/design disposition or implementation of editors, viewers, skill/agent surfaces, orchestration changes, or repo reorganization.
- User request: "baseline requirements for the IDE layers", "review requirements for the structural refactor", "/ide-requirements-baseline".
- At every G0-style intake or before verification planning.

## Inputs
- Existing requirements (PRODUCT_REQUIREMENTS.md + any IDE-specific backlog/plan artifacts).
- Current layered architecture (L0 GUI/Editors/Viewers, L2 Orchestration, L4 Plugin Host for skills/agents, etc.) and gate registry.
- Proposed work (new editor, viewer, generalized skill/agent, pack, repo structure change, functional decomposition).
- Workspace manifests, current traceability matrix, compliance/policy artifacts.

## Procedure

### 1. Quality Scan (SHALL, Verifiability, Criteria)
For every requirement or capability slice:
- Check for clear, unambiguous SHALL language.
- Verify objective, testable acceptance criteria.
- Flag vague terms, compound requirements, or missing "how will we know it works?"
- IDE-specific check: Does it address editors, viewers, agent/skill artifacts as first-class, hybrid execution modes, PowerShell/GitHub native behavior, or layer boundaries (L0-L8)?

### 2. Hierarchy & Functional Decomposition
- Confirm every slice has explicit hierarchy metadata:
  - Parent capability (e.g., "L4 Plugin Host" or "Agent/Skill Editing Surface")
  - Child function (e.g., "Agent Definition Editor with RRA preview")
  - Decomposition level
  - Allocated component/module (e.g., gui/editors/agent or plugins/packs/ide-platform)
  - Verification method
- Support and improve functional decomposition of the IDE layers and cross-cuts (repo structure, self-hosting, compliance).

### 3. Traceability & Architecture Linkage
- Walk the chain: Requirement → Architecture/Design target (from current layered docs or new disposition) → Implementation target → Verification.
- Use source-to-evidence patterns: flag orphan requirements or implementation without backing architecture.
- For repo structural work: explicitly trace to the IDE's own model (agents/skills as editable artifacts, packs as delivery, gates as enforcement).

### 4. Intake Readiness Assessment (Compliance Gate)
- Produce verdict: ready | conditional (with explicit closure criteria and responsible agent) | blocked.
- Check against current policies (governance-policy-compiler output), gate modes, and maturity level.
- Identify compliance risks (missing verification plan, weak traceability, layer violation).
- Prioritize findings by severity, layer impact, and verification cost.

### 5. Handoff & Evidence
- Emit:
  - Requirements quality report with severity-ranked items and file references.
  - Updated traceability slices.
  - Intake verdict + correction actions.
  - Clear handoff package for Architecture/Design Disposition Planner and Verification agents.
- Record evidence suitable for G1 (traceability) and G4 (independent review).

### 6. PowerShell / GitHub Native Steps (examples)
```powershell
# Example invocation (future skill runner or ACP)
pwsh -File tools/requirements/baseline-ide.ps1 -Scope "L0-Editors L2-Orchestration Cross-Structure" -Workspace . -Output evidence/requirements-baseline-$(Get-Date -Format yyyyMMdd).md

# Create compliance issue for findings
gh issue create --title "REQ baseline gaps for agent editor surface" --label requirements,compliance,ide-platform --body-file evidence/requirements-baseline-*.md
```

## Outputs
- Requirements baseline report with hierarchy metadata and traceability gaps.
- Intake verdict and prioritized action list.
- Evidence bundle for gates (G0/G1/G4).
- Recommendations for functional decomposition improvements.

## Escalation
- Major traceability or architecture linkage failures → Architecture/Design Disposition Planner + mandatory review.
- Compliance/policy violations → Governance Policy Compiler + Independent Review Committee (G4).
- Scope creep or missing verification methods on foundational IDE surfaces (editors, skills as artifacts, layers) → Planning Agent + Refactoring Agent for wave re-sequencing.

## Generalization & IDE-Specific Notes
- All original product assumptions (FarmRTK hardware, MATM threat modeling) removed.
- Added explicit support for the IDE's core model: agents and skills as first-class editable artifacts, viewers for evidence/lineage/graphs, pack manifests, hybrid orchestration, PowerShell + GitHub as native, self-hosting of the platform's own requirements.
- This skill is intended to be used on the IDE's own development (including repo structure refactors and functional decomposition of L0-L8).

## Related Platform Artifacts
- Gates: G0, G1, G2 (editor/viewer/skill contracts), G4.
- Agents: Requirements Baseline Steward (primary), Architecture/Design agents, Compliance/Verification agents, Planning Agent.
- Future: Integrated with agent/skill editors and source-to-evidence viewers.
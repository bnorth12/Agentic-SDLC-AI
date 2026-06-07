---
name: ide-requirements-implementation-auditor
description: >
  Generalized skill for auditing requirement and work-package coverage against implementation
  (generalized agents/skills in packs, plans, structure) and verification evidence for the agentic IDE.
  Primary for IDE Requirements Implementation Auditor. Generalizes requirements-implementation-auditor (MATM).
  Critical for closing traceability legs during remaining XGEN and structural IDE integration work.
metadata:
  short-description: "Requirements-to-implementation and work-package-to-verification coverage for generalized IDE agents, skills, and structure"
  agent: ide-requirements-implementation-auditor
  gates: [G1_traceability, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-requirements-implementation-auditor

**Agents:** IDE Requirements Implementation Auditor (primary), Requirements Baseline Steward, Source-to-Evidence Traceability Auditor, Verification Coverage Planner, Refactoring Agent  
**Parent:** [ide-requirements-implementation-auditor.agent.md](../../../agents/ide-platform/ide-requirements-implementation-auditor.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) · `agents/platform/invocations/remaining-xgen-refactoring-session.md`

## Purpose
Audit requirement IDs and governed work packages (from baselines, IDE_REFACTOR_PLAN, layer index, structural execution plans, and invocation records) against implementation evidence (generalized .agent.md and SKILL.md in the ide-platform pack, manifest updates, structure changes, scaffold code) and verification evidence (tests, smoke coverage, re-audits by generalized skills, G4 evidence bundles). Identify missing implementation, missing verification, coverage gaps in the elevation of agents and skills as first-class IDE artifacts, and gaps specific to the remaining XGEN set and FarmRTK integration. Produce actionable gap reports and prioritized remediation that feed the Refactoring Agent and Planning Agent.

## When to Invoke
- After creation or update of any generalized agents/skills in a tranche (this remaining XGEN session).
- After structural content moves, manifest updates, or plan changes that affect implementation legs.
- During Phase 5 (Validation & Closeout) of ide-structural-refactoring.
- At G1 traceability gates, G4 independent review of XGEN or structural work, and before G5 baseline.
- User: "audit requirements-to-implementation coverage for the remaining XGEN and ide-platform registration", "verify the new generalized agents have implementation and verification legs", "/ide-requirements-impl-coverage".
- As a required supporting procedure in self-hosting governance loops on the platform's own work.

## Inputs
- Requirements baselines and ide-structure-requirements-baseline.md.
- Work packages and tranche plans (LAYER_WORK_PACKAGE_INDEX.md, structural-refactor-execution-plan.md, WAVE_01).
- Generalized artifacts (new ide-* .agent.md / SKILL.md in plugins/packs/ide-platform/, their Parent and Generalization sections).
- Manifests (ide-platform, platform/manifest.yaml), layer index XGEN progress, invocation records.
- Prior traceability, policy, and verification reports.
- Test/smoke surface and evidence bundles.

## Procedure

### 1. Build Inventory of Requirements / Work Packages in Scope
- Scope to the current tranche (the 5 pending MATM agents + skills + priority FarmRTK + registration/integration work from this invocation).
- For each requirement or WP-ID, capture explicit references for implementation and verification legs.

### 2. Audit Implementation Leg
- Confirm presence of the generalized artifact in the target location (ide-platform/agents/ or /skills/).
- Verify IDE-native quality: rich content (mission, IDE surface awareness, hierarchy, PS/gh examples, generalization notes), correct Parent links, registration intent in manifest.
- Check for corresponding updates in cross-references (PLATFORM_AGENTS.md, layer index, execution plan, invocation record).

### 3. Audit Verification Leg
- Confirm supporting verification: smoke or unit coverage, re-run of generalized skills (traceability, policy compiler, this auditor, hierarchy steward), G4 evidence, or explicit test artifacts.
- Flag items with implementation but no (or weak) verification.

### 4. Identify Gaps and Systemic Issues
- Report gaps by severity, layer impact, and type (e.g., "new ide-xxx.agent.md present but no corresponding verification in this tranche's evidence bundle").
- Highlight patterns (e.g., many new items missing verification legs, or registration updates lagging creation).
- Produce prioritized remediation (smallest viable next slice).

### 5. PowerShell / GitHub Native Emphasis
```powershell
# Example (future runner or ACP)
pwsh -File tools/audit/requirements-impl-coverage.ps1 -Scope "Remaining-XGEN-Tranche2" -Baseline docs/ide-structure-requirements-baseline.md -Pack plugins/packs/ide-platform -Output evidence/requirements-impl-audit-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Implementation/verification gaps in remaining XGEN agents and skills" --label requirements,traceability,ide-platform --body-file evidence/requirements-impl-audit-*.md
```

### 6. Support Iteration and Self-Hosting
- Re-audit after remediation.
- Apply to the platform's own artifacts (this skill and the new generalized items must themselves have traceable implementation and verification legs from the tranche).
- Feed results into Refactoring Agent Phase 5 and Planning Agent intake.

## Outputs
- Requirement / WP to implementation coverage gaps.
- Requirement / WP to verification coverage gaps.
- Missing-test, missing-registration, and missing-link findings with file references.
- Prioritized remediation recommendations (target files in ide-platform, plan updates, evidence additions).
- Evidence suitable for G1/G4/G5.

## Guardrails
- Explicit references only — no inference.
- Local-first and file-referenced.
- Compatible with independent review and source-to-evidence processes.

## Generalization & IDE-Specific Notes
- Original MATM skill (old Requirements/, src/, Tests/, sprint issues) fully generalized to the IDE model: generalized agents/skills as pack content, WP system, layered plans, self-hosting of the generalization work itself, and the specific remaining XGEN + IDE integration activities in this session.
- Strong emphasis on "agents and skills as first-class editable artifacts" coverage (presence in ide-platform, rich IDE-aware content, manifest registration).
- All product assumptions removed.
- Self-referential: the work of generalizing this skill and its agent is itself subject to the audit.

## Related Platform Artifacts
- Gates: G1, G4, G5.
- Agents: IDE Requirements Implementation Auditor (primary), Requirements Baseline Steward, Traceability Auditor, Verification Coverage Planner, Refactoring Agent.
- Used in parallel with ide-source-to-evidence-traceability and ide-verification-coverage.
- Future: Integrated with coverage viewers and requirement traceability surfaces in the IDE.
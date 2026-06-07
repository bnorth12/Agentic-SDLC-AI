# Invocation Record — Planning Agent + Refactoring Agent for IDE Refactor

**Date:** 2026-06 (initial)  
**Invoked by:** Human (in Grok Build / this session) + direct embodiment  
**Context:** Post-reboot scaffold review. Goal: add Planning + Refactoring agents with skills, then have them drive the plan for the full agentic AI IDE using primarily the copied MATM (24 agents) + FarmRTK (17+ skills) assets, which all require generalization.

## Agents Instantiated
- [planning-agent.agent.md](../planning-agent.agent.md) (composed from multi-sprint-portfolio-planner, sprint-intake-gatekeeper, orchestrate-*, kpi-drift-analyst, remediation-*, requirements-baseline-steward, etc.)
- [refactoring-agent.agent.md](../refactoring-agent.agent.md) (composed from repo-governance-autoflow-orchestrator, architecture-design-*, source-to-evidence-traceability-auditor, artifact-lineage-auditor, governance-policy-compiler, hierarchy-*, repo-audit-*, technical-writer-*, etc.)

## Primary Skills Attached & Executed
- [platform/skills/ide-portfolio-planning/SKILL.md](../../../platform/skills/ide-portfolio-planning/SKILL.md)
- [platform/skills/ide-structural-refactoring/SKILL.md](../../../platform/skills/ide-structural-refactoring/SKILL.md)

## High-Level Flow Used (following the new skills)
1. **Baseline audit** (Refactoring Agent + ide-structural-refactoring Phase 0): dual structure, raw imports, doc bloat, packaging mismatch, legacy dominance, no real executor for the new SKILL.md/.agent.md style yet.
2. **Vision alignment** (Planning Agent): full suites of editors (agent, skill, manifest, evidence), viewers (multiple), user interaction agents, skills first-class (PowerShell+GitHub baked), hybrid orchestration, packs, self-hosting, GitHub as primary work/evidence surface.
3. **Mapping** (Refactoring Agent): every one of the 24 MATM .agent.md and the FarmRTK platform skills was explicitly mapped to roles in the new IDE (planning family → Planning Agent + ide-portfolio-planning; refactoring/governance/traceability family → Refactoring Agent + ide-structural-refactoring; others become core SE examples or pack content).
4. **Phased plan + concrete work packages** produced (see [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md)).
5. **Self-referential output**: The plan calls for ongoing use of these same agents/skills (and their future generalized siblings) to execute the waves, including dogfooding the IDE on its own development.

## Artifacts Created During This Invocation
- Two new platform agent definitions (with composition notes and IDE-specific responsibilities).
- Two new generalized skills in `platform/skills/` (following IMPORT_MANIFEST guidance).
- Starter `plugins/packs/ide-platform/plugin.manifest.yaml`.
- Updates to PLATFORM_AGENTS.md (table + notes), IMPORT_MANIFEST.md, root AGENTS.md, and this invocation record.
- The comprehensive IDE_REFACTOR_PLAN.md (the primary output of the joint agent run) — restructured by abstraction layers (L0–L8 + cross-cutting following FRAMEWORK_DECOMPOSITION.md) while remaining one cohesive, traceable document with layer-prefixed work packages (WP-Lx-xxx, WP-XGEN-xxx), explicit cross-layer dependency matrix, and full links to imported agents/skills + gates.
- New supporting index for manageability: `docs/charter/ide-refactor/LAYER_WORK_PACKAGE_INDEX.md` (work package catalog + dependency matrix, still tied to the master plan).
- Updates to REFACTOR_TODO.md linking the new work.

## How to Re-Invoke (manual or future ACP)
```powershell
# Example future invocation (once a skill runner or ACP host exists)
# Planning Agent for next wave
grok agent run planning-agent --skill ide-portfolio-planning --workspace workspace/current.yaml --gate G0

# Refactoring Agent for a specific generalization tranche
grok agent run refactoring-agent --skill ide-structural-refactoring --target "platform/imports/matm/agents" --output generalized/
```

Or follow the detailed Procedure sections in the two SKILL.md files directly (they are written to be human + agent executable).

## Evidence / Gate Notes
This session's output (the plan + supporting agent/skill files) is itself subject to G0 (wave charter for the IDE refactor), G1 (traceability of new agents/skills back to imported sources + reboot charter), and G4 (independent review recommended before large waves begin).

**Next human or agent action:** Review IDE_REFACTOR_PLAN.md, charter the first R1 wave with the Planning Agent, and begin the first tranche of import generalization + legacy decision with the Refactoring Agent.

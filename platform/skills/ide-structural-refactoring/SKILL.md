---
name: ide-structural-refactoring
description: >
  Structural analysis, generalization, architecture-aligned refactoring, and evidence-lineage repair skill
  for evolving the Agentic-SDLC-AI repo (and any workspace) into a full-featured agentic AI IDE.
  Primary skill for the Refactoring Agent. Generalizes repo-governance-autoflow, architecture-design-*,
  source-to-evidence/artifact-lineage auditors, repo-audit, technical-writer, governance-policy-compiler.
metadata:
  short-description: "Repo structure + imported agents/skills + docs modernization for the agentic IDE"
  agent: refactoring-agent
  gates: [G1_traceability, G2_icd_interfaces, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-structural-refactoring

**Agents:** Refactoring Agent (primary), Architecture/Design Change Author (composed), Source-to-Evidence Traceability Auditor, Artifact Lineage Auditor, Repo Organization Manager, Technical Writer, Governance Policy Compiler  
**Parent:** [refactoring-agent.agent.md](../../../agents/platform/refactoring-agent.agent.md) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [REBOOT_CHARTER.md](../../../docs/charter/REBOOT_CHARTER.md) · [FRAMEWORK_DECOMPOSITION.md](../../../docs/charter/FRAMEWORK_DECOMPOSITION.md)

## Purpose
Systematically transform the current transitional state (raw imports from FarmRTK + MATM, legacy full LangGraph org in `src/`, heavy duplicated historical docs, mixed packaging and bootstrap stories) into a clean, severable, plugin-first agentic IDE platform where:
- Agents and skills are first-class editable artifacts with dedicated editors and viewers.
- The IDE provides full suites of editors (code, agent defs, skill defs, manifests, prompts, gate evidence), viewers (mermaid, graph, stix, icd, audit, etc.), and user-interaction agents.
- PowerShell and GitHub are baked into the core experience and governance autoflow.
- All imported governance and process assets have been generalized and elevated.

## When to Invoke
- Major replatforming or "make the IDE real" waves.
- User: "refactor this repo to the full agentic IDE", "generalize the MATM agents for IDE use", "clean legacy + docs post-reboot".
- After Planning Agent has chartered a structural wave.
- When traceability or lineage audits (G1, source-to-evidence) fail on the platform itself.
- Before G5 baseline or major release of the platform installer.
- Slash command (target): `/refactor-ide-structure` or `/generalize-imports`.

## Inputs
- Full workspace tree + active `workspace/*.yaml`.
- All `agents/platform/*.agent.md` and `platform/imports/.../agents/*.agent.md`.
- All `*/SKILL.md` (imports + any already generalized) + legacy `src/skills/`.
- `platform/gates/registry.yaml`, schemas, `platform/manifest.yaml`, `plugins/packs/**/plugin.manifest.yaml`.
- Current docs tree (charter, governance, plans, policies, operations, project-plan sprint boards, reviews, references).
- Legacy surface: `src/` (agents, graphs, boards, gates, etc.), `Examples/`, `scripts/`, `docker/`, old `validate_structure.py`, `NEXT_STEPS.md`, etc.
- GitHub state for the repo (branches, PRs, Actions if present).
- Existing test surface and packaging (`pyproject.toml`).

## Procedure

### Phase 0: Baseline & Audit (always first)
1. Run generalized `repo-audit-sdlc` (from `repo-audit-farmrtk`): README coverage, folder hygiene, manifest completeness, BACKLOG/index presence.
2. Run source-to-evidence traceability audit focused on the reboot artifacts themselves (every new .agent.md, SKILL.md, gate, schema, viewer registration must have architecture/design linkage or be explicitly marked as scaffold).
3. Run artifact-lineage audit on generated vs. source (logs, evidence packets, old sprint boards, `__pycache__` / egg-info on disk, etc.).
4. Invoke `governance-policy-compiler` (generalized) against current gate modes + any workspace overrides.
5. Produce "Current State of the Reboot" report with severity-ranked findings and recommended refactor work packages.

### Phase 1: Generalize Imported Agents & Skills (core of this skill)
For every item in `platform/imports/matm/agents/*.agent.md` and `platform/imports/*/skills/*/SKILL.md`:
- Strip product suffixes (`-farmrtk`, MATM-specific naming) → produce `*-sdlc` or IDE-specific id.
- Replace hard-coded paths (`Tools/`, `.farmrtk/`, `SYS-DOC-10`, specific CAD/firmware dirs, sibling repo absolute paths) with manifest-driven equivalents:
  - `workspace.repos[].path`
  - `packs[].entry.skills_dir`
  - `gate.registry` + `viewer.*`
  - `runtime.shell` (powershell primary)
- Add explicit IDE surface awareness: "this planning/refactoring skill also plans and refactors editors, viewers, agent interaction models, skill contracts for the IDE host".
- Add PowerShell-first examples + `gh` CLI where the operation is GitHub-native (PR evidence, Action-triggered gates).
- Update or create corresponding entries in `agents/platform/PLATFORM_AGENTS.md` or the owning pack's agent list.
- Ensure each generalized artifact has a clear "used by" (Planning Agent, Refactoring Agent, EIRC, etc.) and maps to one or more gates.

### Phase 2: Structural Repo Reorganization
Apply the severable decomposition:
- Keep / evolve `platform/` (manifests, gates, schemas, skills (generalized), imports (temporary)).
- Keep / evolve `plugins/packs/` (one pack per major capability area; `ide-core` or `agentic-ide-platform` pack for the planning/refactoring + shell + viewer concerns).
- `gui/` for shell + viewers (expand beyond the current Zed snippet + PS1 doc).
- `workspace/` for templates + settings schema.
- `agents/platform/` for the slim process/governance personas (including the two new ones created here).
- Decide fate of `src/` (full options: `legacy/src/` with bridge adapters in `src/platform/`, selective port of valuable pieces (hitl, some tools, state ideas) into new layers, or archive after extraction).
- Create `docs/archive/` (or `docs/history/`) and move historical sprint boards, PHASE_*_COMPLETE, heavy duplicated governance (governance/, operations/, plans/, policies/ overlap), old reviews.
- Produce crisp living docs: focus on charter + current IDE architecture + "how to add an editor / viewer / skill / agent / pack".

### Phase 3: Architecture/Design Change Authoring + Disposition
For every structural slice:
- Create or update architecture/design workpack entries (use patterns from `architecture-design-change-author` + `architecture-design-disposition-planner`).
- Require hierarchy metadata on significant changes.
- Choose disposition path explicitly and record rationale + approval.
- Keep implementation (code, manifests, SKILL.md, .agent.md) in sync with the architecture view.
- Update verification (new or adapted tests in the scaffold style of `test_platform_scaffold.py`, plus skill smoke tests).

### Phase 4: Evidence, Lineage, Baseline & GitHub Integration
- Ensure every refactored component participates in the gate engine (add or update entries in registry.yaml if new gates or viewer types are introduced, e.g. for agent/skill editors).
- Update or add GitHub DevOps pack workflows that enforce relevant gates on PRs that touch platform/, agents/, skills/, gui/, workspace/.
- Produce decision records (`docs/decisions/ADR-*.md`) for major choices (legacy handling, where generalized skills live, ACP vs LangGraph boundaries for IDE surfaces).
- Run configuration baseline skill (generalized) to capture the post-refactor state.
- Update `platform/skills/` inventory and plugin manifests so the new `ide-portfolio-planning` and `ide-structural-refactoring` skills are discoverable.

### Phase 5: Validation & Closeout
- Re-run the audits from Phase 0; all critical findings must be closed or explicitly accepted with mitigation.
- Execute `independent-review-sdlc` (generalized) or EIRC on the refactor wave artifacts.
- Update this SKILL.md and the owning agent.md with lessons (they are self-hosting).
- Bump relevant versions in manifests and produce release notes / installer updates.
- Hand evidence bundle to sprint closeout certifier / G5 baseline if applicable.

## Outputs
- Generalized agent definitions and SKILL.md files (moved out of `imports/` when stable).
- Updated `PLATFORM_AGENTS.md`, gate registry, plugin manifests, workspace templates/schemas.
- Architecture/design change sets + disposition decisions with hierarchy metadata.
- Decision records and technical writing updates.
- Archived historical docs + slimmed living documentation tree.
- GitHub labels, project boards, or PR templates that encode the new governance autoflow for IDE development.
- Evidence packets suitable for independent review and configuration baseline.

## PowerShell / GitHub Native Emphasis
```powershell
# Example refactor step (to be turned into reusable skill fragments or gh workflow steps)
pwsh -File tools/refactor/generalize-imports.ps1 -SourceDir platform/imports/matm -TargetPattern "ide"
gh issue create --title "Generalize kpi-drift-analyst for IDE portfolio" --label refactor,ide-platform
# Gate enforcement via Action (github-devops pack) would call this skill or the agent via ACP
```

## Escalation
- Architecture/design misalignment that cannot be resolved locally → Chief Engineer + mandatory HITL.
- Policy conflicts discovered during governance-policy-compiler step → Governance Policy Compiler + Refactoring Agent iteration.
- Legacy surface too large to refactor in one wave → Planning Agent for sequencing + explicit "bridge" vs "archive" decisions.
- New IDE surface (e.g. a skill editor or agent interaction panel) requires brand new agent or viewer → feed back to Planning Agent.

## Generalization & IDE-Specific Extensions
- All original MATM/FarmRTK product assumptions (threat modeling pipelines, parametric CAD, specific firmware benches, etc.) are treated as *examples of packs*, not core platform behavior.
- New concerns added: editor surface contracts, viewer registration, user-interaction agent slots, skill execution sandbox for procedural + ACP, hybrid router wiring, GitHub as primary evidence and work-item store.
- The skill is self-referential: after a successful run, the updated version of *this* SKILL.md and the Refactoring Agent definition become part of the new baseline.

## Related Platform Artifacts
- Gates: G1 (traceability), G2 (ICD/interfaces for new editor/viewer contracts), G4 (independent review of structural changes), G5 (baseline).
- Viewers: viewer.markdown, viewer.mermaid (for architecture graphs), future viewer for agent/skill graphs, audit trail viewers.
- Future home: `plugins/packs/ide-platform/` or core of engineering-sdlc after full generalization.

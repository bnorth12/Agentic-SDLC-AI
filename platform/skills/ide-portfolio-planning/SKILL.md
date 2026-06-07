---
name: ide-portfolio-planning
description: >
  Generalized IDE portfolio, wave, and sprint planning skill for the agentic AI IDE platform.
  Replaces and generalizes orchestrate-farmrtk + multi-sprint-portfolio-planner + sprint-intake-gatekeeper.
  Primary skill for the Planning Agent.
metadata:
  short-description: "IDE feature portfolio to governed wave/sprint plan"
  agent: planning-agent
  gates: [G0_wave_charter, G4_independent_review]
  maturity: M0+
---

# ide-portfolio-planning

**Agents:** Planning Agent (primary), Chief Engineer (technical runway), Workspace Orchestrator (handoff)  
**Parent:** [planning-agent.agent.md](../../../agents/platform/planning-agent.agent.md) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [REBOOT_CHARTER.md](../../../docs/charter/REBOOT_CHARTER.md)

Generalized platform skill for planning the full-featured agentic IDE (editors, viewers, user interaction agents, skills, hybrid orchestration, plugin packs, PowerShell + GitHub integration) and for planning work *inside* any workspace that uses the IDE.

## Purpose
Turn stakeholder objectives, workspace manifests, current pack inventory, gate registry, legacy debt, and KPI trends into dependency-aware, evidence-linked, gate-governed wave and sprint plans that deliver coherent increments of the IDE or of user systems built with the IDE.

## When to Invoke
- Start of a new wave or major platform/pack increment (user: "plan the next IDE wave", "orchestrate M2 editor + viewer surface").
- After changes to `platform/manifest.yaml`, gate registry, new plugin pack manifests, or significant viewer/editor additions.
- Workspace onboarding or when a new product repo adopts the agentic IDE.
- When KPI drift or remediation signals require re-sequencing.
- Slash command (target): `/plan-ide-wave` or `/orchestrate-ide-portfolio`.

## Inputs
- Active `workspace/*.yaml` (or the example template) — repos, packs, maturity, gate overrides, runtime providers, toolchains, github config.
- `platform/gates/registry.yaml` + any workspace gate mode overrides.
- `platform/manifest.yaml` and `plugins/packs/*/plugin.manifest.yaml`.
- Current feature backlog / issues (GitHub or local BACKLOG.md equivalent).
- Existing agent inventory (`agents/platform/*.agent.md` + pack agents) and skill inventory (SKILL.md files + legacy src/skills where relevant).
- Recent gate evidence bundles and KPI trend artifacts (from program-metrics-sdlc or kpi-drift-analyst).
- Legacy state snapshot (what still lives only in `src/`, old docs, docker, etc.).

## Procedure

### 1. Discover Current State (Platform + Workspace)
```powershell
# From repo root (PowerShell)
$ws = Get-Content "workspace/templates/example-farmrtk.workspace.yaml" | ConvertFrom-Yaml   # or locate active workspace
Get-ChildItem platform/gates, plugins/packs -Filter *.yaml -Recurse | ForEach-Object { $_.FullName }
Get-ChildItem agents/platform -Filter *.agent.md
Get-ChildItem platform/skills, plugins/packs/*/skills -Recurse -Filter SKILL.md | Select FullName
```

### 2. Map Intent to IDE Surfaces and Layers
Classify incoming work against the severable layers (FRAMEWORK_DECOMPOSITION):
- L0 GUI Shell (editors, terminals, agent panels, viewers)
- L1 Agent Runtime (ACP, Grok Build, tool permissions)
- L2 Orchestration (router: procedural / LangGraph / ACP)
- L3 Gate Engine + HITL policy
- L4 Plugin Host + Pack loader
- L5 Workspace manifests + maturity
- L6 Providers (Grok, GitHub, Ollama, etc.)
- L7 Packs (engineering-sdlc, threat-modeling, github-devops, new ide-*, language toolchains)
- Legacy migration / archive items

Produce a work item inventory with explicit layer tags.

### 3. Build Dependency-Aware Wave Plan
For each candidate item produce:
- ID, title, layer(s), target maturity
- Required architecture runway (new schemas, viewer contracts, skill contracts, agent RRA updates)
- Prerequisite skills/agents/packs
- Verification approach (unit of the skill, integration through gate, end-to-end in workspace)
- GitHub-native representation (label, project, Action that will enforce the gate)
- HITL gate(s) from registry (G0, G1, G4, etc.) and mode for current maturity
- Estimated complexity and risk carry-over

Use multi-sprint-portfolio-planner logic generalized: balance core platform thinness vs. useful pack examples vs. migration debt.

### 4. Sprint Intake Gate (G0 / Planning Gate)
For each sprint-sized slice:
- Validate against requirements / architecture linkage (use requirements-baseline-steward + traceability-blocker-planner patterns).
- Confirm hierarchy metadata where applicable (parent capability, child function, decomposition level, allocated component, verification method).
- Check dependency ordering and architecture prerequisites.
- Issue verdict: ready | conditional (with explicit closure criteria) | blocked.
- Record in auditable artifact (e.g. `docs/plans/wave-YYYY-NN-intake.md` or GitHub project note).

### 5. Emit Executable Plan + Delegation Map
Output:
- Wave plan markdown with sections per layer/pack.
- Updated delegation map (who owns what: Planning Agent owns portfolio, Refactoring Agent owns structural modernization, specific pack agents own domain, Chief Engineer owns architecture alignment).
- Fragments for workspace manifest or gate overrides if the plan changes policy.
- List of procedural skills to run, LangGraph subgraphs to invoke, or ACP session starters (Grok Build) for interactive parts.
- PowerShell or `gh` commands that will drive the next steps (e.g. creating branches, labels, or kicking off a gate Action).

### 6. Close the Planning Loop
- Invoke `program-metrics-sdlc` / kpi-drift-analyst style measurement on the plan itself (planning quality, coverage of IDE surfaces, risk distribution).
- Hand off to Workspace Orchestrator or Chief Engineer with clear entry points.
- If this is a platform wave, also run `process-audit-sdlc` (generalized) against the planning artifacts.

## Outputs
- `Wave-Plan-*.md` or GitHub issue with full breakdown.
- Sprint charters / intake verdicts.
- Updated `workspace/*.yaml` proposals (as PRs).
- Delegation matrix (JSON or markdown) consumable by orchestration router.
- Evidence bundle for G0 / planning gate (links to all referenced manifests, agents, skills).

## Escalation
- Architecture runway conflicts or thin-platform violations → Chief Engineer + mandatory HITL.
- Cross-pack dependency explosion → Planning Agent + Refactoring Agent joint session.
- Missing generalized skills/agents for planned IDE surface → create intake for Refactoring Agent or new pack.
- User scope creep on the IDE itself → Program Manager equivalent (or user HITL at G0).

## References & Generalization Notes
- Originally derived from `orchestrate-farmrtk` (wave procedure + delegation) + `multi-sprint-portfolio-planner.agent.md` + `sprint-intake-gatekeeper.agent.md` + `kpi-drift-analyst.agent.md`.
- All FarmRTK-specific paths (`.farmrtk/`, `Tools/`, `SYS-DOC-10`, product backlogs) have been replaced by workspace-manifest-driven + gate-registry-driven + pack-manifest-driven equivalents.
- PowerShell is the default shell for Windows; equivalent bash fragments may be provided for cross-platform packs.
- Future: this skill itself should be invocable as a procedural executor, as a LangGraph node, or as the body of an ACP/Grok Build interactive planning session.

## Related Platform Artifacts
- Gate registry entries: G0_wave_charter (mandatory), G4_independent_review (maturity-gated).
- Viewer: viewer.markdown (for plans), future viewer.graph for portfolio visualization.
- Pack: will eventually live in or be referenced by `plugins/packs/ide-platform/` or core engineering-sdlc generalized skills.

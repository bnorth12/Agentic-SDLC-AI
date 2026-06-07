# Platform Reboot — Major Refactor TODO

**Parent:** [REBOOT_CHARTER.md](REBOOT_CHARTER.md)  
**Status:** Living burn-down — update as imports are generalized

---

## Legend

| Status | Meaning |
|--------|---------|
| `IMPORTED` | Copied from source repo; not yet generalized |
| `RENAME` | Skill/agent id must drop product suffix |
| `WRAP` | Becomes plugin wrapper, not inline code |
| `DROP` | Remove from platform; stays in source repo only |
| `BRIDGE` | Temporary adapter during migration |

---

## FarmRTK → Platform mapping

### Platform skills (`platform/imports/farmrtk/skills/`)

| Source skill | Target platform id | Status | Refactor work |
|--------------|-------------------|--------|---------------|
| `orchestrate-farmrtk` | `orchestrate-sdlc` | IMPORTED | Generalize `delegation_map.json`; workspace-relative paths |
| `independent-review-farmrtk` | `independent-review-sdlc` | IMPORTED | Maturity profiles; product-agnostic EIRC checklist |
| `check-work-commit-farmrtk` | `check-work-commit-sdlc` | IMPORTED | Parameterize repo layout rules |
| `traceability-audit-farmrtk` | `traceability-audit-sdlc` | IMPORTED | REQ/TC patterns configurable per workspace |
| `program-metrics-farmrtk` | `program-metrics-sdlc` | IMPORTED | KPI dashboard path from manifest |
| `requirements-management-farmrtk` | `requirements-management-sdlc` | IMPORTED | Segment path aliases |
| `test-authoring-farmrtk` | `test-authoring-sdlc` | IMPORTED | TC prefix configurable |
| `configuration-baseline-farmrtk` | `configuration-baseline-sdlc` | IMPORTED | Baseline tuple from manifest |
| `icd-maintenance-farmrtk` | `icd-maintenance-sdlc` | IMPORTED | ICD doc path configurable |
| `decision-record-farmrtk` | `decision-record-sdlc` | IMPORTED | ADR dir from manifest |
| `repo-audit-farmrtk` | `repo-audit-sdlc` | IMPORTED | README tree rules generic |
| `validation-plan-farmrtk` | `validation-plan-sdlc` | IMPORTED | V&V plan path alias |
| `risk-register-farmrtk` | `risk-register-sdlc` | IMPORTED | Risk doc id configurable |
| `process-audit-farmrtk` | `process-audit-sdlc` | IMPORTED | Registry paths from platform root |
| `technical-writer-farmrtk` | `technical-writer-sdlc` | IMPORTED | Quick-start template generic |
| `data-storage-farmrtk` | `data-schema-audit-sdlc` | IMPORTED | Schema doc + header paths in manifest |
| `bom-procurement-farmrtk` | `procurement-audit-sdlc` | IMPORTED | BOM + PROC tag configurable |

### Domain pack (`plugins/packs/engineering-sdlc/imports/`)

| Source skill | Pack action | Status |
|--------------|-------------|--------|
| `OpenSCAD-Parametric-FarmRTK` | Stay in engineering pack | IMPORTED |
| `firmware-build-farmrtk` | Generalize → `firmware-build` + toolchain plugin | IMPORTED |
| `integration-bench-farmrtk` | Generalize → `integration-bench` | IMPORTED |
| `electronics-wiring-farmrtk` | Optional embedded pack extension | IMPORTED |
| `rf-antenna-farmrtk` | Optional embedded pack extension | IMPORTED |

### FarmRTK agents

| Source | Platform agent | Status |
|--------|----------------|--------|
| `AGENTS-AND-SKILLS.md` registry | `agents/platform/PLATFORM_AGENTS.md` | TODO R1 |
| Product-specific personas (CAD, RF) | engineering-sdlc pack only | BRIDGE |

---

## MATM → Platform mapping

### Governance skills (`platform/imports/matm/skills/`)

| Skill | Platform role | Status |
|-------|---------------|--------|
| `independent-review-orchestrator` (via agent) | EIRC / governance pack | IMPORTED |
| `remediation-readiness` | Sprint gate skill | IMPORTED |
| `kpi-drift-analyst` | Program metrics alignment | GENERALIZED (Tranche 2) — ide-kpi-drift-analyst (full agent artifact created) | ide-platform pack; self-hosting XGEN + structural health metrics |
| hierarchy-taxonomy-steward (MATM) | Hierarchy taxonomy / decomp | GENERALIZED (Tranche 2) — ide-hierarchy-taxonomy-steward | ide-platform; L0-L8 + WP taxonomy for remaining XGEN/structural |
| requirements-implementation-auditor (MATM) | Req-to-impl coverage | GENERALIZED (Tranche 2) — ide-requirements-implementation-auditor | ide-platform; closes impl/verification legs for generalized artifacts |
| (independent-review-history-rollup-orchestrator + repo-governance-autoflow-orchestrator) | Review rollup + governance autoflow | GENERALIZED (Tranche 2) — ide-independent-review-history-rollup-orchestrator, ide-repo-governance-autoflow-orchestrator | ide-platform; G4 evidence hygiene + autoflow for XGEN tranches |
| `requirements-baseline-steward` | REQ gate skill | IMPORTED |
| `traceability-blocker-planner` | Traceability skill merge | IMPORTED |
| `sprint-closeout-certifier` | Wave end gate | IMPORTED |
| `governance-policy-compiler` | Gate policy compiler | IMPORTED |
| All 26 MATM skills | Audit for overlap with FarmRTK imports | IMPORTED |

### Threat modeling runtime

| MATM asset | Platform action | Status |
|------------|-----------------|--------|
| A1–A9 LangGraph pipeline | `plugins/packs/threat-modeling/` WRAP | TODO R3 |
| Streamlit HMI | Viewer plugin / webview | WRAP |
| `python -m threat_modeler` API | Plugin `entry.api` | WRAP |

### MATM agents (`platform/imports/matm/agents/`)

All 24 `.agent.md` files → merge into platform governance agent registry; dedupe with FarmRTK EIRC/PM roles in R2.

---

## Legacy Agentic-SDLC-AI → Platform

| Legacy module | Action |
|---------------|--------|
| `src/graphs/supervisor.py` | BRIDGE → `src/platform/orchestration/langgraph_adapter.py` or archive after generalized agents provide equivalent governance |
| `src/gates/*` | MERGE → `src/platform/gates/registry.py` + YAML (mostly done in scaffold) |
| `src/agents/*` (12) | Domain/SE logic → packs or generalized imported agents; old implementations moved to `legacy/` during R1–R2 |
| `src/skills/registry.py` | MERGE → platform skill discovery (platform/skills + packs) + contracts |
| Streamlit dashboard | MOVE → `gui/viewers/legacy-streamlit/` (optional) |
| Docker Compose | OPTIONAL / legacy profile in installer |

**New (R1+; XGEN complete for platform skills):** Planning Agent + Refactoring Agent created in `agents/platform/`, with primary skills `ide-portfolio-planning` and `ide-structural-refactoring` (plus ide_core tools) in `plugins/packs/ide-platform/`. Full manifests updated (ide-platform, IMPORT_MANIFEST, platform/manifest, engineering-sdlc, github-devops, threat-modeling) for coordination (see plugin.manifest.yaml for full FarmRTK/MATM list + L4/L7 notes; cross with PLATFORM_AGENTS.md pack-only section, matrix, invocation record, LAYER index). 

See the full layered [IDE_REFACTOR_PLAN.md](./IDE_REFACTOR_PLAN.md) (L0–L8 + cross-cutting; §5 for traceability/capabilities/decomp) and the governing [AGENTIC_IDE_PROJECT_PLAN.md](../../project-plan/AGENTIC_IDE_PROJECT_PLAN.md) (high-level waves/epics with limited details, layer-mapped; WAVE-02 for post-XGEN + GUI/PowerShell-MVP).

**Reusability evaluation (core input to plans, produced by Refactoring Agent via ide-structural-refactoring skill Phases 0-2):** [docs/charter/ide-refactor/REUSABILITY_EVALUATION_REPORT.md](../../charter/ide-refactor/REUSABILITY_EVALUATION_REPORT.md) — full inventory + per-layer reusability verdicts (very high for most MATM 24 agents + 26 skills + FarmRTK 17 platform skills into L2/L3/L4/L5/Cross/XGEN; selective legacy src/ ports; archive for historical docs bulk). All now in ide-platform (coordinated via manifests + tools).

Supporting: `docs/charter/ide-refactor/LAYER_WORK_PACKAGE_INDEX.md` (WP catalog + dep matrix; XGEN complete) and detailed Wave 01/02 plans at `docs/project-plan/WAVE_01_R1_FOUNDATIONS_DETAILED_PLAN.md` + `NEXT_WAVE_02_CHARTER.md`. All imported assets have explicit generalization path + layer fit + manifest registration.

All 24 MATM agents + 17 FarmRTK platform skills processed through `ide-structural-refactoring` + ide_core tools (generalize per layer, add IDE surfaces, PowerShell+GitHub, manifest-driven, evidence, hierarchy per matrix). Legacy `src/` decision, doc hygiene, and self-hosting treated as explicit cross-layer (see structural-refactor-execution-plan.md). Full coordination: manifests (ide-platform primary), PLATFORM_AGENTS (pack-only), matrix (traceability), executor/tools (L2/L4), PowerShell-MVP + custom GUI (no source reuse), gates, invocation record.

---

## GUI / IDE refactor

| Item | Target | Phase |
|------|--------|-------|
| Zed ACP host config | `gui/shell/zed/` | R4 |
| Portable shell abstraction | `src/platform/gui/shell_host.py` | R4 |
| Work-product viewers | `gui/viewers/{markdown,mermaid,stix,icd,graph}/` | R2–R4 |
| Installer | `gui/installer/Install-AgenticPlatform.ps1` | R6 |
| Settings schema | `workspace/templates/platform-settings.schema.json` | R1 |

---

## GitHub integration

| Item | Target | Phase |
|------|--------|-------|
| Actions workflow templates | `plugins/packs/github-devops/workflows/` | R5 |
| PR check bridge | `src/platform/providers/github/` | R5 |
| `gh` CLI tasks | procedural skills in github-devops pack | R5 |

---

## Cross-repo consumption (end state)

```
FarmRTK/          → workspace product only; `.grok/skills` shrinks to farmrtk-pack extensions
MATM/             → threat-modeling plugin source; no governance duplication
Agentic-SDLC-AI/  → platform + installer + packs
```

---

## Revision history

| Rev | Date | Change |
|-----|------|--------|
| 0.1 | 2026-06-06 | Initial refactor map after import scaffold |
| 0.2 | 2026-06 | Added Planning Agent + Refactoring Agent (personas + primary skills) + comprehensive IDE_REFACTOR_PLAN.md produced by them. All imported agents now have a clear generalization path via the new agents/skills. Legacy handling and doc hygiene explicitly scoped. |
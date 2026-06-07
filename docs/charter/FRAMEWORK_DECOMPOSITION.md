# Framework Decomposition — Severable Objects

**Parent:** [REBOOT_CHARTER.md](REBOOT_CHARTER.md)

---

## Layer model

| Layer | ID | Responsibility | Severable artifact |
|-------|-----|----------------|-------------------|
| **L0** | `gui-shell` | Editor host, terminals, layout, settings | `gui/` |
| **L1** | `agent-runtime` | ACP, Grok Build, tool permissions | `src/platform/orchestration/acp/` |
| **L2** | `orchestration` | Router: procedural / LangGraph / ACP | `src/platform/orchestration/` |
| **L3** | `gate-engine` | HITL policies, evidence, enforce hooks | `src/platform/gates/` |
| **L4** | `plugin-host` | Load packs, providers, viewers, toolchains | `src/platform/plugins/` |
| **L5** | `workspace` | Multi-repo manifest, maturity, providers | `workspace/` |
| **L6** | `providers` | LLM + GitHub + secrets | `src/platform/providers/` |
| **L7** | `packs` | Domain capabilities | `plugins/packs/` |
| **L8** | `product-repo` | Application source (external) | FarmRTK, customer apps |

### Capabilities by Layer (Target)

Each layer provides a distinct set of capabilities that are severable and composable. These are the "what" the layer enables for the IDE and for self-hosting development of the platform itself.

- **L0 (GUI Shell)**: Agent/skill/manifest/evidence editors; rich viewers (markdown, mermaid, graph, audit trails); agent interaction panels; PowerShell terminal integration; layout & settings persistence.
- **L1 (Agent Runtime)**: ACP stdio host for interactive multi-agent sessions; tool permission & scoping model scoped to IDE surfaces; session lifecycle and state handoff to L2.
- **L2 (Orchestration)**: Hybrid routing (procedural SKILL.md execution, LangGraph stateful graphs, ACP interactive); invocation of generalized skills/agents; evidence return to L3; basic hybrid dispatch between execution modes.
- **L3 (Gate Engine + HITL + Evidence)**: Registry-driven gate enforcement (G0–G5); maturity-aware policy profiles (strict/advisory); evidence bundle production & validation; HITL interrupt points; viewer hooks for evidence.
- **L4 (Plugin Host)**: Discovery & loading of `SKILL.md` + `.agent.md` from platform/skills/ and packs; viewer & toolchain registration; pack manifest resolution; tool registry loading & permission enforcement.
- **L5 (Workspace)**: Workspace manifest-driven configuration (repos, packs, gates, shell, providers); maturity level affecting gate modes; context provider for all other layers.
- **L6 (Providers)**: LLM provider abstraction (Grok Build ACP primary, others pluggable); GitHub provider (repos, Actions, gh CLI, PR evidence); secrets & auth.
- **L7 (Packs)**: Delivery of domain + platform-process capabilities (ide-platform for Planning/Refactoring/governance; engineering-sdlc, threat-modeling, github-devops, etc.); first-class agent/skill content living inside packs.
- **L8 + Cross**: External product consumption of the IDE; legacy migration strategy (bridge/archive/port); overall doc hygiene & living documentation; continuous generalization (XGEN) of imported assets; self-hosting/dogfooding of the entire platform.

Cross-cutting capabilities (apply to all layers): Traceability (G1), Hierarchy/functional decomposition, PowerShell + GitHub native evidence, self-hosting, editor/viewer surface contracts.

---

## Severable object catalog

### Core platform objects

| Object | Path | Contract |
|--------|------|----------|
| **Platform manifest** | `platform/manifest.yaml` | Version, min Python, supported OS |
| **Skill contract schema** | `platform/schemas/skill-contract.schema.json` | Inputs, outputs, policy checks |
| **Plugin manifest schema** | `platform/schemas/plugin-manifest.schema.json` | Pack metadata, entrypoints |
| **Gate registry** | `platform/gates/registry.yaml` | Gate id, mode, executor, viewer |
| **Agent registry** | `agents/platform/PLATFORM_AGENTS.md` | RRA, skills, readiness |
| **Workspace schema** | `platform/schemas/workspace.schema.json` | Repos, packs, gates, toolchains |

### Plugin object (pack)

```yaml
# plugins/packs/<pack-id>/plugin.manifest.yaml
id: engineering-sdlc
version: 0.1.0
type: pack
entry:
  skills_dir: skills
  agents_dir: agents
toolchains: [platformio, arduino-cli]
languages: [c, cpp, python]
os: [windows, linux, macos]
dependencies:
  packs: []
  providers: [grok-build]
```

### Viewer object

| Viewer id | Work product | Path |
|-----------|--------------|------|
| `viewer.markdown` | REQ, docs, ADR | `gui/viewers/markdown/` |
| `viewer.mermaid` | Architecture, threat diagrams | `gui/viewers/mermaid/` |
| `viewer.stix` | Threat bundles | `gui/viewers/stix/` |
| `viewer.icd-csv` | Interface tables | `gui/viewers/icd-csv/` |
| `viewer.graph-canonical` | MATM canonical JSON | `gui/viewers/graph-canonical/` |
| `viewer.lsp` | Code (all languages) | `gui/shell/` (delegates to host) |

### Provider object

| Provider id | Capability |
|-------------|------------|
| `provider.grok-build` | ACP agent stdio |
| `provider.grok-api` | xAI API BYOK |
| `provider.openai` | OpenAI-compatible |
| `provider.github` | Repos, Actions, PRs, `gh` CLI |
| `provider.ollama` | Local inference (optional) |

### Toolchain plugin object

Supports: JavaScript/Node, CakePHP/PHP, Rust/cargo, C/C++/CMake, Java/Maven/Gradle, Fortran, Python.

Each toolchain declares: detect files, build cmd, test cmd, lint cmd, CI template.

---

## Decomposition diagram

```mermaid
flowchart TB
    subgraph L0 [L0 GUI Shell]
        SHELL[Portable IDE host]
        TERM[OS terminal - PowerShell/bash]
        PANEL[Agent panel ACP]
        EDIT[Agent/Skill/Manifest/ Evidence editors]
    end
    subgraph L4 [L4 Plugin Host]
        PLUG[Plugin + Skill/Agent loader]
        P1[ide-platform (planning, refactoring, governance)]
        P2[engineering-sdlc]
        P3[github-devops]
        TOOLREG[Tool registry & permissions]
    end
    subgraph L2 [L2 Orchestration]
        RTR[Router (procedural / LangGraph / ACP)]
        PROC[Procedural Skill Executor]
        LG[LangGraph adapter]
        ACP[ACP sessions]
    end
    subgraph L3 [L3 Gates + Evidence]
        GREG[Gate registry]
        HITL[HITL policy + evidence bundles]
    end
    SHELL --> PANEL
    PANEL --> ACP
    SHELL --> PLUG
    PLUG --> P1 & P2 & P3
    PLUG --> TOOLREG
    RTR --> PROC & LG & ACP
    PROC & LG & ACP --> GREG
    GREG --> HITL
    EDIT -.-> PLUG
```

**Example Functional Decomposition (Hierarchy Metadata applied)**

For a representative component (Procedural Skill Executor at L2, and a generalized agent at L4/L7):

- **Parent Capability**: L2 Orchestration – Hybrid execution of first-class skills and agents
- **Child Function**: Procedural execution of SKILL.md procedures with evidence return
- **Decomposition Level**: 3
- **Allocated Component/Module**: src/platform/orchestration/executor.py + tools/executor/run-skill.ps1
- **Verification Method**: Smoke test of ide-structural-refactoring procedure; G1 traceability from this plan; G2 executor interface contract

- **Parent Capability**: L4 Plugin Host + L7 Packs – Elevation of agents/skills as editable artifacts
- **Child Function**: Discovery, loading, and registration of ide-* agents/skills from ide-platform pack
- **Decomposition Level**: 2
- **Allocated Component/Module**: plugins/packs/ide-platform/agents/ide-*.agent.md + skills/*/SKILL.md + plugin.manifest.yaml
- **Verification Method**: Pack loader test; hierarchy validation by ide-hierarchy-taxonomy-steward; source-to-evidence audit; G4 review of XGEN tranche

All significant architecture elements (new executor, tools, generalized agents/skills from Tranche 1/2, IDE surfaces) must carry equivalent hierarchy metadata. See ide-structure-requirements-baseline.md and structural-refactor-execution-plan.md for applied examples on repo structure.
---

## Language / framework adaptability

| Stack | Detection | Toolchain plugin | CI template pack |
|-------|-----------|------------------|------------------|
| JavaScript / TS | `package.json` | `toolchain.node` | `github-devops/workflows/node.yml` |
| CakePHP / PHP | `composer.json` | `toolchain.php` | `php.yml` |
| Rust | `Cargo.toml` | `toolchain.rust` | `rust.yml` |
| C / C++ | `CMakeLists.txt`, `Makefile` | `toolchain.cmake` | `cpp.yml` |
| Java | `pom.xml`, `build.gradle` | `toolchain.java` | `java.yml` |
| Fortran | `CMakeLists.txt`, `.f90` | `toolchain.fortran` | `fortran.yml` |
| Python | `pyproject.toml` | `toolchain.python` | `python.yml` |
| Embedded | `platformio.ini` | `toolchain.platformio` | `platformio.yml` |

---

## GitHub linkage

| Feature | Implementation |
|---------|----------------|
| Clone/open repo | Workspace manifest `repos[].url` |
| PR checks | `github-devops` pack → gate enforce at merge |
| Actions | Template workflows per toolchain |
| Evidence | Store run URLs in gate evidence bundle |
| Agent tasks | `gh pr create`, `gh workflow run` via procedural skills |

---

## Revision history

| Rev | Date | Change |
|-----|------|--------|
| 0.1 | 2026-06-06 | Initial decomposition scaffold |
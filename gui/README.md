# GUI — Portable Agentic IDE Shell

**Status:** Scaffold (R4)  
**Parent:** [REBOOT_CHARTER.md](../docs/charter/REBOOT_CHARTER.md)

## Current Approach: PowerShell-First (Interim Primary Shell)

We are continuing development primarily through **PowerShell** (scripts, the L2 procedural executor, `ide_core` tools, direct skill invocation, and terminal-based workflows) until we can instantiate a suitable GUI framework for a clean, minimal custom agentic IDE shell.

This allows us to keep self-hosting and advancing the platform (agents, skills, generalization, executor, tools, governance) using our own generalized capabilities without compromising the principle of building a unique custom GUI (following modern editor patterns like dockable layouts, structure-aware editing, rich viewers, and agent panels — but owning 100% of the implementation, with no source reuse or forking from Zed, VS Code, Eclipse, etc.).

**Zed** remains only a temporary, optional bootstrap for ACP agent sessions and an integrated terminal during early R1 work. It is not the long-term shell.

| Component | Path | Role |
|-----------|------|------|
| Primary shell / interaction | PowerShell + L2 executor + ide_core tools | Current main surface for running skills, editing via tools, evidence capture, generalization work, and self-hosting development |
| Temporary ACP bridge (optional) | `shell/` (zed-agent-servers.json) | Early agent interaction and terminal convenience only |
| Viewers (future) | `viewers/` | Will be custom once a proper GUI framework/MVP shell exists |
| Installer | `installer/` | Bootstrap the PowerShell-centric platform (+ optional temporary Zed bridge) |

## PowerShell as Primary Development Surface

- Most procedural SKILL.md steps are written for PowerShell (Windows primary) + `gh` CLI.
- The L2 executor can run pwsh steps and return structured evidence.
- `src/platform/tools/ide_core.py` provides reusable helpers (read/write artifacts, hierarchy validation, generalization stubs) callable from PowerShell or the executor.
- Daily work (generalization of FarmRTK/MATM skills, running audits, updating the matrix and plans, self-hosting) happens via these PowerShell-centric tools and the generalized ide-* skills.
- This keeps us productive and "inside our own IDE" (via skills, executor, and artifacts) while we wait for the right moment to stand up a minimal custom GUI framework.

## Portable install

```powershell
powershell -File gui/installer/Install-AgenticPlatform.ps1 -Profile minimal
```

Profiles: `minimal` (Zed kit docs), `full` (+ Python platform CLI).

## Viewer registry

| Id | Format |
|----|--------|
| `viewer.markdown` | `.md` REQ, ADR, backlog |
| `viewer.mermaid` | `.mmd`, fenced mermaid |
| `viewer.stix` | STIX 2.1 JSON |
| `viewer.icd-csv` | ICD CSV tables |
| `viewer.graph-canonical` | MATM canonical graph JSON |
| `viewer.lsp` | Code — delegated to shell host |
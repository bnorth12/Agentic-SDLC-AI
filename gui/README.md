# GUI — Portable Agentic IDE Shell

**Status:** Scaffold (R4)  
**Parent:** [REBOOT_CHARTER.md](../docs/charter/REBOOT_CHARTER.md)

## Design

| Component | Path | Role |
|-----------|------|------|
| Shell host | `shell/` | Zed ACP config; future Tauri host |
| Viewers | `viewers/` | Work-product panes (markdown, Mermaid, STIX, ICD) |
| Installer | `installer/` | Bootstrap Zed + Grok + platform |

## Phase 1 host (Zed Personal)

- Integrated **PowerShell** terminal (Windows)
- **Grok Build** via ACP Registry
- Platform skills from workspace manifest
- Viewers open gate artifacts in side panels

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
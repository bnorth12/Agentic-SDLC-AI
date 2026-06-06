---
name: electronics-wiring-farmrtk
description: >
  Scaffold Electronics wiring docs from segment 07-Wiring-Diagram. Electronics
  Engineer. Use for wiring doc, EL-DOC scaffold, or bench wiring notes.
metadata:
  short-description: "EL wiring doc scaffold"
---

# electronics-wiring-farmrtk

**Agent:** Electronics Engineer  
**Parent:** [Electronics/BACKLOG.md](../../../Electronics/BACKLOG.md)

## Scaffold

```powershell
powershell -File Tools/ci/scaffold_el_doc.ps1 -Segment Power-Management -DocId EL-DOC-PWR-001
```

## Steps

1. Align with ICD row in SYS-DOC-04.
2. Update segment `07-Wiring-Diagram.md`.
3. Link BOM electrical lines in [BOM-Full.md](../../../BOM/BOM-Full.md).
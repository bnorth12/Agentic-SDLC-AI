---
name: decision-record-farmrtk
description: >
  Scaffold architecture decision records (ADR) under Docs/System-Level/decisions/.
  Systems Engineer trade studies. Use for ADR, decision record, or trade study log.
metadata:
  short-description: "ADR scaffold"
---

# decision-record-farmrtk

**Agent:** Systems Engineer

## Scaffold

```powershell
powershell -File Tools/ci/scaffold_adr.ps1 -AdrId ADR-001 -Title "Case selection trade"
```

## Steps

1. Create ADR when CE requests trade study (case, CYD variant, power path).
2. Link REQ/ICD in traceability table.
3. Reference ADR from SYS-DOC-02 or segment architecture when accepted.
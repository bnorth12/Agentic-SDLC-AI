---
name: icd-maintenance-farmrtk
description: >
  Audit FarmRTK ICD (SYS-DOC-04) and segment wiring diagram coverage. Systems
  Engineer M-G2 gate. Use for ICD audit, interface consistency, or wiring stub
  check.
metadata:
  short-description: "ICD and wiring audit"
---

# icd-maintenance-farmrtk

**Agent:** Systems Engineer  
**Parent:** [04-System-Interface-Control-Document.md](../../../Docs/System-Level/04-System-Interface-Control-Document.md)

## Steps

1. `powershell -File Tools/ci/icd_audit.ps1`
2. Fix missing `Docs/<Segment>/07-Wiring-Diagram.md` or ICD rows.
3. Pair with `electronics-wiring-farmrtk` for EL-DOC stubs.
4. Document trades via `decision-record-farmrtk` when interfaces change.
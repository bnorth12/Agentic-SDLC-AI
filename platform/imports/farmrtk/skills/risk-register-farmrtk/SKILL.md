---
name: risk-register-farmrtk
description: >
  Audit FarmRTK risk register (SYS-DOC-09) row format and open risk hygiene.
  Risk Manager. Use for risk register audit or risk review.
metadata:
  short-description: "Risk register audit"
---

# risk-register-farmrtk

**Agent:** Risk Manager  
**Parent:** [09-Risk-Register.md](../../../Docs/System-Level/09-Risk-Register.md)

## Steps

1. `powershell -File Tools/ci/risk_register_audit.ps1`
2. Ensure each open risk has owner, mitigation, L/I ratings.
3. Feed TI-03 on program health dashboard.
4. Escalate H-impact open risks to Program Manager wave planning.
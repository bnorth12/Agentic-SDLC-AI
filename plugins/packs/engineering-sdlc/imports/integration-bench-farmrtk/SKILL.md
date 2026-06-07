---
name: integration-bench-farmrtk
description: >
  FarmRTK end-to-end bench bring-up — ICD spot checks, preflight audit, and
  session logs before TC execution. Integration Engineer pairs with System Test
  and Electronics. Use for bench bring-up, integration session, ICD bench demo,
  or ASK-03 bench HITL.
metadata:
  short-description: "ICD bench preflight and session scaffold"
---

# integration-bench-farmrtk

**Agent:** Integration Engineer (primary); System Test Engineer (TC evidence)  
**Parent:** [04-System-Interface-Control-Document.md](../../../Docs/System-Level/04-System-Interface-Control-Document.md) · [Tests/BACKLOG.md](../../../Tests/BACKLOG.md)

End-to-end bench: base + rover + power + BT; ICD compliance demos before field tests (TC-001+).

## When to invoke

- Before any P0 bench session (TC-002, TC-003, TC-005, TC-007, TC-011)
- ASK-03 bench HITL closure
- M-G3 TRR prep — bench readiness gate

## Preflight audit

```powershell
powershell -File Tools/integration/bench_preflight.ps1
```

Or stepwise: `Tools/ci/integration_bench_audit.ps1` then `Tools/test/run_nmea_golden_test.ps1`.

Fix warnings before powering hardware. Pair with `icd-maintenance-farmrtk` for ICD row gaps.

## Scaffold session log

```powershell
powershell -File Tools/ci/scaffold_bench_session.ps1 -SessionId INT-TC002-001 -TcId TC-002 -IcdIds ICD-005,ICD-006
```

Session logs live under `Tests/Integration/sessions/<SessionId>/`. Roll evidence into `Tests/Verification/artifacts/TC-nnn/`.

## Procedure

1. Run `integration_bench_audit.ps1` — zero failures before session.
2. Scaffold session log with target TC and ICD rows ([BENCH_ICD_MAP.md](references/BENCH_ICD_MAP.md)).
3. **Preflight:** flash firmware, serial monitor, power rails per EL-DOC; LoRa/BT as required by TC.
4. **ICD spot checks:** exercise interfaces listed for the TC; log pass/fail in session log.
5. Execute TC procedure with System Test Engineer; capture serial + screenshots per [TC-002 template](../../../Tests/Verification/artifacts/TC-002/execution-log.md).
6. **EIRC** merge-tier before committing artifact updates.
7. Update Tests/BACKLOG and parent TC `execution-log.md` status.

## Escalation

- ICD mismatch → Systems Engineer + `icd-maintenance-farmrtk`
- Wiring / power → Electronics Engineer + `electronics-wiring-farmrtk`
- Firmware defect → Firmware Engineer + `implement`
- Scope change → Program Manager + G0 wave doc
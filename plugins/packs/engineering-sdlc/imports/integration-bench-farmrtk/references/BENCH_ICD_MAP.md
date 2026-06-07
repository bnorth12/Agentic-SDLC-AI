# Bench ICD map

Maps system test cases to ICD interfaces checked on bench.

| TC | Primary ICDs | Bench focus |
|----|--------------|-------------|
| TC-002 | ICD-005, ICD-006 | Base PQT save/load; NMEA to CYD; survey-in UI |
| TC-003 | ICD-003 | Hot-swap 5V rail; dual battery OR |
| TC-005 | ICD-002, ICD-007 | Rover NMEA parse; BT SPP to phone |
| TC-007 | ICD-004 | TP4056 cradle charge current |
| TC-011 | ICD-002 | BT pairing gating; discoverable window |
| TC-008–010 | ICD-008, ICD-009 | SD CSV; mark switch debounce |
| TC-012 | ICD-010 | VVT artifact tree on SD |

**Component tests (preflight):**

| CT | ICD | Parent TC |
|----|-----|-----------|
| CT-BASE-002 | ICD-005, ICD-006 | TC-002 |
| CT-BASE-004 | ICD-006 | TC-002 |
| CT-ROV-003 | ICD-002 | TC-005, TC-011 |
| CT-PWR-001 | ICD-003 | TC-003 |
| CT-PWR-004 | ICD-004 | TC-007 |
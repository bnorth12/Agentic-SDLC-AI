---
name: hierarchy-conformance-auditor
description: "Audit sprint issue hierarchy conformance and report enforceable findings for required decomposition and allocation metadata."
---
# Hierarchy Conformance Auditor Skill

## Purpose
Enforce structural hierarchy completeness in sprint artifacts and publish auditable metrics.

## Inputs
- Sprint ID (YYYY-MM or YYYY_MM)
- independent review outputs in independent_reviews/latest/

## Procedure
1. Run sprint traceability verification:
```bash
python scripts/verify_sprint_traceability.py --sprint <SPRINT>
```
2. Run independent review with update mode:
```bash
python scripts/independent_repo_review.py --sprint <SPRINT> --run-context manual --report-mode update
```
3. Confirm hierarchy governance metrics are present in report output:
- sprint issue files analyzed
- hierarchy coverage ratio
- decomposition level counts
- phase counts
- parent capability fan-out
- missing hierarchy field rows

4. Escalate findings by severity:
- major when hierarchy coverage ratio falls below governance expectation
- minor when isolated field omissions are detected
- informational when taxonomy shape indicates consolidation opportunities

## Expected Outputs
- independent_reviews/latest/independent_review_<sprint>_manual.md
- independent_reviews/latest/independent_review_<sprint>_manual.json

## Guardrails
- Local-only evidence checks unless explicit remote reconciliation is requested.
- Do not downgrade missing required hierarchy metadata to non-governance notes.

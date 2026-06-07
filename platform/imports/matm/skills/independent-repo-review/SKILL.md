---
name: independent-repo-review
description: "Run a full-scope local independent repository review with specialized agent workflow and generate local ignored reports. Use for governance health checks before commits, merges, and branch integration decisions."
---
# Independent Repo Review Skill

## Purpose
Run an independent, local-first review that is separate from GitHub-hosted compliance pipelines.

## Inputs
- Sprint ID (YYYY-MM or YYYY_MM)
- Enforcement mode (auto/off/manual)
- Severity policy profile (optional)
- Severity threshold overrides (optional)
- GitHub reconciliation mode (optional, explicit opt-in)

## Procedure
1. Execute:
```bash
python scripts/independent_repo_review.py --sprint <SPRINT> --run-context manual --report-mode update
```
2. Select a checked-in policy profile:
```bash
python scripts/independent_repo_review.py --sprint <SPRINT> --run-context manual --report-mode update --policy-profile strict
```
3. For profile-based enforcement, execute:
```bash
python scripts/independent_repo_review.py --sprint <SPRINT> --run-context manual --report-mode update --policy-profile strict --enforcement-mode auto
```
Manual enforcement levels:
```bash
python scripts/independent_repo_review.py --sprint <SPRINT> --enforcement-mode manual --enforce-on critical,major
```
4. Optional threshold policy override:
```bash
python scripts/independent_repo_review.py \
	--sprint <SPRINT> \
	--run-context manual \
	--report-mode update \
	--policy-profile default \
	--req-impl-threshold 0.75 \
	--req-verify-threshold 0.70 \
	--req-arch-threshold 0.75 \
	--issue-quality-threshold 0.95 \
	--max-planned-missing-requirement 0
```
5. Read generated markdown/json in independent_reviews/latest/.
6. Report prioritized gaps:
- requirements without implementation evidence
- requirements without verification evidence
- requirements without architecture/design traceability
- requirements with incomplete source-to-evidence chain (source, architecture/design, implementation, verification)
- requirements with incomplete decomposition metadata (parent capability, child function, decomposition level, allocated component/module, verification method)
- conceptual planned items with architecture/design trace but no as-built implementation, with maturity tags
- as-built implementation items lacking architecture/design trace
- issue rows missing requirement IDs
- planned rows lacking requirement linkage
- branch merge risk (current branch, ahead/behind vs origin/main, merge-base risk)
- severity findings against active threshold policy
- trend deltas from prior snapshots (score + severity count deltas)
- compact trend dashboard summary (last N runs)
- remediation readiness summary using a health-based floor
- final remediation strategy section with theme-based sprint intake guidance

7. Treat architecture/design, requirements, implementation, and verification as a single governed chain for the Multi-Agent Threat Modeler application, and note when any of those concepts appear in data-flow modeling or interface boundaries.

8. Explicitly capture where agents and skills are acting as implementation or governance participants, especially when they enforce traceability, boundary validation, or review readiness.

9. Enforce hierarchical decomposition checks in sprint artifacts so each requirement can be traced L0 -> L1 -> L2 with explicit parent-child relationships and code-level allocation.

10. Run hierarchy governance sub-workflows:
- hierarchy-taxonomy-steward for decomposition taxonomy normalization and drift control
- hierarchy-conformance-auditor for enforceable hierarchy conformance findings and metrics

11. Optional local GitHub reconciliation:
```bash
python scripts/independent_repo_review.py \
	--sprint <SPRINT> \
	--run-context manual \
	--report-mode update \
	--policy-profile default \
	--trend-window 5 \
	--github-reconcile \
	--github-repo <OWNER/REPO>
```

12. Optional archival snapshot mode:
```bash
python scripts/independent_repo_review.py --sprint <SPRINT> --run-context manual --report-mode archive
```

## Expected Outputs
- independent_reviews/latest/independent_review_<sprint>_<context>.md
- independent_reviews/latest/independent_review_<sprint>_<context>.json
- independent_reviews/history/reports/independent_review_<sprint>_<context>_<timestamp>.* (when archived)

## Health Metric
- The report uses "health" rather than "goodness" as the primary remediation readiness framing.
- A remediation health floor is read from the active policy profile and drives the final readiness verdict.

## Guardrails
- Local-only evidence execution.
- Do not depend on GitHub Actions or remote CI status.
- Do not edit runtime implementation as part of review reporting.
- GitHub reconciliation is opt-in only and must remain non-blocking unless enforce policy is explicitly chosen.
- Chain completeness must be evaluated with explicit evidence refs, not first-level ID presence.

---
name: requirements-implementation-auditor
description: "Audit requirement IDs against implementation and verification evidence, including missing implementation, missing tests, and feature-to-requirement coverage gaps."
---
# Requirements Implementation Auditor Skill

## Purpose
Check whether requirements are realized in code and tests, and whether the implementation is consistent with the requirement intent.

## Inputs
- Requirement files under Requirements/
- Implementation files under src/, frontend/src/, and scripts/
- Verification files under Tests/
- Sprint issue tracker and traceability matrix artifacts under planning/

## Procedure
1. Identify requirement IDs with implementation evidence.
2. Identify requirement IDs with verification evidence.
3. Flag requirements with implementation evidence but no supporting tests.
4. Flag feature rows or issue rows that lack requirement IDs.
5. Summarize coverage gaps and the smallest viable next remediation slice.

## Outputs
- Requirement-to-implementation coverage gaps.
- Requirement-to-verification coverage gaps.
- Missing-test and missing-link findings.
- Prioritized remediation recommendations.

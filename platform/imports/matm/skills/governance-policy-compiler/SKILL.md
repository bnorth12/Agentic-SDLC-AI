---
name: governance-policy-compiler
description: "Compile and validate policy profiles and context routing into deterministic governance behavior."
---
# Governance Policy Compiler Skill

## Purpose
Convert policy definitions into predictable local enforcement behavior.

## Inputs
- config/independent_review_policy_profiles.json
- branch and run-context routing rules

## Procedure
1. Validate profile schema and threshold consistency.
2. Check routing logic for strict/default/advisory behavior.
3. Detect contradictory or unreachable rule combinations.
4. Emit policy status with actionable fixes.

## Outputs
- Policy compilation status and rule diagnostics.
- Recommended policy corrections.

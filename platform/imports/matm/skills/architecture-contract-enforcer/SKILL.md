---
name: architecture-contract-enforcer
description: "Enforce architecture and interface contract integrity against requirement and implementation changes."
---
# Architecture Contract Enforcer Skill

## Purpose
Ensure architecture and design artifacts remain authoritative and aligned with requirement and implementation intent.

## Inputs
- docs/architecture/
- docs/design/
- Requirements/

## Procedure
1. Evaluate requirement-to-architecture/design traceability coverage.
2. Detect missing or stale interface contract mappings.
3. Flag as-built work that lacks architecture/design trace evidence.
4. Classify conceptual-versus-as-built mismatch risks.

## Outputs
- Contract integrity findings and traceability gaps.
- Merge gate recommendation by severity/profile.

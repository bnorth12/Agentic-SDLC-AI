---
name: architecture-document-surface-enforcer
description: "Enforce required architecture and design document-family coverage for governed review contexts."
---
# Architecture Document Surface Enforcer Skill

## Purpose

Confirm that the governed architecture and design document surfaces are present, referenced, and usable for independent review and traceability workflows.

## Inputs

- Architecture artifacts under docs/architecture/
- Design artifacts under docs/design/
- Independent review and planning artifacts under independent_reviews/ and planning/

## Procedure

1. Identify the required document families for the active governance context.
1. Verify that each required surface exists and is referenced by the review or traceability chain.
1. Flag missing, stale, or unreferenced architecture/design surfaces.
1. Prioritize gaps that affect traceability clarity, review onboarding, or governance completeness.

## Outputs

- Missing architecture/design document surfaces.
- Stale or orphaned document-family references.
- Remediation notes for surface coverage cleanup.

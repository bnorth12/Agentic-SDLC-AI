---
name: implementation-architecture-alignment-auditor
description: "Audit implementation shape against approved architecture and design artifacts for governance parity."
---
# Implementation Architecture Alignment Auditor Skill

## Purpose

Check whether implementation artifacts, tests, and scripts conform to the approved architecture and design model.

## Inputs

- Source implementation under src/, frontend/src/, and scripts/
- Architecture and design artifacts under docs/architecture/ and docs/design/
- Verification evidence under Tests/
- Independent review outputs under independent_reviews/

## Procedure

1. Map implementation artifacts to the governing architecture and design references.
1. Flag implementation-only behavior that lacks an architecture/design anchor.
1. Flag architecture/design expectations that are not represented in the implementation.
1. Record contract drift, boundary mismatches, and missing evidence legs.
1. Return prioritized remediation notes for alignment cleanup.

## Outputs

- Implementation-to-architecture alignment gaps.
- Design-only concepts that need implementation follow-through.
- Implementation-only artifacts lacking architecture/design trace.
- Remediation notes for governance closeout.

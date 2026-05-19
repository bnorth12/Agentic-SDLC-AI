# Software Development Plan

## Plan ID

SDP-001

## Purpose

Define how software capabilities are planned, developed, integrated, verified, and released in alignment with governance policies.

This plan now includes a **Skills Layer** implementation approach: reusable engineering-discipline capabilities that are composed onto agents and enforced at gates.

## Inputs

- Approved requirements baseline
- Approved architecture baseline
- Prioritized backlog and sprint commitments

## Development Lifecycle

1. Intake and decomposition into work items
2. Design and interface confirmation
3. Implementation in controlled branches
4. Unit and integration verification
5. Board and HITL gate review
6. Release preparation and baseline tagging

## Skills Layer Technical Architecture

### Objective

Introduce a modular skill system that keeps agent authority intact while extracting reusable discipline logic (requirements quality, threat modeling, traceability, test design, release readiness).

### Core Components

1. Skill contract schema
2. Skill registry and versioning
3. Agent-skill binding configuration
4. Skill execution engine
5. Gate skill-evidence validator
6. Skill telemetry and audit trail hooks

### Minimum Skill Contract

Each skill implementation shall define:

- metadata: id, discipline, owner-agent roles, version
- input schema and required upstream artifacts
- output schema and produced evidence artifacts
- policy and gate mapping
- confidence and escalation logic
- traceability link generation rules

### Runtime Integration Path

1. Supervisor selects agent for current phase
2. Agent invokes required skills based on gate policy
3. Skill outputs are merged into structured evidence payload
4. Gate validator checks mandatory skill evidence
5. HITL package includes agent decision plus skill evidence bundle

## Engineering Rules

- Work shall be requirement-linked before implementation starts.
- Pull requests shall reference work items and affected requirements.
- Code changes shall include tests or explicit testing rationale.
- Merge decisions shall include quality evidence.
- Skills shall be implemented as reusable modules, not duplicated in agent prompts.
- Mandatory skills for a gate shall fail CLOSED when evidence is missing.

## Sprint Structure

- Sprint planning: goals, scope, dependencies, risk review
- Execution: daily status and blocker escalation
- Validation: test and lint completion
- Review: demonstration of capability and trace links
- Retrospective: process and quality improvements

### Skills Delivery Overlay

- Sprint 4: skill framework + first P0 skills (Requirements Quality, Traceability Synthesis)
- Sprint 5: remaining P0 + P1 verification skills (Architecture Allocation, Threat and Hazard, Test Design, Configuration Baseline)
- Sprint 6: telemetry, observability, and confidence trend reporting for skills
- Sprint 7-8: advanced skills (Release Readiness, Data Governance, Operational Reliability, Compliance Packaging)

## Exit Criteria per Increment

- Requirement traceability complete
- Architecture impact assessed
- Tests passing at required scope
- Security and safety checks complete
- Configuration baseline updated
- Required skills for targeted gates implemented, versioned, and validated
- Skill output schemas and policy checks passing in CI

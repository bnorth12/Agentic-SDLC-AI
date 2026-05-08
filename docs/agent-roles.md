# Agent Roles

## Supervisory Roles

### Program Manager
- **Responsibility:** Mission planning, milestone definition, priority management.
- **Authority:** Approves scope and release objectives.
- **Interactions:** Coordinates with Chief Engineer and governance boards.

### Chief Engineer
- **Responsibility:** Technical leadership and cross-domain arbitration.
- **Authority:** Approves architecture direction and integration strategy.
- **Interactions:** Delegates to specialist agents and triggers board reviews.

## Specialist SDLC Roles

### Systems Engineering Agent
- Defines system context, interfaces, and constraints.
- Maintains system-level traceability from objectives to design artifacts.

### Requirements Agent
- Produces structured, testable requirements.
- Manages change impact and requirement baseline updates.

### Safety/Security/Reliability Agent
- Performs hazard/threat analysis and reliability assessments.
- Escalates critical findings to HITL and review boards.

### Architecture Agent
- Produces logical/physical architecture candidates and trade studies.
- Aligns design decisions with non-functional requirements.

### Development Agent
- Generates implementation plans and code changes.
- Coordinates with Verification Agent on acceptance criteria.

### Verification & Validation Agent
- Creates test strategies, traceability, and evidence mapping.
- Validates implementation against requirements and safety constraints.

### Configuration Management Agent
- Maintains baselines, version metadata, and release manifests.
- Enforces branching, change control, and reproducibility checks.

## Review Boards (Subgraphs)

- **Design Review Board:** Architecture and interface consistency gate.
- **Safety/Security Review Board:** Risk acceptance gate.
- **Release Readiness Board:** Integration, validation, and deployment gate.

# Architecture

## System Overview

The platform uses a hierarchical **LangGraph** topology:

1. **Program Manager Supervisor** handles mission goals, scope, and release priorities.
2. **Chief Engineer Supervisor** manages technical decomposition and cross-discipline trade-offs.
3. **Specialist Agent Layer** executes role-specific tasks (requirements, architecture, development, verification, safety/security, configuration management).
4. **Review Board Subgraphs** enforce governance gates (design review, safety review, release readiness).

## High-Level Graph Design

Conceptual flow:

- Intake objective
- Decompose into SDLC work packages
- Route to specialist agents
- Aggregate artifacts into shared state
- Trigger board reviews at phase gates
- Escalate HITL interrupts for approvals/waivers
- Finalize and publish outcomes

## State Management

- Shared typed state model via Pydantic (`AgentState`)
- Persistent checkpoints (PostgreSQL) for resumable runs
- Explicit message and artifact channels for traceability
- Decision log entries for governance/audit

## HITL Flow

Human intervention is used for:

- Scope/requirement approval
- Safety/security critical decisions
- Architecture exceptions and waivers
- Release go/no-go decisions

Interrupt points are designed as explicit graph nodes so execution can pause safely and resume with approved context.

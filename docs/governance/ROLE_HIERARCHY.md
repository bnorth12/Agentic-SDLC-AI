# Role Hierarchy & Authority Matrix

**Document ID**: ROLE-001  
**Status**: APPROVED (Sprint 0-P1-001 complete)  
**Date**: May 9, 2026  
**Reviewed By**: Program Manager  

---

## Executive Summary

This document defines the organizational hierarchy for the Agentic-SDLC-AI governance system. Six core roles coordinate across the SDLC lifecycle, with clear authority levels, escalation paths, and success metrics.

**Principle**: Every decision has an owner (Accountable person). Escalation is triggered by defined confidence thresholds or risk conditions, never by ambiguity.

---

## Authority Hierarchy

```
Chief Engineer (APEX AUTHORITY)
├── Program Manager (Project leadership)
├── Requirements Agent (Requirement elicitation)
├── Architecture Agent (Technical design)
├── Code Review Board (Quality gates)
└── Deployment Manager (Release execution)
```

---

## Role Definitions

### 1. Chief Engineer — APEX AUTHORITY

**Title**: Chief Architect & Final Authority  
**Authority Level**: SUPREME (approves, rejects, overrides all decisions)

**Responsibilities**:
- Architecture approval and conflict resolution
- Escalation decisions (final arbitration)
- Safety and security risk assessment
- Authorization of high-impact changes
- Authority delegation to other roles

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Architecture Design | ✅ Yes | ✅ Yes | ✅ Yes (all) |
| Requirement Feasibility | ✅ Yes | ✅ Yes | ✅ Yes |
| Code Quality Waivers | ✅ Yes | ✅ Yes | ✅ Yes |
| Security/Safety Issues | ✅ Yes (mandatory) | ✅ Yes | ✅ Yes |
| Schedule/Resource Conflicts | Consults PM | — | ✅ Yes (tiebreaker) |
| Deployment Decision | Consults DM | ✅ Yes (if safety risk) | ✅ Yes |

**Escalation Triggers** (When to escalate TO this role):
- Inter-agent confidence gap > 50% on critical decision
- Architecture feasibility < 70% confidence
- Safety or security risk flagged
- Requirement conflicts blocking progress
- Schedule/resource disputes unresolved by PM

**Escalation Procedure**:
1. Agent flags escalation with evidence (confidence score, risk assessment, conflict description)
2. Chief Engineer reviews within 24 hours
3. Decision recorded in AUDIT_TRAIL.jsonl
4. Decision communicated to all affected parties
5. Implementation proceeds or rework requested

**Success Metrics**:
- Response time: ≤24 hours for escalations
- Decision clarity: 100% of decisions unambiguous (no follow-up questions)
- Authority acceptance: 0 disputes on CE decisions (final authority)
- Conflict resolution rate: ≥95% resolved without rework

**Example Escalation**:
> Requirements Agent proposes feature with 45% confidence (ambiguous acceptance criteria). Threshold = 80%. Escalates to Chief Engineer with evidence. CE reviews, decides: (a) requirements refined, (b) scope reduced, or (c) escalate to stakeholder. CE decision is final; work proceeds accordingly.

---

### 2. Program Manager — PROJECT LEADERSHIP

**Title**: Program Manager & Phase Gate Authority  
**Authority Level**: HIGH (approves phase transitions, resource allocation, schedule)

**Responsibilities**:
- Phase gate approvals (Requirements → Architecture → Implementation → Release)
- Resource allocation and schedule management
- Scope control (priority, change requests)
- Risk tracking and mitigation scheduling
- Cross-team coordination

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Phase Gate Transition | ✅ Yes (if criteria met) | ✅ Yes | No (CE can override) |
| Schedule Changes | ✅ Yes | ✅ Yes | No (CE arbitrates) |
| Scope Changes | ✅ Yes (prioritized) | ✅ Yes | No (CE arbitrates) |
| Resource Reallocation | ✅ Yes | ✅ Yes | No (CE arbitrates) |
| Requirement Completeness | Collaborates w/ Req Agent | Recommends | No (Req Agent decides) |

**Escalation Triggers**:
- Schedule risk (milestone at-risk or overdue)
- Scope creep (change requests threatening deadline)
- Resource conflicts (insufficient capacity)
- Gate readiness disputed (agent claims ready, but gate acceptance criteria not met)
- Requirement conflicts causing schedule impact

**Escalation Procedure**:
1. PM flags escalation with evidence (schedule burn-down, resource utilization, gate checklist)
2. Escalates to Chief Engineer if unresolved with relevant agent
3. CE makes final decision
4. PM executes decision and monitors for schedule impact

**Success Metrics**:
- On-time delivery: ≥95% of phases complete by planned date
- Scope adherence: <10% scope change post-commitment
- Gate pass rate: ≥90% phases pass gate on first submission
- Resource utilization: 80-95% team utilization (avoid underutilization or burnout)

---

### 3. Requirements Agent — STAKEHOLDER VOICE

**Title**: Requirements Engineer & Completeness Authority  
**Authority Level**: MEDIUM (owns requirement quality, completeness, prioritization)

**Responsibilities**:
- Requirement capture and elicitation
- Requirement decomposition (L1 → L2 → L3)
- Acceptance criteria definition
- Prioritization and conflict resolution (requirement-level)
- Completeness and orphan detection

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Requirement Completeness | ✅ Yes (≥80%) | ✅ Yes | No (PM/CE arbitrate) |
| Requirement Prioritization | ✅ Yes | ✅ Yes | No (CE if escalated) |
| Acceptance Criteria | ✅ Yes | ✅ Yes | No (PM if schedule impact) |
| Requirement Feasibility Assessment | Recommends | Escalates to Architecture | No (Arch Agent decides) |
| Scope Changes (requirement-level) | Proposes | Can reject | No (PM decides) |

**Escalation Triggers**:
- Requirement completeness < 80% confidence (ambiguous acceptance criteria, missing interfaces)
- Requirement conflicts (contradictory L1 requirements)
- Requirement feasibility challenge (architecture agent says "not feasible")
- Scope ambiguity > 20% (stakeholders disagree on priority)

**Escalation Procedure**:
1. Requirements Agent flags escalation with evidence (completeness score, conflict description, evidence)
2. If conflict is requirement-level → consult stakeholders
3. If feasibility concern → consult Architecture Agent (collaborative)
4. If conflict unresolved → escalate to Program Manager
5. If still unresolved → escalate to Chief Engineer

**Success Metrics**:
- Requirement completeness: ≥80% on first submission
- Change request rate: <15% requirement changes post-approval
- Orphan requirement rate: 0% (all L1 decomposed)
- Stakeholder satisfaction: ≥95% acceptance criteria clarity

---

### 4. Architecture Agent — TECHNICAL DESIGN AUTHORITY

**Title**: Solutions Architect & Design Authority  
**Authority Level**: MEDIUM (owns design decisions, technical feasibility, interface specs)

**Responsibilities**:
- Architecture decomposition (hardware, software, subsystems)
- Design trade-off analysis
- Technical feasibility assessment
- Component allocation to requirements
- Interface specification

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Architecture Design | ✅ Yes | ✅ Yes | No (CE can override) |
| Technical Feasibility | ✅ Yes | ✅ Yes (flags infeasible) | No (CE arbitrates) |
| Design Trade-offs | ✅ Yes | ✅ Yes | No (CE for high-risk) |
| Component-to-Requirement Mapping | ✅ Yes | ✅ Yes | No (Requirements Agent consults) |
| Interface Specifications | ✅ Yes | ✅ Yes | No (Dev Agent implements) |

**Escalation Triggers**:
- Architecture feasibility < 70% confidence (design complexity, technical risk)
- Design disagreement (multiple competing architectures)
- Requirement feasibility challenge (feature not implementable as specified)
- High-risk design pattern (security vulnerability, performance penalty)
- Interface complexity exceeding integration capacity

**Escalation Procedure**:
1. Architecture Agent flags escalation with evidence (feasibility score, risk assessment, competing designs)
2. If disagreement → present alternatives to Chief Engineer with trade-offs
3. CE makes final architecture decision
4. Implementation proceeds per CE decision

**Success Metrics**:
- Design completeness: ≥90% on first submission
- Feasibility confidence: ≥70% average across components
- Rework rate: <10% designs requiring major revision post-approval
- Peer review pass rate: ≥95% architecture reviews accept with <3 comments

---

### 5. Code Review Board — QUALITY GATES AUTHORITY

**Title**: Quality Assurance & Merge Authority  
**Authority Level**: MEDIUM (owns code quality, security, merge approval)

**Responsibilities**:
- Code quality enforcement (linting, complexity, style)
- Security scanning and vulnerability assessment
- Test coverage verification (≥85% target)
- Peer review coordination (2+ approvals required)
- Merge decision and conflict resolution

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Code Quality (linting/complexity) | ✅ Yes | ✅ Yes | No (CEO for waivers) |
| Test Coverage Threshold | ✅ Yes (≥85%) | ✅ Yes | No (CE for exceptions) |
| Security Issues | ✅ Yes (critical) | ✅ Yes | ✅ Yes (blocking) |
| Merge Approval | ✅ Yes (2+ reviewers) | ✅ Yes | No (CE if safety) |
| Code Review Waivers | No (escalates) | No (escalates) | No (CE decides) |

**Escalation Triggers**:
- Code quality threshold violations (complexity > 10, coverage < 85%)
- Security vulnerability found (any severity)
- Disagreement between reviewers (2+ approvals required, reviewer holds)
- High-risk code pattern (database schema change, auth bypass, etc.)
- Test coverage unexpectedly low (regression)

**Escalation Procedure**:
1. Code Review Board flags issue with evidence (metric violation, security scan result, reviewer disagreement)
2. If security issue → escalate to Chief Engineer immediately (blocking)
3. If coverage/complexity → author refactors and resubmits
4. If reviewer disagreement → third reviewer arbitrates
5. If unresolved → escalate to Chief Engineer

**Success Metrics**:
- Defect escape rate: <5% bugs reaching production
- Code review turnaround: ≤24 hours per review
- Merge success rate: ≥98% (minimal rollback)
- Security issue rate: 0 critical security issues merged

---

### 6. Deployment Manager — RELEASE AUTHORITY

**Title**: Release Manager & Operations Authority  
**Authority Level**: MEDIUM (owns deployment schedule, rollback, ops readiness)

**Responsibilities**:
- Deployment scheduling and readiness assessment
- Rollback procedure testing and execution (if needed)
- Production monitoring and incident response
- Release notes and deployment runbooks
- Operational risk assessment

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Deployment Schedule | ✅ Yes | ✅ Yes (if unready) | No (PM arbitrates) |
| Rollback Decision | ✅ Yes | ✅ Yes (if monitored risk) | ✅ Yes (emergency) |
| Release Readiness | ✅ Yes | ✅ Yes | No (CE for exceptions) |
| Ops Risk Assessment | ✅ Yes | ✅ Yes (blocking) | No (CE arbitrates) |
| Production Configuration | ✅ Yes | ✅ Yes | No (CE for security) |

**Escalation Triggers**:
- Deployment readiness < 90% confidence (monitoring not configured, runbook untested)
- Operational risk flagged (too many simultaneous deployments, incomplete rollback plan)
- Production incident during deployment
- Rollback needed (unplanned)
- Compliance or operational policy violation

**Escalation Procedure**:
1. Deployment Manager flags issue with evidence (readiness checklist, risk assessment, incident data)
2. If safety/compliance risk → escalate to Chief Engineer immediately (blocking)
3. If schedule risk → coordinate with Program Manager
4. If incident during deployment → declare war room, all parties respond

**Success Metrics**:
- Deployment success rate: ≥99% (minimal rollback)
- MTTR (Mean Time to Recovery): <30 min if rollback needed
- Unplanned downtime: 0 minutes
- Deployment readiness score: ≥90% on average

---

## Escalation Decision Tree

```
Decision Point → Authority → Escalate To
├── Requirement completeness < 80%
│   └─ Requirements Agent → Program Manager → Chief Engineer
├── Architecture feasibility < 70%
│   └─ Architecture Agent → Chief Engineer
├── Code quality threshold violated
│   └─ Code Review Board → Chief Engineer (for waiver)
├── Deployment readiness < 90%
│   └─ Deployment Manager → Chief Engineer (if safety)
├── Agent confidence gap > 50%
│   └─ Either Agent → Chief Engineer (arbitration)
├── Safety/security risk flagged
│   └─ Any Agent → Chief Engineer (immediate)
└── Schedule/resource conflict
    └─ Program Manager → Chief Engineer (tiebreaker)
```

---

## Cross-Role Responsibilities

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|------------|-------------|-----------|----------|
| Gate Transition | Submitting Agent | Program Manager | Chief Engineer | All |
| Escalation Decision | Escalating Agent | Chief Engineer | Both Parties | All |
| Risk Mitigation | Assigning Agent | Chief Engineer | Program Manager | All |
| Performance Metrics | Each Role | Chief Engineer | All Roles | Leadership |
| Policy Compliance | Each Role | Chief Engineer | Governance Lead | All |

---

## Summary: Who Decides What?

**Chief Engineer decides:**
- Architecture (final design authority)
- Escalations (conflict arbitration)
- Safety/security waivers
- High-risk decisions

**Program Manager decides:**
- Phase gates (requirements met?)
- Schedule (we deliver when?)
- Scope (what's in this release?)
- Resource allocation

**Requirements Agent decides:**
- Requirement completeness (≥80%?)
- Prioritization (what's most important?)
- Acceptance criteria (done = what?)

**Architecture Agent decides:**
- Technical feasibility (can we build it?)
- Design decomposition (how to structure?)
- Interface specs (how do components talk?)

**Code Review Board decides:**
- Code quality (does it pass checks?)
- Security (any vulns?)
- Merge approval (ready to production?)

**Deployment Manager decides:**
- Deployment readiness (safe to deploy?)
- Rollback (when to undo?)
- Production configuration

---

## Authority Non-Negotiables

1. **Every decision has one Accountable person** (no shared accountability)
2. **Escalation is never optional** when confidence < threshold
3. **Chief Engineer is apex authority** (final say on conflicts, per USAF Acquisition & NASA-STD-7009A)
4. **No role can override another role's core decision** (except as noted above)
5. **All escalations recorded in audit trail** (traceability required per CMMI)
6. **Security & Safety decisions non-delegable** (Chief Engineer sole authority, per USAF SSE & MIL-STD-882G)

---

## Reference Standards

This role hierarchy derives from industry-standard SE processes:

- **INCOSE Systems Engineering Handbook**: Role definitions, responsibilities
- **NASA-STD-7009A**: Technical review authority, gate decision-making
- **USAF Acquisition Strategy**: Phase gate authority, program management
- **USAF System Security Engineering**: Security decision authority
- **MIL-STD-882G**: Safety decision authority, risk acceptance
- **CMMI v2.0**: Process ownership clarity, traceability

See [docs/references/REFERENCES.md](../references/REFERENCES.md) for complete standards mapping.
See [docs/references/USAF_SSE_REFERENCE.md](../references/USAF_SSE_REFERENCE.md) for security role details.
See [docs/references/SAFETY_STANDARDS_REFERENCE.md](../references/SAFETY_STANDARDS_REFERENCE.md) for safety role details.

---

## Reference Standards

This role hierarchy derives from industry-standard SE processes:

- **INCOSE Systems Engineering Handbook**: Role definitions, responsibilities
- **NASA-STD-7009A**: Technical review authority, gate decision-making
- **USAF Acquisition Strategy**: Phase gate authority, program management
- **USAF System Security Engineering**: Security decision authority
- **MIL-STD-882G**: Safety decision authority, risk acceptance
- **CMMI v2.0**: Process ownership clarity, traceability

See [docs/references/REFERENCES.md](../references/REFERENCES.md) for complete standards mapping.

# Agent Communication Protocol

**Document ID**: PROTO-COMM-001  
**Date**: May 12, 2026  
**Scope**: How 13 agents in Agentic-SDLC-AI governance framework communicate, escalate, and coordinate  
**Authority**: Chief Engineer (apex), Program Manager (mediator), Domain Experts (CSO/CSafO/CCO)

---

## Overview

This protocol defines:
- **Communication channels** (async, sync, meetings)
- **Escalation paths** (when & how to escalate)
- **Meeting cadences** (gate meetings, standups, escalation reviews)
- **Decision authority** (who decides what, and when)
- **Notification rules** (who gets informed of what, and when)

**Core Principle**: Agents communicate **asynchronously by default** (async-first). Synchronous meetings only for gate decisions, escalation resolution, or blocked decisions.

---

## 13-Agent Organization

```
APEX
└─ Chief Engineer (CE)

LEADERSHIP
├─ Program Manager (PM)

DOMAIN EXPERTS (Report to CE)
├─ Requirements Manager (RM)
├─ System Architect (Arch)
├─ Chief Security Officer (CSO)
├─ Chief Safety Officer (CSafO)
├─ Chief Compliance Officer (CCO)

SUPPORTING (Report to CE)
├─ Cyber/Security Architect (Cyber Arch)
├─ Code Review Board (CRB)
├─ QA Manager (QA)
├─ Integration & Test Manager (I&T)
├─ Operations Lead (Ops)
├─ Supplier Quality Manager (SQM)
└─ Data/Traceability Manager (DTM)
```

---

## Communication Channels

### 1. **Async-First: Shared Repository** (Primary)

**Medium**: Shared documents (Google Drive, Confluence, or GitHub)

| Channel | Content | Update Cadence | Read By |
|---------|---------|---|---|
| **Daily Standup Log** | Each agent's progress, blockers, decisions | Daily (EOD) | All agents + PM |
| **Risk Register** | Identified risks, owner, mitigation plan | After risk event | CSO + CSafO + PM + CE |
| **Decision Log** | All gate decisions, risk acceptance memos | As decisions made | All agents + CCO |
| **RACI Tracker** | Activity status per agent per phase | Weekly | RM + PM + CE |
| **Escalation Queue** | Pending escalations + status | Real-time | PM + CE |

**Protocol**:
- Agents post updates in structured format (markdown tables preferred)
- No approval required; post immediately
- CCO periodically audits for completeness & consistency
- Async reduces meeting load by ≥50%

---

### 2. **Synchronous: Gate Review Meetings** (Scheduled)

**Timing**: At each gate (Requirements, Architecture, Implementation, Deployment)

| Gate | Meeting Name | Duration | Attendees | Decision |
|------|---|---|---|---|
| **Phase 1** | Requirements Review Board (RRB) | 2 hours | RM, CSO, CSafO, CCO, PM, CE | PASS / CONDITIONAL / FAIL |
| **Phase 2** | Design Review Board (DRB) | 2.5 hours | Arch, CE (chair), CSO, CSafO, CCO, PM | PASS / CONDITIONAL / FAIL |
| **Phase 3** | Code Inspection Board (CIB) | 2 hours | CRB, QA, CSO, CSafO, CCO | PASS / CONDITIONAL / FAIL |
| **Phase 5** | Deployment Readiness Review (DRR) | 2 hours | PM, CE, CSO, CSafO, CCO, Ops | PASS / CONDITIONAL / FAIL |

**Meeting Protocol**:
1. Pre-gate review (2-3 days before) by gatekeeper
2. 24-hour notice with agenda + key metrics
3. Vote at meeting
4. Decision record published same day
5. Risk memos (if CONDITIONAL) signed within 48 hours

---

### 3. **Escalation Meetings** (On-Demand)

**Timing**: Within 24 hours of escalation trigger

| Escalation Type | Duration | Attendees | Decision Authority |
|---|---|---|---|
| **Resource Conflict** (PM vs Arch on feasibility) | 1 hour | PM, Arch, CE | CE decides |
| **Schedule-Quality Trade-off** (PM wants fast, CSO wants thorough) | 1 hour | PM, CSO, CSafO, CE | CE decides (with CSO/CSafO input) |
| **Risk Threshold Disagreement** (CSO thinks risk too high vs PM tolerance) | 1 hour | CSO, PM, CE | CSO proposes, CE approves |
| **Safety-Critical Waiver** (CSafO objects to design) | 1.5 hours | CSafO, Arch, CE | CE decides with CSafO concurrence |
| **High-Risk Vulnerability** (Critical security flaw found late) | 0.5 hours (emergency) | CSO, CRB, CE | Fix immediately or escalate to PM |

**Escalation Entry Criteria**:
- Agents cannot agree within 48 hours
- Decision blocks progress for >1 week
- Risk threshold exceeded
- Safety/security violation detected

---

### 4. **Standups** (Lightweight, Async)

**Frequency**: Weekly (Fridays EOD), or Daily if in critical phase

**Format**: Each agent posts 3-bullet update in shared doc:
```
[Agent Name] - [Date]
- ✅ Completed this week: [item]
- 🔄 In progress: [item]
- 🚧 Blocked by: [item] (owner, target resolution)
```

**No meeting required**. Async updates only.

**Exception**: If ≥2 agents report blocking each other → trigger 30-min sync standup to resolve.

---

## Escalation Paths

### **Escalation Decision Tree**

```
Conflicting Agents
    ↓
[Try to resolve async - 48 hours]
    ↓
Success? Yes → Document in Decision Log, Done
    ↓
No → Trigger Escalation Meeting
    ↓
Escalation Type?
    ├─ Resource/Schedule → PM + Arch (or involved agents) + CE
    ├─ Risk/Quality → CSO/CSafO + PM + CE  
    ├─ Compliance → CCO + PM + CE
    └─ Technical Feasibility → CE + relevant experts
    ↓
CE Decision (with domain expert input)
    ↓
Document in Decision Log + Risk Register
    ↓
Notify all stakeholders (1 hour after decision)
```

### **Escalation Authority Chain**

1. **Level 1** (Resolve locally): Two agents directly involved
   - **Owner**: First agent to identify conflict
   - **Action**: Post in shared channel, attempt resolution within 48 hours
   - **Escalate if**: No agreement by deadline

2. **Level 2** (Mediation): PM + relevant domain expert
   - **Owner**: PM (mediator role)
   - **Action**: 1-hour mediation meeting within 24 hours
   - **Escalate if**: Still unresolved

3. **Level 3** (CE Authority): Chief Engineer decides
   - **Owner**: CE (apex authority)
   - **Action**: Review both sides, make decision, document rationale
   - **Decision Authority**: CE has final authority on:
     - Resource allocation (budget, staffing, schedule)
     - Risk acceptance (residual risk memo)
     - Architecture trade-offs
     - Waiver/exception approval

---

## Decision Authority Matrix

| Decision Type | Authority | Input From | Notes |
|---|---|---|---|
| **Threat Definition & Risk Scoring** | CSO | PM, Arch | CSO owns threat decisions; can override Arch design if threat not addressed |
| **Hazard Definition & Risk Scoring** | CSafO | PM, Arch | CSafO owns hazard decisions; can override Arch design if fault tolerance not addressed |
| **Risk Threshold Acceptance** | CSO (threats) + CSafO (hazards) | PM, CE | If risk exceeds threshold, CSO/CSafO decide if mitigation required or accepted |
| **Requirements Completion** | RM | PM, CSO, CSafO | RM decides when requirements complete; CSO/CSafO input on threat/hazard traceability |
| **Architecture Feasibility** | CE (approval authority) | Arch, PM | CE approves architecture or rejects as infeasible; if <70% feasibility → rework required |
| **Code Quality Gates** | CRB (code review), QA (test) | CSO (security), CSafO (safety) | CRB approves code quality; CSO/CSafO can flag security/safety issues blocking gate |
| **Residual Risk Acceptance** | CE (final authority) | CSO, CSafO | CE co-signs residual threat/hazard acceptance with CSO/CSafO |
| **Deployment Approval** | CE (final authority) | PM, Ops, CSO, CSafO | CE authorizes deployment or holds for risk mitigation |
| **Compliance Certification** | CCO | All agents (evidence providers) | CCO assembles evidence & recommends certification; certifying authority decides |
| **Exception/Waiver** | CE | Relevant domain expert | CE approves exceptions (e.g., CC >10 for state machine, MISRA deviation) |

---

## Notification Rules

### **Who Gets Notified of What**

| Event | Notification | Recipients | Timing |
|---|---|---|---|
| **Gate Decision Made** | PASS / CONDITIONAL / FAIL | All agents | Same day |
| **Risk Accepted** | Risk Acceptance Memo | All agents + stakeholders | Within 48 hours |
| **Escalation Triggered** | Escalation Alert | PM, CE + involved agents | Immediately |
| **Escalation Resolved** | CE Decision Memo | All agents | Within 24 hours |
| **Threat/Hazard Found** | Risk Register update | CSO/CSafO + PM | Within 24 hours |
| **High-Risk Vulnerability** | Security Alert | All agents | Immediately (emergency) |
| **Safety-Critical Defect** | Safety Alert | All agents | Immediately (emergency) |
| **Schedule Impact** | Schedule Update | PM, CE + affected agents | Within 24 hours |
| **Compliance Gap** | Compliance Alert | CCO, PM, CE | Within 24 hours |

---

## Meeting Cadence Summary

| Meeting | Frequency | Duration | Attendees | Purpose |
|---|---|---|---|---|
| **Weekly Standup** | Every Friday EOD | Async | All agents | Progress update |
| **Requirements Gate (RRB)** | End of Phase 1 | 2 hours | RM, CSO, CSafO, CCO, PM, CE | Gate decision |
| **Architecture Gate (DRB)** | End of Phase 2 | 2.5 hours | Arch, CE, CSO, CSafO, CCO, PM | Gate decision |
| **Implementation Gate (CIB)** | End of Phase 3 | 2 hours | CRB, QA, CSO, CSafO, CCO | Gate decision |
| **Deployment Gate (DRR)** | End of Phase 5 | 2 hours | PM, CE, CSO, CSafO, CCO, Ops | Gate decision |
| **Escalation Meeting** | On-demand (within 24 hours) | 0.5-1.5 hours | Involved agents + PM/CE | Resolve conflict |
| **Post-Phase Retrospective** | After each phase | 1 hour | All agents | Lessons learned |

---

## Async Communication Best Practices

**1. Structured Updates**
- Use Markdown tables, numbered lists, bullet points
- Never narrative paragraphs (hard to scan)
- Include decision/recommendation at top

**2. Clear Ownership**
- Every agenda item has one owner
- Owner posts update & calls for input
- Reviewers have 24 hours to comment

**3. Default to Yes**
- If no objection within 48 hours, decision is approved
- Async consent (not explicit approval needed)
- Exception: Gate decisions require explicit vote

**4. Document Everything**
- Decisions logged in Decision Log with rationale
- Risk accepted → Risk Acceptance Memo
- Escalations → Escalation Decision Record
- Nothing verbal without written follow-up

---

## Crisis Communication (High-Priority Issues)

### **When to Escalate Immediately** (Same-Day Meeting)

- **Critical Security Vulnerability**: Exploitable flaw found in production code
  - **Owner**: CSO
  - **Response**: Emergency meeting within 2 hours, fix assigned, timeline 48 hours

- **Safety-Critical Defect**: Failure mode not handled in safety-critical code
  - **Owner**: CSafO
  - **Response**: Emergency meeting within 2 hours, fix assigned, timeline 48 hours

- **Blocked Deployment**: Unresolved blocker found at DRR gate
  - **Owner**: PM
  - **Response**: Emergency meeting within 4 hours, decision on proceed/hold

- **Compliance Violation**: Gap discovered post-gate
  - **Owner**: CCO
  - **Response**: Assessment within 24 hours, mitigation plan by 48 hours

---

## Communication Channels Implementation

**Recommended Tools**:
- **Async Documents**: GitHub (docs/ folder) for RACI, decision logs, risk registers
- **Standup Log**: GitHub Issues (pinned daily summary issue)
- **Decision Log**: GitHub (docs/governance/DECISION_LOG.md) updated real-time
- **Real-Time Chat** (optional): Slack/Teams for urgent escalations only (with GitHub follow-up)
- **Meetings**: Zoom/Teams recorded to GitHub archive

**Archive**:
- All decisions in DECISION_LOG.md (version controlled)
- All risk acceptance memos in docs/governance/RISK_ACCEPTANCE_MEMOS/ (by date)
- All escalation records in docs/governance/ESCALATION_LOG.md (version controlled)

---

## Decision Log Template

```markdown
## Decision Log - [Date]

### Decision ID: [DEC-YYYYMMDD-###]
**Date**: [Date]
**Owner**: [Agent Name]
**Decision**: [What was decided]
**Rationale**: [Why this decision]
**Input From**: [Who was consulted]
**Status**: Approved / Pending / Blocked
**Related Risks**: [If applicable]
**Implementation**: [Who executes, timeline]

### Decision ID: [DEC-YYYYMMDD-###]
...
```

---

## Escalation Decision Record Template

```markdown
## Escalation Record - [Date]

### Escalation ID: [ESC-YYYYMMDD-###]
**Date**: [Date]
**Triggered By**: [Agent Name]
**Issue**: [What was escalated]
**Parties**: [Agents involved]
**Escalation Level**: Level 2 / Level 3
**Meeting Date**: [Date/Time]
**Attendees**: [Names]
**Decision**: [What was decided]
**Decision Maker**: [CE/PM/Domain Expert]
**Rationale**: [Why this decision]
**Follow-Up Actions**: [What happens next]
**Target Resolution**: [Timeline]
```

---

## Success Criteria

| Metric | Target | Measured By |
|---|---|---|
| **Async Resolution Rate** | ≥90% of decisions made async | Decision Log analysis |
| **Escalation Time** | From trigger → decision ≤3 days | Escalation Log timestamps |
| **Gate Decision Timeliness** | Within 24 hours of gate meeting | Gate Decision Records |
| **Meeting Efficiency** | Gate meetings ≤±10 min from scheduled time | Meeting logs |
| **Notification Compliance** | 100% of stakeholders notified per rules | Notification audit |
| **Document Completeness** | Every decision documented within 24 hours | Decision Log audit |
| **Crisis Response** | Critical issues mitigated within 48 hours | Escalation Log |

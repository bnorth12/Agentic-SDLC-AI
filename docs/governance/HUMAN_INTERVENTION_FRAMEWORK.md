# Human Intervention Framework

**Document ID**: FRAME-HUMAN-001  
**Date**: May 12, 2026  
**Scope**: When, how, and why humans can override or intervene with agent decisions  
**Authority**: Chief Engineer (apex), Program Manager (stakeholder mediator), Executive Steering Committee (strategic override)

---

## Overview

**Core Principle**: Agents make routine decisions autonomously. Humans intervene only when:
1. **Decision threatens project success** (schedule, budget, legal, strategic)
2. **Agent authority exceeded** (conflict needs CE or executive decision)
3. **External constraint discovered** (customer demand, legal requirement, vendor change)
4. **Risk acceptance crosses organizational threshold** (requires executive sign-off)

---

## Decision Hierarchy

```
Routine Agent Decision (Autonomous)
    ↓ [No human override needed]
    ↓
Issue Resolved
    ↓
Escalation-Level Decision (Requires CE Review)
    ├─ Architecture feasibility gate
    ├─ Risk acceptance memo
    ├─ Resource allocation conflict
    ├─ Schedule slip
    └─ Safety-critical waiver
    ↓
    [CE Review → Approve / Reject / Escalate]
    ↓
Executive Decision (Requires Steering Committee Override)
    ├─ Cancel/delay phase
    ├─ Accept unacceptable risk (re-baseline risk threshold)
    ├─ Major scope change
    ├─ Budget increase >10%
    └─ Strategic pivot
    ↓
    [Steering Committee Vote → Program proceeds with new constraints]
```

---

## Intervention Scenarios

### **Scenario 1: CE Override (Architecture Redesign Needed)**

**Trigger**: CE reviews architecture at DRB gate; concludes design is not feasible enough

**Symptoms**:
- Feasibility <70%
- Multiple high-risk components
- COTS components unproven
- Technology stack conflicts with requirements

**Intervention Process**:
1. **CE Assessment** (2-3 days before gate): "Design is 55% feasible. Recommend redesign."
2. **Architect Response** (1 day): Architect proposes contingencies or argues feasibility score
3. **CE Decision** (1 day before gate):
   - **Option A**: "Approve with conditions (feasibility checks in Implementation phase)"
   - **Option B**: "Require redesign; gate delayed 2 weeks"
   - **Option C**: "Reject; fundamentally unachievable; escalate to Steering Committee"
4. **Notification**: Decision memo to all agents; gate schedule updated if needed

**Authority**: CE (final decision)

**Risk Management**: Decision documented in gate record + risk register

---

### **Scenario 2: Risk Acceptance Override (Executive Threshold Exceeded)**

**Trigger**: Residual threat/hazard assessment shows risk exceeding program threshold

**Symptoms**:
- CSO: "Residual threats = 3 Critical + 2 Major; risk above threshold"
- CSafO: "Residual failures = 2 Catastrophic; unacceptable without mitigation"
- PM wants to proceed anyway due to schedule pressure

**Intervention Process**:
1. **CSO/CSafO Assessment**: Post residual risk quantification in shared doc (threats, probabilities, consequences)
2. **Risk Acceptance Proposal**: "Residual risk = HIGH. Mitigation options: A) Redesign (2 weeks), B) Operational monitoring + quick fix (1 week)"
3. **CE Review**: 
   - If residual risk ≤ program threshold: **CE approves** residual risk memo
   - If residual risk > program threshold: **CE escalates to Steering Committee**
4. **Executive Steering Committee Decision** (if needed):
   - "Accept residual risk; proceed at own risk" (Steering Committee signs acceptance)
   - "Require mitigation; delay deployment" (Schedule slips)
   - "Accept partial mitigation; monitor in operations" (Operational risk acceptance)
5. **Notification**: Risk Acceptance Memo signed by all authorities + distributed to stakeholders

**Authority**: CE (if within program threshold) / Steering Committee (if exceeds organizational threshold)

**Example**:
- CSO: "Residual threat = Data exfiltration. Probability = 5% annually. Consequence = Critical (data loss). Risk = 5% × Critical = MEDIUM-HIGH."
- Program Threshold: "MEDIUM risk acceptable"
- CE: "Risk = MEDIUM-HIGH, exceeds threshold. Escalate to Steering Committee."
- Steering Committee: "Accept risk. Implement operational monitoring (daily log review)."

---

### **Scenario 3: Schedule Slip Intervention**

**Trigger**: Gate delay threatens project schedule

**Symptoms**:
- Requirements gate needs 4 weeks instead of 2 (threat analysis delays)
- Architecture phase blocked waiting for Requirements approval
- Customer delivery date at risk

**Intervention Process**:
1. **Agent Escalation**: CSO posts: "Threat analysis requires 4 weeks; cannot compress without quality loss."
2. **PM Assessment** (24 hours): Calculate downstream impact on schedule
3. **Trade-Off Options** (for PM/CE decision):
   - **Option A**: "Accept 4-week delay; push delivery date back 4 weeks"
   - **Option B**: "Compress threat analysis to 2 weeks; accept residual risks unanalyzed → Risk Acceptance Memo"
   - **Option C**: "Parallel processing: Requirements & Architecture phases overlap; accept increased risk"
4. **CE Review**: CE assesses feasibility & risk of selected option
5. **Steering Committee Review** (if delivery date affected):
   - If ≤2 week slip: CE approves
   - If >2 week slip: Steering Committee must approve (customer impact, budget)
6. **Decision Memo**: Posted with schedule change justification

**Authority**: CE (≤2 weeks) / Steering Committee (>2 weeks)

---

### **Scenario 4: Safety-Critical Waiver Request**

**Trigger**: CSafO requests exception (e.g., safety-critical code has CC=12 instead of ≤10)

**Symptoms**:
- Complex state machine (hard to simplify)
- Cyclomatic Complexity violation justified by architecture
- CSafO argues: "Refactoring creates new risks; current design acceptable"

**Intervention Process**:
1. **CSafO Justification** (2-3 days before gate): "CC=12 justified by state transitions. Refactoring introduces new call paths (risk). Current design acceptable with ≥2 reviews."
2. **CRB Assessment** (1 day): "Code is well-structured despite CC=12. Risk of refactoring may exceed benefit."
3. **CE Decision** (1 day before gate):
   - **Approve Waiver**: "CC=12 waiver approved with condition: ≥2 expert reviews completed (already done)"
   - **Request Refactor**: "Attempt refactoring. If not feasible in 2 days, waiver approved."
   - **Reject Waiver**: "Not acceptable; must refactor or redesign component"
4. **Documentation**: Waiver recorded in gate decision record + exception log

**Authority**: CE (for MISRA/quality waivers)

**Post-Implementation Tracking**: If waiver approved, component flagged for extra scrutiny during code review & testing phases.

---

### **Scenario 5: Vendor/COTS Component Change**

**Trigger**: Selected COTS component becomes unavailable or has critical vulnerability

**Symptoms**:
- Vendor announces end-of-life (EOL) on component used in architecture
- Security vulnerability discovered in COTS library
- Supplier changes (new vendor, new pricing, lead time uncertainty)

**Intervention Process**:
1. **SQM Alert** (immediate): "COTS Component X EOL announced. Replacement options: A, B, C"
2. **Architect Assessment** (2-3 days): Evaluate replacement options for architectural impact
3. **CE Review** (2-3 days): Assess impact on feasibility, schedule, cost
4. **Decision**:
   - **Option A**: "Use alternative component; no schedule impact" (Gate proceeds)
   - **Option B**: "Use alternative component; requires 2-week re-test" (Schedule slips)
   - **Option C**: "Vendor still supporting component for 3 more years; acceptable risk" (Gate proceeds)
5. **Steering Committee Review** (if schedule/cost impact):
   - If cost increase >$50K or schedule slip >2 weeks: Steering Committee approval needed
6. **Notification**: Component change documented in architecture record + risk register

**Authority**: CE (if no schedule impact) / Steering Committee (if schedule/cost impact)

---

### **Scenario 6: Compliance Requirement Changes**

**Trigger**: New regulation or certification requirement discovered post-gate

**Symptoms**:
- Customer adds certification requirement (e.g., "must be DO-326A compliant")
- Regulatory change (e.g., EU regulations on data processing)
- Audit findings require additional controls

**Intervention Process**:
1. **CCO Alert** (immediate): "New compliance requirement discovered: [requirement]. Impact assessment: [what changes]"
2. **CCO Analysis** (2-3 days): Determine scope & implementation cost
3. **Steering Committee Review** (3-5 days):
   - If cost <$50K + <1 week schedule: CE approves inclusion
   - If cost >$50K or >1 week schedule: Steering Committee decides (incorporate now vs. defer to next release)
4. **Decision**:
   - **Option A**: "Incorporate in current phase; schedule slips 1 week"
   - **Option B**: "Defer to next release; current release non-compliant (accept risk)"
   - **Option C**: "Incorporate as post-deployment patch" (operational risk)
5. **Documentation**: Compliance change documented + risk memo

**Authority**: CE (minor changes) / Steering Committee (major changes)

---

### **Scenario 7: Executive Escalation (Strategic Override)**

**Trigger**: Non-technical business decision overrides technical recommendation

**Symptoms**:
- Customer executive demands feature not in requirements
- Competitor product forces strategy change
- Budget constraints force cost-cutting
- Merger/acquisition changes priorities

**Intervention Process**:
1. **Executive Request** (to PM/CE): "We need to [add feature / cut scope / change direction]"
2. **Impact Assessment** (PM + relevant agents):
   - Schedule impact
   - Budget impact
   - Technical feasibility
   - Risk impact
3. **Steering Committee Review** (24-48 hours):
   - Vote on whether to approve executive request
   - If approved: document scope change + new constraints
   - If denied: explain to executive why change not feasible
4. **Execution**:
   - If approved: Add to backlog; re-baseline schedule/budget; notify all agents
   - Gate timeline may shift; affected activities re-planned

**Authority**: Steering Committee (strategic decisions)

**Risk Management**: Change documented as **Program Change Request (PCR)** with traceability to new requirements

---

## Intervention Authority Matrix

| Decision Type | Authority | Conditions | Escalation If |
|---|---|---|---|
| **Architecture Redesign** | CE | Feasibility <70% | Impossible to achieve ≥70% → Steering Committee |
| **Schedule Slip ≤2 weeks** | CE | Agent justification + PM impact assessment | Slip >2 weeks → Steering Committee |
| **Schedule Slip >2 weeks** | Steering Committee | Customer delivery impact | Stakeholder disagreement → Executive escalation |
| **Risk Acceptance (Program Threshold)** | CE + Domain Expert | CSO/CSafO concurrence | Risk exceeds organizational threshold → Steering Committee |
| **Risk Acceptance (Organizational Threshold)** | Steering Committee | Executive decision-making authority | N/A |
| **Waiver/Exception** | CE | Justification + mitigation plan | Waiver affects safety/security critically → Steering Committee |
| **Vendor/COTS Change** | CE (≤$50K, ≤1 week) / Steering Committee (>$50K, >1 week) | SQM assessment + impact analysis | Cost/schedule threshold exceeded → Steering Committee |
| **Compliance Requirement** | CE (minor) / Steering Committee (major) | CCO analysis + scope determination | Major scope change → Steering Committee |
| **Strategic Override** | Steering Committee | Executive business decision | Non-negotiable |

---

## Intervention Process Template

### **Human Intervention Request Form**

```markdown
## Intervention Request - [Date]

### Request ID: [INT-YYYYMMDD-###]
**Requestor**: [Name + Role]
**Date Submitted**: [Date]
**Type**: Schedule Slip / Risk Acceptance / Waiver / Vendor Change / Compliance / Strategic
**Current Phase**: [Phase name]

**Current Situation**:
- [What is happening]
- [Why it requires intervention]
- [Current agent decision or recommendation]

**Requested Intervention**:
- [What do you want to change]
- [Why is change necessary]
- [Impact if NOT approved]

**Impact Assessment**:
- Schedule impact: [+X weeks / -X weeks / no change]
- Budget impact: [+$X / -$X / no change]
- Risk impact: [increases / decreases / neutral]
- Quality impact: [positive / negative / neutral]

**Authority Review**:
- Assigned to: [CE / Steering Committee]
- Review date: [Date]
- Status: Pending / Approved / Rejected / Conditional

**Decision**:
- Approved? Yes / No / Conditional
- Conditions (if applicable): [Terms]
- Decision maker: [Name + signature]
- Date decided: [Date]

**Follow-Up**:
- Implementation owner: [Name]
- Target implementation: [Date]
- Success criteria: [Measurable outcome]
```

---

## Intervention Success Criteria

| Metric | Target | Measured By |
|---|---|---|
| **Routine Decisions (No Override)** | ≥90% of decisions | Audit trail analysis |
| **CE Overrides** | <5% of all decisions | Intervention log |
| **Steering Committee Overrides** | <2% of all decisions | Intervention log |
| **Override Decision Time** | <3 days from request to decision | Intervention timestamps |
| **Override Implementation Time** | <7 days from approval to action | Intervention follow-up |
| **Stakeholder Satisfaction** | ≥75% agree override was justified | Post-intervention survey |
| **Override Alignment** | 100% follow agent authority hierarchy | Audit (authority chain verified) |

---

## Prevention: Reduce Intervention Need

### **1. Clear Authority Upfront**
- RACI matrix defined & communicated
- Authority boundaries explicit
- Decision rules published

### **2. Regular Reviews**
- Monthly Steering Committee briefing on governance health
- Quarterly agent performance review
- Identify patterns in interventions → address root causes

### **3. Escalation Preparation**
- Before escalating, agent prepares decision memo with options + recommendations
- Facilitates faster human decision-making

### **4. Risk Visibility**
- Risk register updated daily
- Escalation triggers identified early
- Intervention needed proactively, not reactively


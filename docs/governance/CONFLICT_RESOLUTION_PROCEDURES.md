# Conflict Resolution Procedures

**Document ID**: PROC-CONFLICT-001  
**Date**: May 12, 2026  
**Scope**: How to resolve disagreements between agents in Agentic-SDLC-AI governance  
**Authority**: Chief Engineer (apex decision maker), Program Manager (mediator), Domain Experts (authority in domain)

---

## Overview

Conflicts arise when:
- **Domain Experts disagree** on interpretation of risk/quality (CSO vs CSafO vs RM)
- **Schedule vs Quality trade-off** (PM wants fast, CSO/CSafO want thorough)
- **Resource Constraints** (Arch needs resources PM won't allocate)
- **Risk Acceptance** (CSO thinks threat unacceptable, PM wants to accept)
- **Technical Feasibility** (CE says design isn't feasible, Arch argues it is)

**Resolution Process**: Structured escalation with clear decision authority at each level.

---

## Conflict Types & Resolution Paths

### **Type 1: Domain Expert Disagreement** (Within Single Domain)

**Scenario**: RM and CSO disagree on whether threat analysis is "complete"
- RM: "We have 95% of threats identified, ship it"
- CSO: "We have 5 critical uncovered threat vectors, need 2 more weeks"

**Resolution Path**:

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| **1. Async Discussion** | Both post rationale in shared doc | RM + CSO | 24 hours |
| **2. Technical Review** | If technical disagreement, invite relevant expert (Arch, CRB, etc.) | Technical expert | 24 hours |
| **3. Mediation** | If still unresolved, PM mediates with domain expert input | PM + CSO | 24 hours |
| **4. Escalate to CE** | PM recommends decision to CE; CE decides | CE | 24 hours |

**Decision Authority**: 
- Within domain: Domain expert (CSO for security, CSafO for safety, RM for requirements)
- Cross-domain: CE (apex authority)

**Example Resolution**:
- CSO escalates: "Threat X critical, must be analyzed"
- CE reviews: "Allocate 1 week for analysis; include in Requirements gate"
- Decision: Schedule slips 1 week, but gate decision delays only 1 week (not 2)

---

### **Type 2: Schedule vs Quality Trade-Off**

**Scenario**: PM wants Requirements gate in 2 weeks; CSO says need 4 weeks for threat analysis
- PM: "We're behind schedule, customer impatient"
- CSO: "If we rush threat analysis, we miss critical threats → post-deployment vulnerability"

**Resolution Path**:

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| **1. Async Trade-Off Analysis** | CSO posts: "4 weeks needed for comprehensive analysis; 2 weeks acceptable for MVP threat model but with residual risk X" | CSO | 24 hours |
| **2. Risk Quantification** | CSO provides: residual threat list, consequence, probability if rushed | CSO | 24 hours |
| **3. PM Decision Point** | PM decides: accept residual risk (with Risk Acceptance Memo) or allocate 4 weeks | PM + CE input | 24 hours |
| **4. If Accepted** | Create Risk Acceptance Memo; CSO + PM sign; escalate to CE for approval | CSO + PM + CE | 48 hours |

**Decision Authority**: 
- PM decides trade-off, but CSO must concur on risk assessment
- CE reviews Risk Acceptance Memo for final approval

**Example Resolution**:
- PM: "2-week schedule non-negotiable; what's the residual risk if we go with MVP threat model?"
- CSO: "Residual threats = [list of 3 major threats unanalyzed]. Risk level = HIGH. Mitigation = monitor logs for exploit attempts in operations."
- CE: "Risk Acceptance Memo accepted. 2-week gate proceeds. CSO adds threat monitoring to operational procedures."

---

### **Type 3: Risk Threshold Disagreement**

**Scenario**: CSO thinks threat severity should be "Critical" (cost=$500K to mitigate); PM says "Major" (cost=$50K)
- CSO: "This attack vector allows data exfiltration. That's Critical impact."
- PM: "We can reduce attack surface by 90% with minor architectural change; residual risk acceptable."

**Resolution Path**:

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| **1. Technical Debate** | Both post technical analysis in shared doc | CSO + PM/Arch | 24 hours |
| **2. Threat Model Review** | Neutral expert (not CSO, not PM) reviews threat model & risk scoring | CRB or external auditor | 24 hours |
| **3. CE Hearing** | CE hears both sides; CSO advocates for high severity, PM advocates for lower mitigation cost | CE + CSO + PM | 1-hour meeting |
| **4. CE Decision** | CE decides on threat severity & mitigation requirement | CE | 24 hours after meeting |

**Decision Authority**: CE (with CSO technical input on threat severity)

**Examples**:
- **CE Decision 1**: "Agree with CSO. Threat is Critical. Allocate $500K mitigation."
- **CE Decision 2**: "Agree with PM approach. Reduce attack surface, accept residual risk with monitoring plan."
- **CE Decision 3**: "Split difference. $250K architectural improvement + operational monitoring for residual risk."

---

### **Type 4: Architecture Feasibility Disagreement**

**Scenario**: Arch proposes design; CE questions feasibility
- Arch: "Design is 70% feasible; we have contingency plans for unproven components"
- CE: "COTS components unproven for this use case; feasibility only 55%. Redesign required."

**Resolution Path**:

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| **1. Feasibility Scorecard** | Arch completes detailed feasibility scorecard per component | Arch | 2 days |
| **2. CE Review** | CE scores each component; flags low-confidence items | CE | 2 days |
| **3. Risk Mitigation Plan** | Arch proposes mitigation for low-feasibility items (contingencies, prototypes, etc.) | Arch | 3 days |
| **4. CE Decision** | CE reviews mitigation plan; approves if feasibility ≥70% achieved | CE | 2 days |

**Decision Authority**: CE (final authority on feasibility gate)

**Outcome Options**:
- **Approve**: Feasibility ≥70% with mitigations
- **Conditional**: Approve with feasibility checks in next phase
- **Reject**: Feasibility <70%; redesign required

---

### **Type 5: Code Quality Gate Disagreement**

**Scenario**: CRB approves code as MISRA-compliant (95%); CSO flags security patterns missing
- CRB: "Code passes MISRA scan, CC ≤10, no violations."
- CSO: "Code complies with style guide but doesn't implement threat mitigations (e.g., input validation pattern)."

**Resolution Path**:

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| **1. Technical Review** | CSO posts specific security gaps (e.g., "Function X missing input validation per threat ABC") | CSO | 24 hours |
| **2. CRB Analysis** | CRB reviews gap; confirms gap or disputes as non-critical | CRB + Dev | 24 hours |
| **3. Severity Assessment** | If confirmed: Is gap a show-stopper (critical) or minor (can be tracked for later)? | CSO + CRB | 24 hours |
| **4. Decision** | If critical: gate FAILS, dev fixes code, re-test. If minor: document in risk register, proceed. | CSO + CRB | 24 hours |

**Decision Authority**: CSO (security), CRB (code quality) - shared gate

**Example Resolution**:
- CSO: "Function parse_input() missing bounds checking. Per threat THR-012, attacker can cause buffer overflow."
- CRB: "Confirmed. Function needs bounds check before gate pass."
- Dev: "Added bounds check; re-scan passes MISRA ≥95%."
- Gate: **PASS**

---

### **Type 6: Safety-Critical Inspection Disagreement**

**Scenario**: QA says safety-critical code reviewed by ≥2 experts; CSafO says review was insufficient
- QA: "Code reviewed by Expert A + Expert B. Both signed off."
- CSafO: "Expert B is firmware specialist, not safety-critical expert. Needs 3rd reviewer with failure analysis expertise."

**Resolution Path**:

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| **1. Reviewer Qualification** | QA posts reviewer credentials; CSafO evaluates | QA + CSafO | 24 hours |
| **2. Expert Assignment** | If CSafO disputes credentials, CSafO nominates qualified expert | CSafO | 24 hours |
| **3. Additional Review** | Qualified expert conducts review | Qualified expert | 3-5 days |
| **4. Gate Decision** | If all experts concur on safety-critical mechanisms, gate proceeds | CSafO + QA | 24 hours after review |

**Decision Authority**: CSafO (safety expert authority)

**Outcome**: Code gate FAILS unless CSafO-approved experts review.

---

## Conflict Escalation Matrix

```
Conflict Detected
    ↓
[Level 1: Direct Resolution - 48 hours]
Agents discuss async, try to agree
    ↓
Resolved? → Document decision, close ticket
    ↓
Unresolved? → Escalate
    ↓
[Level 2: PM Mediation - 24 hours]
PM + domain expert hear both sides, recommend decision
    ↓
Agreed? → PM decision, document, implement
    ↓
Unresolved? → Escalate
    ↓
[Level 3: CE Authority - 24 hours]
CE reviews evidence, hears both sides (if needed), makes final decision
    ↓
CE Decision Final
Document in Decision Log, notify all parties
Implement immediately
```

---

## Conflict Resolution Priority Matrix

| Conflict Type | Priority | Resolution Path | Timeline |
|---|---|---|---|
| **Schedule vs Quality** | HIGH | Type 2 path (risk quantification) | 3 days |
| **Risk Threshold** | HIGH | Type 3 path (CE hearing) | 3 days |
| **Architecture Feasibility** | HIGH | Type 4 path (feasibility scorecard) | 5 days |
| **Domain Expert Disagreement** | MEDIUM | Type 1 path (mediation) | 3 days |
| **Code Quality** | MEDIUM | Type 5 path (CSO + CRB) | 2 days |
| **Safety Review** | HIGH | Type 6 path (CSafO authority) | 5 days |
| **Resource Conflict** | MEDIUM | PM allocation decision | 2 days |
| **Compliance Gap** | HIGH | CCO + CE escalation | 2 days |

---

## Conflict Prevention (Best Practices)

### **1. Clear Authority Upfront**

**RACI Matrix** (RACI_MATRIX.md) defines:
- Who is **Accountable** for each activity (one person, no shared A)
- Who is **Responsible** for execution (can be multiple)
- Who must be **Consulted** (input required)
- Who is **Informed** (FYI only)

**Effect**: Fewer conflicts because roles are clear upfront.

### **2. Periodic Re-Alignment Meetings**

**Frequency**: After each phase (5 gates total)

**Attendees**: All 13 agents + PM + CE (90 min)

**Agenda**:
- Review what conflicts occurred
- Analyze root cause (unclear roles? conflicting goals?)
- Adjust procedures to prevent recurrence
- Celebrate agreements that went smoothly

---

## Conflict Resolution Success Criteria

| Metric | Target | Measured By |
|---|---|---|
| **Conflicts Resolved at Level 1** | ≥80% of conflicts | Conflict Log |
| **Average Resolution Time** | <3 days from trigger to decision | Conflict Log timestamps |
| **Escalation to CE** | <20% of conflicts | Escalation Log analysis |
| **Post-Resolution Compliance** | 100% of decisions implemented as decided | Audit |
| **Stakeholder Satisfaction** | ≥80% agree decision was fair | Post-resolution survey |
| **Recurring Conflicts** | <5% same conflict twice | Conflict Log analysis |

---

## Conflict Documentation

### **Conflict Log Entry Template**

```markdown
## Conflict Record - [Date]

### Conflict ID: [CONF-YYYYMMDD-###]
**Date Identified**: [Date]
**Identified By**: [Agent Name]
**Parties**: [Agent 1, Agent 2, ...]
**Type**: Schedule vs Quality / Risk Disagreement / Feasibility / Other
**Issue Description**: [What is the disagreement]

**Agent 1 Position**: [Argument]
**Agent 2 Position**: [Argument]

**Async Discussion** (24 hours):
- [Posting 1 with date/time]
- [Posting 2 with date/time]
- Result: Resolved / Unresolved

**Escalation** (if unresolved):
- Escalated to: [PM / CE / Other]
- Meeting date: [Date/Time]
- Attendees: [Names]
- Decision: [What was decided]
- Decision Maker: [Name + title]
- Rationale: [Why this decision]

**Implementation**:
- Assigned to: [Owner]
- Target date: [Date]
- Status: In Progress / Complete

**Resolution Quality**:
- Both parties agree? Yes / No / Partially
- Will this recur? Yes / No / Unknown
- Preventive action: [For similar conflicts]
```

---

## Emergency Conflict Procedures

### **When Conflict Blocks Gate**

**Scenario**: Gate meeting scheduled, key decision still unresolved

**Procedure**:
1. **Attempt Quick Resolution** (30 min before gate): PM + involved agents try compromise
2. **If Unresolved**: Gate goes **CONDITIONAL** (not FAIL)
3. **Risk Acceptance Memo**: Covers unresolved conflict as accepted risk
4. **CE Reviews Memo**: CE approves conditional pass
5. **Follow-Up**: Conflict resolved within 48 hours post-gate

**Effect**: Gate progresses, but risk explicitly accepted & tracked.

### **When Conflict Threatens Schedule**

**Scenario**: Conflict unresolved for 5+ days, holding up phase progress

**Procedure**:
1. **Emergency CE Session** (within 24 hours): CE makes temporary decision
2. **Temporary Decision**: "We proceed with Option A for now. Revisit in Phase X."
3. **Risk Register Entry**: Conflict documented as ongoing risk
4. **Resolution by**: [Specific date]

**Effect**: Prevents schedule paralysis; decision can be revisited later with more data.


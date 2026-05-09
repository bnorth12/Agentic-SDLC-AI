# Governance Metrics & Performance Indicators

**Document ID**: METRICS-GOV-001  
**Date**: May 12, 2026  
**Scope**: How to measure governance framework health, effectiveness, and compliance  
**Measurement Cadence**: Weekly (gates), Monthly (aggregated), Quarterly (strategic)

---

## Overview

Governance metrics track:
1. **Gate Performance** (schedule adherence, pass/fail rates)
2. **Risk Management** (residual risk trends, escalation frequency)
3. **Quality Indicators** (code quality, test coverage, defect trends)
4. **Agent Effectiveness** (decision velocity, authority compliance)
5. **Program Health** (schedule, budget, scope alignment)

---

## Tier 1: Gate Performance Metrics

### **Gate Cycle Time**

| Metric | Definition | Target | Measured By |
|--------|-----------|--------|-----------|
| **Gate Schedule Adherence** | Planned gate date ± Actual gate date | Within ±5 days | PM |
| **Requirements Gate Duration** | Start of Phase 1 → RRB gate date | 4-6 weeks | PM |
| **Architecture Gate Duration** | Start of Phase 2 → DRB gate date | 3-4 weeks | PM |
| **Implementation Gate Duration** | Start of Phase 3 → CIB gate date | 4-6 weeks | PM |
| **Deployment Gate Duration** | Start of Phase 5 → DRR gate date | 2-3 weeks | PM |

**Success Criteria**:
- Requirements gate within schedule ±5 days
- All subsequent gates within ±3 days (more predictable after first gate)

**Failure Triggers**:
- Gate >2 weeks late → PM escalates to Steering Committee
- Gate >1 month late → Program schedule slip > X weeks

### **Gate Pass Rates**

| Metric | Definition | Target | Measured By |
|--------|-----------|--------|-----------|
| **PASS Rate** | # Gates PASS on first submission / Total gates | ≥75% | PM + Gatekeeper |
| **CONDITIONAL Rate** | # Gates CONDITIONAL / Total gates | ≤20% | PM + Gatekeeper |
| **FAIL Rate** | # Gates FAIL / Total gates | ≤5% | PM + Gatekeeper |
| **Re-Gate Cycles Needed** | Total gate submissions / Unique gates | <1.5 avg | PM + Gatekeeper |

**Success Criteria**:
- ≥75% of gates PASS on first submission
- ≤20% CONDITIONAL passes (accepted risks)
- ≤5% outright FAILs requiring rework

**Failure Triggers**:
- FAIL rate >10% → Governance process broken (root cause analysis needed)
- Re-gate cycles >2 average → Gate criteria unclear or quality baseline too high

### **Gate Preparation Quality**

| Metric | Definition | Target | Measured By |
|--------|-----------|--------|-----------|
| **Pre-Gate Readiness** | Gatekeeper says "READY" for gate meeting | ≥90% of time | Gatekeeper |
| **Pre-Gate Review Time** | Days from submission → gatekeeper "READY" | ≤3 days | Gatekeeper |
| **Gate Meeting Efficiency** | Scheduled time ± Actual meeting time | Within ±10 min | Gate organizer |

---

## Tier 2: Risk Management Metrics

### **Threat & Hazard Coverage**

| Metric | Definition | Target | Measured By |
|--------|-----------|--------|-----------|
| **L1 Threat Coverage** | % of threat vectors identified in Requirements phase | ≥95% | CSO |
| **L2 Threat Coverage** | % of L1 threats decomposed at architecture level | ≥95% | CSO |
| **L3 Threat Coverage** | % of L2 threats decomposed at component level | ≥95% | CSO |
| **L1 Hazard Coverage** | % of failure modes identified in Requirements phase | ≥95% | CSafO |
| **L2 Hazard Coverage** | % of L1 hazards decomposed at architecture level | ≥95% | CSafO |
| **L3 Hazard Coverage** | % of L2 hazards decomposed at component level | ≥95% | CSafO |

**Success Criteria**:
- At each level, ≥95% of threats/hazards identified & decomposed
- < 5% of identified threats/hazards "unknown" or "under investigation"

**Failure Triggers**:
- Coverage <80% at any level → emergency analysis sprint

### **Risk Acceptance Rates**

| Metric | Definition | Target | Measured By |
|--------|-----------|--------|-----------|
| **Mitigated Threats** | % of threats exceeding threshold that are mitigated | ≥90% | CSO + PM |
| **Unmitigated Threats (Accepted)** | % of threats exceeding threshold that are residual | ≤10% | CSO + PM |
| **Mitigated Hazards** | % of hazards exceeding threshold that are mitigated | ≥90% | CSafO + PM |
| **Unmitigated Hazards (Accepted)** | % of hazards exceeding threshold that are residual | ≤10% | CSafO + PM |
| **Residual Risk Within Tolerance** | Residual risk score ≤ program acceptable risk threshold | 100% | CSO + CSafO + CE |

**Success Criteria**:
- ≥90% of identified risks mitigated (not just accepted)
- All accepted residual risks formally documented & signed off

**Failure Triggers**:
- Residual risk >10% unmitigated → CSO/CSafO escalate to CE
- Residual risk exceeds program threshold → deployment hold

### **Escalation Frequency**

| Metric | Definition | Target | Measured By |
|--------|-----------|--------|-----------|
| **Escalation Count** | # of escalations / month | <3 per month | PM |
| **Escalation Resolution Time** | Triggered → Decision made | <3 days avg | PM |
| **Escalation Categories** | Breakdown: resource / schedule / risk / quality / compliance | <20% any single category | Escalation log |
| **Recurring Escalations** | Same issue escalated twice | 0 (if occurs, analyze root cause) | PM |

**Success Criteria**:
- <3 escalations per month (normal operation)
- All escalations resolved within 3 days
- <5% of escalations are recurring (addresses root cause)

**Failure Triggers**:
- >5 escalations per month → governance framework needs adjustment
- >1 escalation unresolved >5 days → escalation authority review

---

## Tier 3: Quality Indicators

### **Code Quality Metrics**

| Metric | Definition | Target | Measured By |
|--------|-----------|--------|-----------|
| **MISRA Compliance** | % of code passing MISRA scan | ≥95% | CRB |
| **Cyclomatic Complexity** | % of functions with CC ≤10 | ≥95% | CRB |
| **Test Coverage** | % of code lines executed by tests | ≥95% | QA |
| **Security Vulnerability Density** | # critical/high vulnerabilities per 1000 LOC | <0.1 | CSO + CRB |

**Success Criteria**:
- MISRA ≥95%, CC ≤10 for ≥95% of functions
- Test coverage ≥95%
- <1 critical/high vulnerability per 10KLOC

**Failure Triggers**:
- MISRA <90% → gate FAIL
- CC >10 for >10% of functions → rework required
- Test coverage <90% → gate FAIL

### **Defect Trends**

| Metric | Definition | Target | Measured By |
|---------|-----------|--------|-----------|
| **Critical Defect Escape Rate** | # critical defects found post-gate / pre-gate | <5% | QA |
| **High-Severity Defects** | # open high-severity bugs at each gate | 0-2 max | QA |
| **Defect Resolution Time** | Reported → Fixed | <7 days avg | QA |
| **Defect Recurrence Rate** | Same bug fixed twice | 0% | QA |

**Success Criteria**:
- 0 critical defects in production
- <2 high-severity defects open at deployment
- All defects resolved within 7 days

**Failure Triggers**:
- >5% critical escapes → root cause analysis (testing inadequate)
- >3 high-severity defects at deployment → gate FAIL

---

## Tier 4: Agent Effectiveness

### **Decision Velocity**

| Metric | Definition | Target | Measured By |
|---|---|---|---|
| **Async Decision Velocity** | Days from issue identified → decision made (async) | <2 days | Decision log |
| **Escalated Decision Velocity** | Days from escalation triggered → CE decision made | <3 days | Escalation log |
| **Authority Compliance** | Decisions made by correct authority per RACI | 100% | CCO audit |

**Success Criteria**:
- <2 days for routine async decisions
- <3 days for escalated decisions
- 100% of decisions follow RACI authority

**Failure Triggers**:
- >3 decisions pending >5 days → authority not engaged
- >5% decisions made by wrong authority → RACI confusion

### **Agent Participation**

| Metric | Definition | Target | Measured By |
|---|---|---|---|
| **On-Time Contributions** | Agent posts required inputs by deadline | ≥95% of activities | RACI tracker |
| **Gate Review Attendance** | Agent attends required gate meetings | 100% | Gate sign-in |
| **Authority Delegation** | Agent delegates authority appropriately (no single point of failure) | 100% | CCO audit |

**Success Criteria**:
- All agents >95% on-time with deliverables
- 100% attendance at required gates
- No single agent is bottleneck

**Failure Triggers**:
- Agent <80% on-time → investigate capacity/training issue
- <90% gate attendance → escalate to CE (may replace agent)

---

## Tier 5: Program Health

### **Schedule Metrics**

| Metric | Definition | Target | Measured By |
|---|---|---|---|
| **Schedule Performance Index (SPI)** | Work completed on time / Work planned | ≥0.95 | PM |
| **Phase Variance** | Planned phase duration vs Actual | Within ±10% | PM |
| **Critical Path Status** | Days to delivery vs Baseline plan | On schedule | PM |
| **Schedule Buffer Consumption** | % of schedule contingency used | <50% consumed | PM |

**Success Criteria**:
- SPI ≥0.95 (schedule healthy)
- Phase variance within ±10%
- On-track to delivery date (no slip)
- Schedule buffer <50% consumed

**Failure Triggers**:
- SPI <0.90 → Steering Committee escalation (behind schedule)
- Phase variance >20% → Root cause analysis required

### **Budget Metrics**

| Metric | Definition | Target | Measured By |
|---|---|---|---|
| **Cost Performance Index (CPI)** | Budget spent / Budget planned | ≥0.95 | Finance |
| **Budget Variance** | Planned budget vs Actual spend | Within ±10% | Finance |
| **Contingency Reserve** | % of budget contingency remaining | >30% | Finance |

**Success Criteria**:
- CPI ≥0.95 (budget efficient)
- Budget variance within ±10%
- >30% contingency remaining

**Failure Triggers**:
- CPI <0.90 → over budget (Steering Committee review)
- Budget contingency <20% → risk increase

### **Scope Alignment**

| Metric | Definition | Target | Measured By |
|---|---|---|---|
| **Requirement Stability** | % of L1 requirements changed during phase | <5% | RM |
| **Scope Creep** | # of unplanned features added | 0-1 per phase max | PM |
| **Customer Satisfaction** | Stakeholder approval of deliverables | ≥80% agree | Stakeholder survey |

**Success Criteria**:
- <5% requirement volatility (stable requirements)
- ≤1 scope creep item per phase
- ≥80% stakeholder satisfaction

**Failure Triggers**:
- >10% requirement changes → Requirements process broken
- >3 scope creep items per phase → scope not controlled

---

## Tier 6: Compliance Metrics

### **Governance Compliance**

| Metric | Definition | Target | Measured By |
|---|---|---|---|
| **Gate Criteria Compliance** | % of gate pass criteria met before approval | 100% | Gatekeeper |
| **RACI Compliance** | % of activities executed per RACI matrix | ≥95% | CCO audit |
| **Evidence Collection** | % of compliance artifacts collected per plan | 100% by deployment | CCO |
| **Traceability Integrity** | RTM completeness (Requirements ↔ Design ↔ Code ↔ Test) | ≥99% | RM + DTM |

**Success Criteria**:
- 100% of gate criteria verified before gate approval
- ≥95% of RACI activities executed as planned
- 100% of evidence collected by deployment
- ≥99% traceability links verified

**Failure Triggers**:
- Gate approval without full criteria met → governance override audit
- RACI compliance <90% → training/authority review
- Evidence <90% collected by testing phase → accelerate collection

---

## Dashboard & Reporting

### **Weekly Report** (Friday EOD)

```
GOVERNANCE HEALTH - Week of [Date]

Gate Performance:
- Current phase: [Phase name]
- Days to next gate: [X days]
- Pre-gate readiness: READY / NOT READY
- Last gate result: PASS / CONDITIONAL / FAIL

Risk Status:
- Active escalations: [# pending, # resolved this week]
- High-priority risks: [List]
- Residual risk trend: ↑ / → / ↓

Quality:
- MISRA compliance: [%]
- Test coverage: [%]
- Open defects: [# critical, # high, # medium]

Program:
- Schedule variance: [+/- X days]
- Budget variance: [+/- X%]
- Scope changes: [# this week]

Metrics Alerts:
- Metrics within targets: ✓ / ✗
- Concerning trend: [If any metric flagged]
```

### **Monthly Report** (End of month)

```
GOVERNANCE MONTHLY REVIEW - [Month]

1. Gate Performance Summary
   - Gates completed: [# PASS / # CONDITIONAL / # FAIL]
   - Schedule adherence: [+/- days avg]
   - Re-gate cycles: [# additional cycles needed]

2. Risk Summary
   - Threats identified: [L1: X, L2: Y, L3: Z]
   - Hazards identified: [L1: X, L2: Y, L3: Z]
   - Escalations: [# triggered, # resolved]
   - Residual risk trend: [Historical trend line]

3. Quality Summary
   - Code quality: MISRA [%], CC [%], coverage [%]
   - Defect trends: [# critical, # high, # medium escapes]
   - Security findings: [# critical, # high]
   - Safety findings: [# critical, # high]

4. Compliance Summary
   - Evidence collected: [% of plan]
   - Traceability: [% complete]
   - Standards compliance: [List standards, status]

5. Agent Performance
   - On-time delivery rate: [%]
   - Gate participation: [% attendance]
   - Decision velocity: [avg days to decision]

6. Program Health
   - Schedule Performance Index: [SPI value]
   - Cost Performance Index: [CPI value]
   - Scope changes: [# this month]

7. Recommendations
   - Continue current approach if: [Conditions]
   - Adjust governance if: [Issues to address]
```

### **Quarterly Strategic Review** (End of quarter)

```
GOVERNANCE STRATEGIC REVIEW - Q[X] [Year]

1. Governance Framework Effectiveness
   - Gate pass rates trend: [Historical comparison]
   - Escalation frequency trend: [Historical comparison]
   - Risk acceptance trend: [Residual risk trajectory]

2. Quality Outcomes
   - Code quality trend: [3-month trend line]
   - Defect escape trend: [3-month trend line]
   - Security/Safety posture: [Improvements vs risks]

3. Program Delivery
   - Schedule: On track / Behind / Ahead
   - Budget: Within plan / Over / Under
   - Scope: Stable / Creeping / Constrained

4. Agent Capabilities
   - Governance maturity assessment: [Level 1-5]
   - Training needs: [Agents needing development]
   - Succession plan: [Key person risks]

5. Strategic Adjustments for Next Quarter
   - Governance improvements: [Recommended changes]
   - Process improvements: [Efficiency opportunities]
   - Risk mitigations: [Emerging risks]
```

---

## Metrics Governance

### **Who Owns Metrics**

| Metric Category | Owner | Updates | Cadence |
|---|---|---|---|
| **Gate Performance** | PM + Gatekeeper | Post-gate | Real-time |
| **Risk Metrics** | CSO + CSafO + PM | Post-decision | Weekly |
| **Quality Metrics** | CRB + QA | Post-gate/phase | Weekly |
| **Agent Performance** | Each agent (self-report) | Weekly standup | Weekly |
| **Program Health** | PM + Finance | Post-review | Weekly |
| **Compliance** | CCO | Audit cycle | Monthly |

### **Escalation on Metrics**

If any metric fails target:
1. **Week 1**: Post in metrics dashboard with "yellow flag"
2. **Week 2**: If still failing: PM + agent discuss root cause
3. **Week 3**: If unresolved: Escalate to CE
4. **Week 4+**: CE + Steering Committee review for governance change

**Exception**: Critical metrics (gate pass rate, risk acceptance, defect escape rate) escalate immediately to CE if threshold breached.


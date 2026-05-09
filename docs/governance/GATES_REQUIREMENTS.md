# Requirements Phase Gate (RRB - Requirements Review Board)

**Document ID**: GATES-REQ-001  
**Date**: May 12, 2026  
**Gatekeeper**: Requirements Manager (chairs), CSO, CSafO, CCO (observers)  
**Phase Transition**: Requirements → Architecture  
**Standards Basis**: DO-178C §3, DO-356A §3, ARP 4752A §3, MIL-STD-882G §3, NIST 800-30

---

## Executive Summary

The Requirements Phase Gate determines if a program can proceed from **Requirements Definition** into **Architecture & Design**. This gate validates that:

1. **All stakeholder needs are captured** (≥80% completeness)
2. **Security threats are identified upfront** (L1-level threat analysis)
3. **Safety hazards are identified upfront** (L1-level hazard analysis)
4. **Risks are scored and thresholded** (which threats/hazards need mitigation?)
5. **Security/safety requirements are allocated** (from threats/hazards to L1 requirements)
6. **All requirements are traceable and testable** (RTM complete)
7. **Compliance activities are planned** (evidence collection strategy defined)

**Gate Decision**: Does the program have a complete, accurate, testable foundation to proceed to Architecture?

---

## Phase Entry Criteria (To Begin Requirements Phase)

| Criterion | Owner | Verification |
|-----------|-------|--------------|
| Project charter approved | PM | Signed charter in archive |
| Stakeholder needs elicitation started | RM | Meeting minutes, interview notes |
| Compliance standards identified | CCO | List of applicable standards |
| Program risk tolerance defined | PM + CE | Risk acceptance memo (template) |
| Security threat categories identified | CSO | Initial threat framework |
| Safety hazard categories identified | CSafO | Initial hazard framework |

---

## Gate Pass/Fail Criteria

### ✅ PASS Criteria (ALL Must Be Met)

#### A. Requirements Completeness (≥80% by count, organized by L1→L2→L3)

| Sub-Criterion | Target | Verification | Owner |
|---|---|---|---|
| **A1: L1 Functional Requirements** | ≥80% identified | Requirements spreadsheet count | RM |
| **A2: L1 Non-Functional Requirements** | ≥80% identified | Performance, safety, security, compliance sections | RM |
| **A3: Acceptance Criteria** | 100% defined | Each requirement has test acceptance criteria | RM |
| **A4: Requirements Traceability Matrix (RTM)** | 100% initialized | L1↔L2 mapping defined (L3 TBD) | RM |
| **A5: Requirement Attributes** | 100% populated | Priority, source (stakeholder/threat/hazard), verification method | RM |

**Completeness Calculation**: 
```
% Complete = (# of Requirements with Acceptance Criteria / Total Requirements Needed) × 100
Pass if ≥80%
```

**Exemption**: RM can request waiver if requirements are phased (e.g., 60% Phase 1, 80% Phase 2). Requires PM + CE approval.

---

#### B. Security Threat Analysis (L1-Level, Loss-Based)

| Sub-Criterion | Target | Verification | Owner |
|---|---|---|---|
| **B1: Threat Definition** | All threat categories identified | Threat list per ARP 4761/USAF framework (data, access, interface, crypto, supply chain, deployment) | CSO |
| **B2: Threat Decomposition (L1)** | System-level threats defined | Each threat characterized: attack vector, target asset, consequence category | CSO |
| **B3: Risk Scoring (L1)** | Consequence × Probability scored | Each threat scored: Consequence (Catastrophic/Critical/Major/Minor), Probability (High/Med/Low) | CSO |
| **B4: Risk Thresholding** | Threshold comparison completed | CSO identifies which threats EXCEED program acceptable risk level | CSO |
| **B5: Threat Documentation** | Evidence artifacts created | Threat model (spreadsheet or diagram), risk scores, thresholding decisions | CSO |
| **B6: Mapped to Security Requirements** | Requirements allocated | For threats exceeding threshold → security requirements created (per SEC-001 through SEC-011 activities) | CSO + RM |

**Pass Condition**: At least ONE formal threat analysis artifact exists (e.g., NIST threat model, USAF security categorization) with scored risks and thresholding decisions documented.

**Escalation Trigger**: If CSO reports >5 unmitigated high-risk threats → escalate to Chief Engineer (design must address these).

---

#### C. Safety Hazard Analysis (L1-Level, Loss-Based)

| Sub-Criterion | Target | Verification | Owner |
|---|---|---|---|
| **C1: Hazard Definition** | All hazard categories identified | Functional Hazard Analysis (FHA) per ARP 4752A (loss of function, degraded function, erratic function) | CSafO |
| **C2: Hazard Decomposition (L1)** | System-level hazards defined | Each hazard characterized: failure mode, cause, consequence category | CSafO |
| **C3: Risk Scoring (L1)** | Severity × Probability scored | Each hazard scored: Severity (Catastrophic/Critical/Major/Minor), Probability (Frequent/Remote/Improbable) | CSafO |
| **C4: Risk Thresholding** | Threshold comparison completed | CSafO identifies which hazards EXCEED program acceptable risk level | CSafO |
| **C5: Hazard Documentation** | Evidence artifacts created | FHA spreadsheet/diagram, risk scores, thresholding decisions, severity justification | CSafO |
| **C6: Mapped to Safety Requirements** | Requirements allocated | For hazards exceeding threshold → safety requirements created (per SAF-001 through SAF-011 activities) | CSafO + RM |

**Pass Condition**: Functional Hazard Analysis completed per ARP 4752A with severity classification, probability assessment, and thresholding decisions documented.

**Escalation Trigger**: If CSafO reports catastrophic or critical hazards without mitigations → escalate to Chief Engineer (architecture must include fault tolerance).

---

#### D. Requirements-to-Threat/Hazard Traceability

| Sub-Criterion | Target | Verification | Owner |
|---|---|---|---|
| **D1: Threat-Requirement Mapping** | 100% of identified threats mapped | Each threat ↔ security requirement (if exceeds threshold) OR documented as residual risk | CSO + RM |
| **D2: Hazard-Requirement Mapping** | 100% of identified hazards mapped | Each hazard ↔ safety requirement (if exceeds threshold) OR documented as residual risk | CSafO + RM |
| **D3: Bidirectional Traceability** | 100% initialized | RTM shows L1 Requirements ← Threats/Hazards ← Stakeholder Needs | RM |

---

#### E. Compliance Planning & Evidence Strategy

| Sub-Criterion | Target | Verification | Owner |
|---|---|---|---|
| **E1: Applicable Standards Listed** | Complete inventory | Standards document identifies all applicable DO-178C, DO-256A/355A, ARP 4761, NIST, etc. | CCO |
| **E2: Compliance Requirements Mapped** | Gap analysis completed | CCO maps "what standards require" → "what we must do" in each phase | CCO |
| **E3: Evidence Package Planned** | Collection strategy documented | CCO defines: what artifacts demonstrate compliance (threat models, hazard models, test results, residual risk acceptance) | CCO |
| **E4: Compliance Checklist Created** | Gate criteria documented | CCO creates checklist for Requirements/Architecture/Implementation/Test/Deployment gates (per compliance requirement) | CCO |

**Pass Condition**: Compliance gap analysis & evidence collection strategy documented (per COMP-001 through COMP-005 activities).

---

#### F. Requirements Quality & Testability

| Sub-Criterion | Target | Verification | Owner |
|---|---|---|---|
| **F1: SMART Requirements** | ≥95% of requirements | Specific, Measurable, Achievable, Relevant, Time-bound | RM |
| **F2: Requirement Conflicts** | 0 unresolved conflicts | All conflicting requirements identified & resolved | RM |
| **F3: Requirement Ambiguity** | <5% ambiguous language | Each requirement clear enough for architect to decompose | RM |
| **F4: Verification Methods Assigned** | 100% of requirements | Each requirement has at least ONE verification method (test, inspection, analysis, demonstration) | RM |

---

### ❌ FAIL Criteria (Any One Causes Gate Failure)

| Failure Condition | Impact | Recovery Action |
|---|---|---|
| **Requirements Completeness < 80%** | Incomplete foundation | Schedule 2-week requirements completion sprint; re-gate |
| **Threat Analysis not performed** | Security risks unidentified | CSO performs emergency L1 threat analysis (1 week); re-gate |
| **Hazard Analysis not performed** | Safety risks unidentified | CSafO performs emergency FHA (1 week); re-gate |
| **Identified threats/hazards > Program Threshold, no mitigation strategy** | Risks not acknowledged | CSO/CSafO create mitigation strategy; CE approves or escalates; re-gate |
| **Threat-Requirement Traceability gaps** | Security requirements missing | RM + CSO close gaps; re-gate |
| **Hazard-Requirement Traceability gaps** | Safety requirements missing | RM + CSafO close gaps; re-gate |
| **>5 Critical/Catastrophic Threats without mitigations** | Unacceptable security risk | CSO escalates to CE; schedule urgent architecture planning; re-gate after architecture strategy defined |
| **>5 Critical/Catastrophic Hazards without mitigations** | Unacceptable safety risk | CSafO escalates to CE; schedule urgent architecture planning; re-gate after architecture strategy defined |
| **RTM incomplete** | Traceability broken | RM completes RTM; re-gate |
| **Compliance strategy undefined** | No certification path | CCO creates compliance & evidence strategy; re-gate |

---

## Gate Approval Process

### Step 1: Requirements Manager Pre-Assessment (Day 1-2)
- Verify all requirements documented
- Verify RTM initialized
- Check completeness metric (≥80%?)
- Status: **READY** or **NOT READY FOR GATE**

### Step 2: Chief Security Officer Review (Day 2-3)
- Review L1 threat analysis
- Verify risk scores documented
- Confirm threats exceeding threshold are mapped to security requirements
- Verify residual threats (below threshold) are documented
- **Recommendation**: READY, CONDITIONAL, NOT READY

### Step 3: Chief Safety Officer Review (Day 2-3)
- Review L1 hazard analysis
- Verify severity/probability scores documented
- Confirm hazards exceeding threshold are mapped to safety requirements
- Verify residual hazards (below threshold) are documented
- **Recommendation**: READY, CONDITIONAL, NOT READY

### Step 4: Chief Compliance Officer Review (Day 3)
- Review applicable standards list
- Verify compliance gap analysis completed
- Confirm evidence collection strategy defined
- **Recommendation**: READY, CONDITIONAL, NOT READY

### Step 5: Requirements Review Board (RRB) Gate Meeting (Day 4)
**Attendees**: RM (chair), CSO, CSafO, CCO, Program Manager, Chief Engineer (observer)

**Agenda** (2 hours):
1. RM presents requirements completeness metrics (10 min)
2. CSO presents threat analysis summary (20 min)
3. CSafO presents hazard analysis summary (20 min)
4. CCO presents compliance strategy (10 min)
5. Gate vote: PASS, CONDITIONAL, or FAIL (20 min)
6. If FAIL or CONDITIONAL: Define recovery actions & re-gate schedule (20 min)

**Gate Vote Authority**: 
- **PASS**: RM approval + CSO + CSafO concurrence + CCO confirmation
- **CONDITIONAL**: Pass with agreed-upon deviations (risk acceptance memo required)
- **FAIL**: Requires recovery actions & re-gating

**Risk Acceptance Memo** (if CONDITIONAL):
- Lists specific deviations (e.g., "Threat X scored Catastrophic but no mitigation strategy yet - planned in Architecture phase")
- Signed by: CE (approval), PM (schedule impact acknowledged)
- Attached to gate decision record

---

## Gate Outputs (Success Criteria Met)

Upon PASS decision, document the following in Gate Archive:

1. **Gate Decision Record**
   - Date, attendees, vote result
   - Pass/Conditional/Fail decision
   - If CONDITIONAL: risk acceptance memo signed by CE + PM
   - If FAIL: recovery actions & re-gate scheduled date

2. **Requirements Completeness Report**
   - Final count: X Requirements total
   - Completeness metric: Y%
   - L1/L2/L3 breakdown
   - Verification method assignments

3. **Threat Analysis Summary**
   - Threat count: X identified, Y exceed threshold
   - High-risk threats listed (exceeding threshold)
   - Mapping to security requirements (per RACI SEC-011)
   - Residual threats documented (below threshold)

4. **Hazard Analysis Summary**
   - Hazard count: X identified, Y exceed threshold
   - High-risk hazards listed (exceeding threshold)
   - Mapping to safety requirements (per RACI SAF-011)
   - Residual hazards documented (below threshold)

5. **Requirements Traceability Matrix (RTM)**
   - Stakeholder Needs ← L1 Requirements
   - L1 Requirements ← Threats/Hazards (where applicable)
   - Each L1 Requirement → Acceptance Criteria
   - Each L1 Requirement → Verification Method

6. **Compliance Evidence Plan**
   - Applicable standards checklist
   - Compliance requirements → what artifacts needed
   - Evidence collection schedule per phase
   - Data package assembly plan

---

## Escalation Triggers

| Trigger | Action | Owner |
|---------|--------|-------|
| **Threat Analysis not performed** | CSO notifies PM; emergency 1-week analysis sprint | CSO |
| **>5 High-Risk Threats Unmitigated** | CSO escalates to CE; may delay gate or require risk acceptance | CSO + CE |
| **Hazard Analysis not performed** | CSafO notifies PM; emergency 1-week analysis sprint | CSafO |
| **>5 High-Risk Hazards Unmitigated** | CSafO escalates to CE; may delay gate or require risk acceptance | CSafO + CE |
| **Requirements Completeness < 75%** | RM notifies PM; may require 2-week completion sprint | RM + PM |
| **Unresolvable requirement conflicts** | RM escalates to PM + CE; trade-off decision required | RM + PM + CE |
| **Compliance strategy undefined** | CCO escalates to PM; may delay gate | CCO + PM |
| **Program risk tolerance undefined** | PM + CE define in writing before gate; may delay gate | PM + CE |

---

## Success Metrics (Post-Gate Tracking)

| Metric | Target | Tracked By |
|--------|--------|-----------|
| **Gate Schedule Adherence** | Gate within planned window ±1 week | PM |
| **Threat Analysis Coverage** | ≥95% of threat vectors covered by identified threats | CSO |
| **Hazard Analysis Coverage** | ≥95% of failure modes covered by identified hazards | CSafO |
| **Mitigation Planning** | ≥90% of high-risk threats/hazards have mitigation strategies by end of Architecture phase | CSO + CSafO |
| **RTM Consistency** | ≥99% of L1→L2 traceability maintained through Architecture | RM |
| **Requirement Volatility** | <5% of requirements changed during Architecture phase (indicates requirements stability) | RM |
| **Compliance Adherence** | 100% of planned evidence artifacts collected by Deployment | CCO |

---

## RACI Reference (Activities in This Gate)

This gate executes the following RACI activities:

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|-------------|------------|-----------|----------|
| SEC-001: Threat Definition (L1) | CSO | CSO | RM, Arch | PM |
| SEC-002: Threat Decomposition (L1) | CSO | CSO | Arch | PM |
| SEC-008: Risk Threshold Comparison | CSO | CSO | PM | RM |
| SAF-001: Functional Hazard Analysis (L1) | CSafO | CSafO | RM, Arch | PM |
| SAF-002: Hazard Decomposition (L1) | CSafO | CSafO | Arch | PM |
| SAF-009: Risk Threshold Comparison | CSafO | CSafO | PM | RM |
| RM-009: Requirement Completeness Review | RM | RM | CSO, CSafO | PM |
| RM-010: Requirements Traceability Matrix | RM | RM | CSO, CSafO | PM |
| COMP-001: Applicable Standards ID | CCO | CCO | CSO, CSafO | RM |
| COMP-002: Compliance Requirements Mapping | CCO | CCO | RM | RM |

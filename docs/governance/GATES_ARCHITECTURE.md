# Architecture Phase Gate (DRB - Design Review Board)

**Document ID**: GATES-ARCH-001  
**Date**: May 12, 2026  
**Gatekeeper**: System Architect (chairs), Chief Engineer (approval authority)  
**Phase Transition**: Architecture → Implementation  
**Standards Basis**: DO-178C §4, DO-356A §4, ARP 4754A §3-4, USAF System Security Engineering, NASA-STD-7009A

---

## Executive Summary

The Architecture Phase Gate determines if a program can proceed from **Architecture & Design** into **Implementation**. This gate validates that:

1. **System is decomposed** (L1→L2→L3 hierarchy with clear interfaces)
2. **Design is feasible** (≥70% confidence in technical approach)
3. **Security architecture addresses L2-level threats** (threat-driven design)
4. **Safety architecture addresses L2-level hazards** (failure-driven design)
5. **Mitigation strategies are defined** (for risks exceeding program threshold)
6. **Residual risks are understood and accepted** (for risks below threshold)
7. **Compliance artifacts are traceable** (design decision records, threat→design mapping)

**Gate Decision**: Is the design sound, complete, and ready for detailed implementation?

---

## Phase Entry Criteria

| Criterion | Owner | Verification |
|-----------|-------|--------------|
| Requirements gate PASSED | RM | RRB gate decision record |
| L1 threat analysis baseline | CSO | Threat model with risk scores & thresholding |
| L1 hazard analysis baseline | CSafO | FHA with severity scores & thresholding |
| Architecture framework selected | Arch | High-level system decomposition sketch |
| Technology stack identified | Arch | Preliminary platform/language/tools selection |
| Design patterns inventory | Cyber Arch + Arch | Initial secure & fault-tolerant patterns |

---

## Gate Pass/Fail Criteria

### ✅ PASS Criteria (ALL Must Be Met)

#### A. System Decomposition (L1→L2→L3 with Clear Interfaces)

| Sub-Criterion | Target | Verification | Owner |
|---|---|---|---|
| **A1: Functional Decomposition** | L1→L2→L3 hierarchy | System block diagram with major functions decomposed | Arch |
| **A2: Interface Specifications** | 100% of interfaces defined | L2↔L2 & L2→L3 interfaces documented: data flow, protocols, timing | Arch |
| **A3: Component Allocation** | Hardware/software/COTS identified | Each L2 component assigned to HW/SW/COTS | Arch |
| **A4: Complexity Assessment** | Cyclomatic Complexity per component identified | CC ≤10 for most components (waivers require CE approval) | CRB (code review) |
| **A5: Architecture Diagram** | Certified complete | UML component/deployment diagram or equivalent | Arch |

**Pass Condition**: Decomposition complete through at least L2, with L3 decomposition planned for critical/safety-critical components.

---

#### B. Design Feasibility Assessment (≥70% Confidence)

| Sub-Criterion | Target | Verification | Owner |
|---|---|---|---|
| **B1: Technical Approach** | Proven or low-risk | Technology choices justified; prior use or risk mitigation documented | Arch |
| **B2: Resource Feasibility** | Staffing & schedule realistic | Effort estimates per component; schedule critical path identified | PM |
| **B3: COTS/Vendor Availability** | Components available | Lead times confirmed; alternative sources identified | SQM |
| **B4: Technology Maturity** | Maturity Level 1 minimum | No experimental or beta technologies for critical/safety-critical paths | Arch + CE |
| **B5: Feasibility Score** | ≥70% by CE assessment | CE scores components; any <70% flagged as risk | CE |

**Feasibility Calculation**:
```
Feasibility = (Sum of Individual Component Confidence × Weight) / 100
Must be ≥70% for gate PASS
```

**Waivers**: Components with 60-70% feasibility require CE approval + risk mitigation plan.

---

#### C. Security Architecture (L2-Level Threats, Loss-Based)

| Sub-Criterion | Target | Verification | Owner |
|---|---|---|---|
| **C1: Threat Decomposition (L2)** | L1 threats decomposed | Each L1 threat → L2 attack vectors identified | CSO |
| **C2: Risk Re-Scoring (L2)** | Scores updated | Threats re-scored at L2; may differ from L1 if mitigations planned | CSO |
| **C3: Risk Thresholding (L2)** | Threshold applied | CSO identifies which L2 threats exceed threshold → require mitigations | CSO |
| **C4: Threat-Driven Security Architecture** | Design addresses high-risk threats | For each high-risk L2 threat: design shows mitigation (encryption, access control, etc.) | Cyber Arch + CSO |
| **C5: Secure Design Patterns** | Patterns selected & justified | Authentication, authorization, cryptography, defense-in-depth patterns documented | Cyber Arch |
| **C6: Security Requirements → Design Mapping** | 100% traced | Each security requirement → design component(s) that implements it | CSO + Arch |
| **C7: Residual Threats Documented** | L2 residual threats listed | Threats below threshold documented (will be addressed in operations or accepted) | CSO |

**Pass Condition**: L2 threat decomposition complete, high-risk threats addressed in design, residual threats documented.

**Escalation**: If >5 high-risk L2 threats unaddressed in design → CSO escalates to CE (architecture rework required).

---

#### D. Safety Architecture (L2-Level Hazards, Loss-Based)

| Sub-Criterion | Target | Verification | Owner |
|---|---|---|---|
| **D1: Hazard Decomposition (L2)** | L1 hazards decomposed | Each L1 hazard → L2 failure modes identified | CSafO |
| **D2: Risk Re-Scoring (L2)** | Scores updated | Hazards re-scored at L2; may differ from L1 if mitigations planned | CSafO |
| **D3: Risk Thresholding (L2)** | Threshold applied | CSafO identifies which L2 hazards exceed threshold → require mitigations | CSafO |
| **D4: Failure-Driven Safety Architecture** | Design addresses high-risk failures | For each high-risk L2 hazard: design shows fault tolerance (redundancy, monitoring, fail-safe) | Arch + CSafO |
| **D5: Safety-Critical Components** | ID'd & justified | Components identified as safety-critical (≥2 reviewer rule, ≥95% test coverage) | CSafO + Arch |
| **D6: Fault Tolerance Strategy** | Defined per high-risk failure | Redundancy, monitoring, detection, recovery for each critical failure mode | Arch |
| **D7: Safety Requirements → Design Mapping** | 100% traced | Each safety requirement → design component(s) that implements it | CSafO + Arch |
| **D8: Residual Hazards Documented** | L2 residual hazards listed | Hazards below threshold documented (will be addressed in ops or accepted) | CSafO |

**Pass Condition**: L2 hazard decomposition complete, high-risk failures addressed in design, residual hazards documented.

**Escalation**: If >5 high-risk L2 hazards unaddressed in design → CSafO escalates to CE (architecture rework required).

---

#### E. Mitigation Strategy (For Risks Exceeding Threshold)

| Sub-Criterion | Target | Verification | Owner |
|---|---|---|---|
| **E1: CSO Mitigation Strategy (Threats)** | Documented strategy | CSO defines: which threats need mitigation, how design addresses, residual risks | CSO |
| **E2: CSafO Mitigation Strategy (Hazards)** | Documented strategy | CSafO defines: which hazards need mitigation, how design provides fault tolerance, residual risks | CSafO |
| **E3: Mitigation ↔ Design Mapping** | 100% mapped | Each mitigation strategy → design components | Cyber Arch + Arch |
| **E4: Residual Risk List** | Complete | Both CSO (residual threats) and CSafO (residual hazards) create list of risks that will not be fully mitigated | CSO + CSafO |

---

#### F. Architecture Decision Records (ADRs)

| Sub-Criterion | Target | Verification | Owner |
|---|---|---|---|
| **F1: Critical Decisions Documented** | ≥5 ADRs for architecture | Recorded: technology choice, threat mitigation approach, safety design strategy, trade-off rationale | Arch |
| **F2: ADR Standard** | IEEE 1028 or equivalent | Each ADR: Context, Decision, Consequences, Rationale, Status | Arch |
| **F3: Traceability** | ADR ↔ Requirements/Threats/Hazards | Each decision traceable to driving requirement, threat, or hazard | Arch + CSO + CSafO |

---

#### G. Design Quality & Completeness

| Sub-Criterion | Target | Verification | Owner |
|---|---|---|---|
| **G1: Interface Specifications** | 100% documented | All data, control, power interfaces specified; protocols defined | Arch |
| **G2: Design Review Checklist** | ≥95% items addressed | NASA/INCOSE design review checklist completed | Arch |
| **G3: Traceability (L1 Req → L2 Design)** | ≥95% | Requirements Traceability Matrix extended L1→L2 | RM + Arch |
| **G4: Design Diagrams** | Complete & certified | UML/SysML diagrams reviewed & approved by Arch | Arch |

---

### ❌ FAIL Criteria (Any One Causes Gate Failure)

| Failure Condition | Impact | Recovery Action |
|---|---|---|
| **System decomposition incomplete** | Architecture unclear | Architect completes L2 decomposition; re-gate in 1 week |
| **Feasibility < 70%** | High-risk approach | Address high-risk components or redesign; re-gate after risk mitigation |
| **L2 Threat decomposition not performed** | Security architecture unvalidated | CSO performs emergency L2 threat analysis (1 week); re-gate |
| **L2 Hazard decomposition not performed** | Safety architecture unvalidated | CSafO performs emergency L2 hazard analysis (1 week); re-gate |
| **>5 High-Risk L2 Threats unaddressed in design** | Unacceptable security risk | Cyber Arch redesigns threat mitigations; CE review; re-gate |
| **>5 High-Risk L2 Hazards unaddressed in design** | Unacceptable safety risk | Arch redesigns fault tolerance; CE review; re-gate |
| **Threat→Design mapping incomplete** | Security requirements unclear | CSO + Arch complete mapping; re-gate in 1 week |
| **Hazard→Design mapping incomplete** | Safety requirements unclear | CSafO + Arch complete mapping; re-gate in 1 week |
| **Residual risks not identified** | Compliance gap | CSO + CSafO document residual risks; re-gate |
| **Feasibility waivers not approved by CE** | Unauthorized risk | CE approval obtained or design reworked; re-gate |

---

## Gate Approval Process

### Step 1: System Architect Pre-Assessment (Day 1-3)
- Verify decomposition complete (L1→L2 minimum)
- Verify interfaces documented
- Verify feasibility scoring done
- Status: **READY** or **NOT READY FOR GATE**

### Step 2: Chief Security Officer Review (Day 3-4)
- Review L2 threat decomposition
- Verify threat-to-design mapping
- Confirm high-risk threats addressed in design
- Document residual threats
- **Recommendation**: READY, CONDITIONAL, NOT READY

### Step 3: Chief Safety Officer Review (Day 3-4)
- Review L2 hazard decomposition
- Verify hazard-to-design mapping
- Confirm high-risk hazards addressed in design
- Document residual hazards
- **Recommendation**: READY, CONDITIONAL, NOT READY

### Step 4: Design Review Board (DRB) Gate Meeting (Day 5)
**Attendees**: Arch (chair), CE (approval authority), CSO, CSafO, CCO (observers), Program Manager

**Agenda** (2.5 hours):
1. Arch presents system decomposition (20 min)
2. Arch presents feasibility assessment (15 min)
3. Cyber Arch presents security architecture & threat-driven design (20 min)
4. Arch presents safety architecture & fault-tolerance strategy (20 min)
5. CSO presents L2 threat analysis summary & residual risks (10 min)
6. CSafO presents L2 hazard analysis summary & residual risks (10 min)
7. CE feasibility rating & concerns (10 min)
8. Gate vote: PASS, CONDITIONAL, or FAIL (10 min)
9. If FAIL: Define recovery actions & re-gate schedule (5 min)

**Gate Vote Authority**: 
- **PASS**: Arch + CE approval (CSO + CSafO concurrence)
- **CONDITIONAL**: Pass with agreed risk acceptance (memo required, signed by CE)
- **FAIL**: Requires design rework and re-gating

---

## Gate Outputs (Success Criteria Met)

Upon PASS decision, document in Gate Archive:

1. **Gate Decision Record**
   - Date, attendees, DRB vote result
   - Pass/Conditional/Fail decision
   - If CONDITIONAL: risk acceptance memo (CE approved)

2. **Architecture Decomposition Report**
   - System block diagram (L1→L2→L3)
   - Component list with interface specifications
   - Hardware/Software/COTS allocation table

3. **Feasibility Assessment Report**
   - Feasibility scores per component
   - Technology justification
   - Resource plan & schedule

4. **Security Architecture Summary**
   - L2 threat decomposition
   - Threat-driven design: for each high-risk threat, show mitigation in design
   - Residual threat list (threats accepted below threshold)
   - L1→L2 threat decomposition mapping

5. **Safety Architecture Summary**
   - L2 hazard decomposition
   - Failure-driven design: for each high-risk hazard, show fault tolerance in design
   - Residual hazard list (hazards accepted below threshold)
   - L1→L2 hazard decomposition mapping

6. **Design Documentation**
   - Architecture Decision Records (≥5 ADRs)
   - UML/SysML diagrams
   - Interface specifications
   - Traceability (Requirements ↔ Design)

7. **Risk Acceptance Memo** (if CONDITIONAL)
   - Lists deviations
   - Signed by CE + PM

---

## Escalation Triggers

| Trigger | Action | Owner |
|---------|--------|-------|
| **Feasibility < 70%** | Flag as risk; CE review required | Arch + CE |
| **>5 High-Risk Security Threats Unaddressed** | CSO escalates to CE | CSO + CE |
| **>5 High-Risk Safety Hazards Unaddressed** | CSafO escalates to CE | CSafO + CE |
| **L2 Threat Decomposition Missing** | CSO notifies PM; 1-week emergency analysis | CSO |
| **L2 Hazard Decomposition Missing** | CSafO notifies PM; 1-week emergency analysis | CSafO |
| **Technology Unproven** | Architect justifies or selects alternative | Arch + CE |
| **Schedule Infeasible** | PM + CE trade-off decision | PM + CE |

---

## Success Metrics (Post-Gate Tracking)

| Metric | Target | Tracked By |
|--------|--------|-----------|
| **Architecture Stability** | <10% changes to decomposition during Implementation | Arch |
| **Design-to-Code Traceability** | ≥95% of design components implemented | CRB |
| **Threat-to-Code Mapping** | ≥95% of high-risk threats addressed in code | CSO |
| **Hazard-to-Code Mapping** | ≥95% of high-risk hazards addressed in code | CSafO |
| **Gate Schedule** | Gate within planned window ±1 week | PM |
| **Feasibility Achievement** | Implementation achieves ≥70% of feasibility plan | Arch + PM |

*Template to be populated during Sprint 0, Week 2.*

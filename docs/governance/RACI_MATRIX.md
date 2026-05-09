# RACI Matrix: Responsible, Accountable, Consulted, Informed

**Document ID**: RACI-001  
**Status**: APPROVED (Sprint 0-P1-002 complete)  
**Date**: May 10, 2026  
**Reviewed By**: Chief Engineer  
**Standards**: Based on INCOSE Handbook, NASA-STD-7009A, USAF SE Process  

---

## Executive Summary

This RACI matrix defines responsibility for key systems engineering activities across the SDLC. It establishes who is **Responsible** (does the work), **Accountable** (owns the outcome), **Consulted** (provides input), and **Informed** (gets the result).

**Principle**: Every activity has exactly ONE person Accountable. No ambiguity, no shared accountability.

**Abbreviations**:
- **R** = Responsible (does the work)
- **A** = Accountable (owns the outcome; final decision authority)
- **C** = Consulted (provides input/review before decision)
- **I** = Informed (notified of decision/outcome)

---

## SE Activity Domains

RACI is organized by SE domain (per INCOSE taxonomy):

1. **Requirements Management** (RM)
2. **Architecture & Design** (AD)
3. **Implementation & Integration** (II)
4. **Verification & Validation** (VV)
5. **Configuration & Change Management** (CCM)
6. **Risk Management** (Risk)
7. **Governance & Decision Management** (Gov)

---

## RACI Matrix (Per INCOSE/NASA/USAF Standards)

### Domain 1: Requirements Management

| Activity | Requirements Agent | Architecture Agent | Program Manager | Chief Engineer | Code Review Board | Deployment Manager |
|----------|------|------|------|------|------|------|
| **RM-001: Elicit Stakeholder Needs** | **R** | C | C | I | — | — |
| **RM-002: Capture L1 Requirements** | **R+A** | C | C | I | — | — |
| **RM-003: Define Acceptance Criteria** | **R+A** | C | C | I | — | — |
| **RM-004: Decompose L1→L2 Requirements** | **R+A** | C | C | I | — | — |
| **RM-005: Decompose L2→L3 Tasks** | R | **A** | C | I | — | — |
| **RM-006: Trace Requirements to Design** | R | **R+A** | C | I | — | — |
| **RM-007: Trace Requirements to Test** | R | C | C | I | **R+A** | — |
| **RM-008: Requirement Change Requests** | C | C | **A** | C | — | — |
| **RM-009: Requirement Completeness Review** | **R** | C | **A** | C | — | — |
| **RM-010: Requirements Traceability Matrix (RTM)** | **R** | C | C | I | — | — |

**Domain Owner**: Requirements Agent  
**Escalation Point**: Program Manager (if scope/schedule impact)

---

### Domain 2: Architecture & Design (Per NASA EDS, USAF APD)

| Activity | Requirements Agent | Architecture Agent | Program Manager | Chief Engineer | Code Review Board | Deployment Manager |
|----------|------|------|------|------|------|------|
| **AD-001: System Decomposition** | C | **R+A** | — | C | — | — |
| **AD-002: Architecture Trade Studies** | C | **R** | — | **A** | — | — |
| **AD-003: Component Allocation** | C | **R+A** | — | C | — | — |
| **AD-004: Interface Specifications** | C | **R+A** | — | C | — | — |
| **AD-005: Hardware/Software Split** | C | **R** | — | **A** | — | C |
| **AD-006: Feasibility Assessment** | C | **R** | — | **A** | C | — |
| **AD-007: Design Complexity Review** | C | **R** | — | **A** | C | — |
| **AD-008: Risk Identification (Design)** | — | **R** | — | **A** | C | — |
| **AD-009: Architecture Design Review (ADR)** | C | **R** | — | **A** | C | — |
| **AD-010: Performance & Scalability Assessment** | C | **R** | — | **A** | C | — |

**Domain Owner**: Architecture Agent  
**Escalation Point**: Chief Engineer (if feasibility < 70% or high-risk pattern)

---

### Domain 3: Implementation & Integration

| Activity | Requirements Agent | Architecture Agent | Program Manager | Chief Engineer | Code Review Board | Deployment Manager |
|----------|------|------|------|------|------|------|
| **II-001: Code Development** | — | C | — | — | **A** (reviews) | — |
| **II-002: Unit Test Development** | — | — | — | — | **R+A** | — |
| **II-003: Code Quality Checks** | — | — | — | — | **R+A** | — |
| **II-004: Security Scanning** | — | C | — | — | **R+A** | — |
| **II-005: Complexity Analysis** | — | — | — | — | **R+A** | — |
| **II-006: Peer Code Review** | — | — | — | — | **R+A** (2+ reviewers) | — |
| **II-007: Test Coverage Verification** | — | — | — | — | **R+A** | — |
| **II-008: Configuration Baseline** | C | — | — | — | — | **R+A** |
| **II-009: Build & Integration** | — | C | — | — | **R** | **A** |
| **II-010: Merge Approval** | — | — | — | — | **R+A** (2+ approvers) | — |

**Domain Owner**: Code Review Board (for quality), Deployment Manager (for ops)  
**Escalation Point**: Chief Engineer (if security critical, complexity waiver, or failed gate)

---

### Domain 4: Verification & Validation (Per NASA OAPD, USAF IV&V)

| Activity | Requirements Agent | Architecture Agent | Program Manager | Chief Engineer | Code Review Board | Deployment Manager |
|----------|------|------|------|------|------|------|
| **VV-001: Test Plan Development** | **R** | C | — | — | **A** | — |
| **VV-002: Test Case Development** | **R** | C | — | — | **A** | — |
| **VV-003: RTM Development** | **R+A** | C | — | — | — | — |
| **VV-004: Unit Test Execution** | — | — | — | — | **R+A** | — |
| **VV-005: Integration Test Execution** | — | C | — | — | **R+A** | — |
| **VV-006: System Test Execution** | — | C | — | — | **R+A** | — |
| **VV-007: Test Coverage Analysis** | — | — | — | — | **R+A** | — |
| **VV-008: Defect Tracking & Resolution** | — | — | — | — | **R+A** | — |
| **VV-009: Verification Evidence Compilation** | — | C | — | — | **R** | **A** |
| **VV-010: Validation Confirmation** | **R** | — | — | C | — | **A** |

**Domain Owner**: Code Review Board (IV&V authority)  
**Escalation Point**: Chief Engineer (if coverage < 85%, unresolved defects, validation gap)

---

### Domain 5: Configuration & Change Management

| Activity | Requirements Agent | Architecture Agent | Program Manager | Chief Engineer | Code Review Board | Deployment Manager |
|----------|------|------|------|------|------|------|
| **CCM-001: Establish Baseline** | C | C | **R** | — | — | **A** |
| **CCM-002: Change Request Intake** | C | C | **R+A** | — | — | — |
| **CCM-003: Change Impact Analysis** | **R** | **R** | — | C | — | **A** |
| **CCM-004: Change Approval** | C | C | **R** | **A** (high-risk) | — | — |
| **CCM-005: Baseline Update** | — | — | — | — | — | **R+A** |
| **CCM-006: Configuration Audit** | C | C | — | **A** | — | **R** |
| **CCM-007: Release Management** | — | — | — | — | **R** | **A** |
| **CCM-008: Version Control** | — | — | — | — | **R+A** | — |
| **CCM-009: Release Notes** | **R** | C | — | — | — | **A** |
| **CCM-010: Documentation Versioning** | **R** | **R** | — | — | — | **A** |

**Domain Owner**: Deployment Manager (ops authority), Program Manager (schedule authority)  
**Escalation Point**: Chief Engineer (if compliance/policy violation)

---

### Domain 6: Risk Management (Per NASA NHDM, USAF RMP)

| Activity | Requirements Agent | Architecture Agent | Program Manager | Chief Engineer | Code Review Board | Deployment Manager |
|----------|------|------|------|------|------|------|
| **Risk-001: Risk Identification** | **R** | **R** | C | — | **R** | **R** |
| **Risk-002: Risk Assessment** | C | **R** | — | **A** | C | C |
| **Risk-003: Risk Prioritization** | C | C | **R+A** | C | — | — |
| **Risk-004: Risk Mitigation Planning** | C | **R** | **A** | C | — | — |
| **Risk-005: Risk Mitigation Execution** | **R** | **R** | — | C | **R** | **R** |
| **Risk-006: Risk Monitoring** | C | C | **R+A** | C | — | — |
| **Risk-007: Risk Escalation** | **R** (triggers) | **R** (triggers) | — | **A** (decision) | **R** (triggers) | **R** (triggers) |
| **Risk-008: Risk Documentation** | — | — | **R** | **A** | — | — |
| **Risk-009: Safety Risk Assessment** | C | C | — | **R+A** | C | C |
| **Risk-010: Security Risk Assessment** | C | C | — | **R+A** | **R+A** | C |

**Domain Owner**: Chief Engineer (apex responsibility)  
**Escalation Point**: Chief Engineer (all risks > Medium severity)

---

### Domain 7: Governance & Decision Management

| Activity | Requirements Agent | Architecture Agent | Program Manager | Chief Engineer | Code Review Board | Deployment Manager |
|----------|------|------|------|------|------|------|
| **Gov-001: Architecture Decision Record (ADR)** | C | **R** | — | **A** | — | — |
| **Gov-002: Design Review Gate** | **R** (presents) | **R** (presents) | — | **A** (approves) | C | — |
| **Gov-003: Code Review Gate** | — | — | — | — | **R+A** | — |
| **Gov-004: Test Completion Gate** | — | — | — | — | **R+A** | — |
| **Gov-005: Deployment Readiness Gate** | — | — | — | C | — | **R+A** |
| **Gov-006: Policy Compliance Audit** | **R** | **R** | — | **A** | **R** | **R** |
| **Gov-007: Traceability Audit** | **R+A** | C | — | — | — | — |
| **Gov-008: Governance Decision Log** | — | — | — | **R+A** | — | — |
| **Gov-009: Lessons Learned** | **R** | **R** | — | **A** | **R** | **R** |
| **Gov-010: Metrics & KPI Tracking** | C | C | **R** | **A** | C | C |

**Domain Owner**: Chief Engineer (apex governance authority)  
**Escalation Point**: All governance decisions route through Chief Engineer

---

## Key RACI Rules

1. **Every Activity Has ONE "A"** (Accountable person)
   - No shared accountability
   - "A" makes final decision if consensus not reached
   - "A" signs off on deliverable

2. **R ≠ A** (Responsibility ≠ Accountability)
   - Developer (R) codes; Code Review Board (A) approves merge
   - Requirements Agent (R) elicits; Program Manager (A) gates completeness
   - Avoid: "Someone is R+A and also consulted by others" on same activity

3. **Escalation Points**:
   - Activity fails threshold → escalate to "A" role
   - Disagreement between roles → escalate to Chief Engineer
   - Safety/security flag → escalate to Chief Engineer immediately

4. **Consulted (C) vs. Informed (I)**:
   - **Consulted**: Asked for input BEFORE decision; can influence outcome
   - **Informed**: Notified AFTER decision; for situational awareness

5. **Authority Hierarchy**:
   ```
   Chief Engineer (apex A on governance/risk/design)
     ├── Program Manager (A on scheduling/scope)
     ├── Requirements Agent (A on requirement completeness)
     ├── Architecture Agent (A on design/feasibility)
     ├── Code Review Board (A on code quality/merge)
     └── Deployment Manager (A on ops/release)
   ```

---

## Activity Dependencies

Activities must be sequenced per SE phase:

```
RM-001 to RM-003 → Requirement Capture Phase
   ↓
AD-001 to AD-009 → Architecture Phase
   ↓
RM-006, II-001 to II-010 → Implementation Phase
   ↓
VV-001 to VV-010 → Verification Phase
   ↓
CCM-001, Gov-005 → Release Readiness
   ↓
CCM-007 → Deploy
   ↓
Risk-006, Gov-009 → Closeout & Learning
```

---

## Example: How RACI Flows

**Scenario**: Requirements Agent completes L2 requirements. Now what?

1. **RM-009: Requirement Completeness Review**
   - Responsibility: Requirements Agent (writes completeness report)
   - Accountability: Program Manager (decides "complete enough?")
   - Consulted: Chief Engineer (if conflicts), Architecture Agent (feasibility concerns)
   - Informed: All team

2. **Result**: Program Manager gates completion:
   - ✅ PASS → proceed to Architecture phase
   - ❌ FAIL → Requirements Agent refines, resubmits
   - ⚠️ CONCERN → escalate to Chief Engineer

3. **Next**: AD-001 System Decomposition
   - Responsibility: Architecture Agent (does decomposition)
   - Accountability: Chief Engineer (approves design)
   - Consulted: Requirements Agent (feasibility challenges?), Program Manager (schedule impact?)
   - Informed: All team

---

## Cross-Functional Coordination Rules

| Scenario | Action | Authority |
|----------|--------|-----------|
| Requirements conflict | Requirements Agent consults Architecture Agent → if unresolved, escalate | Program Manager |
| Design feasibility challenged | Architecture Agent assesses → if < 70%, escalate | Chief Engineer |
| Code quality threshold violated | Code Review Board assesses → if waiver needed, escalate | Chief Engineer |
| Test coverage below 85% | Code Review Board flags → refactor or escalate | Chief Engineer |
| Deployment risk flagged | Deployment Manager assesses → if > threshold, escalate | Chief Engineer |
| Schedule at risk | Program Manager flags → PM mitigates or escalates | Chief Engineer |

---

## Summary: Who Decides What

| Decision | Accountable Role |
|----------|-----------------|
| Requirement is complete? | Program Manager |
| Design is feasible? | Chief Engineer |
| Code is ready to merge? | Code Review Board |
| Tests are sufficient? | Code Review Board |
| System is safe to deploy? | Deployment Manager |
| Conflict resolved? | Chief Engineer |
| Risk mitigated? | Chief Engineer |

---

## INCOSE/NASA/USAF Alignment

This RACI aligns with:

✅ **INCOSE SE Handbook** (Sections 3-7): Activity definitions, responsibilities  
✅ **NASA-STD-7009A**: Technical review gates, role authority  
✅ **USAF DAU**: Acquisition phase gating, risk management, CCM  
✅ **ISO/IEC/IEEE 42010**: Architecture decision records, governance  
✅ **CMMI**: Process maturity, responsibility clarity

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

RACI is organized by SE domain (per INCOSE/NASA/USAF taxonomy):

**Existing Domains** (7):
1. **Requirements Management** (RM)
2. **Architecture & Design** (AD)
3. **Implementation & Integration** (II)
4. **Verification & Validation** (VV)
5. **Configuration & Change Management** (CCM)
6. **Risk Management** (Risk)
7. **Governance & Decision Management** (Gov)

**NEW Domains** (6) - Added for Assured SDLC:
8. **Security** (SEC) - Loss-based: Threat identification → risk scoring → mitigation → verification (25 activities)
9. **Safety** (SAF) - Loss-based: Hazard identification → risk scoring → mitigation → verification (25 activities)
10. **Compliance** (COMP) - Discovery & mitigation documentation with residual risk analysis (25 activities)
11. **Operations** (OPS) - Deployment, monitoring, incident response (10 activities)
12. **Supply Chain Risk Management** (SCRM) - Dependencies, SBOM, CVE tracking (10 activities)
13. **Integration Management** (INT) - Build, test environment, CI/CD (10 activities)

**Total: 13 SE Activity Domains with 200+ activities across 13 agents**

**Key Principle**: Security and Safety both follow loss-based systems engineering - define failures/threats upfront, score risks against program threshold, develop mitigations for risks exceeding threshold, verify mitigations, and document residual risk. Both repeat at each decomposition level (L1 → L2 → L3 → component).

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

### Domain 8: Security (Loss-Based Systems Engineering - Threat/Adversary-Induced Failures)

**Foundation**: Loss-based systems engineering with threat identification, risk scoring, mitigation, verification, and compliance documentation. Repeated at each decomposition level (L1 → L2 → L3 → component).

**Phase 1: Threat Identification & Analysis (Repeated at Each Level)**

| Activity | Req Mgr | Arch | CSO | Cyber Arch | Code Review | QA | Ops Lead | SQM |
|----------|---------|------|-----|------------|-------------|-----|----------|-----|
| **SEC-001: Threat Definition (L1)** | C | — | **R+A** | C | — | — | — | — |
| **SEC-002: Threat Decomposition (L1→L2→L3)** | C | — | **R+A** | C | — | — | — | — |
| **SEC-003: Threat Modeling per Level** | C | C | **R+A** | **R** | — | — | — | — |
| **SEC-004: Threat Characterization** | — | C | **R+A** | **R** | — | — | — | — |
| **SEC-005: Attack Vector Identification** | — | — | **R+A** | **R** | C | — | — | — |

**Phase 2: Risk Scoring & Thresholding (Against Program Threshold)**

| Activity | Req Mgr | Arch | CSO | Cyber Arch | Code Review | QA | Ops Lead | SQM |
|----------|---------|------|-----|------------|-------------|-----|----------|-----|
| **SEC-006: Consequence Classification** | — | — | **R+A** | C | — | — | — | — |
| **SEC-007: Probability Assessment** | — | — | **R+A** | C | — | — | — | — |
| **SEC-008: Risk Score Calculation** | — | — | **R+A** | C | — | — | — | — |
| **SEC-009: Risk Threshold Comparison** | — | — | **R+A** | C | — | — | — | — |
| **SEC-010: Mitigation Priority Ranking** | — | — | **R+A** | C | — | — | — | — |

**Phase 3: Mitigation Development (Risks Exceeding Threshold)**

| Activity | Req Mgr | Arch | CSO | Cyber Arch | Code Review | QA | Ops Lead | SQM |
|----------|---------|------|-----|------------|-------------|-----|----------|-----|
| **SEC-011: Security Requirements Allocation** | **R** | C | **A** | — | — | — | — | — |
| **SEC-012: Threat-Driven Architecture** | — | **R** | **A** | **R** (design patterns) | — | — | — | — |
| **SEC-013: Secure Design Pattern Selection** | — | C | C | **R+A** | — | — | — | — |
| **SEC-014: Cryptography Strategy** | — | C | C | **R+A** | — | — | — | — |
| **SEC-015: Access Control Architecture** | — | **R** | **A** | **R** | — | — | — | — |

**Phase 4: Implementation Verification (Mitigations in Code)**

| Activity | Req Mgr | Arch | CSO | Cyber Arch | Code Review | QA | Ops Lead | SQM |
|----------|---------|------|-----|------------|-------------|-----|----------|-----|
| **SEC-016: Security Code Review** | — | — | **R** (oversight) | C | **R+A** (≥2 reviewers) | — | — | — |
| **SEC-017: SAST Scanning (Pattern/Crypto)** | — | — | **R** (config) | — | **R+A** | — | — | — |
| **SEC-018: DAST Testing (Threat Vectors)** | — | — | **R** (test plan) | — | **R** | **R+A** | — | — |
| **SEC-019: Vulnerability Discovery** | — | — | **R+A** | **R** | **R** | **R** | — | — |
| **SEC-020: Vulnerability Remediation** | — | — | **R+A** | — | **R** (code fix) | C | — | C |

**Phase 5: Residual Risk & Acceptance**

| Activity | Req Mgr | Arch | CSO | Cyber Arch | Code Review | QA | Ops Lead | SQM |
|----------|---------|------|-----|------------|-------------|-----|----------|-----|
| **SEC-021: Residual Threat Assessment** | — | — | **R+A** | — | — | — | — | — |
| **SEC-022: Residual Risk Acceptance** | — | — | **R** (recommend) | — | C | — | — | — |
| **SEC-023: Authorization & Accreditation** | — | — | **A** (CSO approval) | — | C | — | — | — |
| **SEC-024: Operational Security Monitoring** | — | — | **R** (config) | — | — | — | **R+A** (execute) | — |
| **SEC-025: Security Incident Response** | — | — | **R+A** | — | — | — | **R** (execute) | — |

**Domain Owner**: Chief Security Officer  
**Key Rule**: Threat analysis → risk scoring → mitigation → verification → acceptance. Repeats at L1, L2, L3, component levels.  
**Escalation Point**: Chief Security Officer + Chief Engineer (risks exceeding threshold or residual risk acceptance)

---

### Domain 9: Safety (Loss-Based Systems Engineering - Natural/Accidental Failures)

**Foundation**: Loss-based systems engineering with hazard identification, risk scoring, mitigation, verification, and compliance documentation. Repeated at each decomposition level (L1 → L2 → L3 → component).

**Phase 1: Hazard Identification & Analysis (Repeated at Each Level)**

| Activity | Req Mgr | Arch | CSafO | Chief Eng | Code Review | QA | SQM |
|----------|---------|------|-------|-----------|-------------|-----|-----|
| **SAF-001: Functional Hazard Analysis (L1)** | C | C | **R+A** | — | — | — | — |
| **SAF-002: Hazard Decomposition (L1→L2→L3)** | C | — | **R+A** | C | — | — | — |
| **SAF-003: FMEA Development per Level** | — | C | **R+A** | C | — | — | — |
| **SAF-004: FTA Development per Level** | — | C | **R+A** | C | — | — | — |
| **SAF-005: Failure Mode Characterization** | — | C | **R+A** | C | — | — | — |

**Phase 2: Risk Scoring & Thresholding (Against Program Threshold)**

| Activity | Req Mgr | Arch | CSafO | Chief Eng | Code Review | QA | SQM |
|----------|---------|------|-------|-----------|-------------|-----|-----|
| **SAF-006: Severity Classification** | — | — | **R+A** | C | — | — | — |
| **SAF-007: Failure Probability Assessment** | — | — | **R+A** | C | — | — | — |
| **SAF-008: Risk Score Calculation** | — | — | **R+A** | C | — | — | — |
| **SAF-009: Risk Threshold Comparison** | — | — | **R+A** | C | — | — | — |
| **SAF-010: Mitigation Priority Ranking** | — | — | **R+A** | C | — | — | — |

**Phase 3: Mitigation Development (Risks Exceeding Threshold)**

| Activity | Req Mgr | Arch | CSafO | Chief Eng | Code Review | QA | SQM |
|----------|---------|------|-------|-----------|-------------|-----|-----|
| **SAF-011: Safety Requirements Allocation** | **R** | C | **A** | C | — | — | — |
| **SAF-012: Safety-Critical Component ID** | — | **R** | **A** | C | — | — | — |
| **SAF-013: Fault Tolerance Architecture** | — | **R** | **A** | C | — | — | — |
| **SAF-014: Redundancy Strategy** | — | **R** | **A** | C | — | — | — |
| **SAF-015: Monitoring & Detection Design** | — | **R** | **A** | C | — | — | — |

**Phase 4: Implementation Verification (Mitigations in Code)**

| Activity | Req Mgr | Arch | CSafO | Chief Eng | Code Review | QA | SQM |
|----------|---------|------|-------|-----------|-------------|-----|-----|
| **SAF-016: Safety-Critical Code Inspection** | — | — | **R** (lead) | — | **R+A** (≥2 expert reviewers) | — | — |
| **SAF-017: Fault Injection Testing** | — | C | **R** (plan) | — | — | **R+A** | — |
| **SAF-018: Safety-Critical Testing** | — | C | **R** (plan) | — | C | **R+A** (≥95% coverage required) | — |
| **SAF-019: Failure Detection Verification** | — | — | **R** (plan) | — | — | **R+A** | — |
| **SAF-020: Recovery Path Testing** | — | — | **R** (plan) | — | — | **R+A** | — |

**Phase 5: Residual Risk & Acceptance**

| Activity | Req Mgr | Arch | CSafO | Chief Eng | Code Review | QA | SQM |
|----------|---------|------|-------|-----------|-------------|-----|-----|
| **SAF-021: Residual Failure Assessment** | — | — | **R+A** | — | — | — | — |
| **SAF-022: Residual Risk Acceptance** | — | — | **R** (recommend) | **A** (co-sign) | — | — | — |
| **SAF-023: Safety Case Closure** | — | — | **R+A** | C | — | — | — |
| **SAF-024: Operational Safety Monitoring** | — | — | **R** (config) | — | — | — | — |
| **SAF-025: Failure Trend Monitoring** | — | — | **R** (plan) | — | — | **R+A** | — |

**Domain Owner**: Chief Safety Officer (Accountable for all safety decisions)  
**Key Rule**: Hazard analysis → risk scoring → mitigation → verification → acceptance. Repeats at L1, L2, L3, component levels.  
**Co-Approver**: Chief Engineer (residual risk acceptance & safety-critical decisions)  
**Escalation Point**: Chief Safety Officer + Chief Engineer (risks exceeding threshold)

---

### Domain 10: Compliance (Discovery, Mitigation, & Residual Risk Documentation)

**Foundation**: Document that no failures (natural or threat-induced) remain undocumented. Demonstrate discovery of hazards/threats, mitigations implemented, and residual risk analysis accepted.

**Phase 1: Compliance Planning & Standards Mapping**

| Activity | Req Mgr | CCO | CSO | CSafO | Chief Eng | Code Review | QA |
|----------|---------|-----|-----|-------|-----------|-------------|-----|
| **COMP-001: Applicable Standards Identification** | C | **R+A** | **R** (security) | **R** (safety) | C | — | — |
| **COMP-002: Compliance Requirements Mapping** | C | **R+A** | **R** (security reqs) | **R** (safety reqs) | — | — | — |
| **COMP-003: Compliance Gap Analysis** | C | **R+A** | C | C | C | — | — |
| **COMP-004: Compliance Planning & Schedule** | — | **R+A** | C | C | C | — | — |
| **COMP-005: Evidence Package Definition** | — | **R+A** | **R** (security evidence) | **R** (safety evidence) | C | — | — |

**Phase 2: Discovery & Analysis Documentation**

| Activity | Req Mgr | CCO | CSO | CSafO | Chief Eng | Code Review | QA |
|----------|---------|-----|-----|-------|-----------|-------------|-----|
| **COMP-006: Threat Analysis Documentation** | C | **R** (package) | **R+A** (analysis) | — | — | — | — |
| **COMP-007: Hazard Analysis Documentation** | C | **R** (package) | — | **R+A** (analysis) | — | — | — |
| **COMP-008: Risk Scoring Artifacts** | — | **R** (package) | **R** (security) | **R** (safety) | C | — | — |
| **COMP-009: Mitigation Strategy Documentation** | C | **R** (package) | **R** (security) | **R** (safety) | C | — | — |
| **COMP-010: Design-to-Requirements Traceability** | **R** | **R** (organize) | C | C | — | — | — |

**Phase 3: Mitigation Verification Evidence**

| Activity | Req Mgr | CCO | CSO | CSafO | Chief Eng | Code Review | QA |
|----------|---------|-----|-----|-------|-----------|-------------|-----|
| **COMP-011: Security Code Review Evidence** | — | **R** (package) | **R** (verify) | — | — | **R+A** (results) | — |
| **COMP-012: Safety-Critical Code Inspection** | — | **R** (package) | — | **R** (verify) | — | **R** (reviews) | **R+A** (results) |
| **COMP-013: SAST/DAST Test Results** | — | **R** (package) | **R** (interpret) | — | — | **R+A** (execute) | — |
| **COMP-014: Security Test Coverage** | — | **R** (package) | **R** (plan) | — | — | C | **R+A** (metrics) |
| **COMP-015: Safety Test Coverage** | — | **R** (package) | — | **R** (plan) | — | C | **R+A** (metrics ≥95%) |

**Phase 4: Residual Risk & Acceptance Documentation**

| Activity | Req Mgr | CCO | CSO | CSafO | Chief Eng | Code Review | QA |
|----------|---------|-----|-----|-------|-----------|-------------|-----|
| **COMP-016: Residual Threat Assessment Doc** | — | **R+A** (package) | **R** (assess) | — | — | — | — |
| **COMP-017: Residual Hazard Assessment Doc** | — | **R+A** (package) | — | **R** (assess) | — | — | — |
| **COMP-018: Residual Risk Analysis** | — | **R+A** | **R** (security) | **R** (safety) | C | — | — |
| **COMP-019: Risk Acceptance Evidence** | — | **R** (package) | — | — | **A** (approved) | — | — |
| **COMP-020: Undocumented Failure Analysis** | — | **R+A** | **R** (threats) | **R** (hazards) | — | C | C |

**Phase 5: Certification & Audit Closeout**

| Activity | Req Mgr | CCO | CSO | CSafO | Chief Eng | Code Review | QA |
|----------|---------|-----|-----|-------|-----------|-------------|-----|
| **COMP-021: Evidence Package Assembly** | **R** (trace) | **R+A** (organize) | **R** (security artifacts) | **R** (safety artifacts) | — | — | — |
| **COMP-022: Compliance Verification Audit** | — | **R+A** | **R** (security audit) | **R** (safety audit) | C | **R** (code artifacts) | **R** (test artifacts) |
| **COMP-023: Certifying Authority Coordination** | — | **R+A** | — | — | — | — | — |
| **COMP-024: Final Data Package Submission** | — | **R+A** | — | — | — | — | — |
| **COMP-025: Certification Maintenance** | — | **R+A** | **R** (security updates) | **R** (safety updates) | — | — | — |

**Domain Owner**: Chief Compliance Officer  
**Key Principle**: No failure (natural, accidental, or threat-induced) remains undocumented with evidence of mitigation.  
**Escalation Point**: Chief Compliance Officer + Chief Engineer (certification issues)

---

### Domain 11: Operations (NEW)

| Activity | Ops Lead | Arch | CSO | Code Review | QA | Integration Mgr | SQM |
|----------|----------|------|-----|-------------|-----|-----------------|-----|
| **OPS-001: Deployment Strategy** | **R+A** | C | C | — | — | C | — |
| **OPS-002: Deployment Procedure** | **R+A** | — | — | — | — | — | — |
| **OPS-003: Rollback Procedure** | **R+A** | — | — | — | — | C | — |
| **OPS-004: Operational Monitoring** | **R+A** | — | **R** (threat intel) | — | **R** (metrics) | — | — |
| **OPS-005: Incident Response Plan** | **R+A** | — | **R** (security incidents) | — | **R** (quality issues) | — | — |
| **OPS-006: Performance Baselining** | **R+A** | C | — | — | **R** | — | — |
| **OPS-007: Patch Management** | **R+A** | — | **R** (security patches) | **R** (code review) | — | — | **R** (dependency patches) |
| **OPS-008: Post-Deployment Validation** | **R+A** | C | — | — | **R** | — | — |
| **OPS-009: Sustainment Procedure** | **R+A** | — | — | — | — | — | — |
| **OPS-010: Disaster Recovery** | **R+A** | C | **R** (security) | — | — | — | — |

**Domain Owner**: Operations Lead  
**Escalation Point**: Operations Lead + Chief Engineer (critical issues)

---

### Domain 12: Supply Chain Risk Management (NEW)

| Activity | SQM | CSO | Cyber Arch | Code Review | Integration Mgr | Ops Lead |
|----------|-----|-----|------------|-------------|-----------------|----------|
| **SCRM-001: Dependency Identification** | **R+A** | — | C | — | C | — |
| **SCRM-002: Software Composition Analysis** | **R+A** | C | — | — | — | — |
| **SCRM-003: Vendor Assessment** | **R+A** | **R** | — | — | — | — |
| **SCRM-004: SBOM Development** | **R+A** | — | **R** (SBOM structure) | — | — | — |
| **SCRM-005: License Compliance** | **R+A** | — | — | — | — | — |
| **SCRM-006: CVE Monitoring** | **R+A** | **R** (threat eval) | — | — | — | — |
| **SCRM-007: Vulnerability Remediation** | **R** (track) | **A** (decide) | **R** (recommend) | **R** (code fix) | — | **R** (deploy patch) |
| **SCRM-008: Dependency Update** | **R** (track) | — | — | **R** (code review) | — | **R** (deploy) |
| **SCRM-009: Supply Chain Incident Response** | **R+A** | **R** (threat) | — | — | — | **R** (ops impact) |
| **SCRM-010: Supplier Quality Audit** | **R+A** | C | — | — | — | — |

**Domain Owner**: Supplier Quality Manager  
**Escalation Point**: Supplier Quality Manager + Chief Security Officer (supply chain threats)

---

### Domain 13: Integration Management (NEW)

| Activity | Integration Mgr | System Arch | Code Review | QA | Ops Lead |
|----------|-----------------|-------------|-------------|-----|----------|
| **INT-001: Integration Strategy** | **R+A** | **R** (input) | — | C | — |
| **INT-002: Build Automation** | **R+A** | — | C | — | — |
| **INT-003: CI/CD Pipeline** | **R+A** | — | **R** | **R** | C |
| **INT-004: Test Environment Setup** | **R+A** | C | — | **R** (requirements) | C |
| **INT-005: Test Data Preparation** | **R+A** | — | — | **R** | — |
| **INT-006: Build Infrastructure** | **R+A** | — | — | — | C |
| **INT-007: Artifact Management** | **R+A** | — | — | — | **R** (deployment) |
| **INT-008: Integration Testing** | **R** | C | — | **R+A** | — |
| **INT-009: Infrastructure Monitoring** | **R+A** | — | — | — | — |
| **INT-010: Build Metrics & SLA** | **R+A** | — | C | **R** | — |

**Domain Owner**: Integration & Test Manager  
**Escalation Point**: Integration & Test Manager + Program Manager (infrastructure impact)

---

## Expanded Authority Hierarchy (13 Agents)

```
Chief Engineer (APEX AUTHORITY)
├── Program Manager (Project leadership)
├── Requirements Manager (Requirements authority)
├── System Architect (Architecture authority)
├── Chief Security Officer (Security authority)
├── Chief Safety Officer (Safety authority)
├── Chief Compliance Officer (Compliance authority)
└── SUPPORTING/SPECIALIZED:
    ├── Cyber/Security Architect (Secure design patterns)
    ├── Code Review Board (Code quality, MISRA, security, safety inspection)
    ├── Quality/QA Manager (Quality gates, verification closure)
    ├── Integration & Test Manager (Build infrastructure, CI/CD)
    ├── Operations Lead (Deployment, operations, incident response)
    └── Supplier Quality Manager (SBOM, SCA, CVE, vendor risk)
```

**Key Principle**: Every activity has ONE Accountable person. No shared "A" unless explicitly co-signed (e.g., residual risk = CSafO + CE)

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
✅ **USAF System Security Engineering**: Security decision authority (Risk-010, II-004, Gov-006)  
✅ **SAE ARP 4752A & MIL-STD-882G**: Safety decision authority (Risk-009, VV-001-010, Gov-005)  
✅ **ISO/IEC/IEEE 42010**: Architecture decision records, governance  
✅ **CMMI**: Process maturity, responsibility clarity

---

## Detailed Standards References

For expanded guidance on specific domains:

- **Security Domain Details**: See [docs/references/USAF_SSE_REFERENCE.md](../references/USAF_SSE_REFERENCE.md)
  - Activities: II-004 (Security Scanning), II-006 (Security Code Review), Risk-010 (Security Risk Assessment), Gov-006 (Security Policy Audit)
  
- **Safety Domain Details**: See [docs/references/SAFETY_STANDARDS_REFERENCE.md](../references/SAFETY_STANDARDS_REFERENCE.md)
  - Activities: AD-008 (Threat/Hazard Analysis), Risk-009 (Safety Risk Assessment), VV-001-010 (Safety Verification), Gov-005 (Deployment Readiness Gate)
  
- **All Standards Mapping**: See [docs/references/REFERENCES.md](../references/REFERENCES.md)
  - Cross-reference table showing which standard governs each governance document

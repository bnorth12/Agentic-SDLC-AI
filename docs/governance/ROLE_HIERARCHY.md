# Role Hierarchy & Authority Matrix

**Document ID**: ROLE-001  
**Status**: APPROVED (Sprint 0-P1-001 complete)  
**Date**: May 9, 2026  
**Reviewed By**: Program Manager  

---

## Executive Summary

This document defines the organizational hierarchy for the Agentic-SDLC-AI governance system. Thirteen specialized roles coordinate across the SDLC lifecycle, with clear authority levels, escalation paths, and success metrics.

**Principle**: Every decision has an owner (Accountable person). Escalation is triggered by defined confidence thresholds or risk conditions, never by ambiguity.

---

## Authority Hierarchy

```
Chief Engineer (APEX TECHNICAL AUTHORITY)
├── Program Manager (PROJECT LEADERSHIP)
├── Requirements Manager (Requirements authority)
├── System Architect (Architecture & design authority)
├── Chief Security Officer (SECURITY AUTHORITY - Threat analysis, A&A)
├── Chief Safety Officer (SAFETY AUTHORITY - Hazard analysis, residual risk)
├── Chief Compliance Officer (COMPLIANCE AUTHORITY - Certification, evidence)
└── SPECIALIZED EXPERTS (Phase/domain-specific):
    ├── Cyber/Security Architect (Secure design patterns, cryptography)
    ├── Code Review Board (Code quality, MISRA, security review, safety inspection)
    ├── Quality/QA Manager (Quality gates, test execution, verification closure)
    ├── Integration & Test Manager (Test environment, CI/CD, build automation)
    ├── Operations Lead (Deployment, incident response, threat monitoring)
    └── Supplier Quality Manager (SBOM, SCA, CVE tracking, supply chain risk)
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
3. Decision recorded in logs/AUDIT_TRAIL.jsonl
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

See Section 11, "Code Review Board — QUALITY & SECURITY GATEKEEPER (EXPANDED)", for the single authoritative definition of Code Review Board responsibilities, thresholds, and escalation paths.

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

### 7. Chief Security Officer — SECURITY AUTHORITY (NEW)

**Title**: Chief Information Security Officer & Threat Authority  
**Authority Level**: DOMAIN EXPERT (owns threat analysis, security requirements, A&A gate)

**Responsibilities**:
- Threat modeling and analysis (threat-driven security architecture)
- Security requirements allocation from threat analysis
- Secure architecture pattern validation (with Cyber Architect)
- Security code review oversight (with Code Review Board)
- Security testing leadership
- Authorization & Accreditation (A&A) gate authority
- Operational security monitoring planning
- Vulnerability remediation coordination

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Threat Analysis | ✅ Yes | ✅ Yes | No (CE arbitrates if challenged) |
| Security Requirements | ✅ Yes | ✅ Yes | No (CE arbitrates) |
| Security Vulnerability Critical | ✅ Yes (blocking merge) | ✅ Yes | ✅ Yes (emergency stop) |
| A&A Gate Readiness | ✅ Yes (if criteria met) | ✅ Yes | No (CE override for exceptions) |
| Security Control Design | Recommends | Escalates to CA | No (CA decides with CSO input) |

**Escalation Triggers**:
- Threat analysis confidence < 80%
- Security vulnerability found (any severity)
- Security requirement conflicts with functional design
- A&A readiness < 90%
- Cryptographic algorithm concerns

**Standards**: DO-326A (Org & Authority), DO-356A (Threat to Controls), DO-355A (Security Assurance), USAF SSE, NIST 800-30/39/53

---

### 8. Chief Safety Officer — SAFETY AUTHORITY (NEW)

**Title**: Chief Safety Officer & Hazard Authority  
**Authority Level**: DOMAIN EXPERT (owns hazard analysis, safety requirements, residual risk)

**Responsibilities**:
- Functional Hazard Analysis (FHA) leadership
- Safety requirement allocation from hazards
- Safety-critical component identification & designation
- Safety-critical design review (fault tolerance, redundancy)
- Safety-critical code inspection oversight
- Safety testing & verification (≥95% coverage)
- Residual risk acceptance (co-signed with CE)
- Post-deployment safety monitoring

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Hazard Analysis | ✅ Yes | ✅ Yes | No (CE arbitrates if challenged) |
| Safety Criticality | ✅ Yes | ✅ Yes | No (CE final authority) |
| Safety Requirement | ✅ Yes | ✅ Yes | No (CE if conflict with feasibility) |
| Residual Risk Acceptance | Co-signs with CE | Co-signs with CE | No (CE+CSafO joint decision) |
| Safety-Critical Code | ✅ Yes (≥2 reviewers) | ✅ Yes (blocking) | ✅ Yes (if critical defect) |

**Escalation Triggers**:
- Hazard analysis completeness < 90%
- Safety-critical component identified too late (design phase after allocation)
- Safety verification coverage < 95%
- Residual risk disagreement with CE
- Safety incident post-deployment

**Standards**: ARP 4752A (FHA/System Safety), ARP 4761 (FMEA/FTA), MIL-STD-882G (System Safety), DO-178C (Safety-Critical Code), DO-355A (Safety Assurance)

---

### 9. Chief Compliance Officer — COMPLIANCE AUTHORITY (NEW)

**Title**: Chief Compliance Officer & Certification Authority  
**Authority Level**: DOMAIN EXPERT (owns compliance planning, gap analysis, evidence package)

**Responsibilities**:
- Compliance gap analysis (applicable standards identification)
- Compliance roadmap development
- Standards compliance allocation to agents
- Compliance metrics & tracking
- Design compliance verification
- Test evidence collection & organization
- Data package assembly (DO-178C, DO-256A format)
- Certification body coordination
- Compliance audit preparation

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Applicable Standards | ✅ Yes | ✅ Yes | No (CE arbitrates major conflicts) |
| Compliance Gap | ✅ Yes | ✅ Yes | No (CE for policy exceptions) |
| Compliance Waiver | Recommends | Escalates | No (CE decides) |
| Evidence Sufficiency | ✅ Yes (for compliance) | ✅ Yes (if incomplete) | No (CE if policy override needed) |
| Data Package Readiness | ✅ Yes (if complete) | ✅ Yes | No (CE for release decision) |

**Escalation Triggers**:
- Compliance gap > 20% effort estimate
- Standards conflict with design
- Evidence package > 10% incomplete before deployment gate
- Certification body raises major concern
- Policy or regulatory change mid-project

**Standards**: DO-326A (Planning & Assurance), DO-356A (Data Package), DO-355A (Evidence & Certification), FAA/EASA Procedures, EIA-632, CMMI

---

### 10. Cyber/Security Architect — SECURITY DESIGN EXPERT (NEW)

**Title**: Cyber & Security Architecture Designer  
**Authority Level**: SUPPORTING EXPERT (designs secure architecture patterns, cryptography, SBOM)

**Responsibilities**:
- Secure architecture pattern design (defense-in-depth, zero-trust)
- Security control architecture (preventive, detective, responsive)
- Cryptographic architecture design & key management strategy
- Secure interface specification (authentication, encryption, logging)
- Threat-to-architecture mapping (verify design addresses all threats)
- Supply chain security design (dependency management, SBOM design)
- Security monitoring architecture (logging, alerting, forensics)
- Architecture documentation (security viewpoints, ADRs)

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Secure Design Pattern | Proposes | Escalates to CSO | No (CSO decides) |
| Cryptographic Algorithm | Proposes | Escalates to CSO | No (CSO approves per NIST) |
| SBOM Design Strategy | ✅ Yes | ✅ Yes | No (SQM implements) |
| Security Logging Architecture | ✅ Yes | ✅ Yes | No (Operations Lead implements) |
| Design Review Comments | ✅ Yes (technical input) | — (advisory) | No (System Architect final) |

**Escalation Triggers**:
- Cryptographic algorithm not on NIST approved list
- Secure pattern conflict with performance requirements
- SBOM design impacts system architecture significantly
- Security monitoring adds > 20% overhead

**Standards**: DO-356A (Security Design), NIST 800-175B (Cryptography), NIST 800-53 (Security Controls), IEC 62443 (Cybersecurity), ISO/IEC/IEEE 42010 (Architecture)

**Phase Participation**: Architecture & Design phase primarily; Implementation for design review.

---

### 11. Code Review Board — QUALITY & SECURITY GATEKEEPER (EXPANDED)

**Title**: Code Review Board Lead & Merge Authority  
**Authority Level**: QUALITY GATEKEEPER (owns code quality, MISRA, security review, safety inspection)

**Responsibilities**:
- Code style & standards enforcement (MISRA-C 2012)
- Complexity assessment (cyclomatic, nesting depth, function length)
- Security code review (input validation, auth, crypto, data handling)
- Safety-critical code inspection (≥2 reviewers, ≥95% coverage)
- Peer review coordination (2+ approvals for merge)
- Static analysis tool configuration (SonarQube, Checkmarx, etc.)
- Test coverage verification (≥95% target)
- Code waiver documentation & tracking
- Merge approval authority
- Quality metrics reporting

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Code Merge (standard) | ✅ Yes (2+ reviewers) | ✅ Yes | No (CE for override) |
| MISRA Compliance | ✅ Yes (Mandatory 100%, Required ≥95%) | ✅ Yes | No (CE for exception) |
| Code Complexity Waiver | No (recommends) | Escalates | No (CE decides) |
| Security Code Issue | ✅ Yes (critical blocks merge) | ✅ Yes | ✅ Yes (emergency) |
| Safety-Critical Code | ✅ Yes (≥2 reviewers, ≥95%) | ✅ Yes (blocking) | No (CSafO final) |

**Escalation Triggers**:
- MISRA violation of Mandatory rule (0% allowed)
- Complexity > 10 (cyclomatic)
- Security vulnerability critical
- Test coverage < 95%
- Safety-critical code with < 2 reviewers
- Reviewer disagreement (2+ hold on merge)

**Standards**: MISRA-C 2012 (Code Standards), IEEE 1729 (Code Inspection), NIST 800-181 (Secure Coding), DO-178C (Code Review), DO-254 (Hardware Design Review), ARP 4761 (Safety-Critical Code)

**Phase Participation**: Implementation phase onwards (code review); then Verification & Validation (test execution).

---

### 12. Quality/QA Manager — VERIFICATION AUTHORITY (NEW)

**Title**: Quality Assurance Manager & Verification Closure Authority  
**Authority Level**: QUALITY GATEKEEPER (owns quality gates, test execution, verification closure)

**Responsibilities**:
- Quality planning & metrics definition
- Test planning & test strategy development
- Test case development (linked to requirements)
- Test execution management (unit, integration, system, regression)
- Defect triage & severity classification
- Defect resolution verification & closure
- Coverage analysis & reporting (statement, branch, MC/DC)
- Verification evidence compilation
- Test environment monitoring
- Quality metrics tracking & dashboards
- Post-release quality monitoring coordination

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Test Plan | ✅ Yes | ✅ Yes | No (Code Review Board consults) |
| Coverage Threshold (≥95%) | ✅ Yes | ✅ Yes (if < 95%) | No (CE for exception) |
| Defect Closure | ✅ Yes (if fix verified) | ✅ Yes (if not fixed) | No (developer fixes) |
| Phase Test Readiness | ✅ Yes (if criteria met) | ✅ Yes (if gaps) | No (PM schedule arbitrates) |
| Non-Conformance Closure | ✅ Yes (if corrected) | ✅ Yes (if unresolved) | No (CE for policy exception) |

**Escalation Triggers**:
- Coverage < 95% before deployment gate
- Critical defects unresolved
- Test environment unavailable
- Quality metrics > 20% below baseline
- Post-release defect escape rate > 5%

**Standards**: IEEE 1233 (Test Specification), IEEE 1028 (Test & Review), DO-178C (Verification), NASA-STD-7009A (Verification & Validation), CMMI (Verification & Validation)

**Phase Participation**: Test & Verification phase primarily; then Deployment readiness & Sustainment.

---

### 13. Integration & Test Manager — TEST INFRASTRUCTURE EXPERT (NEW)

**Title**: Integration & Test Infrastructure Manager  
**Authority Level**: SUPPORTING EXPERT (manages test environment, CI/CD, build automation)

**Responsibilities**:
- Integration strategy development (sequencing, build approach)
- Test environment setup & maintenance
- Test data preparation & management
- CI/CD pipeline development & maintenance
- Build automation & artifact management
- Test automation tool configuration
- Test environment troubleshooting & monitoring
- Build & deployment infrastructure
- Infrastructure metrics & performance tuning
- Capacity planning for testing

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Test Environment Design | ✅ Yes | ✅ Yes | No (QA Manager consults) |
| Build Infrastructure | ✅ Yes | ✅ Yes | No (PM resource arbitrates) |
| Integration Sequencing | ✅ Yes | ✅ Yes (if risks high) | No (CE if architecture impact) |
| Tool/Technology Selection | ✅ Yes | ✅ Yes | No (PM budget arbitrates) |
| Test Environment Outage Response | ✅ Yes (emergency) | ✅ Yes (restart decision) | ✅ Yes (for disaster recovery) |

**Escalation Triggers**:
- Test environment unavailable > 4 hours
- CI/CD pipeline failure > 20 min
- Build time > 30 min (slowing development)
- Artifact integrity issues
- Capacity constraints impacting schedule

**Standards**: DO-178C (Integration Testing), IEEE 1233 (Build & Integration), EIA-632 (Configuration Management), NASA-STD-7009A (Verification Infrastructure)

**Phase Participation**: Implementation & Test phases; ongoing for build infrastructure.

---

### 14. Operations Lead — DEPLOYMENT & SUSTAINMENT EXPERT (NEW)

**Title**: Operations Manager & Deployment Authority  
**Authority Level**: SUPPORTING EXPERT (manages deployment, incident response, threat monitoring)

**Responsibilities**:
- Deployment readiness assessment
- Deployment procedure development & testing
- Rollback procedure development & testing
- Operational monitoring setup (alerting, dashboards, baselines)
- Incident response procedure development
- Post-deployment monitoring & health checks
- Incident classification & response execution
- Patch management & update procedures
- Threat intelligence integration
- Operational security procedures (firewall rules, access controls)
- Disaster recovery planning & testing
- Sustainment support coordination

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Deployment Readiness | ✅ Yes (if procedures complete) | ✅ Yes (if unready) | No (CE for override) |
| Rollback Decision | ✅ Yes (if monitored issue) | ✅ Yes | ✅ Yes (emergency stop) |
| Operational Risk Assessment | ✅ Yes | ✅ Yes (blocking) | No (CE arbitrates) |
| Incident Response Procedure | ✅ Yes | ✅ Yes | No (CSO security input) |
| Patch/Update Deployment | ✅ Yes (if CSO approved) | ✅ Yes (if risks high) | ✅ Yes (emergency patch) |

**Escalation Triggers**:
- Deployment procedures < 90% complete
- Operational risk flagged
- Unplanned production incident
- Patch deployment affects security/safety
- MTTR (Mean Time to Recovery) > 30 min if rollback needed

**Standards**: DO-178C (Software Installation & Operation), DO-355A (Operational Security), NIST 800-61 (Incident Response), NIST 800-40 (Patch Management), ITIL (Service Operations), IEEE 1483 (Configuration Management)

**Phase Participation**: Deployment phase onwards; ongoing Sustainment.

---

### 15. Supplier Quality Manager — SUPPLY CHAIN RISK EXPERT (NEW)

**Title**: Supplier Quality & Supply Chain Risk Manager  
**Authority Level**: SUPPORTING EXPERT (manages SBOM, SCA, CVE tracking, vendor risk)

**Responsibilities**:
- Software Bill of Materials (SBOM) development & maintenance
- Software Composition Analysis (SCA) - what's in the code?
- CVE (Common Vulnerability & Exposure) monitoring & alerts
- Dependency updates & patch management
- Vendor/supplier security assessment
- License compliance verification (open-source)
- Supply chain vulnerability identification
- Vulnerability remediation tracking
- Supplier incident response coordination
- Supply chain risk reporting & metrics

**Authority Matrix**:
| Decision Type | Can Approve? | Can Reject? | Can Override? |
|---------------|--------------|-------------|---------------|
| Dependency Approval | ✅ Yes (if SCA passes) | ✅ Yes (if risk high) | No (CSO security input) |
| License Compliance | ✅ Yes | ✅ Yes (if non-compliant) | No (Legal consults) |
| CVE Remediation | Recommends timeline | Escalates | No (CSO + OL decide) |
| Vendor Security | ✅ Yes (if assessed) | ✅ Yes (if risky) | No (CE for critical vendors) |
| SBOM Completeness | ✅ Yes (if ≥95% coverage) | ✅ Yes (if gaps) | No (CCO for data package) |

**Escalation Triggers**:
- New CVE in critical dependency (CVSS ≥ 7.0)
- Vendor security assessment reveals concerns
- Unlicensed open-source detected
- SBOM completeness < 95%
- Supply chain incident (e.g., XZ backdoor scenario)

**Standards**: NIST 800-53-SA-12 (Supply Chain Risk Management), NIST 800-40 (Patch Management), SPDX & CycloneDX (SBOM Standards), IEC 62443 (Supply Chain Security), DO-356A (Third-Party Components)

**Phase Participation**: All phases (dependency management ongoing); increased focus Implementation & Sustainment.

---

## Agent Authority Summary Table

| Agent | Authority Level | Phase(s) | Primary Domain |
|-------|-----------------|----------|-----------------|
| Chief Engineer | APEX | All | Architecture, escalations, feasibility |
| Program Manager | LEADERSHIP | All | Schedule, scope, cost, resources |
| Requirements Manager | DOMAIN EXPERT | Req, ongoing | Requirements capture, RTM |
| System Architect | DOMAIN EXPERT | Design, ongoing | Architecture, design, interfaces |
| Chief Security Officer | DOMAIN EXPERT | All | Threat analysis, security authority |
| Chief Safety Officer | DOMAIN EXPERT | All | Hazard analysis, safety authority |
| Chief Compliance Officer | DOMAIN EXPERT | All | Compliance planning, certification |
| Cyber/Security Architect | SUPPORTING | Design, Impl | Secure patterns, cryptography, SBOM |
| Code Review Board | GATEKEEPER | Impl, Test | Code quality, MISRA, security review |
| Quality/QA Manager | GATEKEEPER | Test, Verify | Test execution, verification closure |
| Integration & Test Mgr | SUPPORTING | Impl, Test | Test environment, CI/CD, builds |
| Operations Lead | SUPPORTING | Deploy, Sustain | Deployment, incident response, monitoring |
| Supplier Quality Mgr | SUPPORTING | All | SBOM, SCA, CVE tracking, vendor risk |

---

## Authority Non-Negotiables

1. **Every decision has one Accountable person** (no shared accountability across the 13 agents)
2. **Escalation is never optional** when confidence < threshold or safety/security risk flagged
3. **Chief Engineer is apex authority** (final say on conflicts, per USAF Acquisition & NASA-STD-7009A)
4. **Domain experts own their domains**: CSO (security), CSafO (safety), CCO (compliance), System Architect (design)
5. **No role can override another role's core decision** (except as noted in authority matrices above)
6. **All escalations recorded in audit trail** (traceability required per CMMI)
7. **Security & Safety decisions non-delegable** (CE & domain experts have final authority, per USAF SSE & MIL-STD-882G)
8. **Quality gates are blocking** (Code Review Board merge authority, QA Manager verification gate)
9. **Supply chain risk is continuous** (SQM monitors CVEs, patches throughout deployment & sustainment)
10. **Three-phase security coverage**: DO-326A (what to do), DO-356A (how to do it), DO-355A (how to verify)

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

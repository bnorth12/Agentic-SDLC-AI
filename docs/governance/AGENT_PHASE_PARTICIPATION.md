# Agent Phase Participation Matrix

**Document ID**: GOV-PHASE-001  
**Date**: May 11, 2026  
**Purpose**: Define when each of 13 agents engages and exits per SDLC phase  
**Scope**: Requirements → Sustainment lifecycle phases

---

## Executive Summary

This document specifies the phase-by-phase engagement model for 13 specialized agents. Each agent has:
- **Entry Criteria** (when they join the phase)
- **Primary Activities** (key work items for that phase)
- **Exit Criteria** (when they can depart or reduce involvement)
- **Escalation Touchpoints** (where their decisions impact other phases)

**Principle**: No agent remains at 100% allocation throughout. Each scales up/down per phase needs.

---

## Phase Definitions

| Phase | Duration | Focus | Entry Gate | Exit Gate |
|-------|----------|-------|-----------|-----------|
| **Requirements** | Weeks 1-2 | Capture & decompose needs | Kickoff | ≥80% completeness, RTM approved |
| **Architecture** | Weeks 3-4 | Design system & components | Req gate pass | ≥70% feasibility, design reviewed |
| **Implementation** | Weeks 5-8 | Code & integrate | Arch gate pass | ≥95% code complete, ready for test |
| **Test & Verify** | Weeks 9-10 | Execute tests, close defects | Impl gate pass | ≥95% coverage, zero critical defects |
| **Deployment** | Week 11 | Prepare & deploy to prod | Test gate pass | Zero deployment blockers |
| **Sustainment** | Weeks 12+ | Monitor, maintain, update | Deployment success | Program lifecycle end |

---

## Phase 1: Requirements (Weeks 1-2)

### Phase Gate Entry Criteria
- ✅ Project charter approved
- ✅ Stakeholders identified
- ✅ Kickoff meeting held
- ✅ Requirements template ready

### Phase Gate Exit Criteria (Phase 1 → Phase 2)
- ✅ Requirement completeness ≥80%
- ✅ RTM developed & reviewed
- ✅ Acceptance criteria defined for all L1 requirements
- ✅ Requirements Review Board (RRB) approval
- ✅ Security & Safety requirements integrated
- ✅ Compliance requirements identified
- ✅ Sign-off: Requirements Manager, Program Manager, Chief Engineer

---

## Requirements Phase: Agent Participation

### CORE AGENTS

#### Chief Engineer
- **Allocation**: 25% (oversight, escalations)
- **Entry**: Kickoff
- **Primary Activities**:
  - Approve requirements completeness gate (≥80%)
  - Review feasibility assumptions
  - Resolve escalations (if requirements conflict with safety/security)
  - Attend Requirements Review Board (RRB) meeting
- **Exit Criteria**: Requirements gate signed off
- **Handoff**: To architecture phase (feasibility assessment from Architect)

#### Program Manager
- **Allocation**: 50% (schedule, scope, stakeholder coordination)
- **Entry**: Project kickoff
- **Primary Activities**:
  - Develop project schedule & milestones
  - Allocate resources to requirements team
  - Manage stakeholder communication
  - Gate readiness assessment (scope, schedule, risk)
  - CCB chair for requirement change requests
- **Exit Criteria**: Phase gate approved, schedule baselined
- **Handoff**: To architecture phase (resource planning for design team)

#### Requirements Manager
- **Allocation**: 100% (full-time requirements focus)
- **Entry**: Week 0 (pre-project planning)
- **Primary Activities**:
  - Elicit stakeholder needs (interviews, workshops)
  - Capture L1 requirements (stakeholder-facing)
  - Define acceptance criteria (SMART criteria)
  - Decompose L1 → L2/L3 requirements (detailed)
  - Develop Requirements Traceability Matrix (RTM)
  - Integrate security requirements (from CSO threat list)
  - Integrate safety requirements (from CSafO hazard list)
  - Change request processing (early phase change requests)
- **Exit Criteria**: ≥80% completeness, RTM approved, RRB sign-off
- **Handoff**: To architecture phase (reduced allocation, ongoing RTM updates)

#### System Architect
- **Allocation**: 10% (feasibility input only)
- **Entry**: Mid-requirements phase (week 1, after L2 decomposition)
- **Primary Activities**:
  - Review requirement feasibility (rough architecture estimate)
  - Flag infeasible requirements (architecture perspective)
  - Provide feasibility confidence to Requirements Manager
  - Escalate feasibility concerns to CE if < 70% confidence
- **Exit Criteria**: Feasibility assessment complete
- **Handoff**: To architecture phase (full-time design focus)

#### Chief Security Officer
- **Allocation**: 30% (threat analysis, security requirements)
- **Entry**: Week 1 (early phase for threat identification)
- **Primary Activities**:
  - Threat modeling (identify threat categories: access, data, crypto, interface, supply chain)
  - Security requirement allocation from threats (what security features needed?)
  - Security testing requirement definition
  - Integration of security requirements into RTM
  - Participate in RRB (security completeness gate)
- **Exit Criteria**: Security requirements integrated, threat model approved
- **Handoff**: To architecture phase (design review for secure patterns)

#### Chief Safety Officer
- **Allocation**: 20% (hazard analysis start)
- **Entry**: Week 1 (early phase for hazard identification)
- **Primary Activities**:
  - Functional Hazard Analysis (FHA) start
  - Safety-critical function identification
  - Safety requirement allocation from hazards
  - Integration of safety requirements into RTM
  - Participate in RRB (safety completeness gate)
- **Exit Criteria**: Initial FHA complete, safety requirements in RTM
- **Handoff**: To architecture phase (design review for safety-critical components)

#### Chief Compliance Officer
- **Allocation**: 20% (compliance planning)
- **Entry**: Week 0 (pre-project planning, before kickoff)
- **Primary Activities**:
  - Compliance gap analysis (what standards apply?)
  - Compliance roadmap development
  - Compliance requirements identification (data protection, audit trails, etc.)
  - Integration of compliance requirements into RTM
  - Participate in RRB (compliance readiness gate)
- **Exit Criteria**: Applicable standards identified, compliance roadmap approved
- **Handoff**: To architecture phase (ongoing compliance tracking)

### SPECIALIZED AGENTS

#### Cyber/Security Architect
- **Allocation**: 0% (not yet needed)
- **Entry**: Architecture phase (week 3)
- **Note**: Remains in Planning state; participates in RRB as observer if needed

#### Code Review Board
- **Allocation**: 0% (code doesn't exist yet)
- **Entry**: Implementation phase (week 5)
- **Note**: Remains in Planning state; establishes code review standards as observer

#### Quality/QA Manager
- **Allocation**: 10% (test planning)
- **Entry**: Mid-requirements (week 1.5)
- **Primary Activities**:
  - Quality planning & metrics definition
  - Test strategy definition (how to verify requirements?)
  - Test case planning (structure, format)
  - Participate in RRB (test completeness assessment)
- **Exit Criteria**: Test strategy approved, test plan outline ready
- **Handoff**: To architecture phase (test environment planning)

#### Integration & Test Manager
- **Allocation**: 5% (infrastructure planning)
- **Entry**: Mid-requirements (week 1.5)
- **Primary Activities**:
  - Test environment planning (hardware, OS, tools)
  - CI/CD pipeline design (requirements for testing phase)
  - Build infrastructure requirements
- **Exit Criteria**: Test infrastructure plan ready
- **Handoff**: To architecture/implementation phase (infrastructure setup)

#### Operations Lead
- **Allocation**: 5% (operational requirements)
- **Entry**: Late requirements (week 1.75)
- **Primary Activities**:
  - Operational requirement definition (deployment, monitoring)
  - Deployment procedure outline
  - Operational monitoring requirements
  - Escalate any operational constraints to RM
- **Exit Criteria**: Operational requirements captured
- **Handoff**: To deployment phase (full operational planning)

#### Supplier Quality Manager
- **Allocation**: 10% (dependency planning)
- **Entry**: Early requirements (week 0.5)
- **Primary Activities**:
  - Identify external dependencies (libraries, frameworks)
  - Vendor assessment planning
  - SBOM strategy definition
  - Supplier quality requirements capture
- **Exit Criteria**: Vendor list & SBOM strategy approved
- **Handoff**: To implementation phase (ongoing SBOM development)

---

## Phase 2: Architecture (Weeks 3-4)

### Phase Gate Entry Criteria
- ✅ Requirements ≥80% complete, RRB approved
- ✅ Feasibility confidence ≥70%
- ✅ Security & safety requirements baselined
- ✅ Compliance roadmap approved
- ✅ Resources allocated to architecture team

### Phase Gate Exit Criteria (Phase 2 → Phase 3)
- ✅ High-level design (HLD) complete & reviewed
- ✅ Low-level design (LLD) complete for critical paths
- ✅ Design complexity ≤ 10 (cyclomatic)
- ✅ Interface specifications (ICD) complete
- ✅ Safety-critical components identified & designed
- ✅ Secure architecture patterns validated
- ✅ Design Review Board (DRB) approval
- ✅ Sign-off: System Architect, Chief Engineer, Code Review Board

---

## Architecture Phase: Agent Participation

### CORE AGENTS

#### Chief Engineer
- **Allocation**: 40% (design authority, reviews, escalations)
- **Entry**: Architecture gate (week 3)
- **Primary Activities**:
  - Approve HLD & LLD (feasibility ≥70%)
  - Complexity assessment (CC, nesting, fan-out limits)
  - Design trade-off decisions
  - Attend Design Review Board (DRB)
  - Escalation resolution (design conflicts)
- **Exit Criteria**: Design gate signed, ready for implementation
- **Handoff**: To implementation phase (code review oversight)

#### Program Manager
- **Allocation**: 30% (schedule, resources, scope)
- **Entry**: Architecture gate
- **Primary Activities**:
  - Schedule architecture activities
  - Resource allocation to design team
  - Change control (any requirement changes)
  - Risk prioritization (design risks)
  - Coordinate with QA for test environment planning
- **Exit Criteria**: Phase gate approved, architecture schedule baselined
- **Handoff**: To implementation phase (resource management for coding)

#### Requirements Manager
- **Allocation**: 20% (ongoing RTM updates)
- **Entry**: Reduced from Requirements phase
- **Primary Activities**:
  - Update RTM (trace requirements to design)
  - Process requirement change requests (if any)
  - Requirement feasibility validation (comparing design to requirements)
  - Participate in DRB (requirement traceability check)
- **Exit Criteria**: RTM updated to design level, no orphans
- **Handoff**: To implementation phase (ongoing RTM maintenance)

#### System Architect
- **Allocation**: 100% (full-time design focus)
- **Entry**: Architecture gate (week 3)
- **Primary Activities**:
  - System decomposition (functions → components)
  - HLD development (subsystem design)
  - LLD development (component design, critical paths)
  - Component allocation to requirements
  - Interface specification (ICD)
  - Complexity assessment (CC, nesting, etc.)
  - Design Review Board (DRB) chair
  - Safety-critical component identification (with CSafO)
  - Secure architecture pattern design (with Cyber Architect)
  - Architecture Decision Record (ADR) documentation
- **Exit Criteria**: HLD/LLD approved, design gate signed
- **Handoff**: To implementation phase (design review oversight)

#### Chief Security Officer
- **Allocation**: 25% (secure design review)
- **Entry**: Architecture gate
- **Primary Activities**:
  - Security architecture review (threat-to-design mapping)
  - Threat mitigation validation (are all threats addressed?)
  - Secure control design review (with Cyber Architect)
  - A&A readiness start (compliance posture evaluation)
  - Participate in DRB (security design completeness)
- **Exit Criteria**: Security design approved, threat-to-architecture mapping complete
- **Handoff**: To implementation phase (code review security oversight)

#### Chief Safety Officer
- **Allocation**: 30% (safety-critical design)
- **Entry**: Architecture gate
- **Primary Activities**:
  - FMEA/FTA development (from FHA baseline)
  - Safety-critical component identification
  - Fault tolerance & redundancy design review
  - Single-point failure analysis
  - Safety-critical design standards review
  - Residual risk assessment start
  - Participate in DRB (safety design completeness)
- **Exit Criteria**: FMEA/FTA complete, safety-critical components approved
- **Handoff**: To implementation phase (safety code inspection oversight)

#### Chief Compliance Officer
- **Allocation**: 15% (compliance design review)
- **Entry**: Mid-architecture (week 3.5)
- **Primary Activities**:
  - Design compliance review (does design meet standards?)
  - Configuration management design (baselines, versioning)
  - Compliance metrics definition (traceability, evidence)
  - Data package framework design (what evidence to collect?)
  - Participate in DRB (compliance design readiness)
- **Exit Criteria**: Compliance design reviewed, data package plan ready
- **Handoff**: To implementation/test phase (evidence collection)

### SPECIALIZED AGENTS

#### Cyber/Security Architect
- **Allocation**: 40% (secure design patterns)
- **Entry**: Architecture gate (week 3)
- **Primary Activities**:
  - Secure architecture pattern design (defense-in-depth, zero-trust)
  - Security control architecture (preventive, detective, responsive)
  - Cryptographic architecture design (algorithms, key management)
  - Secure interface specification (authentication, encryption, logging)
  - Threat-to-design mapping (validate design addresses threats)
  - SBOM design (dependency structure)
  - Security monitoring architecture (logging, alerting)
  - Architecture Decision Record (ADR) for security patterns
- **Exit Criteria**: Secure design patterns approved, SBOM structure ready
- **Handoff**: To implementation phase (secure code review)

#### Code Review Board
- **Allocation**: 15% (quality standards preparation)
- **Entry**: Mid-architecture (week 3.5)
- **Primary Activities**:
  - Code review standards definition (MISRA rules, complexity limits)
  - Code review process design (peer review workflow)
  - Static analysis tool configuration planning
  - Test coverage expectations (≥95% target)
  - Design review participation (complexity estimation)
- **Exit Criteria**: Code review standards documented, tools planned
- **Handoff**: To implementation phase (active code review)

#### Quality/QA Manager
- **Allocation**: 30% (test planning)
- **Entry**: Architecture gate
- **Primary Activities**:
  - Test plan development (full test strategy)
  - Test case structure design (from requirements & design)
  - Coverage target definition (statement, branch, MC/DC for safety)
  - Quality metrics dashboard setup
  - Verification closure criteria definition
  - Participate in DRB (test completeness assessment)
- **Exit Criteria**: Test plan approved, coverage targets set
- **Handoff**: To implementation/test phase (test execution)

#### Integration & Test Manager
- **Allocation**: 40% (infrastructure setup)
- **Entry**: Architecture gate
- **Primary Activities**:
  - Integration strategy (sequencing, build approach)
  - Test environment setup (hardware, OS, databases)
  - CI/CD pipeline development
  - Build automation design
  - Test data preparation (structure, volume)
  - Infrastructure metrics design
- **Exit Criteria**: Test environment ready, CI/CD pipeline functional
- **Handoff**: To implementation phase (infrastructure operation)

#### Operations Lead
- **Allocation**: 20% (operational design)
- **Entry**: Mid-architecture (week 3.5)
- **Primary Activities**:
  - Deployment procedure design
  - Rollback procedure design (for validation)
  - Operational monitoring architecture design
  - Incident response procedure outline
  - Operational documentation planning
- **Exit Criteria**: Deployment procedures outlined, monitoring design ready
- **Handoff**: To deployment phase (finalize & execute procedures)

#### Supplier Quality Manager
- **Allocation**: 25% (SBOM development start)
- **Entry**: Architecture gate
- **Primary Activities**:
  - SBOM development (from architecture design)
  - Software composition analysis planning
  - Vendor security assessment (initial vendors identified)
  - License compliance check (open-source licensing)
  - Supply chain risk assessment
  - CVE monitoring setup planning
- **Exit Criteria**: Initial SBOM created, vendors assessed
- **Handoff**: To implementation phase (SBOM updates, SCA execution)

---

## Phase 3: Implementation (Weeks 5-8)

### Phase Gate Entry Criteria
- ✅ Design ≥70% feasible, DRB approved
- ✅ Code review standards established
- ✅ Test environment ready
- ✅ Secure patterns approved
- ✅ Safety-critical components identified
- ✅ Resources allocated to development team

### Phase Gate Exit Criteria (Phase 3 → Phase 4)
- ✅ Code ≥95% complete
- ✅ Code complexity meets standards (CC ≤ 10)
- ✅ MISRA compliance ≥95% (Mandatory 100%, Required ≥95%)
- ✅ Security code review complete (critical issues resolved)
- ✅ Unit tests ≥95% coverage
- ✅ SBOM complete & analyzed (CVE checked)
- ✅ Build automation operational
- ✅ Sign-off: Code Review Board, Quality Manager, Chief Engineer

---

## Implementation Phase: Agent Participation

### CORE AGENTS

#### Chief Engineer
- **Allocation**: 15% (escalations, waivers)
- **Entry**: Implementation gate
- **Primary Activities**:
  - Approve code quality waivers (complexity > 10)
  - Escalation resolution (code review conflicts)
  - Security/safety waiver approval
  - Code Inspection Board (CIB) oversight
  - Gate readiness assessment
- **Exit Criteria**: Implementation gate approved, ready for testing
- **Handoff**: To test phase (verification oversight)

#### Program Manager
- **Allocation**: 25% (schedule, resources, risk)
- **Entry**: Implementation gate
- **Primary Activities**:
  - Schedule code development sprints
  - Resource allocation (developers, reviewers)
  - Risk tracking (implementation risks)
  - Change control (any design changes)
  - Defect trend monitoring (early warning)
- **Exit Criteria**: Phase gate approved, implementation schedule baselined
- **Handoff**: To test phase (schedule management for testing)

#### Requirements Manager
- **Allocation**: 10% (ongoing RTM updates)
- **Entry**: Reduced from architecture phase
- **Primary Activities**:
  - RTM updates (trace requirements to code)
  - Requirement change requests (if any)
  - Participate in code inspection (requirement traceability)
- **Exit Criteria**: RTM complete (requirements → design → code)
- **Handoff**: To test phase (test case linkage)

#### System Architect
- **Allocation**: 20% (design review, escalations)
- **Entry**: Reduced from architecture phase
- **Primary Activities**:
  - Design review (code vs. design match)
  - Complexity review (code complexity within limits)
  - Interface validation (components communicate per spec)
  - Escalation resolution (design change requests)
- **Exit Criteria**: Code matches design, no major deviations
- **Handoff**: To test phase (test verification)

#### Chief Security Officer
- **Allocation**: 20% (security code review, threat monitoring)
- **Entry**: Implementation gate
- **Primary Activities**:
  - Security code review oversight (input validation, auth, crypto)
  - Vulnerability scanning (SAST results review)
  - Threat-to-code mapping (are threats mitigated in code?)
  - Security waiver approval (if needed)
  - Participate in Code Inspection Board (CIB)
- **Exit Criteria**: Security code review complete, SAST clean
- **Handoff**: To test phase (security test execution)

#### Chief Safety Officer
- **Allocation**: 25% (safety code review)
- **Entry**: Implementation gate
- **Primary Activities**:
  - Safety-critical code inspection (≥2 reviewers)
  - Fault handling code review (exception handling)
  - Recovery mechanism validation
  - Safety waiver approval (if needed)
  - Participate in Code Inspection Board (CIB)
- **Exit Criteria**: Safety-critical code approved, fault handling validated
- **Handoff**: To test phase (safety test execution)

#### Chief Compliance Officer
- **Allocation**: 10% (compliance tracking)
- **Entry**: Early implementation (week 5.5)
- **Primary Activities**:
  - Evidence collection start (code metrics, review records)
  - Compliance audit trail maintenance
  - Configuration management baseline setup
  - Documentation versioning
- **Exit Criteria**: Evidence collection process established
- **Handoff**: To test phase (evidence compilation continues)

### SPECIALIZED AGENTS

#### Cyber/Security Architect
- **Allocation**: 15% (security pattern validation)
- **Entry**: Early implementation (week 5.5)
- **Primary Activities**:
  - Secure code pattern validation (design patterns implemented?)
  - Cryptography implementation review
  - SBOM dependency verification (match architecture?)
  - Secure logging implementation check
- **Exit Criteria**: Security patterns validated in code
- **Handoff**: To test phase (security test design)

#### Code Review Board
- **Allocation**: 100% (full-time code review)
- **Entry**: Implementation gate (week 5)
- **Primary Activities**:
  - Peer code review (2+ reviewers per merge)
  - MISRA compliance verification (Mandatory 100%, Required ≥95%)
  - Complexity assessment (CC ≤ 10, nesting ≤ 5, LOC ≤ 50)
  - Security code review (with CSO oversight)
  - Safety code inspection (with CSafO oversight)
  - Merge approval authority
  - Code quality metrics reporting
  - Static analysis tool operation (SonarQube, Checkmarx)
- **Exit Criteria**: ≥95% code complete, MISRA ≥95% compliant
- **Handoff**: To test phase (test code review)

#### Quality/QA Manager
- **Allocation**: 20% (test preparation)
- **Entry**: Early implementation (week 5.5)
- **Primary Activities**:
  - Test case development (detailed test cases)
  - Test data preparation
  - Quality metrics baseline setup
  - Unit test result monitoring (developers responsible)
  - Defect tracking setup
- **Exit Criteria**: Test cases ready, test data prepared
- **Handoff**: To test phase (full test execution)

#### Integration & Test Manager
- **Allocation**: 50% (build infrastructure operation)
- **Entry**: Implementation gate
- **Primary Activities**:
  - CI/CD pipeline operation (daily builds)
  - Build troubleshooting & maintenance
  - Test environment monitoring & support
  - Build metrics (build time, failure rate)
  - Artifact storage & management
- **Exit Criteria**: Builds stable, CI/CD reliable
- **Handoff**: To test phase (test environment operation)

#### Operations Lead
- **Allocation**: 5% (operational consideration)
- **Entry**: Late implementation (week 7)
- **Primary Activities**:
  - Operational monitoring code review (logging, alerting)
  - Performance monitoring capability validation
  - Operational documentation update
- **Exit Criteria**: Operational monitoring code ready
- **Handoff**: To test phase (operational testing)

#### Supplier Quality Manager
- **Allocation**: 30% (SBOM maintenance, CVE monitoring)
- **Entry**: Implementation gate
- **Primary Activities**:
  - SBOM updates (as dependencies added)
  - Software Composition Analysis (SCA) execution (weekly)
  - CVE alerts monitoring & evaluation
  - Dependency updates & patching (if needed)
  - License compliance verification
  - Vendor update tracking
- **Exit Criteria**: SBOM complete, CVE clean (or accepted)
- **Handoff**: To test phase (ongoing monitoring)

---

## Phase 4: Test & Verification (Weeks 9-10)

### Phase Gate Entry Criteria
- ✅ Code ≥95% complete, Code Review Board approved
- ✅ Unit tests ≥95% coverage
- ✅ MISRA ≥95% compliant
- ✅ Security code review complete
- ✅ Safety-critical code inspection complete
- ✅ SBOM complete & CVE clean
- ✅ Test environment operational

### Phase Gate Exit Criteria (Phase 4 → Phase 5)
- ✅ Code coverage ≥95% (statement, branch, MC/DC for safety)
- ✅ Zero critical/high defects
- ✅ Security testing complete (functional, attack, penetration, compliance)
- ✅ Safety verification (≥95% coverage of safety-critical)
- ✅ Compliance testing complete
- ✅ Performance baselines met
- ✅ Test & Verification Board (TVB) approval
- ✅ Sign-off: Quality Manager, Chief Engineer, Chief Safety Officer

---

## Test & Verification Phase: Agent Participation

### CORE AGENTS

#### Chief Engineer
- **Allocation**: 10% (escalations, risk acceptance)
- **Entry**: Test gate
- **Primary Activities**:
  - Escalation resolution (test conflicts, unresolved defects)
  - Risk acceptance (known issues, workarounds)
  - Gate readiness assessment
  - Test & Verification Board (TVB) attendance
- **Exit Criteria**: Test gate approved, verification closure
- **Handoff**: To deployment phase (release decision)

#### Program Manager
- **Allocation**: 15% (schedule, resources, risk)
- **Entry**: Test gate
- **Primary Activities**:
  - Schedule test sprints (unit, integration, system, regression)
  - Resource allocation (QA testers, test automation)
  - Defect tracking & trend analysis
  - Risk mitigation (unresolved defects, schedule impact)
  - Change control (any late requirement changes)
- **Exit Criteria**: Test gate approved, defects closed
- **Handoff**: To deployment phase (deployment schedule)

#### Requirements Manager
- **Allocation**: 15% (RTM validation)
- **Entry**: Test gate
- **Primary Activities**:
  - RTM validation (all requirements tested)
  - Test coverage verification (every requirement has test cases)
  - Orphan requirement detection (requirements without tests)
  - Requirements-to-test traceability closure
  - Participate in TVB (requirements validation)
- **Exit Criteria**: RTM validated, no orphans
- **Handoff**: To deployment phase (post-deployment requirements tracking)

#### System Architect
- **Allocation**: 5% (test oversight)
- **Entry**: Reduced allocation
- **Primary Activities**:
  - Architecture validation (design meets performance targets)
  - Integration testing oversight (components communicate correctly)
  - Escalation resolution (architectural issues in test)
- **Exit Criteria**: Architecture validated through testing
- **Handoff**: To deployment phase (production validation)

#### Chief Security Officer
- **Allocation**: 25% (security testing, threat monitoring)
- **Entry**: Test gate
- **Primary Activities**:
  - Security test execution (functional, attack, penetration)
  - Threat-to-test mapping (all threats tested?)
  - Vulnerability remediation oversight
  - CVSS scoring & risk acceptance (if needed)
  - A&A gate preparation (security readiness)
  - Security test result compilation
- **Exit Criteria**: Security testing complete, A&A readiness ≥90%
- **Handoff**: To deployment phase (A&A completion)

#### Chief Safety Officer
- **Allocation**: 20% (safety verification)
- **Entry**: Test gate
- **Primary Activities**:
  - Safety test execution (≥95% coverage target)
  - MC/DC coverage analysis (safety-critical code)
  - Hazard closure verification (all hazards addressed in test?)
  - Residual risk acceptance finalization (with CE)
  - Safety test result compilation
- **Exit Criteria**: Safety verification complete, residual risk accepted
- **Handoff**: To deployment phase (release approval)

#### Chief Compliance Officer
- **Allocation**: 20% (evidence compilation)
- **Entry**: Test gate
- **Primary Activities**:
  - Evidence collection from test phase (test results, coverage reports, defect logs)
  - Compliance audit trail finalization
  - Data package assembly (DO-178C or DO-256A format)
  - Compliance sign-off verification
  - Participate in TVB (compliance readiness)
- **Exit Criteria**: Evidence package ≥95% complete
- **Handoff**: To deployment phase (certification coordination)

### SPECIALIZED AGENTS

#### Cyber/Security Architect
- **Allocation**: 10% (threat-based test validation)
- **Entry**: Reduced from implementation
- **Primary Activities**:
  - Threat-to-test mapping (every threat has test case?)
  - Security control effectiveness validation (do controls work?)
  - Attack surface testing oversight
- **Exit Criteria**: Security threat validation complete
- **Handoff**: To deployment phase (operational security monitoring)

#### Code Review Board
- **Allocation**: 30% (test code review, defect assessment)
- **Entry**: Reduced from implementation
- **Primary Activities**:
  - Test code review (test quality)
  - Defect review & triage (severity, priority)
  - Defect resolution verification (fixes meet requirements)
  - Code change review (if emergency defect fixes in test)
  - Coverage analysis oversight
- **Exit Criteria**: Test code approved, defects resolved
- **Handoff**: To deployment phase (release code review)

#### Quality/QA Manager
- **Allocation**: 100% (full-time test execution)
- **Entry**: Test gate
- **Primary Activities**:
  - Unit test execution (developers run, QA verifies coverage)
  - Integration test execution (components integrated)
  - System test execution (end-to-end testing)
  - Regression test execution (catch regressions)
  - Defect triage & tracking
  - Coverage analysis & reporting (statement, branch, MC/DC)
  - Test & Verification Board (TVB) leadership
  - Verification closure criteria met
- **Exit Criteria**: ≥95% coverage, zero critical defects, test gate approved
- **Handoff**: To deployment phase (post-deployment monitoring)

#### Integration & Test Manager
- **Allocation**: 40% (test environment operation)
- **Entry**: Test gate
- **Primary Activities**:
  - Test environment maintenance (up, stable, responsive)
  - Test data management (correct, available, refreshed)
  - CI/CD pipeline operation (nightly builds, test runs)
  - Test environment troubleshooting
  - Build artifact management
- **Exit Criteria**: Test environment stable, data ready
- **Handoff**: To deployment phase (production environment)

#### Operations Lead
- **Allocation**: 10% (operational testing)
- **Entry**: Test gate
- **Primary Activities**:
  - Operational procedures testing (run through deployment procedures dry-run)
  - Monitoring effectiveness testing (alerts fire correctly?)
  - Incident response procedure testing (war room drill)
  - Rollback procedure testing (tested in safe environment)
  - Operational documentation validation
- **Exit Criteria**: Operational procedures tested & ready
- **Handoff**: To deployment phase (execute procedures)

#### Supplier Quality Manager
- **Allocation**: 15% (dependency validation)
- **Entry**: Reduced allocation
- **Primary Activities**:
  - CVE alert monitoring (ongoing)
  - Dependency testing (dependencies work as expected)
  - Supply chain incident response (if vulnerability found)
  - Final SBOM validation
- **Exit Criteria**: SBOM final, no critical CVEs outstanding
- **Handoff**: To deployment/sustainment phase (ongoing CVE monitoring)

---

## Phase 5: Deployment (Week 11)

### Phase Gate Entry Criteria
- ✅ Test gate passed, ≥95% coverage, zero critical defects
- ✅ Security A&A gate readiness ≥90%
- ✅ Safety residual risk accepted
- ✅ Compliance evidence package ≥95% complete
- ✅ Operational procedures tested
- ✅ Deployment team briefed

### Phase Gate Exit Criteria (Phase 5 → Phase 6)
- ✅ Deployment executed successfully
- ✅ System operational in production
- ✅ Monitoring active & alerting functional
- ✅ Incident response procedure operational
- ✅ A&A gate completed (if required)
- ✅ Zero deployment blockers
- ✅ Sign-off: Operations Lead, Chief Engineer, Chief Compliance Officer

---

## Deployment Phase: Agent Participation

### CORE AGENTS

#### Chief Engineer
- **Allocation**: 10% (go/no-go decision)
- **Entry**: Deployment gate
- **Primary Activities**:
  - Deployment readiness assessment
  - Go/no-go decision authority
  - Deployment Readiness Review (DRR) attendance
  - Emergency escalation authority (if issues during deployment)
- **Exit Criteria**: Deployment approved & executed
- **Handoff**: To sustainment phase (oversight continues)

#### Program Manager
- **Allocation**: 15% (schedule, risk, stakeholder communication)
- **Entry**: Deployment gate
- **Primary Activities**:
  - Deployment schedule execution (phase gates, milestones)
  - Resource coordination (dev team, QA, ops team)
  - Stakeholder communication (status, issues)
  - Risk mitigation (if deployment risks emerge)
  - Change control (emergency changes)
- **Exit Criteria**: Deployment complete, transition to sustainment
- **Handoff**: To sustainment phase (ongoing program management)

#### Requirements Manager
- **Allocation**: 5% (post-deployment requirements)
- **Entry**: Reduced allocation
- **Primary Activities**:
  - Requirements validation in production (features work as specified)
  - Post-deployment requirement change requests (if any)
- **Exit Criteria**: Requirements validated in production
- **Handoff**: To sustainment phase (requirement tracking for updates)

#### System Architect
- **Allocation**: 5% (production validation)
- **Entry**: Reduced allocation
- **Primary Activities**:
  - Architecture validation in production (performance, scaling, resilience)
  - Production incident assessment (architectural issues?)
- **Exit Criteria**: Architecture validated in production
- **Handoff**: To sustainment phase (ongoing validation)

#### Chief Security Officer
- **Allocation**: 20% (A&A completion, threat monitoring)
- **Entry**: Deployment gate
- **Primary Activities**:
  - Authorization & Accreditation (A&A) gate completion (if required)
  - Security posture validation (in production, monitoring active)
  - Threat intelligence integration (operational threats)
  - Incident response activation (if needed)
  - Security monitoring verification
- **Exit Criteria**: A&A completed (or not required), security monitoring operational
- **Handoff**: To sustainment phase (ongoing threat monitoring)

#### Chief Safety Officer
- **Allocation**: 5% (post-deployment safety monitoring)
- **Entry**: Reduced allocation
- **Primary Activities**:
  - Safety monitoring activation (post-deployment safety checks)
  - Post-deployment safety incident response (if any)
- **Exit Criteria**: Safety monitoring operational
- **Handoff**: To sustainment phase (ongoing safety monitoring)

#### Chief Compliance Officer
- **Allocation**: 15% (certification finalization)
- **Entry**: Deployment gate
- **Primary Activities**:
  - Certification body notification (if required)
  - Evidence package finalization & submission
  - Compliance audit trail closure
  - Post-deployment compliance reporting
- **Exit Criteria**: Certification completed (or not required)
- **Handoff**: To sustainment phase (ongoing compliance reporting)

### SPECIALIZED AGENTS

#### Cyber/Security Architect
- **Allocation**: 0% (not active in deployment)
- **Entry**: Sustainment phase only
- **Note**: Supports Operations Lead & CSO for security architecture questions

#### Code Review Board
- **Allocation**: 0% (code review phase ended)
- **Entry**: Reduced to emergency mode (critical hotfix code review)
- **Note**: Supports emergency patching if needed

#### Quality/QA Manager
- **Allocation**: 10% (post-deployment validation)
- **Entry**: Reduced from test phase
- **Primary Activities**:
  - Deployment smoke testing (basic functionality verification)
  - Post-deployment defect monitoring
  - Quality metrics baseline in production
- **Exit Criteria**: Deployment validated, metrics baselined
- **Handoff**: To sustainment phase (ongoing quality monitoring)

#### Integration & Test Manager
- **Allocation**: 5% (production build support)
- **Entry**: Reduced allocation
- **Primary Activities**:
  - Production build artifact verification (correct version deployed?)
  - CI/CD pipeline updates for production (if needed)
- **Exit Criteria**: Production environment verified
- **Handoff**: To sustainment phase (CI/CD for updates/patches)

#### Operations Lead
- **Allocation**: 100% (deployment execution)
- **Entry**: Deployment gate (week 11)
- **Primary Activities**:
  - Deployment procedure execution (step-by-step runbook)
  - Production monitoring activation
  - Incident response activation (if needed)
  - Rollback execution (if deployment fails)
  - Post-deployment operational validation
  - Operational documentation finalization
- **Exit Criteria**: Deployment complete, system operational, monitoring active
- **Handoff**: To sustainment phase (ongoing operations)

#### Supplier Quality Manager
- **Allocation**: 10% (supply chain verification)
- **Entry**: Deployment gate
- **Primary Activities**:
  - Deployed artifact verification (SBOM matches deployed code)
  - Supply chain incident monitoring (any vendor issues during deployment)
  - CVE monitoring (any critical CVEs emerge)
- **Exit Criteria**: Deployed system verified against SBOM
- **Handoff**: To sustainment phase (ongoing CVE monitoring)

---

## Phase 6: Sustainment (Weeks 12+, indefinite)

### Entry Criteria
- ✅ Deployment successful
- ✅ System operational in production
- ✅ Monitoring active
- ✅ Incident response team standby
- ✅ Sustainment support model established

### Ongoing Activities (No exit criteria until end-of-life)

### Sustainment Phase: Agent Participation

#### Chief Engineer
- **Allocation**: 5% (escalations, architecture decisions for updates)
- **Activities**: Escalation authority (critical production issues), architecture decisions for maintenance
- **Ongoing**: Until end-of-life

#### Program Manager
- **Allocation**: 10% (sustainment planning, updates, patches)
- **Activities**: Schedule updates/patches, resource allocation, risk tracking
- **Ongoing**: Until end-of-life

#### Requirements Manager
- **Allocation**: 5% (requirements for updates/patches)
- **Activities**: Process change requests (updates, patches, enhancements)
- **Ongoing**: Until end-of-life

#### System Architect
- **Allocation**: 5% (architecture for updates)
- **Activities**: Architecture decisions for maintenance, refactoring
- **Ongoing**: Until end-of-life

#### Chief Security Officer
- **Allocation**: 20% (threat monitoring, A&A updates, incident response)
- **Activities**: Threat intelligence monitoring, security incident response, A&A re-certification (if required), security patches
- **Ongoing**: Until end-of-life

#### Chief Safety Officer
- **Allocation**: 5% (safety monitoring, incident response)
- **Activities**: Post-deployment safety monitoring, safety incident response
- **Ongoing**: Until end-of-life

#### Chief Compliance Officer
- **Allocation**: 10% (compliance monitoring, audit, re-certification)
- **Activities**: Ongoing compliance monitoring, internal audits, re-certification (if required)
- **Ongoing**: Until end-of-life

#### Cyber/Security Architect
- **Allocation**: 5% (security architecture updates, threat mitigation)
- **Activities**: Security architecture recommendations for patches/updates
- **Ongoing**: Until end-of-life

#### Code Review Board
- **Allocation**: 30% (hotfix code review, emergency patches)
- **Activities**: Code review for emergency patches, security hotfixes
- **Ongoing**: Until end-of-life

#### Quality/QA Manager
- **Allocation**: 10% (quality monitoring, patch testing)
- **Activities**: Quality metrics monitoring, patch testing before deployment
- **Ongoing**: Until end-of-life

#### Integration & Test Manager
- **Allocation**: 15% (CI/CD for patches, test environment)
- **Activities**: Build patches, test infrastructure for updates, emergency builds
- **Ongoing**: Until end-of-life

#### Operations Lead
- **Allocation**: 40% (ongoing operations, incident response)
- **Activities**: 24/7 operations, monitoring, incident response, deployment of patches
- **Ongoing**: Until end-of-life

#### Supplier Quality Manager
- **Allocation**: 30% (CVE monitoring, supply chain risk management)
- **Activities**: CVE alert monitoring (daily), dependency updates, supply chain incident response
- **Ongoing**: Until end-of-life

---

## Summary: Total Agent Allocations by Phase

| Agent | Req | Arch | Impl | Test | Deploy | Sustain |
|-------|-----|------|------|------|--------|---------|
| Chief Engineer | 25% | 40% | 15% | 10% | 10% | 5% |
| Program Manager | 50% | 30% | 25% | 15% | 15% | 10% |
| Requirements Mgr | 100% | 20% | 10% | 15% | 5% | 5% |
| System Architect | 10% | 100% | 20% | 5% | 5% | 5% |
| Chief Security Officer | 30% | 25% | 20% | 25% | 20% | 20% |
| Chief Safety Officer | 20% | 30% | 25% | 20% | 5% | 5% |
| Chief Compliance Officer | 20% | 15% | 10% | 20% | 15% | 10% |
| Cyber/Security Architect | 0% | 40% | 15% | 10% | 0% | 5% |
| Code Review Board | 0% | 15% | 100% | 30% | 0% | 30% |
| Quality/QA Manager | 10% | 30% | 20% | 100% | 10% | 10% |
| Integration & Test Mgr | 5% | 40% | 50% | 40% | 5% | 15% |
| Operations Lead | 5% | 20% | 5% | 10% | 100% | 40% |
| Supplier Quality Mgr | 10% | 25% | 30% | 15% | 10% | 30% |

**Key Insight**: Each phase has 2-3 agents at 100% allocation (primary focus), 3-5 agents at 20-50% (significant involvement), and others at 5-10% (oversight/escalations).

---

## Escalation Touchpoints Across Phases

### Requirements → Architecture
- **RTM Validation**: Requirements Manager validates design traces to requirements
- **Feasibility Assessment**: System Architect provides feasibility confidence to CE
- **Security Requirements**: Chief Security Officer validates threat-based requirements in design
- **Safety Requirements**: Chief Safety Officer validates hazard-based requirements in design

### Architecture → Implementation
- **Design Complexity**: System Architect gates CC ≤ 10, escalates to CE if exceeded
- **Secure Patterns**: Cyber Architect validates secure design patterns in code
- **Safety-Critical Design**: Chief Safety Officer gates safety-critical component implementation

### Implementation → Test
- **Code Quality**: Code Review Board gates merge (MISRA ≥95%, CC ≤ 10)
- **Security Code Review**: Chief Security Officer gates security code merge
- **Safety Code Inspection**: Chief Safety Officer gates safety-critical code merge
- **SBOM Completeness**: Supplier Quality Manager gates SBOM updates with CVE checks

### Test → Deployment
- **Verification Closure**: Quality Manager gates test phase (≥95% coverage, zero critical defects)
- **A&A Gate**: Chief Security Officer gates security readiness
- **Safety Verification**: Chief Safety Officer gates safety test closure with residual risk acceptance
- **Compliance Readiness**: Chief Compliance Officer gates evidence package completeness

### Deployment → Sustainment
- **Operational Readiness**: Operations Lead gates deployment execution
- **Security Monitoring**: Chief Security Officer gates threat monitoring operational
- **Compliance Certification**: Chief Compliance Officer gates certification completion
- **Post-Deployment Validation**: Quality Manager gates production quality metrics baseline

---

## Key Principles

1. **Each phase has clear entry & exit gates** (no ambiguity on when phase starts/ends)
2. **Each agent has defined allocation per phase** (no confusion on when they're active)
3. **Escalation triggers are explicit** (when to go up the chain is documented)
4. **Authority is clear in each domain** (who decides what in each phase)
5. **No agent overdoes or underdoes** (allocations match phase needs)
6. **Handoff between phases is explicit** (clear transition from one phase to next)


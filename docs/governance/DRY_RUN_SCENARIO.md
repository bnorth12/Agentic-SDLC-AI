# Dry-Run Scenario: Sample Project Walk-Through

**Document ID**: SCENARIO-DRY-RUN-001  
**Date**: May 12, 2026  
**Purpose**: Validate Agentic-SDLC-AI governance framework against realistic project scenario  
**Scope**: Requirements → Architecture → Implementation → Test → Deployment (all 5 gates)

---

## Project Overview: "SecurePayments" E-Commerce Platform

**Project Name**: SecurePayments v1.0  
**Description**: Web-based payment processing platform for small businesses  
**Schedule**: 6 months (May - October 2026)  
**Budget**: $2M  
**Team Size**: 15 people (1 PM, 1 CE, 3 architects, 4 developers, 2 QA, 2 ops, 2 admin)  
**Compliance**: PCI-DSS, SOC 2, GDPR (if EU traffic)

---

## Timeline Overview

```
May          Jun          Jul          Aug          Sep          Oct
RRB ─────── DRB ────── CIB ────── TVB ────── DRR ──── Go Live
 ↑            ↑           ↑          ↑         ↑         ↑
Req Phase   Arch Phase  Impl Phase  Test Ph  Deploy    Production
```

---

## PHASE 1: REQUIREMENTS (4 weeks, May 1-31)

### **Phase Start (May 1)**

**Entering Conditions** (checked):
- ✓ Project charter signed
- ✓ Stakeholder needs documented (via customer interviews)
- ✓ Compliance standards identified (PCI-DSS, SOC 2)
- ✓ Program risk tolerance defined: "MEDIUM risk acceptable; CRITICAL risks must be mitigated"
- ✓ Security threat categories identified (payment fraud, data breach, API compromise)
- ✓ Safety hazard categories not applicable (not safety-critical system)

### **Phase Activities (Weeks 1-4)**

**Week 1-2: Requirements Elicitation**
- RM conducts customer interviews → 50+ requirements gathered
- RM organizes into L1 categories (functional, non-functional, security, compliance)
- CSO participates: identifies threat-driven requirements (payment security, encryption)
- CCO participates: identifies compliance requirements (audit logging, data retention)

**Requirements Drafted**: 
```
L1 Functional Requirements (35):
- PAY-001: System shall process credit card payments
- PAY-002: System shall validate card expiration
- [etc.]

L1 Security Requirements (10):
- SEC-REQ-001: All payment data encrypted in transit (TLS 1.2+)
- SEC-REQ-002: All payment data encrypted at rest (AES-256)
- SEC-REQ-003: API authentication required (OAuth 2.0)
- [etc.]

L1 Compliance Requirements (8):
- COMP-REQ-001: Audit logging of all payment transactions
- COMP-REQ-002: Data retention 7 years (PCI-DSS)
- [etc.]
```

**Week 2: Threat Analysis (CSO)**
- CSO conducts L1 threat analysis:
  - Threat framework: USAF System Security Engineering (ARP 4761 adapted)
  - Threat categories: Payment Fraud, Data Breach, API Compromise, Supply Chain, Deployment
  
**Identified Threats** (20 total, organized):
```
Data Breach Threats:
- THR-001: Attacker intercepts payment data in transit
  - Attack Vector: MITM attack on API
  - Consequence: Critical (PCI-DSS violation, liability)
  - Probability: Medium (encrypted TLS vulnerable only if misconfigured)
  - Risk: CRITICAL → MUST MITIGATE
  - Mitigation: TLS 1.3, certificate pinning, API key rotation

- THR-002: Attacker gains access to database
  - Attack Vector: SQL injection, weak credentials
  - Consequence: Critical (all customer data exposed)
  - Probability: Medium (encrypted DB mitigates)
  - Risk: CRITICAL → MUST MITIGATE
  - Mitigation: Parameterized queries, RBAC, encryption

- THR-003: Rogue developer inserts payment skimming code
  - Attack Vector: Compromised developer, supply chain
  - Consequence: Critical (payment theft)
  - Probability: Low (code review, MFA required)
  - Risk: MAJOR → MITIGATE
  - Mitigation: Secure code review, dependency scanning

Payment Fraud Threats:
- THR-004: Attacker replays captured payment request
  - Attack Vector: Replay attack on API
  - Consequence: Major (duplicate charges)
  - Probability: Low (nonce + timestamp prevents)
  - Risk: MAJOR → MITIGATE
  - Mitigation: Nonce validation, request signing

[... 16 more threats ...]

Risk Summary:
- Total threats: 20
- Critical risk: 4 (require mitigation)
- Major risk: 8 (require mitigation)
- Minor risk: 8 (residual accepted)
```

**Week 3: Safety Analysis (CSafO)**
- CSafO: "System not safety-critical (financial impact only, not life safety)"
- No hazard analysis required for this project
- CSafO notes: System reliability important (availability = safety-like concern)

**Week 3-4: Requirements Completion & RTM**
- RM completes 50 L1 requirements
- RM creates RTM: Stakeholder Needs ← Requirements ← Threats/Hazards
- Traceability verified:
  - THR-001 (MITM attack) ← SEC-REQ-001 (TLS encryption)
  - THR-002 (DB breach) ← SEC-REQ-002 (at-rest encryption)
  - [... 18 more mappings ...]

**Week 4: Compliance Planning**
- CCO identifies compliance requirements:
  - PCI-DSS: Payment Card Industry Data Security Standard
  - SOC 2: Service Organization Control
  - GDPR: If processing EU customer data
  
- CCO creates evidence plan:
  - Threat analysis documentation (threat models, risk scores)
  - Security requirements specification
  - Design decisions for threat mitigation
  - Code review evidence (per PCI-DSS 6.5)
  - Test results for mitigations
  - Incident response procedure

### **RRB Gate Meeting (May 31, 2 hours)**

**Attendees**: RM (chair), CSO, CSafO, CCO, PM, CE

**Pre-Gate Assessment** (May 28-30):
- RM: "Requirements completeness = 95% (50 req collected, all in RTM)"
- CSO: "Threat analysis complete: 20 threats identified, 12 exceed threshold (4 Critical, 8 Major)"
- CCO: "Compliance strategy ready; evidence plan identifies 15 artifact types to collect"

**Gate Meeting Agenda**:
1. RM: "Requirements: 50 L1 requirements, ≥80% completeness achieved ✓"
2. CSO: "Threats: 20 identified, 12 require mitigation → mapped to 8 security requirements ✓"
3. CSafO: "System not safety-critical; no hazards identified ✓"
4. CCO: "Compliance: PCI-DSS + SOC 2 compliance plan ready ✓"
5. Vote: RM + CSO + CSafO + CCO: **✓ PASS** (unanimous)

**Gate Decision**: **PASS** (May 31)
- ✓ All requirements captured & testable
- ✓ Threat analysis comprehensive
- ✓ Security requirements allocated per threats
- ✓ Compliance strategy documented
- No residual risks exceeding program threshold

**Gate Outputs Archived**:
- Gate Decision Record (signed)
- Requirements Completeness Report (95%)
- Threat Analysis Summary (20 threats, 12 mitigations planned)
- RTM (50 requirements, 100% traced)
- Compliance Evidence Plan (15 artifact types)

---

## PHASE 2: ARCHITECTURE (3 weeks, June 1-21)

### **Phase Start (June 1)**

**Entering Conditions**:
- ✓ RRB gate PASSED
- ✓ Requirements baseline stable
- ✓ Threats understood

### **Phase Activities**

**Week 1: L2 Decomposition**

**Architect performs L2 system decomposition**:
```
Level 1: Payment Processing System
  ├─ Level 2 Component A: Payment API (REST API for payment requests)
  ├─ Level 2 Component B: Payment Processor (Business logic)
  ├─ Level 2 Component C: Database (PostgreSQL, PCI-DSS encrypted)
  ├─ Level 2 Component D: Payment Gateway Integration (STRIPE / Authorize.net)
  ├─ Level 2 Component E: Audit Logging (Compliance & threat monitoring)
  └─ Level 2 Component F: Admin Console
```

**CSO performs L2 threat decomposition**:
```
THR-001 (MITM attack on API) decomposes to:
  - L2a: API server misconfiguration (TLS cipher suites weak)
  - L2b: Certificate validation disabled in client
  - L2c: Certificate pinning not implemented

THR-002 (DB breach) decomposes to:
  - L2a: SQL injection in Payment Processor component
  - L2b: Weak database credentials
  - L2c: Database backup not encrypted

[... similar decomposition for remaining 12 critical/major threats ...]
```

**Cyber Architect proposes security architecture**:
```
Threat Mitigations (design):
- API Layer: TLS 1.3 mandatory + certificate pinning
- Database Layer: AES-256 encryption at rest + encrypted backups
- Authentication: OAuth 2.0 with MFA + API key rotation
- Payment Gateway: PCI-DSS compliance (use managed service, not home-grown)
- Audit Logging: Immutable audit logs (append-only DB)
- Monitoring: Real-time threat detection (failed login attempts, unusual volumes)
```

**Week 2: Architecture Review & Feasibility Assessment**

**CE reviews architecture**:
```
Feasibility Scorecard by Component:
- Payment API: Feasibility 85% (proven technologies: Spring Boot, REST, OAuth)
- Payment Processor: Feasibility 80% (business logic complex but proven patterns)
- Database: Feasibility 95% (PostgreSQL well-established)
- STRIPE Integration: Feasibility 100% (managed service, low risk)
- Audit Logging: Feasibility 75% (immutable logging complex, but proven solutions)
- Admin Console: Feasibility 85% (standard CRUD interface)

Overall Feasibility: 87% (>70% ✓)

Risk Mitigations for <90% components:
- Audit Logging: Prototype immutable logging pattern (1 week) before Implementation phase
- Business Logic: Design review + domain expert consultation
```

**Week 2-3: Design Decisions & Trade-Offs**

**PM + Arch trade-off: Cost vs Security**
- Arch: "Implement payment gateway directly = lower cost ($20K) but high security risk"
- PM: "Budget tight; can we reduce costs?"
- CSO: "Using managed payment gateway (STRIPE) = $50K annually but removes PCI scope"
- CE decision: "Use STRIPE. $50K annually prevents $500K+ liability risk. Cost justified."
- Decision logged: DEC-20260609-001 (Cost-Security trade-off)

**Week 3: Architecture Diagrams & ADRs**

**Architecture Decision Records (ADRs) created**:
```
ADR-001: Use STRIPE for payment processing (vs home-grown)
  - Context: Build vs buy decision
  - Decision: Use STRIPE (managed PCI compliance)
  - Consequences: $50K annual cost, reduced scope, vendor dependency
  - Rationale: Reduces security risk, PCI compliance easier

ADR-002: TLS 1.3 + Certificate Pinning (vs TLS 1.2)
  - Context: MITM attack (THR-001) threat
  - Decision: TLS 1.3 required, certificate pinning implemented
  - Consequences: More complex implementation, client certificate distribution
  - Rationale: Mitigates MITM threat to residual

ADR-003: AES-256 encryption at rest (for database)
  - Context: DB breach (THR-002) threat
  - Decision: AES-256 encryption mandatory + encrypted backups
  - Consequences: Performance impact ~5%, key management complexity
  - Rationale: Mitigates data breach threat to residual

[... 5 more ADRs ...]
```

### **DRB Gate Meeting (June 21, 2.5 hours)**

**Pre-Gate Assessment** (June 18-20):
- Arch: "Architecture L1→L2 decomposed, 6 components defined, feasibility 87%"
- CSO: "L2 threats decomposed, 12 mitigations mapped to architecture components ✓"
- Cyber Arch: "Security architecture designed: TLS 1.3, encryption, STRIPE integration ✓"

**Gate Meeting**:
1. Arch: "System decomposed into 6 components; interfaces defined ✓"
2. Arch: "Feasibility 87% (>70%) ✓"
3. Cyber Arch: "Security architecture: TLS 1.3, encryption, STRIPE ✓"
4. CSO: "L2 threats decomposed; 12 mitigations addressed in design ✓"
5. CE: "Architecture feasible; components proven ✓"
6. Vote: **✓ PASS** (unanimous)

**Gate Decision**: **PASS** (June 21)
- ✓ System decomposed L1→L2
- ✓ Feasibility ≥70%
- ✓ Security architecture addresses high-risk threats
- ✓ Design decisions documented (7 ADRs)

---

## PHASE 3: IMPLEMENTATION (4 weeks, June 22 - July 19)

### **Phase Start (June 22)**

**Entering Conditions**:
- ✓ DRB gate PASSED
- ✓ Architecture documented
- ✓ Security design ready

### **Phase Activities**

**Week 1-2: Code Development**

**Dev Team implements per architecture**:
```
Components developed:
- Payment API: Endpoints for payment requests (Spring Boot)
- Payment Processor: Business logic for payment validation
- Database: PostgreSQL with AES-256 encryption
- STRIPE Integration: Payment gateway integration
- Audit Logging: Append-only audit log
- Admin Console: User management interface
```

**Security requirements implemented**:
- ✓ TLS 1.3 on all API endpoints
- ✓ OAuth 2.0 authentication
- ✓ AES-256 encryption (at-rest)
- ✓ Parameterized queries (SQL injection prevention)
- ✓ Input validation on all API inputs
- ✓ Audit logging on payment transactions

**Code Quality Checks**:
- MISRA scan: 98% compliant
- Cyclomatic Complexity: 87% of functions ≤10
- Unit test coverage: 92%

**Week 2-3: Security Code Review (CRB + CSO)**

**Code Review for Security Patterns**:
```
Reviewer 1 (Senior Dev): TLS/OAuth implementation ✓
Reviewer 2 (Security Specialist): Crypto implementation ✓
Findings:
- API input validation missing bounds check on amount field → Fixed
- Audit log timestamps not synchronized (clock skew risk) → Fixed
- Database connection pool credentials in config file → Moved to secrets vault

Result: 3 findings, all fixed before gate
```

**SAST Scanning** (CSO):
```
SAST Tool: SonarQube / Checkmarx
Findings:
- 0 Critical vulnerabilities
- 2 High-severity (both fixed):
  - SQL injection risk in search endpoint → Parameterized query
  - Hardcoded API key in config → Moved to environment variable
- 8 Medium-severity issues → Tracked in backlog

Result: No blockers; code ready for test phase
```

**Week 3-4: Safety-Like & Reliability Inspections**

**CSafO notes**: System not safety-critical, but payment processing requires high reliability.

**Reliability Code Inspection** (by QA + CSafO):
```
Inspectors: QA Expert + CSafO (standing in for safety role)
Focus: Failure handling, recovery paths
- Payment timeout handling ✓
- Payment gateway failure handling ✓
- Database connection retry logic ✓
- Audit log persistence guarantee ✓

Result: All failure paths handled
```

### **CIB Gate Meeting (July 19, 2 hours)**

**Pre-Gate Assessment** (July 16-18):
- CRB: "Code quality: MISRA 98%, CC ≤10 for 87% of functions ✓"
- CSO: "Security review: 3 findings fixed; SAST: 0 Critical ✓"
- QA: "Unit tests: 92% coverage ✓"

**Gate Meeting**:
1. CRB: "MISRA 98%, CC ≤10 achieved ✓"
2. CSO: "Security code review complete; SAST 0 Critical, 2 High fixed ✓"
3. QA: "Unit test coverage 92% ✓"
4. All reviewers: **✓ PASS** (unanimous)

**Gate Decision**: **PASS** (July 19)
- ✓ Code quality meets standards
- ✓ Security mitigations implemented
- ✓ Vulnerabilities remediated
- ✓ Unit tests adequate coverage

---

## PHASE 4: TEST & VERIFICATION (2 weeks, July 20 - Aug 2)

### **Test Activities**

**Week 1: Integration & System Testing (I&T)**
- API integration tests: ✓ 100% pass
- End-to-end payment flows: ✓ Critical flows tested
- Payment gateway integration: ✓ Test merchant account validated

**Week 1: Security Testing (DAST by CSO)**
- DAST tool (OWASP ZAP): Vulnerability scanning
- Results: 0 Critical, 0 High findings
- Penetration testing scenario: MITM attack mitigation verified with TLS 1.3 + cert pinning

**Week 2: Load & Stress Testing**
- Baseline: 1000 TPS (transactions per second)
- Target: 500 TPS (expected peak, Black Friday)
- Result: ✓ Achieves 600 TPS; 20% headroom

**Test Coverage**: 96% code coverage (exceeds 95% target)

**Defects Found & Closed**:
- Critical: 0
- High: 0
- Medium: 3 (all fixed)
- Low: 8 (prioritized by PM)

### **TVB Gate Meeting** (Implicit, part of DRR)

Test results documented:
- ✓ Coverage 96%
- ✓ Critical defects: 0
- ✓ All security tests passed

---

## PHASE 5: DEPLOYMENT (1 week, Aug 3-9)

### **Residual Risk Assessment (CSO)**

**CSO Assessment** (Aug 1):
```
Residual Threats (below mitigation threshold, accepted):
- THR-006: Attacker uses phishing to compromise user account
  - Why accepted: Phishing outside system scope; user responsibility
  - Mitigation in ops: Email security training, MFA enforcement
  - Monitoring: Track failed login attempts; alert on anomalies

- THR-007: 0-day vulnerability in STRIPE API
  - Why accepted: Third-party risk; outside our control
  - Mitigation in ops: Automated security updates, incident response plan
  - Monitoring: Monitor STRIPE security bulletins

- THR-012: Insider threat (rogue operations staff)
  - Why accepted: Operational controls (background check, MFA, audit logs)
  - Mitigation in ops: Audit log monitoring, principle of least privilege
  - Monitoring: Review access logs monthly

Residual Risk Assessment: MEDIUM (acceptable per program threshold)
CSO Signature: ✓ [Jane Smith, CSO]
```

### **DRR Gate Meeting (Aug 9, 2 hours)**

**Pre-Gate Assessment** (Aug 7-8):
- Test coverage: 96% ✓
- Defects: 0 Critical ✓
- Security testing: DAST clean ✓
- Residual risks: Documented & accepted ✓
- Operational procedures: Ready ✓
- Compliance evidence: 100% collected ✓

**Gate Meeting**:
1. PM: "Test complete; 96% coverage, 0 critical defects ✓"
2. CSO: "Residual threats assessed; monitoring plan defined ✓"
3. QA: "Load testing 600 TPS; exceeds 500 TPS target ✓"
4. Ops Lead: "Operational procedures ready; team trained ✓"
5. CCO: "All compliance evidence collected (15 artifacts) ✓"
6. CE: "All criteria met; deployment authorized ✓"

**Vote**: **✓ PASS** (unanimous)

**Gate Decision**: **PASS - DEPLOYMENT AUTHORIZED** (Aug 9)

**Deployment Window**: Aug 10, 8 PM - Aug 11, 2 AM (6-hour maintenance window)

---

## Post-Deployment (Aug 11+)

### **Operational Monitoring** (CSO + Ops Lead)

**Week 1 Post-Go**:
- Payment throughput: 150 TPS (within capacity) ✓
- Error rate: 0.1% (acceptable) ✓
- Threat monitoring:
  - Failed login attempts: Normal baseline ✓
  - STRIPE API status: OK ✓
  - Audit logs: Clean ✓

**Incident Response**: No incidents in first week

---

## Lessons Learned (DRY-RUN VALIDATION)

### **What Worked Well**

1. ✓ **Threat-Driven Architecture**: CSO's early involvement (Phase 1) shaped security design → fewer post-implementation security fixes
2. ✓ **Clear Gate Criteria**: All gates PASSED on first submission → smooth phase transitions
3. ✓ **Residual Risk Acceptance**: CSO formally documented accepted risks → no surprises post-deployment
4. ✓ **Compliance Evidence Trail**: CCO tracking artifacts throughout → easy to pass audit

### **Governance Framework Validation**

| Governance Element | Effectiveness | Evidence |
|---|---|---|
| **Gate Criteria** | ✓ Excellent | All 4 gates PASS on first submission |
| **Authority Hierarchy** | ✓ Excellent | CE decisions respected; no conflicts |
| **Threat-Hazard Analysis** | ✓ Excellent | 20 threats identified upfront; 12 mitigated |
| **Risk Thresholding** | ✓ Good | Clear decision: mitigate vs accept |
| **Compliance Planning** | ✓ Excellent | All 15 evidence artifacts collected |
| **Communication** | ✓ Good | Async decisions efficient; few escalations |

### **Metrics Achieved**

| Metric | Target | Actual | Status |
|---|---|---|---|
| Schedule adherence | Within ±5 days | On schedule (0 days variance) | ✓ PASS |
| Gate pass rate | ≥75% | 100% (4/4 PASS) | ✓ PASS |
| Threat coverage | ≥95% | 100% (all threats identified & addressed) | ✓ PASS |
| Code quality | MISRA ≥95% | 98% | ✓ PASS |
| Test coverage | ≥95% | 96% | ✓ PASS |
| Zero critical defects | 0 | 0 | ✓ PASS |
| Residual risk acceptance | Documented | CSO memo signed | ✓ PASS |

---

## Conclusion: Framework Validation ✓

**DRY-RUN RESULT**: Governance framework validated against realistic project.

**Recommendation**: Framework ready for production use.

**Next Steps**: 
1. Conduct 1-2 more dry-runs with different project types (e.g., safety-critical system)
2. Calibrate metrics based on real project data
3. Deploy framework for Phase 2 projects (multiple teams)


# Agent-to-Standards Mapping for Assured SDLC

**Document ID**: GOV-AGENTS-STANDARDS-001  
**Date**: May 8, 2026  
**Purpose**: Map each of 13 agents to regulatory, policy, and guidance documents  
**Focus**: DO-326A, DO-356A, DO-355A (Airworthiness Security), plus DO-178C, ARP 4754A, MIL-STD-882G, NIST standards

---

## Standards Overview

| Std | Title | Scope | Applicability |
|-----|-------|-------|----------------|
| **DO-326A** | Airworthiness Security & Safety Management | Security management framework, oversight, governance | **All agents** - defines management responsibilities |
| **DO-356A** | Airworthiness Security Processes & Requirements | What to do (processes, requirements, controls) | **Security/Compliance agents** - defines work products |
| **DO-355A** | Airworthiness Security & Safety Assurance | How to verify (assurance, evidence, closure) | **QA/Verification agents** - defines verification |
| **DO-178C** | Software Lifecycle Processes | Software development, verification, deployment | **All software agents** - defines SDLC activities |
| **DO-254** | Hardware Lifecycle Processes | Hardware development, verification, deployment | **Architect agents** - if hardware involved |
| **ARP 4754A** | System Architecture & Safety Assurance | System decomposition, architecture, safety | **Architect, Safety Officer** - design authority |
| **ARP 4761** | System Safety Engineering & Failure Analysis | System hazard analysis, FMEA, FTA | **Safety Officer** - hazard analysis |
| **MIL-STD-882G** | System Safety Engineering | Defense/aerospace safety processes | **Chief Engineer, Safety Officer** - safety authority |
| **NIST SP 800-53** | Security Controls Catalog | Security control requirements & guidance | **Security Officer, Cyber Architect** - control spec |
| **NIST SP 800-30** | Risk Assessment | Risk identification & analysis methods | **Program Manager, Risk board** - risk process |
| **IEEE 830** | Software Requirements Specification | Requirements documentation standards | **Requirements Manager** - requirements format |
| **IEEE 1233** | System & Software Requirements | Requirements management practices | **Requirements Manager, QA** - req practices |
| **IEEE 1016** | Software Design Documentation | Design documentation standards | **System Architect, Cyber Architect** - design docs |
| **CMMI v2.0** | Capability Maturity Model | Process maturity, responsibility clarity | **All agents** - process discipline |
| **EIA 632** | Processes & Requirements for Software Systems | System engineering processes | **All agents** - SDLC process framework |
| **ISO/IEC/IEEE 42010** | Architecture Decision Records | Architecture documentation & traceability | **System Architect, Compliance** - ADR format |

---

## Agent 1: Chief Engineer

**Role**: Apex technical authority, feasibility decisions, escalation resolution

### Standards Basis

**DO-326A**:
- Section 3 (Organization & Responsibility): CE as Chief Executive or designated senior technical authority
- Section 4 (Processes): Overall process authority & oversight
- Section 5 (Activities): Technical decision-making responsibility
- Section 6 (Assurance): Technical assurance authority

**DO-356A**:
- Section 3 (Technical Authority): CE technical decision authority documented
- Section 4 (Requirements): CE approves technical requirements feasibility

**DO-178C**:
- Section 3 (Planning): CE approves overall software plan
- Section 4 (Planning & Processes): CE designates technical processes
- Section 12 (Configuration Management): CE approves configuration strategy

**NASA-STD-7009A**:
- Section 3 (Technical Authority): CE as key technical decision authority
- Section 5 (Technical Reviews): CE chairs critical design reviews

**INCOSE**:
- Chief Engineer role definition (SEMP)
- Authority hierarchy establishment
- Escalation authority

**ARP 4754A**:
- System architecture approval authority
- Technical feasibility assessment
- Design review leadership

### Key Responsibilities per Standard

| Responsibility | Standard Ref | Implementation |
|---|---|---|
| Approve/reject architecture | DO-178C-3, ARP 4754A-5 | CE signs HLD/LLD approval memo |
| Feasibility assessment (≥70%) | NASA-STD-7009A-3, DO-326A-5 | CE documents feasibility review & confidence |
| Risk acceptance (technical) | DO-356A-7, MIL-STD-882G-4 | CE approves safety/security risk acceptance |
| Design review authority | DO-178C-6, NASA-STD-7009A-5 | CE chairs or delegates design reviews |
| Escalation receiver | DO-326A-4 | CE receives all technical escalations |
| Compliance authority | DO-355A-3, EIA 632-6 | CE verifies technical compliance posture |

### Governance Boards Led by CE

- **Technical Authority Board (TAB)**: CE chairs (architecture, technology, escalations)
- **Risk Management Board (RMB)**: CE co-chairs (with PM) - technical risk decisions

---

## Agent 2: Program Manager

**Role**: Project leadership, schedule/scope/cost authority, resource allocation

### Standards Basis

**DO-326A**:
- Section 3 (Organization): PM as Program Lead or project manager
- Section 4 (Processes): Process management & schedule authority
- Section 5 (Activities): Project planning & control activities

**DO-356A**:
- Section 2 (Planning & Organization): PM establishes project planning processes
- Section 4 (Schedule Management): PM schedule & resource authority

**DO-178C**:
- Section 2 (Planning): PM develops software development plan
- Section 12 (Project Management): PM tracks schedule, resources, budget

**NASA-STD-7009A**:
- Section 3 (Program Management): PM manages schedule, resources, stakeholders
- Section 7 (Project Metrics): PM owns program metrics & KPIs

**USAF Acquisition Management**:
- PM as milestone authority
- PM controls resource allocation & budget
- PM manages contractor relationships (if applicable)

**CMMI v2.0**:
- Project Planning & Monitoring practices
- Process & Product Quality Assurance
- Supplier Management

**EIA-632**:
- Program planning processes
- Configuration management authority
- Baseline management

### Key Responsibilities per Standard

| Responsibility | Standard Ref | Implementation |
|---|---|---|
| Develop project plan | DO-178C-2, EIA-632-5 | PM creates SDP, SSMP, schedules |
| Schedule management | DO-356A-4, NASA-7009A-3 | PM tracks milestones, critical path, earned value |
| Resource allocation | DO-326A-3, USAF PCARD | PM allocates staff, budget, tools |
| Baseline management | EIA-632-10, DO-178C-12 | PM establishes & maintains baselines |
| Change control | DO-178C-12, EIA-637 | PM leads Configuration Control Board |
| Risk prioritization | DO-356A-7, MIL-STD-882G-5 | PM co-chairs Risk Management Board |
| Stakeholder coordination | NASA-7009A-3, DO-326A-4 | PM manages communication & reporting |
| Metrics tracking | CMMI-2, NASA-7009A-7 | PM owns program metrics & dashboards |

### Governance Boards Led by PM

- **Configuration Control Board (CCB)**: PM chairs (scope/baseline changes)
- **Risk Management Board (RMB)**: PM co-chairs (with CE) - programmatic risks

---

## Agent 3: Requirements Manager

**Role**: Requirements capture, decomposition, traceability, feasibility assessment

### Standards Basis

**IEEE 830**:
- Software Requirements Specification standards
- Requirements format & documentation
- Traceability requirements

**IEEE 1233**:
- System & Software Requirements Specification
- Requirements management practices
- Traceability matrix (RTM) procedures

**DO-178C**:
- Section 5 (Requirements): Requirements capture & standards
- Section 5 (Traceability): Requirements-to-design-to-code traceability
- Section 8 (Testing): Requirements-to-test case linkage

**NASA-STD-7009B**:
- Requirements Management process
- Requirement capture & decomposition
- RTM development & maintenance

**DO-356A**:
- Section 5 (Security Requirements): Security requirement capture & traceability
- Section 5 (Requirement Decomposition): Breaking down system requirements

**ARP 4754A**:
- System requirement allocation to subsystems
- Requirement interface specification
- Feasibility assessment

**EIA-632**:
- Requirements management processes
- Requirement definition & validation
- Traceability establishment

### Key Responsibilities per Standard

| Responsibility | Standard Ref | Implementation |
|---|---|---|
| Capture L1 requirements | IEEE 830-2, NASA-7009B-4 | RM develops requirements spec |
| Decompose to L2/L3 | IEEE 1233-4, EIA-632-4 | RM creates hierarchical requirements |
| Define acceptance criteria | IEEE 830-3, DO-178C-5 | RM writes SMART acceptance criteria |
| Develop RTM | IEEE 1233-5, DO-178C-5-1 | RM creates & maintains traceability matrix |
| Allocate to architecture | ARP 4754A-5, EIA-632-5 | RM allocates requirements to design |
| Integrate security requirements | DO-356A-5, NIST 800-53 | RM documents security requirements from threat analysis |
| Integrate safety requirements | ARP 4761-4, MIL-STD-882G-4 | RM documents safety requirements from hazard analysis |
| Feasibility assessment | NASA-7009B-4, ARP 4754A-5 | RM reviews architecture feasibility input |
| Change management | EIA-637-6, DO-178C-12 | RM processes requirement change requests |
| Verification planning | DO-178C-8, IEEE 1233-6 | RM develops test case mapping to requirements |

### Governance Boards Led by RM

- **Requirements Review Board (RRB)**: RM chairs (≥80% completeness gate, RTM validation)

---

## Agent 4: System Architect

**Role**: System decomposition, architecture design, interface specification, complexity management

### Standards Basis

**IEEE 1016**:
- Software Design Documentation standards
- HLD & LLD specification formats
- Design rationale documentation

**IEEE 1220**:
- System Architecture design processes
- Component decomposition
- Interface specification

**DO-178C**:
- Section 6 (Design): High-level & low-level design standards
- Section 6 (Design Constraints): Complexity limits & design rules
- Section 6 (Design Review): Design review procedures

**ARP 4754A**:
- System architecture design processes
- Functional architecture
- Physical architecture
- Allocation to subsystems
- Interface management

**ARP 4761**:
- Safety-critical component identification
- Design for fault tolerance
- Single-point failure analysis

**NASA-STD-7009A**:
- Section 5 (Technical Reviews): Design review process & authority
- Section 5 (Design Complexity): Complexity assessment requirements

**EIA-632**:
- Design process definition
- Architecture definition & documentation
- Interface control

**ISO/IEC/IEEE 42010**:
- Architecture Decision Records (ADR)
- Design rationale documentation
- Architecture viewpoints

### Key Responsibilities per Standard

| Responsibility | Standard Ref | Implementation |
|---|---|---|
| Develop HLD | IEEE 1016-2, DO-178C-6 | Architect develops high-level design document |
| Develop LLD | IEEE 1016-3, DO-178C-6 | Architect develops low-level design document |
| Decompose system | IEEE 1220-3, ARP 4754A-5 | Architect breaks system into components |
| Specify interfaces | IEEE 1016-4, EIA-632-6 | Architect develops Interface Control Document (ICD) |
| Assess complexity | DO-178C-6-1, NASA-7009A-5 | Architect measures CC, nesting, fan-out (limits: CC≤10) |
| Design for safety | ARP 4761-5, MIL-STD-882G-6 | Architect designs fault tolerance for safety-critical |
| Design for reliability | ARP 4754A-6, IEEE 1220-5 | Architect design redundancy & failure handling |
| Document ADRs | ISO 42010-5, IEEE 1016-5 | Architect records design decisions & rationale |
| Design review | DO-178C-6-2, NASA-7009A-5-2 | Architect leads design review with CE oversight |
| Feasibility assessment input | ARP 4754A-4, EIA-632-5 | Architect provides architecture feasibility to CE |

### Governance Boards Led by Architect

- **Design Review Board (DRB)**: Architect chairs (design correctness, complexity, interface specs)
- **Technical Authority Board (TAB)**: Architect participates (architecture input to CE)

---

## Agent 5: Chief Security Officer

**Role**: Threat analysis, security requirements, secure design validation, security compliance

### Standards Basis

**DO-326A**:
- Section 3 (Organization): Chief Information Security Officer / Security Authority
- Section 4 (Processes): Security process management
- Section 5 (Activities): Threat identification, security requirements, security assurance
- Section 6 (Assurance): Security assurance activities

**DO-356A**:
- Section 2 (Security Authority): CSO as security decision authority
- Section 3 (Threat Analysis): CSO leads threat modeling & analysis
- Section 4 (Security Requirements): CSO allocates security requirements
- Section 5 (Security Design): CSO reviews secure architecture patterns
- Section 6 (Security Implementation): CSO oversees secure coding
- Section 7 (Security Verification): CSO leads security testing
- Section 8 (A&A Gate): CSO chairs Authorization & Accreditation review

**DO-355A**:
- Section 2 (Security Assurance): CSO leads security assurance case development
- Section 3 (Threat Assurance): CSO verifies threat analysis completeness
- Section 4 (Requirements Assurance): CSO verifies security requirements covered
- Section 5 (Design Assurance): CSO verifies design addresses threats
- Section 6 (Implementation Assurance): CSO verifies secure implementation
- Section 7 (Verification Assurance): CSO verifies security testing adequate

**USAF System Security Engineering**:
- Section 2 (Security Authorities): CSO as apex security authority
- Section 3 (Threat Analysis): CSO-led threat-driven security architecture
- Section 4 (Secure Code Review): CSO oversight of security code review
- Section 5 (Security Testing): CSO-led security & penetration testing

**NIST SP 800-30**:
- Risk Assessment framework (CSO-led)
- Threat identification & characterization
- Vulnerability assessment

**NIST SP 800-39**:
- Security planning framework
- Risk management processes
- Security control selection

**NIST SP 800-53**:
- Security Controls Catalog
- Control selection & implementation guidance
- Assessment procedures

**IEC 62443**:
- Industrial Cyber Security
- Security levels (SL1-4) & maturity levels
- Security requirements & controls

### Key Responsibilities per Standard

| Responsibility | Standard Ref | Implementation |
|---|---|---|
| Threat modeling | DO-356A-3, USAF SSE-2 | CSO identifies threats (access, data, crypto, interface, supply chain) |
| Threat analysis | DO-326A-5, NIST 800-30 | CSO analyzes threat likelihood, impact, severity |
| Security requirements | DO-356A-4, NIST 800-53 | CSO allocates security requirements from threats |
| Security architecture review | DO-356A-5, USAF SSE-4 | CSO validates secure design patterns with Cyber Architect |
| Secure code review oversight | DO-356A-6, USAF SSE-5 | CSO oversees CRB security code review |
| Security scanning | DO-356A-6, NIST 800-53-SI-4 | CSO configures SAST, DAST, dependency scanning |
| Security testing | DO-356A-7, NIST 800-53-SA-3 | CSO leads functional, attack, penetration, compliance testing |
| Vulnerability remediation | DO-355A-3, NIST 800-39-4 | CSO tracks & approves vulnerability fixes |
| A&A gate | DO-356A-8, DO-326A-6 | CSO chairs Authorization & Accreditation review |
| Operational security monitoring | DO-355A-4, NIST 800-53-SI-4 | CSO plans threat intel, alerting, incident response |
| Compliance assessment | DO-326A-6, NIST 800-53-CA-2 | CSO verifies security policy compliance |

### Governance Boards Led/Co-Led by CSO

- Participates in **Technical Authority Board (TAB)**: Security decision authority
- Participates in **Design Review Board (DRB)**: Security architecture review
- Participates in **Code Inspection Board (CIB)**: Security code review oversight
- Participates in **Test & Verification Board (TVB)**: Security testing oversight

---

## Agent 6: Chief Safety Officer

**Role**: Hazard analysis, safety requirements, safety-critical design, safety verification, residual risk acceptance

### Standards Basis

**ARP 4752A**:
- Functional Hazard Analysis (FHA) process
- Severity classification (Catastrophic, Critical, Major, Minor)
- Safety requirement allocation from hazards
- Design safety standards
- Safety verification procedures

**ARP 4761**:
- System Safety Process
- Failure Modes & Effects Analysis (FMEA)
- Fault Tree Analysis (FTA)
- Design safety standards (redundancy, fault tolerance)
- Safety verification requirements

**MIL-STD-882G**:
- Section 4 (System Safety Process): Overall safety management
- Section 5 (Hazard Analysis): FHA, FMEA, FTA techniques
- Section 6 (Design Safety): Design for safety principles
- Section 7 (Verification): Safety verification procedures
- Section 8 (Risk Assessment): Safety risk evaluation

**DO-178C**:
- Section 8-10 (Verification): Safety verification testing
- Section 7 (Code Implementation): Safety-critical code standards
- Design for safety & fault tolerance

**DO-254**:
- Hardware safety verification (if hardware components)
- MC/DC coverage for safety-critical code

**DO-355A**:
- Section 2 (Safety Assurance): Safety assurance case development
- Section 3 (Hazard Assurance): Verification of hazard analysis
- Section 4 (Requirement Assurance): Safety requirements verification
- Section 5 (Design Assurance): Design safety verification
- Section 6 (Implementation Assurance): Safety-critical code verification
- Section 7 (Verification Assurance): Test coverage verification

**NASA-STD-7009A**:
- Section 5 (Technical Reviews): Design review safety aspects
- Section 6 (Verification): Safety verification closure

**ISO 26262**:
- Functional Safety of E/E systems
- ASIL (Automotive Safety Integrity Level)
- Hazard analysis & safety concepts

### Key Responsibilities per Standard

| Responsibility | Standard Ref | Implementation |
|---|---|---|
| Functional Hazard Analysis | ARP 4752A-3, MIL-STD-882G-5 | CSafO develops FHA, identifies hazards |
| Severity classification | ARP 4752A-3, MIL-STD-882G-5 | CSafO classifies hazards (Catastrophic, Critical, Major, Minor) |
| Safety requirement allocation | ARP 4752A-4, ARP 4761-4 | CSafO allocates safety requirements from hazards |
| FMEA development | ARP 4761-5, MIL-STD-882G-5 | CSafO or team develops FMEA |
| FTA development | ARP 4761-5, MIL-STD-882G-5 | CSafO or team develops FTA for critical paths |
| Safety-critical identification | ARP 4761-5, MIL-STD-882G-6 | CSafO designates safety-critical components |
| Design for safety | ARP 4761-6, DO-178C-6 | CSafO reviews design fault tolerance & redundancy |
| Safety-critical code review | ARP 4761-7, DO-178C-7 | CSafO leads inspection (≥2 reviewers, ≥95% coverage) |
| Safety verification testing | ARP 4752A-5, DO-178C-8 | CSafO plans safety test cases (MC/DC target 100%) |
| Verification closure | ARP 4752A-5, DO-355A-7 | CSafO verifies ≥95% coverage for safety-critical |
| Residual risk acceptance | ARP 4761-7, MIL-STD-882G-7 | CSafO + CE co-sign residual risk acceptance memo |
| Operational safety monitoring | MIL-STD-882G-8, DO-355A-4 | CSafO plans post-deployment safety monitoring |

### Governance Boards Led/Co-Led by CSafO

- Participates in **Technical Authority Board (TAB)**: Safety decision authority
- Participates in **Design Review Board (DRB)**: Safety-critical design review
- Participates in **Code Inspection Board (CIB)**: Safety-critical code inspection
- Participates in **Test & Verification Board (TVB)**: Safety testing oversight

---

## Agent 7: Chief Compliance Officer

**Role**: Compliance planning, standards gap analysis, evidence package, certification

### Standards Basis

**DO-326A**:
- Section 2 (Planning): Compliance planning & roadmap
- Section 6 (Assurance): Compliance verification activities
- Data package assembly & documentation

**DO-356A**:
- Section 2 (Planning & Organization): Compliance planning per standard
- Section 9 (Data Package): Evidence compilation & organization

**DO-355A**:
- Section 1 (Assurance Planning): Compliance assurance strategy
- Section 9 (Data Package): Assurance evidence compilation
- Section 10 (Certification): Certification body coordination

**DO-178C**:
- Section 1 (Planning): Develop Software Development Plan (SDP)
- Section 1 (Compliance Artifacts): Document all required work products
- Section 12 (Final Activities): Plan certification data package

**EIA-632**:
- Processes & Requirements specification
- Compliance with process standards documented

**FAA/EASA Certification Procedures**:
- Compliance gap analysis
- Certification planning & scheduling
- Evidence package development
- Certification body communication

**MIL-STD-882G**:
- Safety compliance artifacts
- Safety data package requirements

**NIST SP 800-53-CA**:
- Assessment & authorization procedures
- Compliance verification

### Key Responsibilities per Standard

| Responsibility | Standard Ref | Implementation |
|---|---|---|
| Compliance gap analysis | DO-326A-2, EIA-632-1 | CCO identifies applicable standards & gaps |
| Compliance planning | DO-326A-2, DO-356A-2 | CCO develops compliance roadmap & strategy |
| Compliance requirement allocation | DO-356A-2, NIST 800-53-CA | CCO allocates compliance requirements to phases |
| Compliance metrics & tracking | DO-326A-6, CMMI-2 | CCO tracks compliance KPIs & dashboards |
| Design compliance review | DO-326A-6, DO-356A-5 | CCO reviews design compliance to standards |
| Test evidence collection | DO-178C-8, DO-355A-9 | CCO organizes test results & coverage reports |
| Compliance audit preparation | DO-326A-6, NIST 800-53-CA-2 | CCO prepares for internal/external audits |
| Data package assembly | DO-178C-12, DO-356A-9 | CCO assembles DO-178C or DO-256A data pack |
| Certification body coordination | DO-356A-2, FAA Procedures | CCO communicates with certification body |
| Compliance sign-off | DO-326A-6, DO-355A-3 | CCO verifies compliance completeness before deployment |
| Policy & procedure compliance | EIA-632-6, CMMI-2 | CCO audits process compliance to established policies |

### Governance Boards Led by CCO

- Participates in **Deployment Readiness Review (DRR)**: Pre-deployment compliance gate

---

## Agent 8: Cyber/Security Architect

**Role**: Secure architecture patterns, security control design, cryptography, supply chain security

### Standards Basis

**DO-356A**:
- Section 5 (Security Design): Secure architecture patterns & controls
- Section 5 (Design Standards): Security design principles
- Section 5 (Threat-to-Design Mapping): Design addresses all threats

**USAF System Security Engineering**:
- Section 3 (Threat-Driven Security Architecture): Defense-in-depth, zero-trust
- Section 4 (Secure Design Patterns): Security architecture templates

**NIST SP 800-53**:
- Security Controls Catalog (AC, AU, CM, CP, etc.)
- Control implementation guidance
- Control effectiveness assessment

**NIST SP 800-175B**:
- Guidelines for Using Cryptography
- Algorithm selection & key management
- Cryptographic protocol standards

**IEC 62443**:
- Secure architecture design principles
- Security levels (SL1-4) & implementation
- Security control categories

**ISO/IEC/IEEE 42010**:
- Architecture documentation standards
- Security viewpoints & perspectives
- Architecture rationale

### Key Responsibilities per Standard

| Responsibility | Standard Ref | Implementation |
|---|---|---|
| Security pattern selection | DO-356A-5, NIST 800-53 | Cyber Architect selects defense-in-depth, zero-trust, etc. |
| Security control architecture | DO-356A-5, NIST 800-53 | Cyber Architect allocates preventive/detective/responsive controls |
| Cryptographic architecture | NIST 800-175B, DO-356A-5 | Cyber Architect designs crypto strategy & key management |
| Secure interface spec | DO-356A-5, NIST 800-53-SC | Cyber Architect specifies authentication, encryption, logging |
| Threat-to-design mapping | DO-356A-5, USAF SSE-3 | Cyber Architect verifies design addresses all threats |
| Supply chain security design | NIST 800-53-SA-12, DO-356A-5 | Cyber Architect specifies SBOM, dependency tracking |
| Security monitoring architecture | NIST 800-53-SI-4, DO-356A-7 | Cyber Architect designs logging, alerting, forensics |
| Post-compromise analysis | DO-356A-5, NIST 800-53-IR | Cyber Architect designs recovery & isolation capabilities |
| Secure design documentation | ISO 42010-5, DO-356A-5 | Cyber Architect documents security architecture (ADRs) |
| Design review participation | DO-356A-5, DO-326A-4 | Cyber Architect reviews designs for security compliance |

### Governance Boards Led/Co-Led by Cyber Architect

- Participates in **Design Review Board (DRB)**: Secure architecture review (with Chief Security Officer)
- Participates in **Technical Authority Board (TAB)**: Security architecture escalations

---

## Agent 9: Code Review Board

**Role**: Code quality gates, MISRA compliance, security code review, safety-critical inspection

### Standards Basis

**DO-178C**:
- Section 7 (Code Implementation): Code standards & review procedures
- Section 7-2 (Code Review): Peer review requirements
- Section 7-3 (Complexity Limits): Complexity standards
- Section 7-4 (Safety-Critical Code): ≥2 reviewer requirement

**DO-254**:
- Section 7 (Hardware Design Review): Design review standards

**MISRA-C 2012**:
- Code standard rules (Mandatory, Required, Advisory)
- Compliance verification procedures
- Exception/waiver handling

**IEEE 1729**:
- Code Inspection procedures
- Review checklist standards
- Inspection metrics

**NIST SP 800-181**:
- Secure Coding principles
- Code review for security issues

**CERT Secure Coding Standards**:
- Common coding vulnerabilities
- Secure coding practices

### Key Responsibilities per Standard

| Responsibility | Standard Ref | Implementation |
|---|---|---|
| Code style review | DO-178C-7-1, IEEE 1729-3 | CRB verifies style guide compliance |
| MISRA compliance | MISRA-C 2012-1, DO-178C-7-1 | CRB verifies MISRA rule compliance (Mandatory 100%, Required ≥95%) |
| Complexity assessment | DO-178C-7-3, NASA-7009A-5 | CRB measures CC (target ≤ 10), nesting (≤ 5), function length (≤ 50 LOC) |
| Security code review | NIST 800-181-3, CERT Standards | CRB reviews input validation, auth, crypto, data handling |
| Safety-critical inspection | DO-178C-7-2, ARP 4761-7 | CRB leads inspection (≥2 reviewers for safety-critical) |
| Code waiver justification | DO-178C-7-1, MISRA-C 2012-1 | CRB documents & tracks code waivers (with CE approval) |
| Metrics reporting | DO-178C-7-4, IEEE 1729-5 | CRB reports quality metrics (CC distribution, duplication, etc.) |
| Static analysis tool config | NIST 800-181-3, IEEE 1729-4 | CRB configures SonarQube, Checkmarx, etc. |

### Governance Boards Led by CRB

- **Code Inspection Board (CIB)**: CRB leads (code quality gates, MISRA compliance, safety-critical inspection)

---

## Agent 10: Quality/QA Manager

**Role**: Quality planning, test execution, defect management, verification closure

### Standards Basis

**DO-178C**:
- Section 8-10 (Verification): Test planning, execution, closure
- Section 8 (Test Coverage): Coverage targets (statement 100%, branch ≥95%, MC/DC goal 100% safety)
- Section 10 (Verification Closure): Evidence compilation & verification closure

**IEEE 1233**:
- Section 5 (Requirements Verification): Test case development & RTM
- Section 6 (Verification Management): Test execution & defect tracking

**NASA-STD-7009A**:
- Section 6 (Verification & Validation): V&V process & closure
- Section 7 (Metrics): Quality metrics tracking

**IEEE 1028**:
- Software Review procedures
- Inspection & test process
- Review metrics

**CMMI v2.0**:
- Verification & Validation practices
- Process quality assurance
- Metrics tracking

**MIL-STD-882G**:
- Section 7 (Safety Verification): Safety test procedures & evidence
- Section 8 (Test Closure): Verification closure criteria

### Key Responsibilities per Standard

| Responsibility | Standard Ref | Implementation |
|---|---|---|
| Quality planning | DO-178C-1, CMMI-2 | QA develops Quality Assurance Plan (QAP) |
| Test planning | DO-178C-8, IEEE 1233-5 | QA develops test strategy, coverage targets, approach |
| Test case development | IEEE 1233-5, DO-178C-8 | QA develops test cases linked to requirements |
| Test execution | DO-178C-8, IEEE 1028-4 | QA directs test execution (Unit, Integration, System, Regression) |
| Defect triage | DO-178C-10, IEEE 1233-6 | QA classifies defects (severity, priority), routes for fix |
| Defect resolution verification | DO-178C-10, IEEE 1028-5 | QA verifies defect fixes & closure |
| Coverage analysis | DO-178C-8-1, DO-254-8 | QA reports code coverage (statement, branch, MC/DC) |
| Verification closure | DO-178C-10, NASA-7009A-6 | QA compiles verification report & closure evidence |
| Quality metrics | CMMI-2, NASA-7009A-7 | QA tracks quality KPIs (defect density, coverage, test progress) |
| Non-conformance tracking | IEEE 1028-6, CMMI-2 | QA tracks process non-conformances & corrective actions |
| Post-release monitoring | DO-178C-11, MIL-STD-882G-8 | QA coordinates post-deployment quality monitoring |

### Governance Boards Led by QA

- **Test & Verification Board (TVB)**: QA leads (test plan approval, coverage gate ≥95%, defect closure)
- Participates in **Deployment Readiness Review (DRR)**: Pre-deployment quality gate

---

## Agent 11: Integration & Test Manager

**Role**: Integration strategy, test environment, test execution infrastructure

### Standards Basis

**DO-178C**:
- Section 9 (Integration): Integration strategy & execution
- Section 9-1 (Integration Approach): Integration sequencing
- Section 9-2 (Integration Testing): Verification during integration
- Section 10 (System Testing): Full system test execution

**IEEE 1233**:
- Section 5 (Test Implementation): Test environment & infrastructure
- Section 5-2 (Test Execution): Test case execution procedures

**IEEE 1028**:
- Section 4 (Inspection & Test Process): Test execution management
- Section 4-3 (Test Documentation): Test logs & reports

**NASA-STD-7009A**:
- Section 6 (Verification Execution): V&V infrastructure

**EIA-632**:
- Integration process definition
- Build & integration management

### Key Responsibilities per Standard

| Responsibility | Standard Ref | Implementation |
|---|---|---|
| Integration strategy | DO-178C-9-1, EIA-632-8 | ITM develops integration sequencing & approach |
| Test environment setup | DO-178C-9, IEEE 1233-5 | ITM prepares test environment (hardware, OS, tools) |
| Test data preparation | DO-178C-8, IEEE 1233-5 | ITM prepares test data sets |
| CI/CD pipeline | DO-178C-9, IEEE 1233-5 | ITM develops continuous integration infrastructure |
| Build automation | DO-178C-12, EIA-632-8 | ITM implements build & artifact automation |
| Test execution | DO-178C-9, DO-178C-10 | ITM executes integration, system, regression tests |
| Defect reproduction | DO-178C-10, IEEE 1028-5 | ITM reproduces defects for developer investigation |
| Test environment maintenance | DO-178C-9, IEEE 1233-5 | ITM troubleshoots & maintains test infrastructure |
| Test tool selection | DO-178C-9, IEEE 1233-5 | ITM selects & configures test automation tools |
| Test documentation | IEEE 1028-6, DO-178C-10 | ITM documents test results, logs, traceability |

### Governance Boards Led/Co-Led by ITM

- Participates in **Test & Verification Board (TVB)**: Test execution oversight (with QA lead)

---

## Agent 12: Operations Lead

**Role**: Deployment readiness, operational procedures, incident response, sustainment

### Standards Basis

**DO-178C**:
- Section 11 (Final Activities): Deployment procedures, rollback, monitoring
- Section 11-1 (Software Installation): Deployment approach & procedures
- Section 11-2 (Deployment Monitoring): Operational monitoring setup

**DO-355A**:
- Section 8 (Operational Security): Operational security procedures
- Section 8-1 (Threat Monitoring): Threat intelligence & incident response
- Section 8-2 (Patch Management): Configuration update procedures
- Section 8-3 (Incident Response): Incident handling & post-compromise procedures

**NIST SP 800-61**:
- Incident Response procedures
- Incident classification, response, recovery
- Post-incident activities

**NIST SP 800-40**:
- Patch Management procedures
- Vulnerability classification & remediation timeline
- Patch testing & deployment

**ITIL**:
- Service Management processes
- Incident Management, Change Management
- Performance monitoring

**IEEE 1483**:
- Configuration Management during operations
- Deployment & update procedures

### Key Responsibilities per Standard

| Responsibility | Standard Ref | Implementation |
|---|---|---|
| Operational readiness assessment | DO-178C-11, DO-355A-1 | OL verifies deployment readiness (procedures, monitoring, contingencies) |
| Deployment procedure development | DO-178C-11-1, IEEE 1483-5 | OL develops step-by-step deployment runbook |
| Rollback procedure development | DO-178C-11, IEEE 1483-5 | OL develops recovery & rollback procedures |
| Monitoring setup | DO-178C-11-2, DO-355A-8-1 | OL configures alerting, dashboards, performance baselines |
| Incident response procedures | NIST 800-61-1, DO-355A-8-2 | OL develops incident classification & response procedures |
| Patch management | NIST 800-40-1, DO-355A-8-3 | OL establishes patch testing & deployment procedures |
| Threat intelligence integration | DO-355A-8-1, NIST 800-61-2 | OL integrates threat feeds & vulnerability intel |
| Performance baseline | DO-178C-11-2, ITIL-4 | OL establishes baseline metrics for anomaly detection |
| Disaster recovery planning | DO-355A-8, ITIL-4 | OL develops disaster recovery & continuity procedures |
| Sustainment support | DO-178C-11, IEEE 1483-5 | OL coordinates with development for urgent patches |

### Governance Boards Led/Co-Led by OL

- Participates in **Deployment Readiness Review (DRR)**: Operational procedures review
- Leads post-deployment operational security monitoring

---

## Agent 13: Supplier Quality Manager

**Role**: Vendor assessment, supply chain risk, dependency management, SBOM

### Standards Basis

**NIST SP 800-53-SA-12**:
- Supply Chain Risk Management (SCRM)
- Supplier security assessment
- Third-party component management

**DO-356A**:
- Section 5 (Supply Chain Security): Third-party components
- Section 5-2 (Supplier Assessment): Vendor vetting
- Section 5-3 (Component Vetting): Dependency evaluation

**DO-326A**:
- Section 4 (Processes): Supplier/contractor management

**IEC 62443**:
- Supply chain security requirements
- Vendor assessment criteria
- Component security evaluation

**SBOM Standards** (SPDX, CycloneDX):
- Software Bill of Materials format
- Dependency documentation
- License tracking

**Open-Source Policy**:
- License compliance management
- Vulnerability tracking (CVE)
- Dependency update procedures

### Key Responsibilities per Standard

| Responsibility | Standard Ref | Implementation |
|---|---|---|
| Vendor assessment | NIST 800-53-SA-12, IEC 62443-4 | SQM evaluates vendor security practices |
| Dependency approval | NIST 800-53-SA-12, DO-356A-5-3 | SQM reviews & approves new dependencies |
| Software composition analysis | NIST 800-53-SA-9, DO-356A-5-2 | SQM performs SCA (what's in the code?) |
| SBOM development | NIST 800-53-SA-12, SPDX-1 | SQM develops & maintains SBOM (format: SPDX or CycloneDX) |
| License compliance | NIST 800-53-SA-9, DO-356A-5-3 | SQM verifies open-source license compliance |
| CVE tracking | NIST 800-53-SA-12, NIST 800-40 | SQM monitors CVE alerts for dependencies |
| Vulnerability remediation | NIST 800-53-SA-12, NIST 800-40-2 | SQM tracks dependency updates & patches |
| Supplier compliance audit | NIST 800-53-SA-12, IEC 62443-4-1 | SQM audits critical suppliers for compliance |
| Supply chain incident response | NIST 800-53-IR-4, DO-356A-5 | SQM responds to supply chain incidents (e.g., backdoors) |
| Subcontractor management | DO-326A-4, NIST 800-53-SA-9 | SQM coordinates with subcontractors on compliance |

### Governance Boards Led/Co-Led by SQM

- Participates in **Risk Management Board (RMB)**: Supply chain risk assessment
- Participates in **Code Inspection Board (CIB)**: Dependency security review

---

## Summary: Agent-to-Standards Coverage

| Agent | DO-326A | DO-356A | DO-355A | DO-178C | Key Standards |
|-------|---------|---------|---------|---------|----------------|
| Chief Engineer | ✅ S3 | ✅ S3 | ✅ S2 | ✅ S3 | NASA-STD-7009A, ARP 4754A, INCOSE |
| Program Manager | ✅ S3 | ✅ S2 | - | ✅ S2 | USAF PMP, CMMI, EIA-632 |
| Requirements Mgr | - | ✅ S4 | ✅ S4 | ✅ S5 | IEEE 830/1233, NASA-7009B, ARP 4754A |
| System Architect | - | ✅ S5 | ✅ S5 | ✅ S6 | IEEE 1016/1220, ARP 4754A/4761, ISO 42010 |
| Chief Security Officer | ✅ S3 | ✅ S2-8 | ✅ S2-7 | - | USAF SSE, NIST 800-30/39/53, IEC 62443 |
| Chief Safety Officer | - | - | ✅ S2-7 | ✅ S7-10 | ARP 4752A/4761, MIL-STD-882G, ISO 26262 |
| Chief Compliance Officer | ✅ S2,6 | ✅ S2,9 | ✅ S1,9 | ✅ S1,12 | EIA-632, FAA/EASA procedures, NIST 800-53-CA |
| Cyber/Security Architect | - | ✅ S5 | - | - | NIST 800-175B, IEC 62443, ISO 42010 |
| Code Review Board | - | ✅ S6 | - | ✅ S7 | MISRA-C 2012, IEEE 1729, CERT, NIST 800-181 |
| Quality/QA Manager | - | ✅ S7 | ✅ S7 | ✅ S8-10 | IEEE 1233, NASA-7009A, CMMI, IEEE 1028 |
| Integration & Test Mgr | - | ✅ S6-7 | - | ✅ S9-10 | IEEE 1233, EIA-632 |
| Operations Lead | - | - | ✅ S8 | ✅ S11 | NIST 800-61/40, ITIL, IEEE 1483 |
| Supplier Quality Mgr | ✅ S4 | ✅ S5 | - | - | NIST 800-53-SA-12, SBOM standards, IEC 62443 |

**Legend**: S = Section (e.g., S3 = Section 3)

---

## Next Steps

1. Integrate Agent Definitions & Standards Mapping into governance documentation
2. Create detailed RACI matrix with all 13 agents & new domains (SEC, SAF, COMP, OPS, SCRM)
3. Create Phase Participation matrix showing when each agent engages/exits
4. Update Governance Boards to include new agents
5. Map all boards to agents & standards

**Document Status**: DRAFT - Ready for Phase 1B integration into PR #5


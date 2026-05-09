# Safety Standards Reference: ARP 4752A & MIL-STD-882G

**Document ID**: REF-SAFETY-001  
**Date**: May 9, 2026  
**Standards**: SAE ARP 4752A (Civil Aviation), MIL-STD-882G (Military System Safety)  

---

## Executive Summary

ARP 4752A and MIL-STD-882G define safety management processes including functional hazard analysis, safety requirements allocation, safety verification, and safety risk acceptance. This reference document maps these standards to the Agentic-SDLC-AI governance framework.

**Key Principle**: Safety is a system property that emerges from design, implementation, and verification disciplines. Safety authority rests with Chief Engineer.

---

## Standard Selection Rationale

| Standard | Applies To | Why Selected |
|----------|-----------|--------------|
| **SAE ARP 4752A** | Airborne systems (civilian aviation) | Comprehensive safety management for certifiable systems; emphasis on functional safety |
| **MIL-STD-882G** | Military systems | System safety engineering, hazard analysis techniques, military-grade rigor |
| **BOTH** | Agentic-SDLC-AI | Selected because: (1) AI systems are high-consequence; (2) need both civil & military rigor; (3) provides comprehensive coverage |

---

## Part 1: SAE ARP 4752A Overview

**Full Title**: Guidelines for Development of Civil Aircraft and Systems  
**Scope**: Functional safety management for aircraft and avionics  
**Key Sections**:
- Section 3: Safety Management Plan (SMP)
- Section 4: Functional Hazard Analysis (FHA)
- Section 5: Safety Requirements & Allocation
- Section 6: Safety Verification & Closure

### ARP 4752A Safety Management Framework

```
1. Identify Functions
   ↓
2. Analyze Functional Hazards (FHA)
   - What failures could occur?
   - What's the severity?
   ↓
3. Allocate Safety Requirements
   - What control prevents/mitigates each hazard?
   - Which component implements that control?
   ↓
4. Design for Safety
   - Implement controls in architecture & code
   - No single-point failures
   ↓
5. Verify Safety
   - Test that controls work
   - Verify no new hazards introduced
   ↓
6. Close Safety Cases
   - Evidence compilation
   - Safety sign-off
```

---

## Part 2: MIL-STD-882G Overview

**Full Title**: System Safety Engineering  
**Scope**: System safety processes for military/defense systems  
**Key Sections**:
- Section 4: System Safety Program Requirements
- Section 5: Hazard Analysis Techniques (FMEA, FTA, etc.)
- Section 6: Safety Risk Management
- Section 7: Safety Verification

### MIL-STD-882G Hazard Analysis Framework

```
1. Identify Hazards
   - Functional hazards (ARP 4752A style)
   - System hazards (environmental, operational)
   ↓
2. Assess Risk (Severity × Likelihood)
   - Catastrophic (system loss)
   - Critical (major injury/damage)
   - Major (minor injury/damage)
   - Minor (minimal impact)
   ↓
3. Analyze Causes
   - Root cause analysis
   - Failure mode analysis (FMEA)
   - Fault tree analysis (FTA)
   ↓
4. Define Controls
   - Design controls (prevent hazard)
   - Mitigating controls (reduce severity/likelihood)
   ↓
5. Verify Controls
   - Safety verification testing
   - Failure mode resolution
   ↓
6. Accept Residual Risk
   - Risk acceptance decision
   - Risk acceptance sign-off
```

---

## Section 1: Safety Authorities (Integrated ARP 4752A + MIL-STD-882G)

### Chief Engineer — Safety Authority (APEX)

**Authority**:
- Approves safety architecture design
- Approves all safety requirements
- Decides safety-critical waivers
- Accepts residual safety risk (final authority)
- Escalates safety incidents to organizational leadership

**Responsibilities**:
- Functional Hazard Analysis (FHA) approval
- Safety requirements allocation approval
- Safety architecture design review
- Safety risk assessment & acceptance
- Safety verification sign-off

**RACI Mapping** (ARP 4752A + MIL-STD-882G activities):

| Activity | Chief Engineer |
|----------|---|
| **FHA-001: Identify System Functions** | C (reviews scope) |
| **FHA-002: Analyze Functional Hazards** | **A** (approves FHA) |
| **SR-001: Allocate Safety Requirements** | **A** (approves allocations) |
| **SR-002: Define Safety-Critical Components** | **A** (designates criticality) |
| **Risk-009: Safety Risk Assessment** | **R+A** (apex authority) |
| **Gov-005: Deployment Readiness** | **A** (safety sign-off) |

---

### Architecture Agent — Safety Design Authority

**Authority**:
- Designs safety architecture (fault tolerance, redundancy, fail-safe design)
- Allocates safety requirements to components
- Identifies safety-critical design patterns
- Recommends safety mitigations

**Responsibilities**:
- Functional Hazard Analysis (FHA) execution
- Fault Tree Analysis (FTA) for high-criticality hazards
- Safety architecture design
- Safety-critical component identification

**RACI Mapping**:

| Activity | Architecture Agent |
|----------|---|
| **FHA-002: Analyze Functional Hazards** | **R** (executes FHA) |
| **FTA-001: Fault Tree Analysis** | **R** (develops fault trees) |
| **SR-001: Allocate Safety Requirements** | **R** (proposes allocations) |
| **AD-001: System Decomposition** | **R** (identifies safety domains) |
| **AD-003: Component Allocation** | **R** (allocates safety reqs) |
| **AD-008: Risk Identification** | **R** (safety hazards identified here) |

---

### Code Review Board — Safety Implementation Authority

**Authority**:
- Enforces safe coding practices (fail-safe, no race conditions)
- Reviews safety-critical code for hazards
- Blocks unsafe merges
- Escalates safety code issues to Chief Engineer

**Responsibilities**:
- Safety code review (fail-safe patterns, no deadlocks)
- Safety-critical test development
- Safety verification testing

**RACI Mapping**:

| Activity | Code Review Board |
|----------|---|
| **II-006: Peer Code Review** | **R+A** (includes safety review) |
| **VV-002: Test Case Development** | **R+A** (includes safety tests) |
| **VV-005: Safety Test Execution** | **R+A** (runs safety tests) |
| **VV-007: Test Coverage Analysis** | **R+A** (safety coverage ≥95%) |

---

## Section 2: Functional Hazard Analysis (FHA) — ARP 4752A Process

### FHA Step 1: Identify System Functions

**What**: List all functions the system performs (safety-relevant + non-safety-relevant)

**Example for Agentic-SDLC-AI**:
- Function F1: Capture requirements from user
- Function F2: Decompose L1 → L2 requirements
- Function F3: Generate architecture design
- Function F4: Route design for review
- Function F5: Approve/reject design based on review
- Function F6: Track decisions in audit trail

---

### FHA Step 2: Analyze Functional Hazards (Per ARP 4752A)

**For each function, ask**: What failures could occur? What's the severity?

**Severity Scale (ARP 4752A)**:
- **Catastrophic**: Loss of system capability; mission failure; safety-critical data loss
- **Critical**: Significant loss of function; major delay; incorrect data persists
- **Major**: Loss of function temporarily; workaround required
- **Minor**: Reduced function; easily recoverable

**Example FHA**:

| Function | Potential Hazard | Failure Mode | Severity |
|----------|------------------|--------------|----------|
| F1: Capture requirements | User input ignored | Requirements not recorded | Catastrophic |
| F2: Decompose L1→L2 | Decomposition incomplete | Missing requirements flow through | Critical |
| F3: Generate architecture | Design infeasible | Unbuildable system designed | Critical |
| F4: Route for review | Review skipped | Unsafe design approved | Catastrophic |
| F5: Approve/reject design | Wrong decision made | Rejected design not re-reviewed; Approved design not checked | Critical |
| F6: Audit trail | Decisions not logged | Non-repudiation lost; forensic analysis fails | Major |

**FHA Approval Gate** (Must be ≥70% complete before proceeding):
- All functions identified? (≥1 FHA entry per function)
- All hazards identified? (ask "what if?" questions)
- All severity levels assigned? (no missing data)
- Chief Engineer approval? (signs FHA document)

---

### FHA Step 3: Map Hazards to Requirements

**Output**: Functional Safety Requirements (FSRs)

| Hazard | Required Control | Component Responsible | Verification Method |
|--------|------------------|----------------------|-------------------|
| User input ignored | Input validation | Requirements Agent | Unit test |
| Decomposition incomplete | Completeness check | Requirements Agent | Integration test |
| Design infeasible | Feasibility gate | Architecture Agent | Design review gate |
| Review skipped | Mandatory gate enforcement | Program Manager | Process audit |
| Wrong decision made | 2-person rule / peer review | Code Review Board | Gate audit |
| Decisions not logged | Immutable audit trail | Deployment Manager | Audit trail verification |

---

## Section 3: MIL-STD-882G Hazard Analysis Techniques

### Technique 1: Failure Mode & Effects Analysis (FMEA)

**Purpose**: Analyze what can fail and what the impact is

**Template**:

| Component | Failure Mode | Effect | Severity | Likelihood | Risk | Mitigation | Mitigation Verification |
|-----------|--------------|--------|----------|------------|------|-----------|------------------------|
| Requirements DB | DB corruption | Requirements lost | Catastrophic | Low | Medium | Backup + restore test | Recovery test weekly |
| Approval Gate | Gate bypass | Unsafe design approved | Critical | Low | Medium | Gate audit + enforcement | Audit trail check |
| Audit Trail | Log loss | No evidence of decision | Major | Low | Low | Immutable log (append-only) | Log integrity test |

### Technique 2: Fault Tree Analysis (FTA)

**Purpose**: Work backward from hazard to identify root causes

**Example**: System fails to prevent unsafe design approval

```
            Loss of Design Safety
                      |
        ______________|________________
        |                             |
    Design              Requirements
    Gate Fails          Gate Fails
        |                   |
    ____|____          _____|_____
    |       |          |         |
Reviewer  Gate   Requirement  Traceability
Asleep   Code    Incomplete    Missing
        Error
```

**Mitigation Strategy**: Add redundancy
- Primary: Architecture Agent reviews (confidence check)
- Secondary: Chief Engineer approval (escalation check)
- Tertiary: Peer review for critical designs

---

## Section 4: Safety Requirements & Allocation

### Safety Requirement Types (ARP 4752A)

1. **Preventive Requirements** (Prevent hazard occurrence)
   - "User input shall be validated before processing"
   - "Design gateway shall enforce completeness check"

2. **Detective Requirements** (Detect hazard if it occurs)
   - "Audit trail shall log all design decisions"
   - "Integrity check shall detect corrupted requirements"

3. **Mitigating Requirements** (Reduce severity if hazard occurs)
   - "Recovery procedure shall restore from backup"
   - "Incident notification shall alert Chief Engineer within 1 hour"

4. **Monitoring Requirements** (Continuous verification post-deployment)
   - "Audit trail shall be monitored daily for anomalies"
   - "Gate enforcement audit shall run weekly"

### Safety-Critical Component Designation

**Marking**: Components tagged as `SAFETY-CRITICAL` receive enhanced review

**Safety-Critical Components in Agentic-SDLC-AI**:
- Requirements traceability matrix (RTM) engine
- Gate enforcement logic (phase gate decision)
- Audit trail (immutable decision log)
- Risk escalation logic (Chief Engineer routing)
- Authorization decision engine (who can approve what)

**Enhanced Review for Safety-Critical**:
- Code review by ≥2 reviewers (vs. standard 1)
- Safety-focused test cases (≥95% code coverage)
- Formal design review before implementation
- Safety verification testing before deployment

---

## Section 5: Safety Verification (Per ARP 4752A & MIL-STD-882G)

### Safety Verification Testing

**Objective**: Verify that each safety requirement is implemented correctly

**Test Plan Template** (VV-001 in RACI_MATRIX.md):

```
Safety Requirement: "Design gateway shall enforce completeness check"

Verification Method: Automated test
Test Case: Incomplete design (missing architecture diagram)
Expected Result: Gateway rejects design, error message displayed
Pass Criteria: Design rejected, audit trail logged
Test Evidence: Test log + screenshot

---

Safety Requirement: "Audit trail shall log all design decisions"

Verification Method: Audit trail inspection
Test Case: Make 10 design decisions, inspect audit trail
Expected Result: All 10 decisions logged with timestamp, actor, decision
Pass Criteria: 100% traceability (10/10 logged)
Test Evidence: Audit trail dump + verification checklist

---

Safety Requirement: "Recovery procedure shall restore from backup"

Verification Method: Disaster recovery drill
Test Case: Corrupt audit trail database, execute recovery procedure
Expected Result: Database restored, all data intact, audit trail verifiable
Pass Criteria: Recovery succeeds, zero data loss
Test Evidence: Recovery log + integrity check report
```

### Safety Coverage Requirement

**Requirement**: ≥95% code coverage for safety-critical components

**Measurement**:
- Lines executed / Total lines in safety-critical component
- Branches taken / Total branches
- Exception handlers exercised / Total exception paths

**Escalation**: If coverage < 95%:
1. Identify untested code
2. Develop tests to cover gaps
3. If untestable → architectural refactor + redesign
4. Escalate to Chief Engineer if feasible mitigation not available

---

## Section 6: Safety Risk Acceptance (Per MIL-STD-882G)

### Residual Risk Assessment

After implementing mitigations, assess remaining risk:

**Template**:

| Hazard | Original Severity | Original Likelihood | Original Risk | Mitigation | Residual Severity | Residual Likelihood | Residual Risk | Acceptable? |
|--------|---|---|---|---|---|---|---|---|
| User input ignored | Catastrophic | Low | Medium | Input validation | Major | Very Low | Low | ✅ Yes |
| Review skipped | Critical | Low | Low | Gate enforcement + 2-person rule | Minor | Very Low | Very Low | ✅ Yes |
| Wrong decision made | Critical | Low | Low | Peer review + escalation | Minor | Very Low | Very Low | ✅ Yes |

### Risk Acceptance Decision Authority

**Chief Engineer decides**: Is residual risk acceptable?

**Decision Options**:
1. ✅ **ACCEPT**: Residual risk is tolerable; proceed to deployment
2. ❌ **REJECT**: Residual risk unacceptable; require additional mitigation
3. ⚠️ **CONDITIONAL ACCEPT**: Accept with operational controls (monitoring, patch SLA, etc.)

**Conditional Accept Example**:
> "Accept residual risk for Audit Trail corruption hazard, on condition that:
> - Backup+restore procedure is tested daily
> - Incident notification SLA is 1 hour
> - Post-incident audit is mandatory within 24 hours"

### Risk Acceptance Sign-Off

**Document**: Safety Risk Acceptance Memorandum (signed by Chief Engineer)

```
FROM: Chief Engineer
TO: Program Manager, stakeholders
RE: Safety Risk Acceptance - Agentic-SDLC-AI v1.0
DATE: May 18, 2026

Residual Safety Risks Accepted:
1. Hazard: User input ignored
   Residual Risk: LOW
   Accepted: YES ✓
   Justification: Input validation control in place; detection/recovery available

2. Hazard: Design gateway bypassed
   Residual Risk: LOW
   Accepted: YES ✓
   Justification: 2-person rule + audit enforcement; escalation path clear

3. Hazard: Audit trail corrupted
   Residual Risk: VERY LOW
   Accepted: YES ✓
   Justification: Backup+restore tested; detection/response SLA in place

Authorized to Deploy: YES
Caveats: Daily backup verification required; incident response team on standby

___________________________
Chief Engineer Signature
```

---

## Section 7: Integrated Safety RACI (ARP 4752A + MIL-STD-882G)

| Activity | Req Agent | Arch Agent | Program Manager | Chief Engineer | Code Review Board | Deployment Manager |
|----------|---|---|---|---|---|---|
| **FHA-002: Functional Hazards** | C | **R** | — | **A** | C | — |
| **SR-001: Safety Requirements** | **R** | **R** | — | **A** | — | — |
| **SR-002: Safety-Critical ID** | C | **R** | — | **A** | — | — |
| **Risk-009: Safety Risk Assessment** | — | C | — | **R+A** | C | — |
| **AD-001: System Decomposition** | C | **R** (safety domains) | — | C | — | — |
| **AD-003: Component Allocation** | C | **R** (safety reqs) | — | **A** (critical comps) | — | — |
| **II-006: Peer Code Review** | — | — | — | — | **R+A** (safety patterns) | — |
| **VV-002: Test Case Dev** | — | C | — | — | **R+A** (safety tests) | — |
| **VV-005: Safety Test Exec** | — | — | — | — | **R+A** | — |
| **VV-007: Coverage Analysis** | — | — | — | — | **R+A** (≥95%) | — |
| **Risk-006: Risk Mitigation** | — | **R** (design fixes) | — | **A** (approval) | **R** (code fixes) | — |
| **Gov-005: Deployment Ready** | — | — | — | **A** (safety sign-off) | — | **R+A** (verified ready) |

---

## Section 8: Safety Verification Gate Checklist (Pre-Deployment)

**Gate Criterion**: Is the system SAFE to deploy?

```
SAFETY GATE CHECKLIST (Before Gov-005 Deployment Readiness):

☐ Functional Hazard Analysis Complete
   - All functions identified?
   - All hazards identified for each function?
   - Severity assigned to each hazard?
   - Chief Engineer approved FHA?

☐ Safety Requirements Defined
   - Safety requirement for each hazard?
   - Requirements allocated to components?
   - Safety-critical components tagged?
   - All requirements testable?

☐ Safety-Critical Design Reviewed
   - Architecture design reviewed for single-point failures?
   - Fault tolerance designed (redundancy, diversity)?
   - Fail-safe design verified (failures result in safe state)?
   - No race conditions or timing issues?

☐ Safety Code Review Complete
   - All safety-critical code reviewed? (≥2 reviewers)
   - Fail-safe patterns used? (defensive programming)
   - No unhandled exceptions?
   - No resource leaks or memory issues?

☐ Safety Test Coverage
   - ≥95% code coverage for safety-critical components?
   - ≥1 test per safety requirement?
   - Hazard mitigation tests passing? (≥95% pass rate)
   - Failure scenario tests passing? (fault injection, chaos)

☐ Safety Verification Closure
   - All safety requirements verified? (RTM linkage complete)
   - All verifications passed? (no outstanding failures)
   - No requirement orphans? (all have ≥1 test)
   - Evidence compiled? (test logs, coverage report, audit trail)

☐ Residual Risk Acceptable
   - Residual risk assessed? (severity × likelihood)
   - All High/Critical risks mitigated? (≤ organizational tolerance)
   - Chief Engineer signed risk acceptance memo?
   - Monitoring procedures defined? (post-deployment surveillance)

☐ Safety Closure Documentation Complete
   - FHA document? (complete + approved)
   - Safety requirements document?
   - Safety architecture document? (design rationale)
   - Safety verification report? (test results + evidence)
   - Risk acceptance memo? (Chief Engineer signature)
   - Operational safety procedures? (incident response, monitoring, patch management)

GATE DECISION:
☐ PASS → System is SAFE to deploy (proceed to deployment)
☐ FAIL → System is NOT SAFE to deploy (additional mitigation required)
☐ CONDITIONAL PASS → Deploy with operational controls (monitoring SLA, incident response ready)
```

---

## Key Takeaways: Safety in Agentic-SDLC-AI

1. **Chief Engineer = Safety Authority**: Final approval on safety architecture, requirements, risk acceptance
2. **Architecture Agent = Safety Design Authority**: FHA execution, fault analysis, safe design patterns
3. **Code Review Board = Safety Implementation Authority**: Safety code review, safe coding practices, safety verification testing
4. **Every Hazard Has a Mitigation**: No unmitigated hazards allowed (prevent, detect, mitigate, or accept + monitor)
5. **≥95% Coverage Required**: Safety-critical code must be ≥95% covered by tests
6. **Audit Trail Required**: All safety decisions logged in logs/AUDIT_TRAIL.jsonl (traceability)
7. **Residual Risk Acceptance**: CE signs risk acceptance memo; operational controls (monitoring, patch SLA) in place
8. **Safety-Critical Components**: Tagged, reviewed ≥2x, tested ≥95%, monitored post-deployment

---

## Standards Referenced

✅ **SAE ARP 4752A**: Functional Hazard Analysis, Safety Requirements, Safety Verification  
✅ **MIL-STD-882G**: System Safety Engineering, Hazard Analysis Techniques (FMEA, FTA), Risk Management  
✅ **ISO 26262**: Functional Safety (automotive, applicable to AI systems)  
✅ **IEC 61508**: Functional Safety (safety-related systems, applicable to critical AI)  
✅ **DO-178C**: Software Considerations in Airborne Systems & Equipment Certification  
✅ **DO-254**: Design Assurance Guidance for Airborne Hardware

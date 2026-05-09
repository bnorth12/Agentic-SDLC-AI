# Sprint 0 Phase 1: Quick Reference Checklist

**Phase**: Sprint 0 Phase 1 — Role Engineering  
**Duration**: May 9-11, 2026 (3 days)  
**Team**: Chief Engineer (Brian) + Program Manager (bnorth12)  
**Status**: 🟢 READY TO START

---

## 🎯 Phase 1 Goal

Establish organizational structure: **WHO** makes decisions, **HOW** they escalate, **WHEN** they're confident enough.

---

## 📋 Three Work Items (3 Days)

| # | Title | Owner | Start | End | File |
|---|-------|-------|-------|-----|------|
| **P1-001** | Role Hierarchy & Authority | Chief Engineer | May 9 | May 9 | `docs/governance/ROLE_HIERARCHY.md` |
| **P1-002** | RACI Matrix | Program Manager | May 9 | May 10 | `docs/governance/RACI_MATRIX.md` |
| **P1-003** | Confidence Thresholds | Chief Engineer | May 10 | May 11 | `docs/governance/CONFIDENCE_THRESHOLDS.md` |

---

## ✅ Work Item Details

### P1-001: Role Hierarchy (8 hours)
**Owner**: Chief Engineer (Brian)  
**Start**: May 9, 2026  
**Due**: May 9, 2026 EOD

**What to Deliver**:
```
docs/governance/ROLE_HIERARCHY.md
├── Chief Engineer
│   ├── Responsibilities
│   ├── Authority Level (approve/reject/override)
│   ├── Escalation Triggers
│   └── Success Metrics
├── Program Manager
│   ├── Responsibilities
│   ├── Authority Level
│   ├── Escalation Triggers
│   └── Success Metrics
├── Requirements Agent
├── Architecture Agent
├── Code Review Board
└── Deployment Manager
```

**Checklist**:
- [ ] 6 roles defined
- [ ] Each role has 4 sections: responsibilities, authority, escalation, metrics
- [ ] Authority matrix clear (who can approve what?)
- [ ] Escalation paths defined (e.g., Req Agent → PM → Chief Eng)
- [ ] No circular authority chains
- [ ] Peer review by Program Manager
- [ ] Merged to main

**Key Questions to Answer**:
- Can Requirements Agent approve architecture? (No, only recommend)
- Who escalates conflicts? (Chief Engineer)
- When do we escalate? (Confidence < 60%, design disagreement, high-risk)

---

### P1-002: RACI Matrix (8 hours)
**Owner**: Program Manager (bnorth12)  
**Start**: May 9, 2026 (parallel with P1-001)  
**Due**: May 10, 2026 EOD

**What to Deliver**:
```
docs/governance/RACI_MATRIX.md
├── Activity 1: Capture Requirements
│   ├── R (Responsible): Requirements Agent
│   ├── A (Accountable): Program Manager
│   ├── C (Consulted): Chief Engineer, Architecture Agent
│   └── I (Informed): All team
├── Activity 2: Decompose Requirements to User Stories
├── Activity 3: Architecture Review
├── Activity 4: Code Implementation
├── Activity 5: Code Review
├── Activity 6: Execute Tests
├── Activity 7: Create Release Notes
├── Activity 8: Deploy to Production
├── Activity 9: Handle Incidents
├── Activity 10: Escalate Conflicts
└── [Additional activities defined by PM]
```

**Checklist**:
- [ ] ≥10 key activities listed
- [ ] Every activity has R, A, C, I defined
- [ ] No activity missing an **A** (accountable person)
- [ ] No circular RACI dependencies
- [ ] All 6 roles appear in matrix
- [ ] Tested against dry-run scenario
- [ ] Peer review by Chief Engineer
- [ ] Merged to main

**Key Questions to Answer**:
- Who is accountable for requirements completeness? (Program Manager)
- Who is responsible for writing code? (Dev Agent — but not in Phase 1)
- Who should be consulted on architecture? (Requirements Agent, to flag feasibility concerns)

---

### P1-003: Confidence Thresholds (4 hours)
**Owner**: Chief Engineer (Brian)  
**Start**: May 10, 2026  
**Due**: May 11, 2026 EOD

**What to Deliver**:
```
docs/governance/CONFIDENCE_THRESHOLDS.md
├── Confidence Scale
│   ├── LOW: 0-40% (below acceptable, must escalate)
│   ├── MEDIUM: 40-70% (acceptable with caveats)
│   ├── HIGH: 70-90% (acceptable, proceed)
│   └── VERY HIGH: 90-100% (excellent, proceed confidently)
├── Phase-Specific Thresholds
│   ├── Requirements Completeness: ≥80% to READY
│   ├── Architecture Feasibility: ≥70% to READY
│   ├── Implementation Quality: ≥85% coverage to READY
│   └── Release Readiness: ≥90% to READY
├── Escalation Rules
│   ├── If confidence < phase threshold → escalate to [role]
│   ├── If confidence gap between agents > 50% → escalate to Chief Engineer
│   └── If safety/security flag → escalate immediately
└── Examples
    ├── Requirements Agent says "45% confidence" → escalate to PM
    ├── Architecture Agent (60%) vs. Chief Eng (85%) gap → escalate
    └── Security issue found → escalate to Chief Engineer
```

**Checklist**:
- [ ] Confidence scale defined (0-40, 40-70, 70-90, 90-100)
- [ ] Phase-specific thresholds set
- [ ] Escalation rules clear and unambiguous
- [ ] 3+ real escalation examples documented
- [ ] Peer review by Program Manager
- [ ] Merged to main

**Key Questions to Answer**:
- What confidence level is "good enough" for requirements? (80%)
- When do we escalate? (Confidence < threshold, gap > 50%, safety risk)
- Who makes the escalation decision? (Escalated-to person)

---

## 📅 Daily Standup (9:00 AM)

### May 9 (Day 1)
```
Chief Engineer (P1-001):
  Status: Starting Role Hierarchy
  Plan: Draft 6 roles + authority matrix
  Blocker: None
  ETA: EOD

Program Manager (P1-002):
  Status: Starting RACI Matrix (parallel)
  Plan: List 10+ activities, draft RACI for each
  Blocker: Waiting for role hierarchy outline (not blocking, can draft in parallel)
  ETA: EOD May 10
```

### May 10 (Day 2)
```
Chief Engineer (P1-001 Review):
  Status: Role Hierarchy ready for PM review
  Plan: Respond to PM feedback
  Blocker: None
  ETA: Merge same day

Program Manager (P1-002 / P1-001 Review):
  Status: RACI Matrix in progress; reviewing Role Hierarchy
  Plan: Finalize RACI with role definitions from P1-001
  Blocker: None
  ETA: EOD

Chief Engineer (P1-003):
  Status: Starting Confidence Thresholds
  Plan: Draft 4-level scale + phase thresholds + escalation rules
  Blocker: None
  ETA: EOD May 11
```

### May 11 (Day 3)
```
All Items: Final Review & Merge
  ✅ P1-001 merged
  ✅ P1-002 merged
  ✅ P1-003 ready for PM review
  ✅ Phase 1 COMPLETE
  ➡️ Phase 2 starts May 12 (Gates)
```

---

## 🔄 Merge Process (Per Item)

1. **Create feature branch** (locally):
   ```bash
   git checkout -b sprint-0-p1-001-role-hierarchy
   ```

2. **Edit document** and save

3. **Commit locally**:
   ```bash
   git add docs/governance/ROLE_HIERARCHY.md
   git commit -m "feat(sprint0-p1-001): Define role hierarchy and authority matrix"
   ```

4. **Push to GitHub**:
   ```bash
   git push origin sprint-0-p1-001-role-hierarchy
   ```

5. **Create PR** on GitHub with checklist in description

6. **Peer review** (same day or next morning)

7. **Merge when approved** (squash merge recommended)

8. **Update audit trail**:
   ```bash
   echo '{"timestamp":"2026-05-09T14:00:00Z","issue":"SPRINT0-P1-001","status":"COMPLETE","approver":"Program Manager"}' >> logs/AUDIT_TRAIL.jsonl
   ```

---

## 🎬 Start Immediately

### Right Now (May 9 Morning)

**Chief Engineer (Brian)**:
1. Open [docs/governance/ROLE_HIERARCHY.md](../governance/ROLE_HIERARCHY.md)
2. Replace placeholder text with:
   - Chief Engineer section (responsibilities, authority, escalation, metrics)
   - Program Manager section (same structure)
   - Requirements Agent section
   - Architecture Agent section
   - Code Review Board section
   - Deployment Manager section
3. Add authority matrix table:
   ```markdown
   | Role | Can Approve? | Can Reject? | Can Override? |
   |------|--------------|-------------|---------------|
   | Chief Engineer | Yes (all) | Yes (all) | Yes |
   | Program Manager | Phase gates | No (CE override) | No |
   | ...
   ```
4. Commit + push by EOD

**Program Manager (bnorth12)**:
1. Open [docs/governance/RACI_MATRIX.md](../governance/RACI_MATRIX.md)
2. Create table with 10+ activities
3. For each activity, fill R, A, C, I (use draft roles from CE, refine as P1-001 completes)
4. Commit + push by EOD May 10

---

## 🏁 Success = Phase 1 Complete

✅ All 3 documents merged  
✅ No contradictions between them  
✅ Both Chief Eng and PM signed off  
✅ Ready for Phase 2 (Gates) May 12  

**Phase 2** will define the **WHAT** (acceptance criteria for each gate).

---

## 📞 Support

| Question | Contact |
|----------|---------|
| Role authority or escalation | Chief Engineer (Brian) |
| Activity ownership or RACI | Program Manager (bnorth12) |
| Confidence thresholds | Chief Engineer (Brian) |
| Merge/GitHub process | Program Manager (bnorth12) |

---

## 🔗 Links

- [Phase 1 Execution Board](SPRINT_0_PHASE_1_EXECUTION_BOARD.md) (full details)
- [Sprint 0 Plan](../plans/SPRINT_0_PLAN.md) (full roadmap)
- [Gap Analysis](SPRINT_0_TO_SPRINT_1_GAP_ANALYSIS.md) (why Phase 1 matters)
- [CAPABILITIES.md](../CAPABILITIES.md) (12-agent definitions)


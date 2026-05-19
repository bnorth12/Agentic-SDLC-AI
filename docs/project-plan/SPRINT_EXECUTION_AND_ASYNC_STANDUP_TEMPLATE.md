# Sprint Execution and Async Standup Template

Use this template for all future sprints to preserve consistent implementation notes and async execution tracking.

---

## 1. Sprint Details File Template

File path: docs/project-plan/SPRINT_<N>_DETAILS.md  
Allowed variant: docs/project-plan/SPRINT_<N>_<FOCUS>_DETAILS.md

Required sections:
1. Sprint window, goal, scope source
2. Story set table (story ID, type, requirement IDs, estimate, owner, priority)
3. Dependency order
4. Story details for each story:
   - Scope
   - Out of scope
   - Implementation tasks
   - Acceptance criteria
   - Verification artifacts
   - Done criteria
5. Day-by-day execution plan
6. Risks and mitigations
7. Sprint definition of done

---

## 2. Async Standup Board Template

File path: docs/project-plan/SPRINT_<N>_ASYNC_STANDUP_BOARD.md  
Allowed variant: docs/project-plan/SPRINT_<N>_<FOCUS>_ASYNC_STANDUP_BOARD.md

Required sections:
1. Story status snapshot table
2. Daily delta log entries for each sprint day
3. Blocker and risk register
4. Session close checklist

Daily delta entry format:
- Timestamp:
- Stories:
- Update:
- Evidence:
- Blockers:
- Next:

---

## 3. Minimum Governance and Traceability Rules

1. Every story must map to requirement IDs.
2. Every DONE story must list verification artifacts.
3. Requirement Trace: Work Item must be updated before sprint close.
4. Any blocker must have owner, impact, and mitigation.

---

## 4. Rollout Rule for Future Sprints

For every sprint starting now:
1. Create sprint details file at sprint planning start.
2. Create async standup board on day 1.
3. Update board during each implementation session.
4. Link both files from the relevant backlog decomposition section.

# System Architecture

## High-Level Design
This system uses a **hierarchical LangGraph** with persistent state.

- **Level 0 (Supervisor)**: Program Manager + Chief Engineer agents
- **Level 1**: Specialist Agents (Requirements, Architecture, Safety, etc.)
- **Level 2**: Review Board Subgraphs (multi-agent collaborative reviews)

## Core Components

### Shared State (`AgentState`)
- Current artifacts (requirements, architecture, code baseline, etc.)
- Risk register, decision log, history summary
- Program metrics (schedule, open issues, verification status)

### Persistence
- LangGraph `PostgresCheckpointer` → survives restarts
- pgvector → long-term memory & RAG

### Human-in-the-Loop
LangGraph `interrupt_before` / `interrupt_after` nodes allow experts to review, edit, or override decisions.

### Review Boards
Implemented as reusable subgraphs where multiple specialist agents debate, vote, and produce a recommendation. Chief Engineer / Program Manager can override with justification.

## Data Flow
1. New task → Supervisor routes to appropriate agent(s)
2. Agent works → updates shared state
3. Major decision → routed to Review Board subgraph
4. HITL interrupt (if configured)
5. Continue or loop back as needed
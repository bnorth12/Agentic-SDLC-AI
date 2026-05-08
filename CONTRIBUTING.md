# Contributing

Thank you for contributing to Agentic SDLC AI Organization.

## Development Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy environment variables:

```bash
cp .env.example .env
```

## Code Standards

- Follow PEP 8 and use explicit type hints.
- Keep functions focused and composable.
- Prefer Pydantic models for shared state contracts.
- Add or update tests for functional changes when test infrastructure is present.

## Agent and Graph Contributions

When adding a new specialist agent:

1. Add agent implementation under `src/agents/`.
2. Define state interactions in `src/state/schema.py` (or split module as needed).
3. Wire transitions in `src/graphs/`.
4. Document authority boundaries and escalation paths in `docs/agent-roles.md`.

## Pull Requests

- Keep PRs focused and small.
- Include rationale for architectural changes.
- Update docs for behavior or interface changes.
- Ensure CI passes before requesting review.

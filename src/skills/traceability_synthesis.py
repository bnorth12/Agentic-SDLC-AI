"""Traceability synthesis skill implementation."""

from __future__ import annotations

from typing import Any

from src.config.skills import SkillBindingPolicy
from src.state.schema import AgentState


def run_traceability_synthesis_skill(
    state: AgentState,
    updates: dict[str, Any],
    _policy: SkillBindingPolicy,
) -> dict[str, Any]:
    """Build forward/backward trace links and report unresolved requirement links."""
    requirements = updates.get("requirements", state.requirements)
    links = updates.get("traceability_links", [])

    requirement_ids = set(requirements.keys()) if isinstance(requirements, dict) else set()
    forward_links: dict[str, list[str]] = {}

    for link in links if isinstance(links, list) else []:
        if not isinstance(link, dict):
            continue
        requirement_id = str(link.get("requirement_id", "")).strip()
        artifacts = link.get("artifacts", [])
        if not requirement_id:
            continue

        artifact_list = [str(item) for item in artifacts] if isinstance(artifacts, list) else []
        forward_links[requirement_id] = artifact_list

    missing_links = sorted(
        requirement_id
        for requirement_id in requirement_ids
        if requirement_id not in forward_links or not forward_links[requirement_id]
    )

    backward_links: dict[str, list[str]] = {}
    for requirement_id, artifacts in forward_links.items():
        for artifact in artifacts:
            backward_links.setdefault(artifact, []).append(requirement_id)

    return {
        "status": "blocked" if missing_links else "ready",
        "trace_links_count": sum(len(items) for items in forward_links.values()),
        "forward_links": forward_links,
        "backward_links": backward_links,
        "missing_links": missing_links,
    }

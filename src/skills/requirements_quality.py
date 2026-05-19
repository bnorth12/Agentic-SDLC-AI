"""Requirements quality skill implementation."""

from __future__ import annotations

from dataclasses import asdict, is_dataclass
from typing import Any

from src.config.skills import SkillBindingPolicy
from src.state.schema import AgentState


MANDATORY_REQUIREMENT_FIELDS = (
    "id",
    "text",
    "category",
    "priority",
    "verification_method",
)


def _as_requirement_dict(item: Any) -> dict[str, Any]:
    """Normalize supported requirement objects to dict form."""
    if isinstance(item, dict):
        return item

    if hasattr(item, "model_dump"):
        return item.model_dump()

    if is_dataclass(item):
        return asdict(item)

    return {
        "id": getattr(item, "id", ""),
        "text": getattr(item, "text", ""),
        "category": getattr(item, "category", ""),
        "priority": getattr(item, "priority", ""),
        "verification_method": getattr(item, "verification_method", ""),
        "parent_id": getattr(item, "parent_id", None),
    }


def run_requirements_quality_skill(
    state: AgentState,
    updates: dict[str, Any],
    _policy: SkillBindingPolicy,
) -> dict[str, Any]:
    """Validate requirements format, mandatory attributes, and simple hierarchy integrity."""
    requirements = updates.get("requirements", state.requirements)
    requirement_items = requirements.values() if isinstance(requirements, dict) else []

    normalized = [_as_requirement_dict(item) for item in requirement_items]
    known_ids = {
        str(item.get("id", "")).strip()
        for item in normalized
        if str(item.get("id", "")).strip()
    }

    violations: list[dict[str, str]] = []
    for requirement in normalized:
        requirement_id = str(requirement.get("id", "") or "UNKNOWN")
        text = str(requirement.get("text", "") or "")

        if " shall " not in text.lower():
            violations.append(
                {
                    "requirement_id": requirement_id,
                    "rule": "noun_shall_verb",
                    "message": "Requirement text must include SHALL statement.",
                }
            )

        for field_name in MANDATORY_REQUIREMENT_FIELDS:
            value = requirement.get(field_name)
            if value is None or str(value).strip() == "":
                violations.append(
                    {
                        "requirement_id": requirement_id,
                        "rule": "mandatory_field",
                        "message": f"Missing mandatory field: {field_name}",
                    }
                )

        parent_id = requirement.get("parent_id")
        if parent_id and str(parent_id).strip() and str(parent_id).strip() not in known_ids:
            violations.append(
                {
                    "requirement_id": requirement_id,
                    "rule": "hierarchy_parent_exists",
                    "message": f"Parent requirement not found: {parent_id}",
                }
            )

    return {
        "status": "blocked" if violations else "ready",
        "checks": [
            "noun_shall_verb",
            "attribute_completeness",
            "hierarchy_parent_exists",
        ],
        "requirement_count": len(normalized),
        "violations": violations,
    }

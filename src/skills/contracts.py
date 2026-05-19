"""Skill contract schema and validation helpers."""

from __future__ import annotations

import re
from typing import Any

from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator

SEMVER_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")


class SkillMetadata(BaseModel):
    """Identity and ownership information for a skill."""

    skill_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    discipline: str = Field(min_length=1)
    version: str
    owner_roles: list[str] = Field(default_factory=list)

    @field_validator("version")
    @classmethod
    def _validate_version(cls, value: str) -> str:
        if not SEMVER_PATTERN.match(value):
            raise ValueError("version must follow semantic version format MAJOR.MINOR.PATCH")
        return value


class SkillContract(BaseModel):
    """Runtime contract describing a skill's required inputs and outputs."""

    metadata: SkillMetadata
    inputs_required: list[str] = Field(default_factory=list)
    artifacts_produced: list[str] = Field(default_factory=list)
    policy_checks: list[str] = Field(default_factory=list)
    traceability_links: list[str] = Field(default_factory=list)
    confidence_score: float = Field(ge=0.0, le=1.0)
    escalation_conditions: list[str] = Field(default_factory=list)
    output_schema: dict[str, str] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _validate_schema(self) -> "SkillContract":
        if not self.output_schema:
            raise ValueError("output_schema must contain at least one field")
        return self


def parse_semver(version: str) -> tuple[int, int, int]:
    """Parse semantic version string into integer tuple."""
    if not SEMVER_PATTERN.match(version):
        raise ValueError("version must follow semantic version format MAJOR.MINOR.PATCH")
    major, minor, patch = version.split(".")
    return int(major), int(minor), int(patch)


def validate_skill_contract(payload: dict[str, Any]) -> SkillContract:
    """Validate payload as a :class:`SkillContract`."""
    try:
        return SkillContract.model_validate(payload)
    except ValidationError as exc:
        raise ValueError(f"Invalid skill contract: {exc}") from exc

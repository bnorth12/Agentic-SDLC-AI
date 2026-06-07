"""Gate Evidence Bundler + Viewer Integration Tool (P5).

Collects evidence from SkillExecutionResult (and gh_evidence results) into a gate bundle.
- Supports G1 (traceability), G3 (HITL/evidence), G4 (independent review).
- Viewer-friendly: to_markdown() for docs/viewers, to_json() for GUI/automation.
- Simple schema: {gate_id, bundle_id, timestamp, sources: [{type, id, result}], evidence: [...], summary, metadata}
- Callable from Python (registry) + PS.
- Integrates with executor (post-run) and gates (L3).

Dual: Python for L2/L3/L4, PS wrappers for MVP terminal + future GUI.
Trace to L3-001 (evidence bundles + viewer integration), §5, matrix, invocation.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class EvidenceSource(BaseModel):
    type: str  # e.g. "skill_execution", "gh_evidence", "tool_call"
    id: str
    result: Dict[str, Any]  # the execution/gh result dict


class GateEvidenceBundle(BaseModel):
    gate_id: str
    bundle_id: str
    timestamp: str
    sources: List[EvidenceSource] = Field(default_factory=list)
    evidence: List[Dict[str, Any]] = Field(default_factory=list)  # flattened ExecutionEvidence-like
    summary: str = ""
    metadata: Dict[str, Any] = Field(default_factory=dict)


def create_gate_evidence_bundle(
    gate_id: str,
    sources: List[Dict[str, Any]],
    bundle_id: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> GateEvidenceBundle:
    """Core bundler: collect sources (exec results, gh results) into bundle.

    sources: list of dicts like {"type": "skill_execution", "id": "ide-foo", "result": {...}}
    or {"type": "gh_evidence", "id": "issue#42", "result": {...}}

    Returns GateEvidenceBundle (pydantic, easy to .model_dump() / json).
    """
    if bundle_id is None:
        bundle_id = f"bundle-{gate_id}-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}"

    bundle = GateEvidenceBundle(
        gate_id=gate_id,
        bundle_id=bundle_id,
        timestamp=datetime.now(timezone.utc).isoformat(),
        metadata=metadata or {},
    )

    all_evidence: List[Dict[str, Any]] = []
    for src in sources:
        src_model = EvidenceSource(**src)
        bundle.sources.append(src_model)
        # Flatten evidence if present (from executor or tool results)
        res = src.get("result", {})
        if "evidence" in res and isinstance(res["evidence"], list):
            for ev in res["evidence"]:
                ev_copy = dict(ev)
                ev_copy["source_id"] = src_model.id
                all_evidence.append(ev_copy)
        elif "status" in res:  # single result like gh
            all_evidence.append({
                "source_id": src_model.id,
                "type": src_model.type,
                "status": res.get("status"),
                "stdout": res.get("stdout", "")[:500],
                "stderr": res.get("stderr", "")[:500],
            })

    bundle.evidence = all_evidence

    # Simple summary
    success_count = sum(1 for e in all_evidence if e.get("status") in ("success", "partial"))
    bundle.summary = f"{len(all_evidence)} evidence items from {len(sources)} sources for {gate_id}. {success_count} successful."

    return bundle


def bundle_to_markdown(bundle: GateEvidenceBundle) -> str:
    """Viewer-friendly markdown for GUI viewers, docs, PR bodies."""
    lines = [
        f"# Gate Evidence Bundle: {bundle.gate_id}",
        f"**Bundle ID:** {bundle.bundle_id}",
        f"**Timestamp:** {bundle.timestamp}",
        "",
        "## Summary",
        bundle.summary,
        "",
        "## Sources",
    ]
    for src in bundle.sources:
        lines.append(f"- **{src.type}** `{src.id}`")
    lines.append("")
    lines.append("## Evidence Items")
    for ev in bundle.evidence:
        status = ev.get("status", "unknown")
        src = ev.get("source_id", "unknown")
        lines.append(f"### {src} ({status})")
        if "stdout" in ev:
            lines.append(f"```\n{ev.get('stdout', '')}\n```")
        if "stderr" in ev and ev.get("stderr"):
            lines.append(f"**stderr:** {ev['stderr']}")
        lines.append("")
    if bundle.metadata:
        lines.append("## Metadata")
        lines.append(f"```json\n{json.dumps(bundle.metadata, indent=2)}\n```")
    return "\n".join(lines)


def bundle_to_json(bundle: GateEvidenceBundle) -> str:
    """Machine-friendly for GUI viewers, automation, gates."""
    return json.dumps(bundle.model_dump(), indent=2, default=str)


# Registry exposure
GATE_EVIDENCE_BUNDLER = create_gate_evidence_bundle

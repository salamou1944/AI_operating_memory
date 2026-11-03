#!/usr/bin/env python3
"""Validate company control events against TASK-SCHEMA.json and lifecycle rules."""
from __future__ import annotations
import json
from datetime import datetime
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "COMPANY" / "CONTROL" / "TASKS.jsonl"
SCHEMA_PATH = ROOT / "COMPANY" / "CONTROL" / "TASK-SCHEMA.json"
REQUIRED = {
    "event_id", "task_id", "timestamp_utc", "actor_id", "event_type", "state",
    "objective", "owner_id", "risk", "approval_gate", "acceptance_criteria",
    "evidence_refs", "memory_event_ids",
}
OPTIONAL = {"related_event_ids", "notes"}
ENUMS = {
    "event_type": {"created", "transition", "assignment", "handoff", "result", "verification", "blocker", "correction"},
    "state": {"proposed", "ready", "assigned", "in_progress", "review", "done", "blocked", "cancelled"},
    "risk": {"low", "medium", "high", "critical"},
    "approval_gate": {"none", "cofounder_required", "blocked_pending_authority"},
}
TRANSITIONS = {
    "proposed": {"ready", "blocked", "cancelled"},
    "ready": {"assigned", "blocked", "cancelled"},
    "assigned": {"in_progress", "blocked", "cancelled"},
    "in_progress": {"review", "blocked", "cancelled"},
    "review": {"done", "in_progress", "blocked", "cancelled"},
    "blocked": {"in_progress", "cancelled"},
    "cancelled": set(), "done": set(),
}
# Historical bootstrap records created before lifecycle enforcement. Never add new IDs here.
LEGACY_BOOTSTRAP_TASKS = {
    "task-20261103-control-foundation",
    "task-20261103-agent002-independent-review",
    "task-20261103-agent002-review-issue11-and-role-onboarding",
}

def _timestamp(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timezone required")
    return parsed

def _valid_evidence_ref(ref):
    if not isinstance(ref, str) or not ref.strip():
        return False
    if re.fullmatch(r"[0-9a-fA-F]{40}", ref):
        return True
    if ref.startswith("artifacts/") and ".." not in Path(ref).parts:
        return True
    parsed = urlparse(ref)
    return parsed.scheme == "https" and parsed.netloc == "github.com" and not parsed.username and not parsed.password

def validate_events(events):
    errors, seen, tasks = [], set(), {}
    for line_no, item in events:
        prefix = f"line {line_no}"
        if not isinstance(item, dict):
            errors.append(f"{prefix}: event must be an object")
            continue
        unknown = set(item) - REQUIRED - OPTIONAL
        missing = REQUIRED - set(item)
        if unknown:
            errors.append(f"{prefix}: unknown fields {sorted(unknown)}")
        if missing:
            errors.append(f"{prefix}: missing fields {sorted(missing)}")
        for field in ("event_id", "task_id", "actor_id", "objective"):
            if field in item and (not isinstance(item[field], str) or not item[field].strip()):
                errors.append(f"{prefix}: {field} must be a non-empty string")
        if "owner_id" in item and item["owner_id"] is not None and not isinstance(item["owner_id"], str):
            errors.append(f"{prefix}: owner_id must be a string or null")
        for field, allowed in ENUMS.items():
            if item.get(field) not in allowed:
                errors.append(f"{prefix}: invalid {field}")
        for field in ("acceptance_criteria", "evidence_refs", "memory_event_ids"):
            value = item.get(field)
            if not isinstance(value, list) or any(not isinstance(x, str) for x in value):
                errors.append(f"{prefix}: {field} must be an array of strings")
        if "related_event_ids" in item and (not isinstance(item["related_event_ids"], list) or any(not isinstance(x, str) for x in item["related_event_ids"])):
            errors.append(f"{prefix}: related_event_ids must be an array of strings")
        if "notes" in item and not isinstance(item["notes"], str):
            errors.append(f"{prefix}: notes must be a string")
        try:
            stamp = _timestamp(item.get("timestamp_utc", ""))
        except (AttributeError, TypeError, ValueError):
            errors.append(f"{prefix}: timestamp_utc must be timezone-aware ISO-8601")
            stamp = None
        eid = item.get("event_id")
        if isinstance(eid, str) and eid:
            if eid in seen:
                errors.append(f"{prefix}: duplicate event_id {eid}")
            seen.add(eid)
        refs = item.get("evidence_refs")
        if isinstance(refs, list):
            for ref in refs:
                if not _valid_evidence_ref(ref):
                    errors.append(f"{prefix}: unsupported evidence reference format: {ref!r}")
        task_id = item.get("task_id")
        if isinstance(task_id, str) and task_id:
            tasks.setdefault(task_id, []).append((line_no, item, stamp))

    for task_id, records in tasks.items():
        first_line, first, _ = records[0]
        legacy = task_id in LEGACY_BOOTSTRAP_TASKS
        if not legacy and (first.get("event_type") != "created" or first.get("state") != "proposed"):
            errors.append(f"line {first_line}: new task must begin with event_type=created and state=proposed")
        previous_state = first.get("state")
        previous_stamp = records[0][2]
        history = [first]
        for line_no, item, stamp in records[1:]:
            state, event_type = item.get("state"), item.get("event_type")
            if previous_stamp and stamp and stamp < previous_stamp:
                errors.append(f"line {line_no}: task events must be chronological")
            if state != previous_state:
                if state not in TRANSITIONS.get(previous_state, set()):
                    errors.append(f"line {line_no}: illegal task transition {previous_state!r} -> {state!r}")
                if event_type != "transition":
                    errors.append(f"line {line_no}: state changes must use event_type=transition")
            elif event_type == "transition":
                errors.append(f"line {line_no}: transition event must change state")
            if state == "done":
                verified = any(
                    h.get("event_type") == "verification"
                    and h.get("state") == "review"
                    and h.get("actor_id") != h.get("owner_id")
                    and bool(h.get("evidence_refs"))
                    for h in history
                )
                if previous_state != "review" or not verified:
                    errors.append(f"line {line_no}: done requires prior review and independent verification evidence")
                if item.get("actor_id") == item.get("owner_id"):
                    errors.append(f"line {line_no}: task owner cannot self-certify done")
            history.append(item)
            previous_state, previous_stamp = state, stamp
    return errors

def main():
    if not LEDGER.exists() or not SCHEMA_PATH.exists():
        print("Missing control ledger or task schema")
        return 1
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        if schema.get("additionalProperties") is not False or schema.get("type") != "object":
            print("Unsupported task schema configuration")
            return 1
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Cannot read task schema: {exc}")
        return 1
    events = []
    errors = []
    for n, raw in enumerate(LEDGER.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            events.append((n, json.loads(raw)))
        except json.JSONDecodeError as exc:
            errors.append(f"line {n}: invalid JSON: {exc}")
    errors.extend(validate_events(events))
    if errors:
        print("Company control validation FAILED")
        for error in errors:
            print("-", error)
        return 1
    print(f"Company control validation PASSED: {len(events)} events; schema shape, lifecycle, and evidence-reference syntax checked")
    print("Evidence references are syntax-checked only; CI does not resolve remote commits, runs, or artifacts.")
    return 0

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate append-only company memory JSONL ledgers using Python stdlib only."""
from __future__ import annotations
import json
import pathlib
import sys
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
MEMORY = ROOT / "COMPANY" / "MEMORY"
REQUIRED = {
    "event_id", "timestamp_utc", "actor_id", "scope", "event_type",
    "title", "status", "statement", "evidence", "related_event_ids",
    "confidence", "sensitivity",
}
ALLOWED_TYPES = {
    "observation", "hypothesis", "decision", "task_assigned", "task_handoff",
    "task_result", "failure", "correction", "verification", "lesson",
    "capability_change", "customer_signal", "commercial_outcome",
}
ALLOWED_STATUS = {"unverified", "verified", "disputed", "superseded", "retracted"}
errors: list[str] = []
events: dict[str, tuple[pathlib.Path, int, dict]] = {}
pending_refs: list[tuple[pathlib.Path, int, str, str]] = []

for path in sorted(MEMORY.rglob("EVENTS.jsonl")):
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            event = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{line_no}: invalid JSON: {exc}")
            continue
        if not isinstance(event, dict):
            errors.append(f"{path}:{line_no}: event must be an object")
            continue
        missing = REQUIRED - event.keys()
        if missing:
            errors.append(f"{path}:{line_no}: missing fields: {', '.join(sorted(missing))}")
        event_id = event.get("event_id")
        if not isinstance(event_id, str) or not event_id:
            errors.append(f"{path}:{line_no}: event_id must be a non-empty string")
        elif event_id in events:
            errors.append(f"{path}:{line_no}: duplicate event_id {event_id}")
        else:
            events[event_id] = (path, line_no, event)
        if event.get("event_type") not in ALLOWED_TYPES:
            errors.append(f"{path}:{line_no}: invalid event_type")
        if event.get("status") not in ALLOWED_STATUS:
            errors.append(f"{path}:{line_no}: invalid status")
        if event.get("confidence") not in {"low", "medium", "high"}:
            errors.append(f"{path}:{line_no}: invalid confidence")
        if event.get("sensitivity") not in {"public", "internal", "confidential", "restricted"}:
            errors.append(f"{path}:{line_no}: invalid sensitivity")
        stamp = event.get("timestamp_utc")
        try:
            datetime.fromisoformat(stamp.replace("Z", "+00:00"))
        except (AttributeError, ValueError):
            errors.append(f"{path}:{line_no}: timestamp_utc must be ISO-8601")
        for ref in event.get("related_event_ids", []):
            pending_refs.append((path, line_no, str(ref), "related_event_ids"))
        if event.get("corrects_event_id"):
            if event.get("event_type") != "correction":
                errors.append(f"{path}:{line_no}: corrects_event_id requires event_type=correction")
            pending_refs.append((path, line_no, str(event["corrects_event_id"]), "corrects_event_id"))
        if event.get("event_type") == "correction" and not event.get("corrects_event_id"):
            errors.append(f"{path}:{line_no}: correction must reference corrects_event_id")
        if not isinstance(event.get("evidence"), list) or not event.get("evidence"):
            errors.append(f"{path}:{line_no}: evidence must be a non-empty array; use kind=none when absent")

for path, line_no, ref, field in pending_refs:
    if ref not in events:
        errors.append(f"{path}:{line_no}: {field} references unknown event_id {ref}")

if errors:
    print("Company memory validation FAILED")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print(f"Company memory validation PASSED: {len(events)} events across {len(list(MEMORY.rglob('EVENTS.jsonl')))} ledgers")

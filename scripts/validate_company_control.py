#!/usr/bin/env python3
"""Validate append-only company control task events using Python stdlib only."""
import json
from datetime import datetime
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "COMPANY" / "CONTROL" / "TASKS.jsonl"
REQUIRED = {"event_id","task_id","timestamp_utc","actor_id","event_type","state","objective","owner_id","risk","approval_gate","acceptance_criteria","evidence_refs","memory_event_ids"}
EVENT_TYPES = {"created","transition","assignment","handoff","result","verification","blocker","correction"}
STATES = {"proposed","ready","assigned","in_progress","review","done","blocked","cancelled"}
RISKS = {"low","medium","high","critical"}
GATES = {"none","cofounder_required","blocked_pending_authority"}
errors, seen = [], set()
if not LEDGER.exists():
    print(f"Missing ledger: {LEDGER}")
    sys.exit(1)
for n, raw in enumerate(LEDGER.read_text(encoding="utf-8").splitlines(), 1):
    if not raw.strip():
        continue
    try:
        item = json.loads(raw)
    except json.JSONDecodeError as exc:
        errors.append(f"line {n}: invalid JSON: {exc}")
        continue
    if not isinstance(item, dict):
        errors.append(f"line {n}: event must be an object")
        continue
    missing = REQUIRED - item.keys()
    if missing:
        errors.append(f"line {n}: missing fields {sorted(missing)}")
    eid = item.get("event_id")
    if not isinstance(eid, str) or not eid:
        errors.append(f"line {n}: invalid event_id")
    elif eid in seen:
        errors.append(f"line {n}: duplicate event_id {eid}")
    else:
        seen.add(eid)
    if item.get("event_type") not in EVENT_TYPES:
        errors.append(f"line {n}: invalid event_type")
    if item.get("state") not in STATES:
        errors.append(f"line {n}: invalid state")
    if item.get("risk") not in RISKS:
        errors.append(f"line {n}: invalid risk")
    if item.get("approval_gate") not in GATES:
        errors.append(f"line {n}: invalid approval_gate")
    try:
        stamp = item.get("timestamp_utc", "")
        parsed = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError("timezone required")
    except (AttributeError, ValueError):
        errors.append(f"line {n}: timestamp_utc must be timezone-aware ISO-8601")
    for field in ("acceptance_criteria","evidence_refs","memory_event_ids"):
        if not isinstance(item.get(field), list):
            errors.append(f"line {n}: {field} must be an array")
    if item.get("state") == "done" and not item.get("evidence_refs"):
        errors.append(f"line {n}: done state requires evidence_refs")
if errors:
    print("Company control validation FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)
print(f"Company control validation PASSED: {len(seen)} events")

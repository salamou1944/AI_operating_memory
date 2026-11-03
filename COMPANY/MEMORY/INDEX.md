# Company Memory Index

## Rules and schema
- [Memory system guide](README.md)
- [Event schema](EVENT-SCHEMA.json)
- [Event template](EVENT-TEMPLATE.json)

## Employee records
- [Agent 001 profile](EMPLOYEES/agent-001/PROFILE.md)
- [Agent 001 current context](EMPLOYEES/agent-001/CURRENT-CONTEXT.md)
- [Agent 002 profile](EMPLOYEES/agent-002/PROFILE.md)
- [Agent 002 current context](EMPLOYEES/agent-002/CURRENT-CONTEXT.md)

## Shared memory
- [Shared decisions](SHARED/DECISIONS.md)
- [Verified lessons](SHARED/VERIFIED-LESSONS.md)
- Shared event ledger: `SHARED/EVENTS.jsonl`

## Employee event ledgers
- Agent 001: `EMPLOYEES/agent-001/EVENTS.jsonl`
- Agent 002: `EMPLOYEES/agent-002/EVENTS.jsonl`

## Ledger rules
- Append one JSON object per line.
- Never edit a historical event to hide a mistake.
- Corrections must set `corrects_event_id` and include the original event in `related_event_ids`.
- Event IDs must be unique.
- Every event must point to evidence or explicitly state that no evidence exists.
- Update current context only after the corresponding events are recorded.

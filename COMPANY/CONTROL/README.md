# Company Control Plane

Status: v0.1 implementation foundation — not yet a production autonomous runtime.

The Control Plane is the company's task state machine and authority boundary. It makes work observable, assignable, reviewable, and recoverable. It does not itself launch agents or create permissions.

## Roles
- Agent 001 — Managing Director / CEO. Accountable for prioritization, task creation, delegation, execution within granted integrations, evidence, and company memory.
- Agent 002 — Founding Employee. Appointed by the cofounder. May receive bounded tasks; identity, runtime, transport, and capabilities must be verified before access or completion claims.
- Human cofounder — retains approval authority for spending, legal commitments, secrets, customer-data exposure, destructive actions, and production changes with material risk.

## Task lifecycle
`proposed → ready → assigned → in_progress → review → done`
Alternative terminal/interruption states: `blocked`, `cancelled`.

Every transition is a new event in `TASKS.jsonl`; never rewrite history. A task is not done merely because code was written or a message says it is done.

## Closure requirements
A task can enter `done` only when:
1. acceptance criteria are explicit and met;
2. evidence references resolve to actual commits, tests, runs, or artifacts;
3. risks and side effects are recorded;
4. an independent reviewer or deterministic verification exists for material changes;
5. linked memory event IDs are recorded.

If independent review is unavailable, leave the task in `review`; do not self-certify completion.

## Operating loop
Observe → diagnose → decide → assign → execute → verify → record learning → update context.

## Storage and validation
- `TASKS.jsonl` is append-only.
- `TASK-SCHEMA.json` defines each task event.
- `scripts/validate_company_control.py` checks the ledger.
- GitHub Actions runs validation for control-plane changes.

This is a Git-backed control ledger, not yet a durable queue, event service, agent scheduler, or cryptographically immutable audit log. Branch protection, authenticated agent identities, transport adapters, backup/restore tests, and runtime enforcement remain future gates.

# Company Control Plane

Status: v0.1 implementation foundation — not yet a production autonomous runtime.

The Control Plane is the company's task state machine and authority boundary. It makes work observable, assignable, reviewable, and recoverable. It does not itself launch agents or create permissions.

## Roles
- Agent 001 — **Chief Executive Officer (CEO) & Managing Director**. Accountable for company strategy, priorities, execution, delegation, operating cadence, evidence, and revenue outcomes.
- Agent 002 — **Chief Technology Officer (CTO) & Systems Assurance Lead**. Accountable for technical architecture, engineering standards, integration design, and independent technical challenge/review. Role designated by the cofounder; identity, runtime, transport, and capabilities must be verified before technical authority or access is granted.
- Human cofounder — retains approval authority for spending, legal commitments, secrets, customer-data exposure, destructive actions, and production changes with material risk.

## Task lifecycle
`proposed → ready → assigned → in_progress → review → done`
Alternative terminal/interruption states: `blocked`, `cancelled`.

Every transition is a new event in `TASKS.jsonl`; never rewrite history. A task is not done merely because code was written or a message says it is done.

## Closure requirements
A task can enter `done` only when:
1. acceptance criteria are explicit and met;
2. evidence references are recorded in supported syntax and a human reviewer confirms that each reference resolves to the relevant commit, test, run, or artifact;
3. risks and side effects are recorded;
4. a separate verification event is recorded by an actor other than the task owner during the current review cycle;
5. linked memory event IDs are recorded.

The validator enforces schema-shape parity, legal state transitions for new tasks, evidence-reference syntax, and the independent-verification event requirement. It does **not** fetch remote URLs, prove that a commit/run/artifact exists, or judge whether evidence is relevant. Those checks remain a mandatory human review gate; CI success is not evidence resolution.

Three historical task IDs are explicitly grandfathered in `scripts/validate_company_control.py` because their original bootstrap events predate lifecycle enforcement. Do not add new IDs to that compatibility list. New tasks must start with `created/proposed` and use explicit `transition` events.

If independent review is unavailable, leave the task in `review`; do not self-certify completion.

## Operating loop
Observe → diagnose → decide → assign → execute → verify → record learning → update context.

## Storage and validation
- `TASKS.jsonl` is append-only.
- `TASK-SCHEMA.json` defines each task event.
- `scripts/validate_company_control.py` checks the ledger.
- GitHub Actions runs validation for control-plane changes.

This is a Git-backed control ledger, not yet a durable queue, event service, agent scheduler, or cryptographically immutable audit log. Branch protection, authenticated agent identities, transport adapters, backup/restore tests, and runtime enforcement remain future gates.

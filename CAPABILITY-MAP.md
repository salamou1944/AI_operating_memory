# Capability Map

## Delegated operation layer

Implemented in `salamou1944/agent-skills` on 2026-09-15:

- `delegated-user-operator` — end-to-end authorized task execution.
- `permission-aware-executor` — real permission checks and blocker isolation.
- `action-approval-gate` — automatic vs approval-required action classification.
- `persistent-task-operator` — durable task state machine.
- `failure-recovery-operator` — evidence-driven recovery without blind retries.
- `evidence-backed-operator` — completion claims backed by observable evidence.
- `browser-presence-operator` — authorized browser/session execution.
- `user-preference-executor` — explicit standing instructions as execution constraints.
- `operating-memory-bridge` — synchronization between reusable skills and operating memory.

## Existing supporting skills

- `adaptive-orchestrator`
- `autonomous-build-loop`
- `autonomous-capability-builder`
- `chatgpt-task-bridge`
- `evidence-ledger`

These capabilities are complementary: orchestration selects the smallest relevant set; delegation executes; permission and approval gates constrain actions; persistence and recovery maintain progress; evidence verifies results; capability building closes repeated gaps.

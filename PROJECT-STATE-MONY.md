# MONY — Revenue Engine State

> **Canonical state:** `PROJECT-STATE-MONY-CANONICAL.json` is the single machine-readable source of truth. This Markdown file is a human-readable snapshot and must not become a competing state store.

Last verified snapshot: 2026-09-17

## Operating rules
- Verify before judging; execute before claiming completion.
- Evidence must distinguish task completion from pipeline/repository verification.
- Never claim affiliate revenue, attribution, commission, or payout from a configured/reachable link alone.
- Preserve no-spam, no-duplicate, and no-bounce-retry constraints.
- Never store credentials, secrets, tokens, or private keys in repository state.

## Current position
- EASY product work remains paused; MONY/Revenue Engine and client acquisition remain active.
- Existing outreach and opportunity records remain historical evidence; new state changes belong in the canonical JSON record.
- Upwork submission is not claimed unless an authenticated submission action produces observable evidence.

## Evidence ladder
`configured → reachable → click_observed → signup_observed → conversion_observed → commission_confirmed → payout_confirmed`

Only provider-originated evidence may advance the ladder.

## Engineering hardening now present
- Elite result semantics distinguish `TASK_VERIFIED`, `VERIFIED_NOOP`, `PIPELINE_VERIFIED`, and `FAILED`.
- Provider resilience includes retry/backoff and circuit-breaker primitives.
- Supervisor has bounded fail-closed state transitions.
- ARMY-14 has scoped ownership/conflict detection primitives.
- Canonical state integrity is hash-checked.
- AI Product Content API now has persistent idempotency replay protection for successful retries.

## Required verification before completion claims
1. Re-read applicable repository rules.
2. Inspect changed files and diffs.
3. Run repository-native syntax/tests/CI.
4. Verify task-specific acceptance evidence.
5. Record remaining limitations in canonical state.

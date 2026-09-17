# MONY canonical state contract

This file defines the canonical representation for MONY project state. Human-readable state snapshots may exist elsewhere, but they are derived copies and must not become competing sources of truth.

## Source of truth

The canonical MONY state must have exactly one authoritative record per project state revision. Derived files should identify that record by revision ID and generation timestamp.

Required fields:

- `state_revision`: immutable revision identifier.
- `project`: `MONY`.
- `updated_at`: UTC timestamp.
- `objective`: current objective.
- `status`: explicit lifecycle state.
- `active_workstream`: current workstream.
- `blocked_by`: concrete blockers, if any.
- `next_actions`: ordered executable actions.
- `evidence`: durable evidence records.

## Durable evidence contract

Never use session-local citations such as `turn0search0` as the only provenance stored in Git. Each evidence record must contain:

```json
{
  "source_name": "provider or repository name",
  "source_url": "https://...",
  "observed_at": "2026-01-01T00:00:00Z",
  "retrieved_at": "2026-01-01T00:00:00Z",
  "claim": "exact factual claim supported by the source",
  "evidence_hash": "sha256:...",
  "status": "verified|stale|rejected",
  "provider_event_id": null
}
```

`provider_event_id` is mandatory when the claim concerns a provider-side event such as a click, signup, conversion, commission, payment, payout, deployment, or delivery.

## Revenue evidence ladder

Affiliate/revenue state must progress only through observable evidence:

`configured → reachable → click-observed → signup-observed → conversion-observed → commission-confirmed → payout-confirmed`

A tracking URL, adapter health check, or HTTP 200 response can establish reachability/configuration only. It cannot establish revenue.

## Completion semantics

- `TASK_VERIFIED`: requested work implemented and task-specific acceptance checks passed.
- `NOOP_VERIFIED`: task already satisfied and evidence proves it.
- `PIPELINE_VERIFIED`: infrastructure/practical checks passed but requested task is not proven complete.
- `FAILED`: required execution or verification failed.

`PIPELINE_VERIFIED` must never be promoted to a completion or revenue claim.

## Repository copies

If `PROJECT-STATE-MONY.md` or another project snapshot is retained, it must include a pointer to the canonical `state_revision` and must not introduce contradictory state. Update the canonical state first, then regenerate derived snapshots.

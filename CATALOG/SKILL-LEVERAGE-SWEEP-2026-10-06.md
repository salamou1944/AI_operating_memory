# Skill / Capability Leverage Sweep — 2026-10-06

## Decision

A cross-repository sweep was performed against the current canonical Skills and recent Collection-derived capabilities. The result is **reuse/upgrade/compose, not new-layer creation**.

## High-value findings

| Source capability | Canonical destination | Decision | Why |
|---|---|---|---|
| SOAT runtime verification | `soat-runtime-verification` | REUSE | Already canonical; establishes technical evidence and ENTRY_POINT boundary. |
| SOAT commercial progression | `soat-api-factory-verification` | UPGRADE | Strengthened with CUSTOMER_ACTION → REVENUE → PAYOUT evidence and explicit composition with existing Skills. |
| AI evaluation / backup / observability evidence | `ai-evaluation-evidence` | REUSE/MERGE | Already canonical and covers regression/evaluation evidence. |
| Hikhakk reliability patterns | `multi-modal-provider-gateway` | UPGRADE/MERGE | Preflight, error taxonomy, bounded retry, circuit breaker, idempotency, registry and adapter boundary are already incorporated. |
| Knowledge route selection | `knowledge-route-discovery` | REUSE | Prevents duplicate Skill creation and prioritizes verified existing routes. |
| Business outcome evidence | API Factory evidence contract + AI operating memory | REUSE | Already implemented; technical success is explicitly separated from commercial outcome. |

## No-new-Skill decisions

Do **not** create separate Skills for:
- business-outcome-evidence;
- revenue-evidence-gate;
- SOAT-business-gate;
- provider-retry/circuit-breaker;
- Hikhakk-reliability;
- evaluation-fixture evidence.

These are already covered by canonical Skills or project contracts. Creating parallel Skills would increase semantic duplication and weaken route selection.

## Operating composition

`Goal → knowledge-route-discovery → canonical Skill(s) → Collection provenance if needed → execute → independent verification → business outcome evidence → operating memory`

For commercial work:

`TECHNICAL → ENTRY_POINT → USAGE → CUSTOMER_ACTION → REVENUE → PAYOUT`

Each transition requires its own evidence. Provider health, CI success, synthetic tests, link reachability, or a generated artifact cannot be promoted to revenue.

## Evidence references

- `agent-skills@02161556f399df8240851d7c70f3b7a60438a678`: strengthened `soat-api-factory-verification`.
- Existing `soat-runtime-verification`: technical SOAT evidence boundary.
- Existing `ai-evaluation-evidence`: reproducible evaluation/regression evidence.
- Existing `multi-modal-provider-gateway`: Hikhakk-derived reliability controls.
- Existing `knowledge-route-discovery`: canonical-first routing and anti-duplication.
- `Salamou-31/AI-API-HUB/api-factory/business-outcome-evidence.mjs`: machine-readable business progression.
- `Salamou-31/AI-API-HUB/api-factory/SOAT-SUCCESS-LINK-2026-10-06.md`: SOAT-to-business evidence boundary.

## Limitation

This sweep proves repository-level composition and canonicalization. It does **not** claim a new production revenue event. Runtime and commercial claims remain governed by the evidence ladder above.

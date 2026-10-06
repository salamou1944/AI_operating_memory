# AI Execution Operating Layer

Date: 2026-10-06

## Decision

AI Operating is defined as an **Execution Operating Layer**, not as a new general-purpose agent framework.

Its job is to turn existing verified Skills and authorized resources into observable, evidence-backed outcomes while reusing the existing engineering, API, runtime, and verification systems.

## System boundary

COLLECTION → discover / verify / dedupe → agent-skills (canonical Skills) → AI Execution Operating Layer → select → authorize → bind resources → execute → Elite / ARMY-14 / project runtime / API providers → SOAT + independent verification → AI_operating_memory + evidence / ledger → outcome classification → recover / replan / next task

## Existing-system ownership

| Layer | Owner | Rule |
|---|---|---|
| External discovery/provenance | `Project-/COLLECTION` | Never treated as execution proof |
| Reusable procedure | `agent-skills` | Canonical Skill after dedupe |
| Operating decisions/execution loop | AI Execution Operating Layer | Orchestrates existing components |
| Engineering execution | Elite / ARMY-14 | Reuse existing execution path |
| API/provider services | `Salamou-31` | Reuse API Factory/provider boundary |
| Verification | SOAT + independent verifiers | Must produce task-specific evidence |
| Durable state/evidence | `AI_operating_memory` | Canonical operating state; no application secrets |
| Product/business outcomes | Project-specific repositories | Do not mix product state into operating memory |

## Required run contract

Each material execution must persist:
- task/request ID;
- selected Skill + revision;
- provenance;
- authorization scope;
- resources/providers + revisions where applicable;
- acceptance criteria;
- execution timestamps and mode;
- observed result;
- independent verification;
- evidence/artifact references;
- failure/recovery classification;
- business or engineering outcome;
- next-action/replan decision.

## Outcome model

Technical execution and business outcome are separate dimensions.

Technical maturity:
`DISCOVERED → IMPLEMENTED → UNIT_VERIFIED → INTEGRATION_VERIFIED → RUNTIME_VERIFIED → PROVIDER_VERIFIED → E2E_VERIFIED → BUSINESS_FLOW_VERIFIED`

Business outcome:
`DISCOVERED → ENTRY_POINT_VERIFIED → USAGE_OBSERVED → CUSTOMER_ACTION_OBSERVED → REVENUE_OBSERVED → PAYOUT_OBSERVED`

A technical success cannot be promoted to a business outcome without the corresponding evidence.

## Replanning rule

Replanning is allowed only from persisted, verified state.

A failed run must preserve failure evidence, failure class, retryability, attempted remediation, verifier result, and remaining blocker.

The system must never convert a failed or unverified result into success through status mutation.

## Resource selection

The layer should prefer:
1. existing canonical Skills;
2. existing project/runtime capabilities;
3. existing providers and free/self-hosted paths where legitimately available;
4. the smallest external adapter necessary to close a verified gap.

Do not add a framework, gateway, registry, or control plane when an existing component already owns that boundary.

## Security

Execution remains least-privilege and fail-closed.

No automatic authority is granted for credentials or secrets, unrestricted filesystem mutation, unrestricted network access, destructive database operations, production deployment, payment/financial authorization, CAPTCHA/MFA/authentication bypass, or unauthorized external-state changes.

## Success criterion

AI Operating is considered ready for this architecture only when a real end-to-end cycle can demonstrate:

`Skill selection → authorized execution → real result → independent verification → persisted evidence → outcome classification → next-task/replan decision`

A healthy service, passing CI job, queue acknowledgement, or provider reachability signal alone is insufficient.

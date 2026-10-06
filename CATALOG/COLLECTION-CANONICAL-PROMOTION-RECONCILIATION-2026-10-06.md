# Collection Canonical Promotion Reconciliation — 2026-10-06

## Scope

Reconciled the highest-value current entries in `COLLECTION/MASTER/PROMOTION-QUEUE.json` against the canonical `agent-skills` layer. The generated queue is a discovery queue and can remain stale until the next extraction run; this record is the authoritative decision evidence for the entries handled here.

## Decisions

| Candidate | Source | Decision | Canonical target | Reason |
|---|---|---|---|---|
| `agent-orchestration-agents-commands-runbook` | `Panniantong/skillshare`, `ai_docs/tests/agents_commands_runbook.md`, ref `main`, blob `60c19ceaa202e1862d7dae047457a4131cf8ebb2` | MERGE | `agent-skills/skills/ai-evaluation-evidence` | This is evaluation/runbook evidence for agent lifecycle, JSON output, sync, diff, collect, uninstall, trash, restore, backup and doctor behavior; it does not justify a new orchestration Skill. |
| `agent-orchestration-agent-backup-test` | `Panniantong/skillshare`, `tests/integration/agent_backup_test.go` | MERGE | `agent-skills/skills/ai-evaluation-evidence` | Already incorporated into the canonical evaluation/evidence Skill; preserve source provenance only. |
| `agent-orchestration-agent-observability-test` | `Panniantong/skillshare`, `tests/integration/agent_observability_test.go` | MERGE | `agent-skills/skills/ai-evaluation-evidence` | Already incorporated into the canonical evaluation/evidence Skill; preserve source provenance only. |
| `HIKHAKK reliability patterns` | `Hikhakk/higgsfield-mcp-unified`, MIT, captured in `COLLECTION/SKILLS/HIGGSFIELD_RELIABILITY_PATTERNS_2026-10-06.md` | UPGRADE/MERGE | `agent-skills/skills/multi-modal-provider-gateway` | Provider preflight, error taxonomy, bounded retry, circuit breaker, idempotency, provider/model registry, capability selection, structured output, adapter boundary and cheap evidence smoke strengthen an existing provider-neutral gateway rather than creating ten duplicate Skills. |
| low-value generated algorithm/test/documentation entries | multiple Collection sources | REFERENCE | no new Skill | A test file, generated document, algorithm example, or repository-specific fixture is not automatically a reusable canonical operational Skill. Keep as provenance unless a concrete cross-project procedure is extracted and validated. |

## Verification evidence

- Existing canonical evaluation Skill already contains agent backup/restore and observability regression guidance.
- Existing canonical provider gateway was updated in commit `eb112425db210e6335a018a7c5a138ec2439f2a0` with the Hikhakk reliability patterns.
- Hikhakk source is MIT; the experimental private-web-backend path remains excluded.
- No third-party application code was copied into executable Skills.
- No new parallel capability registry or readiness taxonomy was created.

## Remaining queue handling rule

Do not mass-promote the remaining queue by score alone. Continue in descending practical value, but require semantic dedupe against canonical Skills and the two-axis Collection rule. Generated tests/docs that merely describe a repository implementation should normally become provenance/evidence, not new Skills. New Skills require a concrete reusable procedure that is not already covered, followed by deterministic validation and provenance.

## Canonical flow

COLLECTION -> semantic dedupe -> canonical Skill MERGE/UPGRADE/NEW/REFERENCE -> validation -> project execution -> independent evidence -> VERIFIED/READY state.

Collection evidence remains provenance and discovery; it is never production proof.
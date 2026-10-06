# Evaluation Fixture Contract Implementation — 2026-10-06

## Status
EXECUTED

## Decision
The existing fixture pattern in `Salamou-31/AI-API-HUB` was extended into a provider-neutral `evaluation-fixture/v1` contract rather than creating another evaluation Skill.

## Evidence
- Existing reusable fixture precedent: `free-provider-policy-fixture.json` + isolated contract test.
- Existing regression/evidence precedent: `api-factory/business-outcome-evidence.mjs` + test.
- New schema: `Salamou-31/AI-API-HUB/evaluation-fixture.schema.json`
- New contract test: `Salamou-31/AI-API-HUB/test-evaluation-fixture-contract.mjs`
- The schema requires task contract, dataset revision/case IDs, system commit, model/configuration, rubric/thresholds, run metadata, results, failures and invalid cases.
- Optional comparison records baseline/variant, paired deltas and regression status.

## Canonical Skill integration
`agent-skills/skills/ai-evaluation-evidence/SKILL.md` now references the contract as the machine-readable evidence shape.

## Boundary
The schema standardizes evidence structure; it does not claim that an evaluation ran. Execution proof still requires an actual test/evaluation run and preserved artifacts.

## Safety
No credentials, tokens, private data, or provider secrets are permitted in the fixture contract.

## CI note
The new Salamou-31 commits currently show an EASY Runtime Production check in PENDING state. No evaluation execution is claimed from that status.

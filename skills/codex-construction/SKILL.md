---
name: codex-construction
 description: Orchestrate Codex as an autonomous construction worker using explicit contracts, bounded batches, effort tiers, monitoring, acceptance packets, and independent review.
license: MIT
---

# Codex Construction

Use when delegating implementation work to Codex CLI or a compatible construction agent.

## Division of responsibility

- Controller: defines the solution contract, scope, red lines, batch boundaries, acceptance criteria, monitoring, and final acceptance.
- Codex: owns implementation inside one batch, runs required gates, commits staged work, and produces an acceptance packet.
- Controller does not micromanage implementation details; Codex does not make product-level decisions outside the contract.

## Effort selection

- `medium`: well-specified local implementation, mechanical cleanup, known root-cause fix.
- `high`: cross-module work, unknown root cause, architecture-sensitive work, full-batch review.
- `xhigh`: architecture changes, security/concurrency/money-critical work, adversarial final review.

Review effort must be at least the construction effort. If a batch fails because the contract left too much design latitude, redesign the contract or raise the tier rather than endlessly retrying.

## Batch contract

Every batch defines:

1. Site: repository, branch, and known state.
2. Contract: the authoritative design/acceptance document.
3. Scope: what is included and explicitly excluded.
4. Red lines: concrete boundaries such as no production deployment or no destructive migration.
5. Delivery: staged commits plus an acceptance packet containing goal, diff summary, deletions, tests, and unverified items.

Autonomous execution should continue on low-risk ambiguity. Stop only when the decision would invalidate the contract or cross a red line.

## Lifecycle

`contract -> batch -> construct -> gates -> acceptance -> independent review -> targeted repair -> final verification`

Use independent fresh-context review when practical. The reviewer should not silently modify the implementation. Repairs can resume the construction context only when that improves continuity.

## Failure handling

- No delivery: classify before retrying.
- Blocked by a contract assumption: resolve at the controller layer.
- Repeated failure or oscillation: stop and revisit the design instead of adding more retries.
- Controller must independently rerun critical gates; never trust a claimed `passed` without evidence.

## Safety

Do not weaken sandbox, approval, repository, deployment, or secret protections merely to make automation succeed. Any privileged execution must be an explicit, reviewed decision outside this skill.

## Source

Distilled from shengyy/agent-skills `codex-construction`, MIT licensed: https://github.com/shengyy/agent-skills
Original project: shengyy/agent-skills. This file is an adaptation for the AI Operating Memory catalog.

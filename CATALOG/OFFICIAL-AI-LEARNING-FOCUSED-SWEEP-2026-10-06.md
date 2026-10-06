# Focused Official AI Learning Sweep — 2026-10-06

Status: EXECUTED

## Scope

Continued the official-source sweep after the initial learning-source registry, focusing on:
1. Codex engineering workflow governance.
2. Agent context and handoff reliability.
3. RAG evaluation.
4. Model/benchmark provenance.
5. Production cost, latency, and reliability optimization.

## Verified source signals

OpenAI Academy currently provides Codex practical workflows and advanced automation material, and its builder guidance emphasizes repository scoping, verification, review evidence, and reusable workflows. Hugging Face's Agents Course includes explicit agent evaluation against the GAIA benchmark. These signals support governed engineering workflows and evidence-based evaluation rather than prompt-only guidance.

## Dedupe and promotion decisions

### UPGRADE — ai-evaluation-evidence

Promoted into the existing canonical Skill:
- RAG-specific retrieval-versus-generation evaluation.
- Retrieval fixture/corpus/chunk/index provenance.
- Model and benchmark provenance requirements.
- Baseline-versus-variant comparison discipline.
- Quality/cost/latency/reliability trade-off gates.
- Tail-latency and stage-level optimization guidance.

Reason: these capabilities are extensions of the existing evaluation/evidence contract and do not justify separate duplicate Skills.

### UPGRADE — agentic-orchestration

Promoted into the existing canonical Skill:
- minimum durable context for handoffs;
- explicit decisions, constraints, evidence, blockers, next action, and acceptance test;
- durable-artifact-over-transcript rule;
- receiver-side continuation test;
- handoff state is not execution proof.

Reason: handoff reliability is a direct extension of bounded orchestration and checkpoint/reconciliation behavior.

### NEW — codex-engineering-workflow

Created a distinct canonical Skill for the Codex-specific engineering lifecycle:
scope -> inspect -> plan -> bounded implementation -> focused tests -> diff review -> evidence -> completion.

Reason: this is a reusable provider-specific workflow layer for Codex-assisted software work, distinct from general multi-agent orchestration and provider-neutral evaluation.

## Evidence

- agent-skills/skills/ai-evaluation-evidence/SKILL.md
  Commit: caa1197b1c4b6b840cba80565ccc04b11b4e4f2c
  Blob: 728bfc563174339ba6f30ffac0efa9ffc03efc39
- agent-skills/skills/agentic-orchestration/SKILL.md
  Commit: da071daa0dc0f96b32623a300bb6d33854dc2773
  Blob: badfa2b2ee8e0c903a4ad7b2ec35848454dfa8b6
- agent-skills/skills/codex-engineering-workflow/SKILL.md
  Commit: 8a0cb6b63ef4aa729907d0d4bc459216373ee85d
  Blob: 1803d503af2f4cbc80b1a2798b78383b021a0961

All three files were fetched after mutation and their expected content was verified.

## Boundary

No workflow execution or deployment is claimed from these Skill writes alone. Skills are canonical reusable procedure; runtime/CI evidence remains separate.

# Official AI Learning Sweep — 2026-10-06

## Status

EXECUTED: official-source sweep performed against the registered learning-source set.

VERIFIED signals:
- OpenAI Academy currently exposes applied AI workflows, agents/workflows, evaluation, agentic systems, RAG, performance optimization, and governed Codex workflows. citeturn0search4turn0search3
- Hugging Face Learn currently includes an Agents course covering agent design/practice, established agent libraries, Hub publication, and agent evaluation challenges. citeturn0search15turn0search14
- Claude Academy currently covers human-agent teams, skills, agent building, prompt/context/evals, and model capability/limitation awareness. citeturn0search2turn0search8
- AWS Skill Builder currently emphasizes production-ready AI training and hands-on architecture/build workflows. citeturn0search11

## Dedupe result

### UPGRADE / MERGE — existing canonical Skills
1. `ai-evaluation-evidence`
   - Merge signal: evaluation cases, rubrics, failure analysis, regression prevention, traces/observability.
   - Existing Skill already covers provider-neutral evaluation, tool-use signals, regression evidence, and agent reliability.
   - Action: no duplicate Skill created.

2. `agentic-orchestration`
   - Merge signal: bounded agent delegation, roles, handoffs, checkpoints, controlled tools, verified completion.
   - Existing Skill already covers decomposition, bounded objectives, checkpoints, reconciliation and deterministic verification.
   - Action: no duplicate Skill created.

### REFERENCE / FUTURE EXTRACTION
- OpenAI Academy: Codex governed-team workflows, RAG, production optimization.
- Hugging Face Learn: open-agent implementation patterns and evaluation/benchmark workflows.
- Claude Academy: human-agent team operating model and context/skills/evaluation patterns.
- AWS Skill Builder: production architecture and hands-on deployment learning.
- Remaining NVIDIA, Microsoft, DeepLearning.AI, IBM, Google and Meta sources remain registered for subsequent focused sweeps; no unsupported promotion is made from portal names alone.

## Decision

No new canonical Skill is promoted in this sweep. The strongest verified signals are already covered by existing canonical Skills. New Skills require a genuinely distinct reusable contract plus validation evidence.

## Next sweep targets

1. Codex workflow governance/performance.
2. Agent context and handoff reliability.
3. RAG quality/evaluation.
4. Model/dataset evaluation and benchmark provenance.
5. Production AI cost/latency/reliability optimization.

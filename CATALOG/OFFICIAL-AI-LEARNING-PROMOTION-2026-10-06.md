# Official AI Learning Sweep — Promotion Decision — 2026-10-06

## Net-new canonical Skill promoted

### ai-evaluation-evidence

The official-source sweep identified a concrete reusable mechanism that materially strengthens the existing evidence-first architecture: a provider-neutral evaluation contract covering datasets/cases, explicit metrics and thresholds, reproducible rubrics, agent tool-use signals, variant comparison, regression testing, and evidence retention.

This was promoted to:

agent-skills/skills/ai-evaluation-evidence/SKILL.md

Commit: 1920a25c2f78db05c0eba93dc3243efc26ab380f

Verified by reading the file from main after creation.

## Source signals

- Hugging Face Agents Course: agent fundamentals, tools/actions, agent workflow, final testing/certification, and observability/evaluation. 
- Microsoft Learn: structured agent evaluation with quality/cost/performance metrics and Git-based experiment comparison.
- Microsoft Learn: generative-AI evaluation using real, synthetic, and adversarial data, custom evaluators, metrics, and mitigation.
- Microsoft Learn: automated evaluation integrated into GitHub Actions for continuous quality assurance.
- Microsoft Learn: agent evaluators for tool selection, tool input/output use, call success, relevance, abstention, completeness, groundedness and context coverage.

## Dedupe decision

Existing agent-skills already contain broad orchestration, review, verification, research, multimodal and provider-gateway coverage. The new Skill therefore does not create vendor-specific Skills for OpenAI, NVIDIA, Hugging Face, Microsoft, Anthropic, AWS, Meta, Google, IBM, or DeepLearning.AI.

Instead, their reusable evaluation mechanism is consolidated into one provider-neutral canonical Skill.

## Next sweep targets

Continue extracting only implementation-relevant, net-new mechanisms from the ten official sources. Prioritize:
1. evaluation/reliability
2. agent observability
3. model/provider routing
4. multimodal quality
5. production AI operations
6. accelerated inference/optimization
7. dataset/model provenance

Do not turn learning consumption itself into a project. Promotion requires a concrete reusable mechanism and evidence of net-new value.

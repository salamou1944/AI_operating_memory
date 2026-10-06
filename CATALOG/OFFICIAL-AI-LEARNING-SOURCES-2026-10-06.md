# Official AI Learning Source Sweep — 2026-10-06

## Purpose

Treat the supplied learning portals as **Collection sources** for extracting reusable knowledge, workflows, evaluation patterns, and provider-neutral capabilities. They are not automatically converted into executable Skills and are not treated as proof of capability merely because a course exists.

## Sources reviewed

| Source | Official portal | Collection value | Initial priority |
|---|---|---|---|
| OpenAI | academy.openai.com | AI foundations, applied AI workflows, agents/workflows, Codex/API building | Tier 1 |
| NVIDIA | developer.nvidia.com/training | GPU/AI infrastructure, accelerated computing, model deployment and optimization | Tier 1 |
| Hugging Face | huggingface.co/learn | open models, datasets, evaluation, transformers, agents and practical ML | Tier 1 |
| Microsoft | learn.microsoft.com/training | AI engineering, Azure AI, agents, APIs, cloud deployment, security and developer workflows | Tier 1 |
| Anthropic | anthropic.skilljar.com | Claude usage, prompting, agent/workflow patterns and model-oriented development | Tier 1 |
| DeepLearning.AI | deeplearning.ai | practical AI/ML, agents, LLM applications, evaluation and applied workflows | Tier 1 |
| IBM | skillsbuild.org | free AI, cybersecurity, data, generative AI, prompt engineering and career-oriented learning | Tier 1 |
| Google | grow.google/ai | AI literacy and practical AI learning | Tier 2 |
| AWS | skillbuilder.aws | cloud AI/ML, production architecture, services and operational patterns | Tier 1 |
| Meta | ai.meta.com/resources | open-source AI frameworks, models, datasets, demos, system cards and research | Tier 1 |

## Evidence checked

- OpenAI Academy currently exposes AI foundations, applied AI foundations, agents/workflows, and building-with-AI material; its courses are free and self-paced. 
- Microsoft Learn provides interactive modules and learning paths, including generative AI, agents, Azure AI and developer topics.
- IBM SkillsBuild states that its AI/technology learning is free and includes generative AI, cybersecurity, data and prompt-engineering material.
- Meta AI Resources provides official frameworks/tools, models/libraries, datasets, demos, system cards and publications.

## Operating rule

Learning portal -> extract capability/knowledge signal -> verify source and applicability -> dedupe against existing canonical Skills -> distill provider-neutral reusable Skill when justified -> add evidence/QA -> integrate only where it advances a real project.

## Dedupe / promotion candidates

The supplied portals should primarily strengthen existing coverage rather than create ten vendor-specific Skills. Likely reusable capability families are:

1. AI workflow and agent design
2. LLM application engineering
3. Evaluation and reliability
4. Prompting/instruction design
5. Multimodal generation and processing
6. Model/provider routing
7. AI security and responsible deployment
8. GPU/accelerated inference and optimization
9. Data/model/dataset evaluation
10. Production AI/cloud architecture

Existing skills should be preferred whenever they already cover the same reusable mechanism.

## Product leverage

Highest direct leverage for current portfolio:
- EASY: multimodal creative generation, evaluation, media QA, provider-neutral routing.
- Salamou-31: API design, model routing, evaluation, production AI patterns.
- AI_operating_memory / agent-skills: agent workflows, evidence, evaluation, security, skill admission and deduplication.
- SOAT: verification/evidence patterns where training material yields reusable implementation rules.
- Revenue work: use learning only when it produces a concrete acquisition, automation or sellable capability; avoid turning learning into a distraction.

## Safety / provenance

Official training content is a knowledge source, not an unrestricted execution authority. Do not copy proprietary course material wholesale. Distill concepts into original Skills, preserve attribution/provenance where material is derived, and respect provider terms. Never use training material to bypass authentication, quotas, safety controls, privacy boundaries or other provider protections.

## Status

Collection source layer: ADDED.
Canonical Skill promotion: DEFERRED until dedupe identifies a concrete reusable mechanism not already covered.
Next action: sweep these sources for high-value, implementation-relevant capabilities and promote only net-new canonical Skills.

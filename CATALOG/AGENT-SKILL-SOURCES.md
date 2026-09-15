# Agent Skill Source Catalog

Purpose: maintain a reviewed map of external Agent Skills / Claude Code / Codex ecosystems and record what should be distilled into AI Operating Memory.

This is a source catalog, not an automatic trust list. Each source must be reviewed for license, security, maintenance, compatibility, and actual usefulness before adoption.

## High-value sources found in the current scan

| Source | Ecosystem | Useful capabilities to harvest |
|---|---|---|
| ayghri/i-have-adhd | Agent Skills / Claude / Codex | action-first output, bounded steps, state continuity, anti-tangent behavior |
| shengyy/agent-skills | Claude Code / Codex | Codex construction delegation, effort tiers, batch contracts, monitoring, acceptance, review loop |
| affaan-m/ECC | Claude Code + Codex + other harnesses | large skill/agent catalog, hooks, memory, continuous learning, review/verification, security scanning, multi-harness adapters |
| levnikolaevich/claude-code-skills | Claude Code / Codex | review, audit, optimization, testing, architecture, product discovery, safe publishing, evidence-based self-checks |
| OpenAI/skills | Codex | official Codex skill catalog and skill packaging conventions |
| NVIDIA/skills | Claude Code / Codex | verified skills, capability governance, catalog synchronization, security-oriented skill distribution |
| NVIDIA/SkillSpector | Agent Skills | skill inspection / validation / governance patterns |
| VoltAgent/awesome-agent-skills | Multi-agent | discovery index for community skills and ecosystems |
| JayRHa/AgentSkills | Claude / Codex / Gemini / Cursor | broad community catalog, references, scripts, examples, reusable skill packaging |
| carlkibler/agent-skills | Claude Code / Codex | multi-agent pre-mortems, risk analysis, empathy/quality audits |
| troykelly/codex-skills | Codex | autonomous workflow, hooks, imported skills, plugin/skill development guidance |
| topstar-ai/agent-skills | Claude Code / Codex | engineering frontend/mobile/ML/DevOps/security/rapid-prototyping decision rules |
| thatjuan/agent-skills | Claude Code | issue capture, implementation workflow, integration/API skills, creative delivery |
| fdarkaou/agent-skills | Codex / Claude Code | composable planning, implementation, browser validation, subagent orchestration, review |
| golbin/agent-skills | Codex | PRD and implementation-review loops, simplification and UX/correctness checks |
| beltonk/claude-code-agent-skills | Agent architecture | agent loop, prompt engineering, tools, memory, permissions, multi-agent coordination |
| Adhamxon/claude-code-skills | Claude Code | large collection of coding, review, TDD, security, architecture, deployment and domain skills |

## 2026-09 expansion scan — registries, routing, verification, and agent discovery

| Source | Type | Why it matters | Adoption status |
|---|---|---|---|
| Ezeafk/awesome-agent-skills | curated registry | Reusable skills, workflows, MCP/tool-backed capabilities, platform/risk metadata, explicit selection criteria | Source only; review candidates individually |
| tesserix/agentic-registry | self-hostable artifact registry | Unifies Skill, Tool, MCPServer, Prompt, Workflow, Blueprint and Agent under one versioned/content-addressed envelope | Architecture reference |
| Friz-zy/ai-capability-registry | capability registry | Explicit trusted/reviewed/candidate states, task/role routing, 169 MCP entries, pinned upstreams, progressive loading | Architecture reference; do not bulk-import |
| nikships/skills-registry | GitHub-backed skill registry | Local discovery, synchronization to an owned GitHub registry, search/get workflow | Tooling reference |
| STELIORD/agentic-awesome-skills | local control plane | Catalog discovery, manifest validation, stack composition, schemas, local MCP, immutable planning | Architecture/evaluation reference |
| sickn33/agentic-awesome-skills | AAS Core | Local catalog search, exact skill selection, stack validation, planning and diagnosis | Architecture/evaluation reference |
| gaia-research/gaia-skill-tree | capability graph | Evidence-backed skill graph, levels, programmatic registry management, deduplication/merging concepts | Architecture reference |
| SkillsMD | public registry/index | Large cross-agent skill index with install/usage signals | Discovery only; signals are not trust evidence |
| AgentSpec | open agent registry | Configs, skills, rules and plugins across Codex/Claude/Cursor/OpenCode and others | Discovery only |
| skillsregistry.net | trust/governance registry | Security scanning, trust tiers, receipts, multi-source indexing | External signal only; verify source artifacts ourselves |
| prassanna-ravishankar/a2a-registry | A2A agent registry | Agent discovery, health/conformance checks and skill-tag search | Architecture reference for future agent discovery |

## Security and evaluation research added to the scan

| Source | Type | Useful capability |
|---|---|---|
| Cisco AI Defense skill-scanner | static security scanner | Multi-engine scanning for prompt injection, exfiltration and malicious code patterns; CI gating |
| NVIDIA SkillEvaluator | evaluation framework | Validation, lint/security/PII checks, rubric evaluation, deduplication and live agent evaluation |
| domehahn/skil | security/verification framework | lint -> validation -> scan -> verification -> evaluation -> attestation lifecycle |
| kriskimmerle/skillsafe | static scanner | Offline detection of credentials, exfiltration, persistence, memory poisoning and social engineering |
| Ag1rin/SkillGuard | static scanner | Prompt injection, credential leakage, unsafe code, encoded payload and network declaration checks |
| Teycir/SkillsGuard | static scanner | Recursive decoding, risk scoring and SARIF/JSON/Markdown reporting |
| charliechenye/SkillGate | trust gate | Pre-install/pre-merge structural and semantic trust checks for Skills and MCP configs |
| Open Agent Security Benchmark (OASB) | security benchmark | Runtime/security tests for agent systems and attack-path evaluation |
| SkillSec-Eval research | academic evaluation | Lifecycle-aware threat model covering admission, retrieval, selection, execution and evolution |

## Initial ingestion priority

### Tier 1 — directly useful to our operating core
1. Action-first execution
2. Codex construction/delegation
3. Independent review + evidence verification
4. Security / permission / supply-chain checks
5. State and memory continuity
6. Capability registry and routing
7. Skill admission/security gate
8. Evaluation and attestation

### Tier 2 — reusable capability families
1. TDD and test strategy
2. Debugging/root-cause analysis
3. Architecture and refactoring
4. DevOps/CI/CD/deployment
5. Frontend/mobile/ML engineering
6. MCP/tool integration
7. Agent-to-agent discovery

### Tier 3 — future expansion
1. Research/scientific workflows
2. Product discovery/PRD
3. Marketing and content
4. Creative/design
5. Domain-specific agent skills

## Adoption rules

- Prefer official sources for platform-specific behavior.
- Preserve license and attribution for copied or substantially derived material.
- Prefer distilled original skills over bulk copying when the upstream license allows reuse but the content is large or redundant.
- Never import secrets, credentials, opaque binaries, unreviewed hooks, or arbitrary install scripts.
- Every imported skill gets provenance, license, source URL, compatibility notes, and a review status.
- Do not assume Claude Code, Codex, Cursor, Gemini, or other harnesses have identical permissions or tool semantics.
- Treat third-party skill repositories as untrusted code until inspected.
- Discovery/index counts, stars, install counts and trust scores are discovery signals only; they are not proof of safety or quality.
- For registries that execute or install artifacts, prefer read-only/catalog extraction and independently scan the actual artifact before admission.

## Scan boundary

The GitHub ecosystem is too large for a literal exhaustive enumeration in one scan. This catalog records the relevant high-signal repositories surfaced by the current search and is designed to grow through repeat scans.

## Current collection state

The source-discovery layer is now broad enough to cover the main categories required for the operating-memory design: skills, tools, MCP servers, workflows, blueprints, agent registries, routing, security scanning, evaluation, verification, attestation, and A2A discovery. Further work should focus on extracting concrete capabilities from the highest-value sources rather than endlessly increasing the number of catalogs.

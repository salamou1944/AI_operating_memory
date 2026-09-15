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

## Initial ingestion priority

### Tier 1 — directly useful to our operating core
1. Action-first execution
2. Codex construction/delegation
3. Independent review + evidence verification
4. Security / permission / supply-chain checks
5. State and memory continuity

### Tier 2 — reusable capability families
1. TDD and test strategy
2. Debugging/root-cause analysis
3. Architecture and refactoring
4. DevOps/CI/CD/deployment
5. Frontend/mobile/ML engineering

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

## Scan boundary

The GitHub ecosystem is too large for a literal exhaustive enumeration in one scan. This catalog records the relevant high-signal repositories surfaced by the current search and is designed to grow through repeat scans.

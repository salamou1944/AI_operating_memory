# Capability Collection Round — 2026-09-16

## Scope
This round expanded the capability search beyond ordinary skill catalogs into:
- skill registries and cross-harness packaging;
- security scanners and admission gates;
- skill evaluation and benchmarking;
- agent observability and regression workflows;
- MCP discovery/registry infrastructure;
- memory/context infrastructure;
- agent routing/orchestration;
- authorized red-team/security-assessment skills and security-review skills;
- dangerous-capability discovery, retained as knowledge-only references rather than enabled execution.

## Newly recorded high-signal sources

| Source | Capability | License/status evidence | Archive treatment |
|---|---|---|---|
| NVIDIA/SkillSpector | Agent-skill security scanning, vulnerability/malicious-pattern detection, supply-chain checks | Apache-2.0 source license | Candidate for security-gate integration; inspect before adoption |
| NVIDIA/skills | Verified skills catalog, skill packaging, validation, governance/signing pipeline | Skills/docs CC-BY-4.0; source code Apache-2.0 | Catalog/provenance source; copy only license-compatible material |
| Codagent-AI/agent-skills | Portable Claude/Codex/Cursor software-engineering workflow | MIT | Candidate for distilled engineering workflows |
| agents-repo/registry | Cross-harness agent/skill/workflow/runtime registry | MIT | Architecture and registry reference |
| tardigrde/agent-skill-eval | End-to-end skill evaluation through real harnesses | MIT | Candidate for evaluation layer |
| TiesPetersen/SkillBenchmark | With-skill vs without-skill benchmarking, repeated runs, confidence intervals | MIT | Candidate for quantitative skill evaluation |
| magnus919/agent-skills | Vendor-neutral eval/observability and secure engineering skills | MIT | Candidate for distilled methodology |
| datadog-labs/agent-skills | Agent observability, RCA, evaluator/bootstrap, experiment pipelines | Source review required | Candidate; inspect each skill individually |
| pubky/agent-skills | Cross-harness Claude/Codex/Cursor skills and plugin packaging | License file present; inspect exact terms before copying | Catalog/candidate |
| Cisco AI Defense/skill-scanner | Multi-engine static/AST/dataflow/LLM skill security scanning | Open-source repository; inspect license before redistribution | Security-gate reference |
| kriskimmerle/skillsafe | Offline static scanner for credentials, exfiltration, persistence, memory poisoning | Open-source repository; inspect license before redistribution | Security-gate candidate |
| Ag1rin/SkillGuard | Static prompt-injection/credential/unsafe-code scanner | Open-source repository; inspect license before redistribution | Security-gate candidate |
| RudrenduPaul/skillguard | Cross-skill privilege-chain analysis and marketplace typosquatting checks | Open-source repository; inspect license before redistribution | Security-gate reference |
| dkleptsov/skill-security-review | Static audit of network/process execution/install scripts/MCP/symlinks | Apache-2.0 | Security-gate candidate |
| superagent-ai/skills/skill-security | Static + semantic skill security audit methodology | License requires individual review | Candidate methodology; no automatic execution |
| opena2a-org/oasb | Agent-security benchmark with standardized attack scenarios and ATLAS mapping | Open-source; inspect license/benchmark terms | Knowledge/evaluation reference |
| Official MCP Registry | Registry/discovery of MCP servers, versions, validation and health endpoints | Registry terms/docs reviewed separately | Discovery source; every server independently vetted |
| keshrath/agent-discover | MCP discovery/activation/registry proxy | Open-source; inspect license | Architecture reference; no auto-install |
| io.github.n24q02m/mnemo-mcp | Persistent AI memory via MCP | Registry listing; source/license require independent review | Discovery candidate |
| io.github.vshulcz/deja-vu | Local memory across multiple coding agents | Registry listing; source/license require independent review | Discovery candidate |
| io.github.YawLabs/ctxlint | Context-file linting against actual codebase | Registry listing; source/license require independent review | Candidate for context integrity |

## Dangerous / very-dangerous capability discovery

The round also found public skills covering red-team planning, penetration-testing methodology, recon, adversarial security testing, and offensive-security workflows. Examples include:
- neurofoo/agent-skills redteam;
- agent-skills-hub/agent-skills-hub red-team-tools;
- borghei/Claude-Skills engineering/red-team;
- superagent-ai/skills recon-security;
- HoangNguyen0403/agent-skills-standard pentest;
- NeoTheCapt/RedteamAgent;
- audn-ai/skills adversarial testing;
- orq-ai/assistant-plugins orq-red-team.

These are retained as **KNOWLEDGE-ONLY / RESTRICTED references** for capability mapping and security review. No live-target execution, credential acquisition, persistence, exploitation payload deployment, or unauthorized access is enabled by this archive.

## Findings from the collection

1. Skill repositories are increasingly distributed as portable packages across Claude Code, Codex, Cursor, Gemini, OpenCode and other harnesses.
2. Security scanning is becoming a distinct admission layer rather than a final manual review.
3. Evaluation is moving from static prompt quality toward real-harness, state-diff, regression, trajectory and observability testing.
4. Registries are expanding from skills alone to tools, MCP servers, agents, workflows, blueprints and runtime specifications.
5. MCP discovery is now a major capability source, but registry presence is not trust evidence.
6. Cross-skill composition creates risks that single-skill scanning can miss; privilege-chain analysis should therefore be part of our gate.
7. Context/memory integrity is an explicit security surface and must be scanned like code and configuration.
8. Dangerous capability discovery is useful for threat modeling and capability mapping, but storage and execution must remain separate.

## Collection rule

Do not treat this round as exhaustive enumeration of the entire public ecosystem. It is a completed high-signal expansion pass. Future rounds should deepen the highest-value sources, retrieve exact versions/licenses, inspect files, compute hashes, and admit only reviewed capabilities rather than endlessly growing a name list.

## Evidence captured during round

- Cisco AI Defense skill-scanner: multi-engine static/dataflow security scanning.
- NVIDIA SkillSpector: Apache-2.0 licensed security scanner and verified-skills pipeline reference.
- Codagent Agent Skills: MIT-licensed portable software-development workflow.
- agents-repo/registry: MIT-licensed cross-harness registry.
- tardigrde/agent-skill-eval: MIT-licensed real-harness evaluation framework.
- TiesPetersen/SkillBenchmark: MIT-licensed quantitative benchmark.
- Official MCP Registry: live registry with server versions, validation and health documentation.
- Open Agent Security Benchmark: standardized agent-security scenarios and evaluation harness.

## Status

Collection round completed for the current search scope. No user credentials, API keys, private keys, or secret values were collected.

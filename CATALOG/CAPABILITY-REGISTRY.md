# AI Operating Memory — Capability Registry

Purpose: maintain a broad inventory of capabilities found in agent/skill ecosystems without silently enabling unsafe execution.

## Capability classes

### A — SAFE / ENABLED
Capabilities that can be stored and used when technically compatible:
- action-first execution discipline
- task decomposition and state tracking
- planning and implementation workflows
- code generation and refactoring
- code review and test generation
- debugging and root-cause analysis
- documentation and knowledge extraction
- repository navigation and change management
- Git/GitHub workflows
- CI/CD diagnosis and verification
- API design and integration
- frontend/backend/database architecture
- performance analysis
- accessibility and UX review
- product/content workflows
- research and source evaluation
- project planning and pre-mortems
- second-opinion and independent review workflows
- memory/context management
- continuous-learning patterns
- agent routing/orchestration
- skill discovery, validation, provenance and deduplication
- security review, threat modeling and defensive hardening
- supply-chain and dependency auditing
- AI-system security review
- incident analysis and defensive detection engineering

### B — RESTRICTED / STORED, NOT AUTO-ENABLED
Capabilities may be catalogued for future controlled use, but their executable instructions/tools are not activated automatically:
- shell commands with destructive potential
- unrestricted filesystem mutation
- arbitrary network access
- deployment to production
- secret/credential handling
- database destructive operations
- privileged infrastructure changes
- autonomous agent spawning with broad permissions
- browser automation that can transact or change external state
- package installation with untrusted sources
- security testing against real targets
- cloud-account administration
- access-control changes
- automated PR merge/release/publish actions

These entries should retain: source, license, intended scope, required permissions, hazards, and verification status.

### C — DANGEROUS / KNOWLEDGE-ONLY
These capabilities can be indexed as concepts and defensive review material, but are never copied into an automatically executable skill or granted unrestricted execution:
- credential/password cracking
- exploit execution against targets
- privilege escalation procedures
- malware creation or deployment
- persistence/evasion mechanisms
- destructive payloads
- unauthorized reconnaissance or target interaction
- data exfiltration mechanisms
- credential/token theft
- ransomware or destructive automation
- weaponized exploit chains
- bypassing authentication/access controls
- stealth/anti-forensics intended to conceal unauthorized activity

For this class the repository stores capability metadata and safety boundaries, not a ready-to-run offensive playbook.

## Required metadata for every imported capability

1. Name and source repository
2. Original author/organization
3. Source URL
4. License and redistribution status
5. Capability category
6. Runtime/tool permissions required
7. Network requirements
8. Filesystem requirements
9. Secret/credential requirements
10. Security classification: A/B/C
11. Verification/evaluation evidence
12. Adaptation notes for AI_operating_memory
13. Known conflicts or duplication
14. Last reviewed date

## Core principle

Broad knowledge coverage does not require broad execution authority. The memory may know that a dangerous capability exists, how to recognize it, how to audit it, and how to defend against it without granting the agent unrestricted ability to perform it.

## Reference ecosystems reviewed

- i-have-adhd / action-first agent workflow
- ECC / agent harness and engineering workflow ecosystem
- OpenAI/Codex skills ecosystem
- Claude Agent Skills ecosystem
- NVIDIA Agent Skills
- Carl Kibler agent-skills
- jakenuts agent-skills
- SECS security Agent Skills

Sources are recorded separately in `CATALOG/AGENT-SKILL-SOURCES.md`.

---
name: external-skill-review
description: Review external AI-agent skills before ingestion: provenance, license, security, compatibility, evidence, duplication, and adoption decision.
license: MIT
---

# External Skill Review

Use before importing a third-party skill, agent, hook, plugin, script, or tool into AI Operating Memory.

## Review sequence

1. **Provenance** — identify the canonical repository, owner, default branch, commit/ref, and source URL.
2. **License** — record the exact license and whether redistribution/derivation is permitted.
3. **Payload inspection** — inspect SKILL.md, hooks, scripts, install commands, MCP/tool configuration, network calls, file writes, and credential handling.
4. **Compatibility** — distinguish Claude Code, Codex, Cursor, Gemini, and generic Agent Skills behavior; never assume parity.
5. **Value** — extract the smallest reusable capability that improves planning, construction, verification, safety, memory, or domain execution.
6. **Evidence** — record tests, examples, maintenance signals, and known limitations.
7. **Decision** — adopt, adapt, reference-only, quarantine, or reject.

## Security gates

Reject or quarantine until reviewed when a source:

- executes remote shell/install code without a clear need;
- asks for secrets or broad credentials;
- disables sandbox/approval/security controls;
- installs opaque binaries;
- changes global configuration unexpectedly;
- contains hooks with unclear scope;
- downloads mutable content at runtime without integrity controls.

## Output record

Every adopted capability records:

- source repository and URL;
- license and attribution requirement;
- original capability;
- local adaptation;
- compatibility target;
- security review status;
- verification status;
- date/ref reviewed.

## Principle

Import capability, not trust. Preserve provenance. Keep the local operating memory smaller and stronger than the raw ecosystem.

# ARGCYBERSKILLHUB Source Review

## Source
- GitHub account: https://github.com/argcyberskillhub
- Review date: 2026-10-06
- Repositories inspected: OSINT-X, OCTOPUS, Phone-X, Web-Info, GUI-ARGRecon, PowerShell-Ultimate-Customizer, profile repository.

## Extracted reusable capabilities
- Passive domain/DNS/RDAP intelligence.
- Public IP/ASN/ISP and approximate geolocation metadata.
- Public username presence checking across multiple platforms.
- Public phone-number formatting, region, timezone and carrier metadata.
- Modular CLI organization and dependency/status checks.
- Explicit authorization and safety boundaries around active reconnaissance.

## Adoption decision
**Adopt selectively.** The reusable procedure is represented by `agent-skills/skills/authorized-osint-recon/SKILL.md`.

No upstream application code is copied into the canonical Skill layer. Active scanning remains authorization-gated.

## Deduplication
A search of the current `agent-skills` repository did not identify an existing OSINT/recon Skill with the same scope, so this is treated as a new consolidated Skill rather than a duplicate import.

## Exclusions
- Do not import the upstream CLI applications wholesale.
- Do not promote offensive or disruptive functionality into executable Skills.
- PowerShell desktop customization is unrelated to the OSINT capability and is not adopted here.

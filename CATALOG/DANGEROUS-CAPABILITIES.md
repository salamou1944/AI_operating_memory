# Dangerous Capability Catalog

This file is an inventory and governance layer. It is intentionally **not** an executable skill collection.

## Why keep dangerous capabilities in memory?

A strong AI operating system needs to recognize dangerous requests, audit agent extensions for dangerous behavior, understand security research terminology, and know when execution authority must be denied or escalated.

## Catalog

| Capability | Knowledge retained | Automatic execution |
|---|---|---|
| Reconnaissance | concepts, scope/authorization rules, defensive detection | No |
| Vulnerability assessment | methodology and defensive interpretation | No against real targets |
| Web/API security testing | review concepts and safe lab context | No against unapproved targets |
| Credential attacks | detection, risk, defensive testing concepts | No |
| Privilege escalation | detection and hardening concepts | No |
| Malware analysis | analysis, indicators, containment concepts | No malware deployment |
| Exploit development | vulnerability research concepts and mitigations | No weaponized execution |
| Persistence/evasion | detection and prevention concepts | No |
| Exfiltration | data-loss detection and prevention | No |
| Destructive automation | recognition and recovery | No |
| Cloud attack paths | threat modeling and hardening | No unauthorized actions |
| Supply-chain attacks | dependency/repository defense | No |
| Prompt/tool injection | detection and containment | No bypass behavior |

## Import rule

A source containing dangerous skills may be inspected and catalogued. Its dangerous procedures must not be copied into an automatically discoverable executable skill directory merely to increase capability.

## Safe transformation pattern

Dangerous source -> capability metadata -> threat model -> defensive skill -> isolated lab/evaluation -> explicit authorization gate -> controlled execution (where permitted).

## Security gate

Any capability that can materially affect a third-party system, steal secrets, bypass access controls, deploy malware, destroy data, or conceal activity remains restricted even when the source repository is popular or highly starred.

## Sources

See `CATALOG/AGENT-SKILL-SOURCES.md` and `CATALOG/CAPABILITY-REGISTRY.md`.

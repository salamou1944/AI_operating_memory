# Safe Transformation Gate — Dangerous Capability to Defensive Skill

Purpose: convert useful security-research capabilities from Collection into bounded defensive Skills without importing weaponized execution.

## Transformation rule

A dangerous capability is never promoted by copying its offensive procedure verbatim. Promotion means extracting the useful detection, analysis, hardening, and regression-test logic and reimplementing it with explicit safety controls.

## Required transformation stages

1. Identify the capability and its provenance.
2. Classify it as A/B/C using the Capability Registry.
3. Isolate dangerous source code from automatically discoverable Skills.
4. Extract only the reusable mechanism: detection logic, parsers, protocol understanding, indicators, evidence model, remediation pattern, or test oracle.
5. Remove or disable credential theft, auth bypass, persistence, evasion, destructive actions, exfiltration, malware deployment, stealth, and unrestricted target interaction.
6. Add an explicit authorized-scope contract.
7. Add bounded execution: rate/impact limits, timeouts, target allowlists where applicable, and safe failure.
8. Make evidence collection first-class: target, scope, source, timestamp, observation, confidence, limitations.
9. Add remediation guidance and a regression test whenever technically possible.
10. Validate the transformed Skill before admission to the canonical Skill tree.

## Promotion criteria

A capability may become a canonical defensive Skill only when:

- its purpose is defensive or authorized testing;
- its execution boundary is explicit;
- dangerous behavior has been removed or isolated;
- inputs and outputs are predictable;
- evidence can be produced;
- the remediation path is documented;
- regression testing is possible or its limitation is recorded;
- provenance/license status is recorded;
- no secrets are embedded;
- no bypass of authentication, CAPTCHA, MFA, quotas, rate limits, or provider protections is required.

## Red-Team use

Controlled offensive testing may be performed only against assets and environments explicitly in scope. The test objective is to discover a weakness, produce evidence, remediate it, and retest. A successful exploit is not considered a deliverable by itself.

## Canonical output

Every promoted Skill should contain:

- Scope and authorization
- Threat/finding model
- Safe detection or test procedure
- Evidence contract
- Remediation pattern
- Regression/retest procedure
- Safety boundaries
- Provenance and license
- Definition of Done

## Non-promotion

Keep a capability in quarantine when safe transformation would still leave it dependent on weaponized execution, unrestricted target interaction, credential theft, access-control bypass, destructive payloads, persistence/evasion, or data exfiltration.

This gate supplements CATALOG/DANGEROUS-CAPABILITIES.md and CATALOG/CAPABILITY-REGISTRY.md.

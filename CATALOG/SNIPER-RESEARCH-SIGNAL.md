# SNIPER Research Signal

Status: adopted design concept

SNIPER is a defensive first-deviation detection layer for MONY/EASY. The concept was extracted from the discussion of multi-capability security tooling: study how systems chain capabilities, identify gaps, then build a safer, verifiable internal capability.

Core sequence:

Baseline -> first unexplained deviation -> correlation -> confidence/risk -> defensive containment -> recovery -> independent verification.

Relevant signals include identity/session changes, new IP/ASN/device, credential/token changes, permission changes, code/dependency/config/schema/deployment changes, process/service changes, unusual API/tool use, unexpected network destinations, and audit integrity anomalies.

Design rule: a new IP or single anomaly is not proof of compromise. Detection should correlate signals with approved changes, deployment provenance, known automation, and expected behavior.

Allowed response is defensive: alert, step-up authentication, revoke/rotate credentials, isolate internal workloads, freeze sensitive automation, preserve evidence, restore known-good state, and verify.

Prohibited response: counter-intrusion, deletion or modification of third-party data, retaliation, or exfiltration from an attacker.

Reason retained: provides a concrete security architecture pattern that can strengthen the existing 14-agent/Elite ecosystem without turning it into an offensive system.

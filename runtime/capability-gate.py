#!/usr/bin/env python3
"""Policy gate for executable capabilities.

This is intentionally a gate, not an unrestricted command runner.
Security-sensitive capabilities require LAB_MODE and a target that is
explicitly classified as local/lab. Unknown capabilities fail closed.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

SAFE = {
    "code-review", "repo-inspection", "unit-test", "lint", "type-check",
    "dependency-audit", "threat-model", "log-analysis", "static-analysis",
}
LAB_ONLY = {
    "security-scan-lab", "exploit-reproduction-lab", "credential-audit-lab",
    "privilege-boundary-test-lab", "malware-analysis-lab",
}


def decision(capability: str, target: str, mode: str) -> tuple[bool, str]:
    if capability in SAFE:
        return True, "safe capability"
    if capability in LAB_ONLY:
        if mode != "lab":
            return False, "lab-only capability requires --mode lab"
        if not target.startswith("lab:"):
            return False, "lab-only capability requires an explicit lab: target"
        return True, "authorized lab capability"
    return False, "unknown capability: fail closed"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("capability")
    p.add_argument("--target", required=True)
    p.add_argument("--mode", choices=("safe", "lab", "review"), default="review")
    args = p.parse_args()

    allowed, reason = decision(args.capability, args.target, args.mode)
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "capability": args.capability,
        "target": args.target,
        "mode": args.mode,
        "decision": "allow" if allowed else "deny",
        "reason": reason,
    }
    print(json.dumps(record, indent=2))

    if args.mode == "review":
        return 0
    return 0 if allowed else 2


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Fail-closed pre-ingestion gate for skills/tools entering AI_operating_memory.

Static-only: never imports, executes, installs, or contacts network resources.
Exit 0 = accepted, 1 = review/block required, 2 = usage error.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

TEXT_EXT = {".md", ".txt", ".py", ".js", ".ts", ".sh", ".ps1", ".json", ".yaml", ".yml", ".toml"}
SECRET = re.compile(r"(?i)(api[_-]?key|secret|password|token|private[_-]?key)\s*[:=]\s*['\"][^'\"]{8,}")
INJECTION = re.compile(r"(?i)(ignore\s+(all|any|previous)\s+instructions|do not tell the user|hide (this|your) action|override (the )?system)")
EXFIL = re.compile(r"(?i)(webhook\.site|requestbin|curl\s+[^\n]*(\.env|id_rsa)|requests?\.(post|put)\s*\()")
DESTRUCTIVE = re.compile(r"(?i)(rm\s+-rf|format\s+disk|drop\s+database|git\s+push\s+--force|shutdown|:(){:|fork bomb)")
NETWORK = re.compile(r"https?://[^\s\"']+")


def scan(root: Path):
    findings = []
    files = [p for p in root.rglob('*') if p.is_file() and p.suffix.lower() in TEXT_EXT]
    for p in files:
        try: text = p.read_text(encoding='utf-8', errors='replace')
        except OSError as e:
            findings.append(("HIGH", str(p), f"unreadable: {e}")); continue
        rel = str(p.relative_to(root))
        if SECRET.search(text): findings.append(("CRITICAL", rel, "possible hard-coded secret"))
        if INJECTION.search(text): findings.append(("HIGH", rel, "instruction override / concealment pattern"))
        if EXFIL.search(text): findings.append(("HIGH", rel, "possible data-exfiltration/network sink pattern"))
        if DESTRUCTIVE.search(text): findings.append(("HIGH", rel, "destructive command pattern"))
        urls = NETWORK.findall(text)
        if len(urls) > 10: findings.append(("MEDIUM", rel, f"large number of URLs ({len(urls)})"))
    return findings, files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('path', type=Path)
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()
    if not args.path.exists() or not args.path.is_dir():
        ap.error('path must be an existing directory')
    findings, files = scan(args.path)
    digest = hashlib.sha256()
    for p in sorted(files): digest.update(str(p.relative_to(args.path)).encode()); digest.update(p.read_bytes())
    result = {"status": "BLOCK" if findings else "PASS", "sha256": digest.hexdigest(), "files_scanned": len(files), "findings": [{"severity":s,"file":f,"message":m} for s,f,m in findings]}
    if args.json: print(json.dumps(result, indent=2))
    else:
        print(f"incoming-skill-gate: {result['status']} ({len(files)} files)")
        for x in result['findings']: print(f"[{x['severity']}] {x['file']}: {x['message']}")
    raise SystemExit(1 if findings else 0)

if __name__ == '__main__': main()

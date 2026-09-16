# Security Policy

## Security boundary
This repository contains operating material and must never contain live API keys, access tokens, OAuth client secrets, passwords, cookies, private certificates, customer credentials, or other private runtime secrets.

Secrets must stay in protected secret managers or environment variables and must not be copied into repository files, issues, pull requests, logs, or documentation.

## Reporting a suspected leak
Do not copy or repost a suspected credential. Report the file/path and commit reference privately to `easy@agentmail.to` so it can be contained and rotated.

## Public exposure warning
This repository is currently public. Public repository contents can be copied. Do not place credentials, private customer data, or other material that must remain confidential here. Any material that is operationally sensitive should be moved to a private repository before further publication.

## Remediation rule
Any real credential committed to Git history is treated as compromised and must be revoked/rotated before cleanup.

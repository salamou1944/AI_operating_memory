# Canonical State Policy

`PROJECT-STATE-MONY-CANONICAL.json` is the single machine-readable source of truth for MONY state in this repository.

Other MONY state documents are human-readable projections or historical notes. They must not independently declare completion.

A state transition is valid only when:
- the canonical JSON parses;
- `commit_sha` identifies the exact source revision when verification is performed;
- `evidence` records the verification source and timestamp;
- `known_risks` remains explicit;
- `completed_tasks` contains only tasks supported by evidence.

Revenue claims require independent revenue evidence and may not be inferred from affiliate URL reachability, provider health, or synthetic tests.

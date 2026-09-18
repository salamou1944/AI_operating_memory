# Agent Retrieval Signal

Added 2026-09-18.

Signal: repository context acquisition should be measured independently from code generation.

Useful patterns extracted from current public evaluation work:
- file-level retrieval benchmarks with positive, no-gold, and counterfactual controls;
- context precision, recall, and token-yield measurement;
- baseline versus MCP comparisons;
- explicit retrieval provenance before edits;
- task verification remains separate from retrieval success.

Integrated conceptually into agent-skills as the Repository Retrieval Verification skill and Repository Retrieval Intelligence Signal. No external implementation was copied.

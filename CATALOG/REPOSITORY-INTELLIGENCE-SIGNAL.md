# Repository Intelligence Signal

## Signal
Litho (also known as deepwiki-rs) is a Rust-based open-source documentation engine that turns a codebase into C4-style architecture documentation and code-level documentation. Public documentation describes external PDF/Markdown/SQL context, database diagrams, Git-history analysis, cross-referencing and CI/CD generation.

## Strategic lesson
Documentation generation is more valuable when treated as a continuously-derived architecture knowledge layer rather than a static README generator.

## Adopted principle
For the larger system, maintain an evidence-backed repository graph and generated architecture views that can be consumed by Elite/ARMY-14, verification, security and change-impact workflows.

## Guardrails
- Code/repository evidence is authoritative for what actually exists.
- AI explanations must retain provenance.
- External documents are contextual and may conflict with code.
- Generated diagrams must be checked against the current repository.
- Do not claim architecture facts that cannot be traced to evidence.
- External projects are references, not code to copy blindly.

## Reference
https://github.com/sopaco/deepwiki-rs
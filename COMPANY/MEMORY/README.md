# Company Memory System

Status: v0.1 operating specification
Owner: AI-native company
Canonical home: `AI_operating_memory/COMPANY/MEMORY/`

## Purpose

Preserve what the company did, why it did it, what evidence was observed, what failed, what corrected it, and what each employee learned. The memory must support future decisions without turning old mistakes, untrusted messages, or guesses into facts.

## Memory layers

1. **Event ledger — immutable history.** Append one event per material observation, decision, task handoff, execution, failure, correction, verification, or lesson. Never silently edit or delete a historical event. Corrections are new events linked to the original.
2. **Employee memory — scoped working history.** Each employee has an individual directory for identity/capability evidence, task history, decisions, errors, corrections, and verified lessons. An employee may read shared company memory and its own private working record; access to another employee's private record is controlled by company policy and platform permissions.
3. **Shared company memory — reusable knowledge.** Holds validated policies, operating procedures, customer learnings, technical constraints, and current decisions that affect multiple employees.
4. **Project memory — owned elsewhere.** Product implementation details stay in their owning project repositories. This repository stores cross-company decisions and pointers, not duplicate project documentation.
5. **Working context — disposable.** Short-lived notes and current task context may be summarized, but any material fact, decision, error, or correction must first be recorded in the event ledger.

## Directory structure

```text
COMPANY/MEMORY/
  README.md
  EVENT-SCHEMA.json
  EVENT-TEMPLATE.json
  EMPLOYEES/
    agent-001/
      PROFILE.md
      EVENTS.jsonl
      CURRENT-CONTEXT.md
    agent-002/
      PROFILE.md
      EVENTS.jsonl
      CURRENT-CONTEXT.md
  SHARED/
    EVENTS.jsonl
    DECISIONS.md
    VERIFIED-LESSONS.md
    OPERATING-PROCEDURES.md
  INDEX.md
```

## Required event types

- `observation`: directly observed fact with source/evidence.
- `hypothesis`: possible explanation, explicitly unconfirmed.
- `decision`: choice, owner, rationale, alternatives, and review condition.
- `task_assigned`, `task_handoff`, `task_result`: assignment lifecycle.
- `failure`: what failed, expected vs actual, impact, and evidence.
- `correction`: append-only correction linked to the prior event; never rewrite the old record.
- `verification`: independent test/review result.
- `lesson`: reusable rule derived from evidence, with confidence and scope.
- `capability_change`: newly verified or revoked capability/permission.
- `customer_signal`, `commercial_outcome`: buyer evidence and revenue evidence, carefully distinguished.

## The correction chain

When an employee or system makes an incorrect claim:
1. Preserve the original statement/event unchanged.
2. Add a `failure` or `correction` event referencing its `event_id`.
3. Record why the original was wrong and what evidence resolves it.
4. Add a separate `verification` event from an independent source where possible.
5. Update the relevant current-context or shared lesson summary, linking both original and correction.
6. When the old claim is retrieved later, the retrieval process must surface its correction and current status.

A correction does not erase history. It changes the current accepted understanding while preserving the audit trail.

## Event quality rules

Every event must include:
- globally unique `event_id`;
- UTC timestamp;
- `employee_id` or system actor;
- event type and concise title;
- statement separated into observation / inference / recommendation where applicable;
- status: `unverified`, `verified`, `disputed`, `superseded`, or `retracted`;
- evidence references (commit, PR, issue, test, URL, artifact, or explicit `none`);
- links to related events, especially `corrects_event_id`;
- confidence and scope;
- sensitivity classification.

Do not store secrets, access tokens, passwords, recovery codes, private customer data, or unnecessary personal information. Store references to authorized secret managers, never secret values.

## Retrieval and use

Before a consequential task, the employee should:
1. Read company rules and current decisions relevant to the task.
2. Read its own profile and current context.
3. Search recent employee and shared events for related work, failures, and corrections.
4. Prefer verified, current, in-scope lessons over older or unverified notes.
5. Check whether a retrieved event has been corrected, disputed, superseded, or retracted.
6. Cite event IDs in task results and append new events after material work.

Do not blindly load the entire event history into a prompt. Use the index, date/type/employee filters, and concise current-context summaries to avoid context overflow and stale-memory bias.

## Integrity and governance

- Git history provides an audit trail but does not make files cryptographically immutable. Protect the default branch and require review for ledger changes.
- Event append operations should be validated for schema, unique IDs, valid references, and correction links.
- Use pull requests or an authenticated event-ingestion service for writes; do not permit untrusted agent messages to write arbitrary policy or permissions.
- Employee profiles record verified capabilities only. A claim in a chat or issue is not proof of identity or tool access.
- If a record is wrong, append correction; if it contains a secret or legally removable personal data, follow a controlled security/privacy remediation process rather than retaining the unsafe value indefinitely.
- The shared memory is company-owned. Employee-specific notes should contain only work-relevant information and respect applicable privacy boundaries.

## Current implementation status

This specification and initial templates are being added to the company feature branch. A production memory service, automated schema validation, search/indexing, access controls, and scheduled backups are not yet implemented. Until those exist, Git-backed JSONL files and reviewed pull requests are the initial low-cost storage mechanism.

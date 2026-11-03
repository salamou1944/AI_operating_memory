# Company Operating System and First Revenue Mission

## 1. Operating loop

Every task follows:

Intake → classify → assign → independent first pass → execute → challenge/review → verify → accept/rework → record outcome → reuse learning.

Each task record must contain:
- task ID and objective;
- business priority;
- accountable agent and reviewer;
- source/repository/customer context;
- allowed tools and forbidden actions;
- acceptance criteria;
- status and blocker;
- evidence links;
- outcome and follow-up.

A chat message alone is not a task ledger. A GitHub issue is a candidate transport until the employee's identity and ability to use it are confirmed.

## 2. Communication and orchestration

The Agent Exchange Protocol (AEP) in `PROTOCOLS/AGENT-EXCHANGE-PROTOCOL-v0.1.md` is a message contract only. It does not launch agents or create a connection. The company must implement and test one transport adapter, then verify identity through the transport itself.

Current known boundaries:
- ChatGPT can operate through connected tools during an active session.
- Agent #2 has previously been described by the cofounder as an agent with GitHub access, with messages relayed by voice. That is not a verified direct API channel.
- The private `salamou1944/local-bridge.` repository documents a Windows self-hosted Actions runner setup and a read-only diagnostic workflow. Its README says that a successful run proves runner reachability, not a general-purpose MCP connection. Runner online status has not been verified in this review.
- GitHub-connected Codex reviews have been observed on existing pull requests. This is evidence of an automated review integration, not proof that it is Agent #2 or a general-purpose employee.
- The GitHub issue opened for Agent #2 onboarding is `salamou1944/AI_operating_memory#11`. A response from a verified account can establish a candidate transport; account-to-Agent-#2 identity still needs confirmation.

## 3. Existing asset and capability leverage

Prefer existing assets:
- `salamou1944/agent-skills`: reusable delegation, permission, approval, persistence, recovery, evidence, and orchestration skills.
- `salamou1944/AI_operating_memory`: canonical operating rules, evidence, and AEP specification.
- `salamou1944/Salamou-31`: API Factory and the first documented commercial API entry.
- Existing EASY and MONY assets remain separate product/business workstreams; do not merge their state into the company control plane.

Do not build a second task framework, memory database, or agent framework until an observed gap cannot be solved by the existing assets.

## 4. First revenue mission — Username Research API pilot

### Why this is the first candidate
The API Factory commercial runbook in `Salamou-31/AI-API-HUB/products/username-research-api/COMMERCIAL-RUNBOOK.md` records:
- a production and preview customer-facing endpoint;
- customer-specific API-key authentication;
- a successful lifecycle smoke with one real Sherlock request, quota rejection, usage accounting, and key revocation;
- technical customer access verified, but independent customer use and revenue not observed.

This is a stronger starting point than building another product because the implementation and a documented entry point already exist. It is not proof that the current endpoint is healthy today; recheck it before outreach or customer onboarding.

### Proposed buyer
Small lead-generation agencies, recruiting/research operators, and developers who need structured public-profile discovery from supplied usernames. Qualification must verify a real workflow, lawful purpose, expected volume, and willingness to pay.

### Pilot offer
A fixed-scope, short paid pilot:
- customer submits an agreed list of usernames;
- API returns structured discovery evidence and source references;
- results retain uncertainty and `verified:false` unless an independent verification mechanism exists;
- usage cap, turnaround, support, retention, and exclusions are agreed in advance;
- no broad subscription or bespoke feature promise before the pilot validates demand.

### Acquisition test
1. Build a list of 10 qualified prospects from public business contact information.
2. Select 3 with the clearest fit and personalized use case.
3. Send a concise offer only after validating contact channel and compliance.
4. Record reply, problem confirmation, price objection, and next step.
5. Seek one paid pilot, not vanity signups.
6. Issue a customer key only after payment/terms are confirmed and the customer-specific path is checked.
7. Deliver the pilot, obtain customer acceptance, and ask for repeat usage/referral.

### Revenue proof
Revenue is recorded only from a real payment transaction tied to a customer and invoice/order reference. API key creation, a successful request, a verbal promise, or a draft proposal is not revenue.

### Unit economics
Before pricing, measure:
- compute/provider/runtime cost per request;
- research completion rate and latency;
- support and manual QA minutes per pilot;
- refunds/failure handling;
- payment fees and taxes where applicable;
- contribution margin per paid pilot.

Do not invent a price before observing buyer willingness to pay and delivery cost. Do not buy infrastructure or incur a subscription before a customer-funded case exists.

## 5. Current blockers and closure tests

| Blocker | Why it matters | Closure evidence |
|---|---|---|
| Agent #2 identity and direct channel unverified | Cannot assign autonomous work reliably | Authenticated reply, verified account mapping, repeatable handoff |
| No independently running multi-agent runtime proven | Roles may be prompts rather than employees | Two separate runtimes execute separate tasks and return evidence |
| No durable task queue / task ledger proven | Work can be lost or duplicated | State transitions, ownership, idempotency, recovery test |
| Fresh live health and customer path not checked in this review | Historical smoke may be stale | New production smoke with timestamps and response evidence |
| No independent buyer or revenue observed | Technical product is not a business | Customer action and actual payment evidence |
| Pricing and legal/data-use boundaries not settled | Commercial and privacy exposure | Approved terms, data policy, buyer scope, price and payment process |
| Review/verification independence incomplete | Self-review can miss defects | Different agent or deterministic test verifies material result |

## 6. Manager's decision rule

The Managing Director may autonomously choose reversible research and implementation tasks within connected permissions. Escalate or stop when the next step requires unavailable account access, unverified identity, external legal/financial commitment, spending, sensitive data, or a production action whose required approval is absent.

The company is not "complete" when its charter is written. It is complete only when the operational definition in `CHARTER-v0.1.md` is met with evidence.

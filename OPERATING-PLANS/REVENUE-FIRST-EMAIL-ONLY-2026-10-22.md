# REVENUE-FIRST OPERATING PLAN — EMAIL-ONLY, ZERO-UPFRONT-COST
Date: 2026-10-22
Owner: salamou1944
Status: ACTIVE PLAN — baseline documented; inventory still in progress
Canonical home: `salamou1944/AI_operating_memory`
Related assets: `salamou1944/Pastel-`, `salamou1944/Salamou-31`, `salamou1944/Project-`, `salamou1944/agent-skills`, `salamou1944/local-bridge.`

## 1. Objective and operating constraints

Primary objective, in order:
1. Obtain the first real paid customer.
2. Deliver a small, verifiable result and collect payment.
3. Turn the delivery into a repeatable email-led offer.
4. Convert repeatable work into recurring revenue.
5. Reinvest revenue into tools only after it has been received.

Hard constraints:
- Current cash available for investment: €200. Treat it as protected runway, not a spending target.
- No new spending before revenue unless the owner explicitly approves a specific expense.
- No calls, interviews, or meetings as a default sales requirement. Use asynchronous email; allow a customer to choose email-only delivery.
- Do not create a new project or duplicate an existing asset when a usable asset can be finished.
- No claims of production readiness without live proof.
- Never expose secrets, tokens, API keys, customer data, or service-role credentials in GitHub, email, or chat.
- Keep business/revenue operations separate from engineering implementation and COLLECTION research.
- Preserve existing COLLECTION data and existing production services. No destructive rebuilds.
- Do not claim a sale, lead, deployment, or customer outcome until evidence exists.

## 2. Initial strategic decision

### Primary offer to validate
**Multilingual QR Guest Concierge for independent hospitality businesses** — a mobile web experience reached by QR/link that answers only from approved business facts and routes guests to WhatsApp, phone, email, directions, and other approved contact channels.

Target buyer: independent cafés, boutique hotels, guesthouses, small restaurants, and hospitality operators who serve international guests and need basic guest information available without staff repeatedly answering the same questions.

Sales channel: carefully researched, personalized cold email and direct business email contacts. No calls or interviews required. Qualification, scope, approvals, delivery, and support should all be possible in writing.

Why this is the first offer:
- It reuses the existing PASTEL QR Concierge and Host Standard work instead of starting from zero.
- It can be demonstrated with a public link and a short written explanation.
- A small fixed-scope pilot is easier to buy than a broad AI transformation project.
- The same shared Host Standard can be configured for more than one customer.
- It can later become a recurring maintenance/knowledge-update service, but recurring revenue is not assumed until a customer agrees and pays.

### Commercial hypotheses — not validated market facts
Test an initial fixed-scope pilot around **€150–€300 setup** and optional **€20–€50/month maintenance** only after defining exactly what is included and confirming the buyer's interest. These are test prices, not guaranteed market rates or promised income. Adjust after replies and paid conversion evidence.

Fallback offer if QR concierge fails validation: a small, fixed-price AI/API or workflow integration service using existing Salamou-31 assets, but only after selecting one concrete deliverable that can be tested and delivered without paid provider credits.

## 3. PASTEL: finish before selling it as proof

PASTEL is a potential pilot/case study, not yet a production-verified sales claim.

Release gate:
- [ ] Confirm the intended public URL loads on a real mobile browser.
- [ ] Verify the complete user path: open → ask common questions → see verified answers → use contact actions.
- [ ] Check mobile layout, loading, language handling, links, error states, and no invented business facts.
- [ ] Check the current 3D Host presentation and Arabic voice quality against the commercial baseline.
- [ ] Verify avatar and all bundled assets have appropriate commercial/public-web-app rights.
- [ ] Record actual limitations clearly; Arabic lip-sync is not complete merely because Arabic speech fallback exists.
- [ ] Obtain explicit business approval before presenting private information, claiming endorsement, changing a live QR destination, or publishing a case study.
- [ ] Preserve the existing QR destination until the replacement is live and tested on a real phone.

If the 3D avatar quality blocks release, do not let it block the simpler QR concierge offer: separate the verified static QR concierge from the optional 3D Host and sell only what demonstrably works.

## 4. 30-day execution plan

### Phase A — asset and access inventory (Days 1–3)
Produce a canonical inventory with evidence, not recollection:
- GitHub: owned/accessible repositories, visibility, default branch, recent commits, active PRs, failed/running workflows, Pages URLs, CI evidence, known blockers.
- Runtime platforms: Railway, Supabase, Vercel, Render, Replit; project/service IDs, environments, deployment state, domains, storage, configured variable *names only*, volumes, limits, and whether access is read-only or write-capable.
- AI/model options: existing provider eligibility, free-tier terms, live-probe evidence, keys present/not present (never values), rate limits, and whether an actual completion was observed.
- Tools/connectors: Notion, browser, Termalin, email/outreach capability, local laptop inference capability, and any missing or ambiguous connection.
- Commercial assets: PASTEL demo, Host Standard, API Factory, MONY, EASY, content/channel assets, customer/contact history, previous outreach, and current working URLs.
- For every inventory row record: `asset`, `owner/repo/service`, `what exists`, `access level`, `last verified at`, `evidence URL`, `working status`, `cost/limits`, `blocker`, `next action`, `confidence`.
- Mark a category COMPLETE only when its relevant account/project/service list has been enumerated and reconciled. Mark UNKNOWN when the connector cannot see it; never silently count unknown as absent.

### Phase B — offer proof (Days 2–5, overlaps inventory)
- Test PASTEL on mobile and fix only blockers that prevent a truthful demo.
- Produce one concise one-page offer and one short demo link.
- Make a clearly labelled sample configuration for a fictional business if PASTEL approval is unavailable; do not imply the fictional sample is a customer.
- Define exact scope, turnaround, buyer inputs, exclusions, price, payment method, acceptance test, and post-delivery support.
- Keep the deliverable provider-neutral where possible. Do not require paid AI inference if verified static answers and contact actions satisfy the offer.

### Phase C — email prospecting (Days 4–14)
- Select one initial niche and one geographic/language segment at a time.
- Build a small verified list of 50–100 qualified businesses from public official sources; record official email/source URL and a reason the offer fits.
- Send 5–10 individualized emails per working day, within applicable law and platform policies. No bulk spam, scraped personal addresses, deceptive subject lines, or fabricated personalization.
- Use one short email, one relevant demo, one concrete benefit, and one low-friction reply request. State that the process can remain email-only.
- Follow up once after 4–6 business days; stop on refusal or opt-out.
- Track sent, delivered/bounced, replies, positive replies, requests for scope, proposals, accepted proposals, paid invoices, and delivered outcomes. An email sent is not a lead; a positive reply is not revenue.
- Do not send from the owner's account or represent the owner as having approved a claim unless that permission is explicit.

### Phase D — close and deliver first paid pilot (Days 7–21)
- Convert interest into a written scope and acceptance criteria.
- Ask for payment or a clearly agreed deposit before work that incurs cost.
- Deliver the smallest complete, testable result.
- Obtain written acceptance and request permission for a testimonial/case study separately.
- Record actual hours, costs, gross margin, customer feedback, and what can be reused.
- If there are no positive replies after 50 well-targeted emails, review targeting, offer, proof, and copy before sending more.

### Phase E — repeat and recurring revenue (Days 15–30)
- Turn the first delivery into a reusable configuration/template.
- Offer monthly updates/support only when there is ongoing value and a clearly stated service level.
- Reuse the same core implementation for the next customers; avoid bespoke features until paid demand justifies them.
- Reinvest a portion of received revenue in tools only when a specific bottleneck is proven and a free alternative is insufficient.

## 5. Protected €200 budget

Default budget before first revenue: **€0 committed spend**.
- €200 remains protected as reserve.
- No paid hosting, API credit, ads, domains, lead databases, or subscriptions just to make the plan appear active.
- Use current free tiers and existing domains/accounts where suitable, after checking limits and terms.
- After the first payment, approve expenses one by one against a demonstrated bottleneck and expected payback. Never treat free-tier claims as verified until terms and live behavior are checked.

## 6. Parallel workstreams and priority rules

Priority order:
1. **First revenue:** PASTEL/QR Concierge offer proof and targeted email sales.
2. **Evidence inventory:** continue until the asset/access register has no unexplained omissions in the known scope.
3. **COLLECTION:** continue safe incremental cycles, audit the actual current-main snapshot, preserve blocked/deferred records, and do not claim a completed extraction from an earlier run.
4. **API Factory:** keep hardening and free-provider research bounded; do not call it production-ready until storage write/read-back, provider live response, deployment execution, public smoke test, and usage/idempotency persistence are each independently proven.
5. **EASY:** keep paused where provider credit is exhausted; no spend until revenue/credit is available. Only safe, no-cost work that directly supports revenue or reduces a verified blocker.
6. **MONY and other assets:** include in inventory; do not divert the first-revenue workstream unless evidence shows a faster, real, compliant path to payout.

If a workstream is blocked, record the exact blocker and continue the next independent task. Do not stop the whole plan for one missing credential or an external UI action.

## 7. Evidence and reporting contract

Every claimed completion must include one or more of:
- exact repository path and commit SHA;
- CI run URL and final conclusion;
- public URL tested and what path was tested;
- service/deployment identifier and actual status;
- email sent/reply evidence where authorized;
- payment/acceptance evidence before calling it revenue.

Every status entry must distinguish:
- **VERIFIED** — directly observed with evidence;
- **PARTIALLY VERIFIED** — some steps work, named gaps remain;
- **NOT VERIFIED** — not observed;
- **BLOCKED** — exact external action/permission/credit required;
- **NOT APPLICABLE** — reason stated.

A successful unit test is not a production deployment. A successful provider-gate test is not a live provider response. A configured domain is not a tested customer journey. A public repository is not a free hosted model. Never count planned work as completed work.

## 8. Current starting facts and known gaps (as of 2026-10-22)

- PASTEL repo: `salamou1944/Pastel-`; QR Concierge README states the intended Pages URL is `https://salamou1944.github.io/Pastel-/` and says not to replace the old QR destination until the new URL is live and tested on a real phone. Current release state must be rechecked.
- Host Standard README says the source/read-back path exists but browser runtime verification remains required; commercial avatar rights and premium presentation must be checked; Arabic phoneme-level lip-sync remains unresolved.
- API Factory README states `POST /v1/factory/deploy/plan` is preflight only; there is no verified Railway/Vercel deployment execution adapter in the documented version. Provider-backed output is not PROVIDER_VERIFIED without an observed real provider response.
- COLLECTION has an established safe incremental workflow and current-main audit artifacts; the latest cycle must be rechecked from the live Actions run before updating counts or triggering another cycle.
- A prior connection inspection showed multiple Railway/Supabase/Vercel resources, but these must be reconciled by exact IDs, services, environments, deployment state, and current evidence before the inventory is marked complete.
- Previous outbound emails exist according to owner context, but recipient details, outcomes, and whether follow-up is due must be checked from the owner's records before planning repeat outreach.
- Current connector visibility is not equivalent to all resources in an external account. Any connector/workspace not fully enumerated remains an explicit inventory gap.

## 9. First execution checklist

- [ ] Create and maintain the canonical asset/access inventory.
- [ ] Recheck PASTEL Pages deployment and mobile user path; document pass/fail evidence.
- [ ] Recheck current COLLECTION run and continue only after reading actual logs.
- [ ] Reconcile Railway, Supabase, Vercel, Render, Replit, Notion, Termalin, browser, and email access; record inaccessible scopes as UNKNOWN.
- [ ] Review the existing outreach history and choose the next 10 qualified businesses.
- [ ] Finalize the email-only offer and its truthful demo.
- [ ] Begin outreach only when the demo and offer are credible.
- [ ] Update this plan after each material event with commit/run/link evidence and the next action.

## 10. Definition of success

Short-term success is **first collected payment from a real customer**, not a green CI badge or a completed repository task. The next success is a repeatable delivery with positive margin; recurring revenue follows only after the customer receives ongoing value and agrees to pay for it.

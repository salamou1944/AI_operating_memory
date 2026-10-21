# Resource Inventory Supplement — 2026-10-21

This supplements [the connected resource inventory](./RESOURCE-INVENTORY-2026-10-21.md) with repository-level checks completed after its first commit. No credentials were read or stored.

## Confirmed repository roles

- Easy- is the EASY commerce/creative-engine source. Root contains project boundary/rules, package.json, app/apps, api-lab, api-registry, commerce-connector, knowledge-bank, platform, services, src and test. Package `easy-seller-mvp` v0.1.0 uses Node test/check scripts and depends on `@fal-ai/client`. Production requires a real provider adapter, durable persistence, auth, request IDs, integrity checks and a deployed end-to-end test.
- Files- currently contains `collection/mufeedvh/`; the README is only a title, so this is source collection, not a verified runtime.
- Project- contains the bounded COLLECTION pipeline, audit/classification outputs and opportunity/service-pack records.
- Astra is ASTRA Quant Lab research. Kraken data ingestion is verified, but single-asset and cross-asset research gates failed; profitability is not proven and live money is off.
- Astra- is the separate trading-bot boundary with paper execution, idempotency ledger and kill switch. Live trading remains off; do not conflate it with research evidence.
- agent-skills contains reusable skills, Elite engineering automation, ARMY-14 verification, MONY/Revenue Engine and workflows.
- Pastel- contains the mobile-first QR concierge, staff UI, configuration and Supabase functions. Its README says not to replace the existing QR destination until the new URL is live and tested on a real phone.
- Salamou-31 contains API Factory, provider gates, storage gateway integration, deployment notes, and the COLLECTION folder.
- AI_operating_memory is the canonical operating memory and decision/capability policy repository.
- local-bridge. is a private Windows self-hosted-runner control repository. A read-only local machine inventory workflow was added and triggered: [run 39519079143](https://github.com/salamou1944/local-bridge./actions/runs/39519079143). Its job remains **queued** on labels `self-hosted, Windows, X64`; therefore no actual Windows machine, Codex CLI, or local Ollama availability has been proven through this runner yet.

## ChatGPT/Codex interpretation

The API Factory research file records the official Codex local/CLI/IDE route, subject to current ChatGPT plan limits: https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan. This is a coding-agent entitlement, not an OpenAI API key or always-on production inference endpoint. OmniRoute's Codex App-Server route requires a signed-in Codex CLI/app-server and current terms compliance. No ChatGPT/Codex login was performed in this audit.

## Next verified steps

1. Resolve the queued self-hosted runner job through the private repository's runner registration/status; never paste a runner token into chat.
2. If the Windows inventory completes, evaluate local Ollama feasibility from actual RAM, disk, CLI and model evidence.
3. Verify one official provider's free-tier eligibility and terms before configuring its protected secret. The free-API list and OmniRoute catalog are discovery sources, not free credentials.
4. Keep API Factory on the isolated Render preview while testing. Do not move main Render or Railway until durable storage, configuration, migration and deploy execution are verified.


## Fresh evidence checkpoint — 2026-10-21 02:15 UTC

This checkpoint refreshes the live evidence without treating old snapshots as current deployment proof.

### GitHub and workflow evidence
- Repeated repository search returned the same 10 repositories under `salamou1944`; the connected GitHub integration reports admin/write permissions for those 10. This is the connected integration's result, not a claim that no other repositories exist elsewhere or in accounts not connected here.
- COLLECTION cycle 17 remains the latest successful bounded cycle in the latest queried run window: [run 39517526827](https://github.com/salamou1944/Project-/actions/runs/39517526827). It refreshed 80/100 sources, preserved 20 blocked attempts, and reported 4,950 extracted artifacts / 4,970 manifest source rows. Current-main audit: 12,942 JSON/JSONC files, 0 parse failures, 907,402,672 bytes. The workflow explicitly returned `NO_APPROVED_CANDIDATES`; no source was installed/promoted.
- API Factory test [39517350761](https://github.com/salamou1944/Salamou-31/actions/runs/39517350761), SOAT integration smoke [39517350895](https://github.com/salamou1944/Salamou-31/actions/runs/39517350895), provider probe contract [39517350886](https://github.com/salamou1944/Salamou-31/actions/runs/39517350886), Railway token access smoke [39517350831](https://github.com/salamou1944/Salamou-31/actions/runs/39517350831), and Elite supervisor [39524196537](https://github.com/salamou1944/Salamou-31/actions/runs/39524196537) all report success. These are CI/access-contract evidence, not proof of a paid customer, successful production deployment, or free hosted inference.
- The local Windows inventory workflow [39519079143](https://github.com/salamou1944/local-bridge./actions/runs/39519079143) is still queued on a `self-hosted, Windows, X64` runner. No local PC inventory, installed Codex CLI, or installed Ollama has been proven through it.

### Runtime cross-check
- Railway still has five service definitions across two projects, no volumes in the inspected environments, and failed latest deployments in the reported snapshot. The `salamou31-api-factory` service remains inside EASY Runtime Production; do not use it as an API Factory target or alter EASY.
- Supabase project `dyhkdijpkddfsrwruumc` remains ACTIVE_HEALTHY; its `api-factory-storage` Edge Function is ACTIVE v3 and `public.api_factory_registry` has one singleton row with RLS enabled. The separate EASY project `rdcodzowehzmwdxhztxe` has `pastel_orders` with 41 rows and four active Edge Functions. Preserve the separation.
- Render exposes two Free services. Preview `salamou31-api-factory-preview.onrender.com` is the current integration-test target based on prior verified durable-storage smoke; main `salamou-31-api-factory.onrender.com` still has documented HTTP 503 `DURABLE_STORAGE_REQUIRED`. The preview may sleep while idle.
- Vercel still exposes one project `salamou31-api-factory`; its latest listed production deployment state is READY, but recent staging deployments include ERROR. No claim of durable storage or production readiness follows from READY alone.
- Replit returns three editable apps: `FragrantButteryApplicationframework`, `StarkImprobableText`, and `PracticalPastelCalculator`. The connected search did not find an app clearly named EASY Creative Prototype.
- Notion has one confirmed private operating-inventory page: جرد الموارد المتاحة وخطة التنفيذ — 2026-10-21. Earlier keyword searches had missed it; do not infer Notion was empty from a zero-result search.

### Free-model shortlist: verified repository facts versus account eligibility
- [OmniRoute](https://github.com/diegosouzapw/OmniRoute) is MIT-licensed and its current README advertises 467 free-tier catalog entries across 34 recurring pool keys, with a modelled aggregate estimate around 1.62B tokens/month. The README explicitly says to bring your own provider accounts; this is an estimate across third-party quotas, not free credit granted by OmniRoute. The project is a candidate gateway, not a provider and not yet installed or security-reviewed for our workload.
- awesome-free-llm-apis is CC0-licensed and is a discovery list, not a guarantee. Its current README labels Cohere's trial API as non-commercial; Google Gemini free-tier prompts may be used to improve products; Mistral free-mode prompts may be used for training unless the user opts out; Hugging Face inference credits are described as metered/limited. Verify current official terms, region, quota, data retention/training, and commercial-use rights before selecting any provider.
- No hosted provider has been upgraded to `VERIFIED` in this checkpoint: there is still no confirmed provider-specific free-tier setting plus a recorded live sentinel completion. Never set a billing-tier flag to `free` based on a catalogue claim alone.
- Preferred order remains: (1) complete local Windows inventory if the runner becomes available; (2) if local inference is not feasible, verify one provider's official free tier and privacy/commercial terms, then send one controlled sentinel request; (3) only then wire the chosen provider into the isolated Render preview. No new spend, no new service, no EASY credential reuse.

### Inventory completeness boundary
The inventory is complete only for the accounts/resources actually surfaced by the connected integrations and the queried pages. Items not readable through a connector are marked `not verifiable through current connection`, not `absent`. Remaining unresolved blockers are the queued Windows runner, provider free-tier eligibility/live completion, Render main-service migration, generated API durable usage/quota/idempotency storage, and a real external customer/revenue path.


## Fresh evidence checkpoint — 2026-10-21 02:27 UTC

This check repeated the live inventory queries after the 02:15 checkpoint. No credentials were read, no provider calls were made, and no deployments or paid actions were triggered.

### Reconfirmed
- GitHub connector: the same 10 repositories under `salamou1944` are visible with admin/write permission. The authenticated account has no organizations returned by the GitHub org-list endpoint; the installation list shows the user account `salamou1944`. This is the connector's visible scope, not a claim about other accounts.
- COLLECTION: latest successful run in the queried recent window remains [cycle 17, run 39517526827](https://github.com/salamou1944/Project-/actions/runs/39517526827). It reports 80/100 sources refreshed, 20 blocked attempts preserved, 4,950 extracted artifacts / 4,970 source rows, 12,942 JSON/JSONC files audited, zero parse failures, and `NO_APPROVED_CANDIDATES`. Do not describe extraction as installation or promotion.
- API Factory checks remain successful: [API Factory test 39517350761](https://github.com/salamou1944/Salamou-31/actions/runs/39517350761), [SOAT 39517350895](https://github.com/salamou1944/Salamou-31/actions/runs/39517350895), [provider probe contract 39517350886](https://github.com/salamou1944/Salamou-31/actions/runs/39517350886), [Railway token access 39517350831](https://github.com/salamou1944/Salamou-31/actions/runs/39517350831), and [Elite supervisor 39524196537](https://github.com/salamou1944/Salamou-31/actions/runs/39524196537). These are CI or access evidence only.
- Local Windows runner: [inventory run 39519079143](https://github.com/salamou1944/local-bridge./actions/runs/39519079143) is still queued; its job is queued with no runner or steps reported. Therefore there is still no fresh evidence that the connected Windows PC executed a command, or that Codex CLI/Ollama is installed there.
- Railway: direct environment inventory confirms 3 service definitions in EASY Runtime Production and 2 in EASY Developer Platform, with no volumes in either environment. Latest deployments reported for all five services are FAILED. The API Factory Railway service remains inside EASY Runtime Production and is not a safe target.
- Supabase: dedicated API Factory project remains ACTIVE_HEALTHY, with `public.api_factory_registry` (one singleton row, RLS enabled) and active `api-factory-storage` Edge Function v3. Separate EASY project remains ACTIVE_HEALTHY, with `public.pastel_orders` (41 rows, RLS enabled) and four active Edge Functions. Preserve project/data/secret separation.
- Render: two Free services are visible. Preview `salamou31-api-factory-preview.onrender.com` has latest listed deploy status `live` on commit `552f58043e7c3796bec07b838fb7638607be1b07`; this confirms a live deployment record, not a fresh HTTP readiness check. Main `salamou-31-api-factory.onrender.com` has latest listed deploy status `live` on commit `83f69126689eaac920f044b1e54cb8878d52fffc`, but its documented `/ready` result remains HTTP 503 `DURABLE_STORAGE_REQUIRED`. Do not switch the main service to the gateway without safe migration/readiness evidence.
- Vercel: one project `salamou31-api-factory` is visible. A READY deployment status alone does not prove a successful /ready probe, durable state, or production suitability.
- Replit: three editable apps remain visible; no app clearly named EASY Creative Prototype was found in the connected app list.
- Notion: the private inventory page exists and contains the accumulated inventory and execution order. An earlier zero-result keyword search was incomplete; it must not be used to claim that Notion is empty.

### Current decision / next actions
1. Do not attempt to force the queued Windows runner or expose a registration token. The runner must be registered/online on the Windows host before that workflow can run; this cannot be repaired from GitHub repo write access alone.
2. In parallel, inspect official provider terms and eligibility for one candidate, then make exactly one controlled sentinel request only after a protected credential and confirmed free tier are available. A catalog entry is not a credential or quota.
3. Continue API Factory work against the isolated Render preview only. First verify its current `/ready` response and storage gateway configuration; then address generated API usage/quota/idempotency persistence and the missing real deployment adapter. No production-ready claim until external smoke evidence passes.
4. Continue COLLECTION in bounded, verified cycles; only trigger the next cycle after reading the actual prior run output. Preserve the fail-closed no-install policy.
5. Keep a single paid-offer objective in parallel: use the existing outreach/CRM resources to validate one small service offer before spending on tools or ads.

### Scope statement
This is a repeated inventory of resources exposed through the connected integrations and the queried pages as of this timestamp. Any account/service not returned by those integrations remains outside the evidence boundary; do not relabel it as nonexistent or free.


## Additional connector and free-tier check — 2026-10-21 02:30 UTC

- Termalin `hosts_list` returned an empty host list and explicitly stated that saved hosts in the Termalin cabinet are not visible until the connector runs on the server. No shell command can be run on the user's computer/server through Termalin in this session.
- The connected Browser tool returned: “Browser access requires the originating browser context.” Therefore I cannot currently control/read the user's open browser tab through that connector. This is a connection-context blocker, not proof that the browser or computer does not exist.
- Render event history confirms successful build/deploy events for the current preview commit `552f58043e7c3796bec07b838fb7638607be1b07` and main commit `83f69126689eaac920f044b1e54cb8878d52fffc`. A request-log query for `/ready` returned no matching request entries in the queried 7-day window; therefore no new HTTP readiness result was established in this check. The last documented main `/ready` result remains HTTP 503 `DURABLE_STORAGE_REQUIRED`.
- Official Gemini API terms effective 2026-03-23 state that content submitted through unpaid services (including unpaid Gemini API quota/AI Studio) may be used to improve/develop Google products and ML technologies, and human reviewers may process inputs/outputs. Do not send sensitive/confidential/user/customer data through the unpaid tier. The official pricing page currently lists free-tier access for some models, but model availability and rate limits are model-specific; this still does not establish the user's account eligibility. Sources: [Gemini API terms](https://ai.google.dev/gemini-api/terms?hl=en), [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing.md), [Gemini billing](https://ai.google.dev/gemini-api/docs/billing/).
- The live endpoint probe attempted through the available web fetch interface could not access either Render `/ready` URL. This is a tool-access limitation; it is not a pass or a fail for the services. The next useful action is an authenticated/allowed external smoke via the existing workflow or service-side test, not assuming browser access.

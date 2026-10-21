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
- The owner-scoped repository listing returned 10 repositories under `salamou1944`; a separate organization-member affiliation query also exposed the public `Sssssssddddd/.github` repository. Thus 11 repositories are currently verified through the GitHub integration. The organization-membership list itself returned empty, but that does not override the direct repository evidence. Other accounts not connected here remain outside this inventory.
- At the time of the first checkpoint, cycle 17 was latest. It has since been superseded by cycle 18: [run 39533389021](https://github.com/salamou1944/Project-/actions/runs/39533389021), which refreshed 79/100 sources, preserved 21 blocked attempts, and reported 5,029 extracted artifacts / 5,050 manifest source rows. Current-main audit: 13,021 JSON/JSONC files, 0 parse failures, 916,967,626 bytes. The workflow explicitly returned `NO_APPROVED_CANDIDATES`; no source was installed/promoted.
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


## Fresh evidence checkpoint — 2026-10-21 02:35 UTC

### COLLECTION
- Cycle 18 [completed successfully](https://github.com/salamou1944/Project-/actions/runs/39533389021): 100 selected, 79 refreshed, 21 blocked attempts preserved; 5,029 extracted artifacts / 5,050 manifest source rows; 18,551 repositories deferred.
- Current-main audit: 13,021 JSON/JSONC files, zero parse failures, 916,967,626 bytes. Capability/readiness groups 45,415; promotion review items 31,108; restricted items 14,307.
- Installation remains explicitly blocked by `NO_APPROVED_CANDIDATES`: zero installed and zero ready for verification. Do not turn an empty approved queue into an installation claim.
- Large generated files still need a deliberate format/partitioning design: `READY.json` is 79,542,593 bytes and `CANONICAL-PROMOTION-PLAN.json` is 53,727,383 bytes. Current guards pass but these exceed the recommended 50 MB repository size.

### Current free AI route assessment
- [OmniRoute](https://github.com/diegosouzapw/OmniRoute) is an active MIT-licensed router and may reduce provider integration work, but it does not grant ChatGPT/API quota. It needs eligible upstream provider accounts/credentials; its ChatGPT Web/Codex adapter must not be treated as a supported production API without implementation and terms review.
- [awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) is a CC0 discovery list, not an API key or guarantee of free service. Confirm every candidate against its official pricing/terms and account eligibility.
- API Factory's current ranked options remain: (1) local Ollama after actual PC/hardware verification, (2) Gemini free-tier probe after confirming the account/model's eligibility, (3) Groq or OpenRouter free models after official eligibility confirmation. Current provider probes deliberately skip live calls when the explicit free-tier confirmation is empty. No provider is currently promoted to LIVE_VERIFIED based on a skipped probe.
- ChatGPT Free/Codex can support local coding-agent use within plan limits, but it is not a general OpenAI API key, an always-on inference endpoint, or production API quota. Do not use browser cookies/session scraping or unsupported account-session adapters to fake API access.
- GitHub Models inference API was retired 2026-07-30; do not plan new runtime work around it.

### Local computer / access boundary
- Private [local-bridge runner workflow](https://github.com/salamou1944/local-bridge./actions/runs/39519079143) is still queued on `self-hosted, Windows, X64`; no local PC hardware, installed Codex CLI, or local Ollama has been verified through it. The prior workflow's successful CI/metadata checks do not prove the Windows runner is connected.
- Browser connector reports that the originating browser context is required; no GUI automation is available from this session. Termalin's connected host listing returned no available hosts.
- Therefore the next local-resource step is to make the already configured Windows runner appear Idle in GitHub, then run the read-only inventory workflow. Do not paste runner registration tokens into chat.

### Plan checkpoint
1. Finish inventory of accessible service settings and repository roles; mark inaccessible accounts as unknown, not empty.
2. Resolve the Windows runner and record actual hardware/tool inventory.
3. Validate one official free provider with a real sentinel completion and saved evidence; no paid fallback.
4. Use the existing isolated Render preview as the API Factory baseline; do not alter main Render or Railway/EASY. Finish deployment adapter and generated API state persistence before claiming production readiness.
5. Return to COLLECTION install selection only when candidates have evidence, license/security review, and explicit policy approval.


## Connected-account refresh — 2026-10-21 02:50 UTC

This refresh is read-only. It does not inspect or persist API keys, passwords, session cookies, customer messages, or payment credentials.

### Commercial and outreach accounts
- **Apollo:** fresh profile reports 80 lead credits remaining, 160 direct-dial credits effective, 5,000 AI credits, and zero used in the profile. The team usage endpoint reports 80 lead credits, 80 direct-dial credits remaining (limit 160), 150 conversation credits, 5,000 AI credits, 20 inbound-website-visitor credits, and 50,000 broadcast credits; all show zero consumed. Direct-dial balance remains inconsistent across the two official connector views; treat 80 as the conservative usable remainder until reconciled. No credits were consumed by this audit.
- **AgentMail:** 3 inboxes exist: `easy@agentmail.to`, `api-pilot@agentmail.to`, and `pastel-realtime-e2e@agentmail.to`. The accounts endpoint returned zero external app sign-ins. This does not mean the inboxes are absent; it means no connected app account was listed. No messages were read or sent in this check.
- **HubSpot:** organization-details query failed because the account does not have the Brands add-on. This is a feature limitation, not a broken CRM connection. Organization details still need a fresh query without BRANDS.
- **Automations:** 5 automations exist. Only `Revenue + leverage sweep` is enabled; its schedule says daily but `next_run_time` is null and last run was 2026-10-20 03:38 UTC. Do not assume it is actually scheduled to run again until scheduler behavior is verified. `Daily collection digest` is disabled; 3 other automations are also disabled. This should be treated as a scheduling reliability gap.
- **Shopify:** connected store is `My Store`, domain `2eih8n-pc.myshopify.com`, country Algeria, currency DZD, plan trial. Required account notice: "Plan: trial — you'll need to upgrade before you can start selling and unlock full features". The read-only Digital Products connection test reports that the app is not installed. Do not upgrade or install paid apps as part of this no-spend plan.
- **Metricool:** one connected brand was returned with a YouTube channel ID `UCR8aUjgimgvbCOucYaHY8ZA`. This confirms a linked channel identity, not that the intended channel has uploads or revenue.
- **Higgsfield:** selected workspace is Free with 10 credits; free generations are empty and the optional trial remains pending/eligible. Do not start the trial or spend credits without an explicitly selected use case.
- **Canva:** no Brand Kits returned.
- **Figma/Weave:** the Figma Weave integration says the Figma account has not been linked to Weave. This is distinct from the separately installed Figma connector; no account-link action was taken.
- **Wix:** the connected account returned zero sites.
- **GitBook:** the first list attempt did not provide an organization ID and failed. Site inventory remains unknown until the accessible organization list is queried; do not treat the failed call as proof there are no sites.
- **OpenAI Platform:** the key-setup target lookup exposed three organizations/projects (including Team easy / Easy and two default projects). This only proves that API-key setup targets are accessible; it does not prove that a key exists, that API credits are available, or that inference is free. No key was created and no billing setting was changed.
- **GitHub:** profile is the personal account `salamou1944`; one GitHub App installation is visible with repository selection set to all. The integration search surfaced 10 repositories with write/admin permissions. This is the connected installation scope, not proof there are no additional repos outside it.
- **Railway:** current service inventory is unchanged: 3 services under EASY Runtime Production and 2 under EASY Developer Platform. Do not deploy API Factory into the EASY project.
- **Render:** two Free services remain present: API Factory preview and main. Preview is the reference environment; main's last recorded readiness failure remains HTTP 503 `DURABLE_STORAGE_REQUIRED`.
- **Local PC:** the private self-hosted runner job remains queued; browser GUI context and Termalin host access are unavailable. A real machine inventory still cannot be completed remotely from this session.

### Decisions from this refresh
1. Do not spend Apollo, Higgsfield, Shopify, or provider credits until a concrete monetization path is selected.
2. Use the existing AgentMail inboxes for replies/outreach only after inspecting the relevant inbox as a separate task; this refresh did not read messages.
3. Treat the null automation next-run timestamp as an open reliability issue; do not rely on the daily sweep as the sole operating control.
4. Keep the plan no-spend: no Shopify upgrade, no paid add-ons, no provider billing activation, no new Render/Railway services, and no API-key creation.


### Remaining integration checks — 2026-10-21 02:55 UTC
- GitHub's authenticated profile lists no organizations or organization memberships, but the affiliation-filtered repository list independently exposes `Sssssssddddd/.github` (public organization-wide community-health files). Treat the repo as accessible evidence even though the org-list endpoint is empty. Current verified repository scope is 10 personal-owner repositories plus this one organization-owned repository.
- GitBook's authenticated organization-list operation returned an empty list. Therefore there are no GitBook organizations/sites visible through this connection; do not treat GitBook as a usable hosting/documentation asset unless a valid organization becomes available.
- HubSpot's fresh organization-details query succeeded when requested without BRANDS: portal `easy`, account type STANDARD, company currency USD, timezone US/Eastern, seat type `gtm`, no teams and no job titles. The Brands add-on is absent. This is CRM account metadata only; it does not establish an active deal pipeline.
- Notion private/shared/favorites listings were empty, and recent pages surfaced the inventory page only. The inventory page itself is reachable by direct URL and has been updated; do not infer broader Notion databases from that single page.
- The current GitHub App installation covers the personal account's all-repository selection; the owner-scoped listing returned 10 personal repositories and the affiliation-scoped listing additionally exposed Sssssssddddd/.github. The verified editable scope is therefore 11 repositories. The empty organization-membership list does not negate this direct repository access; any other intended repo still needs an exact lookup.


## Fresh verification checkpoint — 2026-10-21 11:20 Algeria time

This update records a second direct inspection of connected GitHub, Railway, Supabase, Vercel, Replit, Notion, and the free-model research repositories. It supersedes older status snapshots only where the same fact is explicitly rechecked here. No secrets were read, copied, or changed; no paid API request, service creation, billing activation, or deployment was performed.

### Confirmed current project inventory

- **GitHub personal account:** authenticated as `salamou1944`; one GitHub App installation visible, repository selection `all`; owner-scoped repository listing returned 10 editable personal repositories: `Salamou-31`, `agent-skills`, `Easy-`, `AI_operating_memory`, `Astra-`, `Astra`, `Files-`, `Project-`, `Pastel-`, and private `local-bridge.`. The separately discovered public `Sssssssddddd/.github` is also accessible, giving 11 verified repositories in this inventory. GitHub's organization-membership endpoint returned an empty list; that endpoint result does not negate direct access to the organization repository. This is the visible integration scope, not proof about unconnected accounts.
- **COLLECTION:** latest verified successful bounded run remains cycle 18, [39533389021](https://github.com/salamou1944/Project-/actions/runs/39533389021): 100 selected, 79 refreshed, 21 blocked attempts preserved; 5,029 extracted artifacts / 5,050 manifest rows; 18,551 deferred repositories. The current-main JSON audit passed with 13,021 JSON/JSONC files, zero parse failures, and 916,967,626 bytes. Latest generated state reported 45,415 capability/readiness groups, 31,108 promotion-review items, and 14,307 restricted items. Installation outcome remains `NO_APPROVED_CANDIDATES`; zero items were installed. Two generated JSON files remain above GitHub's recommended 50 MB: `READY.json` about 79.5 MB and `CANONICAL-PROMOTION-PLAN.json` about 53.7 MB; size guards pass, but this is a maintainability/clone-cost risk.
- **API Factory CI:** latest commit `cf761d3f52f507d9849adbc75f77c93a37dadd83` has successful [API Factory Test 39535393169](https://github.com/salamou1944/Salamou-31/actions/runs/39535393169), [P1 Provider Probe Contract 39535393192](https://github.com/salamou1944/Salamou-31/actions/runs/39535393192), [Railway Token Access Smoke 39535393145](https://github.com/salamou1944/Salamou-31/actions/runs/39535393145), [SOAT Runtime Integration Smoke 39535393138](https://github.com/salamou1944/Salamou-31/actions/runs/39535393138), and Elite supervisor [39551684299](https://github.com/salamou1944/Salamou-31/actions/runs/39551684299). These are test/access evidence, not a verified production deployment or live hosted-model completion.
- **Supabase API Factory project** `dyhkdijpkddfsrwruumc`: project state `ACTIVE_HEALTHY`; public table `api_factory_registry` has one row and RLS enabled; Edge Function `api-factory-storage` is ACTIVE version 3. This is the isolated API Factory storage project.
- **Supabase EASY project** `rdcodzowehzmwdxhztxe`: project state `ACTIVE_HEALTHY`; public `pastel_orders` table has 41 rows; active Edge Functions are `easy-customer-auth` v3, `pastel-order` v1, `pastel-tts` v1, and `pastel-tts-v2` v2. Keep this project and its secrets/data separate from API Factory.
- **Railway:** the inspected production environments contain three services under `EASY Runtime Production` and two under `EASY Developer Platform`. All five have no attached volumes, and the latest deployment records in the inspected snapshot are FAILED. The `salamou31-api-factory` Railway service is inside EASY Runtime Production, has no configured variables in the environment inventory and no volume, and must not be used as the API Factory target. The Railway token-access smoke proves read access only, not deployment readiness. Do not change or redeploy EASY services as a shortcut.
- **Vercel:** one project `salamou31-api-factory` is visible. The deployment list contains a READY production deployment, a READY staging deployment, and recent ERROR staging deployments. READY is only the deployment platform's state; it does not prove durable storage or a successful authenticated `/ready` check. Existing persistence notes say Vercel remains fail-closed without the storage gateway configuration.
- **Render:** the earlier inventory shows two Free services: `salamou31-api-factory-preview` and `salamou-31-api-factory`. The preview is the established test target with prior durable-storage verification; the main service's last documented `/ready` result remains HTTP 503 `DURABLE_STORAGE_REQUIRED`. This session did not query Render again because its connector requires explicit workspace selection before further actions. Do not change the main service until the migration/configuration and existing local state are verified.
- **Replit:** three editable apps are visible: `FragrantButteryApplicationframework`, `StarkImprobableText`, and `PracticalPastelCalculator`. Targeted searches for `EASY` and `API Factory` returned no matches; the old prototype was not found in this connected app listing, which does not prove it was deleted or inaccessible elsewhere.
- **Notion:** the private page [جرد الموارد المتاحة وخطة التنفيذ — 2026-10-21](https://app.notion.com/p/400791c044f98169a48cfb4482a298b6?pvs=204) is reachable and contains the wider connected-account inventory. Private/shared/favorite listings did not reveal additional confirmed project databases in the prior checks; do not infer that unconnected workspaces are empty.
- **Local computer:** private repository [local-bridge.](https://github.com/salamou1944/local-bridge.) is the designed Windows self-hosted-runner bridge. Its read-only machine inventory run [39519079143](https://github.com/salamou1944/local-bridge./actions/runs/39519079143) is still queued, with its `inventory` job queued and no steps executed. Therefore this session has not verified PC RAM/GPU/disk, local Ollama, Codex CLI, or the Windows runner's connection. Browser connector also requires the originating browser context, and Termalin's connected host listing returned no hosts. Do not claim direct computer access until this bridge reaches an Idle runner and completes.

### Free AI / ChatGPT-compatible routes — evidence and limits

- [OmniRoute](https://github.com/diegosouzapw/OmniRoute) is MIT-licensed routing software; its README explicitly says **bring your own provider accounts**. Its free-token aggregate is an estimate across independent third-party quotas, not a quota granted by OmniRoute. It may reduce integration work, but it is not a free ChatGPT subscription/API grant and is not yet installed or security-reviewed for our workload.
- [awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) is CC0 discovery metadata. It lists potential provider free tiers, but it is not an account credential or guarantee. Candidate paths include local Ollama (CI completion proven only, not PC readiness), Google Gemini API, Groq, OpenRouter free models, Mistral, Cloudflare Workers AI, and Hugging Face. Each hosted candidate remains unverified for our account until official terms/model eligibility are confirmed and a deterministic live sentinel completion is recorded.
- The current API Factory document ranks Ollama as the first no-hosted-bill option after local machine verification, then Gemini/Groq/OpenRouter only after account/model eligibility is confirmed. Current provider gates correctly skip network requests when the free-tier confirmation is missing. Do not set a billing-tier flag to `free` just because a public catalog lists a free plan.
- ChatGPT Free may include the supported local Codex coding-agent experience within plan limits, but that is not a general OpenAI API key, free API quota, or always-on production endpoint. Do not use browser cookies/session scraping or unsupported web-session adapters to simulate API access.
- GitHub Models inference API was retired on 2026-07-30; do not build a new runtime on it.
- Free-tier data terms matter: the previously checked official Gemini terms allow unpaid-tier content to be used to improve Google products and ML systems; no secrets, customer data, or confidential business data should be sent through that tier. Review current provider terms and commercial-use limits before any real test.

### Execution plan now grounded in the inventory

1. **Unblock the Windows runner** through the private repository's runner settings and confirm it appears Idle; then run the existing read-only inventory workflow. Do not paste a runner registration token into chat.
2. **Prove one no-cost inference route**: first determine whether a suitable local model is feasible from actual hardware; otherwise verify existing provider account/model eligibility, run exactly one non-sensitive sentinel request, disable paid fallback, and save response metadata. Do not create keys or activate billing without a separate explicit approval.
3. **Keep API Factory isolated on the existing Render preview** while completing the real Railway/Vercel deployment adapter and durable generated-API usage/quota/idempotency storage. Main Render stays blocked until safe storage/config migration is proven. Do not deploy into EASY.
4. **Continue COLLECTION safely** after reading the latest run result; keep install/promotion closed until a candidate has evidence, license/security review, and approval. Address the >50 MB generated JSON files with a tested partition/index approach, not deletion or lossy compaction.
5. **Choose one commercial path** from existing assets after the technical baseline is known; prove a real user-facing flow and customer acquisition before spending credits or adding subscriptions.

### Coverage boundary

This is a complete snapshot of the resources surfaced by the connected integrations and exact queried project/repository pages as of 2026-10-21 11:20 Algeria time. It cannot assert facts for external accounts not connected to these integrations, billing screens not exposed by read-only tools, or the local PC while its runner remains queued. Such items are recorded as **not verified through this connection**, not silently treated as absent. No secrets were read or saved, and no paid operations were performed.

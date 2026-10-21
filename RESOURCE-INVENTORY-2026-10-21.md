# Connected Resource Inventory and Execution Plan — 2026-10-21

Last checked: 2026-10-21 (UTC). This is an evidence-based snapshot of resources visible through the connected integrations, not a claim that every service is production-ready. Never store credentials, API keys, tokens, or raw secrets in this file.

## 1. Operating rules

- No paid upgrade, new billable service, or payment method without explicit approval.
- Do not reuse EASY production data/storage/credentials for API Factory.
- Preserve existing data; fail closed on uncertain persistence or provider status.
- Distinguish configured, reachable, tested, and production-proven.
- GitHub source and test logs are the source of truth for code state; provider dashboards are the source of truth for service configuration.
- No credential copying into repositories, prompts, browser-visible pages, or client code.

## 2. GitHub repositories accessible under salamou1944

The connected GitHub search returned these 10 repositories, with write/admin permissions on each at the time of inspection:

| Repository | Visibility | Operational role / known use |
|---|---|---|
| [Salamou-31](https://github.com/salamou1944/Salamou-31) | Public | API Factory, provider adapters, storage gateway, tests and deployment notes |
| [AI_operating_memory](https://github.com/salamou1944/AI_operating_memory) | Public | Canonical operating memory, capability map, state and decision policies |
| [Files-](https://github.com/salamou1944/Files-) | Public | File/resource project; inspect repo content before assigning runtime role |
| [Astra](https://github.com/salamou1944/Astra) | Public | Knowledge/evidence repository; inspect actual contents before claiming functionality |
| [Pastel-](https://github.com/salamou1944/Pastel-) | Public | Pastel project and its Supabase order/TTS functions |
| [agent-skills](https://github.com/salamou1944/agent-skills) | Public | Control-plane skills, workflows, automation and project supervisor |
| [Easy-](https://github.com/salamou1944/Easy-) | Public | EASY commerce/creative engine source |
| [local-bridge.](https://github.com/salamou1944/local-bridge.) | Private | Diagnostics and share-metadata workflows; two sampled runs passed. This does not prove a persistent self-hosted runner exists. |
| [Project-](https://github.com/salamou1944/Project-) | Public | COLLECTION inventory, extraction, audit, classification and verification workflows |
| [Astra-](https://github.com/salamou1944/Astra-) | Public | Additional Astra repository; do not assume duplicate purpose without inspection |

Known external reference repositories:
- [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) — MIT licensed gateway; project README describes 375 providers and 150+ free-tier entries, but requires users to bring eligible provider accounts/credentials. The advertised aggregate free-token budget is not a grant from OmniRoute.
- [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) — CC0 list of purported free-tier APIs. Provider quotas and terms must be verified against official docs before use. The latest inspected commit removed a malicious credential-stealing security-audit workflow; treat lists as discovery inputs, not trusted executable code.

## 3. Connected deployment and database accounts

### Railway

Two projects are visible in the connected account:

**EASY Runtime Production**
- Services visible: `salamou31-api-factory`, `easy-runtime`, `easy-runtime-current`.
- The API Factory service has no attached volume; its latest deployment is FAILED. It is in an EASY production project and must not be used for a new API Factory rollout without explicit isolation and cost/safety review.
- The EASY services also report failed latest deployments in the dashboard snapshot; do not infer current endpoint health from service labels alone.
- No volumes/buckets were reported in the inspected environment; no shared variables were exposed by the project summary.

**EASY Developer Platform**
- Services visible: `easy-platform-runtime-v3`, `soat-production-runtime`.
- No attached volumes or buckets reported; both latest deployments were FAILED in the inspected metadata.
- A shared variable name `Easy_github_token` is configured at project scope. The value was not retrieved or recorded.

Conclusion: Railway is not currently the safe first choice for API Factory deployment. First use the already-configured Render preview, then resolve the deployment adapter only when the destination is isolated and validated.

### Supabase

Two projects are visible; both dashboard statuses were `ACTIVE_HEALTHY`.

**Dedicated Salamou-31 API Factory project**
- Project: `salamou-31-api-factory` (region `eu-west-1`).
- Active Edge Function: `api-factory-storage`, version 3, JWT verification disabled at the function gateway (the handler must validate its own internal key).
- Table `public.api_factory_registry`: RLS enabled, one singleton row, payload JSONB and updated timestamp.
- The Render preview is documented as using this project via the storage gateway. The main Render service is not yet migrated to this durable configuration.
- A live database status is not proof that every storage path or API request is durable; readiness must verify authenticated registry read/write and artifact upload/download.

**EASY platform database**
- Project: `easy-platform-db` (region `eu-west-1`).
- Active Edge Functions: `easy-customer-auth` v3, `pastel-order` v1, `pastel-tts` v1, `pastel-tts-v2` v2.
- Table `public.pastel_orders`: RLS enabled, 41 rows in the inspected snapshot. Treat this as existing user data; do not alter as part of API Factory work.
- Keep this project isolated from API Factory.

## 4. Render

Workspace visible: `salamou1944` project workspace.

- **Main:** [salamou-31-api-factory](https://salamou-31-api-factory.onrender.com), Render Free plan, Frankfurt, Docker context `AI-API-HUB/api-factory`, branch `main`, auto-deploy on commit. Latest documented external readiness smoke: HTTP 503 `DURABLE_STORAGE_REQUIRED`; registry and artifact modes are `local-file`. Process is reachable, but it is not production-ready.
- **Preview:** [salamou31-api-factory-preview](https://salamou31-api-factory-preview.onrender.com), Render Free plan, Frankfurt, Docker context `AI-API-HUB/api-factory`, branch `fix/api-factory-live-storage-readiness-2026-10-20`, auto-deploy on commit. Prior external smoke documented `DURABLE_STORAGE_VERIFIED` (HTTP 200) with dedicated Supabase gateway and artifact write/readback. Free service may sleep while idle; this is not an uptime guarantee.
- Both services have public network allow-lists. Keep admin or internal endpoints protected at the application layer. Do not expose internal API keys.

## 5. Vercel

- Project `salamou31-api-factory` is visible.
- Latest listed deployment: production target state `READY`, URL [salamou31-api-factory-h82t0tc1b-bleu5.vercel.app](https://salamou31-api-factory-h82t0tc1b-bleu5.vercel.app). Several recent staging deployments for the storage-readiness branch are `ERROR`.
- Deployment state READY only proves that Vercel built/deployed an artifact; it does not prove configured durable storage, correct API credentials, successful request processing, or production readiness.
- Existing docs state Vercel remains fail-closed until the storage gateway URL and matching internal key are configured and tested. Vercel `/tmp` and local-file modes are not durable.

## 6. Replit

The connected Replit account returned three editable apps:
- [FragrantButteryApplicationframework](https://replit.com/@salamou1944s/FragrantButteryApplicationframework), last updated 2026-10-02.
- [StarkImprobableText](https://replit.com/@salamou1944s/StarkImprobableText), last updated 2026-09-12.
- [PracticalPastelCalculator](https://replit.com/@salamou1944s/PracticalPastelCalculator), last updated 2026-09-11.

These names do not prove they are the latest EASY prototype. Search did not return a clearly titled EASY creative app. Inspect the app source/URLs before relying on them as production services.

## 7. Notion, browser and Termalin

- The Notion private page [جرد الموارد المتاحة وخطة التنفيذ — 2026-10-21](https://app.notion.com/p/400791c044f98169a48cfb4482a298b6) exists and contains the broader cross-account inventory; initial keyword searches missed it. Use it as the operating dashboard, while GitHub remains canonical for code, commits and test evidence.
- Browser connector call reported that browser access requires the originating browser context. No browser automation was completed in this audit.
- Termalin host-list call returned no available hosts through this ChatGPT connection. This does not prove the external Termalin account has no hosts; it means no host can be operated through the current connector result.
- No connected desktop or self-hosted GitHub runner was proven available. Sampled `local-bridge.` workflows ran successfully, but job success alone does not prove that a persistent runner exists or that ChatGPT itself can run on it.

## 8. Free model / API options: what is real and what is not

1. **OmniRoute:** best candidate for a unified provider router, not a source of free credentials. Install/run only after inspecting its dependency/supply-chain and credential-handling paths. Connect one verified free-tier provider first and run a minimal test. Do not route private or business data to providers until their retention/training terms are acceptable.
2. **awesome-free-llm-apis:** useful discovery list, not runtime. Check official provider terms, geographic availability, rate limits, data retention/training and whether a credit card is required. Some trial APIs are non-commercial; do not use those for revenue-generating workloads.
3. **Official provider free tiers:** Google Gemini, Mistral, Cohere and others are listed in the external catalogue, but current quotas, model availability and account eligibility must be verified from each official provider page before activation. Do not set environment variables to a supposed free tier until the account actually has eligible access.
4. **Ollama/local inference:** a real no-provider-fee path only if a reachable machine has enough RAM/VRAM and is kept running. The current GitHub CI test that ran a local Ollama completion is evidence for that CI job only; it does not establish a persistent production inference endpoint.
5. **ChatGPT account:** no inspected connector or GitHub repository proves that a ChatGPT subscription can be turned into an authorized general-purpose API endpoint for API Factory. Do not treat a ChatGPT login, GitHub account, or the OmniRoute project description as a free OpenAI API key.

## 9. Verified COLLECTION state

Repository: [Project-](https://github.com/salamou1944/Project-)
- Latest successful bounded cycle inspected: [run 39517526827](https://github.com/salamou1944/Project-/actions/runs/39517526827), cycle 17.
- 80/100 repositories refreshed; 20 blocked attempts preserved; 4,950 extracted source artifacts; 4,970 manifest source rows; 18,630 repositories deferred.
- Current-main JSON audit: 12,942 JSON/JSONC files; 0 parse failures; 907,402,672 bytes.
- Classification snapshot: 44,828 capability/readiness groups, 30,691 promotion-review items, 14,137 restricted items, 55 skill definitions.
- Promotion/install gate returned `NO_APPROVED_CANDIDATES`: no assets installed or promoted. This is a safe no-op, not proof that the queue is empty.
- Large generated JSON files pass the repo's size guard, but `READY.json` and `CANONICAL-PROMOTION-PLAN.json` exceed GitHub's recommended 50 MB file size; maintain guardrails and prefer line-oriented/delta artifacts for future updates.

## 10. Verified API Factory state and next execution order

- Provider contract tests prove fail-closed tier/credential gates, not successful calls to live providers. The latest reviewed NVIDIA NIM, Cloudflare Workers AI, Mistral and Hugging Face gates had no credentials/tier configured, so no live request was made.
- SOAT integration test produced deterministic output `4` from a CI-local Ollama runtime. This is test evidence only, not production inference availability.
- Storage gateway has an active Supabase Edge Function and a dedicated registry table; the Render preview has prior durable-readiness smoke evidence. Main Render remains HTTP 503 until safely configured/migrated.
- API Factory deployment adapter for Railway/Vercel remains unimplemented. Generated API request-idempotency, usage, quota and application/business data are not automatically durable just because registry/artifacts persist.

### Priority order

1. **Do not deploy to Railway or change main Render yet.** Use preview as the safe integration target while verifying the gateway config and actual end-to-end contract.
2. **Test one official free provider first** (prefer Gemini or Mistral only after verifying the user account's actual eligible tier, privacy terms and rate limits). Keep provider credentials in protected service secrets; never commit or paste them into chat.
3. **Evaluate OmniRoute in an isolated, non-production test**. Review license, install scripts, secret storage, logging and provider terms before integrating. Start with a disposable test key and a harmless prompt.
4. **Build/verify the runtime deployment adapter and provider smoke test** only after a safe target and secrets are configured.
5. **Finish durable state design for generated APIs** (idempotency, quota/usage ledger, business data) and add migration/restore tests.
6. **Continue bounded COLLECTION cycles**, validate actual workflow output, and use its extracted evidence to rank candidates. Never promote/install merely because a repo appears in the collection.

## 11. Explicit non-goals for this audit

- No secrets were read into or written from this inventory.
- No paid service was created or upgraded.
- No production deployment or provider API call was made.
- No EASY database or runtime data was modified.
- No third-party code was installed or executed as part of this audit.


## 12. Repository purpose cross-check (README evidence)

- `Astra`: ASTRA Quant Lab v1.7.0 is research-only. Real Kraken data was verified, but single-asset and cross-asset research gates failed; live-money execution is off. This is not a proven profitable strategy.
- `Astra-`: executable ASTRA private trading bot boundary with Kraken public OHLC ingestion, paper execution, idempotent intent ledger, kill switch and gated authenticated order adapter. Live trading remains OFF; do not merge it with the research repo's evidence or claim profitability.
- `agent-skills`: engineering control plane for reusable skills, Elite autonomous coding, ARMY-14 verification and MONY/Revenue Engine workflows. It includes many automation workflows, but each run still needs task-specific evidence.
- `Pastel-`: PASTEL QR Concierge static/mobile-first site. Its README explicitly says not to replace the existing QR destination until GitHub Pages is live and tested on a real phone. The Supabase database also contains Pastel order and TTS functions.
- `Files-`: the README contains only a title; no operational capability is inferred from that alone.
- `Project-`: README is minimal; its actual COLLECTION automation and evidence are recorded in the COLLECTION index and verification reports.
- `local-bridge.`: private control point for a Windows self-hosted GitHub Actions runner. The README requires registering the runner from the Windows machine; connecting GitHub alone does not connect the laptop.
- `Easy-`: the attempted README lookup returned 404, so this audit does not infer its runtime state from that file. The repository exists and is writable, but source-level inspection is still required before claiming implementation readiness.

## 13. Local computer / runner check

A read-only one-shot inventory workflow was committed to `local-bridge.` and triggered as run [39519079143](https://github.com/salamou1944/local-bridge./actions/runs/39519079143). Its job targets `[self-hosted, Windows, X64]` and only checks installed command availability, basic OS/CPU/RAM/C: free space, Ollama localhost API/model names, and names in the explicitly approved share directory. It does not read secret values or files outside that share and makes no external network requests. At the time of the last check, the job was **queued**, not completed. Until it runs successfully, the Windows machine, Codex CLI, Ollama and local model availability are not verified. Do not describe GitHub Actions as running on the user's computer unless this job completes on the self-hosted runner.

## 14. Execution order updated from the inventory

1. Check whether the one-shot local-bridge job completes. If it remains queued, inspect the repository runner registration/status in GitHub Settings; do not work around it by running arbitrary shell commands or exposing a registration token.
2. Use the local inventory result, if available, to decide whether a zero-provider-fee Ollama path is viable on the actual Windows machine (RAM, disk, Ollama CLI/API, model availability).
3. In parallel, validate one provider from the free-tier catalogue against official pricing/terms and account eligibility. Do not assume ChatGPT subscription access is an API key.
4. Keep Render preview as the first isolated API Factory target. The current main service and Railway service are not suitable targets until durable state, credentials and deployment execution are verified.
5. Record the actual runtime smoke and storage tests in API Factory docs, then build and test the generated API's own usage/quota/idempotency persistence.
6. Continue COLLECTION only in bounded, evidence-checked cycles; current queue is large and no promotion/install is approved.

# Resource Inventory Supplement — 2026-10-21

This supplements [the connected resource inventory](./RESOURCE-INVENTORY-2026-10-21.md) with repository-level checks completed after its first commit. No credentials were read or stored.

## Confirmed repository roles

- [Easy-](https://github.com/salamou1944/Easy-) is the EASY commerce/creative-engine source. Root contains project boundary/rules, package.json, app/apps, api-lab, api-registry, commerce-connector, knowledge-bank, platform, services, src and test. Package `easy-seller-mvp` v0.1.0 uses Node test/check scripts and depends on `@fal-ai/client`. Production requires a real provider adapter, durable persistence, auth, request IDs, integrity checks and a deployed end-to-end test.
- [Files-](https://github.com/salamou1944/Files-) currently contains `collection/mufeedvh/`; the README is only a title, so this is source collection, not a verified runtime.
- [Project-](https://github.com/salamou1944/Project-) contains the bounded COLLECTION pipeline, audit/classification outputs and opportunity/service-pack records.
- [Astra](https://github.com/salamou1944/Astra) is ASTRA Quant Lab research. Kraken data ingestion is verified, but single-asset and cross-asset research gates failed; profitability is not proven and live money is off.
- [Astra-](https://github.com/salamou1944/Astra-) is the separate trading-bot boundary with paper execution, idempotency ledger and kill switch. Live trading remains off; do not conflate it with research evidence.
- [agent-skills](https://github.com/salamou1944/agent-skills) contains reusable skills, Elite engineering automation, ARMY-14 verification, MONY/Revenue Engine and workflows.
- [Pastel-](https://github.com/salamou1944/Pastel-) contains the mobile-first QR concierge, staff UI, configuration and Supabase functions. Its README says not to replace the existing QR destination until the new URL is live and tested on a real phone.
- [Salamou-31](https://github.com/salamou1944/Salamou-31) contains API Factory, provider gates, storage gateway integration, deployment notes, and the COLLECTION folder.
- [AI_operating_memory](https://github.com/salamou1944/AI_operating_memory) is the canonical operating memory and decision/capability policy repository.
- [local-bridge.](https://github.com/salamou1944/local-bridge.) is a private Windows self-hosted-runner control repository. A read-only local machine inventory workflow was added and triggered: [run 39519079143](https://github.com/salamou1944/local-bridge./actions/runs/39519079143). Its job remains **queued** on labels `self-hosted, Windows, X64`; therefore no actual Windows machine, Codex CLI, or local Ollama availability has been proven through this runner yet.

## ChatGPT/Codex interpretation

The API Factory research file records the official Codex local/CLI/IDE route, subject to current ChatGPT plan limits: https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan. This is a coding-agent entitlement, not an OpenAI API key or always-on production inference endpoint. OmniRoute's Codex App-Server route requires a signed-in Codex CLI/app-server and current terms compliance. No ChatGPT/Codex login was performed in this audit.

## Next verified steps

1. Resolve the queued self-hosted runner job through the private repository's runner registration/status; never paste a runner token into chat.
2. If the Windows inventory completes, evaluate local Ollama feasibility from actual RAM, disk, CLI and model evidence.
3. Verify one official provider's free-tier eligibility and terms before configuring its protected secret. The free-API list and OmniRoute catalog are discovery sources, not free credentials.
4. Keep API Factory on the isolated Render preview while testing. Do not move main Render or Railway until durable storage, configuration, migration and deploy execution are verified.

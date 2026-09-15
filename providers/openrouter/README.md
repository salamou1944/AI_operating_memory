# OpenRouter Capability Layer

Purpose: treat OpenRouter as a provider/routing layer inside AI Operating Memory, not as a subscription bypass.

## Current verified capabilities

- OpenAI-compatible API surface.
- `openrouter/free` free-model router.
- Free router selects among currently available free variants and filters for request requirements such as image understanding, tool calling, and structured outputs.
- Free router currently exposes a dynamic pool; the provider page reported 25 models when reviewed.
- Free router context window: 200,000 tokens.
- Free router accepts text and images and returns text.
- OpenRouter exposes a live `/api/v1/models` catalog containing model identity, modalities, context limits, pricing, supported parameters, reasoning support, and provider metadata.
- OpenRouter also provides provider routing/fallback controls and an OpenAI-compatible interface.

## Important rule

This layer does NOT bypass ChatGPT/OpenAI subscriptions, authentication, rate limits, quotas, or paywalls. It uses legitimate provider APIs and free tiers where available.

## Operating policy

1. Prefer zero-cost/free variants when the task permits.
2. Never silently spend money.
3. Never store API keys in this repository.
4. Health-check providers before routing when practical.
5. Record model/provider/capability metadata before selecting a model.
6. Fall back to another legitimate provider/model when the selected route is unavailable.
7. Treat free availability and model lists as dynamic; refresh the live catalog instead of relying on a frozen list.
8. For sensitive data, apply the repository's data-handling and security gates before sending content to an external provider.

## Capability dimensions to ingest

- text input/output
- image input
- video input where advertised by the live catalog
- file input where advertised by the live catalog
- tool/function calling
- structured outputs / JSON schema
- reasoning and reasoning-effort controls
- streaming
- long-context support
- provider-specific limits
- pricing (including zero-cost variants)
- expiration/delist status
- benchmark metadata when available

## Dynamic inventory

The authoritative source for the current model inventory is OpenRouter's live models endpoint. This repository should store normalized snapshots only when refreshed, with a timestamp and source URL. Do not claim a static snapshot is exhaustive after the provider changes.

## Sources

- https://openrouter.ai/api/v1/models
- https://openrouter.ai/openrouter/free
- https://openrouter.ai/collections/free-models
- https://openrouter.ai/collections/tool-calling-models

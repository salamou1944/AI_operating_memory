# Free.ai Provider Adapter

Purpose: integrate the capabilities that Free.ai legitimately exposes through its free account/API into AI_operating_memory.

## Verified capabilities (2026-09-16)

- 30,000 free tokens/day for free accounts.
- 400+ AI tools on the developer/API surface; the public homepage currently advertises 477+ tools.
- Chat, image, video, music, voice, OCR, translation and related modalities.
- OpenAI-compatible REST API.
- Self-hosted/open-source model pool, including examples such as Qwen, FLUX, Whisper and Kokoro.
- Python SDK and CLI coding assistant are advertised by Free.ai.
- Free.ai documents a shared token pool between web and API usage.
- Free accounts have rate/request limits; paid-only premium models are not covered by the free pool.

## Integration contract

The adapter MUST:

1. Never attempt to bypass Free.ai authentication, quotas, rate limits, paid-model restrictions, or account controls.
2. Prefer self-hosted models covered by the free daily pool.
3. Track token consumption locally.
4. Fail over to another configured provider when quota/rate limits are reached.
5. Never silently spend paid credits.
6. Store API keys only in environment/secret storage; never commit keys.
7. Record provider/model/capability/license/evidence metadata.
8. Health-check the endpoint before routing production work.

## Routing classes

- `free-self-hosted`: preferred when task is compatible.
- `free-tool`: preferred for supported free tools within daily limits.
- `premium`: disabled by default unless an explicit paid-budget policy permits it.
- `byok`: allowed only when the user supplies/configures their own provider key.

## Source evidence

Official Free.ai developer/API documentation was reviewed on 2026-09-16. Exact counts can change; runtime discovery should query the provider rather than hard-code the current number of tools/models.

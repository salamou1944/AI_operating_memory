# EASY — Entry Point Verification Evidence — 2026-10-06

## Classification

- AI Operating business state: `ENTRY_POINT_VERIFIED`
- `USAGE_OBSERVED`: **not yet promoted**
- `CUSTOMER_ACTION_OBSERVED`: **not yet promoted**
- `REVENUE_OBSERVED`: **not claimed**

## Production entry point

Railway project: `EASY Runtime Production`
Service: `easy-runtime-current`
Environment: `production`
Public entry point:

`https://easy-runtime-current-production.up.railway.app/`

Human-facing routes implemented by the live gateway:

- `/` — EASY live gateway landing page
- `/customer` — seller account entry point
- `/creative` — Creative entry point
- `/integration` — Developer Platform entry point

The `/customer` page provides real registration/login through the live customer service and, after authentication, a direct path into Creative.

## Independent runtime observation

Railway HTTP logs show a real browser request to the live production gateway:

- timestamp: `2026-10-05T04:03:53.201865903Z`
- method: `GET`
- path: `/`
- status: `200`
- user agent: iPhone Safari
- follow-up request: `GET /api/gateway/status`
- status: `200`

This proves a human-facing production entry point was reachable and used outside CI.

It does **not** by itself prove customer action or commercial API usage, so the state remains `ENTRY_POINT_VERIFIED`.

## Current runtime state

At verification time:

- `easy-runtime`: online, latest deployment SUCCESS
- `easy-runtime-current`: online, latest deployment SUCCESS
- `easy-runtime-current` public domain: `easy-runtime-current-production.up.railway.app`
- HTTP requests observed on `easy-runtime-current` in the last 24h: 16 total, all HTTP 2xx
- The live gateway exposes customer, creative, operator and integration routes.

## Evidence rule

Do not promote this record to `USAGE_OBSERVED` merely because the page is reachable or because CI succeeds.

Promotion requires an independently observable production action beyond health/status probing, preferably:

1. a real seller/customer account action through `/customer`, or
2. a real production Creative/API operation with its resulting artifact/response,

followed by independent runtime/log evidence.

No revenue or payout claim is made by this record.

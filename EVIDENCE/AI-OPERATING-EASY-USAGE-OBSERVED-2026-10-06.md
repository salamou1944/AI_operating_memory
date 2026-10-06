# EASY — USAGE_OBSERVED Evidence — 2026-10-06

## State transition

- Previous state: `ENTRY_POINT_VERIFIED`
- New state: `USAGE_OBSERVED`
- `CUSTOMER_ACTION_OBSERVED`: verified for a production test account
- `REVENUE_OBSERVED`: **not claimed**

## Independent production execution

GitHub Actions workflow:
`.github/workflows/easy-production-usage-evidence.yml`

Commit:
`c111befabe7eeb2f3327c51f8859f353e13ca837`

Workflow run:
`37474286177`

Job:
`112305525537`

Result:
`SUCCESS`

The workflow executed against the public Railway production URL, not a local service and not a CI mock.

## Real production actions

The run performed:

1. `GET /` — public EASY entry point — HTTP 200
2. `POST /api/customer/register` — created a production customer test account — HTTP 201
3. `GET /api/customer/me` with the issued bearer token — authenticated session — HTTP 200
4. `POST /api/creative-job/run` using the production Creative Job service — HTTP 200
5. Creative response was independently asserted as `status=SUCCEEDED` and `decision=PASS`.

The test email was generated from the GitHub run ID and used the `example.invalid` domain. No real person's email address was used.

## Independent Railway evidence

Railway HTTP logs for `easy-runtime-current` show the same production execution:

- `2026-10-06T13:52:40.552903519Z` — `GET /` — 200
- `2026-10-06T13:52:41.720065244Z` — `POST /api/customer/register` — 201
- `2026-10-06T13:52:42.172175094Z` — `GET /api/customer/me` — 200
- `2026-10-06T13:52:42.297338125Z` — `POST /api/creative-job/run` — 200

This is independent runtime evidence that the production application received and completed functional requests.

## Interpretation

This is sufficient to promote EASY from `ENTRY_POINT_VERIFIED` to `USAGE_OBSERVED`.

It is **not** evidence of:
- a real external customer paying,
- recurring customer usage,
- provider-funded AI generation,
- revenue,
- payout.

The Creative operation used the existing safe `fixture` mode; therefore it proves production workflow usage and persistence/authentication boundaries, but does not claim provider-backed image generation.

## Next gate

The next legitimate business gate is:

`USAGE_OBSERVED` → `REPEATABLE_USAGE`

Required evidence: a second independent production use, ideally from a different account/session and preferably through the human-facing customer flow, followed by the same independent Railway runtime evidence.

Revenue remains locked until an actual qualifying commercial event is observed.

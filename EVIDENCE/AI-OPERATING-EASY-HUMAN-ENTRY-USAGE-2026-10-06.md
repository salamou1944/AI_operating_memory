# EASY — Human Entry Usage Evidence — 2026-10-06

## Observed state

A human iPhone Safari session reached the production EASY application and navigated through the human-facing routes.

Independent Railway HTTP evidence from `easy-runtime-current`:

- `GET /` → 200
- `GET /customer` → 200
- `GET /creative` → 200
- `GET /integration` → 200
- `GET /operator` → 200
- `GET /api/platform` → 200
- gateway status checks → 200

The session used iPhone Safari and originated from the same external client IP across the observed sequence. No upstream errors were reported.

## Authentication boundary

The session attempted customer registration and login, but the observed outcomes were:

- `POST /api/customer/register` → 409
- `POST /api/customer/login` → 401

Therefore this evidence proves **human-facing production entry and navigation**, but does not yet prove an authenticated customer action.

## State decision

- `ENTRY_POINT_VERIFIED`: PASS
- `HUMAN_ENTRY_USAGE_OBSERVED`: PASS
- `CUSTOMER_ACTION_OBSERVED`: NOT YET PROMOTED
- `REVENUE_OBSERVED`: NOT CLAIMED

Do not treat the 409/401 as a system-wide outage; the public routes and gateway remained healthy. The next technical task is to make the customer entry path complete for a fresh usable account/session, then capture the authenticated action independently.

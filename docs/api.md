# API

Contract: `contracts/openapi.yaml` (OpenAPI 3.1). Base path `/v1`. JSON. Authenticated routes use a bearer session token.

Errors use one shape:

```json
{ "error": { "code": "STEP_UP_REQUIRED", "message": "Tasdiqlash uchun SMS kodni kiriting" } }
```

`message` is a localisation key resolved by the client when it starts with `i18n.`. Codes are stable.

## Conventions

- Money is a string inside the `Money` schema. See ADR 0006.
- Identifiers in paths are UUIDs. Public shipment ids (`YG-0412`) are accepted on a query alias `?publicId=` for the desktop deep link lookup only.
- List endpoints take `limit` (default 50, max 100) and `cursor`.
- Writes that need step-up return `403` with `error.code = STEP_UP_REQUIRED` and a `stepUpToken` from `POST /v1/auth/step-up`. The follow-up request sends header `X-Step-Up: <proof>`.
- Staff routes are under `/v1/staff`. A client session receives `403 ROLE`.
- Idempotency: `POST` of documents, calculations, and fill events accepts `Idempotency-Key`.

## Groups

| Tag | Who | Screens |
|---|---|---|
| `auth` | Public, then Owner | C-02, D-01, S-01, S-04 |
| `setup` | Owner | C-03–C-07, S-03 |
| `shipments` | Owner | C-08–C-17, M-01–M-04 |
| `documents` | Owner | C-09 |
| `calc` | Owner | C-10, C-11, I-01, M-03 |
| `draft` | Owner | C-12, I-04 |
| `fill` | Owner, desktop | D-02–D-07, C-13 |
| `status` | Owner | C-15, C-16 |
| `products` | Owner | C-18 |
| `support` | Owner opens, Support reads | S-02, C-20, SP-02–SP-06 |
| `admin` | Admin | AD-02–AD-07 |
| `account` | Owner | C-19, C-20, S-05, S-06 |
| `reference` | Owner | I-02, I-06, X-07 |

Operation ids are the names in the OpenAPI `operationId` fields. `docs/screens.md` cites those ids.

## Auth boundary

`GET /v1/session` returns the role and, for a grant-scoped support token, the grant id and `masked: true`. Support tokens are minted by the API when a staff member opens a grant. They carry `shipmentId` scope. They cannot call `PATCH` on drafts, `POST` fill events, export, or payment routes. Those routes are absent from the support security scheme, and a test calls them with a support token and expects `403`.

## Versioning

The file is `3.1.0` of the OpenAPI spec and `1.0.0` of this API (`info.version`). Breaking changes bump `info.version` and the handbook in the same pull request. Do not keep a second informal JSON schema for the same resource.

## Mock cabinet

The mock cabinet is not this API. It is a small site the fill engine drives in the page. It does not receive ed2 cookies. Its CSP blocks `ws://127.0.0.1:*` so a practice page cannot reach a real signing service. It has no password field. The sign control is an inert button labelled as practice.

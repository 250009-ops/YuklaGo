# CI, environments, deployment

## Environments

| Name | Data | Cabinet | AI adapter |
|---|---|---|---|
| local | Docker Postgres, Redis, MinIO on the laptop. Demo seed only | mock on port 4010 | stub |
| staging | Uzbekistan. Synthetic companies only | `mashq.yuklago.uz` | stub |
| production | Uzbekistan. Real clients | mock until `ED2_LIVE_AUTOMATION` is on, then ed2 for those sessions | stub until the founder sets `live` |

There is no foreign database, replica, or log drain for client data (ADR 0005). The provider is an operator choice. This handbook does not name one, because no hosting contract is in the source pack. The requirement is the location of the disks and the backups: Uzbekistan.

Object storage, Postgres, Redis, the API, the worker, and the mock cabinet for staging and production run in that boundary. GitHub Actions runs tests. It does not hold production data. CI secrets are limited to nothing on this handbook repository. When the app exists, deploy credentials live in the CI secret store, not in the repo.

## Pipeline

On every pull request:

1. `node packages/i18n/check-copy.mjs` and `--self-test`.
2. Typecheck, once the workspace exists.
3. Vitest for calc, checks, deadlines, fill, and API permissions.
4. Playwright fill of the mock with the YG-0412 draft. Assert the deny-list and the golden totals on the review screen.
5. OpenAPI file parses. When Redocly or an equivalent is added, it lints `contracts/openapi.yaml`.

On main, after the checks: build web, console, API, worker, mock cabinet, and the Electron installer for Windows. macOS is the next installer, not the first.

Deploy staging automatically from main. Deploy production only when a human with the production role approves the workflow. Do not describe that gate as a calendar.

## Desktop distribution

Windows installer, code-signed. Auto-update feed served from the Uzbekistan origin. Mapping packs are signed. The extension is unpacked or store-listed only after Q-3 (supported browsers, store versus unpacked) is answered. Until then, document the extension as a sideload for the fallback and do not imply a store listing.

`DESKTOP_EIMZO_COMPAT` stays `unverified` in the manifest until AC-14.8 is recorded for that OS.

## Observability

- Structured JSON logs. Fields: time, level, request id, route, account id, staff id, error code.
- Do not log OTP codes, tokens, document bodies, PINFL, phones, model request text, or fill values. Fill logs on the server are hashes already.
- Traces via OpenTelemetry to a collector in Uzbekistan. `OTEL_EXPORTER_OTLP_ENDPOINT` empty means traces off.
- Metrics: request latency, job failures, grant expiries, step-up lockouts, calc `completeness=refused` count. No labels that are a STIR or a name.
- Alert on audit-chain verification failure and on a 🔒 flag change. Both page the operator. The flag alert is informational. The chain failure is an incident.

## Backups

Postgres and the object bucket are backed up inside Uzbekistan. A restore drill is part of the launch checklist in `docs/security-checklist.md`. The drill uses a staging copy, not a laptop disk that then leaves the country.

## Feature flags at runtime

Flags are rows in `FeatureFlag`, not only env vars. Env vars set the process defaults for local dev (`.env.example`). Production changes go through AD-05 and, when 🔒, AD-06. `ED2_LIVE_AUTOMATION` additionally requires the founder's confirmation. The API rejects a single-approver write.

## Smoke after deploy

Staging smoke is the stub demo: sign in with the dev OTP policy disabled in staging (real SMS or a staging sink that does not print codes into a public log), open YG-0412 seed, see 16 222 400 and 440 000, open the mock, fill, stop at D-05. No ed2.

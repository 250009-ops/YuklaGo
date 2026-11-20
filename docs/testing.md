# Testing

Every spec acceptance criterion has a test id `ac-<id>` (lowercase, dots kept). P0 tests block a release. P1 tests exist before that feature is called done. Live ed2 tests are manual and stay out of CI.

## Tooling

- Vitest for `packages/calc`, `packages/checks`, `packages/deadlines`, `packages/fill`, and API unit tests.
- Supertest (or Nest's test client) for HTTP permissions.
- Playwright against `services/mock-cabinet` for the fill engine. Not against ed2.
- The copy check is `node packages/i18n/check-copy.mjs`.

## Golden data

| Fixture | Asserts |
|---|---|
| `contracts/calc/golden-yg0412.json` | AC-3.1, AC-11.2, AC-11.3, the screen totals |
| `data/declarant/demo-sets/set-A-*/answer-key.json` | AC-13.1c Set A passes, labelled namuna |
| Set B answer key | 2 errors + 1 warning |
| Set C answer key | 4 errors (2 root causes) + 1 weight warning, conformity unverified |
| `data/declarant/deadlines.md` examples | AC-8.1, AC-8.1d. Presented 12.11 → 26.11 / 27.11. Presented 21.11 → 07.12 / 07.12 |
| `data/declarant/tolerances.json` worked examples | AC-13.1a. Gross D = 1344, diff 86, T = 20 → block. Net line D = 84, diff 14, T = 5 → block while the total warns, worst wins |
| Hostile fill mapping | AC-16.2, AC-14.4 |

The string `310000` as a fee fails the suite (AC-11.2).

## AC index

P0 unless noted. The test name is `ac-` plus the id.

| Area | AC ids | Where |
|---|---|---|
| Signer set-up | 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.7a, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18, 1.19, 1.20, 1.21 | API setup + web C-03–C-05 |
| Router | 2.1, 2.2, 2.3, 2.4, 2.5 | `packages/domain` regime table. 2.5 loops the 10 DEC-9 codes |
| Landed cost | 3.1, 3.2, 3.3 | `packages/calc` |
| Kargo compare | 4.1, 4.2 | P2. Screen stays labelled taxminiy. 4.2 is a process check, not a unit test, until interviews exist |
| Origin | 5.1, 5.2, 5.3 | calc + a copy test that no screen suggests third-country routing |
| E-kontrakt | 6.1, 6.2, 6.3 | draft blockers and clocks |
| Go/no-go | 7.1, 7.2, 7.3, 7.4, 7.5 | requirement rules. Unloaded lists say Tekshirilmadi |
| Clocks | 8.1, 8.1a, 8.1b, 8.1c, 8.1d, 8.2, 8.3, 8.4, 8.5 | `packages/deadlines`. 8.3 asserts processing times are not countdown fields |
| Documents | 9.1, 9.2, 9.3 | Stub extractor confidence. 9.2 fail-closed. 9.3 rejects identity images |
| Classification | 10.1, 10.2, 10.3 | Stub cannot emit a code outside `allowedCodes`. Nothing auto-confirms |
| Engine | 11.1, 11.2, 11.3, 11.4, 11.5 | 11.1 is "all PE tests pass". 11.4 asserts Set A is namuna. 11.5 asserts grafa 43 is not the method and 904 is labelled inference |
| Draft | 12.1, 12.1a, 12.1b, 12.2, 12.3, 12.4, 12.5 | Grafa map keys. Totals: grafa 22 = sum of 42, grafa 12 = sum of 45, grafa 5 = item count |
| Review | 13.1, 13.1a, 13.1b, 13.1c, 13.1d, 13.1e, 13.2 | Tolerances. Pallet question, never auto-subtract |
| Fill | 14.1, 14.1a, 14.1b, 14.2, 14.3, 14.4, 14.5, 14.6, 14.7, 14.8 | Playwright on the mock. 14.8 is manual per OS |
| Pause and log | 15.1, 15.2 | Fill engine |
| Hard stop | 16.1, 16.2, 16.3 | Deny-list |
| Mock | 17.1, 17.2, 17.3, 17.4, 17.5 | Banner snapshot. 17.2 is a release rule: pitch builds have the flag off |
| Hand-off | 18.1, 18.2, 18.3 | P1. Four hard blocks, everything else is a warning plus an option |
| Explainer | 19.1, 19.2, 19.3 | 44 seeded messages. Unknown paste returns nomaʼlum xabar |
| Library | 20.1, 20.2 | P1 |
| Export path | 21.1, 21.2, 21.3, 21.4, 21.5, 21.6, 21.7 | P1. EK10 grafa list length 45 |
| Special regimes | 22.1, 22.2, 22.3, 22.4, 22.5 | P1. "NCTS" absent |
| Records and cases | 23.1, 24.1, 25.1, 26.1, 33.1, 34.1, 34.2, 35.1, 35.2, 35.3, 36.1, 36.2, 36.3, 37.1, 37.2, 38.1, 38.2, 39.1, 40.1, 41.1 | P1 or P2 as in the spec. 24.1: XML hidden while the flag is off |
| Multi-line | 27.1, 27.2, 27.3 | P0 |
| Treasury | 28.1, 28.2 | P0. No payment API call exists |
| E-arxiv | 29.1 | P0 |
| Preliminary | 30.1 | P1. Fee 352000 and a 30-day clock |
| Broker option | 31.1, 31.2, 31.3 | P1 |
| Consent | 32.1, 32.2, 32.3, 32.4 | P0. 32.4 is a runbook review |
| Uzbek text | 42.1, 42.2, 42.3, 42.4 | i18n package. 42.4 fails the build if IBM Plex is imported |
| Staff and security | 43.1, 43.2, 43.3, 43.4, 43.5, 43.6, 43.7, 43.8, 43.9, 43.10, 43.11 | API permission tests |
| Mobile | M1, M2, M3, M4 | Route audit. Test ids `ac-m1` … `ac-m4` |
| Practice banner | D1 | Snapshot. Test id `ac-d1` |

PE-1 through PE-22 each have a Vitest in `packages/calc` named `pe-1` … `pe-22`. AC-11.1 depends on that file passing. PE-22 asserts the blocked state: no calculation is labelled verified.

## Permission tests that must exist before the first staff build

- Support token: `PATCH` draft, `POST` fill event, `POST` export, any admin route → 403.
- Admin token: `GET` a document, `GET` a shipment → 403.
- Owner token: admin routes → 403.
- Staff account with both roles cannot be inserted. A database check constraint or a create-path test.
- DPO self-approval → 409.
- Step-up routes reject a proof minted for a different trigger.

## What CI does not do

- Log in to ed2.
- Call a model.
- Send a real SMS.
- Use a real ERI key.

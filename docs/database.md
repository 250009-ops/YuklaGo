# Database

Contract: `contracts/prisma/schema.prisma` (Prisma ORM 7.10.1, PostgreSQL 17). ADR 0008.

## Rules for migrations

- Generate SQL from that schema. Review the SQL in the pull request. Do not edit production by hand.
- Money columns are `DECIMAL`. Identifiers are UUID.
- Add a column for a passport image or an ERI secret and the review fails. Those values are out of the data model.
- `AuditEvent` is granted `INSERT` and `SELECT` to the application role. `UPDATE` and `DELETE` are not granted. Retention deletion, when `AUDIT_LOG_RETENTION_YEARS` elapses, is a separate job running as a role that the API process does not use, and it is itself audited before the delete. The 3-year figure is a proposal, not a statute (`AUDIT_LOG_RETENTION_YEARS`).
- Signer HMAC columns are deleted when the certificate is replaced or the account is deleted (AC-1.17). Audit rows keep hashes of actions, not the raw PINFL.

## Indexes already implied

Shipments by company, fill events by session time, grants by status and end time, audit by actor and time, tariff rows by code and edition date. Add more when a query in the API is measured, not before.

## Seed

| Data | Source | Loaded into |
|---|---|---|
| Demo company, user, shipments YG-0412 and the home-table rows | Screen hand-off §7, marked synthetic | Dev seed only |
| TN codes | `data/tariff/tiftn_codes_pq181_annex1.csv` | Reference table or a loaded file. 13 138 codes |
| Demo duty rows | `data/tariff/tariff_demo.json` | `TariffEdition` with status active, source and date required |
| Fee bands | `data/tariff/fees.json` | Code in `packages/calc`, not a hand-typed 440000 in the UI |
| Deadlines | `data/declarant/deadlines.json` | `packages/deadlines` |
| Tolerances | `data/declarant/tolerances.json` | `ToleranceSetting` defaults, label fixed |
| Grafa maps | `data/declarant/grafa-map.json`, `grafa-map-ek10.json` | Draft builder and fill mappings |
| Status messages | 44 messages, answers-declarant §7, IDs S01–S11, R01–R15, R99, D01–D09, M01–M08 | `StatusMessage` |
| Holidays | Ops entries with source and date. Seed example: 8 December 2026, Constitution Day, with its decree | `CalendarEntry`. An entry without source and date is rejected (AC-8.1c) |

Demo set A is labelled "namuna", never "verified" or "tasdiqlangan", until PE-22.

## Deletion

Account deletion (step-up `ACCOUNT_DELETION`) deletes shipments, documents, drafts, and object-storage keys for that account's companies when no other account remains on the company. Cabinet declarations are not changed. The consent row is kept for as long as the audit policy needs to prove consent (ZRU-547 art. 21). Say that in the privacy notice. Do not claim a specific extra statutory period that has not been sourced.

Object deletion is a worker job that deletes the key and then the row. A failed object delete retries. The API does not report the account as deleted until the keys are gone or the failure is visible to the operator.

## What the admin connection cannot see

The Admin module's Prisma client is a narrow wrapper that exposes only `FeatureFlag`, `FlagChangeRequest`, `TariffEdition`, `CalendarEntry`, `ToleranceSetting`, and config-scoped `AuditEvent` rows. It does not expose `Document` or `Shipment`. A test imports that wrapper and asserts the other delegates are absent (AC-43.5).

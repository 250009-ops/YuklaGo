# Domain model

The Prisma file is the field-level contract. This page is the invariants the code must keep.

## Company and people

- A **Company** has one STIR. Kind is LLC, YaTT, or other.
- An **Account** is one person, role Owner, one phone. The account user is the signer (DEC-29, AC-1.7).
- **CompanyAccount** links them. Every linked account has the same rights (AC-1.12). There is no permission column.
- A person who will not sign does not get an account (AC-1.14). They receive an export.
- Logins are not shared (AC-1.13). A certificate HMAC that does not match the account stops the fill and points that person at their own account.

## Signer

- YuklaGo does not read ed1. The user confirms "Ha, kiritilganman" or "Hali yoʻq" and types the authority end date, or "muddatsiz" (AC-1.7, AC-1.10).
- Public certificate fields (PINFL, STIR, serial, validity) are compared on the server as HMAC-SHA256. The name is display-only and is not stored. Raw values are not stored (AC-1.15–AC-1.17).
- A new certificate warns. "Ha" records the one-time confirm and requires step-up `SIGNER_CHANGE`. "Yoʻq" locks Y14/Y16 (AC-1.18). Warn-only until the user answers is the legal reading applied in the spec. The CEO confirmation of warn-only is still noted as open in spec Q-21; implement warn-only as specified.
- `TRUSTED_PERSON_CAN_SIGN` and `YATT_EMPLOYEE_SIGNER` stay false (AC-1.3, AC-1.11).
- A broker's specialist is not a user of the client account (AC-1.6). Offer Y18/Y31.

## Shipment

- **Shipment** has a public id `YG-####`, a direction, an optional regime from DEC-9 (10, 11, 12, 40, 41, 42, 51, 61, 70, 80), and a stage: documents, check, review, fill, status, closed.
- **GoodsItem** is one declaration item. Invoice lines group into items by confirmed 10-digit code (Y27). Grafa 31–47 repeat per item.
- IM40 uses the 46 grafa ids in `data/declarant/grafa-map.json`. EK10 uses the 45 ids in `data/declarant/grafa-map-ek10.json`. "48 maydon" is not a product concept.
- Grafa 36 is empty. Grafas 16 and 17 are empty on IM40. Origin is grafa 34, numeric, `000` if unknown. Never write "CN" into the cabinet.
- Grafa 43 on IM40 is 0/1 own needs. On EK10 it is 0/1 own production. Same box, different question (AC-12.4).
- Draft cannot move to fill while a BLOCK finding is open or the attestation tick is unset (AC-12.5, DEC-7).

## Money

- A **Calculation** is immutable. A new input writes a new row and marks the previous one stale (PE-6).
- The trace stores rule-set version, tariff edition date, FX date, BHM value and date, and the active flags (AC-11.3).
- Fee is once per declaration, not per item (PE-14, AC-27.3).
- YuklaGo does not pay. A user mark "Toʻladim" is a manual flag. It is not a bank status (hand-off decision 9).

## Documents

- A **Document** points at an object-storage key. The database does not hold the bytes.
- Upload is refused without a current consent row, except the bytes may sit as "queued, not read" only after the product decision in the screen hand-off: the drop zone stays disabled until the tick (C-09). Do not classify or extract before consent (AC-32.1).
- Passport and ID images are rejected. No column stores them (AC-9.3).

## Fill session

- **FillSession** records target (`MOCK`, `ED2`, `CARGO`), mapping version, and outcome.
- **FillEvent** stores a hash of the value, not the value (AC-43.9). The desktop app keeps the full local log.
- Outcomes that stop the engine: user pause, read-back mismatch, field not found, page changed, your-turn (login, save, sign, send, pay).
- `userMarkedSignedAt` is self-reported. It is not proof of filing.

## Support grant

- Created only by the owner, after step-up `SUPPORT_ACCESS`.
- Scope defaults to one shipment. Duration defaults to 24 hours, also 4 or 72 (screen hand-off).
- Status becomes `EXPIRED` from the worker at `endsAt`, or `REVOKED` when the owner revokes.
- Comments do not change draft fields. The client sees them as info cards.

## Audit

- **AuditEvent** names the account or the staff member, not only the company (AC-43.10).
- Append-only. `rowHash` covers the previous hash. See `docs/audit-log.md`.

## Config

- **FeatureFlag**, **TariffEdition**, **CalendarEntry**, **ToleranceSetting** have no foreign key to documents, shipments, or accounts. Admin queries must not join to those tables.
- A 🔒 flag change is a **FlagChangeRequest** with two different staff ids. Self-approval is rejected.

## Later records (P1, still in the schema)

Valuation cases, arrival events, corrections, appeals, guarantees, and refund packs are tables so the API can grow without a second model. They do not block the P0 demo. Yield norms and guarantee amounts are user-entered. The model never proposes a yield (AC-22.3) and the engine does not compute guarantee size (`TEMP_IMPORT_GUARANTEE_SIZE`).

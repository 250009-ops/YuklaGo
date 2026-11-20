# Audit log

AC-43.8, AC-43.9, AC-43.10. Table `AuditEvent`.

## What is written

Who (the account id or the staff id, and the role), when, device id, action, subject type, subject id, and a hash of the value when a value exists. Also: consent grants and withdrawals, support sessions, flag changes, exports, and sign-ins.

The owner view groups the company's rows by person, so two signers are distinguishable.

## What is never written

Passwords, PINs, ERI keys, OTP codes, refresh tokens, the HMAC key, and anything typed in a login or signing window. Full field values are not written on the server. The desktop app keeps those locally.

Model request text and page images are not written to the audit log or to application logs.

## Hash chain

Each row stores `prevHash` and `rowHash`. `rowHash` is SHA-256 over the canonical JSON of the row plus `prevHash`. The genesis row uses a fixed previous hash of 64 zeroes. Inserts are serialised per chain (one chain per environment). A verifier walks the chain and checks the last hash. PDF and CSV exports print that last hash.

The application database role cannot update or delete these rows. See `docs/database.md`.

## Who can read

| Reader | Scope |
|---|---|
| Owner | Their account and, for a company, every member's rows |
| Support | Rows whose subject is that staff member's own grant session |
| Admin | Rows whose subject type is config: flags, tariffs, calendar, tolerances |
| DPO | The same config log, plus incident access when an incident is opened. Do not give the DPO a standing client-document browser |

## Step-up

Export of the full account ZIP requires `FULL_DATA_EXPORT`. Export of one shipment's audit pack does not. The security log CSV from S-05 does not, matching the screen hand-off.

## Retention

Default 3 years, flag `AUDIT_LOG_RETENTION_YEARS`, proposal, not law, 🔒 DPO. ZRU-764 art. 16 applicability is [UNVERIFIED] (Q-10). Do not label the 3 years "Rasmiy".

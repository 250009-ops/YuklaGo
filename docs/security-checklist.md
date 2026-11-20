# Security checklist

Use this before calling a build releasable. Items marked unverified stay visible in the release notes as unverified. They are not waived by this list.

## Identity and roles

- [ ] Only Owner, Support, and Admin exist. DPO is a flag on an Admin.
- [ ] Two staff roles cannot sit on one person (AC-43.6). TOTP is required for staff.
- [ ] The five step-up triggers work, and payment and signing do not send SMS (AC-43.1).
- [ ] New device notifies other sessions and can end the session (AC-43.2).
- [ ] Support grant expires, revokes, and masks. No unmasked export (AC-43.3, AC-43.4).
- [ ] Admin token cannot read a shipment or a document (AC-43.5).
- [ ] 🔒 flag self-approval fails (AC-43.7).
- [ ] Several accounts on one STIR have equal rights and distinct audit actors (AC-1.12, AC-43.10).

## ERI and the cabinet

- [ ] No code reads `.pfx`, `.p12`, `.key`, password fields, or the E-IMZO socket.
- [ ] Deny-list test passes (AC-16.2).
- [ ] Embedded profile is isolated, wiped on close and after 15 idle minutes, no remote-debugging port (AC-14.5).
- [ ] Allow-list blocks any other origin with a full stop screen.
- [ ] `ED2_LIVE_AUTOMATION` is off unless the founder and the DPO both approved the row.
- [ ] Mock CSP blocks `ws://127.0.0.1:*`. The mock has no password field.
- [ ] AC-14.8 result is written down per OS, or the extension fallback is what that OS ships.

## Data

- [ ] Postgres, objects, Redis, and logs for this environment are in Uzbekistan.
- [ ] Passport and ID images are rejected and not stored.
- [ ] Signer material is HMAC only. Raw PINFL is absent from disk and from logs.
- [ ] Audit chain verifies. Application role cannot update or delete audit rows.
- [ ] Consent is unticked by default. Withdrawal stops new AI jobs (AC-32.1, AC-32.3).
- [ ] `AI_ADAPTER` is `stub`, or the live adapter's region and DPA status are written next to the release. DPA is [PENDING] until Huquq says otherwise.
- [ ] Account deletion removes objects. Cabinet declarations are untouched.
- [ ] Share links are hashed, expire, and need a one-time code.

## Copy and money

- [ ] `node packages/i18n/check-copy.mjs` passes.
- [ ] Must-show lines are on the screens named in `packages/i18n/must-show.json`.
- [ ] Fee is 440 000 or 352 000. "310 000" does not appear.
- [ ] Totals that use estimates wear "≈ Taxmin" or "Namuna". "Rasmiy" is only on signed-off rates.
- [ ] Set A is not labelled verified.

## Operations

- [ ] A named person responsible for personal data exists (PC-15) before production launch. 🔒 flags cannot change until then.
- [ ] Breach runbook exists: 24 h / 72 h for a VMQ 415 cross-border leak. ZRU-764 art. 16 body and deadline are [UNVERIFIED] and the runbook says so.
- [ ] Backups restore in a drill inside Uzbekistan.
- [ ] Dependencies are pinned. Electron auto-update is signed.
- [ ] Secrets are not in the repo, the image, or the logs.

## Explicitly not claimed

- Official integration, a filing API, or a state partnership.
- That automation of ed2 is permitted. The grey-zone conditions in spec §6.1 still apply when the flag is on.
- That YuklaGo is not a broker if staff sign or are listed in ed1. They must not be (PC-2).

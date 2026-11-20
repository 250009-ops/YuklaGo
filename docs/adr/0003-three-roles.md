# ADR 0003 — Three roles

## Status

Accepted. DEC-29. The earlier six-role draft in `docs/sources/team-review/roles-rbac.md` is void.

## Decision

1. **Owner.** The only client role. The account user is the signer. Several accounts may share one company STIR. Each has its own phone, ERI, and ed1 entry. Rights are identical. There is no invite, no viewer, and no accountant login. An accountant receives an exported pack.
2. **Support.** Staff account, mandatory TOTP. Sees masked data only inside a grant the owner opened. Default 24 hours. Cannot edit, export, sign, send, pay, or open the cabinet.
3. **Admin.** Staff account, mandatory TOTP. Tariffs, calendar, tolerances, flags, config log. No client documents. Never the same person as a Support account.

DPO is `StaffAccount.isDpo` on an Admin. It is the second approver for flags marked 🔒 in spec §3A.1. It is not a fourth role. The named person is required before launch (ZRU-547 art. 31, last part; PC-15). The title "DPO" is not required by the statute.

## Consequences

- The permission set of every client account is identical. Test that.
- A staff login with the wrong role is rejected (Support token on an Admin route, and the reverse).
- Step-up SMS has exactly the five triggers in `docs/auth-rbac.md`.

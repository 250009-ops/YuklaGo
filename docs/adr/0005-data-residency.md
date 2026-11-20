# ADR 0005 — Data residency in Uzbekistan

## Status

Accepted.

## Context

ZRU-547 art. 27-1 (as amended by ZRU-1125, in force 27.03.2026) requires in-country storage for biometric, genetic, and telecom-subscriber data. Broader "everything physically in Uzbekistan" wording still sits in MJtK 46-2 part 1; the legal review treats art. 27-1 as the operative rule and flags the old wording as a practice risk [UNVERIFIED as a court outcome]. The product decision is stricter than the minimum: all databases, files, and logs are stored in Uzbekistan.

Passport and ID images are not stored, because whether a passport photo is biometric under art. 26 is [UNVERIFIED].

## Decision

- PostgreSQL, object storage, Redis, and audit logs for staging and production run in Uzbekistan.
- Backups stay in Uzbekistan.
- The only designed cross-border path is the founder-owned AI adapter, after masking, to Google Cloud in Germany or the Netherlands (DEC-15). Those countries were on the VMQ 415 list when the security review read it on 18.11.2026. Re-check the list before turning `AI_ADAPTER=live` on. The DPA is [PENDING: Huquq].
- Certificate HMACs, the HMAC key, and the token vault that maps mask tokens back to values never leave Uzbekistan and are never sent to a model.

## Consequences

- A managed database outside Uzbekistan is not acceptable, including a "EU replica".
- Local development may use localhost. It must not be pointed at a foreign hosted database that contains real client data.

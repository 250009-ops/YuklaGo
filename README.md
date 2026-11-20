# YuklaGo

YuklaGo (yuklago.uz) is a self-filing customs workspace for small Uzbek importers and exporters. The owner uploads documents, sees a landed-cost estimate and a go/no-go check before buying, then the desktop app opens **their own** ed2.customs.uz cabinet and fills the declaration in front of them. It stops at E-IMZO. The owner signs and sends. YuklaGo never signs, sends, or pays.

This repository is the engineering handbook and the contracts. It is not the application. One contributor builds the full stack from these documents: web, API, workers, Electron desktop, mobile shell, and the admin/support console.

The product spec is `docs/sources/yuklago-spec-v3.md`. If this handbook conflicts with that spec, the spec wins. The visual design is the Figma file, view only:

https://www.figma.com/design/MJCyZ6SiNj6HdesKbwxDcM/YuklaGo-%E2%80%94-Product-UI-v1.0

Build screens from screen ID, the exact Uzbek and Russian copy, and the states in `docs/screens.md`. Do not regenerate the design.

## Quick start

1. Read `docs/README.md` (the map) and `docs/definition-of-done.md`.
2. Read decisions DEC-1 through DEC-29 in the spec, then `docs/auth-rbac.md` (3 roles, 5 step-up triggers).
3. Treat `contracts/openapi.yaml` and `contracts/prisma/schema.prisma` as the API and database contracts.
4. Implement AI only behind `contracts/ai/`. The default adapter is the stub. The founder's team replaces it. See `docs/ai-seams.md`.
5. Copy `.env.example` to `.env`. It has no secrets.
6. Run the copy check (no dependencies):

```bash
node packages/i18n/check-copy.mjs
```

Scaffold the monorepo described in `docs/monorepo.md` when implementation starts. Versions and rationale are in `docs/tech-stack.md`.

## What the product must do

- Plain Uzbek (oʻ/gʻ as U+02BB) and Russian.
- Demo shipment YG-0412: code `8539 52 000 9` at 15%, payments ≈ 16 222 400 soʻm, landed cost ≈ 71 022 400 soʻm, grafa 34 = 156, grafa 44 codes 202 · 220 · 301 · 417 · 701. Fee 440 000 soʻm, or 352 000 on a pre-arrival preliminary declaration. Figures are **Namuna** until the gold case (PE-22) exists.
- Live cabinet automation stays off until the founder confirms `ED2_LIVE_AUTOMATION`. Demos use the mock cabinet at `mashq.yuklago.uz` with the MASHQ banner.
- `DESKTOP_EIMZO_COMPAT` is [UNVERIFIED]. If E-IMZO fails in the Electron window, fall back to the system browser with the MV3 extension.
- Data at rest in Uzbekistan. Audit log retention default 3 years (`AUDIT_LOG_RETENTION_YEARS`, proposal, not law). A named personal-data responsible person (called DPO here; the title is not required by ZRU-547 art. 31) is an organisation requirement before launch.

## Doc map

| Path | Contents |
|---|---|
| `docs/architecture.md` | C4 context, containers, components |
| `docs/tech-stack.md` | Versions, rationale, ADR index |
| `docs/monorepo.md` | `apps/*`, `services/*`, `packages/*` |
| `docs/domain-model.md` | Entities and invariants |
| `docs/database.md` | How to read the Prisma contract |
| `docs/api.md` | How to read the OpenAPI contract |
| `docs/auth-rbac.md` | Roles, matrix, step-up, support access |
| `docs/ed2-automation.md` | Electron, mapping engine, mock, hard stops |
| `docs/payments.md` | Fee engine and the YG-0412 worked example |
| `docs/documents-privacy.md` | Storage, masking, consent, residency |
| `docs/audit-log.md` | Hash chain, who can read what |
| `docs/notifications.md` | SMS and push |
| `docs/i18n.md` | UZ/RU, banned phrases, the lint |
| `docs/design-system.md` | Varaq tokens and how to implement them |
| `docs/screens.md` | All 64 screen IDs, routes, states, API calls |
| `docs/ai-seams.md` | Ports, jobs, stubs, where to wire a model |
| `docs/testing.md` | Acceptance tests mapped to AC IDs |
| `docs/cicd.md` | Environments, Uzbekistan hosting, observability |
| `docs/security-checklist.md` | Release checklist |
| `docs/definition-of-done.md` | Done for a story and for launch |
| `docs/backlog.md` | Ordered epics and stories, no dates |
| `docs/open-questions.md` | Open items copied from the spec, with owners |
| `docs/sources/` | Spec, screen hand-off, reviews. Not generation briefs |
| `contracts/openapi.yaml` | OpenAPI 3.1 |
| `contracts/prisma/schema.prisma` | Database contract |
| `contracts/ai/` | Port interfaces, job envelopes, stub adapter |
| `contracts/calc/golden-yg0412.json` | Demo arithmetic fixture |
| `data/` | Grafa maps, deadlines, tolerances, tariff, demo sets |
| `brand/` and `packages/tokens/` | Varaq brand and logo files |
| `packages/i18n/` | Banned-phrase list and the copy check |

## Status tags

Keep the spec's tags in code and UI. A number may show the chip "Rasmiy" only when its rule row is SOURCED and, for money, the tariff specialist has signed it. Everything else is "Namuna", "≈ Taxmin", "Tasdiqlanmagan", or "—". Do not invent legal facts. Mark anything the spec marks [UNVERIFIED] the same way.

Not legal advice. Re-read cited texts on lex.uz and customs.uz before any public claim.

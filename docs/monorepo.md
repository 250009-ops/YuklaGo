# Monorepo layout

Scaffold this tree when implementation starts. The handbook already occupies `docs/`, `contracts/`, `data/`, `brand/`, and `packages/tokens` plus `packages/i18n`.

```
apps/
  web/                 Next.js. Client workspace and PWA. Routes in docs/screens.md
  desktop/             Electron shell, preload, fill engine host
  desktop/extension/   MV3 fallback. Same packages/fill engine
  mobile/              Capacitor config only. Web assets from apps/web
  console/             Next.js. Support and Admin. Separate origin
services/
  api/                 NestJS modular monolith
  worker/              BullMQ processors
  mock-cabinet/        Practice IM40 form. Domain mashq.yuklago.uz
packages/
  ui/                  Components that consume packages/tokens
  tokens/              Varaq CSS, JSON, logos (already here)
  i18n/                Locales, banned phrases, copy check (already here)
  domain/              Types shared by API and clients. No I/O
  calc/                Payment engine. Pure
  checks/              Tolerances and document conflicts. Pure
  deadlines/           15 clocks from data/declarant/deadlines.json
  fill/                Mapping-driven filler. No Node APIs so Electron and the extension both use it
  contracts/           Generated types from contracts/openapi.yaml
contracts/             OpenAPI, Prisma, AI ports. Source of truth, not generated
data/                  Expert data. Loaded, not hand-copied into components
```

## API modules

| Module | Owns |
|---|---|
| `auth` | OTP, sessions, devices, step-up |
| `setup` | STIR, ERI public fields, signer confirm |
| `shipments` | Shipment, items, stage |
| `documents` | Upload, object storage, consent gate |
| `ai` | Enqueue only. Adapter selected by `AI_ADAPTER` |
| `calc` | Calls `packages/calc` |
| `checks` | Calls `packages/checks` |
| `draft` | Grafa values from the maps |
| `fill` | Session hashes. Does not type into ed2 |
| `support` | Grants and comments |
| `admin` | Flags, tariffs, calendar, tolerances |
| `audit` | Append-only hash chain |
| `notify` | SMS and web push |
| `export` | ZIP and PDF. Step-up on full export |

## Dependency rules

- `apps/*` may call the API and may import `packages/ui`, `packages/i18n`, `packages/domain`, `packages/tokens`.
- `apps/desktop` and the extension may import `packages/fill`. The web app may not.
- `packages/calc` may read `data/tariff` as static JSON. It may not import Nest, Prisma, or `contracts/ai`.
- `services/api` is the only writer of business tables.
- `services/worker` may write `AiJob`, `Extraction`, notification rows, and grant expiry. It uses the same Prisma schema.

## Local ports

| Process | Port |
|---|---|
| web | 3000 |
| console | 3001 |
| api | 4000 |
| mock cabinet | 4010 |
| Postgres | 5432 |
| Redis | 6379 |
| MinIO | 9000 |

## Desktop deep link

`yuklago://fill/{shipmentId}` opens D-02 when the app is installed. C-13 is the fallback screen when the protocol does not open. The web session is not copied into the desktop app by a shared cookie. D-01 signs in again. A new device always requires the SMS step-up. The "continue the web session" shortcut is not shown on desktop.

# Tech stack

Pins below were checked against upstream release pages on 20 November 2026. Re-check the patch version on the day you scaffold. Do not adopt a release candidate for the database toolkit.

| Layer | Pin | Why |
|---|---|---|
| Language | TypeScript 5.9 | One language across web, API, desktop, and contracts. |
| Runtime | Node.js 24 LTS (24.22.x to match Electron) | Electron 45 bundles Node 24.22.3. One Node line avoids desktop-only bugs. |
| Package manager | pnpm 10 | Workspaces for the monorepo. |
| Task runner | Turborepo 2 | Cache typecheck and unit tests per package. |
| Web and PWA | Next.js 16.4.6, React 19.3.1, App Router | Current stable Next.js. Server components for the landing page. Client components for the shipment workspace. |
| Staff console | Same Next.js pin, separate app and origin | Cookies and CSP must not mix with the client app. |
| Mobile shell | Capacitor 7 around the deployed PWA | Spec §8 is a PWA. A second UI codebase is out of scope. The shell adds the camera and a home-screen icon. |
| Desktop | Electron 45.4.1 | DEC-28. Same Chromium on every OS. Windows first, macOS next. |
| Extension | Manifest V3, Chromium | Fallback only (DEC-23). |
| API | NestJS 11 on the Fastify adapter | Guards map cleanly onto the three roles and the support grant. |
| Worker | BullMQ 5 on Redis | Grant expiry, reminders, retention, AI jobs. |
| Database | PostgreSQL 17, Prisma ORM 7.10.1 | Prisma 8 is a release candidate as of this writing. The contract is `contracts/prisma/schema.prisma`. |
| Money | `Decimal` in the database, decimal strings on the wire | JSON numbers are forbidden for money. |
| Object storage | S3-compatible, bucket in Uzbekistan | MinIO locally. Production endpoint is an UZ-resident bucket. |
| Validation | Zod 4 at the HTTP boundary | Share schemas with the OpenAPI types where practical. |
| UI | Tailwind CSS 4.3.5, tokens in `packages/tokens` | The brand files are already Tailwind v4 CSS. |
| i18n | Messages in `packages/i18n/locales`, no third-party runtime required on day one | UZ and RU only. A small `t()` helper is enough. |
| Tests | Vitest, Playwright for the mock cabinet, Testing Library for web | See `docs/testing.md`. |
| Observability | OpenTelemetry SDK, logs as JSON | No personal data and no model request text in traces. |

## Explicit non-choices

- **Tauri.** Smaller binary, but E-IMZO behaviour would differ by OS webview. DEC-28 chose Electron so the Chromium build is the same everywhere. `DESKTOP_EIMZO_COMPAT` is still [UNVERIFIED] inside that Chromium.
- **Prisma 8.** Not generally available. Stay on 7.10.1 until an ADR says otherwise.
- **A native Expo app as the primary mobile client.** The mobile review and spec §8 keep filling off the phone. Revisit only if the installed PWA cannot take a multi-page photo or deliver a reminder.
- **Server-side browser automation.** Ruled out. The ERI token cannot be used from the server.
- **Direct OpenAI or Anthropic APIs.** DEC-15. Not in this codebase at all. The live adapter, when the founder writes it, is Google Gemini via Google Cloud in an EU region (Germany or the Netherlands), with AWS or Microsoft EU as fallback.

## ADRs

| ADR | Decision |
|---|---|
| [0001](adr/0001-monorepo-and-modular-monolith.md) | One repo, one API process, workers beside it |
| [0002](adr/0002-electron-desktop.md) | Electron first, extension fallback |
| [0003](adr/0003-three-roles.md) | Owner, Support, Admin |
| [0004](adr/0004-ai-seams.md) | Ports and a stub; founder owns the model |
| [0005](adr/0005-data-residency.md) | Uzbekistan for all stored data |
| [0006](adr/0006-decimal-money.md) | Decimal strings, provenance on every amount |
| [0007](adr/0007-ed2-live-flag.md) | Founder switch, mock until then |
| [0008](adr/0008-prisma-7.md) | Prisma 7.10.1, not the 8 release candidate |

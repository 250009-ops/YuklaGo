# Contributing

One contributor builds YuklaGo from this handbook. These rules keep the build aligned with the spec.

## Branch and review

- `main` holds the released handbook and, later, the released product.
- Work on `cursor/<short-name>-b68e` or a branch your team agrees. Open a pull request into `main`.
- Fill in `.github/PULL_REQUEST_TEMPLATE.md`. Link the epic or story from `docs/backlog.md`.
- Do not add dates or delivery timelines to issues, docs, or the product. The spec forbids them. Legal effective dates and source-read dates are allowed.

## Source of truth

1. `docs/sources/yuklago-spec-v3.md` wins over this handbook and over Figma.
2. `docs/screens.md` plus the screen hand-off win over a Figma frame when a polish item in `docs/sources/figma-review-v1.0.md` disagrees with them.
3. The Figma file is view-only design reference. Implement by screen ID, exact copy, and states. Do not add design-generation text to the repo.
4. `contracts/openapi.yaml` and `contracts/prisma/schema.prisma` are the interface contracts. Change them in the same PR as the behaviour they describe.
5. `data/declarant/` and `data/tariff/` are the expert data. Do not hand-edit a number in the UI that these files already define.

## Roles and safety

- Three roles only: Owner, YuklaGo Support, YuklaGo Admin. DPO is a duty on an Admin account, not a fourth role.
- Step-up SMS has exactly five triggers: new device, signer change, support access, full data export, account deletion. Never on payment or signing.
- Support is consent-based, 24 hours by default, PII masked, logged. Support never signs, sends, pays, edits, exports, or opens the client cabinet.
- Admin sees configuration only.
- The app never reads, stores, or uses an ERI key, PIN, password, or cabinet cookie.
- Do not store passport or ID images.

## AI

- Call models only through `contracts/ai/ports.ts`.
- Default `AI_ADAPTER=stub`. The stub returns demo data and makes no outbound model call.
- The founder's team owns the live adapter. Do not add an OCR, HS, or question-generation implementation.
- The payment engine is deterministic. It must not call a model.

## Copy

- UI strings live in `packages/i18n/locales/`. Uzbek uses U+02BB in oʻ and gʻ.
- Run `node packages/i18n/check-copy.mjs` before you push. It fails on the banned phrases in `packages/i18n/banned-phrases.json`.
- Client UI never says "Support" or "Admin". Use "Yordam xizmati".
- "Rasmiy" is reserved. See `docs/i18n.md`.

## Secrets

- No secrets in git, issues, or logs.
- `.env.example` lists every variable. Add a new one there in the same PR, with an empty or obvious local value.

## Checks

- Copy lint passes.
- New money behaviour has a decimal fixture and a unit test. The YG-0412 fixture is `contracts/calc/golden-yg0412.json`.
- Acceptance criteria you touch are listed in the PR and mapped in `docs/testing.md`.

# Build backlog

Order is dependency order. There are no dates. P0 stories are required for the demo in `docs/definition-of-done.md`. P1 and P2 follow the spec's priorities. A later epic does not start by skipping an earlier safety story.

## E0 — Workspace

The handbook is the starting point. Implementation adds the apps around it.

- **S0.1** Scaffold the monorepo in `docs/monorepo.md` on the pinned versions in `docs/tech-stack.md`. Acceptance: `pnpm typecheck` runs, Prisma 7.10.1 is pinned, Prisma 8 is not installed.
- **S0.2** Load `data/tariff` and `data/declarant` as package inputs. Acceptance: a test reads `8539520009` from the demo tariff and the 46 IM40 grafa ids from the map.
- **S0.3** CI runs the copy check and the calc tests. Acceptance: the workflow in `.github/workflows/handbook.yml` is green and the later test jobs are added beside it.

## E1 — Design system and copy

- **S1.1** `packages/ui` implements button, header, stepper, chips, sheets, and the MASHQ banner from `docs/design-system.md`. Acceptance: saffron is not a button fill. AC-D1 for the banner. AC-42.4 font.
- **S1.2** Locale files hold the must-show lines and the public line. Acceptance: copy check and must-show check pass. AC-42.1–42.3.

## E2 — Auth and the five step-ups

Screens: C-02, D-01, S-01, S-04, C-20.

- **S2.1** Phone OTP session. Acceptance: AC-43.1's sign-in path, wrong code, lockout.
- **S2.2** Devices and new-device step-up, including desktop with no web shortcut. Acceptance: AC-43.2. D-01 states.
- **S2.3** Step-up proofs bound to one trigger. Acceptance: a payment route does not exist, and a sign route does not ask for SMS. The other three triggers are completed in E3, E8, and E9 but the mechanism lands here.

## E3 — Company and signer

Screens: C-03–C-07, S-03.

- **S3.1** STIR lookup and profile. Acceptance: AC-1.1 on the no-key state, C-03 states.
- **S3.2** "Siz imzolaysiz" without a role picker. Acceptance: AC-1.5, AC-1.7, AC-1.7a, AC-1.8, AC-1.11, AC-1.14.
- **S3.3** Several accounts, one STIR, equal rights. Acceptance: AC-1.12, AC-1.13, AC-43.10.
- **S3.4** Certificate HMAC compare, warn-only, lock after "Yoʻq". Acceptance: AC-1.9, AC-1.10, AC-1.15–AC-1.21. Until PC-16, the manual confirm path is the one under test.
- **S3.5** Refuse "ask YuklaGo to sign" and broker-specialist-as-user. Acceptance: AC-1.4, AC-1.6.

## E4 — Shipments, consent, stub reading

Screens: C-08, C-09, M-01, X-03, X-04, X-06.

- **S4.1** Home list and empty state. Acceptance: demo rows, column name "Kelib tushgan narx, soʻm", M-01 shows the same three attention items including YG-0409.
- **S4.2** Consent before read. Acceptance: AC-32.1, AC-32.2. Drop zone disabled until the tick.
- **S4.3** Upload to object storage, reject identity images. Acceptance: AC-9.3, X-04.
- **S4.4** Enqueue the stub extractor. Acceptance: AC-9.1, AC-9.2. No outbound model call. C-10 can render from the stub fields.

## E5 — Calc, clocks, go/no-go

Screens: C-10, C-11, I-01, I-02, M-02, M-03, X-01, X-07.

- **S5.1** Engine PE-1–PE-22 and the golden fixture. Acceptance: AC-3.1–3.3, AC-11.1–11.5, AC-27.1–27.3.
- **S5.2** Fifteen clocks. Acceptance: AC-8.1–8.5 including the worked dates and the unverified-calendar flag.
- **S5.3** Go/no-go states Kerak / Kerak emas / Tekshirilmadi, prohibited stop, IMEI blocker. Acceptance: AC-7.1–7.5, AC-5.1, AC-5.3.
- **S5.4** Pre-arrival card. Acceptance: AC-30.1, X-07c amount 352 000.

## E6 — Review and draft

Screens: C-12, C-14, I-04, X-02.

- **S6.1** Tolerances with the proposal label and the pallet question. Acceptance: AC-13.1, AC-13.1a, AC-13.1c, AC-13.1d, AC-13.1e.
- **S6.2** IM40 draft from the grafa map, EK10 map available but not the demo path. Acceptance: AC-12.1–12.5, AC-21.5 for the EK10 key list even if the UI is P1.
- **S6.3** Attestation and locked review. Acceptance: AC-13.2, X-02 copy includes the declaring-persons line.
- **S6.4** E-arxiv numbers on grafa 44. Acceptance: AC-29.1.
- **S6.5** Code confirm stores the user, never the model. Acceptance: AC-10.1–10.3. Must-show line on C-10 and C-12.

## E7 — Mock cabinet and desktop fill

Screens: C-13, D-01–D-07, M-04.

- **S7.1** Mock cabinet, MASHQ banner, inert sign control, no password field. Acceptance: AC-17.1–17.5, AC-D1, AC-14.3.
- **S7.2** Fill engine, read-back, pause, deny-list. Acceptance: AC-14.1, AC-14.1b, AC-15.1, AC-15.2, AC-16.1–16.3.
- **S7.3** Electron shell, allow-list, profile wipe. Acceptance: AC-14.4, AC-14.5, AC-14.2 while the flag is off.
- **S7.4** Extension fallback. Acceptance: AC-14.1a, AC-14.6.
- **S7.5** Manual AC-14.8 script written into the release notes template. The test itself is not a unit test.
- **S7.6** Phone shows M-04 only. Acceptance: AC-M1–M4.

## E8 — After the signature mark

Screens: C-15, C-16, I-05, S-05.

- **S8.1** Registration number typed by the user, payment instructions, manual "Toʻladim". Acceptance: AC-28.1, AC-28.2, AC-41.1's "no scrape" rule for the number.
- **S8.2** Message library, 44 rows, paste explainer. Acceptance: AC-19.1–19.3.
- **S8.3** Audit pack PDF and full-account export with step-up. Acceptance: AC-43.8, AC-43.9, S-05 rules.
- **S8.4** Account deletion with step-up. Acceptance: objects removed, cabinet not contacted, S-06.

## E9 — Support and admin

Screens: S-02, SP-01–SP-06, AD-01–AD-07, C-19, C-20.

- **S9.1** Grant flow with step-up, expiry worker, revoke. Acceptance: AC-43.3, AC-43.4, AC-43.11 (no external upload control).
- **S9.2** Masked console. Acceptance: SP-03 has no edit, export, sign, send, pay, or cabinet control. Comments do not change the draft.
- **S9.3** Admin config with source and date, tolerance label locked, config log. Acceptance: AC-8.1c, AC-13.1b, AC-43.5.
- **S9.4** 🔒 approvals. Acceptance: AC-43.7. `ED2_LIVE_AUTOMATION` cannot be enabled by an admin alone.
- **S9.5** Separate staff people and TOTP. Acceptance: AC-43.6.

## E10 — Hardening for a real user

- **S10.1** Uzbekistan staging. Acceptance: ADR 0005 checklist, no foreign connection string in the staging env.
- **S10.2** SMS gateway behind `SMS_PROVIDER`. Acceptance: dev logger refused when `NODE_ENV=production`.
- **S10.3** Audit chain verifier and backup restore drill. Acceptance: `docs/security-checklist.md` operations items.
- **S10.4** Signed Windows build and update feed. Acceptance: ADR 0002.

## E11 — Full broker replacement (P1)

Each story is done only with its AC tests. None of them turn on live ed2 by themselves.

- **S11.1** Hand-off pack and optional broker share. AC-18.1–18.3, AC-31.1–31.3. Screen C-17.
- **S11.2** Product library. AC-20.1, AC-20.2. Screen C-18.
- **S11.3** EK10 path. AC-21.1–21.7. Screen X-07b. Target cargo.customs.uz is [UNVERIFIED]. Guide only until the flag covers it.
- **S11.4** Regimes 11, 12, 41, 42, 51, 61, 80. AC-22.1–22.5. Screen X-07a.
- **S11.5** Valuation. AC-35.1–35.3. Related party blocks the draft.
- **S11.6** Arrival, damage, inspections. AC-36.1–36.3, AC-38.1, AC-38.2.
- **S11.7** Corrections, appeals, guarantees, refunds. AC-33.1, AC-37.1, AC-37.2, AC-39.1, AC-40.1.
- **S11.8** Post-release index, 15-day download reminder, accounting CSV. AC-23.1, AC-34.1, AC-34.2, AC-25.1.
- **S11.9** Currency clocks and E-kontrakt blockers. AC-6.1–6.3, AC-5.2.
- **S11.10** Client-entered ed1 history. AC-41.1. Source string "ed1 (siz kiritdingiz)".

## E12 — Explicitly later (P2)

- **S12.1** Kargo comparison, labelled taxminiy, no legal claim. AC-4.1. AC-4.2 waits on interviews (Q-15).
- **S12.2** XML export stays hidden. AC-24.1. Flag `XML_EXPORT` off (PC-3).
- **S12.3** Corridor pack link. AC-26.1.

## Not in the backlog

- Implementing OCR, HS models, or question generation. The stub is the implementation. The founder adds the live adapter outside these stories.
- A native mobile rewrite.
- Reading ed1 or ed2 status automatically.
- Any client role besides Owner.

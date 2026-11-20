# YuklaGo (yuklago.uz) — Product Specification v3 (DRAFT)

**Document status:** DRAFT v3, assembled from spec v2 and the team reviews listed below. It is not final until the [PENDING] slots in §0.3 are filled.
**Owner of this document:** Product (spec v3). Questions go to the Hakathon CEO or the named expert, never to the founder directly.
**Not legal advice.** Laws and official systems change. Re-read every cited text on lex.uz / customs.uz before any public use.
**No timelines.** This spec states what must be true, not when it is built. Dates that appear are legal effective dates or dates on which a source was read.

---

## 0. How to read this document

### 0.1 Status tags

| Tag | Meaning |
|---|---|
| **SOURCED** | Backed by a lex.uz text or an official customs.uz / ed1 / ed2 page that a named review (or this draft) opened and read. Link given. |
| **EXPERT-ONLY** | Stated by a named expert review from practice or from a text not re-opened; no direct link to the exact provision, or the product use depends on the expert's sign-off. |
| **[UNVERIFIED]** | Not confirmed by any official text or named review. Must not be shown as official. |
| **[PENDING: <who/what>]** | Waiting for a named expert answer or a review file that does not exist yet. |
| **[INFERENCE]** | A reviewer's reading of a rule, not the rule's text. Treat as UNVERIFIED for UI purposes. |
| **[HYPOTHESIS]** | Product or market assumption to be confirmed in interviews. |
| **[DECISION NEEDED: Hakathon CEO]** | A product choice the reviews disagree on. |

Product rule that follows from these tags: **a number or rule may carry the "Rasmiy" (official) chip in the UI only if its row in §3 is SOURCED** and, for money rows, the TIF TN va Bojxona To'lovlari Mutaxassisi has signed it off. Everything else shows "Namuna" (sample), "≈ Taxmin" (estimate), "Tasdiqlanmagan" (unverified) or "—".

### 0.2 Experts and owners

| Short name | Role | ID |
|---|---|---|
| **Huquq** | Bojxona Huquq va IT Integratsiya (customs law and official-system integration) | 449f71e6 |
| **TIF TN** | TIF TN va Bojxona To'lovlari Mutaxassisi (nomenclature and payments) | 3d549ef3 |
| **Deklarant** | Bojxona Deklarant Ustoz (declaration practitioner) | d098a0b5 |
| **CEO** | Hakathon CEO (product decisions) | 31cb22f1 |

### 0.3 Inputs: present vs pending

| Input | Status | Used for |
|---|---|---|
| `yuklago-spec-v2.md` | Present | Baseline |
| `pm/spec-v2-audit.md` | Present | Feature/AC/rule counts, risks |
| `team-review/declarant.md` | Present | Rule corrections (§3), grafa map, flow fixes |
| `team-review/broker-import.md` | Present (arrived during drafting) | Import broker task table (§4.1), fees, E-kontrakt, corrections, appeals |
| `team-review/broker-export-regimes.md` (identical copy: `reviews/broker-eksport-maxsus-rejimlar-v1.md`) | Present | Export/regime task table (§4.2), regime codes, regime clocks |
| `team-review/legal.md` | Present (no newer revision found at drafting time; superseded where `answers-legal.md` is more specific) | §6 legal constraints, copy rules, deadlines |
| `team-review/security.md` | Present (updated 03:52 with AI-provider decision) | §6, §7 |
| `team-review/automation.md` | Present | §7 |
| `team-review/engineering.md` | Present | §7, data asks, contradictions |
| `team-review/mobile.md` | Present | §8 |
| `team-review/uiux.md` | Present | §9 |
| `team-review/brand.md` + `team-review/brand-tokens.json` + `team-review/ui-tokens.json` | Present | §9 (brand B "Varaq", UI tokens v0.2-ui) |
| `team-review/research-pitch.md` | Present | §9, §10 copy rules |
| `team-review/product.md` | Present | G1–G8 gap list, placeholder list |
| `deklarant-jarayoni.md`, `global-funksiyalar.md`, `raqobatchilar.md` | Present | Background only |
| `data/tariff/` (`fees.json`, `rules.md`, `tariff_demo.json/.csv` with 10 verified demo codes, `tiftn_codes_pq181_annex1.csv` with 13,138 codes) | Present (TIF TN) | §3A payment engine rules, config flags |
| `team-review/tariff-payments.md` | Present (TIF TN) | §3A, R14–R26 |
| `team-review/answers-legal.md` | Present (arrived during drafting): 9 placeholders + 2 open legal questions answered, with lex.uz citations | §3 rules R6–R10, R27, R31, R34, R59–R63; §6; §11 |
| `team-review/answers-tariff.md` | Present (TIF TN): 8 placeholders answered | §3, §3A, §9 |
| `team-review/answers-declarant.md` | Present (Deklarant): signers, export, conformity, 46-grafa IM40 list, corrected document list, 13 extra Y18 triggers, 44-message Y19 library (count corrected by the v3 check §F), Y4 interview plan | §3, §4, §5 |
| Final brand files `/workspace/yuklago-brand/final/` (`brand-guidelines.md`, `brand-sheet.png`, `logo/`, `tokens/` JSON/CSS/Tailwind, `mock-mode-specimen.png`) | Present (final; `/workspace/yuklago-brand/export/` is ignored) | §9 |
| `team-review/declarant-v3-check.md` (Deklarant check of v3 at 04:06: signer, export, grafa, DEC-17, DEC-18, Q-6 session script §G, PE-22 gold-case plan §H) | Present | R32, R33, Y1, Y8, Y12, Y13, Y14, Y18, Y19, Y21, Q-6, PE-22 |
| `data/declarant/` (`grafa-map.json/.md` 46 IM40 grafas incl. grafa 44 code 904 "МЕТОД" [OUR READING, UNVERIFIED on live ed2]; `grafa-map-ek10.json/.md` 45 EK10 grafas with a `vs_im40` diff (new, Q-19); `deadlines.json/.md` 15 clocks; `tolerances.json/.md` 17 checks with explicit weight `formula` blocks and `gross_weight_scope` (Q-19); `demo-sets/` A/B/C, all SYNTHETIC; `README.md` changelog 18.11 04:20) | Present (Deklarant) | R32, Y8, Y12, Y13, Y17, Y21, §3A.1 |
| `team-review/roles-rbac.md` (security: 3 roles, permission matrix, signer check, 8 SoD rules, audit rules, 9 gaps for PM; Uzbek; dated 2026-11-19) | Present | §6A, Y1, Y43, §3A.1, Appendix A PC-15 |
| `team-review/roles-legal.md` (Huquq, 2026-11-19: signer cases B1, liability B2, Support/Admin access B3, must-stay-visible warnings B4, safe/risky phrases B5, PM questions Q-21 and PC-15; Uzbek; not legal advice) | Present | DEC-25, DEC-29, §6A, §10, Y1, Y43, §3A.1, Q-21, PC-15, PC-16 |
| `design-v0.4/simplify-brief-v0.4.md` (designer brief for web UI v0.4) and PM check `pm/simplify-brief-v0.4-check.md` | Present | §9 D-17–D-20 |

---

## 1. Decisions log

| # | Decision | Decided by | Status | Applied in |
|---|---|---|---|---|
| DEC-1 | **Multi-line invoices (typical 1688 shipments) are IN Phase 1.** One BYUD with N goods items (grafas 31–47 repeat per item; grafa 3 extra sheets; grafa 5 item count). | Hakathon CEO | Active | Y27, Y12, Y11 |
| DEC-2 | **Partner broker path** for inspections, valuation disputes, appeals and corrections. Since DEC-13 it is an **optional fallback**, not the core path. The partner is a notified broker under its own contract with the user; YuklaGo staff never sign or file. | Hakathon CEO | Active, narrowed by DEC-13 | Y31, Y18 |
| DEC-3 | Food goods needing vet/phyto control fully escalated in Phase 1. | Hakathon CEO | **Superseded by DEC-13** | — |
| DEC-4 | **The v2 ban on the 20 % preliminary-declaration fee discount is removed.** VMQ 55 annex 1 footnote text was verified on lex.uz during drafting; PF-250 cl. 2(a) is cited by the TIF TN expert (R22). | Hakathon CEO; verified | Active | R22, Y11, Y30 |
| DEC-5 | **Positioning: "you file it yourself, without needing a broker."** Copy rule: never use the exact phrases "broker o'rnini bosadi" or "rasmiylashtirib beramiz". | Hakathon CEO, from legal.md | **Updated by DEC-25** (public line and ban list) | §10, §9 |
| DEC-6 | **Consent screen is a feature.** | Hakathon CEO, from legal.md/security.md | Active | Y32 |
| DEC-7 | **No "Tez" (fast) mode on the live cabinet.** "Tez" exists only in the practice (mock) portal. Full-draft review is mandatory before signing on the live cabinet. | Hakathon CEO, from legal.md | Active | Y14, Y15 |
| DEC-8 | Export in Phase 1 limited to router + pack + timers; special regimes broker pack only. | Hakathon CEO | **Superseded by DEC-13** | — |
| DEC-9 | **Regime codes follow Yo'riqnoma 2773 annex 3:** export 10, re-export 11, temporary export 12, release for free circulation 40, re-import 41, temporary import 42, inward processing 51, outward processing 61, temporary storage 70, transit 80. | Hakathon CEO | Active | R33, Y2, Y22 |
| DEC-10 | **BK 261 / BK 276 / VMQ 605 cl. 2, 15, 28, 30 wording fixes** (deadline source; liability split; signer = person entered (kiritilgan) in the ed1 declaring-persons list). | Hakathon CEO | Active | R2, R3, R6, §10 |
| DEC-11 | **Brand B "Varaq", per Hakathon CEO.** Indigo `#2E2BA0`, saffron `#F5B43C`, font Onest (tokens from `team-review/brand-tokens.json` and `ui-tokens.json`). Final files land in `/workspace/yuklago-brand/final/`. | Hakathon CEO | Active | §9 |
| DEC-12 | **No building in this round; only the spec.** Design is not redrawn; UI fixes go to §9. | Founder, via Hakathon CEO | Active | Whole document |
| DEC-13 | **SCOPE OVERRIDE — full broker replacement.** YuklaGo covers **every** task in `broker-import.md` (63) and `broker-export-regimes.md` (52) as a feature with testable AC: export, re-export, temporary import/export, processing, transit, guarantees, licensed goods, vet/phyto food goods, inspections, valuation disputes, appeals, corrections. The partner broker is an optional fallback. This overrides DEC-3 and DEC-8. Legal facts are not relaxed: items waiting for official confirmation are in Appendix A with their interim behaviour. | Hakathon CEO, relaying founder | Active | §2, §4, §5, Appendix A |
| DEC-14 | **The founder takes the ed2-automation and broker-activity questions to the Customs Committee himself.** The draft letter in `legal.md` has **not** been sent. | Founder, via Hakathon CEO | Active; outcome pending; see DEC-24 | Appendix A (PC-1, PC-2, PC-9) |
| DEC-15 | **AI provider:** Google Gemini via Google Cloud, EU processing region (Germany or the Netherlands); AWS or Microsoft EU regions as fallback. OpenAI/Anthropic APIs are not used directly. Google Cloud DPA review is pending. | Hakathon CEO, from security.md | Active; DPA [PENDING] | Y32, §6.3 |
| DEC-17 | **Two dates for the import BYUD clock:** "File by" = presentation date + 14 days (conservative: presentation day counted as day 1); "Legal max" = presentation date + 15 days (BK 261). In-app help explains why. | Hakathon CEO, with Deklarant data | Active | R6, Y8 |
| DEC-18 | **Document tolerances ship as admin-configurable defaults labelled "PROPOSAL, not law"**: gross weight warns within max(1 %, 20 kg), blocks beyond; net weight warns within max(0.5 %, 5 kg), blocks beyond; packages and quantities must match exactly. | Hakathon CEO, values from Deklarant `tolerances.json` | Active; formulas made explicit by Q-19 (T computed from the declared figure D; 3-decimal rounding; exact hit on T = warning; per line and total, worst wins) | Y13, §3A.1 |
| DEC-19 | **Freight split across items by gross weight by default**, with an option to split by value; the method used is logged in the audit pack. | Hakathon CEO | Active | PE-18, Y27 |
| DEC-20 | **YuklaGo ops keeps the working-calendar and holiday config** (holidays from official decrees + each post's working hours), every entry with source and date. If a post's calendar is unverified, the app shows the **earlier** date **and** a flag. | Hakathon CEO | Active | Y8, §3A.1 |
| DEC-21 | **Additional unverified config flags with no demo claims:** grafas 41, 33, 45, 47 (to be checked against live ed2); the Set C conformity certificates; the MJtK fine editions dated 30.12.2026 and 05.02.2027. | Hakathon CEO | Active | §3A.1 |
| DEC-22 | **Final brand files** are `/workspace/yuklago-brand/final/`; `export/` is ignored. Designer product rules adopted: oʻ/gʻ stored as U+02BB with auto-replace; practice mode = neutral graphite "MASHQ" banner, never magenta/hazard styling. | Hakathon CEO, brand designer | Active | §9, Y42 |
| DEC-16 | **IM40 draft uses the Deklarant's 46-grafa map** (Yo'riqnoma 2773 cl. 24), keyed by grafa ID × item. The design's "48 maydon" draft is a visual mock only. | Hakathon CEO, from answers-declarant.md | Active; **confirmed by DEC-26** | Y12, R32 |
| DEC-23 | **Q-C1 resolved: the main filing client is a desktop app (Tauri or Electron; engine fixed as Electron by DEC-28)** that opens ed2 in its own embedded browser window (a top-level window, not an iframe, so ed2's `X-Frame-Options: SAMEORIGIN` does not apply). The cabinet opens inside YuklaGo and fills automatically in front of the user, then stops at ERI/E-IMZO, which the user signs locally. **The MV3 browser extension is the fallback** for users who cannot install the desktop app. Reverses automation.md's recommendation (extension first). | Hakathon CEO | Active | §2, §6.5, §7, §8, §9, Y14–Y16, Q-C1 |
| DEC-24 | **`ED2_LIVE_AUTOMATION` is the founder's switch**, not "off by legal default". Status wording: **"ready, enabled when the founder confirms"**. The letter to the Customs Committee stays unsent; the founder talks to the officials himself. Legal facts from answers-legal.md are unchanged; the mock portal stays the demo surface until the flag is on. | Hakathon CEO | Active | §6.1, §3A.1, Y14, Y17, PC-1, PC-9, Q-1 |
| DEC-25 | **Copy:** product scope is full broker replacement. Public line: **"Brokersiz, oʻzingiz topshirasiz — tez va tushunarli"**. Banned phrases: "broker oʻrnini bosadi", "rasmiylashtirib beramiz", and (added 19.11, Hakathon CEO, from `roles-legal.md` B5) "bojxona tasdiqlagan" (customs-approved), "rasmiy hamkor" (official partner) and "100% kafolat" (100% guarantee). Basis per Huquq: ZRU-776 art. 16 (showing approval by a state body is prohibited) and art. 5 (misleading or exaggerated advertising); art. 47 sets the sanction for legal entities (70 BHM). Russian forms: not given in `roles-legal.md` [PENDING: Huquq]. Closes the copy-rule tension (PC-8). | Hakathon CEO | Active; ban list extended 19.11 | §10, §9 D-14, PC-8 |
| DEC-26 | **Grafa 36/43: the Deklarant map stays** (confirms DEC-16): grafa 36 is not in the IM40 list (preferences go to grafa 44 / 6xx); grafa 43 = 0/1 "own needs". The conflicting reading in tariff-payments.md §3 item 8 is closed. **Evidence (declarant-v3-check §C):** 2773 cl. 24 (no 36); cl. 25 sub-point 38 (43 = 0/1); no fill rule for 36 anywhere in the Instruction; preferences in 44 as "6" + payment-type code (Annex 13) + basis act (Annex 14); valuation method = Annex 12 row 113 code 904 "МЕТОД" in grafa 44 [INFERENCE — the Instruction does not name the grafa for 904]; the Annex 1 paper form still prints box "36 Преференция", so leave it empty. | Hakathon CEO | Active | R32, Y12, §3A.1 |
| DEC-27 | **Deklarant v3 check applied** (`team-review/declarant-v3-check.md`): signer wording, broker-notification AC, embedded-window signing test, EK10 grafa list (cl. 21) and EK10 grafa 43 (cl. 22), grafa 16/17 not filled for IM40, DEC-17 end-of-day and unverified-calendar rule, DEC-18 three gross tiers and explicit net max(), 44-message Y19, R33 edition 2773-15, Q-6 and PE-22 blocked with their session/gold-case plans. Until PE-22 is met, demo Set A is labelled "namuna", never "verified". | Deklarant review | Active | R32, R33, Y1, Y8, Y12–Y14, Y16–Y19, Y21, PE-22, Q-6, Q-14 |
| DEC-28 | **Q-C2 closed: desktop engine = Electron**, because it bundles the same Chromium on every OS, so ed2 and E-IMZO behave predictably. **Windows first** (where most E-IMZO users are), **macOS next**. `DESKTOP_EIMZO_COMPAT` / `DESKTOP_EIMZO_SIGNING` stay; if E-IMZO or signing fails in the app window, the user falls back to the system browser with the YuklaGo MV3 extension (DEC-23). The E-IMZO-in-app test is a spec-level acceptance test for the build phase. | Hakathon CEO | Active | §7, §8, Y14, §3A.1, Q-C2 |
| DEC-29 | **Three roles only (founder decision, relayed by the Hakathon CEO).** (1) **User / Owner** — the single client role; does everything (documents, code and payment confirmation, paying in own bank, signing and sending in ed2 with own E-IMZO, exports, AI consent, Support access grants, own audit log); UX uses progressive disclosure, not role screens. **The client account user is the signer:** the director (or YaTT) or a staff specialist entered in the ed1 declaring-persons list; checked at set-up and re-checked when the certificate holder changes or the ed1 authority period ends (Y1 AC-1.7–AC-1.10). There is no second client role. **Phase 1: every account holder is a signer;** there are no accounts for people who do not sign (an accountant receives the downloadable audit pack / export instead; AC-1.14). **A company may have several user accounts, all with the same single client role and identical rights** (Q-20 closed): each person who signs has their own login, their own ed1 declaring-persons entry and their own ERI; logins are never shared; the audit log names the person who did each action (AC-1.12–AC-1.13, AC-43.10). (2) **YuklaGo Support** — only with the Owner's consent, time-limited, masked data only, every action logged and visible to the Owner; cannot edit, sign, submit or pay. (3) **YuklaGo Admin** — tariffs, calendar, tolerances and flags; no access to client documents or personal data. No client sub-roles (accountant, declarant, viewer, approver), no team invites, no per-role permissions and no approval chains between client users. A named person responsible for personal data (ZRU-547 art. 31, last part; called "DPO" in this spec, title not required) is required before launch (PC-15) and is the second approver for every flag marked 🔒 DPO in §3A.1. Server audit-log retention default 3 years (`AUDIT_LOG_RETENTION_YEARS`, proposal, not law). Matrix, SoD rules and audit rules: §6A and `team-review/roles-rbac.md`. **Numbering:** the CEO asked for DEC-27, which was already taken (Deklarant v3 check), so this is DEC-29. **Supersedes all earlier role decisions:** spec v3 had no client RBAC section or role decision before this entry; the 6-role RBAC drafted earlier in `roles-rbac.md` was withdrawn by the security agent and is void. | Founder, via Hakathon CEO | Active | §2, §3A.1, §6.5, §6A, Y1, Y8, Y13, Y43, §9 D-17–D-20, §10, §11 Q-5, Q-20 (closed), Q-21 (closed), Appendix A PC-15, PC-16 |

---

## 2. Product summary and scope

**Who.** Lead user: a small Uzbek importer (shop owner, marketplace seller, small wholesaler; LLC or YaTT) buying from China or Turkey, often via 1688/Alibaba with multi-line invoices. Also: exporters and farmers (EK10, including fruit and vegetables), manufacturers using processing or temporary import, traders using re-export or transit. Partner brokers receive optional hand-off packs.

**What it replaces (DEC-13).** The whole job a customs broker does for a small business: intake and authority set-up, documents, classification, valuation, payments, permits, electronic filing, arrival and storage, inspections, corrections, disputes, release, post-release control and archive — for import, export and special regimes (§4 shows every task). YuklaGo does this **as software the declarant uses**: the declarant (or its own staff specialist) logs in, signs and sends with its own E-IMZO key, and remains the declarant. One client role: the YuklaGo account user is that signer (DEC-29, §6A). Legal basis for self-filing without a broker: VMQ 605 cl. 1 (R1).

**How it should feel.** Easy (plain Uzbek, one next step at a time, no broker vocabulary), fast (prefilled from documents and the product library; the cabinet fill takes seconds on the mock), and clear (every number carries source and date; every rule shows its article; every unverified item says so).

**Hard boundaries (unchanged by DEC-13).**
- YuklaGo never logs in, signs, sends or pays. It never stores, reads or uses ERI keys, PINs, passwords or session cookies (R57; §7).
- YuklaGo staff are never in a client's declaring-persons list and never file for a client (R38; PC-2).
- YuklaGo Support and Admin never sign, submit, pay or edit a client's draft; Support sees masked data only with the Owner's time-limited consent; Admin never sees client documents (DEC-29, §6A).
- No hidden or background filing; no bypass of captcha, tokens or rate limits (R58).
- No guarantee of the final customs amount; YuklaGo does not pay differences (R50).
- No claim of official integration: "We found no public filing API."
- No origin-routing advice.
- Live-cabinet automation is **ready, enabled when the founder confirms** (`ED2_LIVE_AUTOMATION`, DEC-24); until then demos use the mock portal (PC-1). The user logs in and signs with their own key in every mode.

**Clients.** Web (main workspace), mobile PWA (capture, clocks, explainer, landed cost; no signing), and the **desktop app** (Electron, DEC-28; Windows first, macOS next) as the main filing client: it opens ed2 in its own embedded browser window, fills in front of the user and stops at ERI/E-IMZO (DEC-23). The MV3 browser extension is the fallback filing client for users who cannot install the desktop app, and the signing fallback if E-IMZO fails in the app window (the system browser with the YuklaGo MV3 extension (DEC-23)).

**Phasing.** DEC-13 removes phase limits on scope. Order of readiness is set by the legal gate (Appendix A) and data sign-off, not by excluding features. No delivery timeline is stated.

---
## 3. Corrected rules (legal facts the product relies on)

Columns: **ID · Rule · Source · Status · From**. "From" names the review that read the text (D = declarant.md, AD = answers-declarant.md, AL = answers-legal.md, L = legal.md, BI = broker-import.md, BE = broker-export-regimes.md, T = tariff-payments.md / answers-tariff.md, S = security.md, V3 = re-checked live on lex.uz while drafting v3, DC = declarant-v3-check.md). BK = Customs Code https://lex.uz/docs/2876354; VMQ 605 = https://lex.uz/uz/docs/-3844549; VMQ 55 = https://lex.uz/docs/7357270; MJtK = https://lex.uz/uz/docs/-97664.

### 3.1 Who may file and sign

| ID | Rule | Source | Status | From |
|---|---|---|---|---|
| R1 | A foreign-trade participant may fill and submit the declaration over the Internet without a broker (since 1 July 2018). Cite VMQ 605 cl. 1, **not** PF-5414 (spec v2 link returns 404; D reports PF-5414 lost force 01.04.2025 — AL/L could not confirm that date). | VMQ 605 cl. 1; BK 274 | SOURCED (PF-5414 repeal date [UNVERIFIED]) | D, L |
| R2 | The person who signs the TED with ERI is responsible for its data (VMQ 605 cl. 28). Liability split: the declaring person answers for TED data and its match with the documents; the declarant or trusted person answers for the documents' accuracy (VMQ 605 cl. 30). Declarant duties: BK 276. | VMQ 605 cl. 28, 30; BK 276 | SOURCED | D, AD, L |
| R3 | **Declaring person** = (a) the declarant itself, (b) a customs-clearance specialist on the declarant's staff (employment contract, Uzbek citizen), or (c) a specialist of a broker under contract with the declarant. Each must be entered in the ed1 **declaring-persons list** with an authority period (ed1 "Декларацияловчи шахслар рўйхати"; my.gov.uz service 207: free, automatic, no documents). A power of attorney alone is **not** enough to sign [INFERENCE/UNVERIFIED]. A YaTT signs personally or uses a broker (YaTT employee as signer [UNVERIFIED]). | VMQ 605 cl. 2, 15 (stage 2); BK 284; https://my.gov.uz/uz/service/207 | SOURCED (trusted-person and YaTT-employee points [UNVERIFIED]) | AD, D, L |
| R4 | Documents for the TED are uploaded to **E-arxiv**, ERI-signed; each gets a special number referenced in the TED (grafa 44) and shared with the listed specialist/broker. | VMQ 605 cl. 15 | SOURCED | D, AD |
| R34 | ERI keys are issued by the registration centre "Yangi texnologiyalar" ilmiy-axborot markazi under the State Tax Committee — via public-service centres, the single portal, or e-imzo.soliq.uz (portal/e-imzo only for the head of a legal entity). ed2 login accepts PFX file, USB-TOKEN and BAIK-TOKEN through E-IMZO. **No address or fee is shown.** | VMQ 348 (10.05.2018) reglament cl. 2 https://lex.uz/docs/3730168; ZRU-793 art. 9; gov.uz soliq page; VMQ 605 cl. 26; ed2 live page | SOURCED (address, fee [UNVERIFIED]; whether the key must be tied to the company STIR [UNVERIFIED]) | AL, AD, D |
| R35 | Official systems: **ed2.customs.uz** = e-declaration (ERI login); **ed1.customs.uz/PersonCabinet** = participant cabinet (declaring-persons list, payment reconciliation acts, BYUD status); **cargo.customs.uz** = "Экспорт уч қадам" export filing. Legal names: BQ YAAAT / "us-uz.gov.uz" (VMQ 605 cl. 14). Domains are observed, not guaranteed; a single platform is planned (PQ-122 cl. 16a). ed2 sends `X-Frame-Options: SAMEORIGIN` (cannot be iframed). | Live checks 18.11.2026; VMQ 605 cl. 14; PQ-122 https://lex.uz/docs/-7452043 | SOURCED (observation); EK10 via ed2 [UNVERIFIED] | D, AD, E |
| R38 | **Broker** = Uzbek legal entity acting on the declarant's instruction and in its name under contract (BK 15, 277; also 281, 282, 284; arts. 278–280, 283 lost force). Notification to the Customs Committee (ZRU-701 annex 3 pos. 35); working without notification: **20 BHM** fine (annex 4 III pos. 28). VMQ 847 annex 32: legal entity, fee 50 % of BHM, security 1000 BHM, cabinet, ≥2 staff specialists, qualification certificate every 2 years from 01.10.2025, debts cleared in 10 days, staff changes in 5 days, contract with declarant. Broker officials: MJtK 227²⁷ 5–10 BHM (10–20 repeated). | BK; ZRU-701 https://lex.uz/docs/5511879; ZRU-956 https://lex.uz/docs/7093753; VMQ 847 https://lex.uz/docs/7274716 | SOURCED | L, AL, AD |
| R59 | **Path test** (personal vs commercial): non-commercial = for personal needs, judged by quantity, repetition, trip circumstances (BK 155). Passenger: declared at the border, no BYUD (BK 156, 162). Post/courier: to an individual non-commercially **or to a legal entity** up to **30 BHM** — postal/courier documents serve as declaration; otherwise BYUD (BK 165, 167). Duty-free allowances (from 01.05.2025): air 1000 USD, rail/river 500, road/foot 300, courier 200/month, post 100 (VMQ 244 of 19.04.2025 cl. 1) — a payment matter, not the commercial test. An Uzbek individual can be a declarant (BK 274) but goods for business go via BYUD; unregistered business activity: MJtK 176 (5–7 BHM + confiscation). | BK 155, 156, 162, 165, 167, 274; VMQ 244 https://lex.uz/docs/7484114; MJtK 176 | SOURCED (one-off commercial import by an unregistered individual and by the self-employed [UNVERIFIED]) | AL |

### 3.2 Clocks (user clocks vs customs processing times)

**User clocks** (shown with a countdown). **Customs processing times** (R11) are information only, never a user countdown (AL §4).

| ID | Rule | Source | Status | From |
|---|---|---|---|---|
| R5 | Advance cargo information is **mandatory** for road, rail and air, online, before arrival (carrier/authorised person). Specific "1 h / 2 h before" times from background research: [UNVERIFIED]. | BK 206 part 3 | SOURCED | D, L |
| R6 | **Import BYUD: no later than 15 calendar days** from the day goods are presented to the destination customs body (exceptions: BK chapters 22, 23, 25). If the last day is a non-working day of **that customs body**, its next working day is the last day. The Customs Code has no general period-counting article (Deklarant searched the full text); Civil Code art. 146 (period starts the day after the event) is an analogy **not confirmed** for customs periods. **Product (DEC-17):** "File by" = presentation + 14 days; "Legal max" = presentation + 15 days, shifted per the post calendar. UI cites "Bojxona kodeksi 261-modda; VMQ 605 Nizom 11-band". | BK 261 parts 1–2; VMQ 605 cl. 11; CC 146, 148 https://lex.uz/docs/111181; `data/declarant/deadlines.json` | SOURCED (start-day rule [UNVERIFIED]) | AL, L, D, AD-data |
| R7 | Export BYUD: before the goods actually leave. | BK 261; VMQ 605 cl. 11 | SOURCED | AL |
| R8 | Short BYUD for temporary storage: by the next working day after presentation (carrier/authorised person). Post notified within 30 minutes of arrival (VMQ 605 cl. 6). | BK 86; VMQ 605 cl. 6, 8 | SOURCED | L, D |
| R9 | **Temporary storage ≤ 60 calendar days (perishables ≤ 10)**; the exact term is set by the authorised person who declared the placement. Start: the moment customs confirms delivery (mark on the transport document), within 3 h of the carrier's notice. Not a stage if goods stay under permanent control and clearance ends within 24 h of filing (VMQ 605 cl. 10). Before storage ends the goods must be declared to another regime; after placement, removed from the warehouse within 3 days (BK 89). The app computes the end date **only from the term on the warehouse document**; otherwise shows "≤ 60 kun (ombor hujjatidan tekshiring)". Weekend roll-over and day-1 counting: [UNVERIFIED]. What happens to goods after storage expires: [UNVERIFIED]. | BK 85, 89, 226; VMQ 605 cl. 10 | SOURCED (flags as noted) | AL |
| R10 | Preliminary declaration is treated as not filed if goods are not presented within 30 calendar days of its acceptance. | BK 262 part 4 | SOURCED | AL, BI |
| R11 | **Customs processing times (information only):** low risk 3 h, medium 8 h (VMQ 605 cl. 15, VMQ 700 ed., in force 08.02.2026; out-of-hours exceptions); otherwise 1 working day from acceptance and full documents, excluding risk-management measures and other agencies' controls (BK 248 part 4). | VMQ 605 cl. 15; BK 248 | SOURCED | AL, L |
| R12 | Amendment/withdrawal of the BYUD within 3 years of acceptance; withdrawal possible before release. | BK 266 | SOURCED | AL, D |
| R13 | Late declaration / documents: **3 BHM** fine (MJtK 227-10 part 2, ZRU-720 ed.), recorded automatically. Form/place/procedure breaches: 2–5 BHM citizens, 3–7 BHM officials (227-10 part 1). | MJtK 227-10 | SOURCED | AL, D |
| R27 | Customs payments are due **before or at acceptance** of the declaration (BK 327). | BK 327 | SOURCED | AL, D |
| R31 | **E-kontrakt:** business entities (except the self-employed) enter contract, act and invoice data into "E-kontrakt" (TSOYaEAT) with ERI **before** the foreign-trade operation; import/export on an invoice without a contract is allowed if the invoice is entered (Nizom cl. 6); exchange contracts within 1 working day; amendments the same way; if the partner country changes, apply to amend the BYUD within 10 working days (cl. 5). Banks execute operations only if the system data match (cl. 11). Contract ID goes into grafa С item 1. Penalty article for non-compliance [UNVERIFIED]; rejection of a BYUD without an ID [UNVERIFIED]; duty for non-entrepreneur individuals [UNVERIFIED]. | VMQ 283 (14.05.2020; VMQ 40/2026, PF-174 ed.) cl. 1, 5, 6, 11 https://lex.uz/docs/4812419; Yo'riqnoma 2773 grafa С; BK 243 | SOURCED (flags as noted) | AL, BI, D |
| R60 | **180-day currency clocks:** import — goods placed under import/processing/warehouse (or money returned) within 180 days of payment under the import contract (Nizom cl. 23, VMQ 77 ed., from 19.05.2025); export — proceeds or return of goods within 180 days of export/re-export/free-warehouse placement (cl. 24). Fines (ZRU-573 art. 11¹): if not repatriated within 45 days after the 180 (90 days for small business) — 5 % of the unrepatriated sum up to 360 days, +10 % for 360–545 days, +35 % at 545+ days; exemptions exist. Over 180 days = capital-movement operation (art. 11). Bank document lists: [UNVERIFIED] — "get the list from your bank". | VMQ 283 Nizom cl. 23–24; ZRU-573 arts. 11, 11¹, 20, 24 https://lex.uz/docs/4562834 | SOURCED (latest consolidated edition [UNVERIFIED]) | AL, AD, BE |
| R40 | Voluntary correction of typos: within 1 working day after permission (codes and numbers excluded); TED and e-documents may be downloaded within 15 days of clearance (VMQ 605 cl. 30–31, 37). | VMQ 605 cl. 30, 31, 37 | SOURCED | BI |
| R41 | Appeal against a customs decision after inspection/audit to the higher body within **30 days** (BK 409-2); form BK 409-3; court suspends the appealed part (409-7). | BK 409-1–409-7, 411 | SOURCED | BI |
| R61 | Origin certificate supplied **within 1 year** of placement → MFN/preference restored and overpaid duty refunded. | BK 366 | SOURCED | D, BI |
| R28 | Unused advance payments refundable within 3 years of last use (BK 335); overpaid/over-collected payments refundable within 3 years (BK 353–357). | BK 335, 353–357 | SOURCED | BI |
| R29 | Late payment: penalty interest 1/300 of the refinancing rate per day. | BK 349 | SOURCED | D |

### 3.3 Documents, permits, controls

| ID | Rule | Source | Status | From |
|---|---|---|---|---|
| R30 | Invoice must carry 12 minimum fields (seller name/address/STIR; buyer name/address/STIR/phone; HS ≥6 digits; origin country; name/brand/model/article/technical description; value; gross; net; packages; supplementary-unit quantity; Incoterms 2010 term; contract number/date). Packing list is **not** a required document (cl. 11¹). Incoterms 2020 handling in grafa 20 [UNVERIFIED]. | VMQ 605 Annex 1a and cl. 11¹ (VMQ 630) https://www.lex.uz/uz/docs/-7138545 | SOURCED | D, AD |
| R62 | **IM40 document list (signed off by Deklarant):** TED; invoice (12 fields); contract + E-kontrakt ID; transport document; previous document (grafa 40) when there was a previous regime; permits/certificates **in Yagona darcha** for controlled goods; origin certificate ("strongly expected", R15); freight/insurance/loading invoices to the border; evidence of advance funds; E-arxiv numbers; signer in the ed1 list; packing list not required [PRACTICE: posts may ask]; warehouse act/presentation date (product evidence). EK10: TED, invoice, contract/E-kontrakt, transport document, permits, E-arxiv, signer + phyto/vet, origin certificate if the buyer needs it, VAT-0 % evidence afterwards. | AD §5 (VMQ 605 cl. 11¹, 15; 2773; BK 243, 300¹, 304, 327, 334, 366) | SOURCED / [INFERENCE] / [PRACTICE] as tagged | AD |
| R63 | **Yagona darcha gate:** if permit bodies have not entered the permit/certificate into Yagona darcha, the TED is not accepted; from 01.10.2025 all import/export/transit permits go through Yagona darcha only. Identical goods under one contract: certificate/permit may be issued once for up to 1 calendar year. | VMQ 605 cl. 15 stage 1; PQ-122 cl. 17 | SOURCED | D, AD |
| R64 | **Conformity certificate:** issued by an accredited product-certification body (MSO) **chosen by the applicant**; before or after arrival; if before, the importer puts it into Yagona darcha and TSOYaEAT; stage times exist (1–2 working days decision, sampling 1–2 wd, production assessment ≤10 wd, issue 2–3 wd) but tests have no fixed term — **total lead time [UNVERIFIED]**, never shown. Electronic system/URL for applications [UNVERIFIED]. Which goods need it: VMQ 43 annexes [UNVERIFIED — annex text not loaded]. | VMQ 502 (14.08.2024) Nizom cl. 4–5, 9, 13, 14 https://lex.uz/docs/-7080176; O'RQ-354; VMQ 43 https://lex.uz/docs/5249380 | SOURCED (flags as noted) | AD, T |
| R37 | **Asl Belgisi:** for marked goods the aggregated import code (AIK) must be in the BYUD or release for free circulation is prohibited. Groups (VMQ 737 annex 1, ed. VMQ 23 of 23.01.2026): tobacco, alcohol, beer, household appliances (code list), medicines/medical devices, water/beverages, mineral fertilisers/plant-protection products, batteries 8507 (from 01.01.2026). Mapping of old code 8539500000 to HS2022 8539 52: [UNVERIFIED]. 5-day operator notice groups: [UNVERIFIED]. | VMQ 737 (20.11.2020) https://lex.uz/uz/docs/-5115923; VMQ 23 https://lex.uz/docs/-8012407 | SOURCED (flags as noted) | T, BE |
| R65 | **Banned/controlled — drones:** import, sale, storage, use of UAVs and parts (codes in VMQ 658) prohibited except named bodies or by separate Cabinet decision. HS2022 mapping (8806) [UNVERIFIED]. | VMQ 658 (15.11.2022) https://www.lex.uz/uz/acts/-6284990 | SOURCED | T |
| R66 | **IMEI:** for phones (8517 13) IMEI is required in grafa 31; registration after IM40. IMEI fee [UNVERIFIED]. | VMQ 778 (17.09.2019) cl. 14 https://www.lex.uz/docs/-4517458 | SOURCED | T |
| R67 | Phytosanitary certificate travels with **each consignment** of exported plant products; issued through Yagona darcha by territorial departments of the Plant Quarantine and Protection Agency; decision within 5 working days; fee per passport [UNVERIFIED amount]. Old law "30 days notice / 15 days presentation" still applied? [UNVERIFIED]. | Plant Quarantine Law art. 12 https://www.lex.uz/uz/docs/-119173; VMQ 65 annex 3 as amended by VMQ 727 (01.11.2024) https://lex.uz/uz/acts/-7208474 | SOURCED (flags as noted) | AD, BE |
| R68 | Veterinary: export permit per calendar year (application 2 working days), export veterinary certificate (7 working days); transit permits exist. | VMQ 148 (10.04.2023) https://www.lex.uz/acts/-6427764 | SOURCED by BE; [UNVERIFIED] per AD (not re-read) | BE, AD |
| R69 | Certificate of origin for export: issuer **"O'zbekekspertiza" AJ**; forms A (GSP), ST-1 (CIS), ST-UZ, others; 1 working day (fruit/veg 1 wd; up to 2 wd for HS 84–89 or large assortment); agricultural produce needs proof of origin. Fee [UNVERIFIED]; which form Türkiye accepts for dried apricots [UNVERIFIED]. | VMQ 994 (13.12.2019, 2024 ed.) cl. 2, 22, 24, 27, 35–36 https://lex.uz/uz/docs/-4643161 | SOURCED | AD, BE |
| R70 | Fruit/vegetable export (TIF TN 07, 08, 0904, 1202): invoice-based export allowed if entered in TSOYaEAT; natural-loss norms entered; exporters with overdue receivables placed automatically on the "unfair exporters" register and may export only on 100 % prepayment. Minimum export prices by government commission (PQ-107) — current list [UNVERIFIED]. | VMQ 163 cl. 3, 6, 8, 11, 12 https://lex.uz/uz/docs/-4213596; PQ-107 | SOURCED (price list [UNVERIFIED]) | AD, BE |
| R71 | Export control: export of controlled items needs a permit; catch-all obligation for unlisted items with possible military use. | Law 658-II https://lex.uz/uz/docs/-262949 | SOURCED | BE |
| R72 | Export regime: goods leave without obligation to return, in the state they were in at BYUD registration; customs checks permits itself. VAT 0 % proof: contract, export BYUD, transport documents with border mark (or electronic feed) (Tax Code 260–261). Export duty table: none found [UNVERIFIED] → "eksport boji: rasmiy stavka topilmadi". | BK 29–31, 290; Tax Code 258, 260–261 https://lex.uz/docs/4674902 | SOURCED (export duty [UNVERIFIED]) | AD, BE |

### 3.4 Special regimes

| ID | Rule | Source | Status | From |
|---|---|---|---|---|
| R33 | Regime codes (grafa 1/37): 10, 11, 12, 40, 41, 42, 51, 61, 70, 80 (DEC-9). 16 regimes listed in BK 25. Instruction edition includes amendment **2773-15 of 22.07.2026** — re-check before release (declarant-v3-check §C.3). | Yo'riqnoma 2773 annex 3 https://lex.uz/uz/docs/2924955 | SOURCED | BE, DC |
| R44 | **Re-export (11):** identification required; if no transit declaration within 3 working days of placement, goods go to temporary storage (BK 32); duties paid at import refunded if re-exported within 2 years unused (BK 35, ch. 49 procedure). "6 months" export term [UNVERIFIED]. | BK 32–35 | SOURCED | BE |
| R45 | **Temporary import (42):** 2 years (extensions in listed cases), completion no later than the day after expiry (BK 64, 69); full conditional relief (VMQ 212 list — content [UNVERIFIED]) or periodic payments 5 % per full/partial month of import duties and taxes (BK 66); prohibited categories (BK 62). **Temporary export (12):** 2 years (BK 39). **Re-import (41):** within 3 years (BK 59). Guarantee size/form [UNVERIFIED]. | BK 39, 59, 61–69 | SOURCED (flags as noted) | BE |
| R46 | **Inward processing (51):** customs processing permit; yield norm set from technological documents; permit 2 years (up to 5 for regular operations) (BK 70–82, 75, 76). **Outward processing (61):** permit 2 years; extension request ≥ 1 month before expiry (BK 42–54, 47). | BK 42–54, 70–82 | SOURCED | BE |
| R47 | **Transit (80):** transit declaration and accompanying documents; permits where required; some goods only with payment security (list [UNVERIFIED]); max terms: air 3 calendar days, land/water 15 calendar days per 1000 km (BK 116–120). Declared via E-Tranzit or us-uz.gov.uz; TIR carnet and ATA carnet accepted as transit declaration when advance info was given (VMQ 737 of 31.12.2022). Carriage under customs control: air 3 days, road/water 10, rail 30 per 2000 km (BK 218). | BK 116–120, 218; VMQ 737 (2022) https://lex.uz/uz/docs/-6334883 | SOURCED | BE |
| R25 | VMQ 55 fees: transit / inward / outward processing **25 % of BHM per declaration** (verified V3); customs change to a transit declaration 10 % of BHM; no fee for temporary storage, abandonment, destruction. | VMQ 55 annex 1 | SOURCED | BE, V3 |
| R53 | Deferral/instalments only with security (BK 329; special regime for importers with 3+ years: up to 50 % of last 3 years' payments, 6 months, no security); security methods BK 339–346. PF-250 2(b) "no interest up to 14 days for instalments" and "duty deferral up to 120 days from 01.06.2026" — conditions [UNVERIFIED]. | BK 329–333, 336–346; PF-250 https://lex.uz/uz/docs/-7934915 | SOURCED (PF-250 items [UNVERIFIED]) | BI, T |

### 3.5 Liability, data, systems

| ID | Rule | Source | Status | From |
|---|---|---|---|---|
| R39 | Misdeclaration (MJtK 227-22 part 1): confiscation of goods and a fine (citizens 5–10 BHM, officials 7–15 BHM). Other misdeclaration fines 227⁸, 227¹⁰, 227²⁵, 227²⁶ (3–15 BHM); smuggling: Criminal Code 182. | MJtK; JK https://lex.uz/docs/111453 | SOURCED | L, D |
| R42 | Personal data: since 27.03.2026 mandatory in-country storage only for biometric, genetic and telecom-subscriber data (ZRU-547 art. 27-1, ZRU-1125); cross-border transfer to VMQ 415 list countries (49; US only for DPF companies; China not listed) or with the subject's consent / authorised-body conditions (art. 15); consent must be provable (art. 21); disclosure to third parties needs consent (art. 28); registry only for in-country-mandatory databases (art. 20). MJtK 46-2 part 1 still contains old "physically in Uzbekistan" wording (practice risk [UNVERIFIED]); **46-2 part 2: unlawful processing of personal data using AI — 50–100 BHM**. Passport photo as biometric data [UNVERIFIED] → do not store passport/ID images. VMQ 415 breach notice: 24 h notice, 72 h details. | ZRU-547 https://lex.uz/docs/4396419; ZRU-1125 https://lex.uz/docs/8099215; VMQ 415 https://lex.uz/docs/8369688; MJtK 46-2 | SOURCED (flags as noted) | L, S |
| R73 | Cybersecurity law ZRU-764 art. 16 duties (incident prevention, notification of the authorised body, digital-trace retention) likely apply to YuklaGo as an online service [UNVERIFIED: applicability, which body, deadline]. | ZRU-764 https://lex.uz/docs/5960604 | EXPERT-ONLY | L, S |
| R57 | ERI key holder must take all measures to protect the private key; head of a legal entity responsible for key use. | ZRU-793 art. 27 https://lex.uz/docs/6234904 | SOURCED | L |
| R58 | Unauthorised access / special tools for unauthorised access / false information (JK 278-2, 278-3, 278-4); breach of system-use rules by an authorised user (MJtK 155-1). Resource owner sets access rules (560-II art. 12). | JK; MJtK; 560-II https://lex.uz/docs/82956 | SOURCED | L |
| R50 | Limitation of liability: void for intentional breach (Civil Code 333); limits in adhesion/consumer contracts restricted (CC 332; Consumer law 221-I arts. 1, 21). Draft offer clauses 5.1–5.5 in legal.md need a lawyer's review. | CC https://lex.uz/docs/111189; 221-I https://lex.uz/docs/4704 | SOURCED | L |
| R36 | Corridors green/yellow/red/blue. | PQ-122 cl. 15 | SOURCED | D |
| R32 | **IM40 grafa map (DEC-16):** declaring person fills 46 grafa IDs: 1, 2, 3, 5, 7 (post code), 8, 9, 11, 12, 13, 14, 15, 15a, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 54, С. 31–47 repeat per item. Key meanings: 43 = 0 (not own needs) / 1 (own needs); 45 = customs value in contract currency, 2 decimals; 46 = statistical value in thousand USD, CIF/CIP border, 3 decimals, CB rate on acceptance day; 44 = document classifier codes (220 invoice, 301 contract, 417 conformity, 701 "СПТИМ" origin certificate, 6XX exemptions/privileges on payments) + E-arxiv numbers; 34 = origin country code, **"000" if origin is unknown**; 45 = customs value **rounded to 2 decimals**, statistical value (46) **to 3 decimals** (cl. 25 sub-points 40–42); rounding of payment sums to the soʻm stays [UNVERIFIED]; **"6XX" in grafa 44 covers exemptions and privileges on customs payments** ("6" + Annex 13 payment code + Annex 14 basis act, e.g. `629 15-142120030000`; cl. 25 sub-point 39 "е"); **the origin certificate for an FTA or Türkiye preference goes in grafa 44 under code 701 "СПТИМ"** (Annex 12 row 63); whether a tariff preference is **also** entered as 6XX is not stated [UNVERIFIED — `TARIFF_PREF_AS_6XX`]; **36 is not in the IM40 list and has no fill rule anywhere in the Instruction (leave empty; the Annex 1 paper form still prints box 36)**; **valuation method: code 904 "МЕТОД" exists in Annex 12 (row 113) but its grafa is not stated; putting it in grafa 44 is our inference [INFERENCE — `GRAFA44_904_ENTRY`]; the engine never writes the method into grafa 43**; **grafas 16 and 17 are not filled for IM40 — origin goes per item in grafa 34**; С item 1 = contract ID; 37 = 7-digit procedure code; 40 = previous document; 47 incl. payment method ТУ = БН/КТ. Grafa 13 = USD/UZS rate set by the CB on the acceptance date (Deklarant `grafa-map.json`); grafa 36 is not filled for IM40 (DEC-26). Grafas 33 (right part not described for IM40), 41 (numeric unit-code table not loaded), 45 (left subfield content not described; the Instruction places the method in 44/904, whether ed2's 45 left subfield also asks for it is [UNVERIFIED] until Q-6) and 47 (UZS rounding not stated) carry ⚠️ in the Deklarant map and stay flagged until checked against live ed2 (DEC-21). Full map with Cyrillic/Russian names, formats, rules, classifiers and lex.uz deep links: `data/declarant/grafa-map.json`. **Closed (DEC-26):** tariff-payments.md §3 item 8 listed 36 "imtiyoz" and 43 "qiymat usuli" with its own [UNVERIFIED] mark and deferred to the Deklarant; the Deklarant map is confirmed. **EK10 (cl. 21–22):** separate list — 1, 2, 3, 5, 7 (post code), 8, 9, 11, 12, 13, 14, 17, 17a, 18, 19, 20, 22–26, 28–35, 37–50, 54, С (has 17/17a; lacks 15, 15a, 21; no 36). EK10 grafa 43 = **0** if the exporter did not produce the goods itself, **1** if it did (cl. 22 sub-point 38). | Yo'riqnoma 2773 (edition with 2773-15 of 22.07.2026) cl. 21, 22, 24, 25 (sub-points 38–42), 89, Annex 12 rows 63 and 113 https://lex.uz/uz/docs/2924955 (EK10 list #4294922; IM40 list #4304434; IM40 43 #2926926; EK10 43 #2925893); customs.uz e-form page | SOURCED (904 placement [INFERENCE]; flags as noted) | AD, D, T, DC |

---

## 3A. Payment engine rules

Built from `tariff-payments.md`, `answers-tariff.md`, `data/tariff/rules.md`, `fees.json`, `tariff_demo.json` (10 verified demo codes: 8517130000, 8471300000, 6109100000, 6404110000, 6403999600, 9503009500, 3304990000, 8516500000, 8539520009, 9403601000) and `tiftn_codes_pq181_annex1.csv` (13,138 codes). The engine is deterministic, uses decimal arithmetic, and the language model never computes, rounds or invents a number.

| ID | Rule | Source | Status | Acceptance criterion |
|---|---|---|---|---|
| PE-1 | **Valuation method.** Methods 1–6 applied in sequence (1 transaction value; 2 identical goods; 3 similar goods; 4 deductive; 5 computed; 6 fall-back). Method 1 is computed; methods 2–6 are guided (Y35) with the user's evidence. | BK 301–313 | SOURCED | Given a shipment, when method 1 conditions fail (no sale, related party affecting price, conditions on price), then the engine does not output a method-1 value and opens Y35 with the reason. |
| PE-2 | **Related-party question.** "Are you related to the seller (shareholding, family, management)?" If yes, method 1 only if the relationship did not affect the price; warning shown. | BK 306–308 | SOURCED | Given "related = yes", when the user has not provided evidence that price was not affected, then the value shows status "Bog'liq shaxs — tekshiruv kerak" and Y35 is required before draft. |
| PE-3 | **Additions to price** up to the place of entry: freight, loading/handling, insurance, commissions (except buying commission), packing/containers, assists, royalties/licence fees — each with amount, currency, document; costs not listed may not be added. | BK 304 | SOURCED | Given FOB/EXW terms, when freight is entered, then the engine requires a split "chegaragacha / chegaradan keyin" and adds only the first; insurance line is present (≈ Taxmin until a policy is uploaded). |
| PE-4 | **Deductions:** transport after the place of entry excluded if shown separately; if the forwarder invoice has no split, the full amount is added and the user is warned. | BK 305 | SOURCED | Given an unsplit freight invoice, then the full amount is added and a "Hujjatda bo'linish yo'q" warning appears. |
| PE-5 | **Incoterms** decide which costs are already in the price (EXW/FOB/CFR/CIF/CPT/DAP/DDP …). | BK 304; T §2 | SOURCED (Incoterms 2020 in grafa 20 [UNVERIFIED]) | Given CIF to border, then freight/insurance are not added twice (test case per term). |
| PE-6 | **Exchange rate:** CB of Uzbekistan official rate on the BYUD **acceptance date**; estimates use today's rate with the label "kurs BYD kuni o'zgarishi mumkin". Store requested date and the API's returned date (weekend fallback) and `Nominal`. | BK 326; cbu.uz API | SOURCED | Given a draft, when the filing date changes, then all amounts are re-quoted with the new date and the old quote is marked stale. |
| PE-7 | **Duty rates stored by effective date.** Source: PQ-181 annex 2 (in force 01.06.2025), current edition by PQ-58 (11.02.2026), consolidated **16.02.2026**; codes from PQ-181 annex 1. Each calculation stores `rule_set_version`, `tariff_edition_date`, `fx_date`, `bhm_value+date`. The rate that applies is the one in force on the acceptance day (BK 324 — BHM by analogy [ASSUMPTION]). | PQ-181 https://lex.uz/uz/docs/-7533457; https://lex.uz/docs/3802366; annex 1 https://lex.uz/uz/files/7541055.zip; BK 324 | SOURCED | Given two dates on either side of an edition change (e.g. 2515 11 marble 20 % → 0 %), then the engine returns the rate for each date and the library flags the change. |
| PE-8 | **Code validity:** only 10-digit codes in the official list; e.g. 8539 52 000 0 does not exist (…1/…2/…9). | PQ-181 annex 1 | SOURCED | Given a non-existent or partial code, then the engine refuses with "Kod rasmiy ro'yxatda yo'q". |
| PE-9 | **Combined/specific rates:** "X %, but not less than Y USD per unit" → `max(ad valorem, specific × qty × rate)`; "X % plus Y" → sum. Requires a **quantity input** in the supplementary unit (dona/juft/kg) for minimum duties; show both legs and which won. | BK 293; PQ-181 annex 2 | SOURCED ("kg" net vs gross [UNVERIFIED]) | Given 6109100000 (20 %, ≥0.5 USD/dona), when quantity is missing, then the duty line shows "BIRLIK_MIQDORI_YO'Q" and no amount; when quantity is given, both legs and the winner are shown. |
| PE-10 | **Origin and art. 300¹ surcharge:** from 28.02.2026, goods from non-MFN countries or with origin not established get an extra duty: base ≤10 % → +5 pp; 10–20 % → +10; 20–30 % → +15; ≥30 % → +20. Missing/doubtful certificate → surcharge applies; certificate within 1 year → recalculation and refund (BK 366). China (#23) and Türkiye (#37) are on the MFN list (MYU 3267). Inputs: origin country + `origin_status` (bor / yetkazib beruvchi beradi / yo'q). Side-by-side total with and without certificate before the user pays the supplier. | BK 300¹ (O'RQ-1097), 366; MFN list https://lex.uz/uz/docs/-4911943 | SOURCED (band edges, 0 % goods, combined-rate surcharge, VAT-base inclusion [UNVERIFIED]) | Given origin "yo'q" and base 15 %, then a separate 47 line "Qo'shimcha bojxona boji (BK 300¹)" appears; given an exact edge (10/20/30 %), then both possible values are shown with "chegara noaniq". |
| PE-11 | **Preferences (entitlement only, no routing advice):** CIS FTA (Protocol, ZRU-362) with ST-1; Uzbekistan–Türkiye PTA (PQ-65, from 01.07.2023) only for 12 HS6 lines (721049, 841370, 848180, 850213, 850490, 853710, 853720, 853890, 854442, 854449, 903289, 940690) with **EUR.1** and direct transport. Preference evidence: origin certificate (ST-1 / EUR.1) in grafa 44 under code 701 "СПТИМ" (2773 Annex 12 row 63); 6XX in grafa 44 covers exemptions and privileges on customs payments (cl. 25 sub-point 39 "е"); whether a tariff preference is also entered as 6XX is [UNVERIFIED] (`TARIFF_PREF_AS_6XX`). | PQ-65 https://lex.uz/uz/docs/-6388997; https://lex.uz/en/docs/6489973; Instruction 2773 (edition with 2773-15 of 22.07.2026) https://lex.uz/uz/docs/2924955; R32 | SOURCED (ST-1 form text [UNVERIFIED]; 10-digit rates inside the Türkiye HS6 lines to be re-checked) | Given Türkiye origin and an HS6 outside the 12 lines, then the UI shows "Imtiyoz topilmadi" and no x/y rates; given 853710 with EUR.1, then the preferential row is shown with its source. |
| PE-12 | **Excise:** only for Tax Code 289¹ (tobacco), 289² (alcohol), 289³ (oil products, polyethylene granules, natural gas, packaged sweet drinks, energy drinks, chips); base arts. 285–286; otherwise "Aksiz: qo'llanmaydi (SK 289¹–289³)". | Tax Code https://lex.uz/docs/-4674902 | SOURCED | Given a code outside those lists, then the excise line reads "qo'llanmaydi" with the article. |
| PE-13 | **VAT** 12 % of (customs value + duty + excise). | Tax Code 254, 258; BK 322 | SOURCED (300¹ in base [UNVERIFIED]) | Formula label shows all three base components. |
| PE-14 | **Processing fee:** VMQ 55 annex 1 item 1"a" bands by customs value in USD: <10,000 → 1 BHM; 10–20k → 1.5; 20–40k → 2.5; 40–60k → 4; 60–100k → 7; 100–200k → 10; 200–500k → 15; 500k–1M → 20; ≥1M → 25. One fee per BYUD regardless of item count. **1 BHM = 440,000 soʻm from 01.09.2026** (PF-115) → fee 440,000; with **pre-arrival preliminary declaration −20 % → 352,000** (VMQ 55 footnote; PF-250 2(a), from 01.03.2026). Fee once for preliminary/temporary/incomplete/periodic declarations. Band edges only the last is explicit. | VMQ 55 (VMQ 700 ed.) https://lex.uz/docs/7357270 (first bands, 20 % footnote, one-time rule verified V3); PF-115 https://www.lex.uz/uz/docs/-8283656 (440,000 verified V3); PF-250 https://lex.uz/uz/docs/-7934915 | SOURCED (edges, conversion date [UNVERIFIED/ASSUMPTION]) | Given CV 4,671.64 USD, then fee = 440,000 (or 352,000 on a pre-arrival preliminary declaration); "310 000" never appears; given CV exactly 10,000.00 USD, then "chegara noaniq" with both values. |
| PE-15 | **Other VMQ 55 fees:** BYUD change on declarant request 25 % BHM; out-of-hours clearance 25 % BHM (not for automatically cleared BYUDs); inspection with officer 25 % BHM/hour (2 BHM out of hours; part hour = full hour); storage in a customs-owned warehouse 3 % BHM per tonne-day for the first 10 days, then 4 %; advance ruling 75 % BHM (non-refundable); transit/processing 25 % BHM; legal-entity cash currency 2.5 BHM; courier 0.02 BHM/kg. | VMQ 55 annex 1 | SOURCED (75 %, 25 % verified V3; others BI/fees.json) | Each fee row has its own source chip; the "what could still cost money" box lists them for the shipment's corridor. |
| PE-16 | **IMEI:** phones 8517 13 require IMEI per unit in grafa 31; registration after IM40. | VMQ 778 cl. 14 | SOURCED (fee [UNVERIFIED]) | Given 8517130000, when IMEIs are missing, then the draft has a blocker on grafa 31. |
| PE-17 | **Banned-goods check:** VMQ 658 UAV codes → red "No-go: taqiqlangan / faqat VM alohida qarori bilan (VM 658)". | VMQ 658 | SOURCED (HS2022 mapping [UNVERIFIED]) | Given a VMQ 658 code, then the shipment cannot reach draft or fill. |
| PE-18 | **Multi-line allocation (DEC-19):** freight/insurance split across items by **gross weight by default**, option to split by value; Σ allocated = total; method logged in the audit pack. Official rule not found. | BK 304; DEC-19 | Product decision (official rule [UNVERIFIED]) | Given N items and default settings, then allocation is by gross weight, Σ = total to the tiyin, and the audit pack records "taqsimlash usuli: brutto vazn"; switching to value re-quotes and logs the change. |
| PE-19 | **Rounding:** grafa 45 customs value to 2 decimals, statistical value to 3 decimals (SOURCED, 2773 cl. 25 sub-points 40–42); payment sums per payment to whole soʻm — [UNVERIFIED]. | Instruction 2773 (edition with 2773-15 of 22.07.2026) https://lex.uz/uz/docs/2924955 | [UNVERIFIED] | Rounding mode is a config flag and printed in the calculation trace. |
| PE-20 | **Missing data states:** `STAVKA_TOPILMADI` (no amount), `KURS_YO'Q`, `BIRLIK_MIQDORI_YO'Q`, `KELIB_CHIQISH_NOMA'LUM` (300¹ risk), `BOG'LIQ_SHAXS` (Y35), `NAZORAT_TOVARI` (stop), `TAQIQLANGAN` (PE-17). | T §3 item 9 | EXPERT-ONLY | Each state has a unit test; none produces a number. |
| PE-21 | **"Rasmiy" chip** only on: duty rate, VAT rate, excise rate, fee band + BHM, CB rate with date. Freight, insurance, customs value and totals = "≈ Taxmin asosida". | answers-tariff §2 | EXPERT-ONLY (TIF TN sign-off) | No total or estimate-based amount carries "Rasmiy" (snapshot test on p10/p15). |
| PE-22 | **Gold case — BLOCKED.** Reproduce one released IM40 to the soʻm before any calculation is called "verified". Needs (declarant-v3-check §H): a cooperating importer or broker; **one IM40 released after 01.09.2026**, preferably 2–5 items, ad valorem + VAT, no excise/exemption/marking, road, origin certificate present; **signed consent and an NDA** (ZRU-547 arts. 21, 28); the TED and **source documents** (invoice, contract/E-kontrakt ID, CMR, packing list, freight invoice, origin certificate), CB rate on acceptance day and the ed1 reconciliation act; redaction per §H (mask identities, keep every number used). No filled accepted BYUD is published on lex.uz or customs.uz. The TIF TN recalculation of YG-0412 is an illustration only. | spec v2 §1; T §3; DC §H | [PENDING: cooperating importer/broker] | The engine reproduces every grafa 47 row and the total to the soʻm from the kept values, or any difference is explained in writing; until then demo Set A shows "namuna", never "verified". |

### 3A.1 Config flags for every UNVERIFIED engine/rule item

**🔒 DPO** in the Owner column marks a flag that exposes client data. Turning it on or changing it needs two approvers, one of whom is the YuklaGo DPO — the named responsible person under ZRU-547 art. 31 (PC-15; `roles-rbac.md` SoD rule 5). The change is logged with who and when. An Admin alone cannot enable it. `roles-rbac.md` names masking-off, `CABINET_STATUS_READ` and `ED2_LIVE_AUTOMATION`. `AUDIT_LOG_RETENTION_YEARS` is added by PM reading: it decides how long client data is kept. PII masking has no off-switch in this spec (AC-32.3 fail-closed); any future flag that weakens masking or uploads session values is 🔒 DPO by default.

| Flag | Default | Source status | Owner |
|---|---|---|---|
| `FEE_BAND_EDGE_RULE` | lower-inclusive/upper-exclusive + "chegara noaniq" warning at exact edges | ASSUMPTION (VMQ 55 text explicit only for last band) | TIF TN |
| `FEE_USD_CONVERSION_DATE` | acceptance date (BK 326 by analogy) | ASSUMPTION | TIF TN |
| `BHM_DATE_RULE` | BHM in force on acceptance date (BK 324 by analogy) | ASSUMPTION | TIF TN |
| `BHM_PREVIOUS_412000` | disabled (no back-dated calculations) | [UNVERIFIED] (PF-91 not read on lex.uz) | TIF TN |
| `PRELIM_DISCOUNT_SCOPE` | applies only to item 1"a" fee, IM40 pre-arrival | ASSUMPTION (text verified; scope inferred) | TIF TN |
| `ROUNDING_MODE` | payment sums: half-up to whole soʻm, labelled (grafa 45 = 2 decimals and statistical value = 3 decimals are SOURCED, 2773 cl. 25 sub-points 40–42) | [UNVERIFIED] for soʻm payment sums only | TIF TN |
| `S300_BAND_EDGES` | show both values at 10/20/30 % | [UNVERIFIED] | TIF TN / Huquq |
| `S300_ZERO_RATE_GOODS` | show "noaniq", no surcharge amount | [UNVERIFIED] | TIF TN |
| `S300_ON_COMBINED_RATES` | surcharge on ad valorem leg only, labelled | [UNVERIFIED] | TIF TN |
| `S300_IN_VAT_BASE` | include, labelled [INFERENCE] | [UNVERIFIED] | TIF TN |
| `SPECIFIC_KG_NET_OR_GROSS` | net, labelled | [UNVERIFIED] | TIF TN |
| `FREIGHT_ALLOCATION_METHOD` | gross weight (DEC-19); option: value; logged | [UNVERIFIED] official rule; product decision | CEO / TIF TN |
| `INCOTERMS_2020_GRAFA20` | map 2020→code with warning; DPU flagged | [UNVERIFIED] | Deklarant |
| `ST1_FORM_TEXT` | ST-1 claim requires user upload + review | [UNVERIFIED] | TIF TN |
| `TR_PTA_10DIGIT_RATES` | re-check before showing a preferential rate | [UNVERIFIED] | TIF TN |
| `PQ58_EFFECTIVE_DATE` | 16.02.2026 (consolidation date) | [UNVERIFIED] (PQ-58 text) | TIF TN |
| `VM43_CONFORMITY_LIST` | "Tekshirilmadi" instead of "Topilmadi" | [UNVERIFIED] | TIF TN |
| `SES_PHYTO_VET_LICENCE_LISTS` | "Tekshirilmadi" | [UNVERIFIED] | TIF TN |
| `ASL_BELGISI_LED_MAPPING` | do not show "talab qilinmaydi" for 8539 52 | [UNVERIFIED] | TIF TN |
| `ASL_BELGISI_5DAY_NOTICE_GROUPS` | reminder off | [UNVERIFIED] | TIF TN |
| `VM658_HS2022_MAPPING` | treat 8806 as banned pending mapping | [UNVERIFIED] | TIF TN / Huquq |
| `IMEI_FEE` | not shown | [UNVERIFIED] | TIF TN |
| `EXPORT_DUTY_TABLE` | "rasmiy stavka topilmadi" | [UNVERIFIED] | TIF TN |
| `ADVANCE_RULING_TERM_RECHECK` | show "1 yil (BK 369–372)" | [UNVERIFIED] re-check | TIF TN |
| `PF250_INSTALMENT_14D` / `DUTY_DEFERRAL_120D` | not offered; info only | [UNVERIFIED] conditions | TIF TN / Huquq |
| `DAY1_COUNTING_15D` | show both: "File by" +14 and "Legal max" +15 (DEC-17) | [UNVERIFIED] start-day rule | Huquq / Deklarant |
| `STORAGE_WEEKEND_ROLL` | no roll-over | [UNVERIFIED] | Huquq |
| `POST_CALENDAR_VERIFIED[post]` | false → show the earlier date + "post taqvimi tasdiqlanmagan" flag (DEC-20) | per post; ops-maintained, sourced and dated | YuklaGo ops |
| `HOLIDAY_CALENDAR` | official decrees only, each entry with source + date | ops-maintained | YuklaGo ops |
| `TOL_GROSS_WEIGHT` | D = declared gross (invoice figure; per line: invoice line gross); weights rounded to 3 decimals; diff = abs(A − B); diff = 0 pass; ≤ 1 kg info; ≤ T = max(1 % × D, 20 kg) warning (exact hit on T = warning); else block; every pair, per line and total, worst wins — "PROPOSAL, not law" (admin-configurable) | PROPOSAL (no official tolerance found; `tolerances.json` `gross_weight_docs.formula`) | Deklarant / CEO |
| `TOL_NET_WEIGHT` | D = declared net (invoice line net; total: invoice total net); 3 decimals; diff = 0 pass; ≤ T = max(0.5 % × D, 5 kg) warning (explicit max, not min; exact hit = warning; no info tier); else block; per line and total, worst wins (a line error is not hidden by the total) — "PROPOSAL, not law" | PROPOSAL (`tolerances.json` `net_weight_docs.formula`) | Deklarant / CEO |
| `TOL_PACKAGES` / `TOL_QUANTITY` | exact match, else block — "PROPOSAL, not law" | PROPOSAL | Deklarant / CEO |
| `TOL_OTHER_CHECKS` | remaining 13 checks of `tolerances.json` with its proposed defaults | PROPOSAL | Deklarant |
| `PALLETS_AS_PACKAGING` | ask the user whether pallets are in the stated gross; never auto-subtract pallets; explain the CMR vs grafa 35 gap (gross excludes containers and other transport equipment, 2773 cl. 25 sub-point 30; export cl. 22 sub-point 30) | [UNVERIFIED] — UNCONFIRMED whether pallets are packaging or transport equipment (`tolerances.json` `gross_weight_scope.pallets`; README open question 6) | Deklarant |
| `MOVE_OUT_3DAYS_UNIT` | calendar days (earlier) | [UNVERIFIED] calendar vs working (BK 89) | Huquq |
| `GRAFA33_RIGHT_PART` | empty; check live ed2; no demo claim | [UNVERIFIED] | Deklarant |
| `GRAFA41_UNIT_CODES` | unit from PQ-181 annex 1; numeric code check vs live ed2; no demo claim | [UNVERIFIED] | Deklarant |
| `GRAFA44_904_ENTRY` | IM40: propose one grafa 44 line "904 МЕТОД <method number>", e.g. "904 МЕТОД 1" for transaction value (BK 303), labelled our inference; line format is a proposal; not in demo answer keys; check when it is mandatory and the entry UI on live ed2; EK10: not proposed (the EK10 map does not mention 904) | [INFERENCE] — 904 is Annex 12 item 113; grafa not stated; when mandatory and line format UNVERIFIED (`grafa-map.json` grafa 44 `additional_document_codes`, `verified_on_live_ed2: false`) | Deklarant / TIF TN |
| `TARIFF_PREF_AS_6XX` | do not add a 6XX line for a tariff preference; show 701 "СПТИМ" certificate only | [UNVERIFIED] — cl. 25 sub-point 39 "е" covers exemptions/privileges on payments; tariff preference as 6XX not stated | TIF TN / Deklarant |
| `HOLIDAY_ARTICLE_AND_TRANSFERS` | seed known holidays (e.g. 8 Dec 2026, Constitution Day); each entry cites its decree | [UNVERIFIED] Labour Code article and 2026–2027 rest-day transfer decrees | YuklaGo ops / Huquq |
| `DESKTOP_EIMZO_SIGNING` | Electron app: signing tested in the Q-6 session and as a build-phase acceptance test on Windows, then macOS; if it fails, fall back to the system browser with the YuklaGo MV3 extension (DEC-23) | [UNVERIFIED] (ed2 loads `e-imzo-client.js`; local E-IMZO service, origin/API-key checks) | Engineering / Deklarant |
| `BROKER_REGISTER_URL` | not shown | [UNVERIFIED] whether a public register exists | Deklarant |
| `GRAFA45_LEFT_SUBFIELD` | empty; check live ed2; no demo claim | [UNVERIFIED] | Deklarant |
| `GRAFA47_LAYOUT_ROUNDING` | rows per Annex 13 codes; rounding per ROUNDING_MODE; check live ed2; no demo claim | [UNVERIFIED] | Deklarant / TIF TN |
| `SETC_CONFORMITY_CERTS` | Set C shows "sertifikat talabi tekshirilmagan"; no demo claim | [UNVERIFIED] | Deklarant / TIF TN |
| `MJTK_EDITION_2026_12_30` / `MJTK_EDITION_2027_02_05` | fines shown per current edition; re-check 227¹⁰ / 227²⁶ before each date; no demo claim | [UNVERIFIED] future editions on lex.uz | Huquq |
| `MICROWAVE_ENERGY_CLASS_G31` | ask; no demo claim | [UNVERIFIED] | Deklarant |
| `STORAGE_EXPIRY_CONSEQUENCE` | show nothing beyond "muddat tugaydi" | [UNVERIFIED] | Huquq |
| `ADVANCE_INFO_TIMES` | not shown | [UNVERIFIED] | Deklarant |
| `NONENTREPRENEUR_COMMERCIAL_IMPORT` | route to "YaTT yoki MChJ orqali" | [UNVERIFIED] | Huquq |
| `SELF_EMPLOYED_IMPORT` | same as above | [UNVERIFIED] | Huquq |
| `TRUSTED_PERSON_CAN_SIGN` | false | [INFERENCE/UNVERIFIED] | Deklarant / Huquq |
| `YATT_EMPLOYEE_SIGNER` | false (YaTT signs personally or uses broker) | [UNVERIFIED] | Deklarant |
| `SIGNER_KEY_STIR_LINK` | warn | [UNVERIFIED] | Deklarant |
| `ED1_LIST_FORM_FIELDS` | capture in supervised session | [UNVERIFIED] | Deklarant |
| `EKONTRAKT_MISSING_ID_REJECT` | blocker for paid contracts | [UNVERIFIED] | Huquq |
| `EKONTRAKT_PENALTY_ARTICLE` | not shown | [UNVERIFIED] | Huquq |
| `BANK_DOC_LIST` | "ro'yxatni bankingizdan oling" | [UNVERIFIED] | Huquq |
| `CURRENCY_LAW_EDITION` | re-check before launch banner | [UNVERIFIED] | Huquq |
| `EXPORT_EK10_TARGET` | cargo.customs.uz; ed2 off | [UNVERIFIED] | Deklarant |
| `EK10_GRAFA_LIVE_CHECKS` | show "tekshirilmagan" on: grafa 8 foreign-consignee TIN field; grafa 18 vehicle-type codes beyond 70; grafa 31 lines 6–11 absent for EK10; grafa 37 "000"; grafa 40 empty for own production; grafa 43 when consignor ≠ exporter; grafa 45 left subfield; export fee band; no demo claim | [UNVERIFIED] — ⚠️ items in `grafa-map-ek10.md` (point 22 sub-points 17, 31, 47 absent in the edition read) | Deklarant |
| `CONFORMITY_LEAD_TIME` | stage times only, no total | [UNVERIFIED] | Deklarant |
| `CONFORMITY_APPLICATION_URL` | no link | [UNVERIFIED] | Deklarant |
| `PHYTO_DECISION_5WD_CURRENT` | show "5 ish kuni (VMQ 727)" with re-check note | [UNVERIFIED] later amendment | Deklarant |
| `PHYTO_30_15_DAY_NOTICE` | not shown | [UNVERIFIED] | Deklarant |
| `PHYTO_FEE` / `ORIGIN_CERT_FEE` | not shown | [UNVERIFIED] | Deklarant |
| `VET_TIMES_VM148` | show 2/7 wd with "qayta tekshirilsin" | SOURCED by BE, [UNVERIFIED] by AD | Deklarant |
| `ORIGIN_FORM_TR_APRICOT` | "xaridordan so'rang" | [UNVERIFIED] | Deklarant |
| `FRUITVEG_MIN_EXPORT_PRICES` | not shown | [UNVERIFIED] | Deklarant |
| `REEXPORT_6_MONTHS` | not shown | [UNVERIFIED] | Huquq |
| `TEMP_IMPORT_GUARANTEE_SIZE` | not computed; user enters | [UNVERIFIED] | TIF TN / Huquq |
| `VM212_FULL_RELIEF_LIST` | not auto-applied | [UNVERIFIED] | TIF TN |
| `TRANSIT_SECURITY_GOODS_LIST` | ask user / partner | [UNVERIFIED] | Huquq |
| `COTTON_TEXTILE_EXPORT_LIMITS` / `GSP_REX` | "mutaxassis tekshirsin" flag | [UNVERIFIED] | Deklarant |
| `MAX_ITEMS_PER_BYUD_N` | unset; warn above pilot value | [PRACTICE] | Deklarant |
| `DEADLINE_ESCALATION_2WD` | warn at ≤2 working days with blockers; threshold labelled [PRACTICE] | [PRACTICE] | Deklarant |
| `ED2_LIVE_AUTOMATION` | not yet enabled — **ready, enabled when the founder confirms** (DEC-24); mock portal for demos until on | Founder's switch; legal position in PC-1 | Hakathon CEO (coordinates with the founder) · **🔒 DPO** (founder's confirmation + DPO as second approver, DEC-29) |
| `CABINET_STATUS_READ` | off (user enters reg. number) | Appendix A PC-4 | Huquq · **🔒 DPO** |
| `XML_EXPORT` | off | Appendix A PC-3 | Deklarant / Huquq |
| `DESKTOP_EIMZO_COMPAT` | Electron: build-phase acceptance test on Windows first, macOS next; if E-IMZO fails in the app window, fall back to the system browser with the YuklaGo MV3 extension (DEC-23) | [UNVERIFIED] (automation.md: "E-IMZO compatibility ❓" for embedded Chromium) | Engineering / Deklarant |
| `DESKTOP_ENGINE` | Electron (DEC-28); OS order Windows → macOS | Decided | Hakathon CEO / Engineering |
| `AUTOMATION_SAVE_DRAFT_CLICK` | off ("your turn") | [DECISION NEEDED: CEO] | CEO |
| `AUDIT_LOG_RETENTION_YEARS` | 3 (server audit log, stored in Uzbekistan) — "proposal, not law" | PROPOSAL (`roles-rbac.md` §5: "taklif: 3 yil — tasdiqlanmadi"); ZRU-764 art. 16 applicability [UNVERIFIED] (Q-10) | CEO / Huquq · **🔒 DPO** |
| `SUPPORT_ACCESS_DEFAULT_HOURS` | 24; closes automatically; the Owner can revoke at any time | PROPOSAL (`roles-rbac.md` SoD rule 4, "standart 24 soat") | CEO / Security |
| `CERT_PUBLIC_FIELDS_AUTODETECT` | **true** (Hakathon CEO, Q-21 closed 19.11) — conditions in AC-1.15–AC-1.21. Until the E-IMZO domain API key exists (PC-16), the app falls back to the one-time confirm (AC-1.9) | Security YES + Huquq YES with conditions; E-IMZO API and integrator/registration-centre terms [UNVERIFIED]; reading ed1 automatically is grey-zone and not done. The CEO's decision sets the default; as a 🔒 DPO flag it still needs sign-off by the named responsible person (ZRU-547 art. 31, PC-15) before launch | Security / Huquq / Hakathon CEO · **🔒 DPO** |

---
## 4. Full broker task coverage (DEC-13)

Every task from `broker-import.md` (63) and `broker-export-regimes.md` (52) is mapped to a YuklaGo feature with one testable acceptance check. "Human step" means a physical or legal act the **user** (or their own staff) performs — YuklaGo prepares, guides and tracks it; the partner broker (Y31) is offered only as an optional fallback. **Nothing is out of scope**; items whose live behaviour depends on official confirmation point to Appendix A.

### 4.1 Import (broker-import.md)

| Task | Broker task | Feature(s) | Acceptance check |
|---|---|---|---|
| A1 | Client legal status (LLC / YaTT / individual, STIR, FTP) | Y1, Y41 | Given STIR entry, the profile shows status and the allowed paths; an individual with commercial goods is routed per R59. |
| A2 | Path and regime (parcel / passenger / commercial IM40) | Y2 | Given a post/courier shipment ≤30 BHM to a legal entity, the router shows "pochta/kuryer hujjati deklaratsiya sifatida" with BK 165, 167. |
| A3 | Who signs: ERI, declaring person, PoA | Y1 | Given no listed signer in ed1, filing steps stay locked and the my.gov.uz 207 guide is shown. |
| A4 | Contract with a broker (on escalation) | Y31 | Given the user picks a partner, a contract checklist (BK 277) and declaring-persons list entry guide are shown; YuklaGo is not a party. |
| A5 | Client customs history and debt | Y41 | Given the user enters reconciliation-act figures from ed1, debts and advances appear with source "ed1 (siz kiritdingiz)". |
| B1 | Foreign-trade contract and E-kontrakt | Y6 | Given a paid contract without E-kontrakt ID, the draft has a blocker on grafa С item 1 (flag EKONTRAKT_MISSING_ID_REJECT). |
| B2 | Invoice 12-field check | Y9, Y13 | Given an invoice missing any of the 12 fields, the missing field is named with VMQ 605 annex 1a. |
| B3 | Transport document | Y9 | Given a CMR/AWB/B/L/rail bill, number, date, carrier and weight are extracted and cross-checked with the invoice. |
| B4 | Packing list | Y9 | Packing list never appears as "required"; shown as "post so'rashi mumkin" [PRACTICE]. |
| B5 | Origin and certificate | Y5, Y11 | Given origin "yo'q", the 300¹ line and side-by-side totals appear (PE-10). |
| B6 | Conformity certificate | Y7 | Given a code under VMQ 43 [flag], the go/no-go shows "MSO tanlang (VMQ 502)" with stage times and no total lead time. |
| B7 | Sanitary / phyto / vet control | Y7, Y36 | Given a vet/phyto code, the plan shows the permit, body, Yagona darcha step and its own clock; no draft is sent before the permit is in Yagona darcha. |
| B8 | Licence, permit, quota, dual-use | Y7 | Given a licensed/dual-use code, the go/no-go lists the permit body and law; filing is blocked until the user records the permit number. |
| B9 | Asl Belgisi marking | Y7 | Given a VMQ 737 group, the draft requires the AIK code before fill. |
| B10 | Cross-checking documents, translation | Y13, Y9 | Given conflicting weight/value between invoice and transport doc, a conflict card lists both values and sources. |
| C1 | Choosing the code | Y10 | Given a product, at most 3 official codes with official text and reasons; low confidence → clarifying questions or C3. |
| C2 | Splitting a multi-line invoice | Y27 | Given a 1688 invoice with 12 lines, items are grouped by code with Σ values = invoice total. |
| C3 | Advance classification ruling | Y10 | Given low confidence, a ruling request pack with fee 75 % BHM (PE-15) and validity note is generated. |
| D1 | Valuation method choice | Y35 | Given method-1 failure, the user is guided through methods 2–6 with required evidence. |
| D2 | Additions (BK 304) | Y11 | PE-3. |
| D3 | Deductions (BK 305) | Y11 | PE-4. |
| D4 | Incoterms value structure | Y11 | PE-5. |
| D5 | Customs value declaration (BQD) | Y35, Y12 | Given an IM40 draft, the BQD block is generated from the same data and checked for consistency. |
| D6 | Exchange rate and date | Y11 | PE-6. |
| D7 | Value control: extra documents, adjustment, conditional release | Y35, Y36, Y39 | Given a customs value query, the response pack lists requested documents, response deadline (if stated in the message) and conditional-release security option. |
| E1 | Customs duty (ad valorem, specific, combined, extra) | Y11 | PE-7–PE-10. |
| E2 | VAT | Y11 | PE-13. |
| E3 | Excise | Y11 | PE-12. |
| E4 | Customs fees VMQ 55 full list | Y11 | PE-14, PE-15. |
| E5 | Payment: personal treasury account, advance, payment not visible | Y28 | Given payment due, the user sees the amount, bank details source (customs.uz) and a "to'lov ko'rinmayapti" troubleshooting list; YuklaGo never pays. |
| E6 | Deferral, instalments, security | Y39 | Given a deferral request, the eligibility checklist (BK 329–333) and security methods (BK 339–346) are shown; PF-250 items under flags. |
| E7 | Privileges and preferences | Y5, Y11 | PE-11. |
| E8 | Refund of overpayment | Y40 | Given an overpayment, a refund application pack with 3-year clock (BK 353–357) is produced. |
| F1 | Preliminary declaration | Y30 | Given goods not yet arrived, the pre-arrival path shows −20 % fee and the 30-day lapse clock (R10). |
| F2 | Filling the TED (grafas) | Y12, Y14 | Given a draft, 46 IM40 grafas are mapped per item; the desktop app fills the mock, and the live cabinet once `ED2_LIVE_AUTOMATION` is on. |
| F3 | Checking permits in Yagona darcha | Y7 | Given a controlled code, filing is blocked until the user confirms the permit is visible in Yagona darcha (R63). |
| F4 | E-arxiv upload and number in TED | Y29 | Given uploaded files, the user enters each E-arxiv number and grafa 44 shows it. |
| F5 | Sign with ERI and send | Y16 | The automation stops before the sign button; the user signs and sends in the official window. |
| F6 | Format-logic control replies | Y19, Y13 | Given a pasted rejection message, the explainer maps it to grafa and fix (44-message library). |
| G1 | Advance information and arrival notice | Y38 | Given a carrier, the user is told advance info is the carrier's duty (BK 206) and asked to record arrival notice. |
| G2 | Arrival confirmation, warehouse acceptance, unloading discrepancy | Y38 | Given an arrival date entered, R6/R9 clocks start; a discrepancy form is offered. |
| G3 | Clocks (declaration, storage, preliminary) | Y8 | Given dates entered, each clock shows end date, article and counting rule; unknown inputs show "≤60 kun (ombor hujjatidan)". |
| G4 | Viewing goods in warehouse, sampling, warehouse costs | Y36, Y38 | Given a request to view goods, a request template and VMQ 55 storage fee rows are shown. |
| G5 | Damaged/lost goods, broken seal | Y38 | Given a damage report, a notification checklist and photo log are generated; filing paused. |
| H1 | Risk level and waiting time explanation | Y19 | Corridor message explained with R36 and R11 times as "bojxona ishlov muddati", not a user countdown. |
| H2 | Request for originals / extra documents | Y36 | Given a request message, a document checklist with E-arxiv upload steps is produced. |
| H3 | Customs inspection | Y36 | Given a red corridor, an inspection prep checklist (who attends, goods access, fee 25 % BHM/hour) is shown. |
| H4 | Customs examination and samples | Y36 | Given a sampling order, the user sees the sample act checklist and tracks the result. |
| I1 | Change or withdraw before acceptance | Y33 | Given a not-yet-accepted BYUD, withdraw/change steps are shown with BK 266. |
| I2 | Voluntary typo correction (1 working day) | Y33 | Given acceptance, a 1-working-day clock and "kod va raqamlar bundan mustasno" rule are shown (R40). |
| I3 | Correction during clearance (KTS) | Y33 | Given an officer request, the change is prepared and fee 25 % BHM shown if on declarant request. |
| I4 | Post-release correction / withdrawal (3 years) | Y33 | Given a post-release error, a correction pack with the 3-year limit is generated. |
| J1 | Appeal against a customs decision | Y37 | Given a decision date, a 30-day appeal clock (BK 409-2) and form (409-3) draft are produced for the user to file. |
| J2 | Administrative offence case | Y37 | Given a protocol, the case is explained (article, fine range) and the user is told to get legal help; YuklaGo does not represent. |
| K1 | Release conditions and notice | Y19 | Given a release status entered, next steps (payment, permit) are shown. |
| K2 | Download TED and e-documents within 15 days | Y34 | Given release, a 15-day download reminder (VMQ 605 cl. 37) appears. |
| K3 | Exit from warehouse and accounting entry | Y25, Y38 | Given release, an accounting export (CSV) with landed cost per item is produced. |
| L1 | Post-release control and audit | Y23 | Given an audit notice, a document index per BYUD is generated. |
| L2 | Keeping records | Y34 | Given a closed shipment, all documents and calculation traces are retained with version stamps. |
| L3 | E-kontrakt 180-day control | Y6, Y8 | Given an import payment date, a 180-day clock (Nizom cl. 23) and fine stages (R60) appear. |
| L4 | Later origin certificate and refund (1 year) | Y5, Y40 | Given a certificate obtained after release within 1 year, a refund pack (BK 366) is produced. |
| L5 | Product library and repeat import | Y20 | Given a repeat product, the stored code, docs and permits prefill and any rate change since last use is flagged. |
| L6 | Debts and penalty interest | Y41, Y28 | Given an unpaid amount, the 1/300 per-day rule (BK 349) is explained; no amount is computed without the refinancing rate source. |

### 4.2 Export and special regimes (broker-export-regimes.md)

| Task | Broker task | Feature(s) | Acceptance check |
|---|---|---|---|
| A1 | Regime choice EK10 / EK12 / EK11 | Y2 | Given "goods will come back", the router proposes 12 (or 11 for previously imported goods), never 10. |
| A2 | E-kontrakt for export contract/invoice | Y6 | Given an export without E-kontrakt entry, filing is blocked (R31). |
| A3 | Export TIF TN code | Y10 | Same as import C1 with the export library entry. |
| A4 | Fill and submit export BYUD | Y21, Y14 | Given an EK10 draft, the target is cargo.customs.uz (flag EXPORT_EK10_TARGET); the draft uses the EK10 grafa list (cl. 21) and asks "Bu tovarni oʻzingiz ishlab chiqarganmisiz?" for grafa 43. |
| A5 | Export declaration before departure | Y8 | Export clock "chiqib ketishidan oldin" (R7). |
| A6 | Origin certificate via O'zbekekspertiza | Y5, Y21 | Given a buyer country, the form options (ST-1/A/ST-UZ) and 1–2 wd time are shown; fee not shown. |
| A7 | Phytosanitary certificate | Y7, Y21 | Given a plant product, a per-consignment phyto step via Yagona darcha with 5 wd decision is shown. |
| A8 | Veterinary export permit and certificate | Y7, Y21 | Given an animal product, two steps (annual permit, certificate) with VMQ 148 times under flag. |
| A9 | Fumigation, pallet heat-treatment, storage | Y21 | Given an export pack, a packaging/storage checklist is included and marked "manzil davlati talabi — tekshiring". |
| A10 | Perishables: short storage, fast lane | Y8, Y21 | Given perishables, the 10-day storage cap applies. |
| A11 | Fruit/veg rules (loss norms, unfair-exporter register, min price) | Y21 | Given 07/08/0904/1202 codes, the VMQ 163 checklist appears; min prices under flag. |
| A12 | Currency proceeds 180 days + fines | Y6, Y8 | Given an export date, the 180-day clock and 5/10/35 % fine stages appear (R60). |
| A13 | VAT 0 % on export | Y21 | Given release, the VAT-0 proof checklist (Tax Code 260–261) is generated. |
| A14 | Export fee VMQ 55 | Y11 | PE-14 applies to EK10. |
| A15 | Asl Belgisi on export (withdraw codes) | Y7, Y21 | Given marked goods, a "kodlarni aylanmadan chiqarish" step is shown with source [flag]. |
| A16 | Cotton/textile limits, destination certs, GSP+/REX | Y21 | Given textile codes, a specialist-check flag is shown (COTTON_TEXTILE_EXPORT_LIMITS / GSP_REX). |
| A17 | Destination-country requirements | Y21 | Destination checklist marked "tasdiqlanmagan — xaridordan so'rang". |
| B1 | Re-export conditions | Y22 | Given regime 11, identification and "unused, unchanged" confirmations are required. |
| B2 | Re-export documents | Y22 | Re-export document template generated. |
| B3 | 3 working days for transit declaration | Y8, Y22 | Clock "3 ish kuni (BK 32)". |
| B4 | Refund of import duties on re-export (2 years) | Y40, Y22 | Given re-export within 2 years, a refund pack (BK 35) is produced. |
| B5 | Origin/phyto for re-export | Y22, Y7 | Re-export phyto/origin step shown. |
| C1 | Temporary regime choice (exhibition, equipment, lease) | Y2, Y22 | Router questions produce 42 or 12 with reasons. |
| C2 | Conditions and prohibited categories | Y22 | Given a BK 62 category, regime 42 is refused with the article. |
| C3 | Documents (lease/leasing contract) | Y22 | Template includes contract type field. |
| C4 | 2-year term, completion | Y8 | Clock "2 yil (BK 64, 69)". |
| C5 | Full relief (VMQ 212) or 5 %/month | Y11, Y22 | Given partial relief, monthly 5 % of duties/taxes computed (BK 66); full relief list under flag. |
| C6 | Guarantee size and form | Y39 | Given regime 42, the user enters guarantee details; size not computed (flag). |
| C7 | ATA carnet | Y22 | Explainer and checklist for ATA use (R47). |
| C8 | Temporary export (2 y) and re-import (3 y) | Y22, Y8 | Clocks for 12 and 41. |
| D1 | Processing permit | Y22 | Permit application checklist (BK 70–82 / 42–54). |
| D2 | Yield norm | Y22 | Yield norm entered only from the user's technological documents; the LLM never proposes one. |
| D3 | Identification, residues, waste | Y22 | Fields present in the processing pack. |
| D4 | Permit terms and extension 1 month before | Y8 | Clocks per R46. |
| D5 | Completing the regime, accounting for product | Y22 | Completion checklist and raw-material balance sheet from user inputs. |
| D6 | Fee 25 % BHM | Y11 | R25 row. |
| D7 | E-kontrakt for processed-product export | Y6 | Checklist entry. |
| E1 | Who is declarant (usually carrier) | Y2, Y22 | Router asks the user's role; owner-only users are told the carrier/forwarder declares. |
| E2 | Transit declaration via E-Tranzit / us-uz | Y22 | Guide names E-Tranzit/us-uz; no automation target until confirmed (PC-7). |
| E3 | TIR and ATA | Y22 | Explainer per VMQ 737 (2022). |
| E4 | Transit security | Y39 | Security entered by the user (flag TRANSIT_SECURITY_GOODS_LIST). |
| E5 | Transit permits (incl. vet transit) | Y7 | Go/no-go applies to transit. |
| E6 | Transit terms (air 3 d; land/water 15 d per 1000 km) | Y8 | Clock computed from mode and distance with BK 120. |
| E7 | Fee 25 % BHM; change 10 % BHM | Y11 | R25 rows. |
| E8 | Electronic transit (NCTS-like) | Y22 | Copy uses "E-Tranzit"; "NCTS" never shown. |
| F1 | Yagona darcha permits | Y7 | Same as import F3. |
| F2 | Conformity certificate (import) | Y7 | Same as import B6. |
| F3 | Asl Belgisi AIK on import | Y7 | Same as import B9. |
| F4 | Special goods licence | Y7 | Licence body and law named; filing blocked until permit number recorded. |
| F5 | Export control and dual-use | Y7 | Given a dual-use hit or catch-all doubt, a permit step (Law 658-II) is required. |
| F6 | Vet/phyto permits on import | Y7 | Import vet/phyto steps with VMQ 148 ch. 4 times [flag]. |
| F7 | Quotas | Y7 | Quota status shown as "joriy kvotalar tasdiqlanmagan" and the user must confirm with the permit body. |

**Count:** 63 + 52 = **115 tasks, 115 mapped, 0 out of scope.**

---
## 5. Features (Y1–Y43) with acceptance criteria

Priority: **P0** = needed for a full IM40 self-file and the demo; **P1** = needed for full broker replacement (DEC-13); **P2** = convenience. Gap links refer to `product.md` G1–G8 (G8 — "no formal AC in v2" — is closed by this section as a whole). Every AC is testable on the mock portal; live-cabinet AC run only after Appendix A PC-1 clears.

### Y1 Readiness and signer set-up — P0 (G4)
Covers broker tasks A1, A3. Checks ERI (R34), ed1 declaring-persons list via my.gov.uz 207 (R3), E-arxiv access (R4), E-kontrakt access (R31).
- **AC-1.1** Given the user has no E-IMZO key, when they open readiness, then the step names the issuer "Yangi texnologiyalar" ilmiy-axborot markazi, the three channels (PSC, single portal, e-imzo.soliq.uz for heads) and shows **no address and no fee**.
- **AC-1.2** Given the user says the signer is a staff specialist, when the signer is not confirmed as listed in ed1 with a valid authority period, then Y14/Y16 stay locked with the reason "imzolovchi ro'yxatda emas". The staff specialist is then the account user (AC-1.7).
- **AC-1.3** Given a YaTT whose employee wants to sign, then the app shows flag YATT_EMPLOYEE_SIGNER and the options "o'zingiz imzolang yoki broker".
- **AC-1.4** Given the user asks YuklaGo staff to sign, then the request is refused with the R38 explanation and Y31 is offered.
- **AC-1.5** The checklist never says "registered authorised specialist"; it says **"deklaratsiyalovchi shaxslar roʻyxatiga kiritilgan shaxs"** (DEC-10; VMQ 605 cl. 15 wording "roʻyxatga kiritadi").
- **AC-1.6** Given the user says a broker's specialist will sign, then that specialist is **not** a user of this account (DEC-29: one client role, account user = signer). The app offers the hand-off pack (Y18) and the partner-broker option (Y31). The checklist asks the user to confirm "broker xabarnomasi bor" (the broker has notified the Customs Committee, VMQ 847; ZRU-701), that the **broker** (not the user) listed its specialist in ed1, and to upload the broker contract (BK 277). No public broker-register link is shown (`BROKER_REGISTER_URL` [UNVERIFIED]). Confirmed by the Hakathon CEO (DEC-29): a broker's specialist never signs inside a client account.
- **AC-1.7** (DEC-29) At set-up the user confirms that **they are the signer** (the UI says "Siz imzolaysiz" after the check; no role picker): the director (or YaTT) or a staff specialist entered in the ed1 declaring-persons list, with the authority period from ed1. YuklaGo does not read ed1 (`CABINET_STATUS_READ=off`); the user confirms the entry and types the authority end date. One account belongs to one person, who is its signer. The app has no screen to assign a client role or give a user different permissions; other people of the same company get their own accounts (AC-1.12).
- **AC-1.7a** Given the user is not the director (a staff specialist), then set-up warns: "Direktor ed1 → TIF ishtirokchilari roʻyxati orqali sizni qoʻshishi kerak" — the declarant (in practice the director, logging in with the director's own ERI) enters them in the ed1 list as a staff specialist with an employment contract (VMQ 605 cl. 2, 15, 28; BK 284 defines the specialist as an employee of the legal entity). Set-up also shows the permanent line "Faqat oʻz ERI kalitingiz bilan imzolang. Boshqa odamning kalitini ishlatmang." A signature counts as the key holder's (VMQ 605 cl. 28); the private key is known only to its holder (VMQ 348 cl. 3); for a legal entity's key the head is responsible, and any use by others must be reported to the registration centre (ZRU-793 art. 27). Per Huquq, art. 27 has no literal "do not hand over" ban; the rule follows from these provisions together.
- **AC-1.8** Given the user answers that someone else (not the account user) will sign, then filing (Y14/Y16) stays locked with "Imzolovchi shu hisob egasi boʻlishi kerak" and the options: that person opens their own YuklaGo account under the same company (AC-1.12), or the broker hand-off (Y18/Y31). Accounts are never shared (`roles-rbac.md` gap 6).
- **AC-1.9** (Q-21 closed) The signer confirms **once**, at set-up and the first time a new certificate appears ("Men imzolovchiman"). There is no per-session confirmation. With `CERT_PUBLIC_FIELDS_AUTODETECT=true` a new certificate is detected automatically (AC-1.15–AC-1.21). Until the E-IMZO domain API key exists (PC-16), the app cannot detect a new certificate itself: the one-time confirm happens at set-up and again whenever the user reports a new key, an expired certificate or a different holder. YuklaGo never reads the E-IMZO dialog, the private key, the password or the PIN (AC-14.4).
- **AC-1.10** Given the ed1 authority end date entered at set-up, then a reminder appears before it (lead time per the user's notification settings), and on and after that date Y14/Y16 lock with "ed1 vakolat muddati tugagan" until the user confirms a renewed entry and a new end date.
- **AC-1.11** Trusted person (power of attorney) as signer stays off (`TRUSTED_PERSON_CAN_SIGN=false`, PC-5): VMQ 605 cl. 15 lists "ишонч билдирган шахс" for the ed1 list, but the cl. 2 definition of the declaring person does not include them [UNVERIFIED] (`roles-rbac.md` gap 9; Huquq).
- **AC-1.12** (Q-20 closed) Given a company (one STIR) with more than one signer, then each person has their **own** YuklaGo account: own phone login, own ed1 declaring-persons entry and authority period, own ERI. Each account passes AC-1.7 and its own re-checks (AC-1.9, AC-1.10). All accounts of the company have the **same single client role** and identical rights over the company's shipments; there are no per-user permissions, approvals or role differences (test: the permission set of every client account is identical).
- **AC-1.13** A login is never shared: given the signer confirmation or auto-detect (AC-1.9, AC-1.18) shows a person other than the account holder, the fill stops and the app points that person to their own account (AC-1.12).
- **AC-1.14** (Phase 1, Hakathon CEO) Every account holder is a signer who passed AC-1.7. There is no account type for people who do not sign. An accountant or other non-signer receives the downloadable audit pack / export (Y23, Y25, AC-43.8) from the account holder; they get no login. An accountant listed in ed1 as a staff specialist is a signer and may have their own account (`roles-legal.md` B1).
- **AC-1.15** (Q-21, auto-detect) When the user picks a key in E-IMZO, the app reads **only the public certificate fields** PINFL, STIR (TIN), serial number and validity date from E-IMZO's certificate list; the name (CN) is for display only and is not stored. Key-loading and signing functions are deny-listed in YuklaGo code (as AC-16.2). No other certificate field (e.g. address) is kept. The legal basis cited by Huquq is ZRU-793 art. 3, 20, 24.
- **AC-1.16** The comparison runs **on the server**: the client sends the values over TLS; the server computes HMAC-SHA256 in memory with a key held in Uzbekistan and returns only match / mismatch. Raw values never reach disk or logs. A plain salted hash is not used (Security: a 14-digit PINFL can be brute-forced offline; Huquq accepts a hash or the last 4 digits, and HMAC meets both).
- **AC-1.17** Stored: the HMACs of PINFL, STIR and serial, the validity date, and a masked view (e.g. PINFL ••••••••••1234, initials). They are deleted when the key is replaced or the account closes. They are stored in Uzbekistan and are **never sent to a foreign LLM** or any AI provider.
- **AC-1.18** On a mismatch or a new certificate, the app **warns only** ("Imzolovchi oʻzgardi. Yangi imzolovchi ed1 roʻyxatiga kiritilganmi?") and the person decides (ZRU-547 art. 24 — automated decisions; Huquq). If they answer "yes", the one-time confirm (AC-1.9) is recorded. If they answer "no", Y14/Y16 lock until AC-1.7 passes (Huquq: block only after the user's answer). The Owner is notified. Security had proposed blocking the fill on any mismatch; **warn-only is applied as the legal reading and is listed for the CEO to confirm**.
- **AC-1.19** Events are logged without raw values: `signer_match`, `signer_mismatch`, `cert_changed`, `cert_expiring` (Security also lists `cert_expired`), each with time, device and the serial-number hash.
- **AC-1.20** The set-up consent (Y32 consent version) adds a line stating the purpose, as ZRU-547 art. 19 requires: "Imzolovchi oʻzgarmaganini tekshirish uchun ERI sertifikatingizdagi JShShIR va STIRni oʻqiymiz. Ular faqat shifrlangan hash koʻrinishida saqlanadi. Kalit va parolingizga tegmaymiz." (Security's text). The privacy policy states the same purpose ("imzolovchi oʻzgarganini aniqlash va imzolovchi roʻyxatda borligini tekshirish", Huquq).
- **AC-1.21** The ed1 list is **never read automatically** (grey zone, [UNVERIFIED]; `CABINET_STATUS_READ=off`). The user still confirms the ed1 entry and authority expiry (AC-1.7, AC-1.10; VMQ 605 cl. 15). Before integration, the E-IMZO integrator terms and the registration centre's public offer are read (both [UNVERIFIED]; PC-16).

### Y2 Path and regime router — P0
Covers A2 (import), export A1, C1, E1. Regimes per DEC-9.
- **AC-2.1** Given a post/courier shipment to an LLC with value ≤ 30 BHM, then the router shows the BK 165/167 path and does not start a BYUD.
- **AC-2.2** Given "goods return to Uzbekistan", then options 12/41 appear with terms (R45); never EK10.
- **AC-2.3** Given previously imported unused goods leaving, then 11 is proposed with BK 32–35 conditions.
- **AC-2.4** Given a transit user who is only the goods owner, then the router explains the carrier/forwarder declares (E1) and offers the transit pack.
- **AC-2.5** Every regime label uses the code from DEC-9 (unit test over all 10 codes).

### Y3 Pre-purchase landed cost — P0 (G1, G7)
- **AC-3.1** Given a supplier quote, code, quantity, origin status and freight, when the user taps "hisoblash", then duty, 300¹, excise, VAT, fee, total appear with source + date per official row and "≈ Taxmin" on totals (PE-21).
- **AC-3.2** Given origin status "yo'q", then totals with and without a certificate are shown side by side.
- **AC-3.3** Given a missing rate, then `STAVKA_TOPILMADI` and no total.

### Y4 Kargo vs white import comparison — P2 [HYPOTHESIS]
Hypothesis that lead users file their own BYUD rather than use kargo; needs **12–15 interviews** (answers-declarant §8) before investment.
- **AC-4.1** Given the hypothesis is untested, the screen is labelled "taqqoslash — taxminiy" and makes no legal claim about kargo.
- **AC-4.2** Interview plan results are recorded with N ≥ 12 before the feature leaves P2.

### Y5 Origin and preferences — P0
Covers B5, E7, L4, export A6. PE-10, PE-11, R61, R69.
- **AC-5.1** Given Türkiye origin and HS6 853710 with EUR.1 and direct transport, the preference row appears with PQ-65 source and the draft lists the EUR.1 in grafa 44 under code 701 "СПТИМ"; outside the 12 lines "Imtiyoz topilmadi".
- **AC-5.2** Given a certificate obtained ≤ 1 year after release, a BK 366 refund pack is produced (Y40).
- **AC-5.3** No screen suggests routing goods through a third country.

### Y6 E-kontrakt and currency control — P0
Covers B1, L3, export A2, A12, D7. R31, R60.
- **AC-6.1** Given a paid import without an E-kontrakt ID, grafa С item 1 is a blocker.
- **AC-6.2** Given a partner country change, a 10-working-day BYUD amendment clock appears (Nizom cl. 5).
- **AC-6.3** Given an export date, the 180-day proceeds clock plus 45/90-day grace and 5/10/35 % stages appear with ZRU-573 art. 11¹; bank document list shows "bankingizdan oling".

### Y7 Permits, controls and banned goods (go/no-go) — P0 (G5)
Covers B6–B9, F3, export A7–A8, A15, F1–F7, PE-16, PE-17. Vet/phyto food goods are self-filed with permit steps (DEC-13 overrides DEC-3).
- **AC-7.1** Given any code, the go/no-go shows each control (conformity, SES, phyto, vet, licence, Asl Belgisi, IMEI, banned) as "Kerak / Kerak emas / Tekshirilmadi" with source; lists not loaded show "Tekshirilmadi" (flags).
- **AC-7.2** Given a VMQ 658 code, the shipment is red "No-go" and cannot proceed.
- **AC-7.3** Given a required permit, filing is blocked until the user confirms it is entered in Yagona darcha (R63).
- **AC-7.4** Given a vet/phyto good, the plan includes the permit body, Yagona darcha step and VMQ 148 / VMQ 727 times with their flags; if the permit cannot be in Yagona darcha before the 15-day clock ends, the user is warned and Y31 offered as an option.
- **AC-7.5** Conformity: shows "accredited MSO of your choice (VMQ 502)", stage times, no total lead time.

### Y8 Deadline engine (user clocks) — P0 (G6)
Covers G3, export A5, A10, A12, B3, C4, C8, D4, E6, L3. R6–R10, R12, R13, R40, R41, R44–R47, R60.
- **AC-8.1** Given presentation on day D at a post with a verified calendar, the clock shows **"File by" = D + 14** and **"Legal max" = D + 15** (shifted to the post's next working day if non-working — BK 261 part 2), citing BK 261 + VMQ 605 cl. 11 (DEC-17). "By" means **until the end of the post's working hours** on that day (Civil Code art. 148 analogy, [UNVERIFIED] for customs; ed2 takes uploads any time but registration and acceptance depend on the post); the UI never says "24:00 gacha". Worked examples from `deadlines.md` pass: presented 12.11 → 26.11 / 27.11; presented 21.11 (Sat) → 07.12 / 07.12.
- **AC-8.1a** Given the user taps "Nega ikki sana?", in-app help explains: the law counts 15 days "from the day of presentation"; the Customs Code does not say whether that day is day 1; YuklaGo therefore asks you to file by +14 so that either reading is met, while +15 is the legal maximum.
- **AC-8.1b** Given a post whose calendar is unverified (`POST_CALENDAR_VERIFIED=false`), the clock shows **raw D + 14 with no non-working-day shift** (the calendar is what cannot be trusted) **and** a "post taqvimi tasdiqlanmagan" flag (DEC-20, DEC-27).
- **AC-8.1c** Every holiday and post-hours entry in the ops calendar has a source and a date; an entry without both is rejected by the admin tool. The admin tool shows no client documents or personal data, and every change is logged with who and when (DEC-29, §6A). Seed data covers the public holidays in the open window (e.g. 8 December 2026, Constitution Day), each with its decree; the Labour Code article and 2026–2027 transfer decrees are [UNVERIFIED] (`HOLIDAY_ARTICLE_AND_TRANSFERS`).
- **AC-8.1d** The engine implements the 15 clocks of `data/declarant/deadlines.json`; worked examples in `deadlines.md` pass as unit tests.
- **AC-8.2** Given no warehouse term, storage shows "≤ 60 kun (ombor hujjatidan tekshiring)" with no date.
- **AC-8.3** Customs processing times (3 h / 8 h / 1 working day) never appear as a countdown; they appear as "bojxona ishlov muddati".
- **AC-8.4** Given ≤ 2 working days and open blockers, a warning appears (DEADLINE_ESCALATION_2WD) naming the 3 BHM fine (MJtK 227¹⁰ part 2); the "≤ 2 working days" threshold is labelled [PRACTICE].
- **AC-8.5** Hub/home shows all live clocks for all shipments, each with its article.

### Y9 Document reading — P0
Covers B2–B4, B10. LLM extraction only after PII masking (Y32).
- **AC-9.1** Given an invoice image, the 12 fields are extracted with per-field confidence; fields < threshold are marked for user check.
- **AC-9.2** Given masking fails, nothing is sent to the AI provider and the user sees "qo'lda kiriting".
- **AC-9.3** Passport/ID images are never stored (deleted after masking).

### Y10 TIF TN classification and advance ruling — P0
Covers C1, C3, export A3.
- **AC-10.1** Suggestions are only codes in `tiftn_codes_pq181_annex1.csv`; each with official text (e.g. 8539520009 "boshqalar" under 8539 52).
- **AC-10.2** Given confidence below threshold, clarifying questions appear; if unresolved, an advance-ruling pack (75 % BHM, BK 369–372) is offered.
- **AC-10.3** The user confirms the code; the model never auto-confirms.

### Y11 Deterministic payment engine — P0 (G1, G7)
Implements §3A PE-1–PE-22 and config flags.
- **AC-11.1** All PE AC pass in CI.
- **AC-11.2** "310 000" fee never appears; fee for a <10,000 USD BYUD = 440,000, pre-arrival = 352,000.
- **AC-11.3** Every result stores rule_set_version, tariff_edition_date, fx_date, BHM value/date and active flags.
- **AC-11.4** Gold case (PE-22) reproduced before any "tasdiqlangan" label; until then demo Set A is labelled "namuna", never "verified".
- **AC-11.5** The engine never writes the valuation method into grafa 43; it proposes grafa 44 code 904 "МЕТОД" labelled as our inference (`GRAFA44_904_ENTRY`), since Annex 12 lists 904 but no grafa. Proposed line format: "904 МЕТОД <method number>", e.g. "904 МЕТОД 1" for transaction value (BK 303) — a proposal, UNVERIFIED on live ed2 (when it is mandatory is also unknown); demo answer keys carry no 904 line.

### Y12 Declaration draft builder (IM40 46 grafas, EK10, BQD) — P0 (G2)
- **AC-12.1** The IM40 draft is keyed by the 46 grafa IDs in `data/declarant/grafa-map.json` (R32), × item for 31–47; "48 maydon" never appears.
- **AC-12.1a** Totals hold: grafa 22 = Σ 42; grafa 12 = Σ 45; grafa 5 = number of items (Yo'riqnoma 2773 sub-points 4, 9, 18).
- **AC-12.1b** Grafas 33 (right part), 41, 45 (left subfield) and 47 carry an "ed2 da tekshirilmagan" flag and no demo claim until checked against live ed2 (DEC-21).
- **AC-12.2** Grafa 36 is empty in IM40 and EK10 drafts; if live ed2 shows a 36 field, YuklaGo leaves it empty unless Q-6 shows it is required. Exemptions/privileges on payments appear in 44 as "6XX"; an FTA/Türkiye origin certificate appears in 44 as code 701 "СПТИМ"; a tariff preference is not auto-added as 6XX while `TARIFF_PREF_AS_6XX` is unverified. Grafas 16 and 17 are not filled for IM40; origin is in grafa 34 per item.
- **AC-12.3** Grafa 43 = 0/1 per "own needs"; 45 customs value in contract currency rounded to 2 decimals; 46 statistical value in thousand USD rounded to 3 decimals (2773 cl. 25 sub-points 40–42); 34 = "000" when origin is unknown (and PE-10 surcharge state `KELIB_CHIQISH_NOMA'LUM` applies).
- **AC-12.4** EK10 grafa 43 = 0 (not own production) / 1 (own production); the user answers "Bu tovarni oʻzingiz ishlab chiqarganmisiz?" (2773 cl. 22 sub-point 38). Same box as IM40, different meaning (IM40: own needs); see AC-21.7.
- **AC-12.5** Draft cannot pass to fill while any blocker is open.

### Y13 Review and format-logic pre-check — P0
- **AC-13.1** Given invoice/transport/draft mismatches, conflict cards show both values and sources.
- **AC-13.1a** Tolerances (DEC-18; formulas from `tolerances.json`, Q-19): all weights are rounded to 3 decimals first (2773 sub-points 30 and 33); diff = abs(A − B) for every document pair (invoice ↔ packing list ↔ CMR ↔ Σ grafa 35, or ↔ grafa 38 for net); **T is always computed from D, the declared (invoice) figure**, never from A or B. **Gross:** diff = 0 → pass; ≤ 1 kg → info; ≤ T = max(1 % × D, 20 kg) → warning the user must resolve; beyond → block. **Net:** diff = 0 → pass; ≤ T = max(0.5 % × D, 5 kg) → warning (explicit max, not min; no info tier); beyond → block. An exact hit on T is a warning, not a block ("≤" is inclusive). Checks run per item line and on the shipment total; the worst result wins, so a line error is not hidden by the total. Worked examples from `tolerances.json` pass as unit tests (e.g. gross D = 1344, diff 86, T = 20 → block; net line D = 84, diff 14, T = 5 → block while the total D = 3234, diff 14, T = 16.17 → warning, so the result is block). Packages and supplementary quantities must match exactly, else block. Every such message carries the label "PROPOSAL, not law" (UZ: "Taklif, qonun emas").
- **AC-13.1d** The gross-weight message shows the grafa 35 definition: gross = goods with all packaging needed to keep them unchanged until put into circulation, **excluding containers and other transport equipment** (2773 cl. 25 sub-point 30; export: cl. 22 sub-point 30). Pallets are UNCONFIRMED (`PALLETS_AS_PACKAGING` [UNVERIFIED]): when a gross mismatch fires, the card asks "Brutto ogʻirlikka paddonlar kiritilganmi?" and the user chooses; the app never subtracts pallets on its own.
- **AC-13.1e** Every tolerance warning adds: "Deklaratsiyaga bitta qiymat yoziladi — qaysi hujjatdan olinganini tanlang." A warning never implies customs accepts a difference (VMQ 605 cl. 30; MJtK 227²²).
- **AC-13.1b** An Admin can change tolerance defaults in the admin tool; each change is logged with who and when; the label stays. The admin tool shows no client documents or personal data (DEC-29). Tolerance defaults are not 🔒 DPO flags.
- **AC-13.1c** Demo Set B blocks with 2 errors + 1 warning and Set C with 4 errors (2 root causes) + 1 weight warning, exactly as `answer-key.json`; Set A passes.
- **AC-13.2** Full-draft review is mandatory before live signing (DEC-7); the user must open every section.

### Y14 Cabinet fill (Electron desktop app; extension fallback) — P0 (G3, DEC-23, DEC-28)
- **AC-14.1** Given the desktop app, when the user starts a fill, ed2 (or the mock) opens in YuklaGo's own embedded browser window (top-level, not an iframe) and fields are typed visibly, one by one, in front of the user.
- **AC-14.1a** Given the user cannot install the desktop app, the same fill runs through the MV3 extension in the user's own browser, with the same stops (Y16) and logs (Y15).
- **AC-14.1b** The desktop window shows the real cabinet address (URL bar) and a "YuklaGo toʻldirmoqda" indicator while filling.
- **AC-14.2** Given `ED2_LIVE_AUTOMATION` is not yet on, the live-cabinet path shows "Tayyor — asoschi tasdiqlagach yoqiladi" (ready, enabled when the founder confirms) and offers a printable field-by-field copy guide; demos use the mock.
- **AC-14.3** No "Tez" mode on the live cabinet (DEC-7); "Tez" exists only on the mock.
- **AC-14.4** The client never reads, stores or exports cookies, session tokens, passwords, PINs or key files (code review + permission audit), even though the desktop app hosts the browser window.
- **AC-14.5** Each desktop session uses an isolated browser profile that is cleared when the session closes; no remote-debugging port is open; the embedded window loads only ed2, ed1, cargo.customs.uz and the mock domain.
- **AC-14.6** Given E-IMZO does not work in the Electron app window on the user's OS (`DESKTOP_EIMZO_COMPAT`), the app says so and switches the user to the system browser with the YuklaGo MV3 extension (DEC-23).
- **AC-14.7** Signing in the embedded window is tested in the Q-6 session (by the key holder only, with consent); if it fails, signing falls back to the system browser with the YuklaGo MV3 extension (DEC-23) (`DESKTOP_EIMZO_SIGNING`).
- **AC-14.8** Build-phase acceptance test (DEC-28): in the Electron app on Windows (first) and macOS (next), a test key holder logs in to the mock and to ed2 with E-IMZO (PFX, USB-TOKEN, BAIK-TOKEN) and the signing dialog opens in the app window; release on an OS is blocked until this passes or the fallback in AC-14.6 is in place.

### Y15 Visible, pausable, logged automation — P0
- **AC-15.1** Pause/stop is always visible and stops within one field.
- **AC-15.2** Every filled value is logged with source and time; logs exclude secrets.

### Y16 Hard stop at login, signature, sending and paying — P0
- **AC-16.1** Given the fill reaches login/sign/send/pay, the automation stops and shows "Endi sizning navbatingiz"; the user signs locally with E-IMZO (key never leaves the device and never passes through YuklaGo).
- **AC-16.2** No code path clicks those controls (test with selector deny-list).
- **AC-16.3** Clicking "save draft" is off by default (AUTOMATION_SAVE_DRAFT_CLICK, CEO decision).

### Y17 Practice (mock) portal — P0
- **AC-17.1** The mock is visibly labelled "Mashq portali — rasmiy emas" on every screen.
- **AC-17.2** All demos and pitch videos use the mock only.
- **AC-17.3** Demo sets A/B/C from `data/declarant/demo-sets/` load with the "SYNTHETIC — do not file" label; example FX rates are labelled "namuna kurs, CBU emas".
- **AC-17.4** Demo totals match `answer-key.json` (e.g. Set A fee 660,000 = 1.5 BHM band for 16,000 USD). Set A is the interim reference case and is labelled **"namuna"**, never "verified" or "tasdiqlangan", until PE-22 is met.
- **AC-17.5** Set C shows its conformity-certificate status as unverified (`SETC_CONFORMITY_CERTS`); no claim either way.

### Y18 Hand-off pack with reason codes — P1
Triggers: v2 list + the 13 Deklarant triggers (answers-declarant §6); the trigger "regime not IM40/EK10" now reads **"regime not yet implemented in Y22, or not verified"** (DEC-13; declarant-v3-check §F). Under DEC-13 triggers produce a **warning and an option**, not a forced stop, except: signer not ready, request for YuklaGo staff to file, banned goods, permit missing past the deadline — these block self-filing.
- **AC-18.1** Each trigger has a reason code stored in the pack.
- **AC-18.2** The pack includes the ed1 list-entry reminder and E-arxiv numbers (VMQ 605 cl. 15).
- **AC-18.3** The pack can be exported to any broker, not only the partner.

### Y19 Status and message explainer (44-message library) — P0
- **AC-19.1** The library holds the **44** messages from answers-declarant §7 (S01–S11, R01–R15 + R99, D01–D09, M01–M08) with ID, trigger, text, next step, source; each labelled "YuklaGo izohi, rasmiy kod emas".
- **AC-19.2** Given a pasted customs message, the best match and the grafa to fix are shown; no match → "noma'lum xabar" + Y31 option.
- **AC-19.3** Corridor messages use R36 and R11 wording.

### Y20 Product library — P1
- **AC-20.1** Given a repeat product, code/docs/permits prefill and a rate change since last use is flagged (PE-7).
- **AC-20.2** Library changes example for LED lamps shows no invented change (answers-tariff).

### Y21 Export EK10 full path — P1
Covers export A1–A17.
- **AC-21.1** Given an EK10 shipment, the pack contains TED, invoice, contract/E-kontrakt, transport doc, permits, E-arxiv, signer, phyto/vet, origin certificate if needed.
- **AC-21.2** Filing target is cargo.customs.uz (EXPORT_EK10_TARGET); export duty shows "rasmiy stavka topilmadi".
- **AC-21.3** Fruit/veg codes trigger the VMQ 163 checklist; unfair-exporter register warning shown.
- **AC-21.5** The EK10 draft is keyed by the **45** grafa IDs in `data/declarant/grafa-map-ek10.json` (2773 cl. 21 list; fill rules cl. 22), not the IM40 list: only in EK10 — 17, 17a; only in IM40 — 15, 15a, 21; not filled — 4, 6, 10, 15, 15a, 16, 21, 27, 36, 51–53. (Closes the former [PENDING: Deklarant], Q-19.)
- **AC-21.6** The EK10 draft applies the 15 changed grafas from `grafa-map-ek10.json` `diff_vs_im40`: 1 (ЭК, regime 10); 2 = the **Uzbek** exporter with status code and TIN/PINFL + district (these sit in grafa 8 for IM40); 8 = the **foreign** consignee, name, country and address only; 18 adds gross-in-vehicle, vehicle type, VIN, end-of-carriage country, carrier and driver; 20 adds a third subfield (settlement-form + dispatch-form codes); 25 = planned border-crossing vehicle type; 29 = planned exit post; 31 = lines 1–5 with the **producer** TIN/district bottom-left; 37 starts with 10; 40 refers only to a previous GTD (empty for own production, our reading); 43 (AC-12.4); 44 uses 702 "СПТЭК" for the origin certificate and 419 "ФТСС" for phyto, no 904 proposed; 45 follows BK 315–317 for exported goods (our pointer); 47 has no import codes 20/21/27/29 (export duty 25 / export excise 28 only where rates exist); C has line 1 only. ⚠️ items carry `EK10_GRAFA_LIVE_CHECKS` and no demo claim.
- **AC-21.7** EK10 grafa 43: "1" = the exporter is the manufacturer of the goods, "0" = not (2773 cl. 22 sub-point 38); the rule names the consignor (грузоотправитель), so when consignor ≠ exporter the screen shows "tekshirilmagan" (`EK10_GRAFA_LIVE_CHECKS`).
- **AC-21.4** After release, the VAT-0 % proof checklist and the 180-day proceeds clock appear.

### Y22 Special regimes: 11, 12, 41, 42, 51, 61, 80 — P1
Covers export B1–B5, C1–C8, D1–D7, E1–E8.
- **AC-22.1** Each regime has its own document template, conditions checklist and clocks (R44–R47).
- **AC-22.2** Regime 42 partial relief computes 5 % per month of duties/taxes (BK 66); full relief list not auto-applied.
- **AC-22.3** Processing yield norms come only from user documents; the LLM never proposes a norm.
- **AC-22.4** Transit clock from mode + distance (BK 120); TIR/ATA explainers shown; "NCTS" never shown.
- **AC-22.5** Live filing targets for these regimes stay off until PC-1/PC-7 clear; the user receives a field-by-field guide.

### Y23 Post-release control and audit support — P1
- **AC-23.1** Given an audit notice, an index of all documents and calculation traces per BYUD is produced.

### Y24 XML pack — P2 (Appendix A PC-3)
- **AC-24.1** With XML_EXPORT=off, no XML file is offered; the UI says "rasmiy sxema tasdiqlanmagan".

### Y25 Accounting hand-off — P2
- **AC-25.1** Given release, a CSV with landed cost per item and all payment lines is exported.

### Y26 Corridor and letter-of-credit packs — P2
- **AC-26.1** Given a red corridor, the Y36 inspection pack is linked.

### Y27 Multi-line invoices (DEC-1) — P0
- **AC-27.1** Given 12 invoice lines, lines are grouped into BYUD items by code; Σ item values = invoice total.
- **AC-27.2** Freight/insurance allocation method shown (FREIGHT_ALLOCATION_METHOD).
- **AC-27.3** One fee per BYUD regardless of item count.

### Y28 Payment preparation and treasury — P0
Covers E5, L6.
- **AC-28.1** Shows amount due, payment purpose and the user's own steps; YuklaGo never initiates payment.
- **AC-28.2** Given "payment not visible", a troubleshooting list (advance, account, date) is shown.

### Y29 E-arxiv step — P0
- **AC-29.1** For each required document, the user records the E-arxiv number; grafa 44 lists them.

### Y30 Preliminary declaration path — P1
- **AC-30.1** Given goods not arrived, the pre-arrival path is offered with fee 352,000 for a <10,000 USD BYUD and the 30-day lapse clock (BK 262).

### Y31 Partner broker (optional fallback) — P1 (DEC-2)
- **AC-31.1** Offered as an option on every hand-off trigger; never the default path.
- **AC-31.2** The partner is a notified broker (ZRU-701 annex 3 pos. 35) under its own contract with the user; YuklaGo staff never sign.
- **AC-31.3** The user sees who receives which data before sharing.

### Y32 Consent and data protection — P0 (DEC-6, DEC-15)
- **AC-32.1** Before the first upload, an **unticked** consent box explains: data processed by Google Gemini in the EU (DE/NL), PII masked on a UZ server first, masked outputs kept 30 days, no passport/ID images stored; upload is disabled until ticked.
- **AC-32.2** Consent is stored with version and time (ZRU-547 art. 21).
- **AC-32.3** Masking failure → nothing sent (fail-closed).
- **AC-32.4** Breach runbook: 24 h notice, 72 h details (VMQ 415 / ZRU-764 art. 16 [UNVERIFIED applicability]).

### Y33 Corrections — P1
Covers I1–I4.
- **AC-33.1** Before acceptance: withdraw/change guide. After acceptance: 1-working-day typo clock (codes/numbers excluded). During clearance: change with 25 % BHM fee if on declarant request. Post-release: 3-year correction pack (BK 266).

### Y34 Post-release download and records — P1
Covers K2, L2.
- **AC-34.1** Given release, a 15-day download reminder (VMQ 605 cl. 37).
- **AC-34.2** All files and traces retained with version stamps.

### Y35 Valuation module (methods, related party, BQD, value control) — P1
Covers D1, D5, D7, PE-1, PE-2.
- **AC-35.1** Given related party = yes without evidence, draft is blocked on value.
- **AC-35.2** Given a valuation query from customs, a response pack lists requested evidence and the conditional-release-with-security option.
- **AC-35.3** Methods 2–6 require comparable/evidence inputs from the user; the LLM never supplies comparable prices.

### Y36 Inspections and customs requests — P1
Covers H2–H4, G4, D7.
- **AC-36.1** Given a red corridor, the prep checklist (attendance, access, 25 % BHM/hour fee) is shown.
- **AC-36.2** Given a document request, upload-to-E-arxiv steps and the response tracker appear.
- **AC-36.3** Given sampling, the sample act checklist and result tracker appear.

### Y37 Appeals and administrative cases — P1
Covers J1, J2.
- **AC-37.1** Given a decision date, a 30-day clock (BK 409-2) and a draft complaint (409-3 fields) are produced for the user to file and sign.
- **AC-37.2** Given an offence protocol, the article and fine range are explained and the user is advised to get legal help; YuklaGo does not represent.

### Y38 Arrival, storage and damage events — P1
Covers G1, G2, G4, G5, K3.
- **AC-38.1** Arrival date entered → R6/R9 clocks start.
- **AC-38.2** Damage/broken seal → notification checklist and photo log.

### Y39 Guarantees, deferral and instalments — P1
Covers E6, export C6, E4, D7.
- **AC-39.1** Eligibility checklist (BK 329–333) and security methods (BK 339–346); guarantee size entered by the user, not computed.

### Y40 Refunds — P1
Covers E8, L4, export B4.
- **AC-40.1** Refund packs with the applicable clock (BK 335, 353–357, 366, 35).

### Y41 Client profile, customs history and debt — P1
Covers A1, A5, L6.
- **AC-41.1** User-entered ed1 reconciliation figures shown with source "ed1 (siz kiritdingiz)"; no cabinet scraping (CABINET_STATUS_READ=off).

### Y42 Uzbek text normalisation — P0 (DEC-22)
- **AC-42.1** All stored and displayed Uzbek copy uses U+02BB in oʻ, gʻ, Oʻ, Gʻ; the tutuq belgisi is U+02BC.
- **AC-42.2** Given a user types o/O/g/G followed by `'` (U+0027), `‘` (U+2018), `’` (U+2019), `ʼ` (U+02BC) or a backtick, the input replaces it with U+02BB (regex `/([oOgG])['\u2018\u2019\u02BC`]/g → "$1\u02BB"`).
- **AC-42.3** Search folds all variants to U+02BB (searching "o'yinchoq" finds "oʻyinchoq").
- **AC-42.4** IBM Plex Sans is never loaded; UI font is Onest.

### Y43 Account security and YuklaGo staff access — P0 (DEC-29)
Implements §6A and `team-review/roles-rbac.md`. One client role (Owner); YuklaGo Support and Admin are staff roles.
- **AC-43.1** (Hakathon CEO, 19.11) Step-up SMS has **exactly five triggers**: sign-in from a new device, a signer change, granting Support access, a full data export, and account deletion. There is **no** SMS step-up for payment or signing: the bank and the ERI already authenticate those. Step-up sheets are not counted in the brief's action targets.
- **AC-43.2** Given a sign-in from a new device, the Owner gets an immediate notice with a one-tap "Sessiyani tugatish" (SoD rule 7); the event is in the security log.
- **AC-43.3** Support access opens only when the Owner grants it in Settings: the Owner sees the reason, sets the duration (default `SUPPORT_ACCESS_DEFAULT_HOURS` = 24), and can revoke at any time; access closes automatically at expiry. No staff member can grant access to themselves (SoD rule 4; ZRU-547 art. 28).
- **AC-43.4** During an active grant, Support sees documents and the draft **masked** (no full name, PINFL, passport or phone); it may leave comments or suggestions only. It has no edit, export, sign, submit or pay control, in the UI or the API (deny-list test, as AC-16.2). Support never signs, never sends, never joins a client's TIF participants (ed1) list as a trusted person or specialist, and never logs in to a client's cabinet in the client's name (`roles-legal.md` B3 red lines; BK 15, 277; ZRU-701; ZRU-793 art. 27).
- **AC-43.5** The Admin tool covers tariffs, the calendar, tolerances and flags only, with no route to client documents, drafts or personal data (API permission test). Admin reads only the configuration log.
- **AC-43.6** Support and Admin are separate staff accounts, never both on one person, with mandatory 2FA (SoD rule 3).
- **AC-43.7** A flag marked 🔒 DPO in §3A.1 changes only after a second approval by the DPO (PC-15); the attempt, both approvers and the time are logged (SoD rule 5).
- **AC-43.8** The audit log records who (Owner / YuklaGo / Support / Admin), when, from which device, and what (field, value hash, source, read-back result), plus consent grants and revocations, Support sessions, config and flag changes, exports and sign-ins. It never records passwords, PINs, keys, or login and signing windows. It is append-only and hash-chained; exports show the last hash. The Owner reads and exports their own log as PDF/CSV; Support reads only its own session; Admin only the config log; the DPO reads logs when an incident occurs.
- **AC-43.9** Full field values stay on the device; only value hashes go to the server (engineering.md). The server log is stored in Uzbekistan and kept for `AUDIT_LOG_RETENTION_YEARS` (3, proposal, not law). Uploading session values stays open (automation.md Q7; Q-5).
- **AC-43.10** (Q-20) Given several accounts in one company, every audit-log entry names the person (account holder) who did it, not just "the company"; the Owner view lists the company's entries by person, so who filled, confirmed, exported or signed is visible. Each account's step-up and new-device notices (AC-43.1, AC-43.2) go to that account's own phone.
- **AC-43.11** Support and Admin never upload client documents to AI tools outside YuklaGo's own processing (e.g. a personal chatbot); doing so risks MJtK 46-2 part 2 (50–100 BHM) (`roles-legal.md` B3). If Support passes a document to a third party, the data subject is notified in writing within 3 days (ZRU-547 art. 23 part 2, per Huquq).

---
## 6. Legal and security constraints

### 6.1 Automation of the live ed2 cabinet — founder's switch (Appendix A PC-1)
- No law found that bans or permits user-supervised automation of ed2; no public filing API found ("We found no public filing API"). Huquq (answers-legal Q-A): **conditional approval, grey zone** — acceptable only if the user logs in and signs with their own key, every field is visible, nothing is hidden, no protection is bypassed, and the resource owner's rules (560-II art. 12) are respected. Risks if done wrongly: JK 278-2–278-4, MJtK 155-1 (R58).
- `ED2_LIVE_AUTOMATION` is **ready, enabled when the founder confirms** (DEC-24). The founder talks to the officials himself; the formal letter is not sent. Until the flag is on, demos, pitch and training use the mock portal (Y17) and the live path gives a field-by-field copy guide. The legal position above does not change when the flag is switched; the conditions (own login, own key, visible fill, nothing hidden or bypassed) apply in every mode.
- No claim of a state partnership, approval, integration, or "API".

### 6.2 Broker-activity boundary — open (Appendix A PC-2)
- Huquq (answers-legal Q-B): YuklaGo is **not** a broker while it is software the declarant uses and the declarant (or its own staff) signs; it **becomes** broker activity (notification, VMQ 847 conditions, 20 BHM fine for unnotified activity — R38) if YuklaGo staff sign, are listed in a client's declaring-persons list, or act in the client's name.
- Rules: YuklaGo staff never sign or file; never in a client's ed1 list; no "we clear it for you" service; the partner broker (Y31) contracts directly with the user.

### 6.3 Personal data and AI (DEC-15)
- Provider: Google Gemini via Google Cloud EU (DE/NL); fallback AWS / Microsoft EU. Germany and the Netherlands are on the VMQ 415 list (R42) [re-check list]. Google Cloud DPA review: **[PENDING: Huquq]**.
- Hosting in Uzbekistan; PII masked on the UZ server before any AI call; fail-closed if masking fails; masked outputs kept 30 days; no passport/ID images stored; explicit unticked consent before first upload (Y32); breach notice 24 h / 72 h (VMQ 415; ZRU-764 art. 16 [applicability UNVERIFIED]).
- MJtK 46-2 risk: part 1 still has the old localisation wording (practice risk); part 2 fines unlawful AI processing of personal data (50–100 BHM). Mitigation: consent, masking, processing only for the stated purpose.

### 6.4 Liability and offer
- YuklaGo does not guarantee customs amounts; limitation clauses must respect CC 332–333 and Consumer law 221-I (R50). Offer text needs a lawyer's review **[PENDING: Huquq]**.

### 6.5 Security
- ERI keys, PINs, passwords, cookies: never read, stored or used (R57; Y14, Y16).
- Desktop app (DEC-23, Electron per DEC-28): ed2 opens in a top-level embedded window (X-Frame-Options applies only to framing, so it does not block this). Because the app hosts the whole page, users must trust it (automation.md): code signing, auto-update, isolated per-session profile cleared on close, domain allow-list (ed2, ed1, cargo.customs.uz, mock), no remote-debugging port, no cookie/token access by YuklaGo code (AC-14.4–14.5). Embedded-browser automation can be detected by the site (automation.md); no bypass is attempted (R58).
- Extension fallback: host permissions limited to the same domains; until `ED2_LIVE_AUTOMATION` is on, the mock domain only.
- Audit log: every filled value with source and time; logs exclude secrets; append-only and hash-chained; full values stored on the device, hashes on the UZ server, retention `AUDIT_LOG_RETENTION_YEARS` = 3 (proposal, not law); uploading session values only with consent (automation.md Q7 — open, Q-5). Actors and read rights: §6A, AC-43.8.

---

## 6A. Roles, permissions and audit (DEC-29)

Source: `team-review/roles-rbac.md` (security, 2026-11-19, Uzbek, not legal advice). This section summarises it. The file wins on detail, and its lex.uz citations were read by the security agent, not re-read by PM.

**Roles (exactly three).**
1. **User / Owner**: the single client role, and the client account user is the signer (DEC-29; Y1 AC-1.7–AC-1.10). In Phase 1 every account holder is a signer; a non-signer such as an accountant gets the audit pack, not a login (AC-1.14). A company may have several such accounts; all have the same role and identical rights, each with its own login, ed1 entry and ERI, no shared logins, and the audit log names the person (Q-20 closed; AC-1.12, AC-1.13, AC-43.10). Uploads and prepares documents, confirms the code and payments, pays in their own bank (Y28), signs and sends in ed2 with their own ERI (Y16). Gives or withdraws AI consent and Support access, and reads their own audit log. Progressive disclosure replaces role screens (§9 D-17).
2. **YuklaGo Support**: enters only with the Owner's consent, through a time-limited session. Sees masked data only, and every action is logged.
3. **YuklaGo Admin**: tariffs, the calendar, configuration and feature flags (AC-8.1c, AC-13.1b). No access to client documents.

**Permission matrix** (`roles-rbac.md` §2).

| Action | Owner | Support | Admin |
|---|---|---|---|
| View documents and draft | ✓ | Only during an active consent, **masked** | ✕ |
| View unmasked personal data (name, PINFL, passport, phone) | ✓ | ✕ | ✕ |
| Edit / prepare | ✓ | ✕ (comments or suggestions only) | ✕ |
| Sign / send (ed2) | ✓ — in ed2 only, local E-IMZO | ✕ | ✕ |
| Pay | ✓ — own bank | ✕ | ✕ |
| Export (audit pack, PDF/CSV, own log) | ✓ — full data export with step-up | ✕ (no unmasked export) | ✕ |
| Configuration (tariffs, calendar, tolerances, flags) | ✕ (own account settings only) | ✕ | ✓ — logged |
| Give / withdraw AI consent | ✓ | ✕ | ✕ |
| Grant / revoke Support access | ✓ | ✕ | ✕ |
| Read audit log | ✓ — own | Own session only | Config log only |

**Signer check** (`roles-rbac.md` §3; `roles-legal.md` B1; VMQ 605 cl. 2, 15 stage 2, 28): the signer is the director (or YaTT) or a staff specialist listed in ed1 (confirmed by the Hakathon CEO). The user confirms the ed1 entry and authority period themselves (YuklaGo does not read ed1). A staff specialist is warned that the director must first add them in ed1 with the director's own ERI, and nobody signs with someone else's key (AC-1.7a). If the check fails, Y14/Y16 are locked with "imzolovchi roʻyxatda emas" (AC-1.2). A new certificate is auto-detected from its public fields and triggers one confirm; a mismatch warns, it does not block (AC-1.9, AC-1.15–AC-1.21). Authority expiry is user-confirmed (AC-1.10).

**Separation-of-duties rules** (`roles-rbac.md` §4).
1. Staff never sign, send or pay, are never in a client's ed1 (TIF participants) list as a trusted person or specialist, and never log in to a client's cabinet in the client's name (R38, AC-1.4, AC-43.4; `roles-legal.md` B3). Otherwise it becomes broker activity (BK 15, 277; unnotified broker activity: 20 BHM, ZRU-701).
2. The ERI stays on the Owner's device only: the key, PIN and password are never read or stored (ZRU-793 art. 27).
3. Support and Admin are separate staff accounts, never held by one person, with mandatory 2FA (AC-43.6).
4. No one can grant Support access to themselves. Access opens only with the Owner's consent, which states a reason, has a duration (default 24 h, `SUPPORT_ACCESS_DEFAULT_HOURS`) that closes automatically, and can be revoked by the Owner at any time (ZRU-547 art. 28; AC-43.3).
5. Admin cannot alone enable a flag that exposes client data. Such flags need two approvers, one of them the responsible person (the DPO, PC-15), and the change is logged (ZRU-547 art. 27, 31; §3A.1 🔒 DPO; AC-43.7).
6. Step-up for the Owner: a fresh SMS code for exactly five triggers — new device, signer change, Support access, full data export, account deletion; no SMS for payment or signing, which the bank and the ERI already authenticate (Hakathon CEO, 19.11; supersedes `roles-rbac.md` rule 6) (AC-43.1).
7. A sign-in from a new device notifies the Owner immediately, with an option to end the session (AC-43.2).
8. Single-role risk: a stolen account gives full control, and rules 6–7 reduce that risk.

**Audit rules** (`roles-rbac.md` §5; AC-43.8–AC-43.9): who (the named person), when, from which device and what is logged; secrets are never logged; append-only, hash-chained; full values on the device, hashes on the server; server log in Uzbekistan for `AUDIT_LOG_RETENTION_YEARS` = 3 (proposal, not law; ZRU-764 art. 16 applicability [UNVERIFIED]); the Owner exports PDF/CSV.

**Legal notes from Huquq** (`roles-legal.md` B2–B3): no norm forbids one person preparing, paying and signing (internal-control risk, not a legal requirement); the declarant is primarily liable (BK 276) and the signing person may be personally liable (MJtK 227-22; whether an employee counts as an official is not clear). Support and Admin are persons inside the operator, not third parties (Huquq's own reading). Access only per a specific request; masking implements ZRU-547 art. 19 and 27; a word-for-word duty to log every access was not found in ZRU-547 (the Ministry of Justice model procedures were not read — [UNVERIFIED]).

**How each gap in `roles-rbac.md` §6 is handled.**

| # | Gap | Handling |
|---|---|---|
| 1 | No roles section | Added: this §6A (the file suggested §6.5; a dedicated section is used instead and §6.5 links here). |
| 2 | No AC for the Support access flow | Added: AC-43.3, AC-43.4. |
| 3 | Admin "no client data" boundary and two-person flag approval missing | Added: AC-8.1c, AC-13.1b, AC-43.5, AC-43.7; 🔒 DPO marks in §3A.1. |
| 4 | Step-up and new-device notice missing | Added: AC-43.1, AC-43.2. |
| 5 | No re-check on certificate change or ed1 expiry | Added: AC-1.9, AC-1.10. Q-21 closed: auto-detect on (`CERT_PUBLIC_FIELDS_AUTODETECT=true`), one confirm per new certificate, mismatch warns (AC-1.9, AC-1.15–AC-1.21); falls back to the one-time confirm until the E-IMZO domain key exists (PC-16). |
| 6 | Signer who is not the Owner (staff specialist) | CEO decision (DEC-29): the account user is the signer, so the specialist holds the account (AC-1.7, AC-1.8). A company with more than one signer: several accounts, same single role, own login/ed1 entry/ERI each, no shared logins, actions logged per person (Q-20 closed by the CEO; AC-1.12, AC-1.13, AC-43.10). |
| 7 | No responsible person under ZRU-547 art. 31 | Added: a named responsible person (ZRU-547 art. 31, last part; one employee is enough; "DPO" title not required) as an org requirement before launch (PC-15), owner Hakathon CEO. |
| 8 | Audit-log upload and retention open | Retention set: `AUDIT_LOG_RETENTION_YEARS` = 3 (proposal). Upload of session values stays open (Q-5, CEO + Huquq). |
| 9 | Trusted person ("ишонч билдирган шахс") as signer | Stays off and [UNVERIFIED] (AC-1.11, PC-5, `TRUSTED_PERSON_CAN_SIGN=false`), owner Huquq. |

---

## 7. Automation design

| Step | Automated by YuklaGo | User |
|---|---|---|
| Read documents, extract fields | Yes (masked AI + user check) | Confirms low-confidence fields |
| Suggest code | Yes (official list only) | Chooses the code |
| Payments | Yes (deterministic engine) | Reviews; pays from own account |
| Draft (46 grafas, BQD) | Yes | Full review (mandatory before live signing) |
| Login to ed2 / cargo.customs.uz | **No** — the app opens the login page and waits | Logs in with E-IMZO, locally |
| Fill fields | Yes, in the desktop app's embedded window (extension as fallback), visibly, field by field; pausable; logged; live cabinet once `ED2_LIVE_AUTOMATION` is on | Watches; can pause or edit |
| Save draft click | Off by default (CEO decision) | Clicks |
| Sign, send, pay | **No — hard stop** ("Endi sizning navbatingiz") | Signs, sends, pays |
| Status, messages | Explains what the user pastes or enters | Enters reg. number/status |

**Client architecture (DEC-23, DEC-28).** Main filing client: **desktop app built on Electron (DEC-28: same bundled Chromium on every OS, so ed2 and E-IMZO behave predictably; Windows first, macOS next)** that opens the cabinet in its own embedded browser window — a top-level window, not an iframe, so ed2's X-Frame-Options does not apply. Two panes: cabinet window + YuklaGo rail. It fills automatically in front of the user and stops at ERI/E-IMZO, which the user signs locally. **Fallback:** the MV3 extension (side panel next to the user's own tab) for users who cannot install the app, and for signing if E-IMZO fails in the app window — the user falls back to the system browser with the YuklaGo MV3 extension (DEC-23). Server-side automation stays ruled out (the token is on the user's PC). Note: automation.md recommended the extension first and marks E-IMZO compatibility in embedded Chromium/WebView as unknown (❓); the only tested build so far is the extension on the mock — see `DESKTOP_EIMZO_COMPAT`, `DESKTOP_EIMZO_SIGNING` and the build-phase acceptance test AC-14.8.
**Fill modes.** Qadam-baqadam / Oddiy on live; Tez on mock only (DEC-7). Field count dynamic per item count. Interrupt trigger = a real click or keypress in the cabinet.
**Read-back.** After each field the value is read back and normalised; mismatch → stop that field.

---

## 8. Mobile and platform scope (mobile.md; DEC-23)

| On mobile (PWA) | Desktop app (filing) / large web |
|---|---|
| Document capture (camera, multi-page); never photograph ERI/tokens | Cabinet fill (Y14–Y16) in the desktop app's embedded window (Electron; extension fallback), pause, logs |
| Landed cost (Y3) | Wide tables (47-grafa payments, draft, library table view, security log) |
| Status/message explainer (Y19) | ERI login/sign (USB token) |
| Clocks (Y8) and notifications (PWA Web Push; Telegram/SMS optional — CEO question) | Two-pane fill session (≥ 1024 px) |
| Product library cards (Y20) | |
| "Send to computer" link for ERI steps | |

- **AC-M1** Given a phone, no screen offers signing, key upload or password entry.
- **AC-M2** Given a phone user on a filing step, the "Kompyuterga yuborish" link is the only action.
- **AC-M3** Tap targets ≥ 48 px (`space.tapMin`).
- **AC-M4** Given a web or phone user on a filing step, the app offers "YuklaGo ilovasini oching" (desktop app) and, if they cannot install it, the extension fallback.
- Platforms: web workspace (all non-filing work), Electron desktop app (DEC-28: Windows first, macOS next), extension fallback, mobile PWA. One backend.
- Open (mobile.md §4): tab set, offline capture, Telegram reminders — owner CEO.

---

## 9. Design direction notes (no visual redraw; what must change)

**Brand (DEC-11, DEC-22).** Final source of truth: `/workspace/yuklago-brand/final/` — `brand-guidelines.md`, `brand-sheet.png`, `logo/` (svg, png, favicon, app-icon), `tokens/` (`brand-tokens.json`, `tokens.css`, `tailwind.v4.css`, `tailwind.config.snippet.js`, `contrast-report.md`), `mock-mode-specimen.png`, `type-specimen.png`. Ignore `/workspace/yuklago-brand/export/`.

**Tokens (from `final/tokens/brand-tokens.json` and `team-review/ui-tokens.json` v0.2-ui; ui-tokens wins for UI work where they differ).**

| Token | Value | Use / rule |
|---|---|---|
| brand.primary / hover / pressed | `#2E2BA0` / `#24218A` / `#1C1A70` | Primary buttons, links, focus ring |
| brand.onPrimary | `#FFFFFF` | 10.66:1 on primary |
| brand.tint / dark | `#ECEBFA` / `#14143F` | Tint backgrounds; no muted text on tint |
| brand.accent (saffron) | `#F5B43C` | Logo fold and "Endi sizning navbatingiz" panel only; never text, icons, links or button fill |
| text.ink / secondary / muted | `#14152B` / `#525570` / `#5E6178` | Muted never on sunken or tint (fails AA) |
| bg.canvas / surface / sunken / inverse | `#F5F5FA` / `#FFFFFF` / `#EEEFF5` / `#14152B` | |
| border.line / strong / input | `#E1E2EC` / `#C5CCD8` / `#84899A` | Input outline approved |
| button.destructive | `#C0362C` | No black, pink, petrol or saffron-filled buttons |
| status go / caution / stop / info (fg) | `#12795A` / `#A35C00` / `#C0362C` / `#2457A6` | Always icon + word: Tasdiqlangan / Diqqat / Toʻsiq / Maʼlumot |
| yourTurn bg / accent | `#14152B` / `#F5B43C` | ERI login/sign moment only |
| practice banner bg / border / text / pill | `#E8EBF1` / `#C5CCD8` / `#14152B` / `#3A4256` + white | Mock mode only |
| font.ui | Onest, 'Noto Sans', system-ui | Never IBM Plex Sans |
| font.code | JetBrains Mono | TIF TN codes, grafa IDs, URLs only; money never mono |
| scale | display 36/40, h1 28/34, h2 20/28, h3 16/24, body 16/24, caption 13/20, amount 14/20 tabular-nums | |
| space | unit 8; 4, 8, 12, 16, 24, 32, 48, 64; tapMin 48 | |
| radius | 4, 6, 10, 14, 20, pill | |

**Product rules from the designer (DEC-22).**
1. oʻ/gʻ stored as U+02BB; typed apostrophes after o/g auto-replaced; search folds variants (Y42, AC-42.1–42.4).
2. Practice mode: one neutral graphite banner, pinned, not dismissible — UZ pill "MASHQ", "Mashq rejimi — bu haqiqiy bojxona kabineti emas. Hech narsa bojxonaga yuborilmaydi." link "Haqiqiy rejim haqida"; RU pill "УЧЕБНЫЙ РЕЖИМ", "Это не настоящий кабинет таможни. Ничего не отправляется." link "О реальном режиме"; pill also in the mock URL bar; optional 3 px graphite top rule and horizontal 4 % watermark; domain `mashq.yuklago.uz`. **Never** magenta/pink, hazard yellow, diagonal hatching or watermark, or brand/status colours for practice. **AC-D1** Given mock mode, the banner is present on every screen and no magenta/pink/hazard element exists (visual snapshot); given real mode, none of the practice elements appear.

**UI fixes (uiux.md, research-pitch.md, product.md, declarant).**
- D-1 Remove "Rasmiy" chips from sample numbers; "Rasmiy" only on PE-21 rows with source + date (G1).
- D-2 Replace "310 000" fee with the VMQ 55 band value (440,000 for <10,000 USD; 352,000 pre-arrival).
- D-3 Wire the clocks into hub/home with the article and "File by / Legal max" (G6, DEC-17).
- D-4 Replace "48 maydon" with the 46-grafa draft keyed by grafa ID (DEC-16).
- D-5 Remove all `[N]`, `[v2 spec]`, `[asos]`, `xxxx` placeholders; unverified items say "hozircha koʻrsatmaymiz".
- D-6 Merge split boards (04+05, 10+11, 15+16, 17+18).
- D-7 ERI hand-off note sits in the rail, never behind a modal; no password/key field on any YuklaGo surface.
- D-8 Remove "Prototip: jonli toʻldirishni koʻrsatish" from product UI; make the mock's "Imzolash va yuborish" inert during fill.
- D-9 Payment tables: tabular numerals, separated "Jami", source chip per row; "≈ Taxmin" on totals.
- D-10 Empty/loading/error states for home, upload, SMS login, broker link, library.
- D-11 Settings: "ERI va kabinet" screen; "Ilova: versiya · ruxsat etilgan saytlar" (desktop app) and "Kengaytma: versiya · ruxsatlar" (fallback).
- D-12 Filing-target screen says "YuklaGo ilovasida, kabinet oynasi ichida" (desktop app) with "Ilovani oʻrnata olmaysizmi? Kengaytma orqali" as the fallback; real mode shows "Tayyor — asoschi tasdiqlagach yoqiladi" until the flag is on. Keep the board's viewport + rail pattern (it matches the desktop app).
- D-13 Tolerance messages carry "Taklif, qonun emas" (DEC-18).
- D-14 Landing: public line "Brokersiz, oʻzingiz topshirasiz — tez va tushunarli" (DEC-25); the two banned phrases never appear; no official-integration claim; source and date visible on numbers.
- D-15 Motion 120–180 ms with `prefers-reduced-motion`; re-check Russian line lengths.
- D-16 One design system (Varaq) for web, PWA, desktop app and extension panel; retire petrol `#0B5563` and the green PWA theme.
- D-17 (DEC-29) One client role: no team, members, invite, role-picker or approval screens on any surface. Advanced detail sits behind progressive disclosure (the "(i)" sheet, the expert view toggle, the audit pack), not behind roles.
- D-18 (DEC-29) Settings → "Xavfsizlik" gets a "Yordam xizmatiga kirish" sheet with the reason, the duration (24 h default), revoke, and a masked-view note. The session-log action "Yordam xizmatiga ulashish…" opens this consent sheet; it never shares data in one tap. Security log rows name the actor (Siz / YuklaGo / Yordam xizmati / Admin).
- D-19 (DEC-29) Step-up SMS sheet for exactly five triggers: new device, signer change, Support access, full data export, account deletion (no SMS for payment or signing; AC-43.1). The new-device notice has a "Sessiyani tugatish" action. Set-up ends with "Siz imzolaysiz" (no role picker), shows the staff-specialist warning and the own-key line (AC-1.7, AC-1.7a), and asks for the ed1 authority end date (AC-1.10).
- D-20 (Q-19) Weight mismatch card: shows both values, the threshold and "Taklif, qonun emas", plus the pallet question. Pallets are never auto-subtracted (AC-13.1a, AC-13.1d). Full check of the v0.4 simplification brief: `pm/simplify-brief-v0.4-check.md`.
- D-21 (Phase 1) No account type, invite or login for non-signers. Where an accountant needs data, the Owner downloads the audit pack / export (step-up SMS) and shares it outside the app (AC-1.14).
- D-22 (Q-21) New-certificate card: "Imzolovchi oʻzgardi. Yangi imzolovchi ed1 roʻyxatiga kiritilganmi?" with "Ha" / "Yoʻq". A warning, not a block, until the user answers "Yoʻq" (AC-1.18).
- D-23 (`roles-legal.md` B4) **Must stay visible.** Each item is one short line or chip, shown on screen and not hidden behind (i) (ZRU-776 art. 16 risk). These lines do not count toward the 60-word body-copy cap. (1) At code confirm (I2) and review (I10): "Kodni siz tanlaysiz va javob berasiz." (2) Before signing (I12): "Siz oʻzingiz imzolab, oʻzingiz yuborasiz" + "faqat oʻz ERI kalitingiz". (3) The unticked consent with its four facts (≤ 40 words) on its own set-up screen (S6). (4) The "Taklif, qonun emas" and "≈ Taxmin" chips with source date. (5) The deadline: "Topshiring: [sana]" + legal maximum + "post taqvimi tasdiqlanmagan" flag; the article sits behind a tap. (6) "Brokersiz, oʻzingiz topshirasiz." on the landing page and at S4. (7) Signer must be listed: "…roʻyxatiga kiritilgan shaxs" at S5 and in the block state. (8) The MASHQ banner.

---

## 10. Copy rules

1. Public line (DEC-25): **"Brokersiz, oʻzingiz topshirasiz — tez va tushunarli"**. Product scope is full broker replacement.
2. Banned (exact phrases and their apostrophe variants): **"broker oʻrnini bosadi"**, **"rasmiylashtirib beramiz"**, **"bojxona tasdiqlagan"** (customs-approved), **"rasmiy hamkor"** (official partner), **"100% kafolat"** (100% guarantee) (DEC-25; ZRU-776 art. 16 and 5, sanction art. 47: 70 BHM for legal entities). Russian forms: [PENDING: Huquq] — `roles-legal.md` gives only Uzbek forms. Also risky per Huquq (avoid): "brokerni toʻliq almashtiradi", "biz siz uchun topshiramiz", "ed2 bilan integratsiyalangan" (without an official agreement), "xatosiz", "jarimasiz", and "bir tugmada topshiriladi" where it hides the signing step.
2a. Not a phrase ban but a factual limit: copy must not state things that are false — that YuklaGo signs or submits, that a state body approved or partnered with it, or that it uses an official API (§2 hard boundaries).
3. Signer wording: "deklaratsiyalovchi shaxslar roʻyxatiga kiritilgan shaxs" (DEC-10, DEC-27).
3a. Must-stay-visible lines (D-23, `roles-legal.md` B4) stay on screen as short lines or chips and are not counted in the 60-word cap.
4. Customs processing times are "bojxona ishlov muddati", never a user countdown.
5. Every number: source + date, or "≈ Taxmin", "Namuna", "Tasdiqlanmagan", "—".
6. Y19 explanations are labelled "YuklaGo izohi, rasmiy kod emas".
7. Use "E-Tranzit", never "NCTS".

---

## 11. Open questions (owner per item)

| # | Question | Owner |
|---|---|---|
| Q-1 | Live ed2 automation and broker-activity status with the Customs Committee. **Letter stays unsent;** the founder talks to the officials himself (DEC-24). Outcome decides when `ED2_LIVE_AUTOMATION` is switched on. | Hakathon CEO (coordinates with the founder, who holds the switch) |
| ~~Q-C1~~ | ~~Filing client~~ — **resolved by DEC-23** (desktop app main, extension fallback) | — |
| ~~Q-C2~~ | ~~Desktop engine and OS list~~ — **resolved by DEC-28** (Electron; Windows first, macOS next); E-IMZO-in-app is a build-phase acceptance test (AC-14.8) | — |
| Q-2 | May automation click "Saqlash" (save draft)? | CEO |
| Q-3 | Supported browsers; Web Store vs unpacked for pilot | CEO |
| Q-4 | Notification channel (PWA push, SMS, Telegram as reminders only?) | CEO |
| Q-5 | Session-log values: device vs UZ server (upload of session values). Retention is now set by `AUDIT_LOG_RETENTION_YEARS` = 3 (proposal, not law; DEC-29) — Huquq to confirm against ZRU-764 art. 16 / ZRU-547 | CEO + Huquq |
| Q-6 | **BLOCKED.** Live check of grafas 13/33/36/41/43/44(904)/45/47 and selectors (and Q-7 observation, embedded-window signing test). ed2 has no demo login. Needs: a cooperating key holder (company director, its listed staff specialist, or a notified broker's specialist) logging in **with their own E-IMZO on their own PC**; **written consent**; nothing sent, registered or signed; no automation; DevTools read-only by or under the key holder; script in declarant-v3-check §G; output `data/declarant/ed2-observations-YYYYMMDD.md`. | Hakathon CEO (coordinates with the founder as needed); Deklarant runs the session |
| Q-7 | E-IMZO signing on ed2 today (modal vs native window; untrusted input accepted?) | Deklarant |
| Q-8 | Google Cloud DPA review; VMQ 415 list re-check for DE/NL | Huquq |
| Q-9 | Public offer clauses 5.1–5.5 | Huquq |
| Q-10 | ZRU-764 art. 16 applicability, body, deadline | Huquq |
| Q-11 | All TIF TN flags in §3A.1 (band edges, rounding, 300¹ edges and VAT base, kg net/gross, ST-1 text, VM 43/737/658 mappings, IMEI fee, export duty) | TIF TN |
| Q-12 | All Deklarant flags in §3A.1 (EK10 target, signer edge cases, phyto/vet/origin fees and times, conformity lead time, Set C certificates) | Deklarant |
| Q-13 | All Huquq flags (start-day rule, storage roll-over and expiry, E-kontrakt rejection/penalty, bank lists, MJtK future editions, re-export 6 months, transit security list) | Huquq |
| Q-14 | **BLOCKED.** Gold case (PE-22): one released IM40 after 01.09.2026 with consent, NDA and source documents (declarant-v3-check §H). Optional: the founder may ask officials for an anonymised sample in his own talks — nothing sent. | Hakathon CEO (coordinates with the founder as needed); Deklarant runs the comparison |
| Q-15 | Y4 interviews (12–15) | CEO |
| ~~Q-18~~ | ~~Update `tariff-payments.md` §3 item 8~~ — **closed**: the tariff expert fixed §3 item 8 and updated `data/tariff/rules.md`; narrowings applied to R32, PE-11, PE-19, AC-5.1, AC-11.5, AC-12.2, AC-12.3 and flags | — |
| ~~Q-19~~ | ~~Deklarant data-file changes~~ — **closed** (README changelog 18.11 04:20, verified by PM): explicit gross/net formulas and `gross_weight_scope` in `tolerances.json`; grafa 44 code 904 "МЕТОД" in `grafa-map.json` (OUR READING, UNVERIFIED on live ed2; line format a proposal); new `grafa-map-ek10.json/.md` (45 grafas). Applied to DEC-18, AC-11.5, AC-12.4, AC-13.1a, AC-13.1d, AC-21.5–AC-21.7, `TOL_GROSS_WEIGHT`, `TOL_NET_WEIGHT`, `PALLETS_AS_PACKAGING`, `GRAFA44_904_ENTRY`, new `EK10_GRAFA_LIVE_CHECKS`. Unverified marks kept. | — |
| Q-16 | Pilot value for MAX_ITEMS_PER_BYUD_N | Deklarant |
| Q-17 | Mobile tabs and offline capture | CEO |
| ~~Q-20~~ | ~~Company with more than one signer~~ — **closed** by the Hakathon CEO: several user accounts per company, all with the same single client role; each signer has their own login, ed1 entry and ERI; no shared logins; audit log shows who did what (DEC-29; AC-1.12, AC-1.13, AC-43.10, §6A) | — |
| ~~Q-21~~ | ~~Auto-detect a signer change from the public certificate fields~~ — **closed** (Hakathon CEO, 19.11): **Security YES + Huquq YES with conditions.** `CERT_PUBLIC_FIELDS_AUTODETECT=true`. Conditions are AC-1.15–AC-1.21: public fields only (PINFL, STIR, serial, validity), never the private key; server-side HMAC with a key held in Uzbekistan, raw values never on disk or in logs; stored only HMACs, validity date and a masked view, deleted when the key changes or the account closes; never sent to a foreign LLM; consent and privacy-policy text state the purpose (ZRU-547 art. 4, 19, 21); four log events; one confirm per new certificate (the per-session confirm is dropped); ed1 is never read automatically (grey zone, [UNVERIFIED]); the E-IMZO API, integrator terms and registration-centre offer are [UNVERIFIED]. Legal basis per Huquq: ZRU-793 art. 3, 20, 24; ZRU-547 art. 4, 19, 21, 24. **Open for the CEO to confirm:** on a mismatch Security proposed blocking the fill, Huquq says warn only and let the person decide (ZRU-547 art. 24). Warn-only plus an audit-log event is applied as the legal reading (AC-1.18). Fallback until PC-16: the one-time confirm. | Hakathon CEO (confirm warn-only) |

---

## 12. Changelog vs v2

- Scope: from "replaces the broker's main role, Phase 1 IM40" to **full broker replacement** (DEC-13); 115 broker tasks mapped, 0 out of scope; partner broker optional (Y31).
- Features: Y1–Y26 kept and rewritten with AC; new Y27–Y42 (multi-line, payment prep, E-arxiv, preliminary declaration, partner broker, consent, corrections, post-release records, valuation, inspections, appeals, arrival events, guarantees, refunds, client profile, Uzbek text normalisation). v2 had no formal AC (G8).
- Rules: re-sourced on lex.uz; PF-5414 replaced by VMQ 605 cl. 1; "authorised specialist" replaced by declaring-persons list; signer types (AD); ERI issuer (VMQ 348) without address/fee; customs processing times separated from user clocks; storage "≤ 60 days" from warehouse document; 180-day currency clocks and fines; E-kontrakt; path test; Yagona darcha gate; conformity (VMQ 502); export, origin (VMQ 994), phyto (VMQ 727), vet (VMQ 148), fruit/veg (VMQ 163); special-regime rules and codes (DEC-9).
- New §3A Payment engine rules (PE-1–PE-22) and config-flag table.
- Fee: "310 000" removed; VMQ 55 bands, 1 BHM = 440,000; 20 % pre-arrival discount (352,000) allowed (DEC-4).
- Grafa map: "48 maydon" replaced by 46-grafa IM40 map; grafa 36 removed from IM40.
- Clocks: "File by" +14 / "Legal max" +15 (DEC-17); ops calendar (DEC-20).
- Tolerances as "PROPOSAL, not law" (DEC-18); freight by gross weight (DEC-19).
- Automation: no "Tez" on live (DEC-7); desktop app main client, extension fallback (DEC-23); live cabinet behind the founder's switch (DEC-24).
- Security: Gemini EU, masking, consent, retention, breach notices (DEC-15).
- Brand: Varaq tokens and designer rules (DEC-11, DEC-22).
- Copy rules: public line "Brokersiz, oʻzingiz topshirasiz — tez va tushunarli"; only two phrases banned; PC-8 resolved (DEC-25).
- **Q-18 closed (tariff narrowings, Instruction 2773 (edition with 2773-15 of 22.07.2026) https://lex.uz/uz/docs/2924955):** 6XX in grafa 44 = exemptions/privileges on payments (cl. 25 sub-point 39 "е"); FTA/Türkiye origin certificate = grafa 44 code 701 "СПТИМ" (Annex 12 row 63); tariff preference as 6XX [UNVERIFIED] → new flag `TARIFF_PREF_AS_6XX`; 904 "МЕТОД" placement in 44 stays our inference (`GRAFA44_904_ENTRY`); grafa 34 = "000" if origin unknown; grafa 45 rounded to 2 decimals, statistical value to 3 (sub-points 40–42); soʻm rounding of payments stays [UNVERIFIED].
- **DEC-28:** Q-C2 closed — Electron, Windows first, macOS next; E-IMZO-in-app is a build-phase acceptance test (AC-14.8); signing fallback worded everywhere as "the system browser with the YuklaGo MV3 extension (DEC-23)"; Q-6, Q-14, Q-1 and `ED2_LIVE_AUTOMATION` owners set to the Hakathon CEO (coordinates with the founder).
- **DEC-27 (Deklarant v3 check):** signer wording "kiritilgan shaxs"; AC-1.6 broker notification; AC-14.7 embedded-window signing test; EK10 grafa list (cl. 21) and grafa 43 (cl. 22) — `EK10_GRAFA43_CODES` flag deleted; grafa 36 empty, 16/17 not filled, method in 44/904 [INFERENCE]; R33 edition 2773-15 (22.07.2026); DEC-17 end of working hours and raw D+14 for unverified calendars; DEC-18 three gross tiers and explicit net max(), grafa 35 definition; Y18 trigger reworded; Q-6 and PE-22 marked BLOCKED with their plans; Set A "namuna" only.
- **DEC-23–DEC-26:** desktop app is the main filing client with an embedded ed2 window, extension as fallback (Q-C1 closed); `ED2_LIVE_AUTOMATION` is the founder's switch — "ready, enabled when the founder confirms"; grafa 36/43 conflict closed in favour of the Deklarant map.
- Y4 marked hypothesis; Y19 has 44 messages (corrected from 43); Y18 has 13 more triggers, now warnings/options except four hard blocks.
- **DEC-29 (three roles):** one client role (Owner = signer) plus YuklaGo Support and Admin. New §6A Roles (matrix, signer check, 8 SoD rules, audit rules, gap handling). New Y43 (AC-43.1–AC-43.9), Y1 AC-1.6 reworded and AC-1.7–AC-1.11 added, admin boundaries in AC-8.1c / AC-13.1b. 🔒 DPO flags, `AUDIT_LOG_RETENTION_YEARS`, `SUPPORT_ACCESS_DEFAULT_HOURS`, PC-15 DPO, Q-20, Q-21, Q-5 updated, §9 D-17–D-19. No multi-role client RBAC existed in v3, so none had to be removed.
- **CEO decisions on DEC-29 open points (19.11):** AC-1.6 confirmed (a broker's specialist never signs inside a client account; Y18/Y31 offered); Q-20 closed — several accounts per company, same single role, own login/ed1 entry/ERI each, no shared logins, per-person audit (new AC-1.12, AC-1.13, AC-43.10; DEC-29, §6A updated); Q-21 reworded to the public certificate fields (name, PINFL, STIR) returned by E-IMZO, never the private key, pending Security + Huquq; one-tap confirm kept.
- **Q-21 — Security answer recorded (19.11):** yes with conditions (public fields only, server-side HMAC with a UZ-held key, HMACs + validity + masked view stored, four log events, consent line, confirm only at set-up/mismatch/new certificate, ed1 expiry still user-confirmed, separate E-IMZO domain API key [UNVERIFIED]); Huquq and CEO pending. New PROPOSED flag `CERT_PUBLIC_FIELDS_AUTODETECT=false` (🔒 DPO) and PC-16. Current behaviour (one-tap confirm per session) unchanged.
- **roles-legal merge and CEO decisions (19.11):** Q-21 closed (auto-detect on; AC-1.15–AC-1.21; warn-only on mismatch pending CEO confirmation; one confirm per new certificate); PC-15 cites ZRU-547 art. 31 (last part) and drops the re-check note; AC-1.7a staff-specialist and own-key warnings; AC-1.14 no accounts for non-signers in Phase 1; AC-43.1 step-up = five triggers, none for payment or signing; AC-43.4 and §6A: Support never signs, sends, joins the TIF list or logs in as the client; AC-43.11 no external AI and third-party notice; DEC-25 and §10 add "bojxona tasdiqlagan", "rasmiy hamkor", "100% kafolat"; D-21–D-23 (must-stay-visible lines outside the 60-word cap).
- **Q-19 closed:** weight formulas (T from D, 3 decimals, exact hit = warning, per line and total, worst wins), pallet question, 904 line format proposal, EK10 45-grafa map with the IM40 diff (AC-21.5–AC-21.7, `EK10_GRAFA_LIVE_CHECKS`), §9 D-20.

---

## Appendix A. Pending official confirmation

| # | Item | Current legal position (answers-legal / reviews) | Behaviour until confirmed |
|---|---|---|---|
| PC-1 | **Live ed2 automation** | No law permits or bans it; grey zone; conditional approval if user logs in and signs with own key, fill is visible, nothing hidden or bypassed (Huquq Q-A; 560-II art. 12; JK 278-2–278-4 risk). | `ED2_LIVE_AUTOMATION` = **ready, enabled when the founder confirms** (DEC-24). Until on: mock portal for demos and training; live path = field-by-field copy guide. In every mode the user logs in and signs with their own key. |
| PC-2 | **Broker-activity status** | Not broker if SaaS used by the declarant who signs itself; broker if YuklaGo staff sign/are listed/act in the client's name (BK 15, 277; ZRU-701; VMQ 847; 20 BHM fine). | Staff never sign or appear in ed1 lists; partner broker contracts with the user directly. |
| PC-3 | **XML schema / file import** into ed2 | No official public schema found. | `XML_EXPORT=off`; Y24 hidden. |
| PC-4 | Reading status from the cabinet | Not confirmed as allowed. | User enters reg. number/status; `CABINET_STATUS_READ=off`. |
| PC-5 | Trusted person (PoA) signing; YaTT employee as signer | [INFERENCE/UNVERIFIED] — VMQ 605 cl. 2, 15 list only declarant, staff specialist, broker specialist. | Flags false; user signs personally or uses a broker. |
| PC-6 | EK10 filing system (cargo.customs.uz vs ed2) | cargo.customs.uz observed; ed2 for EK10 [UNVERIFIED]. | Target cargo.customs.uz; guide only until the founder's switch is extended to it. |
| PC-7 | E-Tranzit / us-uz.gov.uz for transit; special-regime filing targets | Named in VMQ 737 (2022) and VMQ 605 cl. 14; automation status unknown. | Guide only; no automation. |
| PC-8 | ~~Copy rule vs full-replacement scope~~ — **resolved (DEC-25)** | Scope is full broker replacement; legal.md's broker-activity risk is handled by the conduct rules in PC-2 (staff never sign or are listed), not by avoiding the scope. | Public line "Brokersiz, oʻzingiz topshirasiz — tez va tushunarli"; only "broker oʻrnini bosadi" and "rasmiylashtirib beramiz" banned. Closed. |
| PC-9 | Formal request to the Customs Committee | Draft exists in legal.md; **stays unsent**; the founder talks to the officials himself (DEC-14, DEC-24). | Q-1; PC-1/PC-2 behaviour as above; the founder's confirmation turns on `ED2_LIVE_AUTOMATION`. |
| PC-10 | Google Cloud DPA and cross-border basis | DE/NL on VMQ 415 list; DPA review pending. | Consent + masking + fail-closed; no unmasked PII leaves UZ. |
| PC-11 | E-kontrakt: BYUD rejection without ID; penalty article | [UNVERIFIED]. | Blocker for paid contracts; no penalty shown. |
| PC-12 | Grafas 33/41/44 (904 entry and line format)/45/47 on live ed2; on-screen presence of box 36; EK10 ⚠️ grafas (8, 18, 31, 37, 40, 43, 45; `EK10_GRAFA_LIVE_CHECKS`) on the EK10 filing system | Deklarant map ⚠️ items (DEC-21) and declarant-v3-check §C. Grafa 13 = CB USD/UZS rate (map); grafa 36 left empty and grafa 43 = 0/1 per DEC-26. | Flags; no demo claims; checked only in the Q-6 session. |
| PC-13 | MJtK editions dated 30.12.2026 and 05.02.2027 | Future editions listed on lex.uz. | Show current fines; re-check before each date. |
| PC-14 | Start-day rule for the 15-day clock | No counting article in BK; CC 146 analogy unconfirmed. | "File by" +14 and "Legal max" +15 (DEC-17). |
| PC-15 | **Responsible person for personal data ("DPO" in this spec)** — org requirement before launch | **ZRU-547 art. 31, last part** (https://lex.uz/docs/4396419): the owner and/or operator names a structural unit **or** an official responsible for processing and protecting personal data, and ensures their work per the model procedure. ZRU-1125 (https://lex.uz/docs/8099215) changes only ZRU-547 art. 3 (part 2), art. 20 (part 1) and art. 27-1; it does not touch art. 31. No size or activity exemption; one named employee is enough; the title "DPO" is not required; no registration or notification step. The model procedure (Ministry of Justice, 2023) was not read, so this person's exact duties are [UNVERIFIED] (`roles-legal.md` PC-15). | No responsible person yet, so no launch. 🔒 DPO flags cannot change until one exists. Defaults set by a CEO decision (e.g. `CERT_PUBLIC_FIELDS_AUTODETECT=true`) still need this person's sign-off before launch. Owner: Hakathon CEO (appointment). |
| PC-16 | **E-IMZO API key for the YuklaGo domain** (needed for `CERT_PUBLIC_FIELDS_AUTODETECT`) | Per Security (`roles-rbac.md` § Q-21), the YuklaGo app needs its own E-IMZO API key to call E-IMZO's certificate list; how to obtain one is [UNVERIFIED]. The API is known only from ed2's copy of `e-imzo-client.js`, not vendor documentation. Reusing ed2's localhost keys would be a bypass (R58) and is not allowed. Huquq: E-IMZO integrator terms were not found in open sources, and the registration centre's public offer (ZRU-793 art. 20) was not read — [UNVERIFIED]; read both before integration (`roles-legal.md` Q-21). | Open. Until the key exists, auto-detect falls back to the one-time confirm (AC-1.9). Owner: Security (how to obtain), with Huquq (terms). |

---

## Appendix B. Main sources

Customs Code https://lex.uz/docs/2876354 · VMQ 605 https://lex.uz/uz/docs/-3844549 · VMQ 55 https://lex.uz/docs/7357270 · PF-115 https://www.lex.uz/uz/docs/-8283656 · PF-250 https://lex.uz/uz/docs/-7934915 · PQ-181 https://lex.uz/uz/docs/-7533457 · Yo'riqnoma 2773 https://lex.uz/uz/docs/-2924955 · VMQ 283 https://lex.uz/docs/4812419 · ZRU-573 https://lex.uz/docs/4562834 · VMQ 348 https://lex.uz/docs/3730168 · VMQ 847 https://lex.uz/docs/7274716 · ZRU-701 https://lex.uz/docs/5511879 · VMQ 502 https://lex.uz/docs/-7080176 · VMQ 737 (2020) https://lex.uz/uz/docs/-5115923 · VMQ 658 https://www.lex.uz/uz/acts/-6284990 · VMQ 778 https://www.lex.uz/docs/-4517458 · VMQ 994 https://lex.uz/uz/docs/-4643161 · VMQ 163 https://lex.uz/uz/docs/-4213596 · VMQ 148 https://www.lex.uz/acts/-6427764 · Plant Quarantine Law https://www.lex.uz/uz/docs/-119173 · VMQ 727 (2024) https://lex.uz/uz/acts/-7208474 · PQ-65 https://lex.uz/uz/docs/-6388997 · MFN list https://lex.uz/uz/docs/-4911943 · Tax Code https://lex.uz/docs/4674902 · ZRU-547 https://lex.uz/docs/4396419 · VMQ 415 https://lex.uz/docs/8369688 · ZRU-764 https://lex.uz/docs/5960604 · MJtK https://lex.uz/uz/docs/-97664 · Civil Code https://lex.uz/docs/111181 · my.gov.uz service 207 https://my.gov.uz/uz/service/207

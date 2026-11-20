# YuklaGo — Engineering review (spec v2 + web design v0.1)

*Full-stack engineering, 18 Nov 2026, ~04:00 Tashkent time (UTC+5). This is not legal advice. Every figure here is either quoted from a file or URL I opened, or marked **TODO**.*

**What I read:** `yuklago-spec-v2.md` (v2 overrides the old spec where they differ), `yuklago-web-design-brief.md`, `design-v0.1/design-rationale.md`, all 28 pages of `design-v0.1/yuklago-web-ui-v0.1.pdf` (pdftotext plus page renders), `/workspace/yuklago/ARCHITECTURE.md`, `packages/schemas/src/calc.ts` and `deadlines.ts` (v0.2), `apps/web-mobile-ui`, and the existing `/workspace/yuklago/autofill` prototype. I also checked the law texts already saved on the box: VM 55 (`/workspace/bojxona/fee.txt`), the Customs Code (`bk_clean.txt`) and BYD fill-in Instruction No. 2773 (`y2773.txt`, edition of 22.07.2026).

---

## TL;DR

- **Architecture stance:** keep the modular monolith from ARCHITECTURE.md: Next.js web/PWA, Postgres, MinIO, a deterministic `packages/calc` engine, and everything hosted in Uzbekistan. Spec v2 adds a **cabinet filler**. It should be **one shared fill engine plus versioned mappings**. It runs against a mock portal (`mashq.yuklago.uz`) for the demo. Later it runs inside a desktop shell or the existing browser extension. **It cannot run inside the web app against the real ed2.** I checked this: on 18.11.2026 ed2.customs.uz sent `X-Frame-Options: SAMEORIGIN` and `frame-ancestors 'self'`, so no other site can put it in an iframe.
- **Biggest design risks:**
  1. "Rasmiy" chips sit on amounts that are calculated from estimates.
  2. A clearance fee of 310,000 so'm is labelled "Rasmiy", but it doesn't fit any VM 55 band.
  3. "YuklaGo taxmini" freight has no data source.
  4. The go/no-go screen says "Topilmadi · Rasmiy ro'yxat" with no machine-readable official list behind it.
  5. The mock sign dialog has a **password field on a YuklaGo domain**.
  6. Partial codes like "9405 42 xxx x" are offered as choices.
  7. The real-ed2 path implies the cabinet opens "in this window" in the web app.
  8. The mobile UI still has a **"Qozog'iston + ST-1" variant**. Spec v2 §11 forbids it.
- **Top data asks (P0, by 18 Nov 11:00):**
  - 5–10 demo TN codes with verified duty rows and NOTARIF screenshots.
  - VM 55 band edges, currency and date rules, and a ruling on the 20% discount.
  - Deadline counting rules with article numbers.
  - BYD grafa map for IM40.
  - 3 synthetic document sets with answer keys.
  - Cross-check tolerances.

---

## 1. Architecture and data model behind each core feature

Baseline: **ARCHITECTURE.md §1–§9** (stack, modules, tables, engine, extraction, checks, reference sources, security, mock ed2). This section lists only what spec v2 changes.

### 1.0 What changed with spec v2 (architecture-level)

| Area | ARCHITECTURE.md (v1 brief) | Spec v2 | Engineering decision |
| --- | --- | --- | --- |
| Product goal | Prepare a checked pack; the owner files | Replace the broker's main role; fill the user's **own** cabinet live; stop at ERI | Add a **Filler** subsystem (§1.8). The pack becomes the filler's input and the broker hand-off. |
| Clients | Web + PWA | Web + **desktop** (embedded browser) + mobile app; no Telegram | Web + PWA as now. Desktop = an Electron shell around the same fill engine (post-hackathon). The existing MV3 extension is the bridge (see §4, G1). |
| LLM uses | OCR/extraction + TN ranking only | Adds **document classification** and the **reply-explainer** (Y19). The design adds **translation** and **supplier request text**. | Allowed only with "no new numbers" guard rails (§1.1). **The PO must confirm**, because this widens the original hard constraint. |
| Mock ed2 | `demo-ed2.yuklago.uz`, scripted risk channel, status webhook | Mock used for demos/training; status comes only from what the user marks or pastes (no feed) | Rename to **`mashq.yuklago.uz`** (as in the design). Drop the status webhook into the product. The mock shows a message; the user marks the status or pastes it into Y19. |
| Escalation | Handoff pack for "the declarant" | Y18 broker escalation at any step | Share links plus pack (§1.7). Escalation reasons are stored. |
| New features | — | Y1 readiness, Y2 router, Y4 kargo, Y5 entitlement, Y6 E-kontrakt/bank, Y7 go/no-go incl. Asl Belgisi, Y19 explainer, security journal | Mostly content and rule tables (§1.9). Each one needs expert data (§3). |
| 20% preliminary-declaration discount | Built into the engine (it is in the box copy of the VM 55 footnote) | "Do not publish unless the current official text clearly supports it" | Engine keeps it **behind a flag, default OFF**, with a warning. TIF TN specialist decides (§3). |
| Worked example | 10,000 USD (T1) | Use a value inside a band, e.g. **9,500 USD → 1 BHM** | Change golden test T1 and the mobile mocks to 9,500 USD. Keep 10,000 USD only as a boundary test that returns a warning. |

### 1.1 OCR / extraction (Y9) — ARCHITECTURE.md §5.1
- Pipeline unchanged: classify → schema-constrained vision-LLM extraction → deterministic post-checks → side-by-side review with bbox.
- **Data:** `documents`, `extractions` (raw model output kept), `extracted_fields` (`value`, `user_value`, `confidence`, `page`, `bbox`, `source_snippet`, `reviewed_by/at`).
- **New in v2/design:**
  - Low-confidence handwriting blocks "tasdiqlangan" (design p.9/13).
  - "Asl matn · tarjimani ko'rsatish" means an LLM translation is shown for display only and never feeds a field.
  - Document kinds now include "Ombor dalolatnomasi" (warehouse acceptance act). It is evidence for the deadline start date.
- **Guard rail for all non-extraction LLM text** (translation, explainer, supplier request, code reason): after generation, every number in the output must already appear in the structured input. If one doesn't, the text is rejected and a template is used instead.

### 1.2 TIF TN validation (Y10) — ARCHITECTURE.md §5.2
- Unchanged:
  1. Pull candidates from `tn_codes` (official list).
  2. The LLM picks only from that candidate list.
  3. A hard check confirms the code is on the list, is 10 digits, is active on `as_of`, and has a resolvable duty row.
  4. The user confirms.
- **v2/design deltas:**
  - **Clarifying questions** (p.14, "chiroq korpusi bilan sotiladimi?") come from a **per-heading question table** written by the specialist. They are not invented by the LLM.
  - Answers are stored in `tn_suggestions.answers_json`.
  - The **"Qanchalik ishonchli: Yuqori"** label must not be the model's own self-assessment. Use deterministic signals instead: number of surviving candidates, agreement with the invoice HS prefix, clarifying answers given. No "high" label until the gold set (ARCH §5.2.6) exists.
  - **Official description text** ("Rasmiy nomi") needs the machine-readable PQ-181 Annex 1, which we don't have yet (§3).

### 1.3 Deterministic payment engine (Y3, Y11) — ARCHITECTURE.md §4
- Engine, rule tables, versioning by date and the test list are unchanged. Customs Code basis is confirmed in the box copy:
  - Art. 323: payments are calculated by the declarant, in UZS.
  - Art. 324: the rates used are those in force on the day the declaration is accepted.
  - Art. 326: FX is the CBU rate on the day the declaration is accepted.
- **Provenance model must be richer than `status: sample|verified`.** The design gives every value one of six chips. Calculated amounts mix their inputs, so the server must compute the chip:

  ```ts
  type Provenance = "official" | "estimate" | "document" | "user_confirmed" | "suggestion" | "missing";
  // derived amount provenance = weakest input: missing > suggestion > estimate > document/user_confirmed > official
  ```

  Example from design p.10: duty = 10% (official rate) × customs value that includes ≈ freight. The duty amount is therefore **≈ estimate**, not "Rasmiy". The *rate* chip can still say Rasmiy.
- **Proposed `calc.ts` v0.3** (additive; the mobile UI keeps working):
  - `CalcRequest.lines[]` with `qty`, `qtyUnit`, `netKg`, `grossKg`, `originCountry`, `tnCode`. Today multiple lines only come in through `shipmentId`, and specific (per-unit) duties need quantities.
  - `freightCurrency`, `insuranceCurrency`, `includedInInvoice` flags, `incoterms`, `regime` (`IM40|EK10`), `preliminary`.
  - `Cited.value: string | null` plus `provenance`, `ruleStatus`, `derivedFrom[]`. The design's "Stavka topilmadi → —" can't be expressed today because `value` is required.
  - `CalcResult.completeness: "complete" | "incomplete" | "refused"` alongside `isEstimate`.
  - `fx: Cited[]` (one per currency; the design has CNY invoice + USD kargo). Today it is a single object.
  - `duty` gets `rateType`, `specificAmount/unit`.
  - `customsFee` gets `bhmMultiplier`, `bhmValue`, `adjustments[]`.
  - `alternatives[]: { tnCode, label, deltaTotal: Cited }`, computed server-side (design p.10/14 shows "+3 068 800").
  - `kargo?: { quotePerKg, kg, includesCustoms, total: Cited }`, computed server-side from the **user's** quote only (Y4).

### 1.4 Cross-checks (Y13) — ARCHITECTURE.md §6.1
- Rules engine unchanged (`packages/checks`). Fixed UZ/RU templates; `check_findings.acknowledged_by/at`.
- **Design-driven additions:**
  - Findings are keyed to **grafa** (p.15: "38-grafa · Netto…"), so each rule needs a `grafa_refs` field.
  - A "bir xil kompaniyami? Ha" answer is stored as a user decision with an audit row. It is not a silent pass.
  - The gate (p.16) opens only when blocking findings = 0 **and** the responsibility tick is set **and** every fill-bound field is `user_confirmed`.

### 1.5 Deadline clock (Y8) — ARCHITECTURE.md §6.2
- `deadlines.ts` v0.2 already makes the server count days (good).
- **Missing:**
  - `countingRule` (does day 0 = the presentation day?). The design shows 13.11 → 27.11, i.e. presentation counted as day 1. The mobile mock shows 10.11 → 25.11, i.e. +15. **They disagree** → TODO for Bojxona Huquq.
  - `unit` (`calendar_days | working_days | hours`).
  - `startEvidence` (user-entered + attached document id).
  - `reminders[]`.
- New kinds to add: `preliminary_lapse` (Art. 262), `export_before_departure` (VM 605 cl. 11), `advance_info` (Art. 206, guidance only), `amendment_window` (Art. 266, info).
- Working-day clocks need a holiday calendar (TODO).

### 1.6 Product library (Y20) — ARCHITECTURE.md §6.3
- `products` + `needs_review`. A card is flagged when a loader closes the rule row it depends on (ruleset diff).
- Library cards must hold **full 10-digit codes**. The design's "9401 xx xxx x" / "3926 xx xxx x" / "0813 xx xxx x" (p.25) aren't valid saved codes.
- "Rate change" alerts can only fire for rows *we* load. Use the wording "YuklaGo jadvali yangilandi (manba …, kuchga kirgan …)", not "rasmiy jadval yangilandi" (we have no official feed).

### 1.7 Handoff pack / broker escalation (Y18) — ARCHITECTURE.md §6.4
- PDF + JSON (+ZIP). XML still waits for a validated real sample (Y24).
- **Design adds:**
  - Escalation reason chips → `escalations(reason, note)`.
  - **Secure link, 7 days, revocable, open count** → `share_links(token_hash, expires_at, open_count, revoked_at)`.
  - "Send to the broker's phone or email" needs an SMS/email provider. For the demo: copy the link.
- **Contract fix:** `autofill/samples/handoff.sample.json` (`yuklago.handoff.v1`) carries money as **JSON numbers** (`"total": 18450.00`), while `calc.ts` uses decimal strings. Move handoff to **v2 with decimal strings**, per-field `provenance`, and **only `user_confirmed` values** for anything that is filled.

### 1.8 Cabinet filler + mock portal (Y14–Y17) — new; ARCHITECTURE.md §9 becomes the mock part
- **An existing asset is ahead of the spec.** `/workspace/yuklago/autofill/` already has:
  - one fill engine (`extension/lib/filler.js`) driven by versioned mappings (`mappings/mock-ed2.json`);
  - an MV3 Chrome/Edge extension (side panel, pause/resume/stop, read-back, local JSON log, no network, refuses `.pfx/.p12/.key`, never clicks sign/submit, rejects mappings that touch password/file fields);
  - a Playwright runner with video;
  - a mock cabinet;
  - `mappings/ed2-real.TODO.json`, deliberately empty: "selectors are not guessed".
  
  Reuse all of it. Don't rebuild.
- **Hosts for the same engine:**

  | Host | Real ed2? | Mock? | Notes |
  | --- | --- | --- | --- |
  | Web app (yuklago.uz) | **No.** ed2 sends `X-Frame-Options: SAMEORIGIN` + CSP `frame-ancestors 'self'` (checked 18.11.2026), and a cross-origin iframe can't be scripted anyway | Yes: `mashq.yuklago.uz` framed with `frame-ancestors https://yuklago.uz`, driven over `postMessage` | Enough for the hackathon demo and for training. |
  | Browser extension (exists) | Technically possible in the user's own browser and session, once a lawful mapping exists | Yes | E-IMZO keeps working because it's the user's normal browser. Needs `host_permissions` for ed2 — **legal sign-off first**. |
  | Desktop (Electron, spec v2) | Technically possible: top-level webview + preload with the same filler | Yes | ed2's CSP allows `connect-src ws://127.0.0.1:64646 wss://127.0.0.1:64443` (a local signing service, presumably E-IMZO). **TODO: test that E-IMZO works inside Electron on Windows with a real token.** That test needs Huquq approval and the owner present. |
- **Data:**
  - `fill_sessions(id, shipment_id, target: mock|real, mapping_id@version, speed, started/ended, outcome, user_marked_signed_at)`;
  - `fill_events(session_id, t, actor: user|yuklago, grafa, action, readback_ok, value_hash)`;
  - `grafa_mappings(id, version, target, fields[])`.
  
  Only `value_hash` goes to the server, so session logs don't copy commercial or personal values. The full value table stays on the device (design p.23). **TODO: Security role to confirm.**
- **Fail-closed rules (already in the prototype):** field not found → stop. Read-back mismatch → stop. Never click sign/submit/ERI controls. Never touch password/file inputs. User input (`isTrusted` events) → pause instantly and offer a draft diff (design p.20).
- **Mock ed2 (`mashq.yuklago.uz`) design deltas vs ARCHITECTURE.md §9:**
  - The form follows **Instruction No. 2773 grafa layout** (see §2, p.15 for format issues).
  - **No password or PIN input anywhere**, even simulated (§2, p.21).
  - Registration number `MASHQ-######`.
  - Scripted outcomes (accepted / returned with a library message) feed Y19 by paste, not by webhook.
  - The mock's CSP must block `ws://127.0.0.1:*` so it can never reach a real signing service.

### 1.9 New v2 modules (thin, mostly content + rules)

| Module | Tables | Engine/LLM | Blocked on |
| --- | --- | --- | --- |
| Y1 readiness ("O'zim topshira olamanmi?") | `readiness_profile(org_id, has_entity, eri_status, cabinet_status, signer_type, updated_at)`, all self-declared | Static content | Huquq: ERI issuer, authorised-specialist registration steps + URLs |
| Y2 wrong-flow router | `router_rules` (static) | Static | Huquq: criteria; whether a non-entrepreneur may file commercially |
| Y4 kargo compare | `kargo_quotes` | `calc` | Interviews only; no typical rates |
| Y5 preference entitlement | `preference_rules(tn_prefix, origin, agreement, doc_form, conditions, source, valid_from, status)` | Engine lookup | TIF TN specialist; out of the demo unless a verified row exists |
| Y6 E-kontrakt/bank | `checklist_items(kind, text_uz, url, source, status)` | Static | Huquq |
| Y7 go/no-go incl. Asl Belgisi | `requirement_rules(tn_prefix, req_type: conformity|single_window_permit|marking|prohibition, issuer, source_url, checked_at, status)` | Deterministic lookup | TIF TN + Ustoz; per demo code only |
| Y19 reply-explainer | `status_messages(pattern_uz/ru, meaning_uz, next_step_uz, grafa_refs, source_ref)` | Match against the library first; LLM may only paraphrase a matched entry or give a generic "unknown message" template | Ustoz: real redacted messages |
| Auth + security journal | `sessions/devices`, `audit_log` (exists in ARCH) | — | SMS OTP provider (TODO); demo uses a fixed OTP |
| Notifications | `notification_prefs`, push subscriptions | Jobs | SMS later; **Telegram is out of scope in v2** |

Hosting, ERI boundary and localisation: unchanged from ARCHITECTURE.md §8. Spec v2 §8.5/§9.4 already matches it.

---

## 2. Design review — what is hard or impossible, and what to do instead

Flag key: **[LLM$]** implies the LLM computes money · **[ERI]** implies storing or collecting ERI secrets · **[LEGAL]** an unverifiable legal or official claim · **[ED2]** implies real ed2 integration · **[NOSRC]** a number without a real source/date · **[HARD]** technically hard · **[OK]** feasible as drawn.

| Page / screen | Element | Flag | Why | Do instead |
| --- | --- | --- | --- | --- |
| p.1 Design system | "Every value wears exactly one chip" | [HARD] | Calculated amounts have several inputs (official rate × estimated base) | Server computes provenance as the weakest input (§1.3). Show the rate chip and the amount chip separately. |
| p.1 / p.21 | "Probel" (Space) pauses | [HARD] | Space types a space when focus is inside a cabinet field | Space works only when focus is in the YuklaGo rail. Typing in the cabinet already pauses. |
| p.4 Landing | Sample calc with **"Rasmiy · 01.11.2026"** chips on a public page | [LEGAL][NOSRC] | Layout numbers shown publicly as official | Big "NAMUNA" badge plus a real verified example once one exists (spec v2 proof point), or drop the chips. |
| p.4 / p.10 / p.15 / p.28 | **Yig'imlar 310 000 "Rasmiy"**, base "[asos]" | [NOSRC] | VM 55 Annex 1 (box copy) bands for an ordinary BYD start at 1 BHM; 1 BHM = 440,000 UZS from 1 Sep 2026 (PF-115). 310,000 doesn't fit any band. | Get it from the engine: band + BHM multiplier + BHM row, each with its source. |
| p.10 Landed cost | **QQS "Rasmiy"** on a base that includes ≈ freight; label "(bojxona qiymati + boj) × 12 %" | [NOSRC] | Amount is an estimate. **Label leaves out excise** (spec: 12% × (CV + duty + excise)). | ≈ chip on the amount. Formula label from the engine template including excise. |
| p.10 | Boj "Rasmiy jadval · 01.11.2026" on ≈ 54.8M customs value | [NOSRC] | Same: estimated base | Rate chip Rasmiy, amount chip ≈ |
| p.10 | **Transport "YuklaGo taxmini, rasmiy emas" ≈ 6 200 000** (412 kg, by truck) | [NOSRC][LLM$ risk] | We have no freight rate source. An LLM-made estimate would be an LLM-computed money figure. | User enters a forwarder or kargo quote. Otherwise show "—", mark the total "to'liq emas", and show the total without freight. |
| p.10 | FX "MB kursi · 01.10.2026" next to rates "01.11.2026", screen dated 18.11 | [NOSRC] | One calc must use one `as_of` (Art. 326: CBU rate on the acceptance day) | Engine stamps one date for FX and rates. Estimates use today's CBU rate, labelled. |
| p.10 / p.14 | Alternative **"9405 42 xxx x … 15 % … + 3 068 800"**; "8539 xx xxx x" | [NOSRC][HARD] | A partial code can't be validated or rated. Spec v2 Y10 allows only official-list codes. | Show only validated 10-digit candidates. The engine computes the delta. Otherwise: "boshqa kod bo'lishi mumkin — mutaxassis". |
| p.10/11 Kargo | "Kargo bilan (tovar + $1 854)" 72 053 100 | [OK] | Fine if it comes from the user's quote and is computed by the engine | `kargo` block in calc v0.3. |
| p.8 New shipment | **"Mahsulot havolasi — 1688, Alibaba, Trendyol… sahifadagi nom, narx… o'qiymiz"** | [HARD] | Marketplaces use login walls, anti-bot checks, JS rendering and ToS limits. Scraping is brittle and blocking. | MVP: **screenshot or photo of the listing** → extraction, or pasted text. Link as best effort later. |
| p.6 Path + readiness | Placeholders: ERI issuer, specialist conditions, "3 savol" rules | [LEGAL] | Needs official sources | Huquq supplies text + URLs (§3). Readiness stays self-declared ("siz belgiladingiz"). |
| p.5 / p.27 Login, 2FA | SMS OTP | [HARD-ish] | Needs a UZ SMS gateway contract | Demo: fixed OTP for seeded users. Provider choice TODO. |
| p.7 Home | "Manba: [qonun moddasi]", "1 tasining stavkasi o'zgargan bo'lishi mumkin" | [OK] | Article from the deadlines contract. Alert = ruleset diff on our own loads. | Wording "YuklaGo jadvali yangilandi". |
| p.9 Deadlines | 13.11 → "tugaydi 27.11" (9 days left on 18.11) | [LEGAL] | Day-counting rule not confirmed. Mobile mock uses +15 (10.11 → 25.11). | `countingRule` from Huquq. Server computes. UI shows the rule text. |
| p.9 | "Eslatma … **SMS va Telegram** orqali" | [HARD] | Telegram is out of v2 scope. SMS needs a gateway. | Web push (PWA) now. SMS later. |
| p.12 Go/no-go | "**Rasmiy ro'yxat · 01.11.2026**" + **"Topilmadi"** for Single Window, prohibitions, Asl Belgisi | [LEGAL][NOSRC] | We have no machine-readable official lists (customs.uz/singlewindow is JS-rendered and wasn't fully read). "Not found" is a claim we can't back. | A per-code checklist curated by the specialist with source + check date. Unchecked → "**Tekshirilmagan** — mutaxassis/broker", never "Topilmadi". |
| p.12 | "Guruh ro'yxati o'zgarsa, sizga xabar beramiz" | [LEGAL] | Implies we monitor an official feed | "Jadvalimizni yangilaganda qayta tekshiramiz." |
| p.12 | Certificate "amal qiladi 2027-yil martgacha" | [OK] | Read from the uploaded file; we can't verify it against a registry | Chip "Hujjatdan o'qildi", not "Rasmiy". |
| p.13 Documents | Side-by-side, bbox, handwritten low-confidence, translation toggle | [OK] | — | Translation display only (§1.1). |
| p.14 TIF TN | "Rasmiy nomi: [TIF TN ro'yxatidagi matn]" | [NOSRC] | Needs the official list text (PQ-181 Annex 1, not available as text on lex.uz) | §3 data ask #1. |
| p.14 | "Qanchalik ishonchli: **Yuqori**" | [HARD] | LLM self-confidence isn't calibrated | Deterministic signals (§1.2). No "Yuqori" before the gold set. |
| p.14 | "Bu kod amaldagi rasmiy ro'yxatda yo'q… Eng yaqin: 8539 51…, 8539 52…" | [OK] | Prefix search on `tn_codes` | — |
| p.15 Payments + draft | Grafa 45 "54800000,00" (UZS) | [LEGAL] | Instruction No. 2773 (box copy): grafa 45 right box = customs value **in contract currency** | Ustoz confirms the grafa 45/46/47 formats (§3). |
| p.15 / p.21 | Grafa 46 "4332,02" | [NOSRC] | Instruction No. 2773: grafa 46 = value **in thousands of USD, rounded to 3 decimals, at the CBU rate on the acceptance day** → about "4,332" | Formatter per mapping. Ustoz confirms. |
| p.15 | "48 maydon" fixed | [HARD] | Field count depends on the regime, number of goods lines and the real form | Count comes from the mapping. |
| p.17 Cabinet choice | Real: "ed2.customs.uz · YuklaGo Desktop orqali — hozircha yoqilmagan" | [ED2][OK] | Correctly disabled | Keep disabled until Huquq signs off. |
| p.17 | Step "1 · YuklaGo kabinet sahifasini **shu oynada** ochadi" | [ED2][HARD] | Impossible in the web app for real ed2 (XFO/CSP, checked) | Web = mock only. Real = desktop or extension. Copy-assist works anywhere. |
| p.19–20 Running / paused | Read-back, pause when the user clicks in the cabinet, diff "Siz 31-grafani o'zgartirdingiz" | [OK] in mock/extension/Electron, [HARD] for custom widgets | Content script/preload can see `isTrusted` input events. Custom selects and datepickers in real ed2 are unknown. | Mapping types per widget. Fail closed. |
| **p.21 ERI hand-off (mock)** | Mock sign dialog with **"Kalit paroli"** input + "test kaliti" | **[ERI]** | `mashq.yuklago.uz` is **our** domain. A password field there contradicts "YuklaGo'da parol maydoni yo'q" and teaches users to type their ERI PIN into a YuklaGo page. | Mock dialog = "Simulyatsiya: imzolash" button only, **no text input**, banner "Haqiqiy ERI ishlatilmaydi". |
| p.21 / p.23 | "Imzoladim — sessiyani yakunlash" | [OK] | Self-reported | Stored as `user_marked_signed_at`. |
| p.22 Failure | Tally, "Sahifani qayta o'qib urinish", "qisman qoralamani qanday o'chirish" | [OK] / [LEGAL] | How to delete a partial draft in real ed2 is unknown | Ustoz supplies the steps. Mock has a delete button. |
| p.23 Session record | "**Siz ERI bilan kirdingiz**"; "**Kabinet ko'rsatgan raqam … sahifadan o'qildi**" | [ED2][HARD] | In real ed2 we can only *infer* login from navigation. Reading the registration number from the live page is an automatic status read, which spec v2 §6.14 treats as a separate legal decision. | Real mode: "kirish sahifasidan o'tildi (taxminan)". The user types or pastes the number. Mock may read it. |
| p.23 / p.27 | Field values + journal "CSV/PDF", "Yordam xizmatiga ulashish" | [HARD] (privacy) | Values are commercial/personal data | Server keeps hashes and events. Values stay local unless the user exports or shares them. |
| p.24 After submission | Reply-explainer with specific grafa fix "44-grafaga qo'shamiz" | [OK] if library-driven | An LLM free-reading official messages can invent meanings | Library match first. LLM paraphrase only (§1.9). Keep the "taxminiy talqin" disclaimer (already drawn). |
| p.25 Library | Partial codes "9401 xx xxx x"; "01.11.2026 da **rasmiy** stavkalar jadvali yangilandi" | [NOSRC][LEGAL] | See §1.6 | Full codes. "YuklaGo jadvali" wording. |
| p.26 Broker hand-off | Send to the broker's phone/email; secure link 7 days | [OK] / [HARD-ish] | SMS/email provider; consent for sharing personal data | Demo: copy link. Consent tick. |
| p.27 Settings | "Bu yerda kalit, parol yoki sertifikat yuklash joyi yo'q" | [OK] | Matches spec | Server also rejects key MIME types (ARCH §8). |
| p.28 Mobile | Filling disabled on the phone; "send link to computer"; push when a session starts | [OK] | PWA push | — |
| Mobile UI (built), `/imtiyoz` | **"Variant B · Qozog'iston + ST-1"**, "Xitoy va Qozog'istonni solishtirish" | **[LEGAL]** | Spec v2 §11 explicitly forbids this routing frame | Replace with the Y5 entitlement check ("tovaringiz allaqachon mos keladimi?"). |
| Mobile UI mocks | Fee example at 10,000 USD with "chegarada 1 BHM" | [LEGAL] | Spec v2: use a value inside the band | Use 9,500 USD. |

**Nothing in the design has the LLM computing payments directly.** The risks are mislabelled provenance and the freight "YuklaGo taxmini". **No screen stores ERI**, except the mock password field above, which must go. **Real ed2 is correctly shown as disabled.**

---

## 3. Data we need from the customs experts (ordered by build priority)

Owners: **TN** = TIF TN va Bojxona To'lovlari Mutaxassisi · **HQ** = Bojxona Huquq va IT Integratsiya · **DU** = Bojxona Deklarant Ustoz.
Deadlines are my proposal for a demo on 19 Nov (Tashkent time). Delivery: files in `/workspace/yuklago/data/expert/` (CSV in UTF-8, plus screenshots or PDF extracts). Every row has `source_act`, `source_url`, `clause/row`, `valid_from`, `checked_by`, `checked_at`, `status (verified|sample)`.

### P0 — needed by **18 Nov 11:00** (blocks the engine and the demo)

| # | Owner | What | Format | Notes / open questions |
| --- | --- | --- | --- | --- |
| 1 | TN | **5–10 demo goods with full 10-digit TIF TN codes** + official name (UZ/RU) + unit/supplementary unit + edition. Include: the design's LED bulb (8539 52 000 0?) and its real alternative codes; one "needs conformity certificate" item; one controlled item for the escalation path (design uses a drone); optionally one excisable item. | `tn_codes.csv` | Confirm which TN edition is in force on 18.11.2026 and whether HS-2027 changes are expected from 1 Jan 2027 (PQ-181 cl. 5). |
| 2 | TN | **Duty row for each demo code**: rate type (ad valorem / specific / combined), %, specific amount + currency + unit, combined rule, exceptions, act + annex + row (PQ-3818 Annex 1 as restated by PQ-181 Annex 2, plus any later change). **One dated NOTARIF screenshot per code.** | `duty_rates.csv` + `notarif/<code>_<date>.png` | The engine refuses any code without a row. |
| 3 | TN | **VM 55 fee rules**: (a) boundary rule at 10k/20k/40k/60k/100k/200k/500k/1M USD; (b) which rate and date convert the customs value to USD for the band; (c) whether the band applies to **export** BYD; (d) **20% preliminary-declaration discount**: is it in the current text, and may we show it? (e) "fee charged once" for preliminary/incomplete/periodic declarations; (f) fee is per declaration, not per line. | `fee_rules.md` + lex.uz extract with edition date | Box copy (`/workspace/bojxona/fee.txt`, VM 700 edition, in force 8 Feb 2026) contains the 20% and once-only footnotes. Spec v2 says don't publish the discount. Needs a ruling. |
| 4 | TN | **BHM**: confirm 440,000 UZS from 01.09.2026 (PF-115). Earlier value only if back-dating. | row in `bhm.csv` | — |
| 5 | TN | **VAT and rounding**: confirm 12% × (CV + duty + excise) for IM40; whether anything else enters the base; **rounding rule** (per line or per declaration; so'm or tiyin; half-up?); VAT exemptions for demo codes. | `vat_rules.md` | Engine currently rounds to whole so'm, half-up, as a placeholder. |
| 6 | TN | **Excise**: the act that sets excise on imports, and rows for any demo code, or a written "none of the demo codes is excisable". | `excise_rates.csv` | Spec v2: no excise line is "verified" until the act is named. |
| 7 | TN | **Customs value add-backs**: per Incoterm (EXW/FOB/CFR/CIF/CIP/DAP), what to add up to the UZ border; how to split freight across lines (by weight or by value); which date and rate convert freight invoices. | `valuation_rules.md` | Arts. 303–313, VM 160. |
| 8 | HQ | **Deadline rules**: per clock — start event, length, unit (calendar/working/hours), **whether the start day counts**, end-of-day rule, article/clause, URL, consequence text (UZ). Clocks: Art. 261 (15 days), Art. 85 (60/10), Art. 262 (30), Art. 206 (1h/2h), Art. 266 (3 years), VM 605 cl. 11 (export), Art. 248 (release times). Holiday calendar source. | `deadline_rules.csv` | Resolves design 13.11 → 27.11 vs mobile mock 10.11 → 25.11. |
| 9 | DU | **IM40 grafa map**: every grafa/box we fill, its format per **Instruction No. 2773** (current edition), which document field it comes from, required Y/N, example. Single-line and multi-line. | `grafa_map_IM40.csv` | Specifically confirm grafa 45 currency, grafa 46 (thousands of USD, 3 decimals), grafa 47 (fees on item 1), grafa 33 (10 digits, no spaces), grafa 34 (numeric country code). |
| 10 | DU | **3 synthetic document sets** (no real companies): invoice (ZH/EN), packing list (EN), CMR (RU/EN), contract (RU), warehouse acceptance act. Set A clean; set B with deliberate mismatches (weight, packages, seller name, missing contract no.); set C controlled goods. Each with an **answer key**. | PDF/JPG + `answers_<set>.json` | Drives the extraction demo and check tests. |
| 11 | DU | **Cross-check rules + tolerances**: weight tolerance, package-count rule, name-matching rule, which findings **block** vs **warn**, the VM 605 Annex 1a minimum-field list as practice sees it. | `check_rules.csv` (`rule_id, docs, field, tolerance, severity, message_uz, message_ru`) | ARCH §6.1 has the draft list. |
| 12 | HQ | **Approved public wording**: landing "what we do / don't do", ERI statements, "we found no public filing API", the responsibility tick text, the mock banner. | `copy_legal_uz_ru.md` | Design copy is close. Needs a sign-off. |

### P1 — by **18 Nov 16:00** (makes the demo honest end-to-end)

| # | Owner | What | Format |
| --- | --- | --- | --- |
| 13 | TN + DU | **Go/no-go per demo code**: required conformity certificate (issuing body), Single Window permit types, **Asl Belgisi** membership, prohibitions/licences, each with source URL + check date. Anything not checked gets marked "not checked". | `requirement_rules.csv` |
| 14 | DU | **ed2 status / rejection messages**: real redacted examples (text or screenshot) with meaning and next step, grafa refs. No invented codes. Also: how a partially filled ed2 draft is deleted or resumed. | `status_messages.csv` + `screens/` |
| 15 | HQ | **Readiness and router facts**: where a company gets a customs ERI (issuer, URL); how to register an authorised specialist in the foreign-trade participant cabinet; personal parcel vs passenger vs commercial criteria; whether a non-entrepreneur may file commercially. | `onboarding_facts.md` |
| 16 | DU | **Escalation triggers (Y18)**: the list of conditions where we recommend a broker. | `escalation_rules.csv` |
| 17 | TN | **TN clarifying questions** for each demo heading (e.g. lamp with or without a fitting/housing). | `tn_questions.csv` |
| 18 | DU | **One real accepted declaration, redacted**, with its payment block. The proof point: reproduce it to the so'm. | PDF, redacted |
| 19 | HQ | **E-kontrakt / bank checklist** text + URLs + what is mandatory. | `checklist_items.csv` |

### P2 — post-hackathon (needed for a real product)

| # | Owner | What |
| --- | --- | --- |
| 20 | TN | Full machine-readable TIF TN list (PQ-181 Annex 1) + edition plan for HS-2027 |
| 21 | TN | Full duty table with review workflow; combined-rate rules |
| 22 | TN | Preference entitlement rules (CIS FTA / ST-1 conditions by origin) — entitlement only |
| 23 | TN | Gold set of 30–50 labelled goods for TN suggestion metrics |
| 24 | HQ | Ruling on automating ed2 (portal terms, computer-misuse rules); **only after that** may real ed2 selectors be recorded, in the owner's own session (`mappings/ed2-real.TODO.json`) |
| 25 | HQ | Is paid preparation "broker activity" (Arts. 274, 277–281; VM 847)? |
| 26 | HQ + Security | ZRU-1125 official Uzbek text; whether the adequacy list / standard clauses exist; LLM provider terms |
| 27 | Research | Kargo reality from interviews (no invented rates) |

---

## 4. Gaps and contradictions (spec v2 ↔ design v0.1 ↔ ARCHITECTURE.md ↔ built code)

| # | Item | Where | Resolution proposed |
| --- | --- | --- | --- |
| G1 | **Desktop app vs browser extension.** Spec v2 says the desktop app embeds a browser. The existing filler is an MV3 extension + Playwright runner. The design says "YuklaGo Desktop". | spec §8.1 vs `autofill/` vs design p.17 | Keep one engine. Demo = web + mock. Desktop = Electron (later). Extension = fallback. **Needs PO choice.** |
| G2 | **LLM scope widened** (classification, reply-explainer, translation, supplier text) vs the PO rule "LLM only for OCR + TN" | spec §8.4 vs PO constraint | Allow it with the "no new numbers" guard and library-first explainer. **Needs PO confirmation.** |
| G3 | **20% preliminary discount**: engine has it (law text on the box has it); spec v2 says don't publish | ARCH §4.3 step 7 vs spec §8.5/§11 | Flag off by default until TN rules (P0 #3). |
| G4 | **Worked example** 10,000 USD (ARCH T1, mobile mocks) vs 9,500 USD (spec v2) | ARCH §4.5, `mocks/calc.ts` | Switch to 9,500. Keep 10,000 as a boundary-warning test. |
| G5 | **Mobile UI "Kazakhstan + ST-1" variant** contradicts spec v2 §5/§11 | `apps/web-mobile-ui/src/mocks/calc.ts`, `/imtiyoz` | Remove. Replace with the entitlement screen (design p.11). |
| G6 | **Deadline counting**: design 13.11 → 27.11 vs mobile mock 10.11 → 25.11 | design p.9 vs `mocks/deadline.ts` | P0 #8. Add `countingRule` to the contract. |
| G7 | **Provenance**: contract has `sample|verified`; design has 6 chips; no null value for "Stavka topilmadi" | `calc.ts` v0.2 vs design p.1 | calc v0.3 (§1.3). |
| G8 | **Freight estimate**: design has "YuklaGo taxmini"; ARCH says user input only; spec v2 says "freight labelled an estimate" without saying where it comes from | design p.10 vs ARCH §10.13 vs spec §6.3 | User quote or "—". No YuklaGo freight model until a sourced table exists. |
| G9 | **Mock domain and status flow**: ARCH `demo-ed2.yuklago.uz` + webhook status; design `mashq.yuklago.uz` + user-marked status; spec v2 "no fake feed" | ARCH §9 vs design p.17/24 vs spec Y19 | Use `mashq.yuklago.uz`, user-marked status, no webhook. |
| G10 | **Mock sign dialog password field** vs "YuklaGo has no password field anywhere" | design p.21 vs design rationale §4 / spec Y16 | Remove the field (§2). |
| G11 | **Notifications**: design says SMS + Telegram; spec v2 drops Telegram as a surface; ARCH says web push + email | design p.9 vs spec §8.1 | Web push now. SMS later. No Telegram. |
| G12 | **Auth**: design SMS OTP + SMS 2FA; ARCH email magic link | design p.5/p.27 vs ARCH §1 | SMS OTP (fits users); fixed OTP for the demo; choose a provider. |
| G13 | **Handoff format**: `handoff.v1` uses float money; calc uses decimal strings; no provenance per field | `autofill/samples/handoff.sample.json` vs `calc.ts` | handoff v2 (§1.7). |
| G14 | **Contract version label**: mobile README says schemas v0.1; files say v0.2. README's deadlines example `warnings` lacks the required `severity`/`titleUz`. | `apps/web-mobile-ui/README.md` vs `deadlines.ts` | Fix the README; validate mocks with Zod in CI. |
| G15 | **Single `fx` object** vs multi-currency (CNY invoice + USD kargo/freight) | `calc.ts` v0.2 vs design p.10–11 | `fx: Cited[]`. |
| G16 | **Go/no-go "Topilmadi · Rasmiy ro'yxat"** vs spec v2 Y7 ("maintain official lists; do not invent") and no list source on hand | design p.12 vs spec §8.5 | "Tekshirilmagan" state (§2). |
| G17 | **Grafa formats** (45 currency, 46 thousands of USD / 3 decimals) differ from Instruction No. 2773 | design p.15/p.21 | DU P0 #9. |
| G18 | **Reading the registration number from the cabinet page** vs spec v2 "automatic status read is a separate legal decision" | design p.23 vs spec §6.14 | Mock only; real = user enters it. |
| G19 | **Library "rasmiy jadval yangilandi"** implies an official feed; we only have our own loads | design p.25 vs spec Y20 | Wording fix. |
| G20 | **Clients**: spec v2 says a "mobile app"; built code is a PWA | spec §8.1 vs `apps/web-mobile-ui` | PWA for now. A native app only if push or camera limits bite (TODO). |
| G21 | **Design placeholders** `[v2 spec, …]` for deadlines, ERI issuer, E-kontrakt, permit lists, export steps, but spec v2 itself doesn't contain those facts | design rationale §6 vs spec v2 | Filled by the expert data asks P0 #8 and P1 #13/15/19. The spec can't fill them. |
| G22 | **"48 maydon"** and grafa list hard-coded in the design; spec v2 wants versioned mappings that fail visibly | design p.15/17 vs spec §8.2 | Count and labels come from `grafa_mappings`. |

---

### Pointers
- Architecture baseline: `/workspace/yuklago/ARCHITECTURE.md` (§1 stack, §3 tables, §4 engine + tests, §5 extraction/TN, §6 checks/deadlines/pack, §7 data sources, §8 security/localisation, §9 mock).
- Contracts: `/workspace/yuklago/packages/schemas/src/calc.ts`, `deadlines.ts` (v0.2). Proposed v0.3 deltas: §1.3 and §1.5 above.
- Filler prototype: `/workspace/yuklago/autofill/` (README, `extension/lib/filler.js`, `mappings/`).
- Law copies on the box: `/workspace/bojxona/fee.txt` (VM 55), `bk_clean.txt` (Customs Code), `y2773.txt` (BYD fill-in instruction).

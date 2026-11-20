# Deklarant check of spec v3: signer, export and grafa sections, DEC-16/26, DEC-17, DEC-18, plus Q-6 and PE-22

**Reviewer:** Bojxona Deklarant Ustoz.

**When:** written 18.11.2026, about 04:10 Tashkent time (UTC+5). It is checked against `yuklago-spec-v3.md` as it stood at 04:06; the PM was still editing it, and DEC-23 to DEC-26 had appeared by then.

**What I checked it against:**
- `team-review/answers-declarant.md` (AD) and `team-review/declarant.md` (D);
- `data/declarant/` (README, including the Hakathon CEO decisions of 04:00; `grafa-map.json`, `deadlines.md`, `tolerances.md`, demo-sets);
- the tariff expert's grafa list: `team-review/tariff-payments.md` §3 item 8. There is **no** separate grafa file in `data/tariff/` (`rules.md` only mentions grafa 31 for IMEI);
- the lex.uz text of **Instruction 2773** (Uzbek Cyrillic, edition including 2773-15 of 22.07.2026), saved on the box as `/workspace/bojxona/y2773.txt`, plus the Annex 1 and Annex 2 form images.

**Labels:**
- **Verdict:** OK or FIX.
- **Status tags:** [SOURCED], [UNVERIFIED], [INFERENCE] and [PRACTICE] mean the same as in AD.
- No login, no submit and no outside contact was made.

---

## A. Signer section (§3.1, Y1, PC-5)

| ID | Verdict | Finding / concrete fix | Source |
|---|---|---|---|
| R1 | OK | VMQ 605 cl. 1 replaces PF-5414. Keep the repeal-date flag. | VMQ 605 https://lex.uz/uz/docs/-3844549 |
| R2 | OK | Liability split matches cl. 30 (VMQ 700 edition). | VMQ 605 cl. 28, 30 |
| R3 | OK | The three signer types, the ed1 list with an authority period, and the PoA and YaTT-employee flags all match AD §1. | VMQ 605 cl. 2, 15; Customs Code (BK) 284; my.gov.uz/uz/service/207 |
| R34 / R35 | OK | Nothing to add. EK10 via ed2 stays [UNVERIFIED] (PC-6). | VMQ 348; ed2 and ed1 live pages |
| R38 | OK | Broker rules (VMQ 847, ZRU-701 20 BHM fine) are correct. | VMQ 847 https://lex.uz/docs/-7274716 |
| AC-1.5 | **FIX (Uzbek)** | "roʻyxatiga **qoʻshgan** shaxs" means "the person **who added**". Use **"deklaratsiyalovchi shaxslar roʻyxatiga kiritilgan shaxs"**. | VMQ 605 cl. 15 wording ("roʻyxatga kiritadi") |
| Y1 (new AC-1.6) | **FIX (add)** | When the signer is a broker's specialist, the checklist must confirm that the **broker has notified the Customs Committee** (VMQ 847) and that the broker, not the user, has listed its specialist in ed1. Interim: the user ticks "broker xabarnomasi bor" and uploads the broker contract. **[UNVERIFIED]** whether there is a public broker register URL, so do not show one. | VMQ 605 cl. 15 stage 2; VMQ 847; BK 277 |
| DEC-23 vs signing (Q-7) | **FIX (add risk)** | The embedded ed2 window in the desktop app must still let the **E-IMZO client on the user's PC** sign. ed2 loads `e-imzo-client.js`. **[UNVERIFIED]** that signing works inside a Tauri or Electron webview (local E-IMZO service, origin/API-key checks). Add an acceptance criterion to Y14/Y16: "signing in the embedded window tested in the Q-6 session; if it fails, fall back to the system browser." | ed2 live page (E-IMZO: PFX, USB-TOKEN, BAIK-TOKEN) |

## B. Export section (R60, R62, R67–R72, Y21, §4.2)

| ID | Verdict | Finding / concrete fix | Source |
|---|---|---|---|
| R62 (EK10 part) | OK | Matches AD §5. | AD §5 |
| R67 / R69 / R70 / R72 / R60 | OK | Match AD §2 and keep its flags (phyto fee, 30/15-day law text, origin fee, Türkiye form, export duty, consolidated currency-law edition). R70 is confirmed by the VMQ 163 text: cl. 6 (invoice-based export), cl. 11 (automatic register), cl. 12 (100 % prepayment). | VMQ 163 https://lex.uz/uz/docs/-4213596 (PF-174 edition of 01.09.2026) |
| R68 | OK | It correctly says [UNVERIFIED] per AD. I have still not re-read VMQ 148. | — |
| **§4.2 A4, AC-12.4, flag `EK10_GRAFA43_CODES`, Q-12** | **FIX: flag can be cleared** | **EK10 grafa 43 is now read:** "**0**" means the consignor exports goods it **did not produce itself**; "**1**" means it exports goods it **produced itself**. Replace AC-12.4 with: "EK10 grafa 43 = 0 (not own production) / 1 (own production); user answers 'Bu tovarni oʻzingiz ishlab chiqarganmisiz?'". Delete the flag row. Remove "grafa 43 blocked" from A4. | Instruction 2773 ch. 4, cl. 22 sub-point 38 https://lex.uz/uz/docs/2924955#2925893 [SOURCED] |
| Y21 / EK10 draft (new AC-21.5) | **FIX (add)** | The EK10 draft must use the **EK10 list (cl. 21)**, not the IM40 list (cl. 24). The EK10 list **has 17 and 17a** and **lacks 15, 15a and 21**: 1, 2, 3, 5, 7 (post code), 8, 9, 11, 12, 13, 14, 17, 17a, 18, 19, 20, 22–26, 28–35, 37–50, 54, С. Grafa 36 is absent here too. Build `grafa-map-ek10.json` from cl. 21–22 before the Y21 demo. | Instruction 2773 cl. 21 https://lex.uz/uz/docs/2924955#4294922 [SOURCED] |
| Y21 AC-21.2 | OK | Filing target cargo.customs.uz; export duty shown as "rasmiy stavka topilmadi". | ed1 service list; BK 290 |

## C. Grafa section (R32, Y12, PC-12, R33) and **DEC-16 / DEC-26: grafa 36 and 43**

### C.1 The two readings

- **Deklarant map** (`grafa-map.json`, used by the PM in DEC-16, confirmed by DEC-26):
  - grafa 36 is not filled for IM40; preferences go to grafa 44 as code "6…";
  - grafa 43 = 0/1 "own needs".
- **Tariff expert** (`tariff-payments.md` §3 item 8): "36 (imtiyoz)", "43 (qiymat usuli)". It is marked by the tariff expert themselves as "⚠️ grafa numbers from the standard BYD structure, to be confirmed with the declarant". There is no other tariff version in `data/tariff/`.

### C.2 Evidence from Instruction 2773 [SOURCED unless tagged]

1. **The IM40 list of grafas the declaring person fills** (cl. 24) is 1, 2, 3, 5, 7, 8, 9, 11, 12, 13, 14, 15, 15a, 18–26, 28–35, **37**–50, 54, С. **36 is not in it.** The EK10 list (cl. 21) does not have 36 either, nor does the cl. 76 list. https://lex.uz/uz/docs/2924955#4304434
2. **The Instruction has no filling rule for grafa 36 at all.** A full-text search of the 7,295-line dump for "36-графа" finds nothing. Customs itself fills only 7, 44, 47, A, B and D (cl. 89).
3. **Grafa 43 for IM40** (cl. 25 sub-point 38): "**0**" if the consignee imports goods not intended for its own needs; "**1**" if they are for its own needs. https://lex.uz/uz/docs/2924955#2926926
4. **Exemptions and preferences are declared in grafa 44.** The code is "6", then the payment-type code (Annex 13), then the basis act (Annex 14) (cl. 25 sub-point 39 item "е"). Example in the map: `629 15-142120030000`.
5. **The valuation method has a document code in Annex 12:** row 113, **code 904, letter code "МЕТОД", "Божхона қийматини аниқлаш усули"**. Codes 902/903 are for method 6 on the basis of method 4. So the valuation method is reported in **grafa 44** (code 904) [INFERENCE from the classifier; the Instruction does not say which grafa uses 904]. It is **not** in grafa 43.
6. **Why the other reading exists:** the **paper form image in Annex 1** (BD-1 main sheet, https://lex.uz/uz/files/4624421) still prints a box **"36 Преференция"** and an **unlabelled box 43**. "36 = preference, 43 = valuation-method code" is the EAEU / Russian DT convention [INFERENCE from general knowledge, not checked on an official EAEU source]. The Uzbek Instruction gives 43 a different meaning and gives 36 no rule.

**Decision:**
- **The Deklarant map is right; DEC-16 and DEC-26 stand.**
- The tariff list is closed. It also has a smaller slip: "**16** (kelib chiqish mamlakati)" is **not** in the IM40 list. For IM40, origin goes per item in **grafa 34**; 16 and 17 are not filled for IM40 (`not_filled_by_declarant_for_im40`).

### C.3 Fixes

| ID | Verdict | Concrete fix | Source |
|---|---|---|---|
| DEC-16 / DEC-26 | OK | Add the evidence line: "2773 cl. 24 (no 36); cl. 25 sub-point 38 (43 = 0/1); no fill rule for 36 anywhere; preferences 44/'6'; valuation method Annex 12 code 904; the paper form still prints box 36, so leave it empty". | as above |
| R32 | **FIX (add)** | (a) The valuation method goes in **grafa 44, code 904 "МЕТОД"** [INFERENCE]. The payment engine must never write the method into grafa 43. Add 904 to the grafa-44 code list in `grafa-map.json`. (b) Note "16, 17 not filled for IM40; origin = 34". (c) The grafa-45 ⚠️ (left subfield "may hold the method") is now partly answered: the Instruction places the method in 44/904. Whether ed2's 45 left subfield also asks for it stays [UNVERIFIED] (Q-6). | 2773 Annex 12 row 113; cl. 24 |
| `tariff-payments.md` §3 item 8 | **FIX** (owner: TIF TN) | Replace with: "12, 22, 23, 31, 33, 34, 41, 42, 44 (6xx preferences, 904 method), 45, 46, 47 — per `data/declarant/grafa-map.json`". | — |
| AC-12.2 | OK | Make it stronger: "Grafa 36 is empty in IM40 and EK10 drafts; if live ed2 shows a 36 field, YuklaGo leaves it empty unless Q-6 shows it is required". | 2773 cl. 21, 24 |
| R33 | **FIX** | Edition: the Instruction now includes amendment **2773-15 of 22.07.2026** (README; the lex.uz page shows ONDATE 22.07.2026 links). Change "2773-13, 2773-14" to "2773-15 (22.07.2026); re-check before release". | https://lex.uz/uz/docs/2924955 |
| PC-12 | OK | Grafas 13/33/36/41/45/47 stay flagged until Q-6. I would also add grafa **44 (904 entry UI)** to the list. | — |

## D. DEC-17: deadlines (R6, Y8, `deadlines.md`)

| ID | Verdict | Finding / concrete fix | Source |
|---|---|---|---|
| DEC-17 / R6 / AC-8.1 | OK | The arithmetic is right: with presentation day = day 1, day 15 = D + 14 (the "File by" date). With the Civil Code art. 146 reading, the last day is D + 15 (the "Legal max" date). The shift goes to the **customs body's** next working day, which BK 261 part 2 allows. The `deadlines.md` examples (12.11 → 26.11 / 27.11; 21.11 Sat → 07.12 / 07.12) check out. | BK 261 https://lex.uz/docs/2876354; CC 146, 148 https://lex.uz/docs/111181 |
| AC-8.1b (DEC-20) | **FIX (clarify)** | "Earlier date" should be defined as **raw D + 14 with no non-working-day shift** when the post calendar is unverified. The calendar is the thing we cannot trust, so the shift must not be applied. | DEC-20 |
| AC-8.1 (end of day) | **FIX (add)** | Say what "by" means: until the **end of the post's working hours** on the last day. This is the Civil Code art. 148 analogy, [UNVERIFIED] for customs. ed2 accepts uploads at any time, but **registration and acceptance** depend on the post. The UI must not say "until 24:00". | CC 148; VMQ 605 cl. 15 |
| AC-8.1c (ops calendar) | **FIX (add)** | Seed data must include the public holidays in the remaining window. Example: **8 December 2026 (Constitution Day, Tuesday)**. **[UNVERIFIED]** the exact article in the Labour Code that lists holidays, and any 2026–2027 rest-day transfer decrees. Ops must cite each decree it enters; an entry without a source is rejected (as AC-8.1c already says). | DEC-20 |
| AC-8.4 | OK | 3 BHM fine (MJtK 227¹⁰ part 2); the "≤ 2 working days" threshold is [PRACTICE]. Label it so. | MJtK https://lex.uz/uz/docs/-97664 |
| PC-13 | OK | MJtK editions dated 30.12.2026 and 05.02.2027: re-check before each date. | lex.uz MJtK page |

## E. DEC-18: tolerances (Y13, `tolerances.*`)

| ID | Verdict | Finding / concrete fix | Source |
|---|---|---|---|
| DEC-18 label | OK | No numeric tolerance exists in BK, Instruction 2773 or VMQ 605 (`tolerances.md` bottom line). "PROPOSAL, not law" / "Taklif, qonun emas" is the honest label. | as in tolerances.md |
| AC-13.1a (gross) | **FIX (align)** | The data has **three** tiers: ≤ 1 kg = info; ≤ max(1 %, 20 kg) = warning; beyond = block. The spec lists only two. Add the info tier, or delete it from the JSON, so the spec and data match. | `tolerances.json` gross_weight_docs |
| AC-13.1a (net) | **FIX (data)** | `net_weight_docs` gives `warning_if_rel_le_pct=0.5, warning_if_abs_le_kg=5` but **no combine rule**. Add `"rule": "diff ≤ max(0.5 %, 5 kg) → warning; otherwise blocking"` as for gross. Otherwise engineering may implement min(). | `tolerances.json` |
| AC-13.1a (meaning) | **FIX (add copy)** | Tolerances only compare **documents with each other**. The BYUD itself carries **one** value per item (35 gross, 38 net), taken from the chosen source document. A warning never means "customs will accept a difference". The declaring person answers for the TED data (VMQ 605 cl. 30), and misdeclaration is fined (MJtK 227²²). Add a line to the warning: "Deklaratsiyaga bitta qiymat yoziladi — qaysi hujjatdan olinganini tanlang." | VMQ 605 cl. 30; MJtK 227²² |
| Grafa 35 definition (pallets) | **FIX (add help)** | Gross = goods **with all packaging needed to keep them unchanged until put into circulation, excluding containers and other transport equipment**. Show this in the gross-weight warning. Whether **pallets** count as packaging or as transport equipment stays [UNVERIFIED] (README open question 6). | 2773 cl. 25 sub-point 30 [SOURCED] |
| AC-13.1b | OK | Admin changes are logged and the label stays. | DEC-18 |
| DEC-19 (freight split) | OK | BK 304 requires freight to the border to be added to the customs value. No official rule for splitting it between items was found. A gross-weight default with a value option, logged in the audit pack, is a product choice and is labelled so (`FREIGHT_ALLOCATION_METHOD`). | BK 304 |

## F. Other spec items I noticed

| ID | Verdict | Fix | Source |
|---|---|---|---|
| Y19 title, AC-19.1, changelog | **FIX** | The library in AD §7 has **44** messages, not 43: S01–S11 (11), R01–R15 + R99 (16), D01–D09 (9), M01–M08 (8). My earlier summary said 43; that was my counting error. | AD §7 |
| Y18 triggers | **FIX (scope)** | Since DEC-13 the special regimes are in scope (Y22). Reword the trigger "regime not IM40/EK10" to "**regime not yet implemented in Y22, or not verified**". | AD §6; DEC-13 |
| R62 IM40 list | OK | Matches AD §5. | AD §5 |

---

## G. Q-6: live check of grafas 13/33/36/41/45/47 on ed2.customs.uz

### What is blocking it

ed2 has **no anonymous or demo login**. Every login method is E-IMZO: PFX file, USB-TOKEN or BAIK-TOKEN. So the session needs a **real ERI key held by a person who may file for a real foreign-trade participant**.

**We have no such person or key.** No team member has:
- a company with E-IMZO;
- a listing in any ed1 declaring-persons list;
- a cooperating importer or broker.

I did **not** try to log in, and none of us may use a client's key or PIN on their behalf: the key holder must protect the key (ZRU-793 art. 27, R57), and unauthorised-access risk applies (R58).

### What is needed

1. **A key holder.** One of:
   - (a) the director of a cooperating importer (an LLC, using their own ERI);
   - (b) that importer's staff specialist, already **listed in ed1 with a valid authority period**;
   - (c) a notified broker's specialist working on their own client.

   The founder qualifies only if he heads an Uzbek company that has its own ERI [UNVERIFIED whether he does].
2. **Written consent** from the company, covering: observing, screen recording, redacted screenshots, no submit, no signature, and whether a draft may be saved. Saving a draft depends on Q-2.
3. **The key holder's own PC** with E-IMZO installed. They type the PIN themselves; YuklaGo people only watch (in person or by screen share).
4. **No automation.** `ED2_LIVE_AUTOMATION` stays off (DEC-24) and no scripts are injected. Opening the browser's DevTools Elements panel to read field names is done by the key holder or under their eye. That is a read-only look at their own page [INFERENCE that this is acceptable; confirm with Huquq].

### Session script (supervised, no submit)

1. **Before.** Agree the date. Prepare a test data sheet using **demo Set A** values (synthetic; never real third-party data). Set the recorder to capture **only the ed2 window**. Agree the redaction rules: blur the STIR, name, PINFL and any existing declarations.
2. **Login.** The key holder logs in on ed2.customs.uz. Record the login page and the post-login menu path, but no personal data.
3. **Open a new IM40 draft** (record the menu path and the form version or date if shown). Do **not** use an existing real declaration.
4. **For each grafa below,** record: the label text (exactly); whether it is editable or auto-filled; whether it is required; the input type (text, number, list); the full list of allowed values; the validation message after a deliberately wrong test value; any help text; the DOM `id`/`name` (from DevTools, read-only).
   - **13:** auto-filled with the CB USD rate? For which date (today, or recalculated at acceptance)? Editable?
   - **33:** is there a **right part**? What does it accept, and is it required for ordinary goods?
   - **36:** does the box exist on screen? Its label, whether editable, and its list. Does format control complain if it is left empty?
   - **41:** is the unit code **numeric** (e.g. 796) or a letter code? Capture the full list or a screenshot of it. Is it auto-set from the TIF TN code?
   - **43:** are 0/1 offered? Is the label "own needs"?
   - **44:** is **code 904 "МЕТОД"** in the document list? How are E-arxiv special numbers entered? How is a "6…" exemption line entered?
   - **45:** is there a **left subfield**? Its label and list (valuation method?).
   - **47:** is it calculated by the system or entered by hand? Enter test values and note the **rounding of soʻm** and the number of decimals. Check whether fee rows appear only on item 1, and capture the list of СП (payment-method) codes.
5. **Format-logic control.** If the form has a separate **"check" button (not send)**, press it once and capture the messages. They feed the Y19 library (R-series). **Do not press send, register or sign.**
6. **Q-7 observation only.** Note where the "sign" or "send" button sits and what it says. **Do not open the signing dialog.** If DEC-23 is to be tested, the key holder alone may later repeat steps 2–3 inside the YuklaGo desktop window, separately and with consent.
7. **Exit.** Delete the unsaved draft, or the saved one if Q-2 allowed saving. Log out. The key holder removes the token or PFX. Stop the recorder.
8. **After.** Write `data/declarant/ed2-observations-YYYYMMDD.md` (per-grafa table with screenshot references). Update the ⚠️ flags in `grafa-map.json` and the spec flags (DEC-21, PC-12), and add new R-messages to Y19.

**Planning estimate:** about 1–2 hours of the key holder's time. This is an estimate, not a measured figure.

**Owner of the next step:** the Hakathon CEO or the founder finds the cooperating company and key holder. The Deklarant then runs the script.

---

## H. PE-22 / Q-14: gold case (one real accepted, redacted declaration)

### What is blocking it

**We have no real accepted declaration and no cooperating importer or broker.** I found **no filled, accepted BYUD published** on lex.uz or customs.uz.

### What is needed

1. **A cooperating importer or broker** willing to share **one released IM40** with signed consent and an NDA covering commercial secrecy and personal data (ZRU-547 art. 21 and 28: consent must be provable, and disclosure to third parties needs consent).
2. **Preferred profile:** accepted **after 01.09.2026** (BHM 440,000) and under the current PQ-181/PQ-58 rates; 2–5 items; ad valorem duty plus VAT; no excise, no exemption, no marking; road transport; an origin certificate present.
3. **The full set:**
   - the TED printout or PDF from ed2;
   - invoice, contract (E-kontrakt ID), CMR, packing list, freight invoice, origin certificate;
   - the CB rate on the acceptance day;
   - the **ed1 payment reconciliation act** showing the amounts actually charged.

### Redaction list (mask with tokens; keep every number used in calculation)

| Mask | Keep |
|---|---|
| Grafa 2: seller name and address (keep the country) | 1 (type, regime) |
| Grafa 8: consignee name, address, STIR | 5 (items), 11, 15/15a, 20, 22, 23, 24, 25, 26, 29, 30 |
| Grafa 9: financially responsible person's STIR | 12 (total customs value), 13 (rate) |
| Grafa 14: declarant or broker name, STIR, notification number | Per item: 31 description (generalise brand or article only if sensitive), 33, 34, 35, 37, 38, 41 and its quantity, 42, 43, 45, 46 |
| Grafa 54: signer name, PINFL, phone (keep the date) | 47: all rows (payment type, base, rate, sum, СП) |
| Grafas 18/21: vehicle plates | 44: document **codes** (number masked) |
| Grafa 28: bank details | Acceptance and release dates |
| Grafa 40: previous document numbers | Post code (grafa 7, first part) |
| Grafa 44: document numbers (contract, invoice, CMR, certificates, E-arxiv numbers) | — |
| «С»: E-kontrakt ID | — |
| Registration number in grafa 7 / A, QR and bar codes, ERI signature block | — |
| Officer names and stamps (D, B) | — |

**Acceptance test:** the YuklaGo engine reproduces every grafa 47 row and the total **to the soʻm**, given the kept values. Any difference is explained in writing before anything is labelled "tasdiqlangan".

### Public material usable meanwhile (as **reference only, never "verified"**)

- **Instruction 2773 Annex 1 (BD-1 main sheet)** https://lex.uz/uz/files/4624421 and **Annex 2 (BD-2 additional sheet)** https://lex.uz/uz/files/4624433. These are **blank** form images: useful for box layout and numbering, with **no values**. They are what shows box 36 "Преференция" on paper (§C.2 point 6).
- **customs.uz page "Bojxona yuk deklaratsiyasini toʻldirish tartibi boʻyicha tushuntirish"** https://www.customs.uz/page/bozhhona-yuk-deklaraciyasini-toldirish-tartibi-boyicha-tushuntirish. It holds official explanations for grafas 2, 8, 31, 40 and others. The page is script-rendered and timed out for me; from the search snippet I saw **no filled example** [UNVERIFIED for the full page].
- **Classifiers** (Annex 12 document codes, Annex 13 payment codes, Annex 14 benefit acts), also mirrored as a PDF on static.norma.uz. They are good for code lists, not for a gold case.
- **Interim:** use demo **Set A** (`data/declarant/demo-sets/set-A-furniture-cn-truck/answer-key.json`, SYNTHETIC) as the "namuna" case. Keep PE-22 **[PENDING]**.
- **Optional:** the founder, in his own talks with officials (DEC-14), could ask the Customs Committee for an anonymised sample declaration. **Nothing has been sent.**

---

## Sources

- Instruction 2773 (uz): https://lex.uz/uz/docs/2924955
  - cl. 21, 22 sub-point 38: EK10 list and EK10 grafa 43;
  - cl. 24, 25 sub-points 10, 28, 30, 38, 39, 40, 42: IM40;
  - cl. 76, 89;
  - Annex 12 row 113 (code 904);
  - Annexes 1–2 (form images): /uz/files/4624421 and /uz/files/4624433.
- Customs Code arts. 261, 277, 304: https://lex.uz/docs/2876354
- VMQ 605 cl. 2, 15, 30: https://lex.uz/uz/docs/-3844549
- VMQ 847: https://lex.uz/docs/-7274716
- VMQ 163: https://lex.uz/uz/docs/-4213596
- Civil Code arts. 146, 148: https://lex.uz/docs/111181
- MJtK 227¹⁰, 227²²: https://lex.uz/uz/docs/-97664
- ZRU-793 art. 27 (key protection) and ZRU-547 arts. 21, 28: as cited in spec R57 and R42.
- Team data: `data/declarant/README.md` (CEO decisions 04:00), `grafa-map.json`, `deadlines.md`, `tolerances.md`, `demo-sets/`.

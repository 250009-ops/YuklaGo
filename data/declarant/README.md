# YuklaGo – declarant P0 data (IM40 import)

*Delivered 2026-11-18 (Asia/Tashkent) by the declarant advisor. Not legal advice. Every legal claim links to lex.uz; anything not confirmed is marked ⚠️. All demo values are **SYNTHETIC**.*

## Files

| File | What it is |
|---|---|
| `grafa-map.json` / `grafa-map.md` | All 46 grafas the declarant fills for IM40 (Instruction No. 2773, Ch. 5, points 24–25), with official Uzbek (Cyrillic) + Russian names, Latin transliteration, format, filling rule, source document, classifier, checks, and a lex.uz deep link per grafa (uz + ru). Also: general rules (points 4–14), customs-only grafas (7, 44, 47, A, B, D – points 89–90), classifier list, codes used in demos. |
| `grafa-map-ek10.json` / `grafa-map-ek10.md` | **New 18.11.** EK10 export map from Instruction 2773 Ch. 4, points 20–22: all 45 grafas from the point-21 list, official uz/ru names, format, rule, source doc, lex.uz paragraph link (uz + ru), and a `vs_im40` field per grafa + a differences table (only-IM40: 15, 15a, 21; only-EK10: 17, 17a; changed: 1, 2, 8, 18, 20, 25, 29, 31, 37, 40, 43, 44, 45, 47, C). Grafa 43 = 0 not own production / 1 own production. ⚠️ items marked. |
| `tolerances.json` / `tolerances.md` | 17 cross-checks (invoice ↔ packing list ↔ CMR ↔ BYD). **No official numeric tolerance exists in the law I checked** – official rules (rounding, totals, definitions, Annex 1a, Art. 18, Art. 320, VMQ 605 cl. 15/30/31) listed separately from **PROPOSED product defaults** (clearly labelled). Uzbek/Russian message templates included. |
| `deadlines.json` / `deadlines.md` | 15 clocks: advance info, transit declaration, 30-min notification, 3-h confirmation, short GTD, temporary storage 60/10 days, **15-day filing with start-day rule**, preliminary declaration 30 days, acceptance, clearance 3 h/8 h/1 working day, payment + penya, 3-day removal, 3-year amendment window, 3-year retention; fines (MJtK 227¹⁰, 227²⁶). Worked date examples. |
| `demo-sets/set-A-furniture-cn-truck/` | Clean golden path: 2 models of wooden furniture under one code (2 items), FCA + freight add-back, USD. |
| `demo-sets/set-B-tshirts-tr-truck/` | Cotton T-shirts from Turkey, CPT Tashkent + Art. 305 inland deduction, specific minimum wins. **Seeded:** CMR packages 118 vs 120; CMR gross 1 430 vs 1 344 kg; seller HS 6109.90 vs 6109.10. |
| `demo-sets/set-C-electronics-cn-truck/` | Microwaves + LED lamps, CNY contract, DAP Yallama. **Seeded:** packing list LED qty 2 000 vs 2 400 (→ qty, packages, net checks fail); invoice missing buyer phone (Annex 1a). |
| each set: `invoice.json`, `packing-list.json`, `cmr.json`, `supporting-docs.json` (contract, CoO, transit declaration, freight, arrival, importer profile), `answer-key.json` (expected cross-check results, seeded discrepancies, expected header + item grafa values incl. grafa 47 rows, payments, deadline), `README.md` (readable) |
| `demo-sets/index.json` | One-line outcome + totals per set |
| `_build/` | Generator scripts (Python) – rerun after edits in this order: `build_grafa.py` → `build_grafa_ek10.py` (reads grafa-map.json) → `build_tol.py` → `build_deadlines.py` → `build_sets.py`. They read raw lex.uz dumps from `/workspace/bojxona/` (`ch4_split.json` copied here). |

Duty rates and fee bands are **not re-researched here**: they come from the tariff team's `data/tariff/tariff_demo.json` and `fees.json` (each with its own lex.uz source). Exchange rates in demos are **EXAMPLE** values (1 USD = 12 100 UZS, 1 CNY = 1 700 UZS), not CBU data.

## Key sources (lex.uz)

- Instruction No. 2773 (06.04.2016) on filling the BYD/GTD – uz https://lex.uz/uz/docs/2924955 · ru https://lex.uz/docs/2924953 (edition with change of 22.07.2026, No. 2773-15)
- Customs Code – https://lex.uz/docs/2876354 (Arts. 18, 85, 86, 89, 177, 184, 206, 226, 248, 261, 262, 264, 266, 304, 305, 320, 324, 326, 327, 333, 349)
- VMQ No. 605 (TED Regulation, incl. Annex 1a invoice minimum data) – https://lex.uz/uz/docs/-3844549
- Administrative Liability Code (227¹⁰, 227²², 227²⁶) – https://lex.uz/uz/docs/-97664
- Civil Code Arts. 145–148 (period counting, analogy only) – https://lex.uz/docs/111181

## Open questions (need a decision or an expert check)

1. **15-day start-day rule.** Art. 261 says "from the day of presentation"; the Customs Code has no general counting article. Proposal: show conservative date (presentation day = day 1) as "file by" and +15 as "legal max (interpretation)". **CEO decision.**
2. **Tolerances are proposals.** Gross ±max(1%, 20 kg) warn / beyond = block; net ±max(0.5%, 5 kg); packages/qty exact. OK to ship as product defaults labelled "not law"? **CEO decision**; ideally validated by a practising inspector.
3. **Freight allocation between items** (Art. 304 add-backs) – by gross weight in the demos; no official rule found. **CEO/engineer decision** (weight vs value).
4. **Specific minimums per kg** (furniture 0.4 USD/kg): net or gross kg? Unverified (tariff team flags the same). Demos use net; outcome unchanged in Set A.
5. **Post working calendar.** Art. 261 shifts to the *customs body's* next working day – needs a maintained per-post schedule + public holidays. Who owns this data?
6. **Pallets** – packaging (in grafa 35) or transport equipment (excluded)? Gross excludes "containers and other transport equipment" (Instruction 2773 ch.5 p.25 sub-point 30), but pallets are not named – UNCONFIRMED.
7. **Grafa 33 right part, grafa 45 left subfield, grafa 41 numeric unit codes, grafa 47 fee "base" text and UZS rounding** – not specified in Instruction 2773; check against the live ed2 cabinet / e-GTD format (point 3 refers to a format not published in the Instruction).
8. **Incoterms 2020 DPU** has no Annex 7 code; Annex 1a still says Incoterms 2010.
9. **Advance information**: Art. 206 part 3 makes it mandatory for road/rail/air (prior lesson said optional under Art. 17) – lead time and system not in the Code.
10. **Conformity certificates / energy-efficiency class** for microwaves and LED lamps, and furniture certification – not verified; Single Window list needed before claiming "go".
11. **MJtK future editions** dated 30.12.2026 and 05.02.2027 appear on lex.uz – re-check fines before those dates.
12. **Customs value vs statistical value (grafa 46)** – demos assume CV ≈ CIP border value.

## Decisions by Hakathon CEO (18.11.2026 04:00 Tashkent)
- (a) Show "file by" = presentation + 14 days and "legal max" = + 15 days; in-app help explains why.
- (b) Ship tolerances as admin-configurable defaults; every warning/block shows the label "PROPOSAL, not law".
- (c) Freight split default: by gross weight; user may switch to by invoice value; the chosen method is written into the audit pack.
- (d) YuklaGo ops maintains a working-calendar config (holidays from official government decrees + each post's hours), with source and date per entry. If a post's calendar is unverified, show the earlier date and flag it.
- Unverified items (grafas 41, 33, 45, 47; Set C certificates; 2026/2027 MJtK fine editions) stay flagged; no demo claims on them.
13. **Code 904 МЕТОД** (valuation method, Annex 12 item 113) – when mandatory and exact line format unknown; added to grafa 44 as our reading, UNVERIFIED on live ed2.
14. **EK10 specifics** – foreign consignee TIN field (grafa 8), lines 6–11 of grafa 31, grafa 40 empty for own production, export fee band: confirm on ed2.

## Changelog

- **2026-11-18 04:20 (Asia/Tashkent) – spec v3 Q-19 (PM):**
  - `tolerances.json/.md`: weight rules made explicit with a `formula` block (D = declared/invoice figure, diff = abs(A − B), T computed from D). Gross: pass if 0; info ≤ 1 kg; warning ≤ T = max(1% × D, 20 kg); else blocking. Net: pass if 0; warning ≤ T = max(0.5% × D, 5 kg); else blocking. Per-line and total, worst severity wins. Still labelled PROPOSAL, not law. Added `gross_weight_scope`: gross excludes containers/transport equipment (sub-point 30, lex.uz ru #2927394 / uz #2926849); pallets UNCONFIRMED. New md section "Weight formulas".
  - `grafa-map.json/.md`: grafa 44 gets `additional_document_codes` → 904 МЕТОД (Annex 12 item 113; ru #8355909, uz #8355460; sub-point 39 з) ru #7472695; grafa 45 methods ru #2927501; Customs Code Arts. 302–313), marked OUR READING, UNVERIFIED on live ed2.
  - New `grafa-map-ek10.json/.md` (see table above).
  - Demo answer keys (sets B, C): weight-check details now show the threshold arithmetic; results unchanged.
- **2026-11-18 04:00** – first delivery (grafa map IM40, 3 demo sets, tolerances, deadlines).

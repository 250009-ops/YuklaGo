# Payments and fees

The engine lives in `packages/calc`. It is a pure function. It does not call a model, and a model must not call it to "check" a total. Rules: spec §3A PE-1–PE-22 and `data/tariff/`.

YuklaGo calculates. The owner pays from their own bank. The screen C-15 says "Oʻz hisobingizdan toʻlaysiz. YuklaGo toʻlamaydi." and "Kabinetdagi 47-grafa summasini toʻlang".

## Pipeline

1. Reject a code that is not 10 digits in `tiftn_codes_pq181_annex1.csv` (`STAVKA_TOPILMADI` / "Kod rasmiy roʻyxatda yoʻq"). `8539 52 000 0` does not exist. `8539520009` does.
2. Choose the duty row in force on the acceptance date (PE-7). Store edition date.
3. Method 1 (transaction value) only if there is a sale and the related-party answer is no, or the user supplied evidence that the relationship did not affect the price (PE-1, PE-2). Otherwise open a valuation case and do not output a method-1 number.
4. Add freight, insurance, and the other BK 304 items up to the place of entry. Incoterms decide what is already in the price (PE-3–PE-5). Unsplit freight is added in full with the warning "Hujjatda boʻlinish yoʻq".
5. The demo transport figure ≈ 6 200 000 soʻm is the user's figure or a labelled sample. The engine must not invent a freight rate. If the user has no quote, show "—" and mark the total incomplete.
6. Convert with the CBU rate on the acceptance date. Estimates use today's rate and the label "kurs BYD kuni oʻzgarishi mumkin" (PE-6). The YG-0412 screen uses a **sample** rate, chip "namuna kurs, CBU emas".
7. Duty: ad valorem, specific, or combined. Combined is `max(ad valorem, specific × qty × rate)` or a sum when the text says "plus" (PE-9). Missing quantity yields `BIRLIK_MIQDORI_YO'Q` and no amount.
8. Art. 300¹ surcharge when origin is missing or non-MFN (PE-10). China and Türkiye are on the MFN list that the tariff review read. Edges 10/20/30 percent show both values (`S300_BAND_EDGES`). Whether the surcharge enters the VAT base is [UNVERIFIED] (`S300_IN_VAT_BASE`). The demo below includes it in the side-by-side delta only, and labels the delta "≈ Taxmin".
9. Excise only for Tax Code 289¹–289³ lists. Otherwise the line is "Aksiz: qoʻllanmaydi (SK 289¹–289³)" (PE-12).
10. VAT 12% of (customs value + duty + excise) (PE-13). Formula label includes all three, even when excise is zero.
11. Fee from VMQ 55 bands (PE-14). One fee per declaration.
12. Allocate freight across items by gross weight unless the user picks value (DEC-19). The audit pack records the method. Sum of shares equals the total to the tiyin.

Provenance of a derived amount is the weakest input (ADR 0006). "Rasmiy" only on the rate, the VAT rate, the excise rate, the fee band, the BHM, and the CBU rate with its date (PE-21).

## Fee bands

From `data/tariff/fees.json`. 1 BHM = 440 000 soʻm from 01.09.2026 (PF-115). Convention for edges other than the last band: lower inclusive, upper exclusive, and at an exact edge the UI shows "chegara noaniq" with both amounts. That convention is an assumption. The resolution text is explicit only for the last band.

| Customs value, USD | BHM | Soʻm at 440 000 |
|---|---|---|
| up to 10 000 | 1 | 440 000 |
| 10 000 up to 20 000 | 1.5 | 660 000 |
| 20 000 up to 40 000 | 2.5 | 1 100 000 |
| 40 000 up to 60 000 | 4 | 1 760 000 |
| 60 000 up to 100 000 | 7 | 3 080 000 |
| 100 000 up to 200 000 | 10 | 4 400 000 |
| 200 000 up to 500 000 | 15 | 6 600 000 |
| 500 000 up to 1 000 000 | 20 | 8 800 000 |
| 1 000 000 and over | 25 | 11 000 000 |

Pre-arrival preliminary declaration: −20% on item 1"a" only (`PRELIM_DISCOUNT_SCOPE`). 440 000 × 0.8 = 352 000. The string "310 000" must never appear (AC-11.2).

Other VMQ 55 rows (change 25% BHM, out-of-hours 25% BHM, inspection 25% BHM per hour, storage, advance ruling 75% BHM, transit/processing 25% BHM) are listed in the "what could still cost money" box with their own source chip (PE-15). They are not added into the YG-0412 total.

## Worked example YG-0412 (Namuna)

Fixture: `contracts/calc/golden-yg0412.json`. Do not change these display numbers. They are the screen hand-off §7.2 sample, not a released declaration (PE-22).

Inputs:

- Invoice GM-2611, 2026-09-28, FOB Shenzhen, LED bulb E27 9W 6500K, 2 000 pcs, CNY 27 700.00.
- Code `8539520009`, duty 15% (PQ-181, edition date 16.02.2026).
- Grafa 45 customs value 31 233.76 CNY, which is the invoice plus freight in the contract currency.
- Display customs value ≈ 54 800 000 soʻm, of which transport ≈ 6 200 000 is "≈ Taxmin".
- Origin numeric 156. The primary column assumes an origin certificate. The file set has no certificate, so the total chip says "sertifikat bilan".
- Not preliminary. One item. BHM 440 000.

Arithmetic the engine must reproduce for the primary column:

- Duty = 0.15 × 54 800 000 = 8 220 000.
- Excise = 0.
- VAT base = 54 800 000 + 8 220 000 + 0 = 63 020 000. VAT = 0.12 × 63 020 000 = 7 562 400.
- Fee band: the sample treats the customs value as under 10 000 USD, so 1 BHM = 440 000. (The USD equivalent uses the sample FX. Grafa 46 statistical value is 4.332 thousand USD, so 4 332 USD, which is inside the first band.)
- Payments = 8 220 000 + 7 562 400 + 440 000 = 16 222 400.
- Landed = 54 800 000 + 16 222 400 = 71 022 400.

Side-by-side without a certificate, art. 300¹, base 15% sits in the "10–20 → +10 percentage points" band:

- Extra duty = 0.10 × 54 800 000 = 5 480 000.
- VAT on that extra duty = 0.12 × 5 480 000 = 657 600.
- Combined delta = 6 137 600.
- Landed without certificate = 71 022 400 + 6 137 600 = 77 160 000.

The primary total stays 16 222 400 with the chip "sertifikat bilan". I-01 shows the 300¹ row as "0 · sertifikat bilan (sertifikatsiz +6 137 600)". The inclusion of the surcharge in the VAT base for this delta follows `S300_IN_VAT_BASE` = include, which is [UNVERIFIED] / [INFERENCE]. The chip on the delta is "≈ Taxmin", not "Rasmiy".

Implied sample FX, for the trace only, labelled namuna:

- 54 800 000 / 31 233.76 ≈ 1 754.51 soʻm per CNY.
- Freight in CNY = 31 233.76 − 27 700 = 3 533.76, times that rate ≈ 6 200 000 soʻm.
- 54 800 000 / 4 332 ≈ 12 649 soʻm per USD. This is not a CBU rate.

Grafa 44 for the demo lists 202 (CMR), 220 (invoice), 301 (contract), 417 (conformity), 701 (origin certificate, СПТИМ). 417 and 701 have no E-arxiv number yet, so they are blockers. Grafa 34 = 156. Grafas 16, 17, and 36 stay empty.

Pre-arrival example YG-0417 uses the same fee rule: 352 000 soʻm, chip VMQ 55 · PF-250 and BK 262, plus the 30-day lapse clock.

Multi-line YG-0418 is in the hand-off §7.3. Fee 1.5 BHM = 660 000. Freight shares by gross weight sum to ≈ 9 800 000. The engine checks the sum, it does not invent the shares.

## States that must not produce a number

`STAVKA_TOPILMADI`, `KURS_YO'Q`, `BIRLIK_MIQDORI_YO'Q`, and `TAQIQLANGAN` (PE-17, VMQ 658). `KELIB_CHIQISH_NOMA'LUM` still shows the surcharge path. `BOG'LIQ_SHAXS` blocks the draft on value. `NAZORAT_TOVARI` stops filing until the user confirms the permit is in Yagona darcha.

## Rounding trace

Print `ROUNDING_MODE` in every trace. Payment soʻm rounding is [UNVERIFIED]. Do not label it "Rasmiy".

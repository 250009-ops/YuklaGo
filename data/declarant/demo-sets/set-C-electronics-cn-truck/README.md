# Set C – Microwave ovens + LED lamps from China by truck (CNY contract; 2 seeded issues)

**⚠️ SYNTHETIC DEMO DATA – fictitious companies, people, TINs, PINFLs, plates and document numbers. Not real. Do not file.**

Appliance shop imports microwave ovens and LED bulbs from Ningbo, DAP Yallama (border), contract in CNY, enters at Yallama, cleared at Keles. Packing list under-states LED quantity; invoice lacks buyer phone (VMQ 605 Annex 1a item 2). Shows: non-USD currency, fee band via USD equivalent, specific minimum (5 USD/pc) for microwaves.

## Invoice HS-INV-26-0311

Seller: Ningbo Hanshi Electric Appliance Co., Ltd. (SYNTHETIC) (No. 66 Kexue Rd, Yinzhou, Ningbo, Zhejiang, China, TIN 91330212SYNTH0003) · Buyer: «TEXNO UY SAVDO» MChJ (SYNTHETIC) · Contract HS-UZ-2026/03 of 2026-09-15 · Incoterms DAP Yallama border crossing, Uzbekistan (Incoterms 2010) · Currency CNY

| # | Description | HS (seller) | Qty | Price | Amount | Net kg | Gross kg | Pkgs |
|---|---|---|---|---|---|---|---|---|
| 1 | Microwave oven, 20 L, 700 W, mechanical control, 220 V (HANSHI MW-20S) | 8516.50 | 300 pcs | 260.00 | 78000.00 | 3150.000 | 3690.000 | 300 |
| 2 | LED lamp bulb A60, E27, 9 W, 806 lm, 6500 K (SMD chips, not filament) (HANSHI LB-9W) | 8539.52 | 2400 pcs | 4.50 | 10800.00 | 84.000 | 108.000 | 24 |
| | **Total** | | | | **88800.00** | 3234.000 | 3798.000 | 324 |

## Packing list HS-PL-26-0311

| # | Model | Qty | Pkgs | Net kg | Gross kg |
|---|---|---|---|---|---|
| 1 | MW-20S | 300 | 300 | 3150.000 | 3690.000 |
| 2 | LB-9W | 2000 | 20 | 70.000 | 90.000 |
| | **Total** | | 320 | 3220.000 | 3780.000 |

## CMR CN-KZ-UZ-44120

Taking over: Ningbo, China, 28.10.2026 · Delivery: Keles, Tashkent region, Uzbekistan · Packages: 324 · Gross: 3798 kg · HS: 851650; 853952 · Vehicle: 10A777CA/10XZ321 (860) · Border: 27001 Яллама on 2026-11-14

## Answer key (summary)

**Outcome:** BLOCKED at review: 4 blocking errors from 2 root causes + 1 weight warning. After corrected packing list and invoice, the expected GTD values below apply.

**Seeded discrepancies:**

- `qty_supp_unit / pkg_count / net_weight_docs`: Packing list line 2 shows 2 000 LED lamps in 20 cartons (70 kg net / 90 kg gross) instead of 2 400 in 24 cartons (84 / 108) → error_blocking
- `invoice_annex1a`: Invoice buyer block has no phone number (VMQ 605 Annex 1a item 2 requires name, legal address, TIN and phone) → error_blocking

**Expected cross-checks:**

- `qty_supp_unit`: FAIL – error_blocking — LED lamps: invoice 2400 vs packing list 2000
- `pkg_count`: FAIL – error_blocking — invoice 324 = CMR 324 vs packing list 320
- `gross_weight_docs`: WARN – warning_ack — packing list 3780 kg vs CMR/invoice 3798 kg: 18 kg = 0.47%; T = max(1% × 3798, 20) = 37.98 kg → 1 < 18 ≤ 37.98 (proposal band → explain)
- `net_weight_docs`: FAIL – error_blocking — LED net: invoice 84 kg vs packing list 70 kg (14 kg = 16.7%; per-line T = max(0.5% × 84, 5) = 5 kg → 14 > 5; total 3234 vs 3220 would only warn, worst severity wins)
- `invoice_annex1a`: FAIL – error_blocking — buyer phone number missing (Annex 1a item 2)
- `value_sum`: pass — 78000 + 10800 = 88800.00 CNY
- `hs_prefix`: pass — 851650 / 853952 match
- `origin`: pass — CN
- `currency_incoterms`: pass — CNY, DAP
- `customs_value_logic`: pass — DAP border → CV = invoice
- `dates`: pass — 15.09 ≤ 25.10 ≤ 28.10 ≤ 14.11 ≤ 18.11

| Item | Code | HS reasoning | Customs value | Duty (UZS) | VAT (UZS) |
|---|---|---|---|---|---|
| 1 | 8516500000 | Electro-thermic domestic appliance → 8516; microwave ovens → 8516 50 → 8516 50 000 0. ⚠️ Energy-efficiency class may be required in grafa 31 if microwaves are in the CM Res. 86/2015 annex – not verified. | 78000.00 CNY | 18150000.00 (specific minimum 5 USD/dona (> ad valorem)) | 18090000.00 |
| 2 | 8539520009 | LED light source/lamp → 8539 52; not phosphor-coated filament with ≥24 LEDs (…1), not straight tube ≥25 mm (…2) → 8539 52 000 9 (data/tariff notes 8539520000 does not exist). | 10800.00 CNY | 2754000.00 (ad valorem) | 2533680.00 |

Fee (code 10): 660000.00 UZS (1.5 BHM; band '10 000 dan 20 000 AQSH dollarigacha'). **Total payable (EXAMPLE rates): 42187680.00 UZS.**

EXAMPLE exchange rates (not CBU data): 1 USD = 12 100.00 UZS, 1 CNY = 1 700.00 UZS. Replace with the CBU rate on the GTD acceptance date (Customs Code Art. 326; Instruction 2773 grafa 23).

Deadline: Presented 16.11.2026 (Mon) → file by 30.11.2026 (conservative) / legal max 01.12.2026 (next-day reading).

Full expected grafa values: `answer-key.json` → `expected_gtd`.
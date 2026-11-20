# Set A – Wooden furniture from China by truck (clean golden path)

**⚠️ SYNTHETIC DEMO DATA – fictitious companies, people, TINs, PINFLs, plates and document numbers. Not real. Do not file.**

Small Tashkent furniture retailer imports dining tables and sideboards from Foshan (FCA), Uzbek carrier, enters at Dustlik (Andijan) under transit, cleared at Sergeli inland post. All documents consistent. Shows: two models under ONE code must be two items (Instruction 2773 point 8); freight to the border added to customs value (Customs Code Art. 304(a)); specific-minimum check (0.4 USD/kg) loses to ad valorem.

## Invoice MD-2026-118

Seller: Foshan Mingde Furniture Co., Ltd. (SYNTHETIC) (Longjiang Rd 88, Shunde, Foshan, Guangdong, China, TIN 91440606SYNTH0001) · Buyer: «UYJIHOZ SAVDO» MChJ (SYNTHETIC) · Contract 15/2026 of 2026-09-05 · Incoterms FCA Foshan (Incoterms 2010) · Currency USD

| # | Description | HS (seller) | Qty | Price | Amount | Net kg | Gross kg | Pkgs |
|---|---|---|---|---|---|---|---|---|
| 1 | Dining table, solid rubberwood, 1600x900x750 mm, lacquered (MINGDE DT-1600) | 9403.60 | 40 pcs | 145.00 | 5800.00 | 1520.000 | 1760.000 | 80 |
| 2 | Sideboard / TV stand, solid pine, 1200x450x600 mm (MINGDE SB-1200) | 9403.60 | 30 pcs | 210.00 | 6300.00 | 1560.000 | 1740.000 | 30 |
| | **Total** | | | | **12100.00** | 3080.000 | 3500.000 | 110 |

## Packing list MD-PL-118

| # | Model | Qty | Pkgs | Net kg | Gross kg |
|---|---|---|---|---|---|
| 1 | DT-1600 | 40 | 80 | 1520.000 | 1760.000 |
| 2 | SB-1200 | 30 | 30 | 1560.000 | 1740.000 |
| | **Total** | | 110 | 3080.000 | 3500.000 |

## CMR CN-UZ-77812

Taking over: Foshan, China, 01.11.2026 · Delivery: Tashkent, Uzbekistan · Packages: 110 · Gross: 3500 kg · HS: 940360 · Vehicle: 01A123BC/01XY456 (860) · Border: 03002 Дустлик on 2026-11-10

## Answer key (summary)

**Outcome:** All checks pass → ready for review & ERI signing (green-path candidate; actual risk lane is decided by customs).

**Expected cross-checks:**

- `pkg_count`: pass — 110 = 110 = 110
- `qty_supp_unit`: pass — 40/30 pcs match
- `value_sum`: pass — 5800+6300 = 12100.00
- `gross_weight_docs`: pass — 3500 = 3500 kg
- `net_weight_docs`: pass — 3080 = 3080 kg
- `net_le_gross`: pass — ok
- `hs_prefix`: pass — 940360 = 940360
- `origin`: pass — CN everywhere
- `currency_incoterms`: pass — USD, FCA, 15/2026
- `customs_value_logic`: pass — CV = 12100 + 3900 = 16000.00 USD
- `invoice_annex1a`: pass — all 12 items present
- `dates`: pass — 05.09 ≤ 28.10 ≤ 01.11 ≤ 10.11 ≤ 13.11

| Item | Code | HS reasoning | Customs value | Duty (UZS) | VAT (UZS) |
|---|---|---|---|---|---|
| 1 | 9403601000 | GRI 1/6: furniture, not seats (9401) → 9403; wooden → 9403 60; dining-room furniture → 9403 60 100 0 ('ошхона ва яшаш хоналари учун ёғоч мебель', PQ-181 Annex 1). | 7761.14 USD | 14086469.10 (ad valorem) | 12959551.57 |
| 2 | 9403601000 | Same as item 1 (living-room wooden furniture → 9403 60 100 0). Separate item because model/name differ (Instruction 2773 point 8). | 8238.86 USD | 14953530.90 (ad valorem) | 13757248.43 |

Fee (code 10): 660000.00 UZS (1.5 BHM; band '10 000 dan 20 000 AQSH dollarigacha'). **Total payable (EXAMPLE rates): 56416800.00 UZS.**

EXAMPLE exchange rates (not CBU data): 1 USD = 12 100.00 UZS, 1 CNY = 1 700.00 UZS. Replace with the CBU rate on the GTD acceptance date (Customs Code Art. 326; Instruction 2773 grafa 23).

Deadline: Presented 12.11.2026 (Thu) → file by 26.11.2026 (conservative) / legal max 27.11.2026 (next-day reading). See deadlines.json.

Full expected grafa values: `answer-key.json` → `expected_gtd`.
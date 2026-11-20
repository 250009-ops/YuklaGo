# Set B – Cotton T-shirts from Turkey by truck (2 seeded discrepancies + HS warning)

**⚠️ SYNTHETIC DEMO DATA – fictitious companies, people, TINs, PINFLs, plates and document numbers. Not real. Do not file.**

Clothing wholesaler imports knitted cotton T-shirts from Istanbul, CPT Tashkent, Turkish truck, enters at Alat (Bukhara), cleared at Tashkent-tovarniy. CMR is wrong on packages and gross weight; seller's invoice shows the wrong HS subheading. Shows: specific minimum (0.5 USD/pc) beats ad valorem; inland-freight deduction under Art. 305.

## Invoice ANK-2026-0917

Seller: Anka Tekstil Sanayi ve Ticaret A.Ş. (SYNTHETIC) (Merter Mah. 12, Güngören, İstanbul, Türkiye, TIN TR-SYN-1234567890) · Buyer: «MODA TEKSTIL TRADE» MChJ (SYNTHETIC) · Contract TR-07/2026 of 2026-08-20 · Incoterms CPT Tashkent (Incoterms 2010) · Currency USD

| # | Description | HS (seller) | Qty | Price | Amount | Net kg | Gross kg | Pkgs |
|---|---|---|---|---|---|---|---|---|
| 1 | Men's T-shirt, knitted single jersey, 100% cotton, 160 g/m2, sizes S-XXL, assorted colours (ANKA BASIC AB-100) | 6109.90 | 6000 pcs | 2.10 | 12600.00 | 1260.000 | 1344.000 | 120 |
| | **Total** | | | | **12600.00** | 1260.000 | 1344.000 | 120 |

## Packing list ANK-PL-0917

| # | Model | Qty | Pkgs | Net kg | Gross kg |
|---|---|---|---|---|---|
| 1 | AB-100 | 6000 | 120 | 1260.000 | 1344.000 |
| | **Total** | | 120 | 1260.000 | 1344.000 |

## CMR TR-UZ-20931

Taking over: İstanbul, Türkiye, 03.11.2026 · Delivery: Tashkent, Uzbekistan · Packages: 118 · Gross: 1430 kg · HS: 610990 · Vehicle: 34ABC123/34XYZ45 (792) · Border: 06010 Алат on 2026-11-19

## Answer key (summary)

**Outcome:** BLOCKED at review: 2 blocking errors + 1 warning. After a corrected CMR (120 pkgs, 1 344 kg) and acknowledging the HS warning, the expected GTD values below apply.

**Seeded discrepancies:**

- `pkg_count`: CMR box 7 says 118 packages; invoice and packing list say 120 → error_blocking
- `gross_weight_docs`: CMR box 11 gross 1 430 kg vs packing list 1 344 kg (+6.4%) → error_blocking
- `hs_prefix`: Seller HS 6109.90 vs composition 100% cotton (→ 6109.10) → warning_ack

**Expected cross-checks:**

- `pkg_count`: FAIL – error_blocking — invoice 120, packing list 120, CMR 118
- `gross_weight_docs`: FAIL – error_blocking — packing list 1344 kg vs CMR 1430 kg: diff 86 kg = 6.40%; T = max(1% × 1344, 20) = 20 kg → 86 > 20
- `hs_prefix`: WARN – warning_ack — invoice/CMR 610990 vs chosen 610910 (100% cotton)
- `qty_supp_unit`: pass — 6000 = 6000
- `value_sum`: pass — 6000 × 2.10 = 12600.00
- `net_weight_docs`: pass — 1260 = 1260
- `customs_value_logic`: pass — 12600 − 450 (Art. 305) = 12150.00 USD
- `origin`: pass — TR
- `invoice_annex1a`: pass — all 12 items present (HS present but wrong subheading)
- `dates`: pass — 20.08 ≤ 02.11 ≤ 03.11 ≤ 19.11 ≤ 24.11

| Item | Code | HS reasoning | Customs value | Duty (UZS) | VAT (UZS) |
|---|---|---|---|---|---|
| 1 | 6109100000 | Knitted → Chapter 61; T-shirt → 6109; 100% cotton → 6109 10 → 6109 10 000 0. Seller's 6109.90 ('other textile materials') contradicts the composition → warn. | 12150.00 USD | 36300000.00 (specific minimum 0.5 USD/dona (> ad valorem)) | 21997800.00 |

Fee (code 10): 660000.00 UZS (1.5 BHM; band '10 000 dan 20 000 AQSH dollarigacha'). **Total payable (EXAMPLE rates): 58957800.00 UZS.**

EXAMPLE exchange rates (not CBU data): 1 USD = 12 100.00 UZS, 1 CNY = 1 700.00 UZS. Replace with the CBU rate on the GTD acceptance date (Customs Code Art. 326; Instruction 2773 grafa 23).

Deadline: Presented 21.11.2026 (Sat) → day 15 conservative = 05.12.2026 (Sat) → shifted to Mon 07.12.2026 if the post is closed at weekends; legal max reading also 07.12.2026. See deadlines.json.

Full expected grafa values: `answer-key.json` → `expected_gtd`.
# Cross-check tolerances – invoice ↔ packing list ↔ CMR ↔ BYD (IM40)

*Generated 2026-11-18 (Asia/Tashkent). Twin: `tolerances.json`.*

> **Bottom line:** I found **no official percentage or kg tolerance** in the Customs Code, Instruction No. 2773 or VMQ No. 605 for weight / value / quantity / package differences. Every number in the *Proposal* column below is a **product default, not law** – label it that way in the UI.

## What the law does say

| Topic | Finding | Source |
|---|---|---|
| No numeric tolerance | No official percentage or kg tolerance was found for differences in gross/net weight, quantity, number of packages or value between invoice, packing list, CMR and the BYD in: Customs Code, Instruction No. 2773, VMQ No. 605 (incl. Annex 1a). Searched 2026-11-18 (full-text keyword search + web search). Treat any difference as a discrepancy that must be explained or corrected. |   |
| Rounding (weights) | Gross (grafa 35) and net (grafa 38) weights are rounded mathematically to 3 decimals (6 decimals if < 1 g). | Instruction 2773, ch.5 p.25 sub-points 30, 33 https://lex.uz/docs/2924953#2927394 ; https://lex.uz/docs/2924953#2927413 |
| Rounding (values) | Invoice value (grafa 42) and customs value (grafa 45) are rounded mathematically to 2 decimals; statistical value (grafa 46) to 3 decimals in thousand USD. | sub-points 37, 40, 41 https://lex.uz/docs/2924953#2927453 ; https://lex.uz/docs/2924953#2927498 ; https://lex.uz/docs/2924953#2927503 |
| Rounding (supplementary quantity) | Quantity in supplementary unit: 2 decimals; below 0.01 → 6 decimals. | sub-point 26 (grafa 31) https://lex.uz/docs/2924953#2927362 |
| Totals must equal sums | Grafa 22 total invoice value = Σ grafa 42; grafa 12 total customs value = Σ grafa 45; grafa 5 = number of grafa 31 items. | sub-points 18, 9, 4 https://lex.uz/docs/2924953#2927326 ; https://lex.uz/docs/2924953#2927273 ; https://lex.uz/docs/2924953#2927231 |
| Gross weight definition | Gross = goods + all packaging needed to keep them intact until entering circulation, EXCLUDING containers and other transport equipment. CMR gross may legitimately differ if it includes pallets/transport equipment – reason must be shown. | sub-point 30 https://lex.uz/docs/2924953#2927394 |
| Net weight definition | Net = without any packaging, except inseparable primary retail packaging. | sub-point 33 https://lex.uz/docs/2924953#2927413 |
| Carrier documents content | Road carrier must present CMR + commercial documents containing, among others: consignor/consignee, HS code (≥6 digits), gross weight (kg) and invoice value per code, number of packages, container numbers. | Customs Code Art. 18 part 1 item 1(v) https://lex.uz/docs/2876354 |
| Invoice minimum data | Invoice must contain 12 items: seller (name, address, TIN), buyer (name, address, TIN, phone), HS code ≥6 digits, origin country, description, invoice value, gross kg, net kg, total packages, quantity in supplementary unit, Incoterms (2010), contract number and date. | VMQ 605 Annex 1a (added by VMQ 630, in force 07.01.2025) https://lex.uz/uz/docs/-3844549 |
| Format-logic control | If the e-system finds errors, deficiencies or inconsistencies in the TED it is automatically returned with an e-notification stating reasons. | VMQ 605 clause 15; Annex 1 stage 3 https://lex.uz/uz/docs/-3844549 |
| Automatic clearance condition | Automatic (no-officer) clearance requires, among others, no inconsistencies in TED data and consistency with permit documents. | VMQ 605 clause 18 (per dars-01) https://lex.uz/uz/docs/-3844549 |
| Discrepancy found at unloading | Declarant may request amendment/addition of the TED if differences in quantity, name, description or other features are found during or after unloading into temporary storage. | VMQ 605 clause 30 https://lex.uz/uz/docs/-3844549 |
| Voluntary correction | Declarant may, with customs permission, voluntarily correct errors that do not affect payment calculation or prohibitions/restrictions before customs finds them; customs may allow fixing spelling errors in words (not numbers/letter codes) within one working day. | VMQ 605 clauses 30–31 https://lex.uz/uz/docs/-3844549 |
| Value adjustment | Customs adjusts customs value/payments if, among others, declared value does not match actual value because quantity and/or quality deviate from the contract (evidence: inspection act; agreed claim; expert opinion). | Customs Code Art. 320 https://lex.uz/docs/2876354 |
| Liability | Incorrect declaration affecting payments/measures: MJtK Art. 227²² (confiscation + fine); not affecting the customs decision: 3 BHM (part 2) – per dars-01. | MJtK 227²² https://lex.uz/uz/docs/-97664 |

## Checks and proposed defaults (PROPOSAL – not law)

| Check | Compare | Official tolerance | Proposal | Severity if exceeded |
|---|---|---|---|---|
| `pkg_count` Number of packages | invoice.total_packages; packing_list.total_packages; cmr.packages; gtd.grafa31_line2 (Σ items) | none found | abs=0, rel=None | error_blocking |
| `qty_supp_unit` Quantity in supplementary unit (pcs, pairs…) | invoice.lines.qty; packing_list.lines.qty; gtd.grafa31_bottom_right | none found | abs=0 | error_blocking |
| `value_sum` Invoice arithmetic | Σ(invoice.lines.qty × unit_price); invoice.lines.amount; invoice.total; gtd.grafa22; Σ gtd.grafa42 | Exact after rounding to 2 decimals (Instruction 2773 sub-points 18, 37) | abs=0.01, unit=contract currency, note=0.01 only absorbs per-line rounding | error_blocking |
| `value_contract` Price vs contract/specification | invoice.unit_price; contract.spec.unit_price | none found | abs=0 | warning_ack |
| `customs_value_logic` Customs value build-up | gtd.grafa45; invoice value + Art.304 add-backs − Art.305 deductions | Exact (deterministic engine) | abs=0.01 | error_blocking |
| `gross_weight_docs` Gross weight – documents vs each other | packing_list.total_gross; invoice.total_gross; cmr.gross; gtd Σ grafa35 | none found | info_if_abs_le_kg=1, warning_if_rel_le_pct=1.0, warning_if_abs_le_kg=20, rule=diff = 0 → pass; 0 < diff ≤ 1 kg → info; diff ≤ max(1% of declared gross, 20 kg) → warning_ack (user must explain, e.g. pallets); otherwise error_blocking | error_blocking |
| `gross_weight_items_sum` Σ item gross = packing list total | Σ gtd.grafa35; packing_list.total_gross | Exact after 3-decimal rounding | abs_kg=0.001 | error_blocking |
| `net_weight_docs` Net weight – invoice vs packing list vs GTD | invoice.lines.net; packing_list.lines.net; gtd.grafa38 | none found | warning_if_rel_le_pct=0.5, warning_if_abs_le_kg=5, rule=diff = 0 → pass; diff ≤ max(0.5% of declared net, 5 kg) → warning_ack; otherwise error_blocking (no info tier for net) | error_blocking |
| `net_le_gross` Net ≤ gross; net > 0 | grafa38; grafa35 | Logical (definitions in sub-points 30, 33) | exact | error_blocking |
| `weight_per_package` Plausibility: gross per package | packing_list.gross / packages | none found | rule=flag if any packing-list line has gross/package outside [0.5×, 2×] of that line's median across the shipment | info |
| `hs_prefix` HS code | invoice.hs (≥6 digits, Annex 1a item 3); cmr.hs (Art. 18); gtd.grafa33[0:6] | none found | exact | warning_ack |
| `origin` Country of origin | invoice.origin; certificate_of_origin.country; gtd.grafa34 | none found | exact | error_blocking |
| `currency_incoterms` Currency, Incoterms, contract no./date | contract; invoice; gtd.grafa20/22/44 | none found | exact | error_blocking |
| `parties` Seller/consignor, buyer/consignee names & TIN | contract; invoice; cmr box 1/2; gtd.grafa2/8/9 | none found | rule=TIN exact; names fuzzy after normalising legal-form words, case, punctuation (similarity ≥ 0.9 → ok, else warning) | warning_ack |
| `vehicle` Truck & trailer plates | cmr box 25; transit_declaration; gtd.grafa18/21 | none found | rule=exact after removing spaces/hyphens, Latin↔Cyrillic look-alike normalisation | error_blocking |
| `invoice_annex1a` Invoice completeness (12 Annex-1a items) | invoice fields | All 12 items required (VMQ 605 Annex 1a) | exact | error_blocking |
| `dates` Document dates | contract.date ≤ invoice.date ≤ cmr.date ≤ grafa C arrival date ≤ filing date; certificate validity | none found | exact | warning_ack |

## Weight formulas (PROPOSAL – not law) – implement exactly as written

### `gross_weight_docs` – Gross weight – documents vs each other

> PROPOSAL (product default, not law)

```
units: kg; every weight rounded to 3 decimals first (Instruction 2773 sub-point 30)
declared: D = declared gross weight = invoice total gross (the figure that goes to Σ grafa 35); when evaluating per item use the item's invoice line gross
pair: A, B = the two figures being compared, any pair from {invoice, packing list, CMR, Σ grafa 35}
diff: diff = abs(A − B); T is ALWAYS computed from D (the invoice/declared figure), never from A or B
warn_threshold_kg: T = max(0.01 × D, 20)
info_threshold_kg: 1
decision: if diff == 0: pass; elif diff <= 1: info; elif diff <= T: warning_ack; else: error_blocking
comparison_operators: '<=' is inclusive: diff exactly equal to T is a warning, not a block
scope: evaluate every pair (invoice↔packing list, invoice↔CMR, packing list↔CMR, invoice↔Σ grafa 35) at shipment total and, where a document has lines, per item line; the worst severity wins
```

Worked examples:

- D=3798; A=CMR 3798, B=packing list 3780 → diff=18, T=max(37.98,20)=37.98 → warning_ack (Set C)
- D=1344; A=packing list 1344, B=CMR 1430 → diff=86, T=max(13.44,20)=20 → error_blocking (Set B)
- D=500; A=500, B=500.8 → diff=0.8 → info

**What counts as gross (official):** Gross weight (grafa 35) = goods incl. all packaging needed to keep them intact until entering circulation, EXCLUDING containers and other transport equipment. — Instruction 2773, ch.5 p.25 sub-point 30 (grafa 35); same wording for export: ch.4 p.22 sub-point 30 ([ru](https://lex.uz/docs/2924953#2927394), [uz](https://lex.uz/uz/docs/2924955#2926849)).

**Pallets:** ⚠️ UNCONFIRMED: the Instruction does not name pallets. Whether a pallet is 'packaging' (included) or 'transport equipment' (excluded) is not settled in the text read; the UI must ask the user to state it and must not auto-subtract pallets.

### `net_weight_docs` – Net weight – invoice vs packing list vs GTD

> PROPOSAL (product default, not law)

```
units: kg; every weight rounded to 3 decimals first (Instruction 2773 sub-point 33)
declared: D = declared net weight = invoice net for that item line (the figure that goes to grafa 38); for the shipment total use invoice total net
pair: A, B = the two figures being compared, any pair from {invoice, packing list, grafa 38}
diff: diff = abs(A − B); T is ALWAYS computed from D (the invoice/declared figure)
warn_threshold_kg: T = max(0.005 × D, 5)
decision: if diff == 0: pass; elif diff <= T: warning_ack; else: error_blocking
comparison_operators: '<=' is inclusive
scope: evaluate per item line AND at shipment total; the worst severity wins (a per-line error is not hidden by a large shipment total)
```

Worked examples:

- Set C LED line: D=84; A=84, B=70 (packing list) → diff=14, T=max(0.42,5)=5 → error_blocking
- Set C total: D=3234; A=3234, B=3220 → diff=14, T=max(16.17,5)=16.17 → warning_ack; worst = error_blocking
- D=2000; A=2000, B=2004 → diff=4, T=max(10,5)=10 → warning_ack


## UI message templates

| Check | Uzbek | Russian |
|---|---|---|
| `pkg_count` | Joylar soni hujjatlarda bir xil emas: {a} va {b}. Bojxona yukni qayta sanashi yoki ko'rik tayinlashi mumkin. Tashuvchidan aniqlashtiring. | Количество мест не совпадает: {a} и {b}. Возможен пересчёт или досмотр. Уточните у перевозчика. |
| `qty_supp_unit` | Dona soni invoys va qadoq varag'ida farq qiladi ({a} va {b}). | Количество в доп. единицах в инвойсе и упаковочном листе различается ({a} и {b}). |
| `value_sum` | Invoys summasi qatorlar yig'indisiga teng emas (farq {d}). | Итог инвойса не равен сумме строк (разница {d}). |
| `value_contract` | Invoys narxi kontrakt spetsifikatsiyasidan farq qiladi – qo'shimcha kelishuv kerak bo'lishi mumkin. | Цена в инвойсе отличается от спецификации – может потребоваться доп. соглашение. |
| `customs_value_logic` | Bojxona qiymatiga chegaragacha bo'lgan transport xarajati qo'shilmagan ko'rinadi. | В таможенную стоимость, похоже, не включена доставка до границы. |
| `gross_weight_docs` | Brutto vazn hujjatlarda farq qiladi: {a} kg va {b} kg ({p}%). Sababini (masalan, poddonlar) yozing yoki hujjatni tuzating. | Вес брутто различается: {a} кг и {b} кг ({p}%). Укажите причину (напр., поддоны) или исправьте документ. |
| `gross_weight_items_sum` | Tovarlar bo'yicha brutto yig'indisi jami bilan mos emas. | Сумма брутто по товарам не равна итогу. |
| `net_weight_docs` | Netto vazn hujjatlarda farq qiladi: {a} va {b} kg. | Вес нетто различается: {a} и {b} кг. |
| `net_le_gross` | Netto vazn brutto vazndan katta bo'lishi mumkin emas. | Вес нетто не может превышать брутто. |
| `weight_per_package` | Bir joyning og'irligi g'ayrioddiy – tekshirib ko'ring. | Необычный вес одного места – проверьте. |
| `hs_prefix` | Invoysdagi HS kod ({a}) siz tanlagan koddan ({b}) farq qiladi. Tanlov sababini tasdiqlang. | HS-код в инвойсе ({a}) отличается от выбранного ({b}). Подтвердите обоснование. |
| `origin` | Kelib chiqish mamlakati hujjatlarda har xil. | Страна происхождения в документах разная. |
| `currency_incoterms` | Valyuta / Inkoterms / kontrakt raqami hujjatlarda mos emas. | Валюта / Инкотермс / номер контракта не совпадают. |
| `parties` | Sotuvchi/oluvchi nomi hujjatlarda farq qiladi. | Наименование продавца/получателя различается. |
| `vehicle` | Mashina raqami CMR bilan mos emas. | Номер ТС не совпадает с CMR. |
| `invoice_annex1a` | Invoysda majburiy ma'lumot yo'q: {field} (VMQ 605, 1a-ilova). | В инвойсе нет обязательного реквизита: {field} (ПКМ 605, прил. 1а). |
| `dates` | Hujjat sanalari ketma-ketligi mantiqsiz. | Нелогичная последовательность дат документов. |

## Open points

- Pallets: count in grafa 35 gross or not? Instruction excludes 'containers and other transport equipment' (ch.5 p.25 sub-point 30) but does not name pallets ⚠️ UNCONFIRMED.
- The 1% / 20 kg gross and 0.5% / 5 kg net bands are proposals – ask a practising inspector/broker before demo claims.
- Annex 1a still says Incoterms 2010; most invoices use 2020 – treat 2020 terms as OK but flag DPU (no Annex 7 code).
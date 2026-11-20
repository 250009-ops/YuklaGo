# Deadlines & clocks – IM40 import

*Generated 2026-11-18 (Asia/Tashkent). Machine-readable twin: `deadlines.json`. Not legal advice.*

## The start-day rule (read this first)

- **Art. 261 Customs Code**: the import BYD must be filed *no later than 15 **calendar** days from the day the goods are presented to the destination customs body* (exceptions: Chapters 22, 23, 25). If the last day falls on a day the customs body does not work, the **next working day of that customs body** is the last day. [lex.uz](https://lex.uz/docs/2876354)
- **No general term-calculation article** exists in the Customs Code (full text searched 2026-11-18). So it is not stated whether the day of presentation counts as day 1.
- **Civil Code Art. 146** (civil-law periods start the day *after* the event) and **Art. 148** (action allowed until 24:00 of the last day; in an organisation until its working hours end) – [lex.uz](https://lex.uz/docs/111181). Applicability to customs periods is **not confirmed ⚠️**.
- **Product rule (PROPOSAL, not law):** show *File by* = presentation date + 14 days (presentation day = day 1), shifted past the post's non-working days; also show *Legal maximum (interpretation)* = presentation + 15 days, shifted. Reminders T-5/T-2/T-1. Treat the end of the last day as the end of the post's working hours.

| Example | Presented | File by (conservative) | Legal max (next-day reading) |
|---|---|---|---|
| synthetic | 2026-11-12 (Thu) | 2026-11-26 (Thu) (raw 2026-11-26 (Thu)) | 2026-11-27 (Fri) (raw 2026-11-27 (Fri)) |
| synthetic | 2026-11-21 (Sat) | 2026-12-07 (Mon) (raw 2026-12-05 (Sat)) | 2026-12-07 (Mon) (raw 2026-12-06 (Sun)) |

Shift in the examples assumes the post is closed Sat/Sun; public holidays and each post's schedule must come from a maintained calendar.

## Clocks

| Clock | Duration | Unit | Starts | Legal basis |
|---|---|---|---|---|
| Предварительная информация / Dastlabki axborot | — | — | before actual arrival | [Customs Code Art. 206 parts 3–4](https://lex.uz/docs/2876354) |
| Транзитная декларация / Tranzit deklaratsiyasi | — | — | border crossing | [Customs Code Art. 261 part 3](https://lex.uz/docs/2876354) |
| Уведомление о доставке / Yetib kelganini xabar qilish | 30 | minutes | delivery of goods to the destination customs body (or start of its working hours if delivered outside them) | [Customs Code Art. 226 parts 2–3](https://lex.uz/docs/2876354); [VMQ No. 605 Regulation, clause 6](https://lex.uz/uz/docs/-3844549) |
| Подтверждение доставки / Yetkazib berilganini tasdiqlash | 3 | hours | receipt of the carrier's notification | [Customs Code Art. 226 parts 4–5](https://lex.uz/docs/2876354) |
| Краткая ГТД / Qisqa BYD (vaqtincha saqlash) | 1 | working_day | day goods are presented to the customs body | [Customs Code Art. 86 part 2](https://lex.uz/docs/2876354) |
| Срок временного хранения / Vaqtincha saqlash muddati | 60 | calendar_days | day goods acquire temporary-storage status (= delivery confirmation, Art. 226) | [Customs Code Art. 85](https://lex.uz/docs/2876354); [Customs Code Art. 89](https://lex.uz/docs/2876354); [Customs Code Art. 226 part 5](https://lex.uz/docs/2876354) |
| Срок подачи ГТД при ввозе / Import BYD topshirish muddati | 15 | calendar_days | day goods are presented to the destination customs body | [Customs Code Art. 261 parts 1–2](https://lex.uz/docs/2876354) |
| Предварительное декларирование / Dastlabki deklaratsiya | 30 | calendar_days | day the preliminary declaration is accepted | [Customs Code Art. 262](https://lex.uz/docs/2876354) |
| Принятие ГТД / BYDni qabul qilish | 3 | hours | filing | [Customs Code Art. 264](https://lex.uz/docs/2876354); [VMQ No. 605, clause 15 and Annex 1 (stage 4)](https://lex.uz/uz/docs/-3844549); [Customs Code Arts. 324, 326](https://lex.uz/docs/2876354) |
| Срок оформления / Rasmiylashtirish muddati | — | — | TED acceptance | [VMQ No. 605 Regulation, clause 15 (a)–(v)](https://lex.uz/uz/docs/-3844549); [Customs Code Art. 248 part 4](https://lex.uz/docs/2876354) |
| Уплата таможенных платежей / Bojxona to'lovlarini to'lash | — | — | GTD acceptance | [Customs Code Art. 327](https://lex.uz/docs/2876354); [Customs Code Art. 333](https://lex.uz/docs/2876354) |
| Вывоз с места хранения / Saqlash joyidan olib chiqish | 3 | days | day goods were placed under another regime | [Customs Code Art. 89 part 2](https://lex.uz/docs/2876354) |
| Изменение ГТД / BYDga o'zgartirish kiritish | 3 | years | day of GTD acceptance | [Customs Code Art. 266](https://lex.uz/docs/2876354); [VMQ No. 605 Regulation, clause 30 (right to request amendment when quantity/description discrepancies are found during or after unloading)](https://lex.uz/uz/docs/-3844549) |
| Хранение документов / Hujjatlarni saqlash | 3 | years | year after the year in which goods lost the status of goods under customs control | [Customs Code Art. 184 part 3](https://lex.uz/docs/2876354); [Instruction 2773, point 14](https://lex.uz/docs/2924953) |
| Контроль после выпуска / Chiqarilgandan keyingi nazorat | — | — | release | [Customs Code Arts. 201, 294 (per dars-01)](https://lex.uz/docs/2876354) |

## Details

### Предварительная информация / Dastlabki axborot (`advance_info`)
- Authorised persons MUST submit advance information on goods and vehicles expected by road, rail and air through the Internet into the customs information system before they actually arrive; they are liable for its accuracy.
- ⚠️ Minimum lead time (hours before arrival) and the exact system/format are not stated in the Code ⚠️. Prior lesson (dars-01) cited Art. 17 as 'right, not duty' – Art. 206 part 3 makes it mandatory for road/rail/air; reconcile.

### Транзитная декларация / Tranzit deklaratsiyasi (`transit_declaration`)
- For goods entering the territory, the transit declaration is filed before or at the moment of crossing the customs border.

### Уведомление о доставке / Yetib kelganini xabar qilish (`arrival_notification`)
- Carrier notifies the destination customs body by presenting accompanying documents and the goods, no later than 30 minutes after delivery; if delivered outside working hours, no later than 30 minutes after working hours start (goods wait in the customs control zone).

### Подтверждение доставки / Yetkazib berilganini tasdiqlash (`arrival_confirmation`)
- Destination customs body confirms delivery within 3 hours by marking the accompanying documents (suspended if an offence is found). From the moment of confirmation the goods have the status of goods under the temporary-storage regime.
- This confirmation timestamp is the best machine-readable start for the temporary-storage clock.

### Краткая ГТД / Qisqa BYD (vaqtincha saqlash) (`short_gtd_temporary_storage`)
- Short cargo customs declaration is filed by the carrier or other authorised person no later than the working day following the day of presentation; not needed if the goods are placed under another regime within that time.
- related: [VMQ No. 605 Regulation, clause 10: if goods stay under constant customs control and clearance finishes within 24 hours after hand-over, temporary storage is not applied as a separate stage](https://lex.uz/uz/docs/-3844549) — 

### Срок временного хранения / Vaqtincha saqlash muddati (`temporary_storage_max`)
- Period is set by the authorised person who declared the regime but may not exceed 60 calendar days (10 calendar days for perishable goods) unless the Code provides otherwise (Art. 177 – liquidated warehouses: 60/180 days). Count starts from the day the goods acquired temporary-storage status (Art. 85 part 4 referring to Art. 177 and Art. 226 part 5). Goods must be declared for another regime no later than the day the period ends (Art. 89 part 1) and removed from the storage place within 3 days after placement under the other regime (Art. 89 part 2).
- ⚠️ Whether the 15-day filing clock and the 60-day storage clock run in parallel from the same day for goods under temporary storage (practice: the stricter 15-day clock governs the import GTD) ⚠️.
- Storage in a customs-body warehouse is charged per VM No. 55 (3% of BHM per tonne per day for the first 10 days, then 4% – per dars-01; see data/tariff/fees.json).

### Срок подачи ГТД при ввозе / Import BYD topshirish muddati (`import_gtd_filing`)
- Declaration for imported goods is filed no later than 15 calendar days from the day the goods were presented to the destination customs body, except cases in Chapters 22 (commercial vehicles), 23 (individuals, non-commercial) and 25 (pipeline / power lines). If the last day falls on a day the customs body does not work, the next working day of that customs body is the last day.
- fines: [Administrative Liability Code Art. 227¹⁰ part 2](https://lex.uz/uz/docs/-97664) — Failure to submit the customs declaration, documents or additional information within the established periods → fine of 3 × BHM (BHM = 440,000 UZS from 01.09.2026 → 1,320,000 UZS).
- fines: [Administrative Liability Code Art. 227¹⁰ part 3](https://lex.uz/uz/docs/-97664) — Repeated within one year after the penalty → citizens 5–10 × BHM, officials 10–15 × BHM.
- fines: [Administrative Liability Code Art. 227¹⁰ part 1](https://lex.uz/uz/docs/-97664) — Breach of declaration procedure (form, place, procedure) → citizens 2–5 × BHM, officials 3–7 × BHM.

### Предварительное декларирование / Dastlabki deklaratsiya (`preliminary_declaration`)
- Optional declaring before goods arrive. If the goods are not presented to the customs body within 30 calendar days from acceptance, the preliminary declaration is deemed not filed. After comparison of copies with originals and payment (or security) before arrival, it is the single document for customs operations (unless data/documents incomplete).
- incentive: [VM No. 55, Annex 1, note '*': 20% discount on the customs fee for preliminary declaration; fee charged once](https://lex.uz/docs/-7357270) — 
- incentive: [PF-250 of 17.12.2025, item 2: from 01.03.2026 for IM40 via preliminary declaration before arrival at the border crossing point – clearance fee −20%; no interest for up to 14 days on instalment/deferral](https://lex.uz/uz/docs/-7934915) — 

### Принятие ГТД / BYDni qabul qilish (`gtd_acceptance`)
- Acceptance is registered on the day of filing (Art. 264). E-system: an officer accepts the TED within 3 hours of receipt, otherwise it is accepted automatically (VMQ 605 Annex 1, stage 4). TED counts as accepted from the moment the e-notification is sent (VMQ 605 clause 15). The acceptance date fixes rates (Art. 324) and the exchange rate (Art. 326).

### Срок оформления / Rasmiylashtirish muddati (`clearance_time`)
- Low risk, no amendments: 3 hours; medium risk, no amendments: 8 hours (except TED filed outside working hours); high risk or other cases: general term in law. General term (Code Art. 248 part 4): clearance and document check within one working day from the day the declaration is accepted and all documents/data are presented (extended for risk-management measures).

### Уплата таможенных платежей / Bojxona to'lovlarini to'lash (`payment`)
- Customs payments are paid before or simultaneously with acceptance of the declaration (exceptions in Art. 327). With deferral/instalments – by the last day of deferral / per the agreed schedule (Arts. 327, 333).
- late consequences: [Customs Code Art. 349](https://lex.uz/docs/2876354) — Penalty (penya) for each calendar day of non-payment: 1/300 of the CBU refinancing rate on the debt; total penya ≤ the debt; runs from the day the debt arises to the day actually paid.
- late consequences: [Administrative Liability Code Art. 227²⁶](https://lex.uz/uz/docs/-97664) — Non-payment within established periods → citizens 3–7 × BHM, officials 5–10 × BHM.

### Вывоз с места хранения / Saqlash joyidan olib chiqish (`move_out_after_release`)
- Goods must leave the temporary-storage place within three days (unit 'days' – calendar vs working not stated ⚠️) after placement under another regime, except customs-warehouse regime.

### Изменение ГТД / BYDga o'zgartirish kiritish (`gtd_amendment_window`)
- After clearance, the GTD may be amended, supplemented, re-issued or cancelled within 3 years from acceptance at customs' request or on application; withdrawal before release if reasons accepted. E-GTD changes via a correction form. Fee for declarant-initiated amendment per VM 55 (25% of BHM per correction form – per dars-01).

### Хранение документов / Hujjatlarni saqlash (`record_retention`)
- Customs declaration and other documents needed for customs control are kept for three years from the year following the year in which the goods lost the status of goods under customs control.

### Контроль после выпуска / Chiqarilgandan keyingi nazorat (`post_release_audit`)
- Customs may audit after release (Art. 201) and charge additional payments (Art. 294) – informational.

## Fines summary (BHM = 440,000 UZS from 01.09.2026, PF-115)

| Breach | Article | Sanction |
|---|---|---|
| Late GTD / documents / additional info | MJtK 227¹⁰ part 2 | 3 BHM = 1,320,000 UZS |
| Repeat within 1 year | MJtK 227¹⁰ part 3 | citizens 5–10 BHM; officials 10–15 BHM |
| Breach of declaration form/place/procedure | MJtK 227¹⁰ part 1 | citizens 2–5 BHM; officials 3–7 BHM |
| Late payment | MJtK 227²⁶ + Code Art. 349 penya | citizens 3–7 BHM; officials 5–10 BHM + 1/300 refinancing rate per day |

MJtK: https://lex.uz/uz/docs/-97664 — lex.uz lists editions dated 30.12.2026 and 05.02.2027; re-check these articles before those dates ⚠️.
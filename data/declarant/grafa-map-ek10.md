# BYD (GTD) grafa map for EK10 – export

*Generated 2026-11-18 (Asia/Tashkent). Machine-readable twin: `grafa-map-ek10.json`. Import counterpart: `grafa-map.md`. Examples are **SYNTHETIC**.*

**Legal source:** Instruction No. 2773, Chapter 4, points 20–22 – [ch.4 uz](https://lex.uz/uz/docs/2924955#2925089) · [ch.4 ru](https://lex.uz/docs/2924953#2925168); point 21 list [uz](https://lex.uz/uz/docs/2924955#4294922) · [ru](https://lex.uz/docs/2924953#4303369); point 22 [uz](https://lex.uz/uz/docs/2924955#3854674) · [ru](https://lex.uz/docs/2924953#3908316). Edition: Edition with latest change dated 22.07.2026 (amendment 2773-15, https://www.lex.uz/ru/pdfs/8344992) – read 2026-11-18. Regime code 10 = export (Annex 3, [ru](https://lex.uz/docs/2924953#2928883)).

**Point 21 – grafas filled by the declaring person for EK10:** 1, 2, 3, 5, 7 (post code), 8, 9, 11, 12, 13, 14, 17, 17a, 18, 19, 20, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 54, «С».

> Uzbek names are the official Cyrillic headings; Latin = mechanical transliteration (not official). Anchors are lex.uz element ids. ⚠️ = uncertain / our reading.

## Differences vs IM40 (highlight)

- **Only in IM40:** 15, 21, 15a (country of dispatch, border vehicle).
- **Only in EK10:** 17, 17a (country of destination name / code).

| Grafa | IM40 → EK10 |
|---|---|
| **1** | Direction 'ЭК' instead of 'ИМ'; regime 10 instead of 40. |
| **2** | IM40 grafa 2 = FOREIGN consignor (no TIN/district). In EK10 grafa 2 is the UZBEK consignor/exporter with the upper-right status code and the bottom TIN/PINFL + district code (those fields sit in grafa 8 for IM40). |
| **8** | IM40 grafa 8 = Uzbek importer with status code and TIN/district. EK10 grafa 8 = FOREIGN consignee: name + country + address only – the text read has NO TIN/district bottom part and no upper-right status code. |
| **18** | IM40 grafa 18 = vehicle that carried the goods inside Uzbekistan to the clearing post, without the extra carrier/driver/VIN/vehicle-type fields. EK10 adds gross-in-vehicle, vehicle type code, VIN, end-of-carriage country, carrier and driver identity (sub-point 14 as amended by 2773-9, 2023). |
| **20** | EK10-only third subfield: settlement-form code + dispatch-form code. IM40 grafa 20 has no such subfield. |
| **25** | IM40: code of the grafa-21 vehicle that DID cross (not filled for change of regime). EK10 has no grafa 21; grafa 25 is the planned border-crossing vehicle type. |
| **29** | IM40: entry post (already crossed). EK10: planned exit post. |
| **31** | IM40 grafa 31 has lines 1–11 (incl. energy-efficiency class etc.) and the bottom-left shows the importer/consumer side. EK10: lines 1–5; bottom-left = PRODUCER TIN/district (growing district for listed agri codes). |
| **37** | Starts with 10 instead of 40. The IM40 text's remark that customs transit counts as 'no previous regime' is not repeated in point 22 (sub-point 32). |
| **40** | IM40 grafa 40 almost always holds the transit document (ТД …) or delivery-control book (ККДГ/МДП). EK10 grafa 40 only refers to a previous GTD; for goods produced in Uzbekistan it stays empty (our reading). |
| **43** | Same box, different meaning: IM40 '1' = imported for own needs / '0' = not for own needs. EK10 '1' = exporter is the manufacturer / '0' = not the manufacturer. |
| **44** | Same lettered structure a)–h) as IM40; export-specific examples: 702 СПТЭК (export certificate of origin) instead of 701 СПТИМ, 419 ФТСС phytosanitary certificate. Code 904 МЕТОД: see grafa-map.json (IM40) note – not mentioned for EK10 either ⚠️. |
| **45** | Same format; for export the Customs Code rules for EXPORTED goods apply – our pointer: Arts. 315–317 (https://lex.uz/docs/2876354), not the import methods 302–313. |
| **47** | Same columns/СП codes. Payment codes differ: import duty 20/21, import excise 27 and VAT 29 do not arise for export; export duty 25 / export excise 28 only where rates exist (Annex 13: https://lex.uz/docs/2924953#8356110). |
| **C** | IM40 grafa C has a 2nd line (date of import = border stamp date). EK10 has only line 1. |

- **Same as IM40:** 3, 5, 7, 9, 11, 12, 13, 14, 19, 22, 23, 24, 26, 28, 30, 32, 33, 34, 35, 38, 39, 41, 42, 46, 48, 49, 50, 54.

## Grafa table

| Grafa | Name (uz) | Name (ru) | vs IM40 | Format | Source docs | Example (synthetic) | Rule source |
|---|---|---|---|---|---|---|---|
| **1** | Декларация тури<br>*Deklaratsiya turi* | Тип декларации | **DIFFERENT** | 3 subfields: [ЭК] [2-digit regime code] [empty] | calculated | ЭК \| 10 \| | [uz](https://lex.uz/uz/docs/2924955#2925183) · [ru](https://lex.uz/docs/2924953#2925480) (Ch.4, point 22, sub-point 1) |
| **2** | Экспортчи/юкни жўнатувчи<br>*Eksportchi/yukni joʻnatuvchi* | Экспортер/грузоотправитель | **DIFFERENT** | free text, e-GTD separate fields + upper-right code after № + bottom: № TIN/PINFL / district code | contract, invoice, company_profile | «PAXTA TEKS» MChJ (SYNTHETIC), Ташкентская обл., Ташкентский р-н, ул. Навои 1, тел. +998 71 000 00 00 \| № 100000009/1727265 | [uz](https://lex.uz/uz/docs/2924955#2925190) · [ru](https://lex.uz/docs/2924953#2925489) (Ch.4, point 22, sub-point 2) |
| **3** | Қўшимча варақлар<br>*Qoʻshimcha varaqlar* | Добавочные листы | same | "n/N" integers | calculated | 1/1 (1 item) | [uz](https://lex.uz/uz/docs/2924955#2925238) · [ru](https://lex.uz/docs/2924953#2925531) (Ch.4, point 22, sub-point 3) |
| **5** | Товарлар номларининг умумий сони<br>*Tovarlar nomlarining umumiy soni* | Всего наименований товаров | same | integer | calculated | 1 | [uz](https://lex.uz/uz/docs/2924955#2925746) · [ru](https://lex.uz/docs/2924953#2925535) (Ch.4, point 22, sub-point 4) |
| **7** | БЮДнинг рўйхат рақами<br>*BYUDning roʻyxat raqami* | Регистрационный номер ГТД | same | 5-digit post code (declarant); customs appends /DD.MM.YYYY/serial | user_input | 26010 (declarant) | [uz](https://lex.uz/uz/docs/2924955#2925240) · [ru](https://lex.uz/docs/2924953#2925537) (Ch.4, point 22, sub-point 5) |
| **8** | Импортчи/юкни қабул қилувчи<br>*Importchi/yukni qabul qiluvchi* | Импортер/грузополучатель | **DIFFERENT** | free text; e-GTD separate fields per party | cmr, contract, invoice | TOO «Almaty Textile Trade» (SYNTHETIC), Казахстан, г. Алматы, пр. Абая 100 | [uz](https://lex.uz/uz/docs/2924955#2925242) · [ru](https://lex.uz/docs/2924953#2925539) (Ch.4, point 22, sub-point 6) |
| **9** | Молиявий тартибга солиш учун жавобгар шахс<br>*Moliyaviy tartibga solish uchun javobgar shaxs* | Лицо, ответственное за финансовое урегулирование | same | free text + upper code + bottom: № TIN/PINFL / district code | contract, company_profile | «PAXTA TEKS» MChJ (SYNTHETIC) \| № 100000009/1727265 | [uz](https://lex.uz/uz/docs/2924955#2925259) · [ru](https://lex.uz/docs/2924953#2925563) (Ch.4, point 22, sub-point 7) |
| **11** | Савдо қилинаётган мамлакат<br>*Savdo qilinayotgan mamlakat* | Торгующая страна | same | left: 3-digit country code; right: 1 or 2 | contract | 398 \| 2 | [uz](https://lex.uz/uz/docs/2924955#2925264) · [ru](https://lex.uz/docs/2924953#2925570) (Ch.4, point 22, sub-point 8) |
| **12** | Умумий божхона қиймати<br>*Umumiy bojxona qiymati* | Общая таможенная стоимость | same | decimal(2), currency of grafa 22 | calculated |  | [uz](https://lex.uz/uz/docs/2924955#2925268) · [ru](https://lex.uz/docs/2924953#2925577) (Ch.4, point 22, sub-point 9) |
| **13** | (untitled) USD/UZS rate<br>*(untitled) USD/UZS rate* | (untitled) USD/UZS rate | same | decimal: UZS per 1 USD | cbu_rate |  | [uz](https://lex.uz/uz/docs/2924955#2925270) · [ru](https://lex.uz/docs/2924953#2925580) (Ch.4, point 22, sub-point 10) |
| **14** | Декларант/божхона брокери<br>*Deklarant/bojxona brokeri* | Декларант/таможенный брокер | same | free text + upper: № TIN/PINFL | company_profile | «PAXTA TEKS» MChJ (SYNTHETIC) \| № 100000009 | [uz](https://lex.uz/uz/docs/2924955#2925272) · [ru](https://lex.uz/docs/2924953#2925583) (Ch.4, point 22, sub-point 11) |
| **17** | Келиб тушадиган мамлакат<br>*Kelib tushadigan mamlakat* | Страна назначения | **EK10 only** | country short name (Annex 5) | contract, cmr | Казахстан | [uz](https://lex.uz/uz/docs/2924955#2925275) · [ru](https://lex.uz/docs/2924953#2925588) (Ch.4, point 22, sub-point 12) |
| **17a** | Келиб тушадиган мамлакат коди<br>*Kelib tushadigan mamlakat kodi* | Код страны назначения | **EK10 only** | 3-digit numeric (Annex 5) | contract, cmr | 398 | [uz](https://lex.uz/uz/docs/2924955#2925279) · [ru](https://lex.uz/docs/2924953#2925593) (Ch.4, point 22, sub-point 13) |
| **18** | Жўнатиш/етказиб бериш вақтидаги транспорт воситаси<br>*Joʻnatish/yetkazib berish vaqtidagi transport vositasi* | Транспортное средство при отправлении/прибытии | **DIFFERENT** | left: "<count> <TRANSPORT>: plate[/trailer]; ..."; right: country code; e-GTD extra fields | cmr, transport_order, user_input | 1 АВТО: 10A123BC/10XY456 \| 860; extra: 18450.000 кг; 23; VIN XTC00000000000000; 398; carrier «TRANS YO'L» MChJ (SYNTHETIC) TIN 100000010; driver Rahimov Bobur (SYNTHETIC), PINFL 30000000000000, AA0000000 | [uz](https://lex.uz/uz/docs/2924955#2925281) · [ru](https://lex.uz/docs/2924953#2925597) (Ch.4, point 22, sub-point 14) |
| **19** | Контейнер<br>*Konteyner* | Контейнер | same | 0 or 1 | cmr, packing_list | 0 | [uz](https://lex.uz/uz/docs/2924955#2925294) · [ru](https://lex.uz/docs/2924953#2925610) (Ch.4, point 22, sub-point 15) |
| **20** | Етказиб бериш шартлари<br>*Yetkazib berish shartlari* | Условия поставки | **DIFFERENT** | 3 subfields: [numeric Incoterms code] [letter code + place] [settlement form/dispatch form] | contract, invoice | 02 \| FCA Ташкентский р-н \| 10/01 | [uz](https://lex.uz/uz/docs/2924955#5092363) · [ru](https://lex.uz/docs/2924953#5094580) (Ch.4, point 22, sub-point 16) |
| **22** | Валюта ва товарларнинг умумий фактура қиймати<br>*Valyuta va tovarlarning umumiy faktura qiymati* | Валюта и общая фактурная стоимость товаров | same | left: 3-digit currency code; right: decimal(2) | contract, invoice | 840 \| 24000.00 | [uz](https://lex.uz/uz/docs/2924955#2925331) · [ru](https://lex.uz/docs/2924953#2925659) (Ch.4, point 22, sub-point 18) |
| **23** | Валюта курси<br>*Valyuta kursi* | Курс валюты | same | "<nominal>/<rate>" with comma decimals | cbu_rate | 1/12100,00 (EXAMPLE rate, not CBU) | [uz](https://lex.uz/uz/docs/2924955#2925339) · [ru](https://lex.uz/docs/2924953#2925665) (Ch.4, point 22, sub-point 19) |
| **24** | Битим хусусияти<br>*Bitim xususiyati* | Характер сделки | same | left: transaction-nature code; right: 3-digit settlement currency | contract | 01 \| 840 | [uz](https://lex.uz/uz/docs/2924955#2925349) · [ru](https://lex.uz/docs/2924953#2925676) (Ch.4, point 22, sub-point 20) |
| **25** | Чегарадаги транспорт тури<br>*Chegaradagi transport turi* | Вид транспорта на границе | **DIFFERENT** | 2-digit code (Annex 6) | cmr, user_input | 30 | [uz](https://lex.uz/uz/docs/2924955#2925358) · [ru](https://lex.uz/docs/2924953#2925681) (Ch.4, point 22, sub-point 21) |
| **26** | Мамлакат ичкарисидаги транспорт тури<br>*Mamlakat ichkarisidagi transport turi* | Вид транспорта внутри страны | same | 2-digit code | calculated | 30 | [uz](https://lex.uz/uz/docs/2924955#2925365) · [ru](https://lex.uz/docs/2924953#2925686) (Ch.4, point 22, sub-point 22) |
| **28** | Молия ва банк маълумотлари<br>*Moliya va bank maʼlumotlari* | Финансовые и банковские сведения | same | TIN/PINFL | company_profile |  | [uz](https://lex.uz/uz/docs/2924955#7471899) · [ru](https://lex.uz/docs/2924953#7472607) (Ch.4, point 22, sub-point 23) |
| **29** | Чегарадаги божхона<br>*Chegaradagi bojxona* | Таможня на границе | **DIFFERENT** | 5-digit code + name (Annex 4) | user_input, cmr | 27001 Яллама | [uz](https://lex.uz/uz/docs/2924955#2925385) · [ru](https://lex.uz/docs/2924953#2925700) (Ch.4, point 22, sub-point 24) |
| **30** | Товарлар турган жой<br>*Tovarlar turgan joy* | Местонахождение товаров | same | text + (e-GTD) district code | transit_declaration, user_input | Ташкентская обл., Ташкентский р-н, ул. Навои 1 (склад экспортёра) (SYNTHETIC) \| 1727265 | [uz](https://lex.uz/uz/docs/2924955#4628859) · [ru](https://lex.uz/docs/2924953#4631100) (Ch.4, point 22, sub-point 25) |
| **31** | Юк жойлари ва товар тавсифи / Маркировка ва миқдор — контейнерлар рақами — товар тавсифи<br>*Yuk joylari va tovar tavsifi / Markirovka va miqdor — konteynerlar raqami — tovar tavsifi* | Грузовые места и описание товара / Маркировка и количество — номера контейнеров — описание товара | **DIFFERENT** | numbered lines 1–5 + bottom-left producer TIN/district + bottom-right supplementary quantity | invoice, packing_list, classification, company_profile, phytosanitary_certificate | 1) Футболка мужская трикотажная, 100% хлопок, модель PT-01, бренд PAXTA TEKS<br>2) 200 мест, картонные коробки<br> \| 100000009/1727265 \| 4000 шт | [uz](https://lex.uz/uz/docs/2924955#2925407) · [ru](https://lex.uz/docs/2924953#2925712) (Ch.4, point 22, sub-point 26) |
| **32** | Товар №<br>*Tovar №* | Товар № | same | integer | calculated | 1 | [uz](https://lex.uz/uz/docs/2924955#2925453) · [ru](https://lex.uz/docs/2924953#2925732) (Ch.4, point 22, sub-point 27) |
| **33** | Товар коди<br>*Tovar kodi* | Код товара | same | 10 digits, no spaces | classification, invoice | 6109100000 | [uz](https://lex.uz/uz/docs/2924955#2925462) · [ru](https://lex.uz/docs/2924953#2925735) (Ch.4, point 22, sub-point 28) |
| **34** | Келиб чиқиш мамлакати коди<br>*Kelib chiqish mamlakati kodi* | Код страны происхождения | same | 3-digit numeric (or "EU", "000") | certificate_of_origin, invoice | 860 | [uz](https://lex.uz/uz/docs/2924955#2925468) · [ru](https://lex.uz/docs/2924953#2925737) (Ch.4, point 22, sub-point 29) |
| **35** | Брутто вазн (кг)<br>*Brutto vazn (kg)* | Вес брутто (кг) | same | decimal(3) kg | packing_list, cmr | 2150.000 | [uz](https://lex.uz/uz/docs/2924955#2925474) · [ru](https://lex.uz/docs/2924953#2925741) (Ch.4, point 22, sub-point 30) |
| **37** | Процедура<br>*Protsedura* | Процедура | **DIFFERENT** | 7 digits | calculated | 1000000 | [uz](https://lex.uz/uz/docs/2924955#2925801) · [ru](https://lex.uz/docs/2924953#2926444) (Ch.4, point 22, sub-point 32) |
| **38** | Нетто вазн (кг)<br>*Netto vazn (kg)* | Вес нетто (кг) | same | decimal(3) kg | packing_list, invoice | 2000.000 | [uz](https://lex.uz/uz/docs/2924955#2925806) · [ru](https://lex.uz/docs/2924953#2926453) (Ch.4, point 22, sub-point 33) |
| **39** | Квота<br>*Kvota* | Квота | same | quantity + unit | license | (empty) | [uz](https://lex.uz/uz/docs/2924955#2925830) · [ru](https://lex.uz/docs/2924953#2926470) (Ch.4, point 22, sub-point 34) |
| **40** | Умумий декларация/аввалги ҳужжат<br>*Umumiy deklaratsiya/avvalgi hujjat* | Общая декларация/предшествующий документ | **DIFFERENT** | "ГТД post/date/number — item — gross kg — net kg — supp qty" | previous_gtd | (empty – own production, no previous regime) | [uz](https://lex.uz/uz/docs/2924955#2925846) · [ru](https://lex.uz/docs/2924953#2926476) (Ch.4, point 22, sub-point 35) |
| **41** | Қўшимча ўлчов бирлиги<br>*Qoʻshimcha oʻlchov birligi* | Дополнительная единица измерения | same | unit code | classification | 796 (шт) ⚠️ verify unit code | [uz](https://lex.uz/uz/docs/2924955#2925873) · [ru](https://lex.uz/docs/2924953#2926489) (Ch.4, point 22, sub-point 36) |
| **42** | Товарнинг фактура қиймати<br>*Tovarning faktura qiymati* | Фактурная стоимость товара | same | decimal(2), contract currency | invoice | 24000.00 | [uz](https://lex.uz/uz/docs/2924955#2925877) · [ru](https://lex.uz/docs/2924953#2926492) (Ch.4, point 22, sub-point 37) |
| **43** | (untitled) own-production flag<br>*(untitled) own-production flag* | (untitled) own-production flag | **DIFFERENT** | 0 or 1 | company_profile, user_input | 1 | [uz](https://lex.uz/uz/docs/2924955#2925888) · [ru](https://lex.uz/docs/2924953#2926497) (Ch.4, point 22, sub-point 38) |
| **44** | Қўшимча маълумотлар/тақдим этилаётган ҳужжатлар<br>*Qoʻshimcha maʼlumotlar/taqdim etilayotgan hujjatlar* | Дополнительная информация/представляемые документы | ≈ similar | one document per line: "<code> <short> № ... от DD.MM.YYYY" | contract, invoice, cmr, certificates, certificate_of_origin | 202 СМР № UZ-KZ-0001 от 10.12.2026<br>220 ИНВ № PT-2026-001 от 09.12.2026<br>301 КНТ № PT-KZ/01 от 01.10.2026<br>702 СПТЭК № UZKZ00000000 от 09.12.2026 (SYNTHETIC) | [uz](https://lex.uz/uz/docs/2924955#2925897) · [ru](https://lex.uz/docs/2924953#2926501) (Ch.4, point 22, sub-point 39) |
| **45** | Божхона қиймати<br>*Bojxona qiymati* | Таможенная стоимость | ≈ similar | decimal(2), contract currency (right subfield) | invoice, calculated | 24000.00 | [uz](https://lex.uz/uz/docs/2924955#2925968) · [ru](https://lex.uz/docs/2924953#2926538) (Ch.4, point 22, sub-point 40) |
| **46** | Статистик қиймат<br>*Statistik qiymat* | Статистическая стоимость | same | decimal(3), thousand USD | calculated, cbu_rate | 24.000 | [uz](https://lex.uz/uz/docs/2924955#2925980) · [ru](https://lex.uz/docs/2924953#2926543) (Ch.4, point 22, sub-point 41) |
| **47** | Божхона тўловларининг ҳисоби<br>*Bojxona toʻlovlarining hisobi* | Исчисление таможенных платежей | ≈ similar | table rows: Вид \| Основа начисления \| Ставка \| Сумма \| СП | calculated, fee_table | 10 \| 1 ГТД \| <fee per VM 55 band> \| … \| БН | [uz](https://lex.uz/uz/docs/2924955#2925997) · [ru](https://lex.uz/docs/2924953#2926546) (Ch.4, point 22, sub-point 42) |
| **48** | Тўловларни кечиктириш<br>*Toʻlovlarni kechiktirish* | Отсрочка платежей | same | "XX.DD.MM.YYYY" per payment; instalments "ПН.ХХ.ДД.ММ.ГГГГ.СУММА" | customs_decision | (empty) | [uz](https://lex.uz/uz/docs/2924955#2926016) · [ru](https://lex.uz/docs/2924953#2926568) (Ch.4, point 22, sub-point 43) |
| **49** | Омбор номи<br>*Ombor nomi* | Наименование склада | same | licence number and date | user_input | (empty) | [uz](https://lex.uz/uz/docs/2924955#2926298) · [ru](https://lex.uz/docs/2924953#2926574) (Ch.4, point 22, sub-point 44) |
| **50** | Ишонч билдирган шахс<br>*Ishonch bildirgan shaxs* | Доверитель | same | fixed sentence + full name, position, phone, PINFL (+ power of attorney) | company_profile, user_input |  | [uz](https://lex.uz/uz/docs/2924955#2926304) · [ru](https://lex.uz/docs/2924953#2926577) (Ch.4, point 22, sub-point 45) |
| **54** | Жой ва сана<br>*Joy va sana* | Место и дата | same | numbered lines 1–5; GTD own number PINFL/DD.MM.YYYY/serial | company_profile, calculated |  | [uz](https://lex.uz/uz/docs/2924955#3903135) · [ru](https://lex.uz/docs/2924953#3908942) (Ch.4, point 22, sub-point 46) |
| **C** | «С» (untitled)<br>*«S» (untitled)* | «С» (untitled) | **DIFFERENT** | line 1 only | contract | 1) 0000000000 (SYNTHETIC) | [uz](https://lex.uz/uz/docs/2924955#2926362) · [ru](https://lex.uz/docs/2924953#2926601) (Ch.4, point 22, sub-point 48) |

## Filling rules per grafa (summary of the official text, EK10)

### Grafa 1 — Тип декларации / Deklaratsiya turi
- **Rule:** Subfield 1: direction 'ЭК'. Subfield 2: two-digit regime code per Annex 3 (export = 10). Subfield 3 is not filled.
- **vs IM40 (different):** Direction 'ЭК' instead of 'ИМ'; regime 10 instead of 40.
- **Classifier:** Annex 3 – customs regimes (10 = export; https://lex.uz/docs/2924953#2928883)
- **Source:** Ch.4, point 22, sub-point 1 — [uz](https://lex.uz/uz/docs/2924955#2925183), [ru](https://lex.uz/docs/2924953#2925480)

### Grafa 2 — Экспортер/грузоотправитель / Eksportchi/yukni joʻnatuvchi
- **Rule:** Consignor AND exporter (Uzbek side). Same person: individual – full name, permanent address, phone; legal entity – short name, legal address, phone, e-mail (if any). A branch acting for the exporter: branch details, then the legal entity's details. Different persons (consignor ships on the exporter's instruction): consignor name, address, phone, then 'по поручению' + exporter name and address; if grafa 9 already shows the exporter, it need not be repeated here. Upper-right after '№': 00000001 resident individual, 00000002 non-resident individual, 00000003 organisation with state share, 99999999 diplomatic/consular, 88888888 international/government organisation offices, otherwise empty. Bottom after '№': consignor TIN (PINFL for an individual; branch TIN if a branch acts) '/' district (city) code per Annex 15 by legal address; no TIN/PINFL → 999999999. Not filled on additional paper sheets.
- **vs IM40 (different):** IM40 grafa 2 = FOREIGN consignor (no TIN/district). In EK10 grafa 2 is the UZBEK consignor/exporter with the upper-right status code and the bottom TIN/PINFL + district code (those fields sit in grafa 8 for IM40).
- **Classifier:** Annex 15 – districts and cities
- **Checks:** = seller in contract and invoice; TIN 9 digits / PINFL 14 digits; district code exists in Annex 15
- **Source:** Ch.4, point 22, sub-point 2 — [uz](https://lex.uz/uz/docs/2924955#2925190), [ru](https://lex.uz/docs/2924953#2925489)

### Grafa 3 — Добавочные листы / Qoʻshimcha varaqlar
- **Rule:** Sheet number / total sheets incl. main and additional. Paper: main sheet holds 1 item, each additional sheet holds 3 items (point 17), max 33 additional sheets. E-GTD: show the numbers as if printed. No additional sheets → '1/1'.
- **Checks:** N = 1 + ceil((items-1)/3)
- **Source:** Ch.4, point 22, sub-point 3 — [uz](https://lex.uz/uz/docs/2924955#2925238), [ru](https://lex.uz/docs/2924953#2925531)

### Grafa 5 — Всего наименований товаров / Tovarlar nomlarining umumiy soni
- **Rule:** Total number of goods items = number of filled grafa 31 entries. Max 100 items per GTD (point 6).
- **Checks:** = count(items); <= 100
- **Source:** Ch.4, point 22, sub-point 4 — [uz](https://lex.uz/uz/docs/2924955#2925746), [ru](https://lex.uz/docs/2924953#2925535)

### Grafa 7 — Регистрационный номер ГТД / BYUDning roʻyxat raqami
- **Rule:** 5-digit code (Annex 4) of the customs post where the GTD WILL BE filed. Customs completes the registration number (point 90).
- **Classifier:** Annex 4 – customs posts
- **Source:** Ch.4, point 22, sub-point 5 — [uz](https://lex.uz/uz/docs/2924955#2925240), [ru](https://lex.uz/docs/2924953#2925537)

### Grafa 8 — Импортер/грузополучатель / Importchi/yukni qabul qiluvchi
- **Rule:** Person named as consignee in the transport documents (foreign buyer side): individual – full name, residence (country short name per Annex 5 + address); legal entity – short name and location (country short name + address). If the consignee receives on behalf of another person: consignee first, then 'по поручению' + that person. E-GTD: consignee, the person on whose behalf it receives (the contract party with the grafa-9 person) and other persons from the accompanying documents each in its own field. Not filled on additional paper sheets.
- **vs IM40 (different):** IM40 grafa 8 = Uzbek importer with status code and TIN/district. EK10 grafa 8 = FOREIGN consignee: name + country + address only – the text read has NO TIN/district bottom part and no upper-right status code.
- **Checks:** = CMR box 2 consignee; = buyer in contract (or 'по поручению' chain)
- ⚠️ **Uncertain:** Whether the live ed2 form still shows a TIN field for the foreign consignee – not described in point 22 ⚠️.
- **Source:** Ch.4, point 22, sub-point 6 — [uz](https://lex.uz/uz/docs/2924955#2925242), [ru](https://lex.uz/docs/2924953#2925539)

### Grafa 9 — Лицо, ответственное за финансовое урегулирование / Moliyaviy tartibga solish uchun javobgar shaxs
- **Rule:** Person who concluded the foreign-trade contract and is responsible for settlements: name, legal address, phone, e-mail (legal entity) or full name, residence, phone (individual). Upper '№' codes as in grafa 8 (00000001/00000002/00000003/99999999/88888888 or empty). Bottom: TIN (PINFL for an individual) / district code (Annex 15); none → 999999999. Not filled for gratuitous supplies.
- **Checks:** = seller/exporter in contract; = grafa 2 exporter (if same person)
- **Source:** Ch.4, point 22, sub-point 7 — [uz](https://lex.uz/uz/docs/2924955#2925259), [ru](https://lex.uz/docs/2924953#2925563)

### Grafa 11 — Торгующая страна / Savdo qilinayotgan mamlakat
- **Rule:** Left: numeric code (Annex 5) of the country where the counterparty that signed the contract with the grafa-9 person is registered/resides. If no contract – per accompanying documents. Right: '1' if that country/territory is on the offshore list approved by MoJ reg. No. 2467 of 12.06.2013, otherwise '2'.
- **Classifier:** Annex 5 – countries; offshore list reg. No. 2467
- **Checks:** buyer country in contract = code
- **Notes:** Offshore list must be loaded as a separate reference table (not in this file).
- **Source:** Ch.4, point 22, sub-point 8 — [uz](https://lex.uz/uz/docs/2924955#2925264), [ru](https://lex.uz/docs/2924953#2925570)

### Grafa 12 — Общая таможенная стоимость / Umumiy bojxona qiymati
- **Rule:** Total customs value = sum of grafa 45 of all items, in the grafa-22 currency.
- **Checks:** = Σ grafa 45 (exact)
- **Source:** Ch.4, point 22, sub-point 9 — [uz](https://lex.uz/uz/docs/2924955#2925268), [ru](https://lex.uz/docs/2924953#2925577)

### Grafa 13 — (untitled) USD/UZS rate / (untitled) USD/UZS rate
- **Rule:** US dollar rate to UZS set by the Central Bank on the date the GTD is accepted for clearance.
- **Notes:** Rate date = acceptance date, which the product cannot know in advance → recompute at filing (Customs Code Art. 326).
- **Source:** Ch.4, point 22, sub-point 10 — [uz](https://lex.uz/uz/docs/2924955#2925270), [ru](https://lex.uz/docs/2924953#2925580)

### Grafa 14 — Декларант/таможенный брокер / Deklarant/bojxona brokeri
- **Rule:** Customs broker or declarant (legal entity) that filled in and files the GTD: short name, legal address, phone, e-mail; individual declarant: full name, address, phone, e-mail. Upper '№': TIN (PINFL for an individual). For YuklaGo self-filing this is the importer itself.
- **Source:** Ch.4, point 22, sub-point 11 — [uz](https://lex.uz/uz/docs/2924955#2925272), [ru](https://lex.uz/docs/2924953#2925583)

### Grafa 17 — Страна назначения / Kelib tushadigan mamlakat
- **Rule:** Short name of the country of destination = the last country to which the goods are to be delivered.
- **vs IM40 (ek10_only):** Not used for IM40 (IM40 uses 15/15a country of dispatch instead).
- **Classifier:** Annex 5 – countries
- **Source:** Ch.4, point 22, sub-point 12 — [uz](https://lex.uz/uz/docs/2924955#2925275), [ru](https://lex.uz/docs/2924953#2925588)

### Grafa 17a — Код страны назначения / Kelib tushadigan mamlakat kodi
- **Rule:** Numeric code of the destination country.
- **vs IM40 (ek10_only):** Not used for IM40.
- **Classifier:** Annex 5 – countries
- **Checks:** = code of grafa 17 name
- **Source:** Ch.4, point 22, sub-point 13 — [uz](https://lex.uz/uz/docs/2924955#2925279), [ru](https://lex.uz/docs/2924953#2925593)

### Grafa 18 — Транспортное средство при отправлении/прибытии / Joʻnatish/yetkazib berish vaqtidagi transport vositasi
- **Rule:** Vehicle(s) on which the goods are loaded for delivery to the border crossing point (or, if transhipped before the border, to the transhipment place). Left: number of vehicles, space, short transport name (Annex 6), colon, identifiers separated by ';' (vessel name, flight, wagon no., plate …); road trains: trailers after '/'. Right: numeric country code of the vehicle (of the tractor unit for road trains); several countries → '999' (paper: 'см. на обороте'; e-GTD: no reference, all data in fields). Pipeline / power line: 'ТРУБОПРОВОД' / 'ЛЭП'. Additionally (e-GTD separate fields): gross kg of goods in the vehicle; 2-digit vehicle type code (10 car ≤8 seats, 21 truck ≤10 t, 22 truck 10–20 t, 23 truck >20 t, 31/32/33 buses by seats, 40 minibus, 50 tractor, 60 motorcycle, 70 special); VIN; numeric code of the country where carriage ends; carrier (individual: full name, PINFL, passport series/no.; legal entity: name, TIN) and driver (full name, PINFL, passport). Non-resident carrier/driver without TIN/PINFL → '99999999999999'.
- **vs IM40 (different):** IM40 grafa 18 = vehicle that carried the goods inside Uzbekistan to the clearing post, without the extra carrier/driver/VIN/vehicle-type fields. EK10 adds gross-in-vehicle, vehicle type code, VIN, end-of-carriage country, carrier and driver identity (sub-point 14 as amended by 2773-9, 2023).
- **Classifier:** Annex 6 – transport types; Annex 5 – countries
- **Checks:** plate = CMR box 25; gross in vehicle ≥ Σ grafa 35 of this GTD
- ⚠️ **Uncertain:** The vehicle-type code list in the text read ends at '70'; check ed2 for further codes ⚠️.
- **Source:** Ch.4, point 22, sub-point 14 — [uz](https://lex.uz/uz/docs/2924955#2925281), [ru](https://lex.uz/docs/2924953#2925597)

### Grafa 19 — Контейнер / Konteyner
- **Rule:** '0' – not in a container; '1' – in a container or the container itself is declared as goods.
- **Source:** Ch.4, point 22, sub-point 15 — [uz](https://lex.uz/uz/docs/2924955#2925294), [ru](https://lex.uz/docs/2924953#2925610)

### Grafa 20 — Условия поставки / Yetkazib berish shartlari
- **Rule:** 1st: numeric delivery-terms code (Annex 7). 2nd: letter code + geographic place. 3rd (per contract): 2-digit settlement form, '/', 2-digit dispatch form (separate e-GTD fields). Settlement form: 10 prepayment; 20 letter of credit; 30 bank guarantee; 40 export-contract insurance policy (political & commercial risks); 50 payment after export; 60 consignment; 70 barter; 80 free-of-charge. Mixed forms → the one with the largest absolute amount. Dispatch form: 01 goods sent directly to the contract party; 02 not sent directly to the contract party. Gratuitous supplies: terms from accompanying documents.
- **vs IM40 (different):** EK10-only third subfield: settlement-form code + dispatch-form code. IM40 grafa 20 has no such subfield.
- **Classifier:** Annex 7 – delivery terms
- **Checks:** Incoterms = contract = invoice; settlement form consistent with contract payment terms
- ⚠️ **Uncertain:** No Annex 7 code for Incoterms 2020 DPU (same issue as IM40) ⚠️.
- **Source:** Ch.4, point 22, sub-point 16 — [uz](https://lex.uz/uz/docs/2924955#5092363), [ru](https://lex.uz/docs/2924953#5094580)

### Grafa 22 — Валюта и общая фактурная стоимость товаров / Valyuta va tovarlarning umumiy faktura qiymati
- **Rule:** Left: numeric code (Annex 8) of the contract currency (currency in which goods are priced). Right: total invoice value of the consignment = Σ grafa 42.
- **Classifier:** Annex 8 – currencies (840 USD, 156 CNY, 949 TRY, 860 UZS)
- **Checks:** = Σ grafa 42 (exact); = invoice total; currency = contract currency
- **Source:** Ch.4, point 22, sub-point 18 — [uz](https://lex.uz/uz/docs/2924955#2925331), [ru](https://lex.uz/docs/2924953#2925659)

### Grafa 23 — Курс валюты / Valyuta kursi
- **Rule:** CBU rate of the grafa-22 currency to UZS on the date of GTD acceptance, written as nominal/rate, e.g. '1/63,41', '10/220,09'; UZS contract → '1/1'.
- **Source:** Ch.4, point 22, sub-point 19 — [uz](https://lex.uz/uz/docs/2924955#2925339), [ru](https://lex.uz/docs/2924953#2925665)

### Grafa 24 — Характер сделки / Bitim xususiyati
- **Rule:** Left: transaction nature code per Annex 9 (01 = ordinary trade with settlement in national or foreign currency). Right: numeric code of the currency in which the grafa-9 party settles with the counterparty.
- **Classifier:** Annex 9 – nature of transaction
- **Source:** Ch.4, point 22, sub-point 20 — [uz](https://lex.uz/uz/docs/2924955#2925349), [ru](https://lex.uz/docs/2924953#2925676)

### Grafa 25 — Вид транспорта на границе / Chegaradagi transport turi
- **Rule:** Transport type code of the vehicle on which the goods WILL actually cross the Uzbek customs border.
- **vs IM40 (different):** IM40: code of the grafa-21 vehicle that DID cross (not filled for change of regime). EK10 has no grafa 21; grafa 25 is the planned border-crossing vehicle type.
- **Classifier:** Annex 6 – transport types
- **Source:** Ch.4, point 22, sub-point 21 — [uz](https://lex.uz/uz/docs/2924955#2925358), [ru](https://lex.uz/docs/2924953#2925681)

### Grafa 26 — Вид транспорта внутри страны / Mamlakat ichkarisidagi transport turi
- **Rule:** Transport type code (Annex 6) of the grafa-18 vehicle.
- **Classifier:** Annex 6
- **Source:** Ch.4, point 22, sub-point 22 — [uz](https://lex.uz/uz/docs/2924955#2925365), [ru](https://lex.uz/docs/2924953#2925686)

### Grafa 28 — Финансовые и банковские сведения / Moliya va bank maʼlumotlari
- **Rule:** TIN (PINFL for an individual) of the payer of customs payments; if a non-resident pays – TIN/PINFL of the broker or declarant.
- **Source:** Ch.4, point 22, sub-point 23 — [uz](https://lex.uz/uz/docs/2924955#7471899), [ru](https://lex.uz/docs/2924953#7472607)

### Grafa 29 — Таможня на границе / Chegaradagi bojxona
- **Rule:** Code and name of the customs post through which the goods WILL leave Uzbekistan. Pipeline / power line: the control post.
- **vs IM40 (different):** IM40: entry post (already crossed). EK10: planned exit post.
- **Classifier:** Annex 4 – customs posts
- **Source:** Ch.4, point 22, sub-point 24 — [uz](https://lex.uz/uz/docs/2924955#2925385), [ru](https://lex.uz/docs/2924953#2925700)

### Grafa 30 — Местонахождение товаров / Tovarlar turgan joy
- **Rule:** Location of goods at filing: customs or free warehouse / duty-free shop → number and date of its licence; place without customs-warehouse status → postal address (no postcode); railway station → its name. E-GTD: separate field with district (city) code per Annex 15.
- **Classifier:** Annex 15
- **Source:** Ch.4, point 22, sub-point 25 — [uz](https://lex.uz/uz/docs/2924955#4628859), [ru](https://lex.uz/docs/2924953#4631100)

### Grafa 31 — Грузовые места и описание товара / Маркировка и количество — номера контейнеров — описание товара / Yuk joylari va tovar tavsifi / Markirovka va miqdor — konteynerlar raqami — tovar tavsifi
- **Rule:** Description sufficient for unambiguous 10-digit classification; each element on a new numbered line. 1: trade name, trademark/brand, model, article, grade, standards, technical and commercial characteristics, composition (e-GTD: brand in separate field; 'без марки'/'без бренда' if none); parameters in other units and production date if needed for payments or prohibitions/restrictions. The generic heading text of the TN VED is not allowed. 2: packages – number of packages, packing type and number of packings ('часть коробки' if not whole); bulk: 01 насыпью, 02 навалом, 03 наливом; not filled for pipeline/power line. 3: container numbers ('часть' if partly). 4: excise stamps – series, numbers (ranges with hyphen) and quantity. 5: pipeline/power line: 'Поставка в период с … по …'. Bottom-left (separate field): TIN (PINFL) of the PRODUCER (manufacturer/grower) '/' district code (Annex 15) by legal address; for HS 07, 08, 0904, 1202, 1008, 1207409000, 2008191900 the district where the produce was GROWN per the phytosanitary certificate – one item per district if several. Producer unknown or several producers → consignor's TIN (PINFL) and territory code. Bottom-right: quantity in supplementary unit + symbol (code in grafa 41; e-GTD quantity only); 2 decimals, <0.01 → 6 decimals; kg-only codes → empty.
- **vs IM40 (different):** IM40 grafa 31 has lines 1–11 (incl. energy-efficiency class etc.) and the bottom-left shows the importer/consumer side. EK10: lines 1–5; bottom-left = PRODUCER TIN/district (growing district for listed agri codes).
- **Checks:** packages = packing list = CMR; quantity = invoice = packing list; producer TIN present
- ⚠️ **Uncertain:** Lines 6–11 of IM40 are absent from point 22 in the edition read; confirm ed2 does not require them for EK10 ⚠️.
- **Source:** Ch.4, point 22, sub-point 26 — [uz](https://lex.uz/uz/docs/2924955#2925407), [ru](https://lex.uz/docs/2924953#2925712)

### Grafa 32 — Товар № / Tovar №
- **Rule:** Sequential number of the item declared in grafa 31; single item → '1'.
- **Source:** Ch.4, point 22, sub-point 27 — [uz](https://lex.uz/uz/docs/2924955#2925453), [ru](https://lex.uz/docs/2924953#2925732)

### Grafa 33 — Код товара / Tovar kodi
- **Rule:** 10-digit TN VED (TIF TN) code of the grafa-31 goods, written without spaces or separators (left part).
- **Checks:** code exists in the TN VED; first 6 digits vs invoice HS – warn on mismatch
- **Notes:** Right part of grafa 33 is not described in point 22 for EK10 – leave empty unless the cabinet requires it ⚠️.
- **Source:** Ch.4, point 22, sub-point 28 — [uz](https://lex.uz/uz/docs/2924955#2925462), [ru](https://lex.uz/docs/2924953#2925735)

### Grafa 34 — Код страны происхождения / Kelib chiqish mamlakati kodi
- **Rule:** Left: numeric origin-country code (Annex 5). Unknown at clearance → '000'. Certificate naming only the European Union → 'EU' (Latin).
- **Classifier:** Annex 5
- **Checks:** = certificate of origin (702 СПТЭК) country, if issued; = invoice origin
- **Notes:** For own-produced Uzbek goods normally 860 (UZ).
- **Source:** Ch.4, point 22, sub-point 29 — [uz](https://lex.uz/uz/docs/2924955#2925468), [ru](https://lex.uz/docs/2924953#2925737)

### Grafa 35 — Вес брутто (кг) / Brutto vazn (kg)
- **Rule:** Gross mass in kg of the grafa-31 goods: total mass incl. all packaging needed to keep goods intact until they enter circulation, EXCLUDING containers and other transport equipment. Round mathematically to 3 decimals (<1 g → 6 decimals).
- **Checks:** Σ grafa 35 vs CMR gross (box 11); Σ grafa 35 = packing list gross; gross ≥ net
- **Notes:** Gross excludes containers and other transport equipment (sub-point 30); pallets not stated ⚠️.
- **Source:** Ch.4, point 22, sub-point 30 — [uz](https://lex.uz/uz/docs/2924955#2925474), [ru](https://lex.uz/docs/2924953#2925741)

### Grafa 37 — Процедура / Protsedura
- **Rule:** Procedure code = declared regime (2 digits, Annex 3) + previous regime (2 digits; '00' if none) + movement-feature code (3 digits, Annex 11).
- **vs IM40 (different):** Starts with 10 instead of 40. The IM40 text's remark that customs transit counts as 'no previous regime' is not repeated in point 22 (sub-point 32).
- **Classifier:** Annex 3, Annex 11
- ⚠️ **Uncertain:** '000' = no movement feature is our reading of Annex 11 (as for IM40) ⚠️.
- **Source:** Ch.4, point 22, sub-point 32 — [uz](https://lex.uz/uz/docs/2924955#2925801), [ru](https://lex.uz/docs/2924953#2926444)

### Grafa 38 — Вес нетто (кг) / Netto vazn (kg)
- **Rule:** Net mass in kg: without any packaging, except primary packaging in which goods are sold at retail and/or which cannot be separated before use without loss of consumer properties (e.g. coffee in a can). Bulk goods → total mass. Round to 3 decimals.
- **Checks:** net ≤ gross; = packing list net; = invoice net
- **Source:** Ch.4, point 22, sub-point 33 — [uz](https://lex.uz/uz/docs/2924955#2925806), [ru](https://lex.uz/docs/2924953#2926453)

### Grafa 39 — Квота / Kvota
- **Rule:** Only for goods under quantitative restrictions: remaining quota per licence, not counting the goods now declared.
- **Source:** Ch.4, point 22, sub-point 34 — [uz](https://lex.uz/uz/docs/2924955#2925830), [ru](https://lex.uz/docs/2924953#2926470)

### Grafa 40 — Общая декларация/предшествующий документ / Umumiy deklaratsiya/avvalgi hujjat
- **Rule:** Only if the goods were under ANOTHER customs regime before export: code 'ГТД', previous GTD registration number, item number (grafa 32), gross kg, net kg, supplementary quantity + symbol. Goods previously split over several GTDs → one line per GTD. Example from the text: 'ГТД 14010/31.03.2012/0353761 — 2 — 5980 кг — 5900 кг — 250,2 м3'.
- **vs IM40 (different):** IM40 grafa 40 almost always holds the transit document (ТД …) or delivery-control book (ККДГ/МДП). EK10 grafa 40 only refers to a previous GTD; for goods produced in Uzbekistan it stays empty (our reading).
- ⚠️ **Uncertain:** 'Empty when no previous regime' is our reading of 'Если товары до заявляемого таможенного режима были помещены…' – confirm on ed2 ⚠️.
- **Source:** Ch.4, point 22, sub-point 35 — [uz](https://lex.uz/uz/docs/2924955#2925846), [ru](https://lex.uz/docs/2924953#2926476)

### Grafa 41 — Дополнительная единица измерения / Qoʻshimcha oʻlchov birligi
- **Rule:** Code of the supplementary unit (TN VED 'table of units') for the quantity in grafa 31 bottom-right; empty if only kg applies.
- **Notes:** Supplementary unit per code is in data/tariff/tiftn_codes_pq181_annex1.csv; the numeric unit code table is not in this file ⚠️.
- **Source:** Ch.4, point 22, sub-point 36 — [uz](https://lex.uz/uz/docs/2924955#2925873), [ru](https://lex.uz/docs/2924953#2926489)

### Grafa 42 — Фактурная стоимость товара / Tovarning faktura qiymati
- **Rule:** Invoice value of the item actually paid or payable (or compensated by counter-deliveries) per the contract, in contract currency; gratuitous/no contract → per accompanying documents. Round to 2 decimals.
- **Checks:** = Σ invoice lines for this item; Σ = grafa 22
- **Source:** Ch.4, point 22, sub-point 37 — [uz](https://lex.uz/uz/docs/2924955#2925877), [ru](https://lex.uz/docs/2924953#2926492)

### Grafa 43 — (untitled) own-production flag / (untitled) own-production flag
- **Rule:** '0' – the consignor exports goods NOT of its own production; '1' – the consignor exports goods of its OWN production.
- **vs IM40 (different):** Same box, different meaning: IM40 '1' = imported for own needs / '0' = not for own needs. EK10 '1' = exporter is the manufacturer / '0' = not the manufacturer.
- **Checks:** if 1: grafa 31 bottom-left producer TIN should equal grafa 2 TIN
- ⚠️ **Uncertain:** The rule speaks of the 'грузоотправитель' (consignor); if consignor ≠ exporter, which party's production counts is not stated ⚠️.
- **Source:** Ch.4, point 22, sub-point 38 — [uz](https://lex.uz/uz/docs/2924955#2925888), [ru](https://lex.uz/docs/2924953#2926497)

### Grafa 44 — Дополнительная информация/представляемые документы / Qoʻshimcha maʼlumotlar/taqdim etilayotgan hujjatlar
- **Rule:** Documents for each item with Annex-12 code (each on a new line): a) licence (101 ЛИЦЕНЗИЯ … срок); b) transport and commercial documents (e.g. 202 СМР, 205 АВИА, 220 ИНВ); c) contract (301 КНТ) and the transport contract with a non-resident carrier + its e-system ID; d) permits/certificates of other authorities (417 ССТ, 419 ФТСС phytosanitary …); e) registration of the contract / individual-entrepreneur certificate (501, 502); f) benefit: '6' + payment code (Annex 13) + Annex-14 act code (empty if no exemption or no rate); g) certificate of origin – export example 702 СПТЭК; h) other documents (deferral, commission/pledge contract, fine decision or 'form-2', etc.).
- **vs IM40 (similar):** Same lettered structure a)–h) as IM40; export-specific examples: 702 СПТЭК (export certificate of origin) instead of 701 СПТИМ, 419 ФТСС phytosanitary certificate. Code 904 МЕТОД: see grafa-map.json (IM40) note – not mentioned for EK10 either ⚠️.
- **Classifier:** Annex 12 – document types; Annex 13; Annex 14
- **Checks:** contract, invoice and CMR present; certificate of origin present if buyer needs preference
- **Source:** Ch.4, point 22, sub-point 39 — [uz](https://lex.uz/uz/docs/2924955#2925897), [ru](https://lex.uz/docs/2924953#2926501)

### Grafa 45 — Таможенная стоимость / Bojxona qiymati
- **Rule:** Right subfield: customs value of the item in the contract currency (gratuitous / no contract → currency of accompanying documents), determined under the Customs Code. Rounded to 2 decimals.
- **vs IM40 (similar):** Same format; for export the Customs Code rules for EXPORTED goods apply – our pointer: Arts. 315–317 (https://lex.uz/docs/2876354), not the import methods 302–313.
- ⚠️ **Uncertain:** Left subfield not described (as for IM40) ⚠️.
- **Source:** Ch.4, point 22, sub-point 40 — [uz](https://lex.uz/uz/docs/2924955#2925968), [ru](https://lex.uz/docs/2924953#2926538)

### Grafa 46 — Статистическая стоимость / Statistik qiymat
- **Rule:** Statistical value in thousand USD, converted from grafa 45 at the CBU rate on the GTD acceptance date, rounded to 3 decimals.
- **Source:** Ch.4, point 22, sub-point 41 — [uz](https://lex.uz/uz/docs/2924955#2925980), [ru](https://lex.uz/docs/2924953#2926543)

### Grafa 47 — Исчисление таможенных платежей / Bojxona toʻlovlarining hisobi
- **Rule:** Per item and per payment type; the clearance fee always on the main sheet / item 1. 'Вид' = Annex 13 code – for export typically 10 (clearance fee); 25 export customs duty and 28 excise on exported goods only where a rate is set. 'Основа' in UZS (grafa 12/45 at CBU rate on acceptance date) unless set in foreign currency or non-money units. 'Ставка' = applied rate. 'Сумма' in UZS (or foreign currency if law requires). 'СП' codes as IM40 (БН, КТ, … ОП deferral, РП instalments, ВЗ VAT offset, ОО no payment). No row if no rate, zero rate, or the regime creates no obligation.
- **vs IM40 (similar):** Same columns/СП codes. Payment codes differ: import duty 20/21, import excise 27 and VAT 29 do not arise for export; export duty 25 / export excise 28 only where rates exist (Annex 13: https://lex.uz/docs/2924953#8356110).
- **Classifier:** Annex 13 – customs payments
- ⚠️ **Uncertain:** Export clearance fee band/amount not re-checked here – use data/tariff/fees.json and confirm it applies to export ⚠️.
- **Source:** Ch.4, point 22, sub-point 42 — [uz](https://lex.uz/uz/docs/2924955#2925997), [ru](https://lex.uz/docs/2924953#2926546)

### Grafa 48 — Отсрочка платежей / Toʻlovlarni kechiktirish
- **Rule:** Deferral: payment code + final due date per payment type, one line each. Instalments: month no., payment code, due date, amount per instalment, one line each.
- **Source:** Ch.4, point 22, sub-point 43 — [uz](https://lex.uz/uz/docs/2924955#2926016), [ru](https://lex.uz/docs/2924953#2926568)

### Grafa 49 — Наименование склада / Ombor nomi
- **Rule:** Number and date of the customs/free warehouse licence if the goods were previously placed under a regime involving storage there; otherwise not filled.
- **Source:** Ch.4, point 22, sub-point 44 — [uz](https://lex.uz/uz/docs/2924955#2926298), [ru](https://lex.uz/docs/2924953#2926574)

### Grafa 50 — Доверитель / Ishonch bildirgan shaxs
- **Rule:** Text: 'Ответственность за представленные документы и сведения несет …' + full name, position, phone, PINFL (separate e-GTD field) of the person responsible – the declarant or its authorised person. Non-resident without PINFL → 14 nines. If an authorised person: number, date and validity of the contract/power of attorney.
- **Source:** Ch.4, point 22, sub-point 45 — [uz](https://lex.uz/uz/docs/2924955#2926304), [ru](https://lex.uz/docs/2924953#2926577)

### Grafa 54 — Место и дата / Joy va sana
- **Rule:** Declaring person filing on behalf of the grafa-14 person: 1 place of filling; 2 full name + e-mail; 3 phone; 4 (broker only) number/date of broker–client contract; 5 declarant's own GTD number '99999999999999/99.99.9999/999999' = PINFL / filling date / serial number increasing within the year (restarts each year, never repeated). E-GTD authenticity is certified by the declaring person's ЭЦП (ERI).
- **Checks:** serial unique within year
- **Notes:** 'Declaring person' = declarant filing itself or a customs-clearance specialist employed by the declarant/broker (point 1).
- **Source:** Ch.4, point 22, sub-point 46 — [uz](https://lex.uz/uz/docs/2924955#3903135), [ru](https://lex.uz/docs/2924953#3908942)

### Grafa C — «С» (untitled) / «S» (untitled)
- **Rule:** 1: identification number of the foreign-trade contract in the Unified Electronic Information System of Foreign Trade Operations.
- **vs IM40 (different):** IM40 grafa C has a 2nd line (date of import = border stamp date). EK10 has only line 1.
- **Source:** Ch.4, point 22, sub-point 48 — [uz](https://lex.uz/uz/docs/2924955#2926362), [ru](https://lex.uz/docs/2924953#2926601)

## Not filled by the declarant for EK10

Every grafa not in the point-21 list (e.g. 4, 6, 10, 15, 15a, 16, 21, 27, 36, 51–53) is not filled by the declaring person for EK10.

## Filled by customs only (same as IM40, points 89–90)

- **7 (number part)**: 99999/DD.MM.YYYY/9999999 – post code / acceptance date / serial number of the post's GTDs in the year
- **A**: paper additional sheets only: registration number from grafa 7
- **B**: e-GTD only: per payment code, total amount over all items; exemptions shown with 'без оплаты'
- **D**: customs decision marks; filling grafa D completes clearance (point 13)

## Related law (lex.uz)

- Customs Code Arts. 29–31 (export regime, conditions, documents) – https://lex.uz/docs/2876354
- Customs Code Art. 19 (documents on exit) – https://lex.uz/docs/2876354
- Customs Code Arts. 315–317 – https://lex.uz/docs/2876354

## Uncertainties

- Point 22 sub-points 17, 31 and 47 are absent in the edition read (numbering jumps 16→18, 30→32, 46→48); presumably repealed or empty ⚠️.
- Grafa 8: Whether the live ed2 form still shows a TIN field for the foreign consignee – not described in point 22 ⚠️.
- Grafa 18: The vehicle-type code list in the text read ends at '70'; check ed2 for further codes ⚠️.
- Grafa 20: No Annex 7 code for Incoterms 2020 DPU (same issue as IM40) ⚠️.
- Grafa 31: Lines 6–11 of IM40 are absent from point 22 in the edition read; confirm ed2 does not require them for EK10 ⚠️.
- Grafa 37: '000' = no movement feature is our reading of Annex 11 (as for IM40) ⚠️.
- Grafa 40: 'Empty when no previous regime' is our reading of 'Если товары до заявляемого таможенного режима были помещены…' – confirm on ed2 ⚠️.
- Grafa 43: The rule speaks of the 'грузоотправитель' (consignor); if consignor ≠ exporter, which party's production counts is not stated ⚠️.
- Grafa 45: Left subfield not described (as for IM40) ⚠️.
- Grafa 47: Export clearance fee band/amount not re-checked here – use data/tariff/fees.json and confirm it applies to export ⚠️.
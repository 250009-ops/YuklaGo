# BYD (GTD) grafa map – IM40 (release for free circulation / import)

*Generated 2026-11-18 (Asia/Tashkent). Machine-readable twin: `grafa-map.json`. All example values are **SYNTHETIC**.*

**Legal source:** Инструкция о порядке заполнения грузовой таможенной декларации (рег. № 2773 от 06.04.2016) / Божхона юк декларациясини тўлдириш тартиби тўғрисидаги йўриқнома (рўйхат рақами 2773, 06.04.2016). Uzbek: https://lex.uz/uz/docs/2924955 · Russian: https://lex.uz/docs/2924953. Edition read: Edition with latest change dated 22.07.2026 (amendment 2773-15, https://www.lex.uz/ru/pdfs/8344992) – read 2026-11-18. Import = Chapter 5, points 23–25 ([uz](https://lex.uz/uz/docs/2924955#2926366), [ru](https://lex.uz/docs/2924953#2926603)). Customs-filled grafas: points 89–90 ([ru](https://lex.uz/docs/2924953#5095336)).

> Uzbek names are the official Cyrillic headings; the Latin column is a mechanical transliteration (not official). Anchors (#id) are lex.uz element ids.

## General rules the engine must enforce

- Grafas filled by the declaring person for IM40: 1, 2, 3, 5, 7 (post code), 8, 9, 11, 12, 13, 14, 15, 15а, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 54, «С». — [point 24](https://lex.uz/docs/2924953#4307061)
- Customs fills: 7 (registration number), 44 (its own documents e.g. inspection act), 47 (fees for out-of-hours/out-of-place clearance), «А» (paper additional sheets only), «В» (e-GTD only: totals per payment code; exemptions marked 'без оплаты'), «D» (decision marks). — [points 89–90](https://lex.uz/docs/2924953#5095336)
- Declaration is electronic via the e-declaration system, signed with the declaring person's ЭЦП; all data go into the e-GTD fields/detail tables – no references to other grafas or attachments. — [points 1–3, 15](https://lex.uz/docs/2924953#2925105)
- One GTD may cover goods sent from one consignor to one consignee under one transport document and one regime (road: several transport documents allowed only under the extra conditions of point 4). Different regimes → separate GTDs. — [point 4](https://lex.uz/docs/2924953#6540088)
- Max 100 goods items per GTD. — [point 6](https://lex.uz/docs/2924953#2925124)
- One item = goods of one name, type and brand, one 10-digit code, one origin (or one economic union / unknown), same tariff and non-tariff treatment. — [point 7](https://lex.uz/docs/2924953)
- Consumer goods (except TN VED 4901, 4902, 4908–4911) not for own needs, same code but different names, trademarks, brands, models or specs → declared as separate items. Pharma (group 30) and 9018: extra mandatory attributes. — [point 8](https://lex.uz/docs/2924953)
- Fill in Uzbek or Russian; no erasures; names written in Latin/other scripts in source docs go in Latin letters, Cyrillic names stay Cyrillic. — [points 9, 11](https://lex.uz/docs/2924953#2925128)
- No information not provided for by the Instruction may be entered. — [point 10](https://lex.uz/docs/2924953)
- Not using available payment benefits/preferences and not reflecting them in the GTD is also treated as a deficiency at pre-check. — [point 12](https://lex.uz/docs/2924953#5846975)
- Declarant keeps the GTD and supporting documents for the period of Customs Code Art. 184 part 3: three years from the year following the year in which goods lost the status of goods under customs control. — [point 14; Customs Code Art. 184](https://lex.uz/docs/2876354)

## Grafa table

| Grafa | Name (uz) | Name (ru) | Level | Filled by | Format | Source docs | Example (synthetic) | Rule source |
|---|---|---|---|---|---|---|---|---|
| **1** | Декларация тури<br>*Deklaratsiya turi* | Тип декларации | header | declarant | 3 subfields: [IM] [2-digit regime code] [empty] | calculated | ИМ \| 40 \| | [uz](https://lex.uz/uz/docs/2924955#2926375) · [ru](https://lex.uz/docs/2924953#2926607) (Ch.5, point 25, sub-point 1) |
| **2** | Экспортчи/юкни жўнатувчи<br>*Eksportchi/yukni joʻnatuvchi* | Экспортер/грузоотправитель | header | declarant | free text, separate e-GTD fields per party | cmr, invoice, contract | Foshan Mingde Furniture Co., Ltd. (SYNTHETIC), Китай, Guangdong, Foshan, Shunde, Longjiang Rd 88 | [uz](https://lex.uz/uz/docs/2924955#2926379) · [ru](https://lex.uz/docs/2924953#2926611) (Ch.5, point 25, sub-point 2) |
| **3** | Қўшимча варақлар<br>*Qoʻshimcha varaqlar* | Добавочные листы | header | declarant | "n/N" integers | calculated | 1/2 (2 items) | [uz](https://lex.uz/uz/docs/2924955#2926406) · [ru](https://lex.uz/docs/2924953#2926628) (Ch.5, point 25, sub-point 3) |
| **5** | Товарлар номларининг умумий сони<br>*Tovarlar nomlarining umumiy soni* | Всего наименований товаров | header | declarant | integer | calculated | 2 | [uz](https://lex.uz/uz/docs/2924955#2926632) · [ru](https://lex.uz/docs/2924953#2927231) (Ch.5, point 25, sub-point 4) |
| **7** | БЮДнинг рўйхат рақами<br>*BYUDning roʻyxat raqami* | Регистрационный номер ГТД | header | declarant+customs | 5-digit post code (declarant); customs appends /DD.MM.YYYY/serial | user_input | 26010 (declarant) → 26010/27.11.2026/0001234 (customs) | [uz](https://lex.uz/uz/docs/2924955#2926634) · [ru](https://lex.uz/docs/2924953#2927233) (Ch.5, point 25, sub-point 5) |
| **8** | Импортчи/юкни қабул қилувчи<br>*Importchi/yukni qabul qiluvchi* | Импортер/грузополучатель | header | declarant | free text + upper-right code after № + bottom: № TIN / district code | cmr, contract, company_profile | «UYJIHOZ SAVDO» MChJ (SYNTHETIC), г. Ташкент, Чиланзарский р-н, ул. Бунёдкор 1, тел. +998 71 000 00 00 \| № 123456789/1726294 | [uz](https://lex.uz/uz/docs/2924955#2926636) · [ru](https://lex.uz/docs/2924953#2927235) (Ch.5, point 25, sub-point 6) |
| **9** | Молиявий тартибга солиш учун жавобгар шахс<br>*Moliyaviy tartibga solish uchun javobgar shaxs* | Лицо, ответственное за финансовое урегулирование | header | declarant | free text + upper code + bottom: № TIN/PINFL / district code | contract, company_profile | «UYJIHOZ SAVDO» MChJ ... \| № 123456789/1726294 | [uz](https://lex.uz/uz/docs/2924955#2926673) · [ru](https://lex.uz/docs/2924953#2927263) (Ch.5, point 25, sub-point 7) |
| **11** | Савдо қилинаётган мамлакат<br>*Savdo qilinayotgan mamlakat* | Торгующая страна | header | declarant | left: 3-digit country code; right: 1 or 2 | contract | 156 \| 2 | [uz](https://lex.uz/uz/docs/2924955#2926682) · [ru](https://lex.uz/docs/2924953#2927268) (Ch.5, point 25, sub-point 8) |
| **12** | Умумий божхона қиймати<br>*Umumiy bojxona qiymati* | Общая таможенная стоимость | header | declarant | decimal(2), currency of grafa 22 | calculated |  | [uz](https://lex.uz/uz/docs/2924955#2926688) · [ru](https://lex.uz/docs/2924953#2927273) (Ch.5, point 25, sub-point 9) |
| **13** | (untitled) USD/UZS rate<br>*(untitled) USD/UZS rate* | (untitled) USD/UZS rate | header | declarant | decimal: UZS per 1 USD | cbu_rate |  | [uz](https://lex.uz/uz/docs/2924955#2926691) · [ru](https://lex.uz/docs/2924953#2927275) (Ch.5, point 25, sub-point 10) |
| **14** | Декларант/божхона брокери<br>*Deklarant/bojxona brokeri* | Декларант/таможенный брокер | header | declarant | free text + upper: № TIN/PINFL | company_profile | «UYJIHOZ SAVDO» MChJ ... \| № 123456789 | [uz](https://lex.uz/uz/docs/2924955#2926694) · [ru](https://lex.uz/docs/2924953#2927277) (Ch.5, point 25, sub-point 11) |
| **15** | Жўнатувчи мамлакат<br>*Joʻnatuvchi mamlakat* | Страна отправления | header | declarant | country short name (Annex 5) | cmr | КИТАЙ | [uz](https://lex.uz/uz/docs/2924955#2926697) · [ru](https://lex.uz/docs/2924953#2927280) (Ch.5, point 25, sub-point 12) |
| **15a** | Жўнатувчи мамлакат коди<br>*Joʻnatuvchi mamlakat kodi* | Код страны отправления | header | declarant | 3-digit numeric (Annex 5) | calculated | 156 | [uz](https://lex.uz/uz/docs/2924955#2926703) · [ru](https://lex.uz/docs/2924953#2927285) (Ch.5, point 25, sub-point 13) |
| **18** | Жўнатиш/етказиб бериш вақтидаги транспорт воситаси<br>*Joʻnatish/yetkazib berish vaqtidagi transport vositasi* | Транспортное средство при отправлении/прибытии | header | declarant | left: "<count> <TRANSPORT>: plate[/trailer]; ..."; right: country code | cmr, transit_declaration | 1 АВТО: 01A123BC/01XY456 \| 860 | [uz](https://lex.uz/uz/docs/2924955#2926705) · [ru](https://lex.uz/docs/2924953#2927287) (Ch.5, point 25, sub-point 14) |
| **19** | Контейнер<br>*Konteyner* | Контейнер | header | declarant | 0 or 1 | cmr, packing_list | 0 | [uz](https://lex.uz/uz/docs/2924955#2926720) · [ru](https://lex.uz/docs/2924953#2927300) (Ch.5, point 25, sub-point 15) |
| **20** | Етказиб бериш шартлари<br>*Yetkazib berish shartlari* | Условия поставки | header | declarant | sub1: 2-digit code; sub2: Incoterms letters + place; sub3: payment-form code "/" dispatch-form code | contract, invoice | 02 \| FCA Foshan \| 10/01 | [uz](https://lex.uz/uz/docs/2924955#2926725) · [ru](https://lex.uz/docs/2924953#2927304) (Ch.5, point 25, sub-point 16) |
| **21** | Чегарадаги транспорт воситаси<br>*Chegaradagi transport vositasi* | Транспортное средство на границе | header | declarant | same as grafa 18 + country code | cmr, transit_declaration | 1 АВТО: 01A123BC/01XY456 \| 860 | [uz](https://lex.uz/uz/docs/2924955#2926737) · [ru](https://lex.uz/docs/2924953#2927312) (Ch.5, point 25, sub-point 17) |
| **22** | Валюта ва товарларнинг умумий фактура қиймати<br>*Valyuta va tovarlarning umumiy faktura qiymati* | Валюта и общая фактурная стоимость товаров | header | declarant | left: 3-digit currency code; right: decimal(2) | contract, invoice | 840 \| 12100.00 | [uz](https://lex.uz/uz/docs/2924955#2926751) · [ru](https://lex.uz/docs/2924953#2927326) (Ch.5, point 25, sub-point 18) |
| **23** | Валюта курси<br>*Valyuta kursi* | Курс валюты | header | declarant | "<nominal>/<rate>" with comma decimals | cbu_rate | 1/12100,00 (EXAMPLE rate) | [uz](https://lex.uz/uz/docs/2924955#2926763) · [ru](https://lex.uz/docs/2924953#2927330) (Ch.5, point 25, sub-point 19) |
| **24** | Битим хусусияти<br>*Bitim xususiyati* | Характер сделки | header | declarant | left: transaction-nature code; right: 3-digit settlement currency | contract | 01 \| 840 | [uz](https://lex.uz/uz/docs/2924955#2926772) · [ru](https://lex.uz/docs/2924953#2927336) (Ch.5, point 25, sub-point 20) |
| **25** | Чегарадаги транспорт тури<br>*Chegaradagi transport turi* | Вид транспорта на границе | header | declarant | 2-digit code | calculated | 30 | [uz](https://lex.uz/uz/docs/2924955#2926777) · [ru](https://lex.uz/docs/2924953#2927340) (Ch.5, point 25, sub-point 21) |
| **26** | Мамлакат ичкарисидаги транспорт тури<br>*Mamlakat ichkarisidagi transport turi* | Вид транспорта внутри страны | header | declarant | 2-digit code | calculated | 30 | [uz](https://lex.uz/uz/docs/2924955#2926783) · [ru](https://lex.uz/docs/2924953#2927343) (Ch.5, point 25, sub-point 22) |
| **28** | Молия ва банк маълумотлари<br>*Moliya va bank maʼlumotlari* | Финансовые и банковские сведения | header | declarant | TIN/PINFL | company_profile | 123456789 | [uz](https://lex.uz/uz/docs/2924955#7472162) · [ru](https://lex.uz/docs/2924953#7472652) (Ch.5, point 25, sub-point 23) |
| **29** | Чегарадаги божхона<br>*Chegaradagi bojxona* | Таможня на границе | header | declarant | 5-digit code + name | transit_declaration, cmr | 03002 Дустлик | [uz](https://lex.uz/uz/docs/2924955#2926798) · [ru](https://lex.uz/docs/2924953#2927352) (Ch.5, point 25, sub-point 24) |
| **30** | Товарлар турган жой<br>*Tovarlar turgan joy* | Местонахождение товаров | header | declarant | text + (e-GTD) district code | transit_declaration, user_input | г. Ташкент, Сергелийский р-н, ... (SYNTHETIC) \| 1726283 | [uz](https://lex.uz/uz/docs/2924955#4629251) · [ru](https://lex.uz/docs/2924953#4631151) (Ch.5, point 25, sub-point 25) |
| **31** | Юк жойлари ва товар тавсифи / Маркировка ва миқдор — контейнерлар рақами — товар тавсифи<br>*Yuk joylari va tovar tavsifi / Markirovka va miqdor — konteynerlar raqami — tovar tavsifi* | Грузовые места и описание товара / Маркировка и количество — номера контейнеров — описание товара | item | declarant | numbered lines 1–11 + bottom-left consumer TIN/district + bottom-right supplementary quantity | invoice, packing_list, cmr, contract, classification | 1) Стол обеденный из массива гевеи, модель DT-1600, 1600x900x750 мм, бренд MINGDE ...<br>2) 80 мест, картонные коробки<br>... \| 123456789/1726294 \| 40,00 | [uz](https://lex.uz/uz/docs/2924955#2926808) · [ru](https://lex.uz/docs/2924953#2927362) (Ch.5, point 25, sub-point 26) |
| **32** | Товар №<br>*Tovar №* | Товар № | item | declarant | integer | calculated | 1 | [uz](https://lex.uz/uz/docs/2924955#2926832) · [ru](https://lex.uz/docs/2924953#2927385) (Ch.5, point 25, sub-point 27) |
| **33** | Товар коди<br>*Tovar kodi* | Код товара | item | declarant | 10 digits, no spaces | classification, invoice | 9403601000 | [uz](https://lex.uz/uz/docs/2924955#2926838) · [ru](https://lex.uz/docs/2924953#2927388) (Ch.5, point 25, sub-point 28) |
| **34** | Келиб чиқиш мамлакати коди<br>*Kelib chiqish mamlakati kodi* | Код страны происхождения | item | declarant | 3-digit numeric (or "EU", "000") | certificate_of_origin, invoice | 156 | [uz](https://lex.uz/uz/docs/2924955#2926843) · [ru](https://lex.uz/docs/2924953#2927390) (Ch.5, point 25, sub-point 29) |
| **35** | Брутто вазн (кг)<br>*Brutto vazn (kg)* | Вес брутто (кг) | item | declarant | decimal(3) kg | packing_list, cmr | 1760.000 | [uz](https://lex.uz/uz/docs/2924955#2926849) · [ru](https://lex.uz/docs/2924953#2927394) (Ch.5, point 25, sub-point 30) |
| **37** | Процедура<br>*Protsedura* | Процедура | item | declarant | 7 digits | calculated | 4000000 | [uz](https://lex.uz/uz/docs/2924955#2926866) · [ru](https://lex.uz/docs/2924953#2927408) (Ch.5, point 25, sub-point 32) |
| **38** | Нетто вазн (кг)<br>*Netto vazn (kg)* | Вес нетто (кг) | item | declarant | decimal(3) kg | packing_list, invoice | 1520.000 | [uz](https://lex.uz/uz/docs/2924955#2926877) · [ru](https://lex.uz/docs/2924953#2927413) (Ch.5, point 25, sub-point 33) |
| **39** | Квота<br>*Kvota* | Квота | item | declarant | quantity + unit | license | (empty for demo goods) | [uz](https://lex.uz/uz/docs/2924955#2926892) · [ru](https://lex.uz/docs/2924953#2927424) (Ch.5, point 25, sub-point 34) |
| **40** | Умумий декларация/аввалги ҳужжат<br>*Umumiy deklaratsiya/avvalgi hujjat* | Общая декларация/предшествующий документ | item | declarant | "<doc code> post/date/number — item — gross kg — net kg — supp qty" | transit_declaration | ТД 03002/10.11.2026/0012345 — 1 — 1760 кг — 1520 кг — 40 шт (SYNTHETIC) | [uz](https://lex.uz/uz/docs/2924955#2926898) · [ru](https://lex.uz/docs/2924953#2927430) (Ch.5, point 25, sub-point 35) |
| **41** | Қўшимча ўлчов бирлиги<br>*Qoʻshimcha oʻlchov birligi* | Дополнительная единица измерения | item | declarant | unit code | classification | 796 (шт) ⚠️ verify code | [uz](https://lex.uz/uz/docs/2924955#2926918) · [ru](https://lex.uz/docs/2924953#2927450) (Ch.5, point 25, sub-point 36) |
| **42** | Товарнинг фактура қиймати<br>*Tovarning faktura qiymati* | Фактурная стоимость товара | item | declarant | decimal(2), contract currency | invoice | 5800.00 | [uz](https://lex.uz/uz/docs/2924955#2926921) · [ru](https://lex.uz/docs/2924953#2927453) (Ch.5, point 25, sub-point 37) |
| **43** | (untitled) own-needs flag<br>*(untitled) own-needs flag* | (untitled) own-needs flag | item | declarant | 0 or 1 | user_input | 0 | [uz](https://lex.uz/uz/docs/2924955#2926926) · [ru](https://lex.uz/docs/2924953#2927458) (Ch.5, point 25, sub-point 38) |
| **44** | Қўшимча маълумотлар/тақдим этилаётган ҳужжатлар<br>*Qoʻshimcha maʼlumotlar/taqdim etilayotgan hujjatlar* | Дополнительная информация/представляемые документы | item | declarant+customs | one document per line: "<code> <short> № ... от DD.MM.YYYY" | contract, invoice, cmr, packing_list, certificate_of_origin, conformity_certificate | 202 СМР № CN-UZ-77812 от 01.11.2026<br>220 ИНВ № MD-2026-118 от 28.10.2026<br>222 УПЛИСТ № MD-PL-118 от 28.10.2026<br>301 КНТ № 15/2026 от 05.09.2026<br>701 СПТИМ № 26C4400A0123 от 30.10.2026 | [uz](https://lex.uz/uz/docs/2924955#2926930) · [ru](https://lex.uz/docs/2924953#2927462) (Ch.5, point 25, sub-point 39) |
| **45** | Божхона қиймати<br>*Bojxona qiymati* | Таможенная стоимость | item | declarant | decimal(2), contract currency (right subfield) | calculated, invoice, freight_invoice | 7761.14 | [uz](https://lex.uz/uz/docs/2924955#2927008) · [ru](https://lex.uz/docs/2924953#2927498) (Ch.5, point 25, sub-point 40) |
| **46** | Статистик қиймат<br>*Statistik qiymat* | Статистическая стоимость | item | declarant | decimal(3), thousand USD | calculated | 7.761 | [uz](https://lex.uz/uz/docs/2924955#2927013) · [ru](https://lex.uz/docs/2924953#2927503) (Ch.5, point 25, sub-point 41) |
| **47** | Божхона тўловларининг ҳисоби<br>*Bojxona toʻlovlarining hisobi* | Исчисление таможенных платежей | item | declarant+customs | table rows: Вид \| Основа начисления \| Ставка \| Сумма \| СП | calculated | 20 \| 93909794.00 \| 15% \| 14086469.10 \| БН | [uz](https://lex.uz/uz/docs/2924955#2927017) · [ru](https://lex.uz/docs/2924953#2927535) (Ch.5, point 25, sub-point 42) |
| **48** | Тўловларни кечиктириш<br>*Toʻlovlarni kechiktirish* | Отсрочка | item | declarant | "XX.DD.MM.YYYY" or "ПН.XX.DD.MM.YYYY.SUM" | customs_decision | (empty for demo) | [uz](https://lex.uz/uz/docs/2924955#7472322) · [ru](https://lex.uz/docs/2924953#7472706) (Ch.5, point 25, sub-point 43) |
| **49** | Омбор номи<br>*Ombor nomi* | Наименование склада | item | declarant | licence number and date | user_input | (empty) | [uz](https://lex.uz/uz/docs/2924955#2927040) · [ru](https://lex.uz/docs/2924953#2927559) (Ch.5, point 25, sub-point 44) |
| **50** | Ишонч билдирган шахс<br>*Ishonch bildirgan shaxs* | Доверитель | header | declarant | fixed sentence + full name, position, phone, PINFL (+ power of attorney) | company_profile, user_input | Ответственность ... несет Каримов Азиз Бахромович, директор, +998 90 000 00 00 \| ПИНФЛ 12345678901234 (SYNTHETIC) | [uz](https://lex.uz/uz/docs/2924955#2927043) · [ru](https://lex.uz/docs/2924953#2927562) (Ch.5, point 25, sub-point 45) |
| **54** | Жой ва сана<br>*Joy va sana* | Место и дата | header | declarant | numbered lines 1–5; GTD own number PINFL/DD.MM.YYYY/serial | company_profile, calculated | 1) г. Ташкент<br>2) Каримов Азиз Бахромович, info@example.uz<br>3) +998 90 000 00 00<br>5) 12345678901234/26.11.2026/000017 | [uz](https://lex.uz/uz/docs/2924955#3903328) · [ru](https://lex.uz/docs/2924953#3909316) (Ch.5, point 25, sub-point 46) |
| **C** | «С» (untitled)<br>*«С» (untitled)* | «С» (untitled) | header | declarant | numbered lines 1–2 | contract, cmr, transit_declaration | 1) 2026-UZ-000123456 (SYNTHETIC ID)<br>2) 10.11.2026 | [uz](https://lex.uz/uz/docs/2924955#2927067) · [ru](https://lex.uz/docs/2924953#2927585) (Ch.5, point 25, sub-point 48) |

## Filling rules per grafa (summary of the official text, IM40)

### Grafa 1 — Тип декларации / Deklaratsiya turi
- **Rule:** Subfield 1: direction 'ИМ'. Subfield 2: two-digit customs regime code per Annex 3 (release for free circulation = 40). Subfield 3 is not filled.
- **Classifier:** Annex 3 – customs regimes (40 = import)
- **Source:** Ch.5, point 25, sub-point 1 — [uz](https://lex.uz/uz/docs/2924955#2926375), [ru](https://lex.uz/docs/2924953#2926607)

### Grafa 2 — Экспортер/грузоотправитель / Eksportchi/yukni joʻnatuvchi
- **Rule:** Person named as consignor in the transport document: for a legal entity – short name + location (country short name per Annex 5 + address); for an individual – full name + residence. If the consignor ships on behalf of another person: consignor first, then 'по поручению' + the person who contracted with the grafa-9 party. In the e-GTD each party goes into its own field. Optional consignor TIN after '№' only for simplified corridor / AEO mutual-recognition cases. Latin-script names stay in Latin (point 11).
- **Checks:** CMR box 1 consignor = invoice seller (or 'on behalf of' chain explained)
- **Notes:** Not filled on additional sheets of a paper GTD.
- **Source:** Ch.5, point 25, sub-point 2 — [uz](https://lex.uz/uz/docs/2924955#2926379), [ru](https://lex.uz/docs/2924953#2926611)

### Grafa 3 — Добавочные листы / Qoʻshimcha varaqlar
- **Rule:** Sheet number / total sheets incl. main and additional. Paper: main sheet holds 1 item, each additional sheet holds 3 items (point 17), max 33 additional sheets. E-GTD: show the numbers as if printed. No additional sheets → '1/1'.
- **Checks:** N = 1 + ceil((items-1)/3)
- **Source:** Ch.5, point 25, sub-point 3 — [uz](https://lex.uz/uz/docs/2924955#2926406), [ru](https://lex.uz/docs/2924953#2926628)

### Grafa 5 — Всего наименований товаров / Tovarlar nomlarining umumiy soni
- **Rule:** Total number of goods items = number of filled grafa 31 entries. Max 100 items per GTD (point 6).
- **Checks:** = count(items); <= 100
- **Source:** Ch.5, point 25, sub-point 4 — [uz](https://lex.uz/uz/docs/2924955#2926632), [ru](https://lex.uz/docs/2924953#2927231)

### Grafa 7 — Регистрационный номер ГТД / BYUDning roʻyxat raqami
- **Rule:** Declarant enters the 5-digit code of the customs post where the GTD is filed (Annex 4). Customs (point 90) completes the registration number: 99999/DD.MM.YYYY/9999999.
- **Classifier:** Annex 4 – customs posts
- **Source:** Ch.5, point 25, sub-point 5 — [uz](https://lex.uz/uz/docs/2924955#2926634), [ru](https://lex.uz/docs/2924953#2927233)

### Grafa 8 — Импортер/грузополучатель / Importchi/yukni qabul qiluvchi
- **Rule:** Importer/consignee: legal entity – short name, legal address, phone, e-mail (if any); individual – full name, permanent address, phone. If consignee ≠ importer: consignee first, then 'по поручению' importer. If grafa 9 already shows the importer, the importer need not be repeated here. Upper-right after '№': 00000001 resident individual, 00000002 non-resident individual, 00000003 organisation with state share, 99999999 diplomatic missions, 88888888 international/governmental organisation offices; otherwise empty. Bottom after '№': consignee TIN (of the branch if a branch acts), '/', district (city) code per Annex 15; no TIN → 999999999.
- **Classifier:** Annex 15 – districts and cities
- **Checks:** CMR box 2 consignee = importer (or chain explained); TIN 9 digits; district code exists in Annex 15
- **Notes:** Not filled on additional sheets of a paper GTD.
- **Source:** Ch.5, point 25, sub-point 6 — [uz](https://lex.uz/uz/docs/2924955#2926636), [ru](https://lex.uz/docs/2924953#2927235)

### Grafa 9 — Лицо, ответственное за финансовое урегулирование / Moliyaviy tartibga solish uchun javobgar shaxs
- **Rule:** Person who concluded the foreign-trade contract and is responsible for settlements: name, legal address, phone, e-mail (legal entity) or full name, residence, phone (individual). Upper '№' codes as in grafa 8 (00000001/00000002/00000003/99999999/88888888 or empty). Bottom: TIN (PINFL for an individual) / district code (Annex 15); none → 999999999. Not filled for gratuitous supplies.
- **Checks:** = buyer in contract; = buyer in invoice (Annex 1a item 2)
- **Source:** Ch.5, point 25, sub-point 7 — [uz](https://lex.uz/uz/docs/2924955#2926673), [ru](https://lex.uz/docs/2924953#2927263)

### Grafa 11 — Торгующая страна / Savdo qilinayotgan mamlakat
- **Rule:** Left: numeric code (Annex 5) of the country where the counterparty that signed the contract with the grafa-9 person is registered/resides. If no contract – per accompanying documents. Right: '1' if that country/territory is on the offshore list approved by MoJ reg. No. 2467 of 12.06.2013, otherwise '2'.
- **Classifier:** Annex 5 – countries; offshore list reg. No. 2467
- **Checks:** seller country in contract = code
- **Notes:** Offshore list must be loaded as a separate reference table (not in this file).
- **Source:** Ch.5, point 25, sub-point 8 — [uz](https://lex.uz/uz/docs/2924955#2926682), [ru](https://lex.uz/docs/2924953#2927268)

### Grafa 12 — Общая таможенная стоимость / Umumiy bojxona qiymati
- **Rule:** Total customs value = sum of grafa 45 of all items, in the grafa-22 currency.
- **Checks:** = Σ grafa 45 (exact)
- **Source:** Ch.5, point 25, sub-point 9 — [uz](https://lex.uz/uz/docs/2924955#2926688), [ru](https://lex.uz/docs/2924953#2927273)

### Grafa 13 — (untitled) USD/UZS rate / (untitled) USD/UZS rate
- **Rule:** US dollar rate to UZS set by the Central Bank on the date the GTD is accepted for clearance.
- **Notes:** Rate date = acceptance date, which the product cannot know in advance → recompute at filing (Customs Code Art. 326).
- **Source:** Ch.5, point 25, sub-point 10 — [uz](https://lex.uz/uz/docs/2924955#2926691), [ru](https://lex.uz/docs/2924953#2927275)

### Grafa 14 — Декларант/таможенный брокер / Deklarant/bojxona brokeri
- **Rule:** Customs broker or declarant (legal entity) that filled in and files the GTD: short name, legal address, phone, e-mail; individual declarant: full name, address, phone, e-mail. Upper '№': TIN (PINFL for an individual). For YuklaGo self-filing this is the importer itself.
- **Source:** Ch.5, point 25, sub-point 11 — [uz](https://lex.uz/uz/docs/2924955#2926694), [ru](https://lex.uz/docs/2924953#2927277)

### Grafa 15 — Страна отправления / Joʻnatuvchi mamlakat
- **Rule:** Country of dispatch: country from which goods were sent to Uzbekistan without commercial deals or other operations in intermediate countries changing their legal status; determined from the transport document that started the international carriage. Several transport documents → first country where the goods were taken over for carriage to the grafa-8 consignee.
- **Checks:** CMR box 4 (place of taking over) country
- **Source:** Ch.5, point 25, sub-point 12 — [uz](https://lex.uz/uz/docs/2924955#2926697), [ru](https://lex.uz/docs/2924953#2927280)

### Grafa 15a — Код страны отправления / Joʻnatuvchi mamlakat kodi
- **Rule:** Numeric code of the dispatch country.
- **Classifier:** Annex 5
- **Source:** Ch.5, point 25, sub-point 13 — [uz](https://lex.uz/uz/docs/2924955#2926703), [ru](https://lex.uz/docs/2924953#2927285)

### Grafa 18 — Транспортное средство при отправлении/прибытии / Joʻnatish/yetkazib berish vaqtidagi transport vositasi
- **Rule:** Vehicle that carried the goods inside Uzbekistan to the clearing post. Left: number of vehicles, space, short transport name per Annex 6 (e.g. АВТО), colon, vehicle identifiers separated by ';' with trailers after '/'. Right: numeric code of the country of registration of the tractor unit; several countries → '999' (e-GTD lists all in fields, no 'see reverse').
- **Classifier:** Annex 6 – transport types
- **Checks:** plates = CMR box 25 / transit declaration
- **Source:** Ch.5, point 25, sub-point 14 — [uz](https://lex.uz/uz/docs/2924955#2926705), [ru](https://lex.uz/docs/2924953#2927287)

### Grafa 19 — Контейнер / Konteyner
- **Rule:** '0' – not in a container; '1' – in a container or the container itself is declared as goods.
- **Source:** Ch.5, point 25, sub-point 15 — [uz](https://lex.uz/uz/docs/2924955#2926720), [ru](https://lex.uz/docs/2924953#2927300)

### Grafa 20 — Условия поставки / Yetkazib berish shartlari
- **Rule:** Delivery terms from the contract. Sub1 numeric code and sub2 letter code + geographic point per Annex 7. Sub3: payment form 10 prepayment, 20 letter of credit, 30 bank guarantee, 40 collection, 50 upon import, 60 consignment, 70 barter, 80 gratuitous (mixed → the one with the largest share); then '/' dispatch form 01 shipped directly by the contracting party, 02 not directly. E-GTD: each code in its own field.
- **Classifier:** Annex 7 – delivery terms (01 EXW, 02 FCA, 03 FAS, 04 FOB, 05 CFR, 06 CIF, 07 CPT, 08 CIP, 09 DAF, 10 DES, 11 DEQ, 12 DDU, 13 DDP, 14 DAP, 15 DAT, 99 other)
- **Checks:** invoice Incoterms = contract Incoterms; payment terms in contract → code
- **Notes:** ⚠️ Annex 7 has no DPU (Incoterms 2020) – likely '99' + letters; VMQ 605 Annex 1a still says 'Incoterms-2010'. Open question.
- **Source:** Ch.5, point 25, sub-point 16 — [uz](https://lex.uz/uz/docs/2924955#2926725), [ru](https://lex.uz/docs/2924953#2927304)

### Grafa 21 — Транспортное средство на границе / Chegaradagi transport vositasi
- **Rule:** Vehicle(s) on which the goods actually crossed the Uzbek customs border; same format as grafa 18; right: country code of the tractor unit's registration; several countries → '999'. Not filled if the goods have not crossed the border before (change of regime).
- **Checks:** = CMR vehicle; = border-post stamp
- **Source:** Ch.5, point 25, sub-point 17 — [uz](https://lex.uz/uz/docs/2924955#2926737), [ru](https://lex.uz/docs/2924953#2927312)

### Grafa 22 — Валюта и общая фактурная стоимость товаров / Valyuta va tovarlarning umumiy faktura qiymati
- **Rule:** Left: numeric code (Annex 8) of the contract currency (currency in which goods are priced). Right: total invoice value of the consignment = Σ grafa 42.
- **Classifier:** Annex 8 – currencies (840 USD, 156 CNY, 949 TRY, 860 UZS)
- **Checks:** = Σ grafa 42 (exact); = invoice total; currency = contract currency
- **Source:** Ch.5, point 25, sub-point 18 — [uz](https://lex.uz/uz/docs/2924955#2926751), [ru](https://lex.uz/docs/2924953#2927326)

### Grafa 23 — Курс валюты / Valyuta kursi
- **Rule:** CBU rate of the grafa-22 currency to UZS on the date of GTD acceptance, written as nominal/rate, e.g. '1/63,41', '10/220,09'; UZS contract → '1/1'.
- **Source:** Ch.5, point 25, sub-point 19 — [uz](https://lex.uz/uz/docs/2924955#2926763), [ru](https://lex.uz/docs/2924953#2927330)

### Grafa 24 — Характер сделки / Bitim xususiyati
- **Rule:** Left: transaction nature code per Annex 9 (01 = ordinary trade with settlement in national or foreign currency). Right: numeric code of the currency in which the grafa-9 party settles with the counterparty.
- **Classifier:** Annex 9 – nature of transaction
- **Source:** Ch.5, point 25, sub-point 20 — [uz](https://lex.uz/uz/docs/2924955#2926772), [ru](https://lex.uz/docs/2924953#2927336)

### Grafa 25 — Вид транспорта на границе / Chegaradagi transport turi
- **Rule:** Transport type code (Annex 6) of the grafa-21 vehicle. Not filled if goods did not cross the border before.
- **Classifier:** Annex 6 (10 sea, 20 rail, 30 road, 40 air, 71 pipeline, 72 power line, 80 river, 90 self-propelled)
- **Source:** Ch.5, point 25, sub-point 21 — [uz](https://lex.uz/uz/docs/2924955#2926777), [ru](https://lex.uz/docs/2924953#2927340)

### Grafa 26 — Вид транспорта внутри страны / Mamlakat ichkarisidagi transport turi
- **Rule:** Transport type code (Annex 6) of the grafa-18 vehicle.
- **Classifier:** Annex 6
- **Source:** Ch.5, point 25, sub-point 22 — [uz](https://lex.uz/uz/docs/2924955#2926783), [ru](https://lex.uz/docs/2924953#2927343)

### Grafa 28 — Финансовые и банковские сведения / Moliya va bank maʼlumotlari
- **Rule:** TIN (PINFL for an individual) of the payer of customs payments; if a non-resident pays – TIN/PINFL of the broker or declarant.
- **Source:** Ch.5, point 25, sub-point 23 — [uz](https://lex.uz/uz/docs/2924955#7472162), [ru](https://lex.uz/docs/2924953#7472652)

### Grafa 29 — Таможня на границе / Chegaradagi bojxona
- **Rule:** Code and name (Annex 4) of the customs post through which the goods entered Uzbekistan. Not filled if goods did not cross the border before.
- **Classifier:** Annex 4
- **Checks:** = border post stamp on CMR / transit declaration
- **Source:** Ch.5, point 25, sub-point 24 — [uz](https://lex.uz/uz/docs/2924955#2926798), [ru](https://lex.uz/docs/2924953#2927352)

### Grafa 30 — Местонахождение товаров / Tovarlar turgan joy
- **Rule:** Location of goods at filing: customs or free warehouse / duty-free shop → number and date of its licence; place without customs-warehouse status → postal address (no postcode); railway station → its name. E-GTD: separate field with district (city) code per Annex 15.
- **Classifier:** Annex 15
- **Source:** Ch.5, point 25, sub-point 25 — [uz](https://lex.uz/uz/docs/2924955#4629251), [ru](https://lex.uz/docs/2924953#4631151)

### Grafa 31 — Грузовые места и описание товара / Маркировка и количество — номера контейнеров — описание товара / Yuk joylari va tovar tavsifi / Markirovka va miqdor — konteynerlar raqami — tovar tavsifi
- **Rule:** Description sufficient for unambiguous 10-digit classification. Line 1: trade name, trademark/brand, model, article, grade, standards, technical and commercial characteristics, quantitative and qualitative composition; energy-efficiency class for appliances listed in the annex to CM Resolution No. 86 of 09.04.2015; e-GTD: brand in separate field ('без марки'/'без бренда' if none); parameters in other units and production date when needed for payments or measures. Using only the TN VED heading text is NOT allowed. Line 2: number of packages, packaging type and number of packings ('часть коробки' if partial; bulk codes 01 насыпью/02 навалом/03 наливом). Line 3: container numbers ('часть' if partial). Line 4: excise stamps. Line 5: pipeline/power-line supply period. Line 6: aggregated import code (separate table). Line 7: shelf life for food and medicines. Line 8: investment-project codes (101/102/103/201/202/203 and further codes in the text). Line 9: 3-digit technological-equipment sphere code (Annex 16) for listed HS headings, '000' if sphere not listed. Line 10: year of manufacture / technical parameters of such equipment. Line 11: '01' state procurement / '02' not state procurement. Bottom-left: TIN/PINFL of the end consumer + '/' district code (unknown or several → consignee). Bottom-right: quantity in supplementary unit, 2 decimals (6 if < 0.01); e-GTD: number only; not filled if only 'kg'.
- **Classifier:** Annex 15, Annex 16
- **Checks:** packages (line 2) = CMR box 6-7 = packing list = invoice; supp. quantity = invoice qty = packing list qty; description not equal to bare heading text; brand present or 'без бренда'
- **Notes:** One item = same name, type, brand, one 10-digit code, one origin, same tariff treatment (point 7). Consumer goods with the same code but different names/brands/models/specs must be separate items (point 8). For smartphones: IMEI required in grafa 31 per tariff team note (VM 778) – out of demo scope.
- **Source:** Ch.5, point 25, sub-point 26 — [uz](https://lex.uz/uz/docs/2924955#2926808), [ru](https://lex.uz/docs/2924953#2927362)

### Grafa 32 — Товар № / Tovar №
- **Rule:** Sequential number of the item declared in grafa 31; single item → '1'.
- **Source:** Ch.5, point 25, sub-point 27 — [uz](https://lex.uz/uz/docs/2924955#2926832), [ru](https://lex.uz/docs/2924953#2927385)

### Grafa 33 — Код товара / Tovar kodi
- **Rule:** 10-digit TN VED (TIF TN) code of the grafa-31 goods, written without spaces or separators (left part).
- **Checks:** code exists and active in PQ-181 Annex 1 list; first 6 digits vs invoice HS (Annex 1a item 3) – warn on mismatch
- **Notes:** Right part of grafa 33 is not described in point 25 for IM40 – leave empty unless the cabinet requires it ⚠️.
- **Source:** Ch.5, point 25, sub-point 28 — [uz](https://lex.uz/uz/docs/2924955#2926838), [ru](https://lex.uz/docs/2924953#2927388)

### Grafa 34 — Код страны происхождения / Kelib chiqish mamlakati kodi
- **Rule:** Left: numeric origin-country code (Annex 5). Unknown at clearance → '000'. Certificate naming only the European Union → 'EU' (Latin).
- **Classifier:** Annex 5
- **Checks:** = certificate of origin country; = invoice origin (Annex 1a item 4)
- **Notes:** Origin drives the Art. 300¹ surcharge for non-MFN/unknown origin (see data/tariff).
- **Source:** Ch.5, point 25, sub-point 29 — [uz](https://lex.uz/uz/docs/2924955#2926843), [ru](https://lex.uz/docs/2924953#2927390)

### Grafa 35 — Вес брутто (кг) / Brutto vazn (kg)
- **Rule:** Gross mass in kg of the grafa-31 goods: total mass incl. all packaging needed to keep goods intact until they enter circulation, EXCLUDING containers and other transport equipment. Round mathematically to 3 decimals (<1 g → 6 decimals).
- **Checks:** Σ grafa 35 vs CMR gross (box 11); Σ grafa 35 = packing list gross; gross ≥ net
- **Notes:** Whether pallets count as packaging or transport equipment is not stated ⚠️.
- **Source:** Ch.5, point 25, sub-point 30 — [uz](https://lex.uz/uz/docs/2924955#2926849), [ru](https://lex.uz/docs/2924953#2927394)

### Grafa 37 — Процедура / Protsedura
- **Rule:** Procedure code = declared regime (2) + previous regime (2; '00' if none or only customs transit) + movement-feature code (3) per Annex 11 ('000' = feature not established).
- **Classifier:** Annex 3, Annex 11
- **Source:** Ch.5, point 25, sub-point 32 — [uz](https://lex.uz/uz/docs/2924955#2926866), [ru](https://lex.uz/docs/2924953#2927408)

### Grafa 38 — Вес нетто (кг) / Netto vazn (kg)
- **Rule:** Net mass in kg: without any packaging, except primary packaging in which goods are sold at retail and/or which cannot be separated before use without loss of consumer properties (e.g. coffee in a can). Bulk goods → total mass. Round to 3 decimals.
- **Checks:** net ≤ gross; = packing list net; = invoice net (Annex 1a item 8)
- **Source:** Ch.5, point 25, sub-point 33 — [uz](https://lex.uz/uz/docs/2924955#2926877), [ru](https://lex.uz/docs/2924953#2927413)

### Grafa 39 — Квота / Kvota
- **Rule:** Only for goods under quantitative restrictions: remaining quota per licence, not counting the goods now declared.
- **Source:** Ch.5, point 25, sub-point 34 — [uz](https://lex.uz/uz/docs/2924955#2926892), [ru](https://lex.uz/docs/2924953#2927424)

### Grafa 40 — Общая декларация/предшествующий документ / Umumiy deklaratsiya/avvalgi hujjat
- **Rule:** Previous document. Previous GTD: 'ГТД post/date/number — item — gross — net — supp qty'. Customs transit: 'ТД 06010/01.03.2022/0003761 — 3 — 7980 кг — 7900 кг — 350,2 м3'. No GTD/TD but delivery-control document: 'ККДГ post/date/ИМnumber — gross' (Cyrillic letters) or 'МДП post/date/XYnumber — gross' (Latin letters). Several previous documents → one per line. Vehicle imported under return obligation → 'МB …'.
- **Checks:** TD weights vs GTD weights
- **Notes:** For a truck cleared at an inland post the transit declaration is normally the previous document (Customs Code Art. 261 part 3).
- **Source:** Ch.5, point 25, sub-point 35 — [uz](https://lex.uz/uz/docs/2924955#2926898), [ru](https://lex.uz/docs/2924953#2927430)

### Grafa 41 — Дополнительная единица измерения / Qoʻshimcha oʻlchov birligi
- **Rule:** Code of the supplementary unit (TN VED 'table of units') for the quantity in grafa 31 bottom-right; empty if only kg applies.
- **Notes:** Supplementary unit per code is in data/tariff/tiftn_codes_pq181_annex1.csv; the numeric unit code table is not in this file ⚠️.
- **Source:** Ch.5, point 25, sub-point 36 — [uz](https://lex.uz/uz/docs/2924955#2926918), [ru](https://lex.uz/docs/2924953#2927450)

### Grafa 42 — Фактурная стоимость товара / Tovarning faktura qiymati
- **Rule:** Invoice value of the item actually paid or payable (or compensated by counter-deliveries) per the contract, in contract currency; gratuitous/no contract → per accompanying documents. Round to 2 decimals.
- **Checks:** = Σ invoice lines for this item; Σ = grafa 22
- **Source:** Ch.5, point 25, sub-point 37 — [uz](https://lex.uz/uz/docs/2924955#2926921), [ru](https://lex.uz/docs/2924953#2927453)

### Grafa 43 — (untitled) own-needs flag / (untitled) own-needs flag
- **Rule:** '0' – consignee imports goods NOT for its own needs; '1' – for its own needs.
- **Source:** Ch.5, point 25, sub-point 38 — [uz](https://lex.uz/uz/docs/2924955#2926926), [ru](https://lex.uz/docs/2924953#2927458)

### Grafa 44 — Дополнительная информация/представляемые документы / Qoʻshimcha maʼlumotlar/taqdim etilayotgan hujjatlar
- **Rule:** Documents supporting each item, each with ordinal code and letter code per Annex 12: licence (101 ЛИЦЕНЗИЯ … срок), transport & commercial docs (202 СМР, 220 ИНВ, 221 ИНВПРФ, 222 УПЛИСТ, 223 ИНВ_ОТ …), contract (301 КНТ), supplementary agreement (302 ДОП), contract specification (307 SPES_N), transport contract with non-resident carrier (305 КНТ_ТР) and its e-system ID (306 IDN_ТР), permits & certificates (e.g. 417 ССТ conformity certificate, 441 MTD declaration of conformity), contract registration (501…), benefits ('6' + payment code + Annex 14 act code, e.g. '629 15-142120030000'), certificate of origin (701 СПТИМ), other docs (deferral, commission contract, fine decision, foreign export declaration …). Customs adds its own entries (inspection act etc., point 90).
- **Classifier:** Annex 12 – document types; Annex 14 – benefit acts
- **Checks:** every doc referenced exists in the pack; dates: contract ≤ invoice ≤ CMR; certificate valid on filing date
- **Code 904 МЕТОД** (Метод определения таможенной стоимости / Bojxona qiymatini aniqlash usuli; Annex 12 item 113): States which customs valuation method was used for the item's customs value (grafa 45). Customs Code Art. 302 lists the methods for imported goods: transaction value (Art. 303), identical goods (Art. 309), similar goods (Art. 310), deduction (Art. 311), addition/computed (Art. 312), fall-back (Art. 313). Proposed line: `904 МЕТОД <method number> — e.g. '904 МЕТОД 1' for transaction value (Art. 303)`. ⚠️ OUR READING of Instruction 2773 ch.5 p.25 sub-point 39 'з) иные документы и сведения' + Annex 12 item 113 (code 904 МЕТОД). UNVERIFIED on live ed2: the Instruction does not say WHEN 904 is mandatory or HOW the method is written (number vs text); the format above is a proposal. — Annex 12 [ru](https://lex.uz/docs/2924953#8355909) · [uz](https://lex.uz/uz/docs/2924955#8355460); grafa 44 'з) other documents' [ru](https://lex.uz/docs/2924953#7472695) · [uz](https://lex.uz/uz/docs/2924955#7472313); grafa 45 methods [ru](https://lex.uz/docs/2924953#2927501) · [uz](https://lex.uz/uz/docs/2924955#2927011); Customs Code https://lex.uz/docs/2876354 (Arts. 302, 303, 309–313). Demo answer keys do not include a 904 line; add '904 МЕТОД 1' if ed2 confirms it is required for transaction-value declarations.
- **Source:** Ch.5, point 25, sub-point 39 — [uz](https://lex.uz/uz/docs/2924955#2926930), [ru](https://lex.uz/docs/2924953#2927462)

### Grafa 45 — Таможенная стоимость / Bojxona qiymati
- **Rule:** Right subfield: customs value of the item in contract currency (gratuitous/no contract → currency of accompanying documents), determined by the Customs Code valuation methods (Arts. 302–313). Round to 2 decimals.
- **Checks:** ≥ invoice value when Incoterms leave freight to the border unpaid (Art. 304); Σ = grafa 12
- **Notes:** Left subfield content is not described for IM40 in point 25 ⚠️ (cabinet may require valuation-method code).
- **Source:** Ch.5, point 25, sub-point 40 — [uz](https://lex.uz/uz/docs/2924955#2927008), [ru](https://lex.uz/docs/2924953#2927498)

### Grafa 46 — Статистическая стоимость / Statistik qiymat
- **Rule:** Statistical value in thousand USD: grafa-42 invoice value brought to 'CIP (CIF) – border of Uzbekistan' terms, converted at CBU rate on acceptance date; 3 decimals.
- **Source:** Ch.5, point 25, sub-point 41 — [uz](https://lex.uz/uz/docs/2924955#2927013), [ru](https://lex.uz/docs/2924953#2927503)

### Grafa 47 — Исчисление таможенных платежей / Bojxona toʻlovlarining hisobi
- **Rule:** Per item and per payment type. 'Вид' = payment code (Annex 13: 10 clearance fee, 20 import duty, 21 additional duty, 27 import excise, 29 VAT …). 'Основа' in UZS (conversion of grafa 12/45 at CBU rate on acceptance date) unless law sets a foreign-currency or non-money base (then quantity + unit). 'Ставка' = applied rate. 'Сумма' in UZS. 'СП' method: БН bank transfer, КТ cash, УН conditional accrual, ОП deferral, РП instalments, ПП per-batch under periodic GTD, ВЗ VAT offset, ОО not payable. Clearance fees always shown only once (e-GTD: under item No. 1). No row when rate not set / zero or no obligation under the regime.
- **Classifier:** Annex 13 – customs payments
- **Notes:** Customs adds fees for clearance outside working hours/places (point 90). Rounding of UZS amounts is not stated in the instruction ⚠️.
- **Source:** Ch.5, point 25, sub-point 42 — [uz](https://lex.uz/uz/docs/2924955#2927017), [ru](https://lex.uz/docs/2924953#2927535)

### Grafa 48 — Отсрочка / Toʻlovlarni kechiktirish
- **Rule:** Only when deferral/instalments granted: per payment type the deadline 'XX.DD.MM.YYYY' (XX = payment code); instalments 'ПН.XX.DD.MM.YYYY.SUM' one per line.
- **Source:** Ch.5, point 25, sub-point 43 — [uz](https://lex.uz/uz/docs/2924955#7472322), [ru](https://lex.uz/docs/2924953#7472706)

### Grafa 49 — Наименование склада / Ombor nomi
- **Rule:** Number and date of the customs/free warehouse licence if the goods were previously placed under a regime involving storage there; otherwise not filled.
- **Source:** Ch.5, point 25, sub-point 44 — [uz](https://lex.uz/uz/docs/2924955#2927040), [ru](https://lex.uz/docs/2924953#2927559)

### Grafa 50 — Доверитель / Ishonch bildirgan shaxs
- **Rule:** Text: 'Ответственность за представленные документы и сведения несет …' + full name, position, phone, PINFL (separate e-GTD field) of the person responsible – the declarant or its authorised person. Non-resident without PINFL → 14 nines. If an authorised person: number, date and validity of the contract/power of attorney.
- **Source:** Ch.5, point 25, sub-point 45 — [uz](https://lex.uz/uz/docs/2924955#2927043), [ru](https://lex.uz/docs/2924953#2927562)

### Grafa 54 — Место и дата / Joy va sana
- **Rule:** Declaring person filing on behalf of the grafa-14 person: 1 place of filling; 2 full name + e-mail; 3 phone; 4 (broker only) number/date of broker–client contract; 5 declarant's own GTD number '99999999999999/99.99.9999/999999' = PINFL / filling date / serial number increasing within the year (restarts each year, never repeated). E-GTD authenticity is certified by the declaring person's ЭЦП (ERI).
- **Checks:** serial unique within year
- **Notes:** 'Declaring person' = declarant filing itself or a customs-clearance specialist employed by the declarant/broker (point 1).
- **Source:** Ch.5, point 25, sub-point 46 — [uz](https://lex.uz/uz/docs/2924955#3903328), [ru](https://lex.uz/docs/2924953#3909316)

### Grafa C — «С» (untitled) / «С» (untitled)
- **Rule:** 1: identification number of the foreign-trade contract in the Unified Electronic Information System of Foreign Trade Operations; 2: date of import into Uzbekistan = date of the stamp of the border post on the accompanying documents, or date of registration of the delivery-control book / TIR carnet at the border post.
- **Checks:** contract registered in the e-system (ID present); date of import ≤ filing date
- **Source:** Ch.5, point 25, sub-point 48 — [uz](https://lex.uz/uz/docs/2924955#2927067), [ru](https://lex.uz/docs/2924953#2927585)

## Not filled by the declarant for IM40

Every grafa not in the point-24 list (e.g. 4, 6, 10, 16, 17, 27, 36, 51–53) is not filled by the declaring person for IM40.

## Filled by customs only

- **7 (number part)**: 99999/DD.MM.YYYY/9999999 – post code / acceptance date / serial number of the post's GTDs in the year
- **A**: paper additional sheets only: registration number from grafa 7
- **B**: e-GTD only: per payment code, total amount over all items; exemptions shown with 'без оплаты'
- **D**: customs decision marks; filling grafa D completes clearance (point 13)

## Classifiers (annexes to Instruction 2773)

- Annex 3: Customs regimes
- Annex 4: Customs posts (edition 2773-14 of 04.02.2026)
- Annex 5: Countries of the world
- Annex 6: Transport types
- Annex 7: Delivery terms
- Annex 8: Currencies
- Annex 9: Nature of transaction
- Annex 11: Movement features
- Annex 12: Document types for grafa 44
- Annex 13: Customs payments
- Annex 14: Benefit legal acts for grafa 44
- Annex 15: Districts and cities of Uzbekistan
- Annex 16: Main spheres (technological equipment)

Codes used in the demo sets were read from the annexes on 2026-11-18: regimes 40 (import), 80 (transit); transport 30 АВТО; Incoterms 02 FCA, 07 CPT, 14 DAP; currencies 840 USD, 156 CNY, 949 TRY; countries 156 CN, 792 TR, 860 UZ; payments 10 fee, 20 import duty, 21 additional duty, 27 excise, 29 VAT; documents 202 СМР, 220 ИНВ, 222 УПЛИСТ, 301 КНТ, 417 ССТ, 701 СПТИМ; posts 03002 Дустлик, 06010 Алат, 27001 Яллама, 26010 Сергели, 26002 Ташкент-товарный, 27020 Келес; districts 1726294 Chilonzor, 1726283 Sergeli, 1726266 Yunusobod, 1727265 Tashkent district.

## Uncertainties

- Grafa 33 right part and grafa 45 left subfield are not described for IM40 in point 25 — check the live cabinet form.
- Grafa 44 code 904 МЕТОД (valuation method): when it is mandatory and the exact line format are not stated in the Instruction — UNVERIFIED on live ed2.
- Grafa 41 numeric unit codes (e.g. 796 = шт) must be verified against the TN VED unit table.
- Grafa 20: no Annex-7 code for Incoterms 2020 DPU.
- Grafa 35: pallets — packaging or transport equipment? Not stated.
- Grafa 47: UZS rounding rule not stated in the Instruction.
- The e-GTD XML/field structure (point 3: 'established format and structure') is not published in this Instruction.
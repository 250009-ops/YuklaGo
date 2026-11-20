# YuklaGo rules engine — bojxona to'lovlari qoidalari (P0)

Tayyorlangan: 18.11.2026 (Toshkent, UTC+5). Har bir qoida lex.uz dagi joriy tahrirdan 18.11.2026 da o'qildi.
Belgilar: **[VERIFIED]** — matn o'qildi; **[ASSUMPTION]** — rasmiy matnda yo'q, engine shunday qiladi va UIda aytadi; **[UNVERIFIED]** — tekshirilmadi.

Asosiy hujjatlar:
- Bojxona kodeksi (O'RQ-400, 20.01.2016, joriy tahrir): https://lex.uz/docs/-2876354
- Soliq kodeksi (30.12.2019, joriy tahrir): https://lex.uz/docs/-4674902
- Import boj stavkalari: PQ-3818 (29.06.2018) 1-ilova, PQ-181 (14.05.2025) 2-ilova tahririda (ilova 01.06.2025 dan kuchda), PQ-58 (11.02.2026, 16.02.2026 dan) bilan o'zgartirilgan. Rasmiy o'zbekcha: https://lex.uz/uz/docs/-7533457 ; konsolidatsiyalangan (norasmiy ruscha tarjima): https://lex.uz/docs/3802366
- TIF TN 10 xonali kodlar ro'yxati: PQ-181 1-ilova (PDF, 874 bet): https://lex.uz/uz/files/7541055.zip → parse qilingan: `tiftn_codes_pq181_annex1.csv` (13 138 ta noyob kod; PDF matnidan avtomatik ajratilgan — ehtimoliy kamchiliklar bor, qarang pastda)
- Yig'imlar: VM 55 (31.01.2025): https://lex.uz/docs/-7357270 ; PF-250 (17.12.2025): https://lex.uz/uz/docs/-7934915
- BHM: PF-115 (23.06.2026): https://www.lex.uz/uz/docs/-8283656
- MFN / erkin savdo davlatlari ro'yxati: MYU qarori, ro'yxat raqami 3267 (30.06.2020): https://lex.uz/uz/docs/-4911943
- Valyuta kursi: MB JSON API `https://cbu.uz/uz/arkhiv-kursov-valyut/json/{CCY}/{YYYY-MM-DD}/`

---

## 1. Bojxona qiymati (1-usul, bitim qiymati) [VERIFIED]

- 302-modda: 6 usul ketma-ket — (1) bitim qiymati (asosiy), (2) aynan bir xil tovar, (3) o'xshash tovar, (4) chegirib tashlash, (5) qo'shish, (6) zaxira. Har biri oldingisi qo'llanib bo'lmasagina; 4 va 5 teskari tartibda ham bo'lishi mumkin.
- 303-modda: bitim qiymati = to'langan/to'lanadigan narx, 304 va 305-moddalar bo'yicha tuzatilgan; bir bitimdan qism deklaratsiya qilinsa — miqdorga mutanosib.
- **304-modda — narxga qo'shiladi (agar narxda bo'lmasa):**
  - a) tovarni **bojxona hududiga olib kiriladigan joygacha** bo'lgan: tashish qiymati; yuklash, tushirish, qayta yuklash xarajatlari; sug'urta qiymati;
  - b) xaridor xarajatlari: vositachilik/brokerlik haqi (xarid vositachiligidan tashqari), ko'p martalik idish, o'rov-joylov;
  - v) xaridor bepul/arzon bergan xomashyo, asbob-qolip, materiallar, dizayn/muhandislik ishlari (taqsimlangan qiymati);
  - (moddaning qolgan bandlari — litsenziya to'lovlari va h.k. — engine kiritish maydonlari sifatida qo'shilsin; to'liq ro'yxatni 304-moddadan o'qing).
- **305-modda — narxdan chiqariladi (alohida ko'rsatilgan bo'lsa):** olib kirilgandan keyingi montaj/sozlash; **olib kirilgandan keyingi transport**; O'zbekistonda to'lanadigan bojxona to'lovlari (sotuvchi to'lasa). Hujjat bilan tasdiqlanadi.
- 306-modda: 1-usul qo'llanmaydigan hollar (cheklovlar, shartlar, keyingi daromad, o'zaro bog'liqlik ta'siri). 307–308: o'zaro bog'liq shaxslar belgilari va oqibati → engine savol beradi, "ha" bo'lsa — broker/odam ko'rib chiqishi.
- Tartib detallari: VM 160 (06.04.2022) Nizomi — https://lex.uz/acts/-5941961 [UNVERIFIED: bu sessiyada o'qilmadi].

**Engine qoidasi:** Incoterms bo'yicha qaysi xarajat narxda borligini aniqlang (FOB → freight+insurance qo'shiladi; CIF chegaragacha → qo'shilmaydi). Ekspeditor "Shenzhen → Toshkent" bitta summa bersa — chegaradan keyingi qism ajratilmaguncha butun summa qo'shiladi (305-modda ajratilgan bo'lishini talab qiladi) va UI "chegaradan keyingi qismni ajrating — qiymat kamayishi mumkin" deydi.

```
cv_foreign_parts = invoice_price (+ adjustments 304 b,v) - deductions_305
cv_uzs = Σ convert(part.amount, part.ccy, decl_date) + convert(freight_to_border) + convert(loading_to_border) + convert(insurance_to_border)
```

## 2. Valyuta kursi sanasi [VERIFIED]

- **326-modda:** bojxona to'lovlarini hisoblash uchun chet el valyutasi **bojxona deklaratsiyasi qabul qilingan kuni** MB rasmiy kursi bo'yicha qayta hisoblanadi (rasmiylashtiruvga bog'liq bo'lmagan to'lovlar — harakat bajarilgan kun).
- **323-modda:** hisob milliy valyutada (so'm) olib boriladi.
- **324-modda:** stavkalar ham deklaratsiya qabul qilingan kuni amalda bo'lganlari olinadi.
- Engine: `rate = cbu_rate(ccy, decl_acceptance_date)`. Narx so'rovidan oldingi (pre-purchase) hisobda — bugungi kurs, chip "≈ Taxmin, kurs DD.MM.YYYY"; to'lov ekranida — deklaratsiya sanasi bo'yicha qayta hisob.
- MB API kuzatuvi [ASSUMPTION]: `/json/USD/2026-11-16/` so'rovi `Date: 14.11.2026` qaytardi — ya'ni javobdagi `Date` kursning amal qilish boshlanish sanasi; engine so'ralgan sana uchun javobdagi `Date` ni saqlasin va UIda ko'rsatsin. MB kursi qachondan amal qilishi (e'lon kunining ertasidanmi) — MB qoidalarida tekshirilsin [UNVERIFIED].
- Xos (specific) stavkalar USD da → shu kundagi USD kursi bilan so'mga.
- Nominal: API `Nominal` maydoni bor (masalan, ba'zi valyutalar 10/100 birlik uchun) → `rate_per_unit = Rate / Nominal`.

## 3. Import boji [VERIFIED]

- **293-modda:** advalor (% × bojxona qiymati), xos (stavka × miqdor), aralash:
  - "% , lekin birlik uchun X dan kam bo'lmagan" → **katta qiymat** (max);
  - "% va birlik uchun X" → **yig'indi**.
- Tarif qatorini topish: 10 xonali kod uchun eng aniq qator (10 → 6 → 4 xona) — PQ-181 2-ilova jadvali "4 xonali pozitsiya, quyidagilar bundan mustasno: ..." tuzilishida; istisno ro'yxatidagi kodlar alohida stavka oladi.

```
duty_adv  = cv_uzs * adv_pct/100
duty_spec = qty_in_unit(unit) * spec_usd * usd_rate(decl_date)      # unit: dona/juft/kg
duty_base = max(duty_adv, duty_spec)   # "kam bo'lmagan" turi
```
- `kg` uchun netto yoki brutto — PQ-3818 matnida aytilmagan [UNVERIFIED → ASSUMPTION: netto, UIda ko'rsatiladi].

## 4. MFN / MFN bo'lmagan ustama — 300¹-modda [VERIFIED, 28.02.2026 dan]

- Boj tarifi stavkasi MFN davlatlarda ishlab chiqarilgan tovarga qo'llanadi (jo'natuvchi davlatdan qat'i nazar).
- MFN bo'lmagan yoki kelib chiqishi aniqlanmagan tovarga **qo'shimcha boj**: advalor stavka 10% gacha → +5%; 10–20% → +10%; 20–30% → +15%; 30% va undan yuqori → +20%.
- 366-modda: kelib chiqish sertifikati yo'q yoki shubhali → 300¹ ustamasi qo'llanadi (365-modda holati bundan mustasno); sertifikat 1 yil ichida taqdim etilsa MFN/erkin savdo rejimi tiklanishi va ortiqcha to'lov qaytarilishi mumkin (49-bob).
- 364-modda: sertifikat majburiy hollar — preferensiya so'ralganda, kvota/cheklovli tovarlar, kelib chiqish ma'lumoti yo'q yoki shubhali bo'lganda, qonun/shartnomada nazarda tutilganda.
- MFN ro'yxati (MYU 3267): 47 davlat, jumladan **Xitoy (23)** va **Turkiya (37)**. Erkin savdo ro'yxati: Belarus, Gruziya, Qozog'iston, Qirg'iziston, Moldova, Rossiya, Turkmaniston*, Ukraina, Tojikiston, Ozarbayjon.
- **Ochiq savollar [UNVERIFIED]:**
  - aynan 10% / 20% / 30% chegarasi: "o'n foizgacha" va "o'n foizdan yigirma foizgacha" — 10% qaysi bandga? Engine: chegarada **ikkala variantni** ko'rsatadi va "odam tasdiqlasin" deydi.
  - 0% stavkali tovar: "o'n foizgacha → besh foiz" so'zma-so'z 0% ni ham qamraydi; ikkilamchi manbalar "bojdan ozod — ustamadan ham ozod" deydi. Engine: 0% kodda ustama `unknown`, UI ogohlantiradi.
  - aralash stavkada "advalor stavka turi" — engine advalor komponentni oladi (ASSUMPTION).
- Ustama summasi: `surcharge = cv_uzs * surcharge_pct/100` [ASSUMPTION: qo'shimcha boj ham advalor].

## 5. Erkin savdo (MDH, ST-1) va boshqa preferensiyalar [VERIFIED / qisman]

- **300-modda:** erkin savdo davlatlarida ishlab chiqarilgan **va** shu davlatlardan olib kirilgan tovarlarga boj qo'llanmaydi; eksportchi shartnoma ishtirokchisi davlatning rezidenti bo'lishi va tovar ishtirokchi davlat hududidan kelishi shart. Aks holda — tarif stavkasi.
- MDH ZST shartnomasi (18.10.2011) — O'zbekiston uchun Protokol (Minsk, 31.05.2013), ratifikatsiya ZRU-362 (27.12.2013): https://lex.uz/docs/2304877. Protokolga ko'ra O'zbekiston bilan savdoda **1993-yil 24-sentabrdagi MDH kelib chiqish qoidalari** qo'llanadi [protokol matni nrm.uz dan o'qildi; lex.uz dagi protokol matni ochilmadi — UNVERIFIED on lex]. Sertifikat shakli — ST-1 [UNVERIFIED on lex.uz].
- **Turkiya:** O'zbekiston–Turkiya imtiyozli savdo bitimi (Toshkent, 29.03.2022), PQ-65 (22.02.2023) bilan tasdiqlangan, kuchga kirgan 01.07.2023: https://lex.uz/docs/-6488935 (o'zb.), https://lex.uz/en/docs/6489973 (ingl.). Turkiya tovarlari uchun imtiyoz faqat **I-B ilovadagi 12 ta HS6** ga: 721049, 841370, 848180, 850213, 850490, 853710, 853720, 853890, 854442, 854449, 903289, 940690 (asosan 50% kamaytirish, 940690 — 60%). Kelib chiqish dalili — **EUR.1** harakat sertifikati; to'g'ridan-to'g'ri tashish talabi (II ilova, 12-modda). Kiyim, poyabzal, telefon, LED lampa, mebel (9403) — **ro'yxatda yo'q**.
- Boshqa imtiyozli rejimlar (engine'da "mavjud, lekin qo'llab-quvvatlanmaydi → odamga"): xalqaro brendlar uchun pasaytirilgan stavkalar (PQ-393, 12.10.2022; PQ-374, 13.12.2025 tahriri: https://lex.uz/uz/docs/-7912240), tarif kvotalari (VM 416, 29.07.2026 — UNVERIFIED, faqat nrm.uz ro'yxatida ko'rildi).

```
if origin in FTA_LIST and exporter_resident_of_FTA and shipped_from_FTA_territory and cert(ST-1 yoki shartnoma shakli):
    duty = 0
elif origin == "TR" and hs6 in TR_PTA_IB and cert == "EUR.1" and direct_transport:
    duty = cv * pta_rate
elif origin in MFN_LIST and (cert_not_required or cert_present):
    duty = duty_base
else:
    duty = duty_base + surcharge_300_1
```
Hech qachon "boshqa davlat orqali jo'nating" maslahati yo'q (Spec v2).

## 6. Aksiz [VERIFIED]

- Aksiz to'lanadigan tovarlar va stavkalar: Soliq kodeksi **289¹** (tamaki), **289²** (alkogol), **289³** (neft mahsulotlari, polietilen granulalar, tabiiy gaz, qadoqlangan shirin ichimliklar, energetik ichimliklar, chips). Baza — **285-modda** (import: advalor → bojxona qiymati; qat'iy → naturadagi hajm). Aksiz sanasi importda — import rejimiga chiqarish sanasi (286-modda).
- 289³ ning 2-qismi: tabiiy gaz stavkasi importda qo'llanmaydi.
- Demo tovarlar (telefon, noutbuk, futbolka, poyabzal, o'yinchoq, kosmetika, mikroto'lqinli pech, LED lampa, mebel) — **aksiz yo'q**.
- Engine: aksiz jadvali alohida (`excise_rule`), kod → aksiz guruhi xaritasi qo'lda tasdiqlanadi.

## 7. QQS [VERIFIED]

- **258-modda:** stavka 12% (36-bobdagi hollarda 0%).
- **254-modda:** import bazasi = bojxona qiymati + to'lanadigan aksiz + to'lanadigan bojxona boji. Bojxona kodeksi **322-modda** ham shuni aytadi.
- QQSdan ozod import: **246-modda** — kod bo'yicha xarita alohida qilinsin [UNVERIFIED for demo codes].
- **300¹ qo'shimcha boji QQS bazasiga kiradimi** — 254-modda "bojxona boji" deydi; qo'shimcha boj ham bojxona boji turi → kiradi deb hisoblaymiz [ASSUMPTION].

```
vat_base = cv_uzs + duty_total + excise
vat      = vat_base * 0.12
```

## 8. Rasmiylashtirish yig'imi [VERIFIED; chegaralar ASSUMPTION] — `fees.json` ga qarang

```
cv_usd = cv_uzs / usd_rate(decl_date)
band   = first band where from <= cv_usd < to     # chegaralar ASSUMPTION
fee    = bhm(decl_date) * band.multiplier
if regime == "IM40" and pre_arrival_declaration and decl_date >= 2026-03-01: fee *= 0.8
```

## 9. Yaxlitlash [UNVERIFIED — rasmiy qoida topilmadi]

- Bojxona kodeksi 293, 322–326-moddalarida, Soliq kodeksi 254/258-moddalarida va VM 55 da **yaxlitlash qoidasi yo'q** (o'qilgan matnlarda topilmadi). BYDni to'ldirish yo'riqnomasi (AV ro'yxat № 2773, 2773-15 / 22.07.2026 tahriri, https://lex.uz/uz/docs/2924955 ) 25-band 40-kb: grafa 45 dagi bojxona qiymati (shartnoma valyutasida) «математик қоидаларга кўра вергулдан сўнг икки белгигача» yaxlitlanadi; 41-kb: statistik qiymat — 3 xonagacha; 42-kb (grafa 47): to'lov summalari so'mda, har bir tovar va to'lov turi bo'yicha alohida, 12/45 qiymatlari so'mga BYD qabul qilingan kundagi MB kursi bo'yicha qayta hisoblanadi. **To'lov summasini so'mgacha yaxlitlash qoidasi yo'riqnomada ham topilmadi.** MB kurs qoidalari o'qilmadi.
- **Taklif qilingan ASSUMPTION (UIda yozilsin):** `Decimal` arifmetika; kurs MB bergan aniqlikda (2 xona); oraliq natijalar yaxlitlanmaydi; har bir to'lov turi (boj, aksiz, QQS, yig'im) oxirida **so'mgacha ROUND_HALF_UP**; QQS bazasi yaxlitlangan boj summasidan hisoblanadi (deklaratsiyada boj summasi butun so'mda yoziladi deb). Bitta haqiqiy qabul qilingan BYD bilan so'mgacha solishtirib tasdiqlang.

## 10. Muddatlar va boshqalar (ma'lumot uchun) [VERIFIED]

- 327-modda: to'lovlar deklaratsiya qabul qilinguncha yoki qabul bilan bir vaqtda.
- 349-modda: kechiktirilgan qarzdorlikka penya.
- 262-modda: dastlabki deklaratsiya — tovar 30 kalendar kun ichida taqdim etilmasa, berilmagan hisoblanadi.
- PF-250: 01.03.2026 dan — dastlabki deklaratsiyada yig'im −20%, bo'lib to'lashda 14 kungacha foiz yo'q; 01.06.2026 dan — tadbirkorlarga bojni 120 kungacha kechiktirish imkoniyati.
- Dastlabki tasnif qarori: 370–374-moddalar, 1 yil amal qiladi (372), yig'im 0,75 BHM (VM 55, 6-pozitsiya).
- IMEI (8517 13 telefonlar): VM 778 (17.09.2019) Nizom, 14-band — import IMEI kodlari BYD **31-grafasida** majburiy; IM-40 rasmiylashtirilmaguncha UZIMEI ro'yxatiga qo'yilmaydi: https://www.lex.uz/docs/-4517458 . To'lov — Nizom 6-ilova [miqdori UNVERIFIED on lex; uzimei.uz: 20% BHM].

## 11. `tiftn_codes_pq181_annex1.csv` haqida
- Manba PDF matnidan `pdftotext` bilan ajratildi; 13 149 qator, 13 138 noyob kod (11 ta takror — sahifa sarlavhalari yoki "+" belgili qayta ishlatilgan kodlar).
- `plus_flag_reused_code=1` — "ko'rsatilgan raqamli kod TIF TN oldingi tahririda foydalanilgan, lekin boshqa tovarlarni qamrab olgan" (1-ilova kirish qismi).
- Tavsif faqat birinchi qator (davomi kesilgan); qo'shimcha o'lchov birligi PDF ustunidan.
- PQ-181 dan keyin VM tomonidan tasdiqlangan kod o'zgarishlari (PQ-181 4-band) va PQ-58 (2515 bo'linishi) bu CSVda **yo'q** → production uchun NOTARIF bilan solishtiring.

---
O'zgarishlar: 18.11.2026 04:30 (UTC+5) — §9 ga BYD yo'riqnomasi № 2773 (2773-15, 22.07.2026) 25-band 40–42-kb bo'yicha yaxlitlash/grafa 45–47 ma'lumoti qo'shildi. Grafa xaritasi: tariff-payments.md §3 8-band va data/declarant/grafa-map.json (grafa 36 IM40 da ishlatilmaydi; 43 = 0/1; imtiyoz 44/6XX; kelib chiqish 34). Grafa 31 (IMEI) o'zgarmadi.

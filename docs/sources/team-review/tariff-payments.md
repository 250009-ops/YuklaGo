# YuklaGo design-v0.1 — TIF TN, bojxona qiymati va to'lovlar ekranlari bo'yicha ekspert sharhi

Muallif: TIF TN va Bojxona To'lovlari Mutaxassisi (`3d549ef3`) · Tekshirilgan sana: 18.11.2026 (Toshkent, UTC+5)
Manbalar: spec `yuklago-spec-v2.md`, `design-v0.1/yuklago-web-ui-v0.1.pdf` (28 bet), `design-rationale.md`.
Mashina o'qiydigan ma'lumotlar: `/workspace/hackathon/data/tariff/` (`tariff_demo.json/.csv`, `fees.json`, `rules.md`, `tiftn_codes_pq181_annex1.csv`).

Belgilar: **✅ to'g'ri** · **❌ xato** · **➕ yetishmaydi** · **⚠️ TASDIQLANMAGAN (UNVERIFIED)** — rasmiy matnda topilmagan yoki faqat ikkilamchi manbadan.
Qoida: har bir stavka hujjatga havola qilinadi. Hech qanday raqam taxmin qilinmagan. Dizayndagi barcha raqamlar `design-rationale.md` bo'yicha "namuna" — lekin ular "Rasmiy" chip bilan ko'rsatilgan, shuning uchun xato deb belgilandi.

---

## 0. Qisqa xulosa (3 qator)

1. **Eng katta xatolar:** "Rasmiy" chip namunaviy raqamlarda turibdi — 8539 52 000 0 kodi rasmiy ro'yxatda yo'q (faqat …1/…2/…9), LED lampa boji 10% emas **15%**, yig'im 310 000 emas **1 BHM = 440 000** (dastlabki deklaratsiyada 352 000), CBU kurslari 01.10.2026 ning haqiqiy kurslariga mos emas va sana noto'g'ri (kurs BYD qabul qilingan kun bo'yicha olinadi, BK 326-m.), TIF TN tahriri "01.11.2026" emas — oxirgi tahrir **16.02.2026 (PQ-58)**.
2. **Eng katta yetishmayotgan mantiq:** bojxona qiymati usuli (1–6) va o'zaro bog'liq shaxs savoli yo'q; chegaradan keyingi transport xarajati qiymatga qo'shilmoqda (BK 304/305); kombinatsiyalangan stavkaning "kam bo'lmagan" minimum qismi (dona/juft/kg) uchun qo'shimcha o'lchov birligi so'ralmaydi; kelib chiqish / MFN (BK 300¹ ustama) va imtiyoz (FTA, Turkiya PTA, EUR.1/ST-1) hisob-kitobi yo'q; stavkalar sana bo'yicha versiyalanmagan.
3. **Ma'lumot manbalari holati:** boj stavkalari (PQ-181 2-ilova, PQ-58 tahririda), 10 xonali kodlar ro'yxati (PQ-181 1-ilova PDF), QQS (SK 254/258), aksiz (SK 289¹–289³), yig'im (VM 55, VM 700 tahririda), BHM (PF-115), MFN ro'yxati (MYU 3267), Turkiya PTA (PQ-65) va CBU API — **lex.uz/cbu.uz da tekshirildi**; yaxlitlash qoidasi, yig'im oraliqlari chegaralari (aniq 10 000 USD), 300¹ chekka holatlari, kg netto/brutto, ST-1 matni, ruxsatnoma ro'yxatlari mazmuni — **TASDIQLANMAGAN**.

---

## 1. TIF TN kodi ekrani (PDF p.14, kutubxona p.25, go/no-go p.12)

### ✅ To'g'ri
- Kod 10 xonali ko'rinishda, "Taklif" (AI) va "Siz tasdiqladingiz" chiplari ajratilgan — spec v2 Y4/Y5 ga mos.
- Muqobil kodlar bilan solishtirish (alternativ kod boji farqi) g'oyasi to'g'ri.
- AI kodni o'zi "tasdiqlamaydi", foydalanuvchi tasdiqlaydi — to'g'ri (yakuniy javobgarlik deklarantda, MJtK 227²²).

### ❌ Xato
| Joy | Dizaynda | Rasmiy holat | Manba |
|---|---|---|---|
| p.14, p.25 kod | `8539 52 000 0` "✓ Joriy" | Bunday 10 xonali kod **yo'q**. 8539 52 000 faqat 3 ga bo'linadi: `8539 52 000 1` (≥24 ta ketma-ket LED filamentli kompozit asosli), `8539 52 000 2` (≥25 mm diametrli to'g'ri ikki uchli trubkalar), `8539 52 000 9` (boshqalar). Qo'shimcha birlik: dona. | PQ-181 (14.05.2025) 1-ilova, 01.06.2025 dan kuchda — https://lex.uz/uz/files/7541055.zip ; https://lex.uz/uz/docs/-7533457 |
| p.14 boj | 10% | `853952` (LED lampalar) — **15%** | PQ-181 2-ilova (PQ-58 11.02.2026 tahririda, ruscha konsolidatsiya https://lex.uz/docs/3802366 ) |
| p.14 muqobil | 9405 42 — 15% | 9405 asosiy stavkasi **5%**; istisno ro'yxatidagi kodlar (jumladan 9405420012/019/032/033/039) — **10%, lekin 1 kg uchun 0,5 USD dan kam emas**. Qaysi biri ekanini 10 xonali kod hal qiladi. | o'sha |
| p.25 kutubxona | "bu kod qatori 01.11.2026 … o'zgardi" | 01.11.2026 da tarif tahriri yo'q. Konsolidatsiyalangan matn tahrirlari: 16.02.2026, 20.05.2025, 29.01.2025, … | https://lex.uz/docs/3802366 tahrirlar ro'yxati |
| p.14 tahrir sanasi | "tahrir 01.11.2026" | Joriy tahrir: PQ-181 2-ilova, PQ-58 (11.02.2026) bilan o'zgartirilgan, 16.02.2026 dan | o'sha |
| p.12 dron (YG-0409) | "Tovar nazoratda: [ruxsat turi]" | VM 658 (15.11.2022) bo'yicha UUA (dron) va qismlarini noqonuniy olib kirish **taqiqlangan**; faqat nomlangan tashkilotlar yoki VM alohida qarori bilan ruxsat. Bundan tashqari VM 658 eski kodlarni (8802200001/02/08, 8803100000, 8803200000) keltiradi, HS2022 da dronlar **8806** ga o'tgan — kod xaritalash ochiq. | https://www.lex.uz/uz/acts/-6284990 ; https://gov.uz/oz/uzcaa/pages/dronlar-uua |
| p.14 "Asl belgisi: talab qilinmaydi" (LED) | talab yo'q | VM 737 1-ilova 4-band ("Maishiy texnika", 15.04.2022 dan) ro'yxatida `8539500000` (eski LED lampa kodi) bor. HS2022 dagi 8539 52 000 x ga qo'llanishi — **ochiq savol**; "talab qilinmaydi" deb yozish mumkin emas. Mikroto'lqinli pech `8516500000` ro'yxatda aniq bor. | VM 737 (20.11.2020), 1-ilova VM 23 (23.01.2026) tahririda — https://lex.uz/uz/docs/-5115923 |

### ➕ Yetishmaydi (maydonlar / holatlar)
1. **10 xonali validatsiya**: faqat raqam, aynan 10 belgi, PQ-181 1-ilova ro'yxatida mavjudligi (`tiftn_codes_pq181_annex1.csv`, 13 138 noyob kod). Holatlar: `KOD_TOPILMADI`, `KOD_FAOL_EMAS` (eski tahrirdagi kod, masalan 8539500000), `STAVKA_QATORI_YO'Q`, `NOANIQ_10_XONA` (6 xona aniq, oxirgi 4 xona bo'yicha bir nechta variant).
2. **"+" belgisi**: PQ-181 1-ilovada "+" bilan belgilangan kodlar — oldingi tahrirdagi kod qayta ishlatilgan, lekin qamrovi boshqa. Foydalanuvchi kutubxonasidagi eski kod bilan solishtirishda ogohlantirish kerak.
3. **Nomzod kodlar ro'yxati**: har bir nomzod uchun — ishonch darajasi (AI), qaysi **ATQ (TIF TN ni talqin qilishning asosiy qoidalari) 1–6** qo'llangani va qisqa asos (masalan: "ATQ 1 — 8539 pozitsiya matni; ATQ 6 — 8539 52 subpozitsiyasi; 10 xona — diametr/filament belgisi bo'yicha"). Hal qiluvchi belgi uchun foydalanuvchiga savol (masalan, "trubka shaklidami? diametri ≥25 mm?").
4. **Rasmiy nom**: PQ-181 1-ilovadagi rasmiy matn (kirill → lotin transliteratsiya alohida belgilanadi) + qo'shimcha o'lchov birligi.
5. **Dastlabki qaror (BK 370–374)**: "Kod bo'yicha dastlabki qaror olish" yo'li — yig'im 0,75 BHM (VM 55 1-ilova), qaror 1 yil amal qiladi (⚠️ muddat BK matnidan qayta tekshirilsin). Qaror bo'lsa — kod "Dastlabki qaror №…, sana" chipi bilan qulflanadi.
6. **Nazorat bayroqlari**: sertifikatlash (VM 43 ro'yxatlari), Asl Belgisi (VM 737 1-ilova), IMEI (telefonlar, VM 778), taqiqlangan/litsenziyalanadigan (dron — VM 658). Har biri manba + tahrir sanasi bilan; manba yuklanmagan bo'lsa — "Tekshirilmadi", "Topilmadi" emas.
7. **Kod o'zgarishi xaritasi**: eski kod → yangi kod (VM 349, 04.06.2025: TIF TN yangilanishi munosabati bilan kodlari o'zgargan mahsulotlar — https://lex.uz/en/acts/7558317 ). Kutubxona saqlangan kodlar uchun kerak.

---

## 2. Bojxona qiymati ekrani (p.10 "Yetkazib berilgan narx", p.11)

### ✅ To'g'ri
- Tovar qiymati + transport ajratilgan; transport "≈ Taxmin" sifatida ko'rsatilishi kerakligi rationale da bor.
- Dizayndagi arifmetika ichki jihatdan izchil (48,6 mln + 6,2 mln; boj 5,48 mln; QQS 7 233 600; jami 67 823 600; bojxona ulushi 13 023 600; muqobil +3 068 800) — xato faqat kirish raqamlarida.

### ❌ Xato
| Joy | Dizaynda | To'g'risi | Manba |
|---|---|---|---|
| p.10 transport | "Shenzhen → Toshkent ≈ 6 200 000" "[Rasmiy manba]" | Qiymatga faqat **O'zbekiston bojxona chegarasidagi kirish joyigacha** bo'lgan transport, yuklash/tushirish, sug'urta qo'shiladi (BK 304); kirish joyidan keyingi transport, agar alohida ajratilgan bo'lsa, chegirib tashlanadi (BK 305). Taxminga "Rasmiy" chip qo'yilmaydi. | Bojxona kodeksi 304, 305-m. — https://lex.uz/docs/-2876354 |
| p.10 kurs | USD 12 650 · CNY 1 754,51 "Rasmiy 01.10.2026" | CBU 01.10.2026: USD **11 808,76**, CNY **1 761,29**. Bundan tashqari to'g'ri sana — **BYD qabul qilingan kun** (BK 326), 01.10 emas. | https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/2026-10-01/ |
| p.10 hujjat nomi | "[Rasmiy hujjat nomi] · tahrir 01.11.2026" | Tovar qiymati — rasmiy hujjat emas, invoys (chip: "Hujjat"). Kurs uchun: "O'zbekiston Respublikasi Markaziy banki rasmiy kursi, {sana}". | — |

### ➕ Yetishmaydi
1. **Usul tanlash 1–6** (BK 301–313): 1 — bitim qiymati (303); 2 — aynan o'xshash tovar; 3 — o'xshash tovar; 4 — chegirish; 5 — qo'shish; 6 — zaxira usul. Ketma-ket qo'llanadi. MVP: faqat 1-usul; boshqa holatda — "Deklarantga yo'naltirish".
2. **O'zaro bog'liq shaxs savoli** (BK 306–308): "Sotuvchi bilan aloqadormisiz (ulush, oila, boshqaruv)?" → "Ha" bo'lsa: ogohlantirish + deklarantga eskalatsiya; 1-usul faqat bog'liqlik narxga ta'sir qilmagani isbotlansa.
3. **Qo'shiladigan elementlar** (BK 304): komissiya/broker haqi (xarid komissiyasidan tashqari), qadoq va idish, xaridor bergan materiallar (assists), litsenziya to'lovlari, sug'urta, yuklash/tushirish. Har biri: summa, valyuta, hujjat.
4. **Incoterms** maydoni: EXW/FOB/CIF/DAP… → qaysi xarajatlar narxga kirgani avtomatik tekshiriladi.
5. **Kurs sanasi mantiqi**: `fx_date = BYD qabul qilingan sana` (oldindan ko'rsatishda — "bugungi kurs, BYD kuni o'zgarishi mumkin" ogohlantirishi). CBU API qaytargan `Date` so'ralgan sanadan oldin bo'lishi mumkin (dam olish kunlari: 16.11.2026 so'ralganda `Date` = 14.11.2026) — ikkalasi saqlanadi. `Nominal` maydoni hisobga olinadi.
6. **Qo'shimcha o'lchov birligi va netto og'irlik**: kombinatsiyalangan stavka minimumi uchun (dona/juft/kg). ⚠️ "kg" netto yoki brutto ekanligi stavka matnida aniqlanmagan.
7. **Bir nechta tovar qatori**: transport/sug'urtani qatorlar o'rtasida taqsimlash usuli (og'irlik yoki qiymat bo'yicha) — ⚠️ rasmiy taqsimlash qoidasi tekshirilmagan; foydalanuvchi tanlovi + belgi.

---

## 3. To'lovlar ekranlari (p.10, p.15–16 BYD qoralamasi grafa jadvali)

### ✅ To'g'ri
- To'lov turlari ajratilgan: boj, QQS, yig'im (aksiz yo'q — dizayndagi tovarlar uchun to'g'ri).
- QQS 12% — SK 258.
- Boj → QQS ketma-ketligi (QQS bazasiga boj qo'shiladi) to'g'ri.

### ❌ Xato
| Joy | Dizaynda | To'g'risi | Manba |
|---|---|---|---|
| p.15 yig'im | 310 000 "Rasmiy · 01.11.2026", "[asos]" | VM 55 1-ilova: bojxona qiymati ≤10 000 USD — **1 BHM**. BHM 01.09.2026 dan **440 000** so'm → **440 000**. Dastlabki (kelgunga qadar) deklaratsiyada 20% chegirma → **352 000**. 310 000 hech bir rasmiy qiymatga mos emas. | VM 55 (31.01.2025) 1-ilova, VM 700 (06.11.2025) tahririda — https://lex.uz/docs/-7357270 ; PF-115 (23.06.2026) 3(b)(ii); PF-250 (17.12.2025) 2(a) — https://lex.uz/uz/docs/-7934915 |
| p.10/p.15 QQS formulasi yorlig'i | "QQS = (qiymat + boj) × 12%" | Baza = bojxona qiymati + boj + **aksiz** (BK 322; SK 254). Aksizsiz tovarda natija bir xil, lekin formula/yorliq to'liq bo'lishi kerak. ⚠️ 300¹ ustamasi bazaga kirishi — tekshirilmagan (rules.md §7). | SK 254, 258; BK 322 |
| Spec v2 (27-qator) | "20% chegirmani e'lon qilmang" | **Eskirgan**: PF-250 2(a) — 01.03.2026 dan kelgunga qadar erkin muomalaga deklaratsiyada yig'im 20% kam; VM 55 1-ilova izohida ham bor (⚠️ izohni kiritgan aniq hujjat tekshirilmagan). | PF-250 |
| Spec v2 §8.5 | aksiz akti "nomlanmagan" | SK **289¹** (tamaki), **289²** (alkogol), **289³** (neft mahsulotlari, polietilen granulalar, tabiiy gaz, qadoqlangan shirin ichimliklar, energetik ichimliklar, chipslar); baza — SK 285, 286. Telefon, kiyim, lampa — aksizsiz. | Soliq kodeksi — https://lex.uz/docs/-4674902 |

### YG-0412 qayta hisob (illyustratsiya; sana 18.11.2026, rasmiy kurslar bilan)
Kirish (dizayndan): invoys 27 700 CNY, transport 6 200 000 so'm (⚠️ chegaradan keyingi qism ajratilmagan — taxmin), kod 8539 52 000 9, boj 15%.
| Qator | Hisob | So'm |
|---|---|---|
| CNY kursi 18.11.2026 | CBU | 1 801,75 |
| Bojxona qiymati | 27 700 × 1 801,75 + 6 200 000 | 56 108 475 |
| Boj 15% | 56 108 475 × 0,15 | 8 416 271 |
| QQS bazasi | 56 108 475 + 8 416 271 | 64 524 746 |
| QQS 12% | | 7 742 970 |
| Qiymat USD da | 56 108 475 / 12 010,45 | 4 671,64 USD → ≤10 000 oralig'i |
| Yig'im | 1 BHM (dastlabki deklaratsiya bo'lsa 352 000) | 440 000 |
| **Bojxona to'lovlari jami** | | **16 599 241** (dizaynda 13 023 600) |
⚠️ Yaxlitlash (butun so'mgacha, har bir to'lov alohida) — taxminiy qoida, rasmiy matn topilmagan.

### ➕ Yetishmaydi
1. **Kombinatsiyalangan stavka** (BK 293): "X%, lekin … dan kam emas" → `max(ad valorem, specific)`; "X% va …" → `yig'indi`. Spesifik qism USD da → kurs bilan so'mga. Birlik miqdori (dona/juft/kg) maydoni majburiy.
2. **Aksiz** qatori: 289¹–289³ ro'yxatida bo'lsa hisoblash, aks holda "Aksiz: qo'llanmaydi (SK 289¹–289³)".
3. **Kelib chiqish va MFN**: kelib chiqish mamlakati maydoni → MFN ro'yxatida bo'lmasa yoki sertifikat yo'q bo'lsa — BK **300¹** ustamasi: asosiy stavka ≤10% → +5 p.p.; 10–20% → +10; 20–30% → +15; ≥30% → +20 (O'RQ-1097, 28.02.2026 dan). ⚠️ Aniq chegara (10% qaysi guruhga), 0% tovarlar, kombinatsiyalangan stavkalar — ochiq. Xitoy (#23) va Turkiya (#37) MFN ro'yxatida bor (MYU 3267, 30.06.2020 — https://lex.uz/uz/docs/-4911943 ).
4. **Imtiyoz (preferensiya)**: MDH FTA (2011 Shartnoma; O'zbekiston uchun Protokol ZRU-362, 16.05.2014 dan; sertifikat ST-1 — ⚠️ lex.uz da shakl matni tekshirilmagan) va Turkiya PTA (PQ-65, 01.07.2023 dan; faqat 12 ta HS6 qator, EUR.1, to'g'ridan-to'g'ri tashish). Kelib chiqish sertifikati yo'q bo'lsa — BK 366: imtiyoz yo'q + 300¹; 1 yil ichida sertifikat bilan qayta ko'rib chiqish.
5. **Rate effective-date versioning**: stavka BYD qabul qilingan kundagi tahrir bo'yicha (BK 324). Har bir hisobda `rule_set_version`, `tariff_edition_date`, `fx_date`, `bhm_value+date` saqlanadi. BHM o'zgarishi (412 000 → 440 000, 01.09.2026) — `bhm` jadvali sanalar bilan.
6. **Muddatlar**: to'lov BYD qabul qilinishidan oldin/bir vaqtda (BK 327); kechiksa penya (BK 349); dastlabki deklaratsiya — tovar 30 kalendar kun ichida taqdim etilmasa bekor (BK 262); PF-250 2(b) — bo'lib to'lashda 14 kun foizsiz; 8(a) — 01.06.2026 dan boj to'lovini 120 kungacha kechiktirish (⚠️ shartlar to'liq tekshirilmagan).
7. **IMEI** (telefonlar 8517 13): BYD 31-grafada IMEI majburiy (VM 778, 17.09.2019, 14-band — https://www.lex.uz/docs/-4517458 ); ro'yxatdan o'tkazish IM-40 dan keyin. ⚠️ IMEI yig'imi miqdori lex.uz da tekshirilmagan.
8. **BYD qoralama grafalari (IM40)** (p.15–16) — BYD to'ldirish yo'riqnomasi (AV ro'yxat № 2773, 2773-15 / 22.07.2026 tahriri, https://lex.uz/uz/docs/2924955 ) bo'yicha: deklarant IM40 da faqat 24-bandda sanalgan grafalarni to'ldiradi (1, 2, 3, 5, 7 (post kodi), 8, 9, 11, 12, 13, 14, 15, 15а, 18–26, 28–35, 37–50, 54, «С») — **16, 17 va 36 bu ro'yxatda yo'q**. To'lov/qiymat uchun kerakli grafalar: 12 (umumiy bojxona qiymati, 25-band 9-kb), 23 (valyuta kursi, 19-kb), 31 (tovar tavsifi; IMEI — VM 778), 33 (tovar kodi, 28-kb), **34 (kelib chiqish mamlakati kodi — har bir tovar bo'yicha, 29-kb; noma'lum bo'lsa «000»)**, 41 (qo'shimcha o'lchov birligi, 36-kb), 42 (fakturaviy qiymat, 37-kb), **43 = «0» (o'z ehtiyoji uchun emas) / «1» (o'z ehtiyoji uchun), 38-kb — qiymat usuli EMAS**, **44 (hujjatlar, 39-kb): to'lov imtiyozlari — «6» + to'lov turi kodi + asos hujjat (39-kb «е»; 12-ilova 62-qator, kod 6XX); kelib chiqish sertifikati (import) — 12-ilova 63-qator, kod 701 «СПТИМ»; qiymat usuli — 12-ilova 113-qator, kod 904 «МЕТОД»** (qaysi grafada 904 qo'llanishi yo'riqnomada aytilmagan — 44 ekanligi XULOSA), 45 (bojxona qiymati, 40-kb; shartnoma valyutasida, verguldan keyin 2 xonagacha matematik yaxlitlanadi), 46 (statistik qiymat, 41-kb), 47 (to'lovlar hisobi, 42-kb; har bir tovar va to'lov turi bo'yicha alohida, yig'im esa asosiy varaqning 47-grafasida). **36-grafa bo'sh qoldiriladi** (qog'oz shakldagi «36 Преференция» katagi ham); 16-grafa IM40 da to'ldirilmaydi. Grafa 7, 44, 47, A, B, D ni bojxona organi ham to'ldiradi (89-band). Batafsil: `data/declarant/grafa-map.json`.
9. **Holatlar**: `STAVKA_TOPILMADI` → summa ko'rsatilmaydi; `KURS_YO'Q` (CBU javobi bo'sh); `BIRLIK_MIQDORI_YO'Q` (minimum hisoblanmaydi → ogohlantirish); `KELIB_CHIQISH_NOMA'LUM` → 300¹ xavfi; `BOG'LIQ_SHAXS` → eskalatsiya; `NAZORAT_TOVARI` → to'xtatish.

---

## 4. Rules engine — ma'lumot manbalari

| Ma'lumot | Hujjat (tahrir) | URL | Holat |
|---|---|---|---|
| 10 xonali kodlar ro'yxati, rasmiy nomi, qo'shimcha birlik | PQ-181 (14.05.2025) 1-ilova, 01.06.2025 dan | https://lex.uz/uz/files/7541055.zip | ✅ yuklab, 13 138 kod parse qilindi |
| Import boj stavkalari | PQ-181 2-ilova (o'zbekcha); PQ-3818 (10.07.2018) konsolidatsiya, oxirgi tahrir 16.02.2026 (PQ-58, 11.02.2026) | https://lex.uz/uz/docs/-7533457 ; https://lex.uz/docs/3802366 | ✅ |
| Kod o'zgarishlari xaritasi | VM 349 (04.06.2025) | https://lex.uz/en/acts/7558317 | ✅ mavjud, ⚠️ to'liq parse qilinmagan |
| Brendlar uchun pasaytirilgan stavkalar | PQ-374 (13.12.2025), PQ-393 (12.10.2022) ni o'zgartiradi | https://lex.uz/uz/docs/-7912240 | ⚠️ MVP dan tashqari |
| Tarif kvotalari | VM 416 (29.07.2026) | — | ⚠️ faqat nrm.uz |
| Bojxona qiymati, kurs, stavkalar sanasi, to'lov muddati | Bojxona kodeksi 293, 300, 300¹, 301–313, 322–327, 349, 358–366, 369–374, 262 | https://lex.uz/docs/-2876354 | ✅ moddalar o'qildi |
| MFN ustamasi | BK 300¹ (O'RQ-1097, 27.11.2025; 28.02.2026 dan) | BK ichida | ✅ / ⚠️ chekka holatlar |
| MFN mamlakatlar ro'yxati | MYU ro'yxatga olish № 3267 (30.06.2020) | https://lex.uz/uz/docs/-4911943 | ✅ |
| Turkiya PTA | PQ-65 (22.02.2023), 01.07.2023 dan | https://lex.uz/uz/docs/-6388997 ; https://lex.uz/docs/-6488935 | ✅ |
| MDH FTA | Protokol (Minsk, 31.05.2013), ZRU-362 (27.12.2013), 16.05.2014 dan | https://lex.uz/docs/2304877 | ✅ / ⚠️ ST-1 qoidalari |
| QQS | Soliq kodeksi 246, 254, 258 | https://lex.uz/docs/-4674902 | ✅ |
| Aksiz | SK 285, 286, 289¹–289³ | o'sha | ✅ |
| Bojxona yig'imi | VM 55 (31.01.2025) 1-ilova, VM 700 (06.11.2025; 08.02.2026 dan) va VM 393 (20.07.2026) tahririda | https://lex.uz/docs/-7357270 | ✅ / ⚠️ oraliq chegaralari |
| Dastlabki deklaratsiya chegirmasi | PF-250 (17.12.2025) 2(a), 01.03.2026 dan | https://lex.uz/uz/docs/-7934915 | ✅ |
| BHM | PF-115 (23.06.2026), 01.09.2026 dan 440 000; oldingi 412 000 (PF-91, 02.06.2025) | https://www.lex.uz/uz/docs/-8283656 | ✅ / ⚠️ PF-91 lex da tekshirilmagan |
| Valyuta kursi | CBU API | https://cbu.uz/uz/arkhiv-kursov-valyut/json/{CCY}/{YYYY-MM-DD}/ | ✅ |
| Asl Belgisi | VM 737 (20.11.2020) 1-ilova, oxirgi tahrir 23.01.2026 (VM 23) | https://lex.uz/uz/docs/-5115923 | ✅ ro'yxat o'qildi |
| Majburiy sertifikatlash/deklaratsiyalash | VM 43 (30.01.2021), lex tahrirlari: 09.09.2026 (oxirgi), 01.01.2027 (rejalashtirilgan) | https://lex.uz/docs/5249380 | ⚠️ ilovalar matni yuklanmadi |
| Dronlar | VM 658 (15.11.2022) | https://www.lex.uz/uz/acts/-6284990 | ✅ (rasmiy uzcaa sahifasi orqali) |
| IMEI | VM 778 (17.09.2019) 14-band | https://www.lex.uz/docs/-4517458 | ✅ / ⚠️ yig'im |
| Javobgarlik | MJtK 227²² | https://lex.uz/docs/97661 | ✅ |
| customs.uz kalkulyator/sahifalar | — | customs.uz | ⚠️ JS, o'qilmadi |

---

## 5. Formulalar (pseudo-kod; batafsil — `data/tariff/rules.md`)

```
inputs: lines[], decl_date, fx_ccy, origin_country, pre_arrival(bool), cert_of_origin(type|null)

fx(ccy) = cbu_rate(ccy, decl_date) / nominal          # BK 326; saqlash: requested_date, cbu_date
for line in lines:
    cv = invoice*fx(inv_ccy) + additions_to_border(304) - deductions(305)    # 1-usul, BK 303
    row = tariff_line(line.code10, at=decl_date)       # BK 324; yo'q -> STAVKA_TOPILMADI, STOP
    adv = cv * row.ad_valorem_pct/100
    spec = row.specific_amount * fx(row.specific_ccy) * line.qty_in(row.specific_unit)  # qty yo'q -> STOP
    duty = max(adv, spec) if row.combine_rule=='min' else adv+spec if row.combine_rule=='sum' else adv   # BK 293
    pref = preference(origin_country, line.code10, cert_of_origin)              # FTA / PTA / null
    if pref: duty = apply_pref(pref)                                             # BK 300
    elif not mfn(origin_country) or cert_missing_required(): duty += cv*surcharge_pp(row.ad_valorem_pct)/100   # BK 300¹, 366 ⚠️
    excise = excise_calc(line) if line.code10 in excise_lists(289¹–289³) else 0
    vat = (cv + duty + excise) * 0.12 if not vat_exempt(246) else 0            # SK 254, 258; BK 322
total_cv_usd = sum(cv) / fx('USD')
fee = band(total_cv_usd).bhm_mult * bhm(decl_date)                               # VM 55 1-ilova ⚠️ chegaralar
if pre_arrival and decl_date >= 2026-03-01: fee *= 0.8                          # PF-250 2(a)
round each payment: Decimal, ROUND_HALF_UP to 1 so'm   # ⚠️ TASDIQLANMAGAN
```

---

## 6. Ma'lumotlar modeli

```
tariff_line(
  code10 CHAR(10) PK-part, effective_from DATE PK-part, effective_to DATE NULL,
  ad_valorem_pct DECIMAL, specific_amount DECIMAL NULL, specific_ccy CHAR(3) NULL,
  specific_unit ENUM(dona, juft, kg, l, ...) NULL, combine_rule ENUM(none, min, sum),
  excise_group ENUM(none, 289_1, 289_2, 289_3), vat_exempt_ref TEXT NULL,
  source_doc TEXT, source_url TEXT, edition_date DATE, verified BOOL, notes TEXT)
code_list(code10 PK, name_uz, name_ru, supplementary_unit, plus_flag BOOL,
  list_doc, list_edition_date, valid_from, valid_to)
code_map(old_code10, new_code10, source_doc, effective_from)            -- VM 349
fx_rate(ccy, requested_date, cbu_date, rate, nominal, fetched_at)        PK(ccy, requested_date)
bhm(value_uzs, effective_from, effective_to, source_doc)
fee_band(lower_usd, upper_usd, lower_inclusive, upper_inclusive, bhm_mult,
  effective_from, effective_to, source_doc, verified)
fee_item(kind, bhm_mult | per_kg_mult, basis, source_doc)               -- tranzit, kuryer, dastlabki qaror...
discount(kind='pre_arrival', pct=20, effective_from=2026-03-01, source_doc='PF-250 2(a)')
country(iso2, name_uz, mfn BOOL, mfn_source, fta_cis BOOL, pta_turkey BOOL)
preference(agreement, hs6_or_code10, base_rate, pref_rate, cert_form, direct_transport BOOL,
  effective_from, source_url)
control_flag(code10_or_prefix, kind ENUM(certification, declaration_of_conformity, asl_belgisi,
  imei, prohibited, license), list_doc, list_edition_date, effective_from, note)
calc_run(id, inputs_json, rule_set_version, tariff_edition_date, fx_dates, bhm_value,
  outputs_json, created_at)                                              -- takrorlanuvchanlik (spec §8.3)
```

---

## 7. Spec v3 uchun aniq o'zgartirishlar
1. 27-qatordagi "20% chegirmani e'lon qilmang" → PF-250 2(a) havolasi bilan ruxsat (01.03.2026 dan, kelgunga qadar erkin muomalaga deklaratsiya).
2. §8.5 jadvali: boj — "PQ-181 2-ilova (PQ-58 tahririda)", kodlar — "PQ-181 1-ilova PDF", aksiz — "SK 289¹–289³", yig'im — "VM 55 1-ilova (VM 700 tahririda) + PF-115 BHM".
3. Kurs sanasi: "BYD qabul qilingan kun (BK 326)".
4. Namuna tovarlar: LED lampa bojini 15% ga; yig'imni 440 000/352 000 ga; kodni 8539 52 000 9 ga (yoki …1/…2, tovarga qarab); dron misolini "taqiqlangan / VM alohida ruxsati" holatiga o'zgartirish yoki boshqa tovar tanlash.
5. "Rasmiy" chip faqat: boj stavkasi, QQS stavkasi, aksiz stavkasi, yig'im oralig'i + BHM, CBU kursi (sanasi bilan). Transport, sug'urta, jami summalar — "≈ Taxmin asosida".

## 8. Qolgan noaniqliklar (UNVERIFIED)
- Yaxlitlash qoidasi (har bir to'lov, so'm/tiyin) — rasmiy matn topilmadi.
- VM 55 oraliq chegaralari: aniq 10 000, 20 000 … USD qaysi oraliqqa kiradi ("…gacha" / "…dan ortiq") — faqat oxirgi oraliq aniq.
- BK 300¹: aynan 10/20/30% bazaviy stavka qaysi guruhga; 0% tovarlar; kombinatsiyalangan stavkaga ustama; QQS bazasiga kirishi.
- Spesifik minimumdagi "kg" — netto yoki brutto.
- ST-1 shakli va MDH kelib chiqish qoidalari matni lex.uz da.
- PF-91 (412 000 BHM) lex.uz da; VM 55 izohini kiritgan hujjat.
- VM 43 ilovalaridagi aniq TIF TN kodlari (sertifikat vs deklaratsiya) — lex.uz sahifasi matnni yuklamadi.
- VM 737 dagi 8539500000 ning HS2022 kodlariga tatbiqi; VM 658 eski 8802/8803 kodlarining 8806 ga xaritasi.
- IMEI ro'yxatdan o'tkazish yig'imi; dastlabki qaror muddati (1 yil) — BK matnidan qayta tekshirish.
- customs.uz kalkulyatori bilan solishtirish qilinmadi.

---
O'zgarishlar: 18.11.2026 04:30 (UTC+5) — §3 8-band (BYD grafalari) BYD yo'riqnomasi № 2773 (2773-15, 22.07.2026) 24-band, 25-band 9/19/28/29/36–42-kichik bandlari, 89-band va 12-ilova bo'yicha tuzatildi: 16 va 36 olib tashlandi, 43 = 0/1 «o'z ehtiyoji», imtiyozlar/sertifikat/usul — 44 (6XX / 701 / 904); manba: team-review/declarant-v3-check.md, lex.uz da qayta tekshirildi.

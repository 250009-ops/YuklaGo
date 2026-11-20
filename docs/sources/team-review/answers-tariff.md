# Javoblar: product.md (c) — TIF TN va Bojxona To'lovlari Mutaxassisi (`3d549ef3`)

Tekshirilgan: 18.11.2026 (Toshkent, UTC+5). Har bir javob — lex.uz/rasmiy manba + tahrir sanasi, yoki **UNVERIFIED**. Taxmin yo'q.
Batafsil asoslar: `team-review/tariff-payments.md`, `data/tariff/` (`tariff_demo.json`, `fees.json`, `rules.md`).

---

### 1. `[Rasmiy hujjat nomi]` (p.10 l.32) — tarif / kurs manbasi
- **Boj stavkasi:** "O'zbekiston Respublikasi Prezidentining 2025-yil 14-maydagi PQ-181-son qaroriga 2-ilova — Import bojxona boji stavkalari", 01.06.2025 dan kuchda; **joriy tahrir — PQ-58 (11.02.2026) bilan, 16.02.2026 dan**. Uzbekcha: https://lex.uz/uz/docs/-7533457 ; konsolidatsiyalangan (rus., PQ-3818 10.07.2018): https://lex.uz/docs/3802366 (tahrirlar: 16.02.2026, 20.05.2025, 29.01.2025, …).
- **Kod va rasmiy nom:** PQ-181 1-ilova (TIF TN, 10 xonali) — https://lex.uz/uz/files/7541055.zip .
- **Kurs:** "O'zbekiston Respublikasi Markaziy banki rasmiy kursi" — https://cbu.uz/uz/arkhiv-kursov-valyut/json/{CCY}/{YYYY-MM-DD}/ ; sana = BYD qabul qilingan kun (Bojxona kodeksi 326-m., https://lex.uz/docs/-2876354 ).
- **Chip matni:** "PQ-181, 2-ilova · tahrir 16.02.2026" (boj) va "MB kursi · {BYD sanasi}". "tahrir 01.11.2026" — **noto'g'ri**, bunday tahrir yo'q.
- Tovar qiymatining o'zi (48 600 000) rasmiy hujjat emas — chip "Hujjat (invoys)".

### 2. `[Rasmiy manba]` (p.10 l.40) — qaysi qatorlar rasmiy
| Qator | Rasmiy? | Manba |
|---|---|---|
| Boj stavkasi | ✅ | PQ-181 2-ilova (16.02.2026 tahriri) |
| QQS stavkasi 12% | ✅ | Soliq kodeksi 258-m. (baza — 254-m.; BK 322) https://lex.uz/docs/-4674902 |
| Yig'im (oraliq + BHM) | ✅ | VM 55 1-ilova (VM 700 tahriri) + PF-115 BHM |
| CBU kursi (sanasi bilan) | ✅ | cbu.uz API |
| Transport Shenzhen → Toshkent | ❌ **Taxmin** | — ("≈ Taxmin" chipi). Bundan tashqari faqat chegaradagi kirish joyigacha bo'lgan qismi qiymatga kiradi (BK 304), keyingisi chiqariladi (BK 305). |
| Bojxona qiymati, boj/QQS summalari, jami | ⚠️ Rasmiy stavka × taxminiy baza | "Taxmin asosida hisoblangan" — "Rasmiy" chip emas. |

### 3. Turkiya imtiyozi (p.11 l.22–23) — `[kelishuv nomi]`, `[x]`, `[y]`, `[shakl nomi]`
- Kelishuv mavjud: **O'zbekiston–Turkiya Imtiyozli savdo bitimi** (Toshkent, 29.03.2022), PQ-65 (22.02.2023) bilan tasdiqlangan, 01.07.2023 dan kuchda — https://lex.uz/uz/docs/-6388997 ; matn https://lex.uz/docs/-6488935 , https://lex.uz/en/docs/6489973 . Sertifikat: **EUR.1**; to'g'ridan-to'g'ri tashish talabi (II ilova 12-m.).
- Lekin O'zbekiston imtiyozlari (I-B ilova) faqat **12 ta HS6**: 721049, 841370, 848180, 850213, 850490, 853710, 853720, 853890, 854442, 854449, 903289, 940690 (masalan 853710: 10% → 5%; 940690: 10% → 4%).
- Dizayndagi Turkiya tovari (telefon g'iloflari, YG-0415) bu ro'yxatda **yo'q** → **"imtiyoz topilmadi" holati qolsin, x/y to'ldirilmasin.** (Turkiya MFN ro'yxatida #37 — 300¹ ustamasi qo'llanmaydi, MYU 3267, https://lex.uz/uz/docs/-4911943 .)
- Agar demo uchun haqiqiy imtiyozli misol kerak bo'lsa: masalan 853710 (boshqaruv paneli) — 10% o'rniga 5%, EUR.1 bilan. ⚠️ Ushbu HS6 ichidagi 10 xonali kodlar stavkasi PQ-181 2-ilovadan qayta tekshirilsin.

### 4. Kutubxona `[x]` → `[y]` (p.25 l.30–31) — sanali o'zgarish
- 8539 52 (LED lampa) uchun o'zgarish **yo'q**: 29.01.2025 tahririda LED lampalar 8539 umumiy qatori bo'yicha 15%, 20.05.2025 va 16.02.2026 tahrirlarida 853952 — 15%. Shuning uchun LED misolida "o'zgardi" deb yozib bo'lmaydi.
- Tasdiqlangan haqiqiy misol: **marmar/travertin 2515 11 000 0, 2515 12 000 0** — **20%** (PQ-181 2-ilova, 2515 pozitsiyasi, 20.05.2025 tahriri; 01.06.2025 dan) → **0%** (PQ-58, 11.02.2026; konsolidatsiya tahriri 16.02.2026). Manba: https://lex.uz/docs/3802366 (tahrirlarni ONDATE bilan solishtirish), uzbekcha https://lex.uz/uz/docs/-7533457 .
- Tavsiya: iste'molchi tovarlari demosi uchun mos sanali misol topilmagan bo'lsa — **misolni olib tashlash** yoki marmar misolidan foydalanish. ⚠️ PQ-58 ning kuchga kirish sanasi (16.02.2026 konsolidatsiya sanasidan) — PQ-58 matnidan qayta tekshirilsin.

### 5. `[v2 spec, "Ruxsatnomalar manbalari"]` (p.12 l.54) — ro'yxatlar
| Ro'yxat | Hujjat | Tahrir sanasi | URL | Holat |
|---|---|---|---|---|
| Asl Belgisi (majburiy raqamli markirovka) | VM 737 (20.11.2020) 1-ilova | 23.01.2026 (VM 23); oldingi 22.10.2025 | https://lex.uz/uz/docs/-5115923 | ✅ o'qildi: sigaret/tamaki, alkogol, pivo, maishiy texnika (kodlar ro'yxati, 15.04.2022 dan), dori/tibbiy buyumlar, suv/ichimliklar, mineral o'g'itlar/OHV, elektr akkumulyatorlar 8507 (01.01.2026 dan) |
| Majburiy muvofiqlikni tasdiqlash (sertifikat / deklaratsiya) | VM 43 (30.01.2021), 01.05.2021 dan | oxirgi 09.09.2026; rejalashtirilgan 01.01.2027 | https://lex.uz/docs/5249380 | ⚠️ **UNVERIFIED** — ilova matnini yuklab bo'lmadi; ikkilamchi manbaga ko'ra 4-ilova VM 472 (07.09.2026) tahririda |
| Dronlar (UUA) | VM 658 (15.11.2022) | — | https://www.lex.uz/uz/acts/-6284990 | ✅ (uzcaa rasmiy sahifasi orqali) |
| IMEI | VM 778 (17.09.2019) 14-band | — | https://www.lex.uz/docs/-4517458 | ✅ |
| Kod o'zgarishi (eski → yangi) | VM 349 (04.06.2025) | — | https://lex.uz/en/acts/7558317 | ✅ mavjud |
| Sanitariya-epidemiologik xulosa, fitosanitariya, veterinariya, litsenziyalanadigan tovarlar | — | — | — | ⚠️ **UNVERIFIED** — manba yuklanmagan; "Topilmadi" o'rniga "Tekshirilmadi" ko'rsatilsin |

Muhim: VM 737 da `8539500000` (eski LED lampa kodi) bor — HS2022 8539 52 000 x ga tatbiqi **ochiq**; p.14 dagi "Asl belgisi: talab qilinmaydi" olib tashlansin.

### 6. `[ruxsat turi]` (p.12 l.66) — dron
- VM 658 (15.11.2022): UUA, ularning butlovchi va ehtiyot qismlarini (qaror keltirgan kodlar 8802200001, 8802200002, 8802200008, 8803100000, 8803200000) noqonuniy **olib kirish, sotish, saqlash, foydalanish taqiqlangan**; istisno — nomlangan tashkilotlar; boshqalarga faqat **Vazirlar Mahkamasining alohida qarori** bilan ruxsat; keyin Mininfokom (radioelektron vosita), "O'zaviatsiya" (ro'yxat) va havo hududi ruxsati. O'yinchoq modellarga tegishli emas. Manba: https://www.lex.uz/uz/acts/-6284990 ; https://gov.uz/oz/uzcaa/pages/dronlar-uua .
- Ekran matni: "Tovar taqiqlangan / faqat VM alohida qarori bilan ruxsat (VM 658)" — **qizil "No-go"**.
- ⚠️ UNVERIFIED: HS2022 da dronlar 8806 da — VM 658 kodlarining yangi kodlarga xaritasi; 2026-yilda yuridik shaxslarga ruxsat berish haqidagi xabarlar (faqat OAV) — lex.uz da tasdiqlanmagan. Xavfsizroq yo'l: misolni tasdiqlangan guruhga almashtirish (masalan, mikroto'lqinli pech 8516500000 — Asl Belgisi majburiy, VM 737).

### 7. `[TIF TN ro'yxatidagi matn]` (p.14 l.27) — LED lampa
PQ-181 1-ilova (14.05.2025; 01.06.2025 dan), https://lex.uz/uz/files/7541055.zip :
- Rasmiy matn (kirill, PDF dan aynan):
  - `8539 52 000` — "– – светодиодли лампалар (LED):"
  - `8539 52 000 1` — "– – – таркибида фосфор бўлган композит билан қопланган, подложкада камида 24 та кетма–кет уланган светодиод бўлган светодиод иплари билан" — dona
  - `8539 52 000 2` — "– – – диаметри камида 25 мм бўлган тўғри қувурлар шаклида икки томонлама" — dona
  - `8539 52 000 9` — "– – – бошқалар" — dona
  - Lotin transliteratsiyasi (rasmiy emas, belgi bilan): "svetodiodli lampalar (LED)"; "…9 — boshqalar".
- `8539 52 000 0` **mavjud emas**. Boj: 15% (853952, PQ-181 2-ilova).

### 8. `[asos]` (p.15 l.47) — yig'im
- Asos: **VM 55 (31.01.2025) 1-ilova** ("Bojxona yig'imlari stavkalari"), VM 700 (06.11.2025; 08.02.2026 dan) tahririda — https://lex.uz/docs/-7357270 .
- Bojxona qiymati **10 000 AQSh dollarigacha — 1 BHM**. BHM 01.09.2026 dan **440 000 so'm** (PF-115, 23.06.2026, 3(b)(ii), https://www.lex.uz/uz/docs/-8283656 ) → **440 000 ✅ tasdiqlandi**.
- Dastlabki (kelgunga qadar) deklaratsiyada −20% → **352 000** (PF-250, 17.12.2025, 2(a), 01.03.2026 dan — https://lex.uz/uz/docs/-7934915 ; VM 55 1-ilova izohi).
- **310 000 — hech qaysi rasmiy qiymatga mos emas, olib tashlansin.** 9 500 USD misoli — 1 BHM oralig'ida ✅. ⚠️ Aniq 10 000,00 USD qaysi oraliqqa tushishi — UNVERIFIED (misolda ishlatilmasin).

### Qo'shimcha
- **Aksiz akti:** Soliq kodeksi **289¹** (tamaki), **289²** (alkogol), **289³** (neft mahsulotlari, polietilen granulalar, tabiiy gaz, qadoqlangan shirin ichimliklar, energetik ichimliklar, chipslar); baza — 285, 286-m. https://lex.uz/docs/-4674902 . Dizayndagi tovarlar (LED, telefon, kiyim) — aksizsiz.
- **QQS bazasi:** bojxona qiymati + boj + aksiz (SK 254; BK 322), stavka 12% (SK 258). ✅. ⚠️ BK 300¹ ustamasining bazaga kirishi — UNVERIFIED.
- **Namuna 10% / 15%:** LED lampa (853952) — **15%** (10% emas). Muqobil 9405 42 — **5%**, yoki istisno ro'yxatidagi 10 xonali kodlar uchun **10%, lekin 0,5 USD/kg dan kam emas** (15% emas). Boshqa tasdiqlangan stavkalar: smartfon 851713 — 5%; noutbuk 8471 — 0%; mikroto'lqinli pech 851650 — 10%, kamida 5 USD/dona; futbolka 6109 — 20%, kamida 0,5 USD/dona; kosmetika 3304 — 30%, kamida 0,5 USD/kg; o'yinchoq 9503 — 10%; mebel 9403 — 15%, kamida 0,4 USD/kg (PQ-181 2-ilova, 16.02.2026 tahriri).

---
O'zgarishlar: 18.11.2026 04:30 (UTC+5) — grafa raqamlari tekshirildi (BYD yo'riqnomasi № 2773, 2773-15 / 22.07.2026); bu faylda grafa havolasi yo'q, o'zgartirish kerak emas. Grafa xaritasi uchun: tariff-payments.md §3 8-band.

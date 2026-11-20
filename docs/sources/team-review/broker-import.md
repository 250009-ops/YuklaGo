# YuklaGo — import brokeri ko'zi bilan audit (v1)

**Kim yozdi:** litsenziyali bojxona brokeri roli (15+ yil, import: Xitoy/Turkiya iste'mol tovarlari, elektronika, to'qimachilik, oziq-ovqat).
**Sana:** 18-noyabr 2026, Toshkent vaqti (UTC+5).
**Nima tekshirildi:** `yuklago-spec-v2.md` (§ raqamlari bilan), `design-v0.1/yuklago-web-ui-v0.1.pdf` (28 sahifa; "d-p10" = PDF 10-sahifa = `pg10.txt`), `design-v0.1/design-rationale.md`, jamoa eslatmalari (`deklarant-jarayoni.md`, `global-funksiyalar.md`, `raqobatchilar.md`). Bot fayllar papkasi (`.../attachments/`) mavjud emas edi.
**Spec va dizayn fayllari o'zgartirilmadi.** Bu yuridik xulosa emas.

## 0. Qanday o'qish kerak

**Belgilar:**
- **[Qonun: …]** — men shu audit davomida lex.uz'da ochib, matnini o'qigan manba. Havolalar 18.11.2026 da ishlagan.
- **tajriba (qonun emas)** — broker amaliyotidan olingan bilim. Qonun matni emas, uni rasmiy qoida deb aytmang.
- **tekshirilmagan** — raqam, muddat yoki modda rasmiy matndan tasdiqlanmadi. Mahsulotga ham, pitchga ham shu holicha kiritmang.
- **(spec manbasi)** — spec keltirgan, lekin men bu auditda qayta ochmagan manba.

**To'rtta hukm (har bir vazifaga bittadan):**
- **Covered (Qamrab olingan)** — spec va dizaynda bor va to'g'ri.
- **Partial (Qisman)** — bor, lekin muhim qismi yetishmaydi yoki noto'g'ri.
- **Missing (Yo'q)** — umuman yo'q.
- **Needs a human (Inson kerak)** — qonun yoki amaliyot bo'yicha odam (broker, mijozning o'zi, boshqa organ) bajarishi kerak. Dasturning vazifasi esa faqat tayyorlash, eslatish va tushuntirish.

**Asosiy manbalar (o'zim ochib o'qiganlarim):**
| Qisqa nom | Hujjat | Havola |
|---|---|---|
| BK | Bojxona kodeksi (O'RQ-400), joriy matn | https://lex.uz/docs/-2876354 |
| VM-605 | VM 31.07.2018 dagi 605-son qaror (elektron deklaratsiyalash nizomi). Lex.uz'dagi oxirgi tahriri **21.07.2026** (VM 20.07.2026 dagi 393-son). Spec esa 08.02.2026 tahririni keltiradi | https://lex.uz/uz/docs/-3844549 |
| VM-160 | VM 06.04.2022 dagi 160-son qaror (import bojxona qiymati nizomi) | https://lex.uz/uz/docs/-5941961 |
| VM-55 | VM 31.01.2025 dagi 55-son qaror (bojxona yig'imlari stavkalari), 1-ilova | https://lex.uz/uz/docs/-7357270 |
| VM-630 | VM 04.10.2024 dagi 630-son qaror (VM-605 ga 11-1-band) | https://lex.uz/uz/docs/-7138545 |
| VM-283 | VM 14.05.2020 dagi 283-son qaror (E-kontrakt, tashqi savdo monitoringi) | https://lex.uz/uz/docs/-4812419 |
| MJtK | Ma'muriy javobgarlik to'g'risidagi kodeks | https://lex.uz/uz/docs/-97664 |

Spec keltirgan, lekin men qayta ochmagan manbalar (spec manbasi): PF-5414, PQ-181, PF-115 (1 BHM = 440 000 so'm), Soliq kodeksi 258-modda (QQS 12%), VM-847.

**Dizayn ekranlari xaritasi (d-pNN):** d-p1 dizayn tizimi · d-p4 bosh sahifa (landing) · d-p5 kirish va "Brokerga topshiring" · d-p6 yo'l tanlash va "O'zim topshira olamanmi?" · d-p7 bosh sahifa (yuklar, muddatlar) · d-p8 yangi yuk · d-p9 muddatlar · d-p10–11 kelib tushgan narx, kargo, imtiyoz · d-p12 jo'natishdan oldin (ruxsatnomalar) · d-p13 hujjatlar (OCR) · d-p14 TIF TN kodi · d-p15–16 to'lovlar va qoralama tekshiruvi · d-p17–18 kabinetni to'ldirish (boshlash) · d-p19–22 avtomatlashtirish holatlari (yozish, pauza, ERI navbati, xato) · d-p23 sessiya yakuni · d-p24 topshirilgandan keyin (xabarni tushunish) · d-p25 mahsulotlar kutubxonasi · d-p26 brokerga topshirish · d-p27 sozlamalar (ERI) · d-p28 mobil.

---

## 1. Qisqa xulosa

**Hisob (63 ta vazifa):** Covered **9** · Partial **29** · Missing **16** · Needs a human **9**.

YuklaGo "oddiy yo'l"ning **o'rtasini** yaxshi qamraydi: hujjat o'qish, kod taklifi, to'lov hisobi, qoralama, kabinetni to'ldirish va imzoda to'xtash. Broker ishining **boshi va oxiri** esa deyarli yo'q:
- **boshida:** bojxona qiymatini to'g'ri qurish, kelib chiqish mamlakati, ko'p pozitsiyali invoys, E-arxiv;
- **oxirida:** to'lov oqimi, tuzatishlar, chiqarilgandan keyingi arxiv, 3 yillik audit, shikoyat.

Eng xavfli ikki joy — **bojxona qiymatiga transportni noto'g'ri qo'shish** (d-p10) va BK **300-1/366-moddalardagi qo'shimcha boj**ning hisobga olinmagani. Ikkalasi ham "kelib tushgan narx"ni, ya'ni mahsulotning asosiy va'dasini buzadi.

---

## 2. Vazifalar bo'yicha audit

### A. Mijozni qabul qilish, shartnoma va vakolat

#### A1. Mijozning huquqiy maqomini aniqlash (YuL / YaTT / jismoniy shaxs, STIR, TIF ishtirokchisi)
- **Broker nima qiladi:** kim deklarant bo'la olishini tekshiradi. U kompaniya yoki YaTT bo'lishi, STIRga ega bo'lishi va tashqi savdo shu nomdan bo'lishi kerak.
- **YuklaGo'da:** spec §2, §6 1–2-qadam, Y1, Y2; d-p6 ("Kompaniya yoki YaTT", STIR).
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - O'zini o'zi band qilgan shaxslar holatini alohida ko'rsatish kerak: VM-283 1-band ularni E-kontraktga kiritish majburiyatidan chiqargan. Bu ular uchun import yo'li boshqacha bo'lishi mumkinligini bildiradi (tekshirilmagan).
  - Tadbirkor bo'lmagan jismoniy shaxs tijorat importini qila oladimi — spec buni ham tekshirilmagan deb belgilagan.
  - "TIF ishtirokchilari ro'yxati"da kompaniya bor-yo'qligi so'ralishi kerak (VM-605 2-band ta'rifi).
- **Tipik xatolar (tajriba (qonun emas)):**
  - Yuk bir kompaniya nomiga kelgan, pulni esa boshqa kompaniya yoki shaxsiy karta to'lagan.
  - Direktor almashgan, lekin ERI eski direktor nomida qolgan.
- **Chekka holatlar:** filial yoki doimiy muassasa (BK 274-modda); norezident.
- **Inson kerakmi:** yo'q. Lekin murakkab holatda broker yoki yurist kerak.
- **Qonun:** BK 274-modda (kim deklarant bo'la oladi); VM-283 1-band.

#### A2. Jarayon va rejimni tanlash (shaxsiy posilka / yo'lovchi / tijorat BYD, IM40)
- **Broker nima qiladi:** qaysi deklaratsiya turi va qaysi rejim kerakligini aniqlaydi.
- **YuklaGo'da:** spec §3, Y2; d-p6 (uch yo'l), d-p8, d-p15 (1-grafa "IM 40").
- **Hukm:** Covered (1-bosqich uchun).
- **Nima qo'shish kerak:** kargo bilan kelgan yuk uchun alohida savol: "Deklaratsiya kimning nomida?" (d-p11 da bor). Natijada "deklarant siz emassiz" degan yo'l ham bo'lishi kerak.
- **Tipik xatolar (tajriba (qonun emas)):** tijorat partiyasini "shaxsiy posilka" qilib bo'lib yuborish. Bu BK 23-bobi (notijorat) va 24-bobi (pochta/kuryer) doirasidan chiqadi va MJtK bo'yicha javobgarlik xavfini tug'diradi.
- **Inson kerakmi:** yo'q.
- **Qonun:** BK 25-modda (rejim turlari), 23-bob (155–164-moddalar), 24-bob (165–169-moddalar).

#### A3. Kim imzolaydi: ERI, "deklaratsiyalovchi shaxs", ishonchnoma
- **Broker nima qiladi:**
  - Kim imzolashini aniqlaydi: deklarantning o'zimi yoki shtatdagi mutaxassismi.
  - ERI kimga tegishli ekanini va muddatini tekshiradi.
  - Ishonch bildirilgan shaxs uchun ishonchnoma yoki shartnoma borligini tekshiradi.
- **YuklaGo'da:** Y1; d-p6 ("4 · Kim imzolaydi", "[ERI beruvchi markaz — v2 spec]"), d-p27.
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - Dizayndagi bo'sh joyni to'ldiring: VM-605 26-band bo'yicha ERIni **"Yangi texnologiyalar ilmiy-axborot markazi" AJ** tarqatadi va hisobini yuritadi. Kalit maxsus himoyalangan qurilmada saqlanishi shart.
  - Uch rolni ajrating: "deklaratsiyalovchi shaxs", "ishonch bildirilgan shaxs" va "TIF ishtirokchilari ro'yxati" (VM-605 2-band).
  - Imzolovchi bo'yicha VM-605 28-bandni ko'rsating: kalit egasi ma'lumotlarni o'z imzosi bilan tasdiqlaydi.
  - VM-605 30-band oxiri: deklarant TEDni o'z nomidan topshirsa, u bojxona rasmiylashtiruvi bo'yicha mutaxassisning huquq va majburiyatlariga ega bo'ladi. Buni foydalanuvchiga ochiq aytish kerak.
- **Tipik xatolar (tajriba (qonun emas)):** ERI muddati imzo kuni tugagan bo'ladi; xodim direktorning tokeni bilan imzolaydi.
- **Inson kerakmi:** ha, imzo qismi uchun. Uni faqat kalit egasi qo'yadi.
- **Qonun:** VM-605 2, 26, 28, 30-bandlar; BK 284, 287-moddalar.

#### A4. Broker bilan shartnoma (eskalatsiya qilinganda)
- **Broker nima qiladi:**
  - Shartnoma tuzadi: broker deklarant nomidan va uning topshirig'i bilan ishlaydi.
  - Brokerning javobgarligi shartnoma bilan cheklanmaydi.
  - Broker fuqarolik javobgarligini **BHMning 1000 baravari** miqdorida sug'urtalaydi.
- **YuklaGo'da:** Y18, spec §9.2; d-p26 (toplam, 7 kunlik havola, "brokerni o'zi tanlamaydi").
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - Foydalanuvchiga 3 ta tekshiruv bering: broker xabardor qilish reyestridami (license.gov.uz — spec manbasi), shartnoma bormi, sug'urta polisi bormi.
  - Toplamga "imzolanmagan qoralama, kod — taklif" degan rasmiy belgi qo'ying.
- **Tipik xatolar (tajriba (qonun emas)):** og'zaki kelishuv bilan ishlash; brokerga ERI tokenini berib qo'yish.
- **Inson kerakmi:** ha. Broker va mijoz shartnomani o'zlari imzolaydi.
- **Qonun:** BK 277, 281, 282-moddalar. **Eslatma:** joriy matnda 278–280, 283, 285-moddalar mazmundagi ro'yxatda yo'q; 283 va 285 kuchini yo'qotgan. Spec "Arts. 277–281" deb yozgan. "1000 BHM xavfsizlik" deb yozilgan joy BK 282-moddada **sug'urta** deb berilgan; VM-847 matni tekshirilmagan.

#### A5. Mijozning bojxona tarixi va qarzdorligini ko'rish
- **Broker nima qiladi:** shaxsiy g'azna hisobvarag'idagi qoldiqni, to'lanmagan qarz yoki penyani, oldingi BYDlarni va avvalgi muammolarni so'raydi.
- **YuklaGo'da:** yo'q (Y23 faqat eski fayllarni audit qiladi).
- **Hukm:** Missing.
- **Nima qo'shish kerak:** onboarding'da "kabinetingizda qarzdorlik yoki ochiq talabnoma bormi?" degan savol. Qarzdorlik nima ekanini tushuntiring (BK 347–349-moddalar, penya).
- **Tipik xatolar (tajriba (qonun emas)):** eski penya tufayli yangi rasmiylashtiruv to'xtab qoladi (tekshirilmagan — bu qanday mexanizm bilan sodir bo'lishi).
- **Inson kerakmi:** yo'q.
- **Qonun:** BK 347, 348, 349-moddalar.

### B. Hujjatlarni yig'ish va tekshirish

#### B1. Tashqi savdo shartnomasi va E-kontrakt
- **Broker nima qiladi:**
  - Shartnoma rekvizitlarini tekshiradi.
  - E-kontraktdagi ID raqamini tekshiradi.
  - Qo'shimcha kelishuvlar ham tizimga kiritilganini tekshiradi.
  - To'lovdan keyingi 180 kunlik muddatni kuzatadi.
- **YuklaGo'da:** Y6, spec §6 6-qadam, §9.7 ("E-kontrakt majburiyligi tekshirilmagan"); d-p9, d-p10 ("Shartnoma va bank ✓ E-kontrakt").
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - Spec'dagi noaniqlikni yoping: VM-283 1-band bo'yicha xo'jalik yurituvchi subyektlar (o'zini o'zi band qilganlardan tashqari) kontrakt, dalolatnoma va invoys ma'lumotlarini ERI bilan "E-kontrakt"ga **kiritadi**.
  - VM-283 5-band: qo'shimchalar ham xuddi shu tartibda kiritiladi. Hamkor davlat o'zgarsa, deklarant **10 ish kuni** ichida BYDga o'zgartirish so'rab murojaat qilishi shart.
  - Nizomning 23-bandi: import kontrakti bo'yicha to'lovdan keyin tovar **180 kun** ichida rasmiylashtirilishi kerak. Buni L3 dagi soatga ulang.
  - E-kontrakt IDsiz BYD qabul qilinmasligi VM-283 matnidan topilmadi — **tekshirilmagan**.
- **Tipik xatolar (tajriba (qonun emas)):**
  - Invoysdagi summa yoki valyuta E-kontraktdagidan farq qiladi.
  - Xitoy sotuvchisi nomi E-kontraktda boshqacha yozilgan (d-p13 dagi "Guang Ming" holatiga o'xshash).
- **Chekka holatlar:** shartnomasiz, faqat invoys bilan import; birjada tuzilgan shartnomalar.
- **Inson kerakmi:** yo'q. Kiritishni foydalanuvchi o'z ERIsi bilan qiladi.
- **Qonun:** VM-283 1, 5-bandlar, Nizom 23-band.

#### B2. Invoysni tekshirish (VM-605 1a-ilovadagi 12 ta majburiy maydon)
- **Broker nima qiladi:** majburiy maydonlarni tekshiradi:
  - sotuvchi va xaridor (nomi, manzili, STIR, telefon);
  - TIF TN kodi (kamida 6 raqam);
  - kelib chiqish mamlakati, tovar nomi, markasi va brendi;
  - faktura qiymati, brutto va netto vazn, joylar soni;
  - qo'shimcha o'lchov birligi, Incoterms, shartnoma raqami va sanasi.
- **YuklaGo'da:** Y9, Y13, spec §6 11-qadam, §8.3 ("missing Annex 1a fields"); d-p13, d-p15.
- **Hukm:** Covered.
- **Nima qo'shish kerak:**
  - 12 ta maydonni nomma-nom chek-list qiling (d-p13 da 11 ta o'qilgan maydon ko'rinadi).
  - 1a-ilovada "Inkoterms — 2010" yozilgan. 2020 tahriri bilan nima qilish kerakligi ochiq savol (spec §9.7).
- **Tipik xatolar (tajriba (qonun emas)):** proforma invoys yakuniy invoys o'rniga beriladi; invoysda HS kodi yoki kelib chiqish mamlakati yo'q; netto vazn qo'lda yozilgan (d-p13 aynan shu holat).
- **Inson kerakmi:** yo'q.
- **Qonun:** VM-605 1a-ilova (12 band).

#### B3. Transport hujjati (CMR / AWB / konosament / temir yo'l yuk xati)
- **Broker nima qiladi:**
  - Transport turi va hujjatini tekshiradi.
  - Kargo yukida "uy" va "master" hujjatni ajratadi.
  - Joylar soni va brutto vaznni solishtiradi.
- **YuklaGo'da:** spec §6 9-qadam (faqat CMR misol); d-p13 (CMR).
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - AWB, dengiz konosamenti va temir yo'l yuk xati uchun maydon xaritasi.
  - Konsolidatsiya qilingan yuk uchun: bitta transport hujjatida bir nechta oluvchi bo'lishi.
  - Multimodal yo'l (masalan, dengiz + temir yo'l + avto).
- **Tipik xatolar (tajriba (qonun emas)):** CMRdagi joylar soni packing listdan farq qiladi; kargo yukida transport hujjati oluvchi nomida emas.
- **Inson kerakmi:** yo'q.
- **Qonun:** BK 9-modda (kuzatuv hujjatlari), 18-modda (kirishda taqdim etiladigan hujjatlar).

#### B4. Packing list
- **YuklaGo'da:** spec §6 9-qadam (to'g'ri: VM-605 11-1-band bo'yicha majburiy ro'yxatda yo'q, lekin post so'rashi mumkin); d-p13 da solishtiriladi.
- **Hukm:** Covered.
- **Qonun:** VM-605 11-1-band (VM-630 bilan kiritilgan).

#### B5. Kelib chiqish mamlakati va sertifikati (ST-1, Form A va boshqalar)
- **Broker nima qiladi:**
  - Ishlab chiqarilgan mamlakatni aniqlaydi (bu jo'natilgan mamlakat bilan bir xil bo'lmasligi mumkin).
  - Preferensiya uchun sertifikat kerakmi, tekshiradi.
  - Sertifikat bo'lmasa nima bo'lishini mijozga tushuntiradi.
- **YuklaGo'da:** Y5, spec §1, §11; d-p10–11 ("Imtiyozli stavka", "kelib chiqishi Xitoy").
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:** **katta bo'shliq.**
  - BK **300-1-modda** (28.02.2026 dan kuchda): eng ko'p qulaylik rejimi (MFN) qo'llanilmaydigan mamlakatda ishlab chiqarilgan yoki **kelib chiqishi aniqlanmagan** tovarga qo'shimcha boj undiriladi. Miqdori asosiy advalor stavkaga bog'liq:
    - 10% gacha — +5%;
    - 10–20% — +10%;
    - 20–30% — +15%;
    - 30% va undan yuqori — +20%.
  - BK **366-modda**: sertifikat bo'lmasa yoki unga shubha bo'lsa, shu qo'shimcha boj qo'llaniladi (365-moddadagi holatdan tashqari).
  - Lekin to'lovli rejimga joylashtirilgandan keyin **1 yil** ichida to'g'ri sertifikat berilsa, MFN yoki erkin savdo rejimi tiklanadi va ortiqcha to'lov qaytariladi (BK 49-bob).
  - Landed cost dvigateliga "kelib chiqish isboti" tugunini qo'shing. Qaysi mamlakatlar MFN ro'yxatida — **tekshirilmagan**, rasmiy ro'yxat kerak.
  - BK 364-modda sertifikat majburiy bo'lgan holatlarni sanaydi: preferensiya, kvota, ma'lumot yo'q yoki shubha bor.
  - VM-160 22-band: sertifikat yo'qligi 1-usulni qo'llashga to'siq emas.
- **Tipik xatolar (tajriba (qonun emas)):** "Made in China" yozuvi bor, lekin hujjatlarda kelib chiqish ko'rsatilmagan; Turkiyadan jo'natilgan Xitoy tovari "Turkiya" deb yozilgan.
- **Chekka holatlar:** aralash partiya (bir invoysda turli mamlakat tovarlari); qayta eksport qilingan tovar.
- **Inson kerakmi:** yo'q. Shubha bo'lsa broker kerak.
- **Qonun:** BK 300-1, 358–366-moddalar; VM-605 11-1-band; VM-160 22-band.

#### B6. Muvofiqlik sertifikati / texnik reglament
- **Broker nima qiladi:**
  - Shu kod uchun majburiy sertifikat kerakmi, aniqlaydi.
  - Sertifikat model, brend va ishlab chiqaruvchiga mosmi, muddati o'tmaganmi, tekshiradi.
  - Sertifikat "Yagona darcha"ga kiritilganini tekshiradi.
- **YuklaGo'da:** Y7; d-p12 (sertifikat yuklangan, muddati), d-p7 (YG-0415 "sertifikat yo'q"), dizaynda "[organ va tartib — v2 spec]".
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - Rasmiy talablar ro'yxati manbasi va uning yangilanish sanasini ko'rsating.
  - Sertifikatdagi model, brend va ishlab chiqaruvchini invoys bilan avtomatik solishtiring.
  - Sertifikat qog'ozda bo'lsa ham, Yagona darchada bo'lmasa TED qabul qilinmaydi (F3 ga qarang).
- **Tipik xatolar (tajriba (qonun emas)):** sertifikat boshqa model yoki boshqa ishlab chiqaruvchiga berilgan; seriya sertifikati boshqa partiyaga ishlatiladi.
- **Inson kerakmi:** sertifikatlash organi bilan ishlashni mijozning o'zi qiladi.
- **Qonun:** BK 271-modda (ruxsatnomalar chiqarish sharti), 57-modda (bojxona ruxsat hujjatlarini axborot tizimida o'zi tekshiradi); VM-605 15-band.

#### B7. Sanitariya, fitosanitariya va veterinariya nazorati (oziq-ovqat, o'simlik, hayvon mahsulotlari)
- **Broker nima qiladi:** chegarada yoki postda boshqa organ nazoratini tashkil qiladi, namuna olish va xulosa kutish jarayonini boshqaradi.
- **YuklaGo'da:** spec §3 (3-bosqich, "to'xta va eskalatsiya qil"), Y7, Y18.
- **Hukm:** Needs a human.
- **Nima qo'shish kerak:** oziq-ovqat yoki o'simlik kodini tanlaganda "bu yo'lni 1-bosqichda qo'llab-quvvatlamaymiz" degan aniq yo'naltirish. Muddatga ta'sirini ham ko'rsating: tez buziladigan tovar vaqtincha saqlashda ko'pi bilan **10 kun** turadi (BK 85-modda).
- **Tipik xatolar (tajriba (qonun emas)):** fitosanitariya sertifikati jo'natuvchi davlatdan olinmagan; harorat rejimi buzilgan.
- **Inson kerakmi:** ha. Boshqa organ inspektori va mijoz yoki broker joyida bo'lishi kerak.
- **Qonun:** BK 248-modda 3-qism (rasmiylashtiruv vet/fito va boshqa nazoratdan keyin tugaydi), 276-modda (deklarant shu hujjatlarni beradi).

#### B8. Litsenziya, ruxsatnoma, kvota, ikki xil maqsadli tovar
- **YuklaGo'da:** Y7, Y18, spec §3; d-p7 va d-p12 (YG-0409 dron — "imkoniyatdan tashqarida").
- **Hukm:** Needs a human.
- **Nima qo'shish kerak:** ruxsat turini ko'rsating (dizayndagi "[ruxsat turi — v2 spec]" bo'sh joyi). Rasmiy manba sifatida license.gov.uz va Yagona darcha ro'yxatlari (spec manbasi).
- **Tipik xatolar (tajriba (qonun emas)):** Wi-Fi yoki Bluetooth modulli tovar (radioelektron vosita) oddiy elektronika deb o'ylanadi; dron, rasiya va shifrlash qurilmalari.
- **Inson kerakmi:** ha. Ruxsat beruvchi organ va broker.
- **Qonun:** BK 23, 24-moddalar (cheklov va taqiqlar), 271-modda.

#### B9. Majburiy raqamli markirovka (Asl Belgisi)
- **YuklaGo'da:** Y7; d-p12 ("Bu tovar guruhi uchun talab qilinmaydi").
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:** rasmiy tovar guruhlari ro'yxati yuklanmagan (spec §8.5 ham shuni aytadi). Kodlarni qachon buyurtma qilish va qayerda yopishtirish (chet elda yoki omborda) — **tekshirilmagan**, operator manbasidan olish kerak.
- **Tipik xatolar (tajriba (qonun emas)):** markirovka kodlari tovar chegaraga kelganda buyurtma qilinadi.
- **Inson kerakmi:** yo'q.
- **Qonun:** BK 194-modda (tamg'alanishni tekshirish); markirovka akti — tekshirilmagan.

#### B10. Hujjatlarni o'zaro solishtirish va tarjima
- **YuklaGo'da:** Y9, Y13, spec §8.3; d-p13 (soni, brutto, sotuvchi nomi), d-p15 (to'siq va ogohlantirish).
- **Hukm:** Covered.
- **Qo'shimcha:** BK 276-modda bo'yicha deklarant tovar hujjatlarga mos kelmasligini aniqlasa, bojxonani xabardor qilishi shart (G5 ga qarang).

### C. TIF TN (HS) bo'yicha tasniflash

#### C1. Kodni tanlash (asosiy talqin qoidalari, izohlar, aniqlovchi savollar)
- **Broker nima qiladi:**
  - Tovar nima ekanini aniqlaydi: material, funksiya, to'plam yoki alohida.
  - Talqin qoidalari va tushuntirishlar bo'yicha 10 xonali kodni tanlaydi.
  - Shu kodga bog'liq ruxsatnoma va stavkani tekshiradi.
- **YuklaGo'da:** Y10, spec §6 10-qadam, §8.4 (LLM faqat rasmiy ro'yxatdagi nomzodlarni tartiblaydi); d-p14 (sabab, muqobillar, "chiroq korpusi bilan sotiladimi?" savoli, ro'yxatda yo'q kodni rad etish).
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - Har bir taklifga talqin qoidasi va izoh manbasini yozing.
  - Ishonch past bo'lsa, tarif mutaxassisi ko'radigan navbat.
  - BK 374-moddadagi dastlabki qarorlar reyestridan o'xshash qarorni qidirish.
  - Kod faqat stavkaga emas, qo'shimcha o'lchov birligiga ham ta'sir qiladi (1a-ilova 10-maydon).
- **Tipik xatolar (tajriba (qonun emas)):**
  - Boji past kodni "tanlash".
  - To'plamni (lampochka + chiroq) bo'lib yozish.
  - Ehtiyot qism va tayyor mahsulotni adashtirish.
  - Kiyimda tola tarkibi noma'lum bo'ladi (to'qimachilikda tarkib kodni belgilaydi).
- **Chekka holatlar:** aqlli (Wi-Fi) qurilmalar; to'plamlar; yig'ilmagan holda kelgan tovar.
- **Inson kerakmi:** ishonch past bo'lsa — ha (tarif mutaxassisi).
- **Qonun:** BK 367–369-moddalar; spec bo'yicha PQ-181 (spec manbasi).

#### C2. Ko'p tovarli invoysni BYD pozitsiyalariga ajratish
- **Broker nima qiladi:**
  - 1688 dan 30–200 qatorli invoys keladi. Broker uni kodlar bo'yicha guruhlaydi.
  - Har bir pozitsiyaga vazn, qiymat va transportni taqsimlaydi.
  - Har pozitsiyaga ruxsatnomani bog'laydi.
- **YuklaGo'da:** yo'q. Dizaynda faqat bitta tovar (LED lampochka, 48 maydon).
- **Hukm:** Missing.
- **Nima qo'shish kerak:**
  - "Pozitsiyalar" ekrani: qatorlarni kod bo'yicha birlashtirish va netto vaznni taqsimlash.
  - Transport va sug'urtani pozitsiyalarga bo'lish qoidasi. Qaysi asosda (vazn yoki qiymat) — **tekshirilmagan**, mutaxassis aniqlasin.
- **Tipik xatolar (tajriba (qonun emas)):** hamma narsani bitta "aralash tovar" kodiga yozish; netto vaznni taxminan bo'lish.
- **Inson kerakmi:** murakkab partiyada — ha.
- **Qonun:** BK 258-modda (BYD), 369-modda.

#### C3. Dastlabki qaror (classification ruling)
- **YuklaGo'da:** Y10 ("dastlabki qaror yo'li, BHMning 75%"); d-p14 ("broker bilan maslahatlashaman").
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - So'rov tayyorlash ustasi (BK 371-modda) va namuna yoki rasm to'plami.
  - Qaror **1 yil** amal qiladi (BK 372-modda). Mahsulot kutubxonasida qaror raqami va muddat soatini saqlang.
  - Qaror bojxona organlari uchun majburiy (BK 370-modda).
  - Fakt: yig'im BHMning 75%i (VM-55, 1-ilova 6-band). Qaror bekor qilinsa yoki o'zgartirilsa, yig'im qaytarilmaydi (VM-55, 1-ilova izohi).
  - Qaror qancha vaqtda chiqishi — tekshirilmagan.
- **Inson kerakmi:** so'rovni mijoz o'zi topshiradi; ekspertiza kerak bo'lishi mumkin (BK 215-modda).
- **Qonun:** BK 370–374-moddalar, 215-modda; VM-55.

### D. Bojxona qiymatini aniqlash

#### D1. Usulni tanlash (6 usul) va 1-usulni qo'llab bo'lmaydigan holatlar
- **Broker nima qiladi:**
  - 1-usul (bitim qiymati) qo'llanishi mumkinmi, tekshiradi. U o'zaro bog'liq shaxslar, cheklovlar, qiymat asosi yo'q bitim (bepul namuna, barter) yoki tasdiqlanmagan ma'lumot bo'lsa qo'llanmaydi.
  - Qo'llab bo'lmasa, usullarni ketma-ket ko'rib chiqadi.
- **YuklaGo'da:** spec §4, §8.3 ("method 1 as default").
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - 1-usulga to'siqlar bo'yicha 6–7 savollik test (BK 306–308-moddalar).
  - Test natijasi "1-usul mumkin emas" bo'lsa, avtomatik **eskalatsiya**.
  - 6 usul ro'yxati: VM-160 6-band; 1-usul asosiy usul — 7-band.
- **Tipik xatolar (tajriba (qonun emas)):** bepul namuna yoki "gift" deb yozilgan tijorat tovari; yetkazib beruvchi va xaridor bir egaga tegishli.
- **Inson kerakmi:** 1-usul bo'lmasa — ha.
- **Qonun:** BK 302–313-moddalar; VM-160 6–12-bandlar.

#### D2. Bitim narxiga qo'shiladigan xarajatlar (BK 304-modda)
- **Broker nima qiladi:** narxda bo'lmasa, quyidagilarni qo'shadi:
  - tovarni bojxona hududiga **olib kiriladigan joygacha** bo'lgan transport, yuklash va tushirish, sug'urta;
  - vositachilik va brokerlik haqi (xarid vositachiligidan tashqari);
  - idish va o'rov;
  - xaridor bepul bergan materiallar, qoliplar, dizayn (assist);
  - litsenziya to'lovlari (royalti);
  - qayta sotishdan sotuvchiga tegadigan ulush.
- **YuklaGo'da:** spec §4 va §8.3 (faqat transport va sug'urta); d-p10 va d-p15 ("Bojxona qiymatiga transport kiradi: 6 200 000 so'm", sug'urta qatori yo'q).
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - Sug'urta qatorini qo'shing (bo'lmasa "yo'q" deb belgilansin).
  - Royalti, assist, o'rov va vositachilik bo'yicha "ha / yo'q" savollar.
  - Har bir qo'shimchaga hujjat manbasi.
- **Tipik xatolar (tajriba (qonun emas)):** brend uchun royalti alohida to'lanadi va yashiriladi; qolip yoki dizayn uchun alohida to'lov qilingan.
- **Inson kerakmi:** yo'q (oddiy holatda).
- **Qonun:** BK 304-modda; VM-160 25-band.

#### D3. Bitim narxidan chiqariladigan xarajatlar (BK 305-modda) — chegaradan keyingi transport
- **Broker nima qiladi:** quyidagilar narxdan **ajratib ko'rsatilgan** bo'lsa, ularni chiqaradi:
  - tovar bojxona hududiga kirgandan **keyingi** transport;
  - kirgandan keyingi montaj va sozlash;
  - shartnoma bo'yicha sotuvchi to'laydigan O'zbekistondagi bojxona to'lovlari (DDP).
- **YuklaGo'da:** yo'q. d-p10 da **"Transport Shenzhen → Toshkent ≈ 6 200 000"** to'liq bojxona qiymatiga qo'shilgan.
- **Hukm:** Missing.
- **Nima qo'shish kerak:**
  - Transportni ikki qismga bo'ling: "chegaradagi kirish joyigacha" va "kirishdan keyin".
  - Ekspeditordan shu bo'linish bilan hisob-faktura so'rash shabloni.
  - Bo'linish hujjatda bo'lmasa — **tajriba (qonun emas):** amalda bojxona ko'pincha to'liq summani qo'shadi; buni mijozga ochiq ayting.
- **Inson kerakmi:** yo'q.
- **Qonun:** BK 305-modda; VM-160 26-band.

#### D4. Incoterms bo'yicha qiymat tuzilishi (EXW / FOB / CFR / CIF / CPT / DAP / DDP)
- **YuklaGo'da:** d-p10, d-p13, d-p15 da FOB Shenzhen misoli.
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:** har bir atama uchun qaysi xarajat narxda bor, qaysi biri qo'shiladi yoki chiqariladi — shuni ko'rsatadigan jadval (D2 va D3 qoidalari bilan). DAP Toshkent va DDP alohida ogohlantirish oladi. EXW bo'lsa, Xitoy ichidagi transport ham qo'shiladi (BK 304-modda "a" bandi).
- **Tipik xatolar (tajriba (qonun emas)):** invoysda CIF, haqiqiy to'lov esa FOB; Incoterms umuman yozilmagan.
- **Qonun:** BK 304, 305-moddalar; VM-605 1a-ilova 11-maydon.

#### D5. Bojxona qiymati deklaratsiyasi (BQD)
- **Broker nima qiladi:** BYD bilan birga BQD shaklini to'ldiradi: usul, qo'shimchalar, chegirmalar, tasdiqlovchi hujjatlar.
- **YuklaGo'da:** yo'q. Spec va dizaynda BQD tilga olinmagan; qoralama "48 maydon" (d-p15).
- **Hukm:** Missing.
- **Nima qo'shish kerak:** BQD qoralamasi. Uning maydonlari Bojxona qo'mitasining BQD to'ldirish yo'riqnomasidan olinsin. Yo'riqnoma BK 276-moddaga LexUZ sharhida keltirilgan: DBQ 08.02.2017 dagi 01-02/8-4-son, ro'yxat raqami 2868. Uning joriy tahriri — **tekshirilmagan**.
- **Inson kerakmi:** yo'q.
- **Qonun:** BK 318-modda (qiymatni ma'lum qilish), 276-modda 2-qism; VM-160 3-band.

#### D6. Valyuta kursi va stavka sanasi
- **Broker nima qiladi:** kurs va stavkani **deklaratsiya qabul qilingan kun** bo'yicha oladi.
- **YuklaGo'da:** spec §8.3 ("dated Central Bank rate"); d-p10 va d-p11 (kurs 01.10.2026).
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - Taxminda ishlatilgan kurs sanasini ko'rsating. Topshirish kuni hisobni avtomatik qayta hisoblang.
  - Rasmiy stavkalar ham shu kun bo'yicha qo'llanadi. Saqlangan hisobga "eskirgan" belgisi qo'ying.
- **Qonun:** BK 324-modda (stavka qabul kuni amaldagi), 326-modda (kurs qabul kuni).

#### D7. Qiymat nazorati: qo'shimcha hujjat, tuzatish, shartli chiqarish
- **Broker nima qiladi:**
  - Bojxona qiymatga rozi bo'lmasa, qo'shimcha dalil beradi: bank to'lovi, prays-list, eksport deklaratsiyasi, yozishmalar.
  - Kerak bo'lsa shartli chiqarishni so'raydi. Bunda bojxona 3 ish kuni ichida shartli qiymat va ta'minot miqdorini xabar qiladi; ta'minot 60 kun amal qiladi.
- **YuklaGo'da:** Y13 (bozor narxi bazasi yo'q — to'g'ri), Y18 ("valuation looks disputed" → eskalatsiya); d-p24 (faqat xabarni tushuntirish).
- **Hukm:** Needs a human.
- **Nima qo'shish kerak:**
  - "Qiymat dalillari" chek-listi va shablon xat.
  - Bojxona qiymatni tuzatsa, to'lov qanday o'zgarishini ko'rsatadigan ekran.
  - Shartli chiqarish muddatlari soati.
- **Tipik xatolar (tajriba (qonun emas)):** past invoys qiymati; to'lov bir necha qismda, uchinchi shaxs orqali qilingan.
- **Inson kerakmi:** ha. Bojxona bilan muloqot va dalillarni himoya qilish uchun broker yoki mijozning o'zi kerak.
- **Qonun:** BK 319, 320, 321-moddalar.

### E. To'lovlar

#### E1. Bojxona boji (advalor, spetsifik, kombinatsiyalangan, qo'shimcha boj)
- **YuklaGo'da:** Y11, spec §4, §8.3; d-p10, d-p15 ("10% Rasmiy · 01.11.2026").
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - Spetsifik (kg, dona yoki litr uchun) va kombinatsiyalangan ("…% lekin kamida …") stavkalarni qo'llab-quvvatlang.
  - BK 300-1-moddadagi qo'shimcha bojni qo'shing (B5).
  - Tarif kvotalari (BK 292-modda).
- **Qonun:** BK 289–293-moddalar, 300-1-modda.

#### E2. QQS
- **YuklaGo'da:** spec §4, Y11 ("12% × (qiymat + boj + aksiz)"); d-p10, d-p15.
- **Hukm:** Covered.
- **Izoh:** d-p10 dagi formula yorlig'i "(bojxona qiymati + boj) × 12%" — aksizni ham yozing. Imtiyozlar ro'yxati alohida yuritilishi kerak (spec §8.5). Stavka (spec manbasi): Soliq kodeksi 258-modda — bu auditda qayta ochilmadi.

#### E3. Aksiz
- **YuklaGo'da:** spec §8.5 ("akt nomlanmagan"); d-p15 ("Stavka topilmadi — taxmin qilmaymiz").
- **Hukm:** Partial.
- **Nima qo'shish kerak:** tarif mutaxassisi joriy aktni nomlasin. Aksiz markasi yoki markirovka bilan bog'liqlikni ham ko'rsating.

#### E4. Bojxona yig'imlari (VM-55) — to'liq ro'yxat
- **Broker nima qiladi:** faqat rasmiylashtirish yig'imini emas, boshqalarini ham hisoblaydi.
- **YuklaGo'da:** spec §4, §8.5 (faqat rasmiylashtirish yig'imi bandlari); d-p10 va d-p15 ("Rasmiylashtirish yig'imi … 310 000").
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak (VM-55, 1-ilova bo'yicha, lex.uz'dan o'qilgan):**
  - **Dastlabki deklaratsiyada yig'imdan 20% chegirma** bor (1-ilova "*" izohi). Spec §1, §8.5 va §11 buni "aytmang" deydi. Joriy rasmiy matn buni qo'llab-quvvatlaydi, shuning uchun spec'ni yangilash kerak. Dastlabki, vaqtinchalik, to'liq bo'lmagan va davriy deklaratsiyada yig'im bir marta olinadi.
  - Deklarant murojaati bilan BYDga o'zgartirish kiritish — BHMning 25%i (2-band).
  - Ish vaqtidan tashqari, dam olish va bayram kunlari rasmiylashtirish — BHMning 25%i. Avtomatik rasmiylashtirilgan BYD bundan mustasno (3-band "a").
  - Xodim ishtirokidagi ko'rik yoki yuk operatsiyasi (3-band "b"): ish vaqtida BHMning 25%i, ish vaqtidan tashqari BHMning 2 baravari. Bir soatdan kam vaqt ham to'liq soat hisoblanadi (izoh).
  - Egasi bojxona bo'lgan omborda saqlash: dastlabki 10 sutkada 1 tonna (brutto) uchun har sutka BHMning 3%i, keyin 4%i (4-band).
  - Tasdiq: rasmiylashtirish yig'imi bandlari — 10 000 $ gacha BHMning 1 baravari, 10–20 ming $ 1,5 baravar va hokazo.
  - Dizayndagi namunaviy "310 000" hech bir bandga mos kelmaydi (1 BHM = 440 000 — spec manbasi). Bu layout namunasi bo'lsa ham, demo oldidan tuzating.
  - Chegara qiymatlarda (masalan, aynan 10 000 $) yaxlitlash — tekshirilmagan.
- **Inson kerakmi:** yo'q.
- **Qonun:** VM-55, 1-ilova (VM-700 va VM-393 tahririda).

#### E5. To'lash: shaxsiy g'azna hisobvarag'i, avans, to'lov ko'rinmasligi
- **Broker nima qiladi:**
  - Mijozga to'lov rekvizitini beradi.
  - Avansni oldindan o'tkazishni maslahat beradi.
  - To'lov tizimda ko'ringanini tekshiradi.
  - Ortib qolgan avansni qaytarishni so'raydi.
- **YuklaGo'da:** yo'q (spec §4 faqat "after … payment" deydi).
- **Hukm:** Missing.
- **Nima qo'shish kerak:**
  - "To'lov" qadami: qancha to'lanishi, qachon to'lanishi va qayerga to'lanishi (rekvizitlar faqat rasmiy manbadan).
  - "Avansim yetadimi?" tekshiruvi.
  - Qaytarish arizasi uchun eslatma (BK 335-modda): dastlabki pul mablag'lari oxirgi foydalanilgan kundan keyin **3 yil** ichida qaytarib so'ralishi mumkin.
  - To'lovlar BYD qabul qilinguncha yoki qabul bilan bir vaqtda to'lanadi (BK 327-modda).
- **Tipik xatolar (tajriba (qonun emas)):** to'lov boshqa STIR nomidan qilinadi; to'lov kuni bank kech o'tkazadi.
- **Inson kerakmi:** to'lovni mijozning buxgalteri qiladi.
- **Qonun:** BK 327, 328, 334, 335, 340-moddalar.

#### E6. Kechiktirish, bo'lib to'lash va ta'minot
- **YuklaGo'da:** yo'q.
- **Hukm:** Missing.
- **Nima qo'shish kerak:**
  - Hozircha faqat tushuntirish va eskalatsiya.
  - BK 329-modda: ta'minot sharti bilan beriladi. 3 yildan ortiq importchilar uchun alohida tartib bor: oxirgi 3 yil to'lovlarining 50% igacha, 6 oyga, ta'minotsiz.
  - Ta'minot usullari: BK 339–346-moddalar (garov, bank kafolati, sug'urta, kafillik, depozit, bosh ta'minot).
- **Inson kerakmi:** ha (bank, broker).
- **Qonun:** BK 329–333, 336–346-moddalar.

#### E7. Imtiyozlar va tarif preferensiyalari
- **YuklaGo'da:** Y5; d-p11 ("faqat tovaringiz allaqachon mos keladigan imtiyoz").
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - ST-1 dan tashqari tovar yoki maqsadga qarab beriladigan imtiyozlar (investitsiya loyihasi, texnologik uskuna va h.k.). Ular qaysi aktlarda — **tekshirilmagan**.
  - Har bir imtiyozga "shartli chiqarish" holatini va uning 3 yillik foydalanish cheklovini ko'rsating (BK 22-modda).
- **Qonun:** BK 296–300-moddalar, 22-modda.

#### E8. Ortiqcha to'langan summani qaytarish
- **YuklaGo'da:** yo'q (Y23 summa va'da qilmaydi — to'g'ri).
- **Hukm:** Missing.
- **Nima qo'shish kerak:** qaytarish holatlarini aniqlash, ariza shabloni va **3 yillik** muddat soati (BK 353-modda). Holatlar: stavka o'zgargan, imtiyoz tiklangan, hisoblash tartibi buzilgan, qiymat tuzatilgan (BK 354-modda). Arizaga dalil hujjat ilova qilinadi (BK 355-modda).
- **Inson kerakmi:** arizani mijoz yoki broker topshiradi.
- **Qonun:** BK 353–357-moddalar.

### F. Dastlabki deklaratsiya va elektron topshirish

#### F1. Dastlabki deklaratsiya (tovar kelmasdan oldin)
- **Broker nima qiladi:** tez chiqarish uchun tovar yo'lda bo'lganda BYD beradi.
- **YuklaGo'da:** spec §6 8-qadam (faqat 30 kunlik soat), Y8.
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - "Dastlabki deklaratsiya" yo'lini tanlash imkoniyati.
  - Foydasini ko'rsating: 20% yig'im chegirmasi (E4) va kelganda tezroq ishlash.
  - Xavfini ko'rsating: qabul qilingandan keyin 30 kalendar kun ichida tovar taqdim etilmasa, deklaratsiya berilmagan deb hisoblanadi (BK 262-modda 4-qism).
  - Kuzatuv hujjatlarining deklarant tasdiqlagan nusxalari ilova qilinadi; tovar kelgach asl nusxa bilan solishtiriladi (262-modda 2-qism).
- **Qonun:** BK 262-modda; VM-55 1-ilova izohi.

#### F2. TEDni to'ldirish (grafalar) — 1-bosqich import
- **YuklaGo'da:** Y12, Y14–Y17, spec §8.2; d-p15 (48 maydon, manbasi bilan), d-p17–d-p22.
- **Hukm:** Covered (mashq portalida; haqiqiy kabinet yuridik savolga bog'liq — spec §9.1).
- **Qo'shimcha:** VM-605 14-band (21.07.2026 tahriri) "us-uz.gov.uz" axborot tizimini Yagona tizim bilan birga tilga oladi. Maydonlar xaritasi qaysi tizim uchun qilinishini aniqlang (ochiq savol).
- **Qonun:** VM-605 13, 14, 15-bandlar.

#### F3. "Yagona darcha"dagi ruxsatnomalarni tekshirish
- **YuklaGo'da:** Y7, spec §4; d-p12 ("'Yagona darcha' orqali ruxsatnoma — topilmadi").
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:** YuklaGo Yagona darchani o'qiy olmaydi. Foydalanuvchiga "kabinetda shu raqam ko'rinyaptimi?" deb tasdiqlatish qadami kerak. Qoidaning o'zi: vakolatli organ hujjatni kiritmagan bo'lsa, tizim TEDni **qabul qilmaydi** (VM-605 15-band). Bojxona ham ruxsatnoma borligini o'zi tekshiradi (BK 57-modda).
- **Qonun:** VM-605 15-band; BK 57-modda.

#### F4. "E-arxiv"ga hujjatlarni yuklash va TEDda ularning raqamini ko'rsatish
- **Broker nima qiladi:** TIF ishtirokchisi kabinetidagi "E-arxiv" xizmatiga hujjatlarni ERI bilan yuklaydi. Har biri maxsus raqam oladi va TEDda shu raqam ko'rsatiladi.
- **YuklaGo'da:** yo'q (spec'da "E-arxiv" tilga olinmagan; d-p15 44-grafa "6 ta hujjat").
- **Hukm:** Missing.
- **Nima qo'shish kerak:**
  - Kabinet sessiyasiga "E-arxiv" bosqichini qo'shing: fayllarni tayyorlash, format va hajm talablari, raqamlarni 44-grafaga yozish.
  - Fayl formati va ro'yxatini Bojxona qo'mitasi belgilaydi va E-arxiv orqali e'lon qiladi (VM-605). Talablar — tekshirilmagan.
- **Inson kerakmi:** ERI bilan tasdiqlash — foydalanuvchi.
- **Qonun:** VM-605 2-band ("E-arxiv" ta'rifi) va 2-bobdagi E-arxiv qoidalari.

#### F5. ERI bilan imzolash va yuborish
- **YuklaGo'da:** Y16, spec §8.2 6-qadam; d-p21 ("Endi sizning navbatingiz"), d-p23.
- **Hukm:** Needs a human (dizayn buni to'g'ri qiladi: to'xtaydi).
- **Nima qo'shish kerak:** imzodan oldin oxirgi tekshiruv: kurs va stavka sanasi, ERI muddati, to'lov tayyorligi.
- **Qonun:** VM-605 28-band; BK 264-modda (qabul qilingandan keyin BYD yuridik ahamiyatga ega hujjat).

#### F6. Format-mantiqiy nazoratdan qaytgan javoblar
- **YuklaGo'da:** Y19; d-p24 ("44-grafada muvofiqlik sertifikati yo'q").
- **Hukm:** Covered.
- **Qo'shimcha:** xabarlar kutubxonasini haqiqiy qaytarish matnlaridan to'plang (spec §8.5 — rasmiy sabab kodlari o'ylab topilmasin).
- **Qonun:** VM-605 1-ilova sxemasi (format-mantiqiy nazorat, qaytarish).

### G. Yuk kelishi va vaqtincha saqlash

#### G1. Dastlabki ma'lumot va kelish haqida xabar (tashuvchi vazifasi)
- **YuklaGo'da:** spec §6 8-qadam ("Art. 206 … guidance").
- **Hukm:** Partial.
- **Nima qo'shish kerak:** ekspeditorga "dastlabki ma'lumot yuborildimi?" degan tasdiq so'rovi. Muddatlarni BK 206-moddaning o'zidan oling (spec va `deklarant-jarayoni.md` 1 soat / 2 soat deydi — men 206-modda matnini bu auditda ochmadim, **tekshirilmagan**).
- **Inson kerakmi:** tashuvchi.
- **Qonun:** BK 17, 206-moddalar.

#### G2. Kelishni tasdiqlash, omborga qabul, tushirishdagi tafovut
- **Broker nima qiladi:**
  - Ombor qabul hujjatini oladi.
  - Tushirishda soni yoki vazni farq qilsa, dalolatnoma tuzdirib TEDga o'zgartirish so'raydi.
- **YuklaGo'da:** d-p9 ("Hisob boshi: 13.11.2026 — siz kiritdingiz (ombor qabul dalolatnomasi)").
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:** tafovut bo'lsa, VM-605 30–31-bandlardagi yo'l:
  - Deklarant TEDga o'zgartirish so'raydi.
  - Murojaat asosli deb topiladi, agar tovar doimiy nazoratda bo'lgan bo'lsa, ombor vakili dalolatnoma tuzgan bo'lsa, videoyozuv bo'lsa yoki ekspert xulosasi bo'lsa.
  - Bojxona murojaatni **1 ish kuni** ichida ko'radi.
- **Inson kerakmi:** ha. Omborda dalolatnoma tuzishda mijoz yoki broker hozir bo'lishi kerak.
- **Qonun:** VM-605 6–8, 30–31-bandlar.

#### G3. Muddatlar soati (deklaratsiya, saqlash, dastlabki deklaratsiya)
- **YuklaGo'da:** Y8; d-p7 va d-p9 ("Saqlash: [N] kun", "[Muddat uzunligi va qonun moddasi — v2 spec]").
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak (bo'sh joylarni to'ldirish, hammasi lex.uz'dan o'qilgan):**
  - Import BYD — tovar taqdim etilgan kundan **15 kalendar kun**. Muddat bojxona ishlamaydigan kunga tushsa, **keyingi ish kuni** oxirgi kun hisoblanadi (BK 261-modda 1–2-qismlar). Dizayn hozir 27.11 ni qat'iy ko'rsatadi; dam olish kuni qoidasi yo'q.
  - Vaqtincha saqlash — **60 kalendar kun**, tez buziladigan tovar uchun **10 kalendar kun**. Hisob tovar shu maqomni olgan kundan boshlanadi (BK 85-modda).
  - Dastlabki deklaratsiya — 30 kun (BK 262-modda).
  - Muddat o'tsa: MJtK 227-10-modda 2-qismi bo'yicha deklaratsiya yoki hujjatlarni muddatida bermaslik — BHMning 3 baravari jarima; bir yil ichida takrorlansa, kattaroq jarima.
- **Qonun:** BK 85, 261, 262-moddalar; MJtK 227-10-modda.

#### G4. Omborda tovarni ko'rish, namuna olish, ombor xarajatlari
- **YuklaGo'da:** d-p9 ("ombor to'lovlarini taxmin qilmaymiz").
- **Hukm:** Needs a human.
- **Nima qo'shish kerak:** egasi bojxona bo'lgan omborning rasmiy stavkasini ko'rsating (VM-55 4-band, E4). Xususiy ombor narxi shartnomaga bog'liq.
- **Inson kerakmi:** ha, jismonan omborda bo'lish uchun.
- **Qonun:** BK 87-modda (saqlashdagi operatsiyalar), 211-modda (namuna olish).

#### G5. Shikastlangan yoki yo'qolgan tovar, buzilgan plomba haqida xabar berish
- **YuklaGo'da:** yo'q.
- **Hukm:** Missing.
- **Nima qo'shish kerak:** "Tovar hujjatga mos emas / plomba buzilgan" tugmasi, bojxonani o'z vaqtida xabardor qilish bo'yicha yo'riqnoma va eskalatsiya.
- **Qonun:** BK 276-modda (deklarantning xabar berish majburiyati), 88-modda.

### H. Ko'rik va xavf kanallari

#### H1. Xavf darajasi va kutish vaqtini tushuntirish
- **YuklaGo'da:** spec §4; d-p24 (holatni foydalanuvchi qo'lda belgilaydi).
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak (VM-605 joriy matni bo'yicha):**
  - **Past xavf:** 3 soat. Hujjat asli so'ralmaydi, ko'rik va ekspertiza yo'q.
  - **O'rta xavf:** 8 soat. Jismoniy ko'rik o'tkazilmaydi.
  - **Yuqori xavf:** qonundagi umumiy muddat — BK 248-modda: hujjatlar to'liq berilgandan keyin 1 ish kuni.
  - Ish vaqtidan tashqari topshirilganda bu muddatlar boshqacha hisoblanadi.
  - Avtomatik rasmiylashtirish shartlari: VM-605 18-band.
- **Qonun:** VM-605 16, 18-bandlar; BK 248-modda.

#### H2. Hujjat asli yoki qo'shimcha hujjat so'rovi
- **YuklaGo'da:** yo'q.
- **Hukm:** Missing.
- **Nima qo'shish kerak:** "Bojxona hujjat so'radi" holati. Qaysi hujjat, qachongacha javob berish kerakligi va tayyor fayl to'plami.
- **Qonun:** BK 190, 263-moddalar.

#### H3. Bojxona ko'rigi
- **YuklaGo'da:** yo'q (faqat holat).
- **Hukm:** Needs a human.
- **Nima qo'shish kerak:** ko'rik tayinlanganda tasdiqlangan elektron xabarnomada joy va vaqt bo'ladi (VM-605 31-band). Foydalanuvchiga "kim borishi kerak, nima olib borish kerak" chek-listini va yig'imni ko'rsating (VM-55 3-band "b").
- **Inson kerakmi:** ha. Ko'rik odatda deklarant hozirligida o'tkaziladi (BK 195-modda).
- **Qonun:** BK 195-modda; VM-605 31-band.

#### H4. Bojxona ekspertizasi va namuna
- **Hukm:** Needs a human.
- **Nima qo'shish kerak:** ekspertiza tayinlanganda chiqarish tartibi (BK 271-1-modda) va deklarantning huquqlari (BK 214-modda) haqida tushuntirish.
- **Qonun:** BK 208–217-moddalar, 271-1-modda.

### I. GTD/BYDga tuzatish va o'zgartirish

#### I1. Qabul qilinguncha o'zgartirish yoki qaytarib olish
- **YuklaGo'da:** d-p20 (pauza, qo'lda tahrir), d-p22 (xato: "hech narsa yuborilmagan"), spec §8.2 5-qadam.
- **Hukm:** Covered.
- **Qonun:** BK 265-modda 2-qism.

#### I2. Imlo xatolarini ixtiyoriy tuzatish (1 ish kuni)
- **YuklaGo'da:** yo'q.
- **Hukm:** Missing.
- **Nima qo'shish kerak:**
  - "Ixtiyoriy tuzatishga ruxsat berildi" xabarnomasini tanib olish (Y19).
  - Ish kunlari bo'yicha **1 ish kuni** soati.
  - Kodlar va raqamlarga bu yo'l tegishli emas.
  - To'lovga va cheklovlarga ta'sir qilmaydigan xatolarni ixtiyoriy tuzatishda ma'muriy protokol tuzilmaydi.
- **Qonun:** VM-605 30-band (ixtiyoriy tuzatish huquqi), 31-band (1 ish kuni).

#### I3. Rasmiylashtiruv paytida tuzatish (TEDga o'zgartirish, KTS)
- **YuklaGo'da:** d-p24 ("44-grafani tuzatish … qayta to'ldiring va o'zingiz qayta imzolang").
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - Qaytarilgan TED bilan qabul qilingan TEDga o'zgartirishni farqlang.
  - Elektron BYDga o'zgartirish "tuzatishlar kiritish shakli"ni rasmiylashtirish orqali qilinadi (BK 266-modda 3-qism).
  - O'zgartirish deklaratsiya doirasini kengaytirmasligi kerak (BK 265-modda 4-qism).
  - Yig'im: BHMning 25%i (VM-55 2-band).
- **Qonun:** BK 265, 266, 320-moddalar.

#### I4. Chiqarilgandan keyin tuzatish, qaytarib olish, bekor qilish (3 yil)
- **YuklaGo'da:** Y8 (266-modda faqat ma'lumot sifatida).
- **Hukm:** Missing.
- **Nima qo'shish kerak:**
  - Arizani tayyorlash ustasi: sabab, dalil, to'lovga ta'siri (qo'shimcha to'lov yoki qaytarish).
  - E-kontraktdagi o'zgarishlardan keyin 10 ish kunlik majburiyat (VM-283 5-band).
  - Chiqarilgunga qadar qaytarib olish (BK 266-modda 2-qism).
- **Qonun:** BK 266-modda (qabul kunidan 3 yil), 320-modda.

### J. Nizolar va shikoyatlar

#### J1. Bojxona qarori ustidan shikoyat (yuqori organ yoki sud)
- **YuklaGo'da:** yo'q.
- **Hukm:** Needs a human.
- **Nima qo'shish kerak:**
  - Qaror sanasidan boshlanadigan muddat soati. Tekshiruv yoki audit natijasidagi qarorga yuqori organga **30 kun** ichida shikoyat beriladi (BK 409-2-modda).
  - Shikoyat shakli va mazmuni bo'yicha shablon (BK 409-3-modda).
  - Sudga berilsa, qarorning shikoyat qilingan qismi sud ishni qabul qilgan kundan to'xtatiladi (BK 409-7-modda).
  - Ma'muriy sud tartibi: BK 409-1-modda LexUZ sharhi bo'yicha.
- **Inson kerakmi:** ha (yurist yoki broker).
- **Qonun:** BK 409-1 – 409-7, 411-moddalar.

#### J2. Ma'muriy huquqbuzarlik ishi (jarima, musodara)
- **YuklaGo'da:** spec §9.5 (227-22-modda tilga olingan).
- **Hukm:** Needs a human.
- **Nima qo'shish kerak:** "Protokol tuzildi" holati va advokat yoki brokerga yo'naltirish. Jarima miqdorlarini faqat MJtK'dan ko'rsating:
  - **227-22-modda 1-qism:** noto'g'ri deklaratsiyalash — musodara va fuqarolarga BHMning 5–10 baravari, mansabdor shaxslarga 7–15 baravari.
  - **227-22-modda 2-qism:** noto'g'ri ma'lumot qarorga ta'sir qilmagan bo'lsa — BHMning 3 baravari.
  - **227-10-modda:** deklaratsiyalash tartibini buzish — fuqarolarga 2–5 BHM, mansabdor shaxslarga 3–7 BHM; muddatida bermaslik — 3 BHM.
  - Javobgar shaxs (MJtK 17-2-modda bo'yicha): hujjatdagi noto'g'ri axborot sabab bo'lsa — hujjatni bergan deklarant yoki uning ishonchli vakili.
- **Inson kerakmi:** ha.
- **Qonun:** MJtK 17-2, 227-10, 227-22-moddalar.

### K. Chiqarish

#### K1. Chiqarish shartlari va xabarnoma
- **YuklaGo'da:** d-p24 ("Chiqarildi" — foydalanuvchi belgilaydi), spec §6 14-qadam.
- **Hukm:** Partial.
- **Nima qo'shish kerak:** BK 271-moddadagi chiqarish shartlari bo'yicha chek-list:
  - qonunbuzarlik aniqlanmagan;
  - ruxsatnomalar bor;
  - rejim shartlari bajarilgan;
  - to'lov to'langan yoki ta'minlangan.
  - Chiqarish xodim ishtirokisiz ham bo'lishi mumkin.
- **Qonun:** BK 271-modda; VM-605 17, 19-bandlar.

#### K2. TED va elektron hujjatlarni 15 kun ichida yuklab olish
- **Broker nima qiladi:** rasmiylashtiruvdan keyin darhol TED va e-hujjatlar nusxasini yuklab oladi va arxivlaydi.
- **YuklaGo'da:** yo'q.
- **Hukm:** Missing.
- **Nima qo'shish kerak:**
  - "Chiqarildi" belgilanganda "15 kun ichida kabinetdan yuklab oling" eslatmasi va YuklaGo arxiviga yuklash.
  - Keyinroq kerak bo'lsa, Bojxona qo'mitasining 3 yillik **pulli** saqlash xizmati borligini ayting.
- **Inson kerakmi:** yuklab olishni foydalanuvchi o'z kabinetida qiladi.
- **Qonun:** VM-605 30-band (yuklab olish huquqi — rasmiylashtirilgan sanadan 15 kun), 37-band.

#### K3. Ombordan olib chiqish va buxgalteriyaga kirim
- **YuklaGo'da:** Y25 (CSV/1C — past prioritet).
- **Hukm:** Partial.
- **Nima qo'shish kerak:** buxgalter uchun "qaysi summa qaysi schyotga" eksport. QQS hisobga olish masalasi — tekshirilmagan (soliq maslahatchisi). Ombor bilan hisob-kitob.
- **Inson kerakmi:** omborga borish va buxgalter.

### L. Chiqarilgandan keyingi nazorat va arxiv

#### L1. Chiqarilgandan keyingi bojxona nazorati va audit
- **YuklaGo'da:** Y23 (o'z-o'zini audit).
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - "Audit tayyorgarligi" papkasi: shartnoma, invoys, to'lov, transport, BYD va BQD bir joyda.
  - BK 201-modda bo'yicha:
    - nazorat va qo'shimcha hisoblash tovar bojxona nazoratidan chiqqan paytdan **3 yil** ichida bo'lishi mumkin;
    - bitta kontrakt bo'yicha ko'pi bilan bir marta;
    - qaror asosida: maqsad, muddat, tarkib va davr yoziladi;
    - bojxona auditi tartibini VM belgilaydi (BK 201-moddaning LexUZ sharhida VM 06.11.2025 dagi 700-son qaror keltirilgan; audit tartibi aynan shu aktdami — tekshirilmagan).
- **Inson kerakmi:** audit paytida mijoz yoki buxgalter va broker.
- **Qonun:** BK 201-modda.

#### L2. Hujjatlarni saqlash
- **YuklaGo'da:** spec §8.5, §9.4 (fayllarni O'zbekistonda saqlash); d-p27 ("ma'lumotlarni yuklab olish").
- **Hukm:** Partial.
- **Kamchilik / nima qo'shish kerak:**
  - TEDga asos bo'lgan **qog'oz** hujjatlarni saqlash javobgarligi deklarantda. U ularni xavfsiz saqlashi va o'zgartirishdan himoyalashi shart (VM-605 30-band).
  - Elektron hujjatlarni saqlash: VM-605 32-band.
  - Bojxonaning o'zi BYDni nazoratdan chiqqan yildan keyingi yildan boshlab 3 yil saqlaydi (VM-605 36-band).
  - Mahsulot: o'zgartirilmaydigan (hash bilan) arxiv va saqlash muddatlari jadvali. Deklarant uchun aniq saqlash muddati — **tekshirilmagan** (amalda kamida BK 201-moddadagi 3 yil bilan moslang — tajriba (qonun emas)).
- **Qonun:** VM-605 30, 32, 36, 37-bandlar.

#### L3. E-kontrakt bo'yicha 180 kunlik nazorat
- **YuklaGo'da:** yo'q.
- **Hukm:** Missing.
- **Nima qo'shish kerak:** avans to'langan kundan **180 kun** soati: shu muddatda import rasmiylashtirilishi yoki pul qaytarilishi kerak. Muddat yaqinlashganda ogohlantirish.
- **Tipik xatolar (tajriba (qonun emas)):** Xitoyga avans to'langan, tovar kechikadi va muddat o'tib ketadi.
- **Qonun:** VM-283 Nizom 23-band.

#### L4. Kelib chiqish sertifikatini keyin berish va qaytarish (1 yil)
- **YuklaGo'da:** yo'q.
- **Hukm:** Missing.
- **Nima qo'shish kerak:** qo'shimcha boj to'langan bo'lsa, "1 yil ichida sertifikat bering — qaytarish mumkin" degan soat va E8 dagi ariza.
- **Qonun:** BK 366-modda, 49-bob.

#### L5. Mahsulot kutubxonasi va takroriy import
- **YuklaGo'da:** Y20; d-p25 (stavka o'zgarsa "qayta tasdiqlang").
- **Hukm:** Covered.
- **Qo'shimcha:** kutubxonada dastlabki qaror raqami va muddatini saqlang (C3).

#### L6. Qarzdorlik va penya monitoringi
- **YuklaGo'da:** yo'q.
- **Hukm:** Missing.
- **Nima qo'shish kerak:** talabnoma (BK 348-modda) kelganda Y19 orqali tushuntirish, muddat va penya haqida ogohlantirish (BK 349-modda).
- **Qonun:** BK 347–352-moddalar.

---

## 3. Hisob jadvali

| Bosqich | Covered | Partial | Missing | Needs a human | Jami |
|---|---|---|---|---|---|
| A. Qabul va vakolat | 1 | 3 | 1 | 0 | 5 |
| B. Hujjatlar | 3 | 5 | 0 | 2 | 10 |
| C. TIF TN | 0 | 2 | 1 | 0 | 3 |
| D. Bojxona qiymati | 0 | 4 | 2 | 1 | 7 |
| E. To'lovlar | 1 | 4 | 3 | 0 | 8 |
| F. Elektron topshirish | 2 | 2 | 1 | 1 | 6 |
| G. Kelish va saqlash | 0 | 3 | 1 | 1 | 5 |
| H. Ko'rik va kanal | 0 | 1 | 1 | 2 | 4 |
| I. Tuzatishlar | 1 | 1 | 2 | 0 | 4 |
| J. Nizolar | 0 | 0 | 0 | 2 | 2 |
| K. Chiqarish | 0 | 2 | 1 | 0 | 3 |
| L. Keyingi nazorat va arxiv | 1 | 2 | 3 | 0 | 6 |
| **Jami** | **9** | **29** | **16** | **9** | **63** |

---

## 4. Top-10 ustuvor kamchilik va tavsiyalar

1. **Bojxona qiymati noto'g'ri quriladi (D2–D5).** Transport faqat bojxona hududiga kirish joyigacha qo'shiladi, undan keyingisi chiqariladi. Sug'urta, royalti, assist va o'rovni ham hisoblash kerak. BQD qoralamasini qo'shing; Incoterms jadvali bo'yicha qoidalar dvigatelini yarating (BK 304, 305, 318-moddalar).
2. **Kelib chiqish va qo'shimcha boj yo'q (B5, E1, L4).** Kelib chiqishi aniqlanmagan yoki MFN bo'lmagan tovarga +5…+20% qo'shimcha boj bor (BK 300-1, 366-moddalar). Landed cost'ga "kelib chiqish isboti" tugunini, MFN ro'yxatini va 1 yillik qaytarish soatini qo'shing.
3. **Ko'p pozitsiyali invoys yo'q (C2).** 1688 yuklari ko'p qatorli bo'ladi. Pozitsiyalarga guruhlash, vazn va qiymatni taqsimlash va har pozitsiyaga ruxsatnoma bog'lash ekranini qo'shing.
4. **To'lov oqimi va yig'imlar to'liq emas (E4, E5, E8, D6).** Quyidagilar kerak:
   - g'azna hisobvarag'i, avans va "to'lov ko'rinyaptimi" tekshiruvi;
   - VM-55 ning barcha yig'imlari (o'zgartirish, ish vaqtidan tashqari, ko'rik, ombor);
   - qabul kunidagi kurs va stavka bo'yicha qayta hisob;
   - qaytarish arizasi.
5. **Rasmiylashtiruvdan keyin arxiv yo'q (K2, L2).** "TED va e-hujjatlarni 15 kun ichida yuklab oling" eslatmasi (VM-605 30-band) va o'zgarmaydigan audit papkasi kerak.
6. **E-arxiv va Yagona darcha qadamlari yo'q (F3, F4).** Hujjatlarni E-arxivga ERI bilan yuklash va raqamlarni 44-grafaga bog'lash; ruxsatnomani kabinetda tasdiqlatish (VM-605 15-band).
7. **Tuzatishlar moduli yo'q (G2, I2–I4).** Imlo xatosini 1 ish kunida tuzatish, tushirishdagi tafovut, KTS, 3 yillik o'zgartirish (BK 266-modda) va E-kontrakt o'zgarganda 10 ish kunlik majburiyat.
8. **Muddatlar dvigatelidagi bo'sh joylar (G3, L3, J1).**
   - BK 85: 60/10 kun.
   - BK 261: dam olish kuni bo'lsa keyingi ish kuni.
   - BK 262: 30 kun.
   - VM-283: 180 kun.
   - BK 409-2: 30 kun.
   - BK 366: 1 yil.
   - Bularni ish kuni kalendari bilan birga yuriting.
9. **Dastlabki deklaratsiya yo'li yo'q (F1).** Uni tanlash imkonini qo'shing. Spec'dagi "20% chegirmani aytmang" qoidasini yangilang: joriy VM-55 1-ilovasida bu chegirma bor.
10. **Inson kerak bo'lgan bosqichlar uchun xizmat yo'q (D7, H2–H4, J1–J2, G4).** "Bojxona hujjat so'radi / ko'rik tayinlandi / qiymatga e'tiroz / protokol" holatlari kerak. Har biriga chek-list va hamkor broker (navbatchi) yoki yurist bilan bog'lanish yo'li bo'lsin.

---

## 5. Spec v2 va dizayn v0.1 uchun aniq tuzatish takliflari (fayllar o'zgartirilmadi)

- **VM-605 tahriri:** spec 08.02.2026 tahririni keltiradi, lex.uz'da esa 21.07.2026 tahriri bor (VM-393). 14-band us-uz.gov.uz'ni tilga oladi. Qayta o'qing.
- **20% chegirma:** spec §1, §8.5 va §11 dagi taqiq joriy VM-55 1-ilova izohiga zid. Rasmiy manba havolasi bilan qaytarish mumkin.
- **E-kontrakt:** spec §6 6-qadam va §9.7 dagi "majburiyligi tekshirilmagan" o'rniga VM-283 1-band (kiritish majburiy, o'zini o'zi band qilganlar bundan mustasno) va Nizom 23-band (180 kun) yozilsin.
- **Broker moddalari:** "277–281" emas, joriy matnda 277, 281, 282-moddalar. 1000 BHM — sug'urta (BK 282-modda).
- **Dizayn bo'sh joylari:**
  - d-p6 ERI beruvchi — "Yangi texnologiyalar ilmiy-axborot markazi" AJ (VM-605 26-band);
  - d-p7 va d-p9 saqlash — 60 / 10 kun (BK 85-modda);
  - deklaratsiya muddati — 15 kun va keyingi ish kuni qoidasi (BK 261-modda).
- **d-p10 transport:** "Shenzhen → Toshkent" o'rniga "kirish joyigacha" va "kirishdan keyin" deb ikkiga bo'ling.
- **d-p10 sug'urta:** sug'urta qatori qo'shilsin.
- **d-p10 va d-p15 yig'im:** namuna "310 000" VM-55 bandiga mos emas, demo oldidan tuzating.
- **d-p9 eslatmalar:** "SMS va Telegram orqali" — spec §8.1 Telegramni mahsulot yuzasi sifatida chiqarib tashlagan. Bildirishnoma kanali sifatida ruxsat etilishini jamoa hal qilsin.

---

## 6. Ochiq savollar

**Sarvarbek uchun:**
1. 1-bosqichda ko'p pozitsiyali invoys (C2) qamraladimi? Busiz 1688 xaridorlari uchun mahsulot to'liq emas.
2. Hamkor broker (navbatchi) modeli rejadami? 9 ta vazifa baribir inson talab qiladi.
3. Oziq-ovqat (vet/fito) 1-bosqichda butunlay "eskalatsiya"mi?
4. Spec'dagi 20% chegirma taqiqini olib tashlaymizmi?

**TIF TN (tarif) mutaxassisi uchun:**
1. PQ-181 bo'yicha mashina o'qiy oladigan 10 xonali ro'yxat va uning tahrir sanasi.
2. Spetsifik va kombinatsiyalangan stavkalar.
3. Aksiz akti.
4. BK 300-1 uchun MFN mamlakatlar ro'yxatining rasmiy manbasi.
5. Ko'p pozitsiyali invoysda transport va sug'urtani taqsimlash qoidasi.

**Bojxona huquqi mutaxassisi uchun:**
1. ed2'ni avtomatlashtirish qonuniymi (spec §9.1)?
2. YuklaGo broker faoliyati hisoblanadimi (spec §9.2)?
3. E-kontrakt IDsiz BYD qabul qilinadimi?
4. us-uz.gov.uz va YAAAT'ning roli (VM-393).
5. Bojxona auditi tartibi qaysi aktda (VM-700?).
6. VM-847 dagi "1000 BHM" — ta'minotmi yoki sug'urta?
7. Deklarant uchun hujjat saqlash muddati qancha?
8. Incoterms 2010 va 2020 masalasi.
9. BK 206-moddadagi dastlabki ma'lumot muddatlari.

**Ekspeditor yoki kargo bilan intervyu uchun:** transport hisob-fakturasida "chegaragacha / chegaradan keyin" bo'linishi odatda bormi (tajriba savoli)?

---

## 7. CEO uchun 3 qator (English)

- YuklaGo covers the middle of the broker's job well (document reading, code suggestion, payment estimate, draft, guided cabinet fill that stops at signature). Of 63 import-broker tasks: 9 Covered, 29 Partial, 16 Missing, 9 Need a human.
- The biggest risk is that the "landed cost" promise is wrong today. Freight is added all the way to Tashkent instead of only to the border (Customs Code Arts. 304–305), and the extra duty for goods with unproven origin is not modelled (Arts. 300-1, 366: +5 to +20 points).
- Before the demo: fix valuation and origin, add multi-line invoices, payment and archive steps (download within 15 days), a corrections module, and a broker-on-call path for inspections, valuation disputes and appeals.

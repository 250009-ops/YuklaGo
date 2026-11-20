# YuklaGo — PM savollariga huquqiy javoblar (Bojxona Huquq va IT Integratsiya, `449f71e6`)

*2026-yil 18-noyabr, Toshkent vaqti (UTC+5). Manba: `team-review/product.md`, (c) bo'lim, "Bojxona Huquq va IT Integratsiya" jadvali (product.md 91–103-qatorlar).*
*Har bir javob shu kuni lex.uz'da ochilgan joriy matnga asoslangan. Tekshira olmaganim — **UNVERIFIED**. Bunday joylarda taxmin yo'q. Yuridik xulosa emas.*
*Batafsil tahlil: `team-review/legal.md`.*

---

## 1) Yo'l tanlash: shaxsiy jo'natma / yo'lovchi / tijorat BYD
**Placeholder:** `[v2 spec, "Yoʻl tanlash" boʻlimi]` — PDF p.06 line 31.

**Asosiy test — maqsad (BK 155-modda).** Jismoniy shaxsning shaxsiy ehtiyoji uchun olib kiriladigan va tadbirkorlik uchun mo'ljallanmagan tovar — "notijorat". Maqsad uch belgi bo'yicha aniqlanadi:
- **Miqdor:** oila ehtiyojidan ortiq bir turdagi tovar tadbirkorlik uchun deb qaraladi, agar shaxs aksini isbotlamasa.
- **Takroriylik:** bir xil tovarni bir necha marta olib kirish ham tadbirkorlik uchun deb qaraladi, agar shaxs aksini isbotlamasa.
- **Safar holatlari:** maqsadi va davomiyligi.

Manba: [BK 155-modda](https://lex.uz/docs/2876354)

| Yo'l | Huquqiy shart | Deklaratsiya shakli | Manba |
|---|---|---|---|
| **Yo'lovchi (qo'l yuki / bagaj)** | Notijorat maqsad (BK 155) | Chegaradan o'tishda, tovarni taqdim etish bilan bir vaqtda. "Yashil" yo'lak — og'zaki deklaratsiya. Taqiqlangan/cheklangan tovar yoki bojsiz normadan ortiq bo'lsa — yashil yo'lak yo'q. BYD to'ldirilmaydi (transport vositasi bundan mustasno) | BK 156, 162, 261-moddalar |
| **Xalqaro pochta / kuryer jo'natmasi** | Jismoniy shaxsga notijorat maqsadda, **yoki yuridik shaxsga**, qiymati **30 BHMgacha** | Pochta: Butunjahon pochta ittifoqi hujjatlari deklaratsiya hisoblanadi. Kuryer: tijorat hujjatlari deklaratsiya hisoblanadi. **Boshqa hollarda — BYD** | BK 165, 167-moddalar |
| **Tijorat (BYD, eksport/import rejimi)** | Notijorat testidan o'tmaydigan har qanday tovar; 30 BHMdan ortiq jo'natma; yuridik shaxs/YaTT importi | To'liq BYD/TED; 15 kalendar kun muddat | BK 167, 258, 261-moddalar; VM 605 |

**Bojsiz olib kirish normalari (shaxsiy ehtiyoj, 2025-yil 1-maydan):**
- havo transporti — 1000 AQSh dollari;
- temir yo'l va daryo — 500 AQSh dollari;
- avtomobil yoki piyoda o'tish punkti — 300 AQSh dollari;
- **xalqaro kuryer — 200 AQSh dollari** (kuryer uchun norma bir kalendar oy davomida qo'llanadi);
- **xalqaro pochta — 100 AQSh dollari**.

Chet elda temir yo'l/avto bilan 2 kundan, havo bilan 3 kundan kam bo'lganda normalar qo'llanmaydi. Manba: [VM 2025-yil 19-apreldagi 244-son qaror, 1-band](https://lex.uz/docs/7484114). Bu normalar to'lov masalasi. Ular "shaxsiy yoki tijorat" testini almashtirmaydi.

**Tadbirkor bo'lmagan shaxs tijorat maqsadida olib kira oladimi?**
- O'zbekiston jismoniy shaxsi deklarant bo'la oladi (BK 274-modda 1-band).
- Lekin tovar tadbirkorlik uchun bo'lsa, u notijorat imtiyozlaridan foydalana olmaydi (BK 155–156) va umumiy tartibda (BYD) deklaratsiya qilinadi.
- Tadbirkorlik faoliyatini davlat ro'yxatidan o'tmasdan yuritish — noqonuniy tadbirkorlik: huquqbuzarlik ashyolari musodara qilinadi va 5–7 BHM jarima (MJtK 176-modda, [lex.uz/docs/97664](https://lex.uz/docs/97664)).
- **Amaliy javob:** sotish uchun muntazam olib kirish — YaTT yoki yuridik shaxs orqali.
- **UNVERIFIED:** ro'yxatdan o'tmagan jismoniy shaxsga bir martalik tijorat partiyasini BYD bilan rasmiylashtirishga bojxona amalda ruxsat beradimi; "o'zini o'zi band qilgan" shaxs tovarni sotish uchun import qila oladimi.

**UI matni (p.06):** "Qatʼiy qoidalar: shaxsiy ehtiyoj uchunmi yoki sotish uchunmi — miqdor, takroriylik va safar maqsadi bo'yicha aniqlanadi (Bojxona kodeksi 155-modda). Jo'natma qiymati 30 BHMdan oshsa yoki tovar sotish uchun bo'lsa — BYD kerak (167-modda)."

---

## 2) ERI (elektron raqamli imzo) beruvchi markazning rasmiy nomi
**Placeholder:** `[ERI beruvchi markaz va manzil — v2 spec]` — PDF p.06 line 50.

- **Rasmiy nomi:** "O'zbekiston Respublikasi Davlat soliq qo'mitasi huzuridagi Yangi texnologiyalar ilmiy-axborot markazi" (Ro'yxatga olish markazi). Bu nom [VM 2018-yil 10-maydagi 348-son qarori, Ma'muriy reglament 2-band](https://lex.uz/docs/3730168) matnida turibdi. Hozirgi rasmiy sahifada nom "Soliq qo'mitasi huzuridagi "Yangi texnologiyalar" ilmiy-axborot markazi" deb yozilgan ([gov.uz/oz/soliq/sections/view/11769](https://gov.uz/oz/soliq/sections/view/11769)).
- **Qayerda olinadi:**
  - Davlat xizmatlari markazlari orqali bevosita;
  - Yagona interaktiv davlat xizmatlari portali orqali;
  - **e-imzo.soliq.uz** rasmiy resursi orqali. Portal yoki e-imzo.soliq.uz orqali faqat yuridik shaxs **rahbari** murojaat qila oladi; boshqa xodimlar — Davlat xizmatlari markaziga boradi.
  - Manba: o'sha gov.uz sahifasi; VM 348.
- **Qonuniy asos:** ERI kalitlarini akkreditatsiyadan o'tgan, O'zbekiston rezidenti bo'lgan yuridik shaxs — "ro'yxatga olish markazi" beradi ([ZRU-793, 9-modda](https://lex.uz/docs/6234904)).
- **Bojxona uchun eslatma:** ed1 xizmat pasportiga ko'ra BYD yuklash USB-token ERI bilan ishlaydi (legal.md'da qayd etilgan).
- **Manzil va narx — UNVERIFIED.** Yozmang. UI'da faqat havola bering.

**UI matni:** "ERI ni rasmiy markazdan olasiz: Soliq qoʻmitasi huzuridagi "Yangi texnologiyalar" ilmiy-axborot markazi — Davlat xizmatlari markazlari yoki e-imzo.soliq.uz orqali."

---

## 3) BK 261-modda va VM 605 Nizomi 11-band — joriy matn
**Placeholder:** `[qonun moddasi]` — PDF p.07 line 20.

**BK 261-modda (joriy matn, tasdiqlandi), asosiy qismlari:**
- 1-qism: import tovar uchun deklaratsiya "товар келиб тушадиган божхона органига товарлар тақдим этилган кундан эътиборан **ўн беш календарь кундан** кечиктирмай берилади". BK 22, 23, 25-boblaridagi hollar bundan mustasno.
- 2-qism: muddat oxiri bojxona organi ishlamaydigan kunga to'g'ri kelsa, navbatdagi ish kuni muddat tugaydigan kun hisoblanadi.
- Eksport tovar uchun deklaratsiya — tovar amalda olib chiqilgunga qadar.

[lex.uz/docs/2876354](https://lex.uz/docs/2876354)

**VM 605 Nizomi 11-band (joriy matn, tasdiqlandi):** import uchun BYD "товарлар тақдим этилган кундан эътиборан ўн беш календарь кундан кечиктирмай" beriladi ("божхона қонунчилик ҳужжатларида белгиланган ҳолатлар бундан мустасно"). Eksport — tovar amalda olib chiqilgunga qadar. Hujjat: VM 2018-yil 31-iyuldagi 605-son qarori, [lex.uz/docs/3844549](https://lex.uz/docs/3844549).

**Ha, 15 kun — kalendar kun, tovar bojxonaga taqdim etilgan kundan.**

**UI'da ko'rsatiladigan iqtibos:** "Manba: Bojxona kodeksi, 261-modda; Vazirlar Mahkamasining 31.07.2018 dagi 605-son qarori, Nizom 11-band."

**UNVERIFIED:** taqdim etilgan kun 1-kun hisoblanadimi (13.11 → 27.11 yoki 28.11). Har doim erta sanani ko'rsating.

---

## 4) Bosh ekranda qaysi qonuniy soatlar ko'rinishi mumkin
**Placeholder:** `[v2 spec, "Muddatlar"]` — PDF p.07 line 31.

Faqat quyidagilar ko'rsatilsin. Ularning hammasi lex.uz'da tasdiqlandi.

| Soat | Muddat | Qachondan | Modda |
|---|---|---|---|
| Import deklaratsiyasi | 15 kalendar kun ichida, kechiktirmay; oxiri dam olish kuniga tushsa — keyingi ish kuni | Tovar bojxonaga taqdim etilgan kun | BK 261; VM 605 Nizomi 11-band |
| Vaqtincha saqlash | ≤ 60 kalendar kun (tez buziladigan tovar — ≤ 10). Aniq muddatni joylashtirishni ma'lum qilgan vakolatli shaxs belgilaydi | Tovar vaqtincha saqlash maqomini olgan kun (7-savolga qarang) | BK 85, 226-moddalar |
| Saqlash tugashidan oldin rejim | Boshqa rejimga ma'lum qilish — saqlash tugaydigan kundan kechiktirmay. Rejimga joylashtirilgach — 3 kun ichida ombordan olib chiqish | Saqlash tugash sanasi | BK 89-modda |
| Dastlabki deklaratsiya | 30 kalendar kun ichida tovar taqdim etilmasa — berilmagan hisoblanadi | Dastlabki deklaratsiya qabul qilingan kun | BK 262-modda |
| Bojxona to'lovlari | Deklaratsiya qabul qilingunga qadar yoki u bilan bir vaqtda | — | BK 327-modda |
| Eksport deklaratsiyasi | Amalda olib chiqilgunga qadar | — | BK 261; VM 605 11-band |
| BYDni o'zgartirish/bekor qilish | 3 yil | Qabul qilingan kun | BK 266-modda |
| Import repatriatsiyasi (valyuta) | Tovarni rasmiylashtirish yoki pulni qaytarish — ≤ 180 kun | Import shartnomasi bo'yicha to'lov kuni | VM 283 Nizomi 23-band |
| Eksport tushumi | ≤ 180 kun | Eksport rejimiga rasmiylashtirilgan kun | VM 283 Nizomi 24-band |

**Ko'rsatmang** (foydalanuvchining soati emas yoki tasdiqlanmagan): BK 248 "1 ish kuni" va VM 605 15-band "3/8 soat" — bular bojxonaning ish vaqti (faqat ma'lumot sifatida ko'rsatish mumkin); ombor to'lovlari; sertifikat olish muddatlari (p.07 line 26 dagi `[N]` — bu **qonuniy soat emas**; Y7 qoidasiga ko'ra bo'sh qoldiring).

---

## 5) Yuk hubidagi topshirish soati — uzunligi va moddasi
**Placeholder:** `[Muddat uzunligi va qonun moddasi — v2 spec'dan]` — PDF p.09 line 35.

**15 kalendar kun**, tovar kelib tushadigan bojxona organiga taqdim etilgan kundan. Oxirgi kun bojxona ishlamaydigan kunga tushsa — keyingi ish kuni. Istisnolar: BK 22, 23, 25-boblar (tijorat transport vositalari, jismoniy shaxslarning notijorat tovarlari, quvur/elektr liniyasi).

Manba: [BK 261-modda](https://lex.uz/docs/2876354); [VM 605 Nizomi 11-band](https://lex.uz/docs/3844549).

**UI matni:** "Rasmiy manba: Bojxona kodeksi 261-modda — tovar bojxonaga taqdim etilgan kundan 15 kalendar kundan kechiktirmay."

---

## 6) Muddat o'tkazib yuborilsa — huquqiy oqibat
**Placeholder:** `[oqibatlar — v2 spec]` — PDF p.09 line 35.

- **MJtK 227-10-modda 2-qism (tasdiqlandi):** "Божхона органига товарлар ва транспорт воситалари учун божхона декларациясини, худди шунингдек ҳужжатлар ва қўшимча маълумотларни белгиланган муддатларда тақдим этмаслик" — **BHMning 3 baravari miqdorida jarima** (ZRU-720 tahriri). [lex.uz/docs/97664](https://lex.uz/docs/97664)
- Deklaratsiya shakli, joyi yoki tartibini buzish — fuqarolarga 2–5 BHM, mansabdor shaxslarga 3–7 BHM (227-10, 1-qism).
- **UNVERIFIED:** vaqtincha saqlash muddati tugab, tovar hech qaysi rejimga joylashtirilmasa, BK bo'yicha tovar bilan nima qilinishi (alohida modda topmadim). Taxmin qilmang.

**UI matni:** "Muddat oʻtsa: deklaratsiyani muddatida bermaganlik uchun BHMning 3 baravari miqdorida jarima (MJtK 227-10-modda 2-qism)."

---

## 7) Vaqtincha saqlash (BK 85-modda): muddat, boshlanishi, tugash sanasi
**Placeholder:** `[N]`, `[sana]`, `[Saqlash muddati — v2 spec]` — PDF p.02, 09, 10, 12–15, 17, 23, 24, 26.

- **Muddat (BK 85, tasdiqlandi):**
  - Muddatni tovarni bu rejimga joylashtirishni ma'lum qilgan **vakolatli shaxs belgilaydi**.
  - Muddat **60 kalendar kundan oshmaydi** (177-moddada boshqacha bo'lmasa — ombor tugatilgan holat).
  - **Tez buziladigan tovar — eng ko'pi 10 kalendar kun.**
- **Qachon boshlanadi:**
  - BK 85 oxirgi qism: hisob tovar 177-modda va **226-moddaning beshinchi qismiga** muvofiq vaqtincha saqlash maqomini olgan kundan boshlanadi.
  - BK 226: bojxona organi tovar yetkazilganini tasdiqlagan (kuzatuv hujjatiga belgi qo'ygan) **paytdan** tovar shu maqomni oladi. Tasdiq tashuvchi xabar bergandan keyin 3 soat ichida bo'ladi.
- **Istisno:** tovar doimiy bojxona nazoratida bo'lsa va rasmiylashtirish topshirilgandan keyin 24 soat ichida tugasa, vaqtincha saqlash bosqich sifatida qo'llanmaydi (VM 605 Nizomi 10-band).
- **Tugash sanasi:** boshlanish sanasi + vakolatli shaxs belgilagan kunlar soni (≤ 60 yoki ≤ 10). Shu kundan kechiktirmay tovar boshqa rejimga ma'lum qilinishi kerak (BK 89).
- **UNVERIFIED:**
  - 85-moddada dam olish kuni qoidasi yo'q (261-moddadagi qoida faqat deklaratsiya muddati uchun). Saqlash tugash sanasi dam olish kuniga tushsa, surilishi tasdiqlanmagan.
  - 1-kunni sanash usuli tasdiqlanmagan.
- Ombor to'lovlari — taxmin qilmang.

**UI matni:** "Vaqtincha saqlash: odatda 60 kalendar kungacha (tez buziladigan tovar — 10 kun). Aniq muddat omborga joylashtirishda belgilanadi — ombor hujjatini tekshiring. Hisob bojxona tovar yetkazilganini tasdiqlagan kundan boshlanadi. Manba: Bojxona kodeksi 85, 89, 226-moddalar."

Diqqat: ilova `[N]`ni faqat foydalanuvchi ombor hujjatidagi muddatni kiritganda hisoblasin. Aks holda: "≤ 60 kun (ombor hujjatidan tekshiring)".

---

## 8) E-kontrakt'da ro'yxatdan o'tish qachon majburiy
**Placeholder:** `[shartlar — v2 spec]` (E-kontrakt) — PDF p.11 line 36.

**Joriy akt:** VM 2020-yil 14-maydagi 283-son qarori (oxirgi tahrirlar VM 2026-yil 30-yanvardagi 40-son va PF-174 bilan) — [lex.uz/docs/4812419](https://lex.uz/docs/4812419).

- **Kim uchun (1-band):** **xo'jalik yurituvchi subyektlar** tashqi savdo kontraktlari, dalolatnomalar va invoyslar ma'lumotlarini ERI bilan Bojxona qo'mitasining "E-kontrakt" tizimiga kiritadi. **O'zini o'zi band qilgan shaxslar bundan mustasno.**
- **Kontraktsiz ham bo'ladi:** kontrakt tuzmasdan, **invoys asosida** import va eksport qilishga ruxsat bor (Nizom 6-band). Invoys ham tizimga kiritiladi.
- **Qachon:**
  - kontrakt va invoyslar — **tashqi savdo operatsiyalari boshlangunga qadar** (Nizomga 2-ilova, 1-bosqich);
  - birjada tuzilgan kontrakt — tuzilgandan keyin 1 ish kuni ichida;
  - ish va xizmat dalolatnomalari — dalolatnoma tuzilgan oydan keyingi oyning 20-sanasigacha (Nizom 6-band).
- **Oqibat:**
  - Talabga rioya qilmaslik va ma'lumotni noto'g'ri shakllantirish eksport-import tartibini buzish deb baholanadi (6-band). Aniq jarima moddasi bu yerda ko'rsatilmagan — **UNVERIFIED**.
  - Banklar bank operatsiyasini kontrakt bilan tizimdagi ma'lumot mos kelgandagina bajaradi (11-band).
- "Import qiluvchi" ta'rifi: yuridik shaxslar va yuridik shaxs tashkil etmagan tadbirkor jismoniy shaxslar (Nizom 2-band).
- **UNVERIFIED:** tadbirkor bo'lmagan jismoniy shaxs uchun majburiyat — matnda ko'rsatilmagan; xulosa chiqarmayman.

**UI matni:** "Qachon talab qilinadi: kompaniya yoki YaTT boʻlsangiz, har bir tashqi savdo kontrakti yoki invoysi E-kontrakt tizimiga yuk joʻnatilishi va toʻlovdan **oldin** kiritilishi kerak (VM 283-son qarori, 1-band va Nizom). Oʻzini oʻzi band qilganlar bundan mustasno."

---

## 9) Bank so'raydigan hujjatlar va valyuta tushumi muddatlari
**Placeholder:** `[v2 spec, "Bank"]` — PDF p.11 line 41.

**Tasdiqlangan muddatlar:**
- **Import (VM 283 Nizomi 23-band, VM 77-son tahriri, 19.05.2025dan):** tovarni import, qayta ishlash yoki ombor rejimiga rasmiylashtirish (yoki ish/xizmat bajarilishi, yoki pulni qaytarish) — import kontrakti bo'yicha **to'lov kunidan 180 kundan** oshmasligi kerak.
- **Eksport (24-band):** tushum yoki tovarni qayta olib kirish — tovar eksport/reeksport/erkin ombor rejimiga rasmiylashtirilgan kundan (xizmatda — qabul dalolatnomasi imzolangan kundan) **180 kundan** oshmasligi kerak.
- **Jarima ([ZRU-573 "Valyutani tartibga solish to'g'risida", 11-1-modda](https://lex.uz/docs/4562834)):**
  - Repatriatsiya to'lov yoki eksport kunidan 180 kun o'tgach, ko'pi bilan **45 kun** ichida ta'minlanmasa (kichik tadbirkorlik subyektlari uchun **90 kun**), jarima solinadi.
  - 360 kungacha kechikish — repatriatsiya qilinmagan summaning **5 %**;
  - 360–545 kun — **qo'shimcha 10 %**;
  - 545 kun va undan ortiq — **qo'shimcha 35 %**.
  - Istisnolar bor (fors-major, 180 kundan uzun yetkazib berish muddati belgilangan uskunalar va h.k.).
- **ZRU-573, 11-modda:** muddat norezident majburiyati yuzaga kelgan kundan 180 kundan oshsa, operatsiya kapital harakati operatsiyasi deb baholanadi.

**Tasdiqlangan hujjat qoidalari:**
- Banklar valyuta operatsiyasini rezident bank talab etadigan tegishli hujjatlarni taqdim etsa bajarishi shart (ZRU-573, 20-modda).
- Valyuta nazorati organlari faqat shu operatsiyaga bevosita taalluqli hujjatlarni talab qila oladi (24-modda).
- Bank E-kontrakt'dagi ma'lumotni kontrakt bilan solishtiradi; farq bo'lmasa operatsiyani bajaradi. Avans to'lov yoki akkreditivda tizim ma'lumotini tekshiradi (VM 283 Nizomi 11-band).
- E-kontrakt identifikatsiya raqami (IDN) kontrakt va invoysga tizimda beriladi (283, 1-ilova).

**UNVERIFIED:** Markaziy bank yoki tijorat banklarining **aniq hujjatlar ro'yxati** (masalan, to'lov topshirig'iga qaysi ilovalar kerakligi). Markaziy bankning tegishli normativ hujjatini lex.uz'da topib o'qimadim — ro'yxat bermayman.

**UI matni:** "Bank soʻraydigan hujjatlar: E-kontrakt'da roʻyxatdan oʻtgan kontrakt yoki invoys va bankingiz soʻraydigan hujjatlar (roʻyxatni bankingizdan oling). Muddatlar: importda toʻlovdan keyin 180 kun ichida tovar rasmiylashtirilishi yoki pul qaytishi kerak; eksportda tushum 180 kun ichida (VM 283 Nizomi 23–24-bandlar). Kechiksa — jarima (Valyutani tartibga solish toʻgʻrisidagi qonun, 11-1-modda)."

---

## Qo'shimcha A) ed2.customs.uz kabinetini avtomatlashtirish mumkinmi?
**Shartli ruxsat (kulrang zona).** Taqiqlovchi norma topilmadi, ruxsat beruvchi rasmiy qoida ham yo'q. Ochiq API yo'q, ed2 foydalanish shartlari e'lon qilinmagan (aniq emas). Faqat quyidagi shartlar bilan:
- foydalanuvchining o'z kabineti va o'z kompyuteri;
- kirish va har bir imzo — faqat foydalanuvchi o'zi;
- ERI, PIN va parol saqlanmaydi;
- himoyalarni chetlab o'tish yo'q (JK 278-2, 278-3; MJtK 155-1);
- imzodan oldin to'liq ko'rib chiqish;
- Bojxona qo'mitasiga rasmiy so'rov, javob kelguncha demoda faqat mock.

Manbalar: BK 275; VM 605 15, 28-bandlar; ZRU-793 27-modda; 560-II 12-modda. Batafsil va xat loyihasi: `legal.md` 1-bo'lim.

## Qo'shimcha B) Pulli tayyorlash VM 847 bo'yicha "broker faoliyati"mi?
- **Foydalanuvchi o'zi imzolab yuboradigan dastur (SaaS)** — ehtimol broker faoliyati emas (UNVERIFIED, rasmiy tushuntirish yo'q).
- **Broker faoliyati bo'ladi,** agar YuklaGo yoki uning xodimi:
  - mijoz nomidan va topshirig'i bilan shartnoma asosida rasmiylashtirsa;
  - o'z ERI'si bilan imzolasa yoki yuborsa;
  - mijozning TIF ro'yxatiga broker yoki ishonchli shaxs sifatida kiritilsa.
  
  Manba: BK 15, 277-moddalar.
- **Broker uchun talablar:**
  - Bojxona qo'mitasiga xabarnoma (ZRU-701 3-ilova 35-poz.);
  - xabarnomasiz ishlash — 20 BHM jarima (4-ilova III 28-poz.);
  - VM 847 32-ilova: 1000 BHM ta'minot, 2+ mutaxassis, yig'im BHMning 50 %.

  Manbalar: [ZRU-701](https://lex.uz/docs/5511879), [VM 847](https://lex.uz/docs/7274716). Batafsil: `legal.md` 2-bo'lim.

---

## UNVERIFIED ro'yxati (bu fayl bo'yicha)
- Ro'yxatdan o'tmagan jismoniy shaxsning bir martalik tijorat importi amalda; o'zini o'zi band qilganlarning tovar importi.
- ERI markazi manzili va narxi (ataylab berilmadi).
- 15 kunlik va saqlash muddatlarida 1-kunni sanash; saqlash tugash sanasi dam olish kuniga tushsa surilishi.
- Saqlash muddati tugagach tovarning taqdiri (BK'da alohida modda topilmadi).
- E-kontrakt talabini buzganlik uchun aniq jarima moddasi; tadbirkor bo'lmagan shaxs uchun E-kontrakt.
- Markaziy bank va tijorat banklarining aniq hujjatlar ro'yxati.

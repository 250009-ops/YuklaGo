# YuklaGo — Spec v2 va Dizayn v0.1 bo'yicha xavfsizlik tekshiruvi

Tayyorladi: Xavfsizlik va Muvofiqlik · 2026-11-18 (Toshkent vaqti) · Yuridik xulosa emas.
Tekshirilgan fayllar: `yuklago-spec-v2.md` (§ raqamlari bilan), `design-v0.1/yuklago-web-ui-v0.1.pdf` (sahifa = "d-p19" ko'rinishida), `design-v0.1/design-rationale.md`.
Asos: `/workspace/yuklago-security/legal.md`, `threat-model.md`, huquq rolining `team-review/legal.md` fayli ("Xavfsizlik jamoasi savollariga javoblar" bo'limi). Faqat o'zim ochib tekshirgan manbalar keltirilgan; qolgani — **tasdiqlanmadi**.
**v2 yangilanish (2026-11-18, 03:46 dan keyin):** legal.md bilan moslashtirildi. VM 415-son, MJtK 46-2 2-qism (ZRU-1115), ZRU-764 16-modda va DPF ro'yxati alohida tekshirildi (1.4–1.6, G10, P0, 5-bo'lim).

**Umumiy baho:** Spec ham, dizayn ham asosiy chiziqni to'g'ri ushlaydi: ERI dan oldin to'xtash, parol so'ralmaydi, MASHQ rejimi haqiqiy kabinetdan aniq ajratilgan, haqiqiy kabinet o'chirilgan. Bo'shliqlar bor joylar: **domen qulfi va sandbox, sessiyani tozalash, audit log qayerda saqlanishi va yaxlitligi, LLM ga nima ketishi, avtomatlashtirish tezligi**, shuningdek "brokerni almashtiramiz" degan pozitsiya.

---

## 1. Spec v2 ga xos tahdid modeli

### 1.1 ERI va parol qurilmadan chiqmaydi
- **Fakt:** ed2.customs.uz foydalanuvchi kompyuteridagi E-IMZO orqali imzolaydi (`wss://127.0.0.1:64443`, https://ed2.customs.uz/eri_new/e-imzo.js). BYuD yuklash faqat USB-TOKEN bilan kirilganda ishlaydi (ed1.customs.uz xizmat pasporti).
- **Huquqiy asos:** ZRU-793 27-modda — yopiq kalit xavfsizligi kalit egasining zimmasida (https://lex.uz/docs/6234904).
- **Talablar:**
  - Embedded browser haqiqiy `https://ed2.customs.uz` originini **foydalanuvchi qurilmasida** yuklaydi. Server tomonidagi brauzer yoki proxy ishlatilmaydi.
  - YuklaGo Desktop kodi E-IMZO WebSocket'iga **o'zi ulanmaydi** — unga faqat kabinet sahifasi ulanadi.
  - `.pfx` fayllar o'qilmaydi. Login/imzo oynalarida DOM hook, keylog va screenshot ishlatilmaydi.
- **Spec bilan moslik:** §8, §8.2 qadam 6, §9.3, Y16 — mos. Dizayn: d-p17, d-p18 ("YuklaGo unga ulanmaydi"), d-p21, d-p27 — mos.

### 1.2 Sessiya izolyatsiyasi
- Har bir YuklaGo hisobi va har bir yuk sessiyasi uchun alohida brauzer profili (partition) bo'ladi. Cookie faqat xotirada saqlanadi, diskka yozilmaydi.
- "Sessiyani tugatish", logout va harakatsizlik (15 daqiqa) paytida cookie, storage, cache va yuklab olingan fayllar o'chiriladi.
- Navigatsiya allowlist: faqat `ed2.customs.uz` (yoki `mashq.yuklago.uz`) va E-IMZO localhost ruxsat etiladi. Pop-up/yangi oyna ochilmaydi, TLS xatoda sahifa bloklanadi.
- Electron ishlatilsa: context isolation yoqiladi, nodeIntegration o'chiriladi, sandbox yoqiladi.
- **Spec'da yo'q** (§8.1–8.2 bu haqda jim).

### 1.3 Audit log
- Har avtomatik va qo'lda qilingan harakat yoziladi: vaqt, kim (Siz/YuklaGo), grafa, qiymat **hashi yoki kategoriyasi**, qayta o'qish natijasi. Yozuvlar hash-zanjir bilan bog'lanadi, ya'ni append-only.
- Login/imzo oynalaridagi hech narsa yozilmaydi (dizayn d-p23 buni to'g'ri aytadi).
- Ikki qatlam:
  - lokal to'liq log — foydalanuvchi qurilmasida;
  - serverga faqat hodisa xulosasi (field qiymatlarisiz) sinxronlanadi.

### 1.4 Ma'lumotlarni saqlash va lokalizatsiya (legal.md 3.2–3.4 bilan kelishilgan)
- **Huquqiy holat:**
  - Amalda **yangi 27-1-modda** qo'llanadi (ZRU-547, ZRU-1125 tahririda, 27.03.2026 dan). O'zbekistonda saqlash shart bo'lganlar: biometrik, genetik va telekom abonent ma'lumotlari (https://lex.uz/docs/4396419, https://lex.uz/docs/8099215).
  - MJtK 46-2 1-qismidagi "jismonan O'zbekistonda" iborasi blanket norma, mazmuni ZRU-547 ga tayanadi. Huquq roli lex posterior (ZRU-682 18-modda) asosida 27-1 ustun deb hisoblaydi. ZRU-682 ni men o'zim ochmadim; legal.md xulosasini qabul qilamiz. Tekshiruvchi 46-2 ni so'zma-so'z qo'llashi xavfi qoladi.
  - **Yangi va bevosita xavf — MJtK 46-2 2-qism** (ZRU-1115, 21.01.2026). Men o'zim tekshirdim (https://lex.uz/docs/97664): sun'iy intellekt texnologiyalari yordamida shaxsga doir ma'lumotlarga qonunga xilof ishlov berish yoki ularni OAV, telekom tarmoqlari yoki Internetda tarqatish — qurollar musodarasi bilan **50–100 BHM** jarima. → AI quvurimiz uchun qonuniy asos (rozilik), minimallashtirish va maskalash **majburiy**.
  - **20-modda (reyestr):** faqat 27-1 2-qismidagi bazalar uchun majburiy. Biometrikka ishlov bermasak — **bizga majburiy emas** (legal.md 3.3).
  - **Pasport fotosi:** 26-modda bo'yicha biometrik hisoblanadimi — aniq emas. Agar hisoblansa, lokalizatsiya va reyestr majburiy bo'ladi. → **Pasport/ID rasmini so'ramaymiz va saqlamaymiz** (P0, 4-bo'lim).
  - Yuridik shaxs ma'lumotlari (kompaniya nomi, kompaniya STIR, summa, tovar) shaxsga doir ma'lumot emas. Rahbar F.I.Sh., imzo, telefon, haydovchi pasporti, JShShIR va YaTT ma'lumotlari esa shaxsga doir ma'lumot (legal.md 3.4).
- **Qaror:** barcha bazalar, fayllar va loglar O'zbekistonda saqlanadi (spec §8.5 "Hosting" bilan mos). Faqat LLM chaqiruvi chegaradan o'tadi — 1.5 ga qarang.
- **Saqlash muddatlari:**
  - shaxsga doir maydonlar va hujjatlar — yuk yopilgandan keyin foydalanuvchi belgilagan muddat (taklif: 12 oy);
  - raw LLM chiqishi — 30 kun;
  - rozilik jurnali — rozilik qaytarib olingandan keyin ham isbot uchun saqlanadi.
  - "Hisobni o'chirish" (d-p27) haqiqiy o'chirishni bajaradi.
- **Shifrlash:** saqlashda (at-rest) va uzatishda (TLS).
- **Spec'da muddatlar va shifrlash hali ko'rsatilmagan** — spec §8.5 ga qo'shiladi.

### 1.5 LLM ga ma'lumot chiqishi — qaror

**Tekshirilgan faktlar (2026-11-18):**
- **VM 415-son, 29.07.2026, 03.08.2026 dan kuchda** (https://lex.uz/docs/8369688): "bir xil himoya" ta'minlovchi **49 davlat** ro'yxati. Ro'yxatda Germaniya, Niderlandiya, Irlandiya, Belgiya, Finlyandiya va boshqa Yevropa Ittifoqi davlatlari, Buyuk Britaniya, Shveytsariya, Yaponiya, Koreya, Singapur, Rossiya, Gonkong bor. **AQSh — "*"** belgisi bilan: "EU-US Data Privacy Framework doirasida faoliyat ko'rsatayotgan kompaniyalar uchun". Xitoy (Gonkongdan tashqari) ro'yxatda yo'q.
- VM 415 4-band:
  - ro'yxatda yo'q davlatga uzatish — vakolatli organ (IIV huzuridagi Migratsiya va personallashtirish departamenti, 3-band) belgilagan huquqiy, tashkiliy va texnik shartlar bajarilganda;
  - transchegaraviy uzatishda sizib chiqish aniqlansa — **24 soatda xabar, 72 soatda batafsil ma'lumot**.
  - 7-band: ro'yxatda yo'q davlatlar uchun talablar 3 oyda ishlab chiqilishi kerak edi. Ular e'lon qilinganmi — **tasdiqlanmadi**.
- **DPF rasmiy ro'yxati** (dataprivacyframework.gov, rasmiy API `dpfapi.azurewebsites.net/api/participants`, 2026-11-18 da so'raldi):
  - **Google LLC** — EU-US Certification **Active**, Non-HR ma'lumot qamrab olingan, amal qilish muddati 2027-09-13 gacha (participant 5780).
  - **Microsoft Corporation** — EU-US **Active**, 2027-08-31 gacha (6474).
  - **Amazon.com, Inc.** — EU-US **Active**, 2027-01-02 gacha; qamrab olingan subyektlar ro'yxatida "Amazon Web Services, Inc." bor (5776).
  - **"OpenAI"**, "OpenAI OpCo", "Open AI", **"Anthropic"**, "Anthropic PBC" bo'yicha qidiruv — **0 natija** (Active va Inactive ro'yxatlarda). Bu endi rasmiy qidiruv natijasi, faqat ikkilamchi manba emas. Lekin boshqa yuridik nom ostida qatnashish ehtimoli 100% istisno qilinmagan.

**Qaror / tavsiya:**
| Variant | Asos | Holat |
|---|---|---|
| **1 (tavsiya): Google Gemini — Google Cloud (Vertex AI) orqali, ishlov berish mintaqasi VM 415 ro'yxatidagi Yevropa Ittifoqi davlatida** (masalan, Germaniya yoki Niderlandiya) | Ikki mustaqil asos: (a) mintaqa davlati VM 415 ro'yxatida; (b) Google LLC DPF da Active — AQShga uzatilgan taqdirda ham "*" sharti bajariladi | **Tavsiya.** Vertex'dagi aniq mintaqa variantlari, "no training" va zero-retention shartlari, shartnoma tomoni (masalan, Google Cloud EMEA, Irlandiya) — **tasdiqlanmadi**, ulanishdan oldin DPA va mahsulot shartlaridan o'qiladi |
| 2 (zaxira): boshqa model AWS yoki Microsoft bulutida, Yevropa Ittifoqi mintaqasida | AWS (Amazon.com Inc. qamrovida) va Microsoft DPF da Active; mintaqa davlati ro'yxatda | Qaysi modellar qaysi mintaqada mavjudligi va retention shartlari — **tasdiqlanmadi**. Model egasi DPF da bo'lmasa, bulut provayderi orqali ishlov berish 415 ni qondiradimi — huquq roli savoli |
| ✕ OpenAI API yoki Anthropic API to'g'ridan-to'g'ri, AQShda ishlov berish | Rasmiy DPF qidiruvi 0 natija → "*" sharti bajarilmaydi | **MVP da ishlatilmaydi.** Faqat ZRU-547 15-modda bo'yicha aniq rozilik + VM 415 4-band shartlari bilan mumkin (shartlar e'lon qilinmagan) |
| ✕ Xitoy provayderlari (materik) | Xitoy VM 415 ro'yxatida yo'q | Ishlatilmaydi |
| Kelajak | O'zbekistondagi OCR/model | Chegaradan o'tish butunlay yo'qoladi |

- **Demo (hackathon):** faqat sintetik hujjatlar, real shaxsga doir ma'lumot yo'q. Shu sababli demoda provayder tanlovi huquqiy xavf tug'dirmaydi, lekin arxitektura 1-variantga mos quriladi.
- **DPF holati vaqtinchalik.** Har relizdan oldin va har chorakda qayta tekshiriladi (sertifikat muddati tugashi mumkin).

**Nima yuboriladi va maskalash:**
| Vazifa (spec §8.4) | Modelga ketadi | Ketmaydi |
|---|---|---|
| Hujjat tasnifi | Sahifa rasmi — **maskalangandan keyin** | Pasport/ID sahifalari (umuman qabul qilinmaydi) |
| Field extraction | Tovar qatorlari, summa, og'irlik, Incoterms, kompaniya nomlari | JShShIR, pasport raqami, shaxs F.I.Sh., telefon, imzo, muhr, haydovchi ma'lumotlari, hisob raqami (IBAN). Bular yuborishdan oldin O'zbekistondagi serverda (yoki desktop'da lokal) OCR + regex/NER bilan aniqlanib, `[SHAXS_1]` kabi token yoki qora to'rtburchak bilan almashtiriladi. Token↔qiymat jadvali faqat O'zbekistonda saqlanadi |
| TIF TN kod tanlash | Faqat tovar tavsifi va rasmiy ro'yxatdagi nomzod kodlar | Har qanday shaxsga doir ma'lumot |
| Y19 xabar tushuntirish | Maskalangan xabar matni | Skrinshotdagi STIR/JShShIR/ism (avval maskalanadi) |
- Kompaniya STIR shaxsga doir ma'lumot emas, lekin modelga kerak emas — minimallashtirish uchun u ham maskalanadi. YaTT STIR shaxsga doir deb hisoblanadi.
- Maskalash ishlamasa (ishonch past bo'lsa) — **fail-closed**: sahifa modelga yuborilmaydi, foydalanuvchiga qo'lda kiritish taklif etiladi.

**Rozilik (ZRU-547 15, 21-moddalar; legal.md 3.5 matni asosida):**
- Birinchi hujjat yuklashdan oldin alohida ekran ko'rsatiladi: provayder nomi, mamlakat yoki mintaqa, maskalash, "o'qitishga ishlatilmaydi", saqlash muddati, "asosiy baza O'zbekistonda".
- Checkbox **standart holatda belgilanmagan** bo'ladi.
- Rozilik jurnalga yoziladi: foydalanuvchi, vaqt, matn versiyasi.
- Rozilikni Sozlamalarda (d-p27) qaytarib olish mumkin. Rozilik bo'lmasa, AI o'qish o'chadi va qo'lda kiritish rejimi qoladi.

**Saqlash muddati (retention):**
- Provayderda: no-training + zero/minimal retention (shartnomaviy; 1-variant uchun **tasdiqlanmadi**).
- Bizda: raw model chiqishi (spec §8.4 "both stored for audit") — maskalangan holda **30 kun**, keyin o'chiriladi. Foydalanuvchi tasdiqlagan qiymatlar yuk bilan birga saqlanadi.
- Promptlar va javoblar umumiy loglarga (APM, crash-report) tushmaydi.

**Pul hisoblash:** §8.3, §8.4 — LLM hisoblamaydi. Mos (ZRU-547 24-modda ruhiga ham mos — qarorni foydalanuvchi qabul qiladi).

### 1.6 ZRU-764 (Kiberxavfsizlik) 16-modda — nazoratlar ro'yxati
**Taalluqlilik.** 3-moddadagi "kiberxavfsizlik subyekti" ta'rifi "milliy axborot resurslari"ga egalik, foydalanish va ular bo'yicha elektron axborot xizmatlari ko'rsatish bilan bog'langan. Bizga to'liq taalluqliligi **aniq emas**. Legal.md bilan bir xil yondashuv: amalda taalluqli deb hisoblaymiz (https://lex.uz/docs/5960604, 16-modda men tekshirdim).

| 16-modda majburiyati | YuklaGo nazorati | Prioritet |
|---|---|---|
| Ma'lumotlarning noqonuniy tarqalishi, o'g'irlanishi, yo'qolishi, yaxlitligi buzilishi, bloklanishi, qalbakilashtirilishi va ruxsatsiz kirishning oldini olish | Shifrlash, RBAC, 2FA (d-p27 da bor), maskalash, hash-zanjirli log, minimal ma'lumot | P0 (demo darajasida) / P1 |
| Ruxsatsiz kirishdan keyin tizim va resurslarni tezkor tiklash | Shifrlangan zaxira nusxalar O'zbekistonda, tiklash sinovi | P1 |
| Hodisa va kiberjinoyatlar haqida vakolatli organni xabardor qilish; raqamli izlarni saqlash; hodisalarni tahlil qilish | Incident response runbook. Server va kirish loglarini o'chirib bo'lmaydigan holda belgilangan muddat saqlash. Qaysi organga va qaysi muddatda xabar berilishi — **tasdiqlanmadi**. Cross-border sizib chiqish uchun VM 415: 24 soat / 72 soat | P1 (runbook loyihasi — P0) |
| Kiberxavfsizlik obyektlarini himoya qilish va monitoring bo'yicha vakolatli organ bilan ma'lumot almashish | Kontakt shaxs (security lead) belgilanadi | P2 |
| Vakolatli organ belgilagan kiberxavfsizlik talablariga rioya | Talablar ro'yxatini olish va mapping — **tasdiqlanmadi** (talablar matni ochilmadi) | P1 |
| Hodisalarga javob mexanizmi / kiberxavfsizlik bo'linmasi; bo'lmasa — vakolatli organ ruxsati bilan autsorsing | Kichik jamoada: security lead + runbook. Autsorsing faqat ruxsat bilan | P1 |
| Vakolatli organga monitoring tizimlari va (yoki) obyektlarga kirish berish | Arxitekturada hisobga olinadi. Bu ERI yoki foydalanuvchi kalitlariga taalluqli emas — ular bizda yo'q | P2 |

---

## 2. Bo'shliqlar va ziddiyatlar

| # | Qayerda | Muammo | Nazorat bilan ziddiyat | Taklif |
|---|---|---|---|---|
| G1 | spec "What changed in v2" (9-qator), Y14 "replaces the broker's typing" | "takes over the broker's main role" iborasi | Broker ta'rifi — deklarant topshirig'i bilan va uning **nomidan** shartnoma asosida ish qiluvchi (BK 15, 277-moddalar, https://lex.uz/docs/2876354). Pullik tayyorlash broker faoliyatiga yaqinlashadi | Ommaviy matnda "brokerni almashtiradi" deyilmaydi. O'rniga: "o'zingiz topshirishingiz uchun dastur" |
| G2 | spec §8.2 qadam 4 ("fills them quickly"); dizayn rationale §4, d-p17 "Oddiy — tez yozadi", "Tez — to'xtamaydi" | To'liq tezlikda yozish | threat-model D1. MJtK 155-1 — ruxsati bor shaxsning tizim qoidalarini buzishi | Inson tezligiga yaqin throttle. Haqiqiy kabinetda "Tez" rejimi o'chiriladi. Faqat mock'da qoladi |
| G3 | spec §8.1–8.2; d-p19..d-p22 viewport | Domen allowlist, TLS, pop-up taqiqi, sandbox spec'da yo'q. Dizaynda URL ko'rsatilgan, lekin "tasdiqlangan domen / qulf" belgisi yo'q | threat-model S1, E1 | §8.2 ga "origin lock + sandbox" qo'shiladi. Viewport chrome'ga domen qulfi belgisi qo'yiladi |
| G4 | spec §8.2; d-p21/d-p23 "Sessiyani tugatish" | Sessiya tugaganda cookie/profil tozalanishi aytilmagan | threat-model I2, I4 | Spec'ga wipe va idle timeout qo'shiladi. UI'da "Sessiya ma'lumotlari bu kompyuterdan o'chirildi" ko'rsatiladi |
| G5 | spec §8.1 ("logs actions locally") vs d-p27 "Xavfsizlik jurnali" (telefon va tashqi qurilma hodisalari) va d-p23 "Yordam xizmatiga ulashish" | Log lokalmi yoki serverdami — ziddiyat | Saqlash joyi, lokalizatsiya, maxfiylik | 1.3 dagi ikki qatlamli model qabul qilinadi va spec'ga yoziladi |
| G6 | spec §8.2 qadam 5 ("value **category**") vs d-p23 jadvali "Yozilgan qiymat" (to'liq qiymat), d-p19 "8 · Oluvchi STIR · qayta o'qildi" | Spec kategoriya deydi, dizayn to'liq qiymatni (STIR, summa) logda saqlaydi | ZRU-547 19-modda (hajm maqsadga mos), 28-modda (maxfiylik) | To'liq qiymat faqat lokal logda qoladi. Server va support nusxasida qiymat maskalanadi |
| G7 | spec va dizayn — hamma joyda | Audit log tamper-evident (hash-zanjir) emas | threat-model T4, R1 | Hash-zanjir qo'shiladi. PDF eksportda oxirgi hash ko'rsatiladi |
| G8 | spec §8.2; d-p19 kabinetdagi "Saqlash" tugmasi va bo'lim tablari | Avtomat qaysi tugmalarni bosishi mumkinligi aniq emas. "Saqlash" va tab almashtirishni bosadimi? | threat-model E2 | Kodda qattiq **blocklist**: Yuborish/Imzolash/To'lash/Tasdiqlash/Login. Allowlist: faqat field input va tab navigatsiyasi. Spec'ga yoziladi |
| G9 | spec umuman; dizayn | Bojxona to'lovini **to'lash** bosqichi va "YuklaGo hech qachon to'lamaydi" qoidasi yo'q | threat-model A6, E2 | Spec'ga "Pay — faqat foydalanuvchi" qo'shiladi. d-p21 va d-p24 ga indikator qo'yiladi |
| G10 | spec §8.4, §9.4; d-p13 (invoys yuklash), d-p24 (Y19 skrinshot) | LLM provayderi, joylashuvi, maskalash, retention va foydalanuvchi roziligi yo'q. UI hujjat AI ga yuborilishini aytmaydi | ZRU-547 15, 21-moddalar; VM 415-son (https://lex.uz/docs/8369688); **MJtK 46-2 2-qism — AI orqali noqonuniy ishlov berish uchun 50–100 BHM** | **Qaror (1.5):** Gemini — Google Cloud orqali, VM 415 ro'yxatidagi Yevropa Ittifoqi mintaqasida (Google LLC DPF Active). OpenAI/Anthropic API to'g'ridan-to'g'ri ishlatilmaydi (DPF qidiruvi 0). Yuborishdan oldin maskalash, fail-closed. Alohida rozilik ekrani (d-p13 oldidan). Raw chiqish 30 kun. d-p13 va d-p24 ga "Qayerga yuboriladi" izohi. Spec §8.4/§9.4 ga provayder, mintaqa va retention yoziladi |
| G11 | d-p27 "Broker uchun to'plam havolasi · 7 kun · Tashqi qurilmada ochildi" | Hujjatlar to'plami autentifikatsiyasiz havola orqali uchinchi shaxsga beriladi | ZRU-547 28-modda (subyekt roziligisiz oshkor qilmaslik) | Havola + bir martalik kod, qisqa muddat. "Bekor qilish" bor — yaxshi. Ulashishdan oldin rozilik so'raladi |
| G12 | d-p23 "Kabinet ko'rsatgan raqam ... kabinet sahifasidan o'qildi" | Kabinetdan ma'lumot o'qish (scraping) | 560-II 12-modda — axborot olish tartibini resurs egasi belgilaydi (https://lex.uz/docs/82956) | Mock'da OK. Haqiqiy kabinetda faqat yuridik ruxsatdan keyin; ungacha foydalanuvchi raqamni o'zi kiritadi |
| G13 | spec §8.2 | Desktop yangilanishlari imzolanishi va mapping versiyalarining yaxlitligi yo'q | threat-model T3 | P2: kod imzolash, imzolangan mapping paketlari |
| G14 | dizayn rationale §4 (web "manual copy-assist", nusxalash tugmasi) | Clipboard'da STIR/summa qolib ketadi | I-turdagi kichik risk | P2: clipboard'ni 60 soniyadan keyin tozalash |
| G15 | spec Appendix | Manbalar holati: VM 847-son, VM 605-son va MJtK 227-22 ni huquq roli tasdiqladi (legal.md; men o'zim qayta ochmadim). PF-5414 havolasi 404 (legal.md 21-qator). ZRU-1125 uchun spec'dagi lex.uz/en/docs/8104580 — **tasdiqlanmadi** (men 8099215 ni tekshirdim) | — | Spec'da 8099215 havolasiga almashtiriladi. PF-5414 o'rniga VM 605 1-bandi keltiriladi (legal.md taklifi) |

**Yaxshi tomonlar (saqlab qolinsin):**
- d-p5 va d-p21 dagi "parol so'rasa — firibgarlik" ogohlantirishi;
- d-p27 "kalit yuklash joyi yo'q";
- d-p20 kabinetga bosish bilan darhol pauza;
- d-p22 fail-closed ("taxmin qilib yozmadim");
- d-p16 dagi bloklovchi tasdiq;
- MASHQ belgilarining to'rt qatlami;
- haqiqiy kabinet "hozircha yoqilmagan" (d-p17).

---

## 3. UI xavfsizlikni qanday isbotlaydi (foydalanuvchi va hakamlar uchun)

| Indikator | Mavjud ekran | Holat / kerakli o'zgarish |
|---|---|---|
| Lokal imzo belgisi ("Imzo sizning kompyuteringizda, E-IMZO orqali. YuklaGo kalitga ulanmaydi") | d-p18, d-p21 matnda bor | **Qisman.** Doimiy badge yo'q → rail tepasiga doimiy "🔒 Lokal imzo" badge qo'yiladi |
| "Avtomat hech qachon Yuborish/Imzolash/To'lash ni bosmaydi" | d-p17 ("faqat siz bosasiz"), d-p21 | **Qisman.** "To'lash" tilga olinmagan. Viewport'dagi bu tugmalar ustiga "Faqat siz" qulf belgisi qo'yiladi |
| Jonli harakatlar logi | d-p19 rail "Yozildi · oxirgilari", d-p23 to'liq yozuv | **Bor.** Har yozuv yoniga hash-zanjir/"o'zgartirilmagan" belgisi qo'shiladi (G7) |
| Domen qulfi indikatori | d-p19..22 URL satri (faqat mashq) | **Yo'q.** Kerak: "✓ ed2.customs.uz · TLS tekshirildi · boshqa saytga o'tish bloklangan". Begona domen bo'lsa — to'liq qizil to'xtash ekrani |
| Ma'lumot joylashuvi izohi | — | **Yo'q.** d-p27 ("Ma'lumotlaringiz sizniki") va d-p13 ga: "Hujjatlaringiz O'zbekistondagi serverda saqlanadi. AI o'qish: Google Cloud, [Yevropa Ittifoqi mintaqasi], ism/pasport/JShShIR/telefon yashirilgan, model o'qitishga ishlatilmaydi" |
| LLM rozilik ekrani | — | **Yo'q.** Birinchi hujjat yuklashdan oldin (d-p13 oldidan) qo'shiladi; checkbox standart holatda belgilanmagan; Sozlamalarda (d-p27) qaytarib olish mumkin (1.5) |
| "Pasport rasmini yuklamang" izohi | d-p13 (hujjat turlari ro'yxati) | **Yo'q.** Yuklash maydoni oldida: "Pasport yoki ID rasmini yuklamang — faqat kerakli rekvizitlarni matn sifatida kiritasiz" |
| Imzodan oldin ko'rib chiqish ekrani | d-p15/16 (to'ldirishdan oldin), d-p21 (hand-off) | **Bor, kuchaytiriladi.** d-p21 ga: qoralama ↔ kabinet farqlari, jami to'lovlar, "1 ta maydonni siz o'zgartirdingiz" ro'yxati |
| Sessiya tozalandi tasdig'i | d-p23 | **Yo'q.** "Cookie va sessiya bu kompyuterdan o'chirildi · 10:21" qatori qo'shiladi |
| MASHQ / haqiqiy farqi | d-p19..23 | **Bor** — a'lo |
| Login/imzo oynasiga yozmaslik | d-p21, d-p23 | **Bor** |
| Tezlik/rate-limit izohi | d-p17 | **O'zgartiriladi:** haqiqiy kabinetda "Tez" yo'q (G2) |

---

## 4. Demo uchun P0 tuzatishlar
1. **Faqat MASHQ portalida demo** (spec §9.1 va dizayn bilan mos). Real ed2 va real tokenlar ishlatilmaydi, real invoyslar demoga olinmaydi.
2. **Domen qulfi + sandbox:** mashq domeni allowlist'da. Begona URL ochilsa, qizil to'xtash ekrani chiqadi. UI'da qulf indikatori (G3).
3. **Tugmalar blocklist'i** kodda va UI'da: Yuborish/Imzolash/To'lash/Login ustida "Faqat siz" belgisi. Demoda avtomat urinib ko'rib bloklanganini logda ko'rsatish mumkin (G8, G9).
4. **Sessiya wipe:** "Sessiyani tugatish" bosilganda profil tozalanadi va d-p23 da tasdiq chiqadi (G4).
5. **Hash-zanjirli log:** d-p23 ning PDF eksportida yakuniy hash. Server/support nusxasida qiymatlar maskalangan (G5–G7).
6. **LLM: maskalash + rozilik + provayder:** demo hujjatlari sintetik. Pipeline'da JShShIR/pasport/ism/telefon/imzo maskalash yoqiladi, fail-closed. d-p13 oldidan rozilik ekrani va "qayerga yuboriladi" izohi. Provayder: Gemini — Google Cloud, Yevropa Ittifoqi mintaqasi. Bu spec §8.4 ga yoziladi (G10, 1.5). Sabab: MJtK 46-2 2-qism.
7. **Pasport/ID rasmi saqlanmaydi:**
   - pasport/ID skanerlari so'ralmaydi va qabul qilinmaydi;
   - foydalanuvchi baribir yuklasa — fayl saqlanmaydi va LLM ga yuborilmaydi, faqat kerakli matnli rekvizitlar qo'lda kiritiladi;
   - yuz tanish funksiyasi yo'q.
   Sabab: 26-modda bo'yicha biometrik maqomi aniq emas. Aks holda 27-1 lokalizatsiya va 20-modda reyestr majburiy bo'lishi mumkin (legal.md 3.3).
8. **Incident runbook loyihasi (1 sahifa):** kim, nima, qachon; VM 415 24/72 soat; ZRU-764 16-modda (1.6).
9. **Pitch matni:** "brokerni almashtiradi" o'rniga "o'zingiz topshirishingiz uchun dastur; imzo va javobgarlik sizda" (G1).

P1 (pilotdan oldin): throttle va haqiqiy kabinetda "Tez" yo'q (G2); broker havolasiga kod va legal.md dagi ogohlantirish matni (G11; legal.md 4.2, 16-qator); kabinetdan o'qishni o'chirish (G12); shifrlash va retention siyosati; admin RBAC; provayder DPA va zero-retention shartnomasi; ZRU-764 1.6 jadvalidagi P1 bandlari.
P2: imzolangan yangilanishlar (G13); clipboard tozalash (G14).

---

## 5. "Bojxona Huquq va IT Integratsiya" uchun ochiq savollar
Javob berilgan va olib tashlangan savollar:
- broker chegarasi;
- reyestr (20-modda);
- 27-1 va 46-2 ziddiyati;
- "axborot vositachisi";
- VM 847/605;
- ZRU-764 taalluqliligi (legal.md, "Xavfsizlik jamoasi savollariga javoblar").

Qolganlari:
1. **Bojxona qo'mitasiga so'rov:** legal.md dagi xat loyihasi tayyor, lekin YUBORILMAGAN. Kim imzolaydi va qaysi kanal orqali yuboriladi? Javob kelguncha haqiqiy kabinet o'chiq qoladi.
2. **Kabinetdan ma'lumot o'qish** (registratsiya raqami, status — G12) 560-II 12-modda va JK 278-2 nuqtai nazaridan qabul qilinadimi? Bu legal.md da alohida javob berilmagan.
3. **VM 415 4-band 1-xatboshi doirasi:** "qo'shimcha ruxsatsiz va xabardor qilmasdan avtomatik uzatish" matnda "xalqaro kelishuvlar asosida tashkil etilgan axborot tizimlari orqali" uzatishga tegishli. Xususiy SaaS → Google Cloud (Yevropa Ittifoqi) uzatish uchun asos 15-modda 2-qismi (ro'yxatdagi davlat) deb hisoblash to'g'rimi? Vakolatli organni xabardor qilish kerakmi?
4. Shartnoma tomoni Yevropa Ittifoqi sho''ba kompaniyasi bo'lsa (masalan, Google Cloud EMEA), ishlov berish esa Yevropa Ittifoqi mintaqasida bo'lsa — bu 415 ni qondiradimi? Model egasi DPF da bo'lmasa-yu, bulut provayderi (AWS/Microsoft) DPF da bo'lsa-chi?
5. VM 415 7-band bo'yicha ro'yxatda yo'q davlatlar uchun talablar va standart shartnoma shartlari e'lon qilinganmi?
6. ZRU-764: hodisa haqida qaysi vakolatli organga va qaysi muddatda xabar beriladi? Biz amal qilishimiz kerak bo'lgan kiberxavfsizlik talablari hujjati qaysi?
7. Pasport/ID fotosi 26-modda bo'yicha biometrikmi (P0 da baribir saqlamaymiz)?
8. Spec'dagi lex.uz/en/docs/8104580 havolasi (ZRU-1125?) va PF-5414 manbasi.

## Manbalar (faqat tekshirilganlar)
- https://lex.uz/docs/2876354 · https://lex.uz/docs/4396419 · https://lex.uz/docs/8099215 · https://lex.uz/docs/6234904 · https://lex.uz/docs/165074 · https://lex.uz/docs/82956 · https://lex.uz/docs/97664 · https://lex.uz/docs/111453 · https://lex.uz/docs/7093753
- https://lex.uz/docs/8369688 (VM 415-son) · https://lex.uz/docs/5960604 (ZRU-764, 3 va 16-moddalar) · MJtK 46-2 2-qism (ZRU-1115) — https://lex.uz/docs/97664
- DPF: https://www.dataprivacyframework.gov/participant/5780.Google (sahifa JS; ma'lumot rasmiy API orqali o'qildi: https://dpfapi.azurewebsites.net/api/participants/5780, /6474, /5776 va qidiruv `POST /api/participants`, 2026-11-18)
- https://ed2.customs.uz/eri_new/e-imzo.js · https://ed1.customs.uz/PersonCabinet/template/property/ted_proper.jsp
- Huquq rolidan qabul qilingan, men qayta ochmaganlar: ZRU-682 18-modda (https://lex.uz/docs/5378966), VM 847-son, VM 605-son, MJtK 227-22

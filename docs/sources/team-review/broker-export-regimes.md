# YuklaGo — broker auditi: eksport, reeksport, vaqtincha olib kirish, qayta ishlash, tranzit va nazoratdagi tovarlar (v1)

**Kim yozdi:** eksport va maxsus rejimlar bo'yicha bojxona broker nuqtai nazaridan audit (Grok Bot).
**Sana:** 2026-yil 18-noyabr, Toshkent vaqti (UTC+5).
**Nima ko'rildi:** `/workspace/hackathon/yuklago-spec-v2.md` (spec v2), `/workspace/hackathon/design-v0.1/` (PDF matni `all.txt`, `pg01–pg28.txt`, `design-rationale.md`), kontekst uchun `deklarant-jarayoni.md`.
**Bu yuridik xulosa emas.** Har bir qoida lex.uz'dagi amaldagi matn bo'yicha 2026-11-18 kuni o'qildi. Tekshirib bo'lmagan narsa **"tasdiqlanmagan"** deb yozilgan. Hech bir raqam, stavka yoki muddat o'ylab topilmagan.

**Holat belgilari:**
- **Qamralgan** — spec yoki dizaynda bor va broker darajasida yetarli.
- **Qisman** — bor, lekin yarim, faqat importga moslangan yoki muhim qadami yo'q.
- **Yo'q** — spec ham, dizayn ham bu ishni qilmaydi (eng ko'pi "brokerga topshiring" deydi).
- **Odam kerak** — dasturga to'liq berib bo'lmaydi: litsenziyali broker yoki mutaxassis qarori kerak. Bunda spec bu holatni to'g'ri yo'naltiradimi, shu baholanadi.

---

## 1. Qisqa xulosa

1. **Import uchun yaxshi skelet bor, eksport va maxsus rejimlar uchun deyarli yo'q.** Spec §3 eksportni "Phase 1" deydi, lekin Y21 (eksport yo'li) "Medium" va "import yo'li mustahkam bo'lgandan keyin". Dizaynda eksport uchun alohida ekran yo'q, bitta matn bor xolos: "Eksport tanlansa: kelib chiqish sertifikati, fitosanitar talablar va valyuta tushumi bosqichlari qo'shiladi. Qoidalar — [v2 spec, "Eksport"]" (`pg08.txt`). Specda esa bunday "Eksport" bo'limi yo'q, ya'ni havola hech qayerga olib bormaydi.
2. **Reeksport, vaqtincha olib kirish/chiqish, qayta ishlash, tranzit Phase 2'da va hozir "Yo'q".** Spec ularni "taniydi, tushuntiradi va brokerga yuboradi" deydi (§3). Lekin oqimda **rejimni aniqlovchi savol yo'q**: "Yangi yuk" ekranida faqat "Import / Eksport" tugmalari bor (`pg08.txt`). Shuning uchun ko'rgazma uskunasini (vaqtincha olib kirish) olib kelayotgan foydalanuvchi oddiy importga (IM 40) tushib qoladi.
3. **Nazoratdagi tovarlar import tomonida qisman qamralgan** (Y7 go/no-go, `pg12.txt`). Eksport tomonidagi fitosanitariya, veterinariya, kelib chiqish sertifikati, eksport nazorati va Asl belgisi oqimi yo'q.
4. **Sanoq:** 52 ta vazifa bor. Qamralgan 4 ta, Qisman 11 ta, Yo'q 22 ta, Odam kerak 15 ta (pastdagi jadvallarga qarang).

## 2. CEO uchun 3 qator

1. YuklaGo hozir **import vositasi**. Eksport va maxsus rejimlar specda bor deb yozilgan, lekin qoidalari ham, ekranlari ham yo'q. Eksportchi yoki fermerga hozircha va'da berib bo'lmaydi.
2. Eng arzon va eng katta yutuqlar: (a) **rejimni aniqlovchi savollar**, (b) **eksport paketi**: E-kontrakt, kelib chiqish, fito/vet sertifikatlari, 180 kunlik valyuta tushumi soati, (c) har bir rejimning **muddat soatlari**. Hammasi lex.uz'da tasdiqlandi.
3. Qayta ishlash normalari, tranzit/TIR, vaqtincha olib kirish kafolatlari va litsenziyali tovarlar **broker ishi bo'lib qolishi kerak**. Ularni "brokerga tayyor paket" sifatida mahsulotga aylantirish to'g'ri strategiya.

---

## 3. Muhim tuzatish: rejim kodlari (O'zbekiston kodlari Rossiya/YeOII kodlari emas)

Topshiriqda EK31 (reeksport) va IM53 (vaqtincha olib kirish) misol qilingan. **O'zbekistonda bu kodlar boshqacha.** Bojxona yuk deklaratsiyasini to'ldirish tartibi to'g'risidagi yo'riqnoma (2773-son, 06.04.2016), 3-ilova "Bojxona rejimlari tasniflagichi" — https://lex.uz/uz/docs/2924955 (lex.uz'da 2026-11-18 kuni o'qildi):

| Rejim | Kod (grafa 1) |
|---|---|
| Eksport | **10** (EK 10) |
| Reeksport | **11** (EK 11), 31 emas |
| Vaqtincha olib chiqish | **12** |
| Erkin muomalaga chiqarish (import) | **40** |
| Reimport | **41** |
| Vaqtincha olib kirish | **42** (IM 42), 53 emas |
| Bojxona hududida qayta ishlash | **51** |
| Bojxona hududidan tashqarida qayta ishlash | **61** |
| Vaqtincha saqlash | **70** |
| Bojxona tranziti | **80** (TR 80) |

**Xulosa:** YuklaGo'da rejim kodlari 2773-son yo'riqnomadan olinishi va sanali bo'lishi kerak. Yo'riqnomaga 2025–2026 yillarda o'zgartirishlar kiritilgan (2773-13: https://www.lex.uz/docs/7921085 ; 2773-14: https://lex.uz/docs/8031771), shuning uchun kod jadvalini tarif mutaxassisi har chiqarilishdan oldin qayta tekshirsin. Bojxona kodeksidagi 16 ta rejim ro'yxati: 25-modda (https://lex.uz/docs/2876354).

---

## 4. Lex.uz bo'yicha tasdiqlangan asosiy qoidalar (bu auditda o'qilgan)

| # | Qoida | Manba (lex.uz) |
|---|---|---|
| L1 | Eksport rejimi: Bojxona kodeksi 29–31-moddalar. Hujjatlar ro'yxatini Vazirlar Mahkamasi belgilaydi. Ruxsat hujjati bo'lsa, bojxona uning axborot tizimida borligini **o'zi tekshiradi** (31-modda 2-qism). | https://lex.uz/docs/2876354 |
| L2 | Reeksport (32–35-moddalar): tovar identifikatsiya qilinishi kerak (33). Reeksport rejimiga joylashtirilgan kundan **3 ish kuni ichida tranzit deklaratsiyasi** berilmasa, tovar vaqtincha saqlashga o'tkazilishi kerak (32). Ilgari importda to'langan boj va soliqlar quyidagi shartlar birga bajarilsa qaytariladi: import e'lon qilingan kundan **2 yil ichida** reeksport va tovar ishlatilmagan (35, 49-bob tartibida). | https://lex.uz/docs/2876354 |
| L3 | Vaqtincha olib kirish (61–69): muddat **2 yil** (64). Ayrim hollarda 2 yildan ortiq uzaytiriladi (lizing, xalqaro shartnoma va h.k.). Rejim muddat o'tgan kunning ertasidan kechiktirmay tugallanishi kerak (69). Davriy to'lovlar: har bir to'liq/to'liq bo'lmagan oy uchun importda to'lanadigan boj va soliqlarning **5 foizi** (66). To'liq shartli ozod qilinadigan tovarlar ro'yxati VM 212-son (20.06.2016) qarori bilan belgilanadi (65-moddaga ishora). | https://lex.uz/docs/2876354 |
| L4 | Vaqtincha olib chiqish muddati **2 yil** (39). Reimport: chiqarilgandan **3 yil ichida** (59). | https://lex.uz/docs/2876354 |
| L5 | Hududda qayta ishlash (70–82): bojxona beradigan **qayta ishlash ruxsatnomasi** asosida (70). Shartlar: identifikatsiya, **chiqish normasi**, taqiq va cheklovlar, to'lov ta'minoti (72). Norma yoki texnologiya o'zgarsa yangi ariza beriladi (72). Ruxsatnoma **2 yilga** beriladi, muntazam operatsiyalar uchun **5 yilgacha** (75). Chiqish normasini texnologik hujjatlar asosida vakolatli shaxs belgilaydi (76). | https://lex.uz/docs/2876354 |
| L6 | Hududdan tashqarida qayta ishlash (42–54): ruxsatnoma **2 yilga** (47). Uzaytirish arizasi muddat tugashiga **kamida 1 oy qolganda** beriladi (47). | https://lex.uz/docs/2876354 |
| L7 | Tranzit (116–120): tranzit deklaratsiyasi va kuzatuv hujjatlari kerak (118). Ruxsatnoma talab qilinadigan tovarga ruxsatnoma bo'lishi shart (117). Faqat to'lov ta'minoti bilan tranzit qilinadigan tovarlar ro'yxatini qonunchilik belgilaydi (117). Eng ko'p muddat: **havo — 3 kalendar kun; yer usti va suv — 1000 km uchun 15 kalendar kun** (120). | https://lex.uz/docs/2876354 |
| L8 | Bojxona nazorati ostida tashish (218): yetkazish muddati havo 3 kun, avto va suv 10 kun, temir yo'l 2000 km uchun 30 kun. Kodeks bu yerda VM 737-son (31.12.2022) va VM 800-son (22.12.2020) qarorlariga havola beradi. | https://lex.uz/docs/2876354 |
| L9 | Vaqtincha saqlash: odatda **60 kalendar kun**, tez buziladigan tovar uchun **10 kalendar kun** (85). Import deklaratsiyasi taqdim etilgandan **15 kalendar kun** ichida (261). Dastlabki deklaratsiya 30 kun ichida tovar taqdim etilmasa berilmagan hisoblanadi (262). | https://lex.uz/docs/2876354 |
| L10 | Bojxona yig'imi (VM 55-son): "tranzit", "hududda qayta ishlash", "hududdan tashqarida qayta ishlash" rejimlarida **bir deklaratsiya uchun BHMning 25 foizi**. Tranzit deklaratsiyasiga bojxona organi tomonidan o'zgartirish kiritish — BHMning 10 foizi. Vaqtincha saqlash, voz kechish va yo'q qilish rejimlarida yig'im olinmaydi. | https://lex.uz/docs/-7357270 |
| L11 | Tranzit deklaratsiyasi "E-Tranzit" yoki "us-uz.gov.uz" orqali beriladi. Dastlabki axborot berilgan bo'lsa, **TIR daftarchasi va ATA karneti tranzit deklaratsiyasi sifatida qabul qilinadi**. Deklaratsiya chegarani kesib o'tgunga qadar yoki o'tish vaqtida beriladi (VM 737-son, 31.12.2022). | https://lex.uz/uz/docs/-6334883 |
| L12 | Valyuta tushumi: tashqi savdo bo'yicha repatriatsiya **180 kundan** oshsa, operatsiya kapital harakati deb baholanadi (11-modda). Jarima: 180 kundan keyin yana **45 kun** (kichik tadbirkorlik uchun **90 kun**) o'tsa, kechikishga qarab **5% / +10% / +35%** (11¹-modda). | https://www.lex.uz/docs/-4562834 |
| L13 | E-kontrakt (TSOYaEAT) — VM 283-son (14.05.2020). Oldindan to'lov kafolatlangan eksport kontraktlari bo'yicha hisob-kitob ma'lumotnomalari tizimga **bojxona rasmiylashtiruvigacha** kiritiladi. | https://www.lex.uz/docs/-4812419 |
| L14 | Meva-sabzavot eksporti (VM 163-son Nizom, 23.02.2019, amaldagi tahrir). Qamrov: TIF TN 07, 08, 0904, 1202. Kontraktsiz, **invoys asosida** eksport qilsa bo'ladi, sharti invoys TSOYaEATga kiritilgan bo'lishi (6-band, PF-174 2026 tahriri). Tashishda **tabiiy yo'qotish normalari** TSOYaEATga kiritiladi (8-band). Muddati o'tgan debitorligi bor eksportchi **"nohalol eksportchilar reyestri"**ga avtomatik tushadi (11-band). | https://lex.uz/uz/docs/-4213596 |
| L15 | Meva-sabzavot uchun minimal eksport narxlari ro'yxatini Hukumat komissiyasi tasdiqlaydi (PQ-107, 29.02.2024, 2-band). | https://lex.uz/uz/acts/-6825806 |
| L16 | Kelib chiqish sertifikati (VM 994-son Nizom, 2024 tahriri). Vakolatli organ: **"O'zbekekspertiza" AJ**. Shakllar: GSP davlatlariga **A shakli**, MDHga **ST-1**, shartnoma shakllari, **ST-UZ**. Ekspertiza va sertifikat **1 ish kuni** ichida; meva-sabzavot uchun ham 1 ish kuni; 84–89 guruhlar yoki katta assortiment uchun 2 ish kunigacha. | https://lex.uz/uz/docs/-4643161 |
| L17 | O'simliklar karantini to'g'risidagi qonun, 12-modda: eksport qilinayotgan o'simlik mahsulotining **har bir turkumi** fitosanitariya sertifikati bilan jo'natiladi. | https://www.lex.uz/en/docs/-119173 |
| L18 | Karantin ostidagi mahsulot uchun fitosanitariya talablari (4-son, 21.12.2022): eksport mahsuloti saqlanadigan ombor va muzlatgichlarga talablar (6-bob), yog'och taglik va o'ramlarda termo-muhr, binolarni mavsum oldidan profilaktik fumigatsiya qilish. | https://www.lex.uz/uz/docs/-6379574 |
| L19 | Veterinariya (VM 148-son, 10.04.2023). Nazoratdagi tovar eksportiga **ruxsatnoma kalendar yilga** beriladi (7-band). Eksport ruxsatnomasi arizasi **2 ish kunida**, eksport veterinariya sertifikati arizasi **7 ish kunida** ko'riladi (3-bob). Tranzit uchun ham ruxsatnoma bor (5-bob). | https://www.lex.uz/acts/-6427764 |
| L20 | Eksport nazorati to'g'risidagi qonun (658-II): eksport nazorati obyektlarini olib chiqish uchun **ruxsatnoma** kerak. Ro'yxatda bo'lmagan tovar qurolga ishlatilishi mumkinligi ma'lum bo'lsa ham majburiyat bor (catch-all). | https://lex.uz/uz/docs/-262949 |
| L21 | Raqamli markirovka (VM 737-son, 20.11.2020): agregatsiyalangan import kodi (AIK) BYDda ko'rsatilmasa, tovarni **"erkin muomalaga chiqarish (import)"ga rasmiylashtirish taqiqlanadi**. Markirovka majburiyati ishlab chiqaruvchi va importchida. | https://lex.uz/docs/-5115923 ; o'zgartirishlar: VM 23-son (23.01.2026) https://lex.uz/docs/-8012407 |

---

## 5. Rejimlar bo'yicha checklist

Ustunlar: **Vazifa** — broker amalda nima qiladi. **Asos** — §4'dagi L-raqam. **Holat**. **Spec/dizaynda qayerda**. **Nima qo'shish kerak**.

### 5A. Eksport (EK 10) — meva-sabzavot, to'qimachilik, paxta mahsulotlari

| # | Vazifa | Asos | Holat | Spec / dizaynda qayerda | Nima qo'shish kerak |
|---|---|---|---|---|---|
| A1 | To'g'ri rejimni tanlash: EK 10, EK 12 (vaqtincha olib chiqish) yoki EK 11 (reeksport) | §3, L4 | **Qisman** | `pg08.txt`: faqat "Import / Eksport" tugmalari; Y2 faqat posilka / yo'lovchi / tijorat | "Tovar qaytib keladimi? Ilgari import qilinganmi? Qayta ishlanadimi?" savollari va rejim kodiga xarita (5 va 7-bo'limlarga qarang) |
| A2 | Kontrakt yoki invoysni E-kontrakt (TSOYaEAT)ga kiritish | L13, L14 | **Qisman** | Y6, §6 6-qadam (importga yo'naltirilgan; "mandatory scope [UNVERIFIED]") | Eksport uchun checklist: VM 283 havolasi; meva-sabzavotda invoys asosida eksport qilish sharti (VM 163, 6-band); oldindan to'lovli kontraktda ma'lumotnoma rasmiylashtiruvgacha kiritiladi |
| A3 | Eksport tovari uchun TIF TN kodi | — | **Qisman** | Y10 (umumiy); kutubxonada "Quritilgan o'rik (eksport) 0813" (`pg25.txt`) | Eksportga xos tekshiruv: VM 163 qamrovi (07, 08, 0904, 1202) avtomatik belgilansin. To'qimachilik va paxta kodlari murakkab bo'lsa, "Odam kerak" bayrog'i |
| A4 | Eksport BYDsini to'ldirish va ed2 orqali topshirish | L1 | **Qisman** | Y12 "Phase 1: import and export"; mock to'ldirishda faqat "IM 40" bor (`all.txt`, mashq ekrani) | EK 10 grafalari xaritasi va mock'da eksport stsenariysi (masalan, quritilgan o'rik → Turkiya) |
| A5 | Eksport deklaratsiyasi tovar chiqib ketishidan oldin beriladi | spec: VM 605, 11-band | **Qamralgan** | §6 8-qadam | Muddat soatida ko'rsatish kifoya. VM 605 matnini huquq roli qayta o'qisin (bu auditda qayta ochilmadi) |
| A6 | Kelib chiqish sertifikati: ST-1 (MDH), A shakli (GSP), ST-UZ — "O'zbekekspertiza" | L16 | **Qisman** | Y5 (import uchun entitlement), Y21 "GSP+ only here"; `pg08.txt`dagi bo'sh havola | Eksport go/no-go'da "manzil davlati → kerakli shakl" qatori, rasmiy havola, 1 ish kunlik muddat. Marshrut maslahati bermaslik qoidasi saqlansin |
| A7 | Fitosanitariya sertifikati (meva-sabzavot, o'simlik mahsuloti) | L17, L1 | **Qisman** | §3 Phase 3 "phytosanitary permits"; Y7 umumiy; `pg08.txt` "fitosanitar talablar … qo'shiladi" | Eksport go/no-go: "har bir turkumga fito sertifikat"; Yagona darchada borligini tekshirish (bojxona o'zi tekshiradi — L1). Organning ariza muddati tasdiqlanmagan, ko'rsatilmasin |
| A8 | Veterinariya: eksport ruxsatnomasi va veterinariya sertifikati | L19 | **Yo'q** | Faqat umumiy "veterinary permits" (§3) | Go/no-go'da 2 qadam: ruxsatnoma (yillik, 2 ish kuni) va sertifikat (7 ish kuni). Rejalash soati yuk chiqishidan orqaga sanasin |
| A9 | Fumigatsiya, yog'och taglikda termo-muhr, ombor va muzlatgich talablari | L18 | **Yo'q** | — | Eksportchi uchun "qadoq va ombor" checklisti. Manzil davlati talab qilgan fumigatsiya → **Odam kerak** (karantin mutaxassisi) |
| A10 | Tez buziladigan yuk: qisqa saqlash muddati, tez yo'lak | L9 | **Qisman** | §6 8-qadam: "10 days for perishables (Art. 85)" (import vaqtincha saqlash uchun) | Eksportda tez yo'lak yoki "yashil yo'lak" qoidasi **tasdiqlanmagan**, uni va'da qilmaslik kerak. Eksport oqimida "tez buziladi" bayrog'i fito va kelib chiqish sertifikatini oldindan olishga undasin |
| A11 | Meva-sabzavotga xos qoidalar: tabiiy yo'qotish normalari, nohalol eksportchilar reyestri, minimal eksport narxi | L14, L15 | **Yo'q** | — | (a) yuk chiqishidan oldin "reyestrdamisiz?" tekshiruvi (rasmiy portal havolasi); (b) tabiiy yo'qotishni TSOYaEATga kiritish eslatmasi; (c) minimal narx ro'yxati faqat rasmiy manbadan (hozirgi ro'yxat **tasdiqlanmagan**) |
| A12 | Valyuta tushumi: 180 kun + jarima bosqichlari | L12 | **Qisman** | Y6 "currency-proceeds steps"; Y21 "Currency-proceeds rules belong with Y6"; Y8 soatlari ro'yxatida yo'q | Y8'ga "eksport sanasidan 180 kun" soati; 180+45 (kichik biznes 180+90) ogohlantirishi; 5/10/35% faqat lex.uz havolasi bilan |
| A13 | Eksportda QQS 0% shartlari | spec: Soliq kodeksi 258-modda | **Qisman** | §3, Y21 | Shartlar ro'yxati soliq mutaxassisi bilan. Bu auditda 258-modda qayta o'qilmadi |
| A14 | Eksport bojxona yig'imi (VM 55 bandlari) | L10 | **Qamralgan** | Y11, §8.3 | VM 55 eksport va import yig'im stavkalarini bir xillashtiradi; engine ikkalasiga ham qo'llasin |
| A15 | Asl belgisi: eksportda markirovka kodlarini aylanmadan chiqarish | L21 | **Odam kerak** | Y7 faqat import tomonini aytadi | Eksportdagi aniq tartib **tasdiqlanmagan**. Markirovkalangan tovar eksport qilinsa → brokerga yoki markirovka operatoriga |
| A16 | Paxta va to'qimachilik: eksport cheklovlari, manzil davlati sertifikatlari, Yevropa Ittifoqi GSP+ uchun REX | — | **Odam kerak** | Y21 GSP+ (umumiy) | Paxta tolasi eksportiga cheklov va REX talabi **tasdiqlanmagan**. Paxta va paxta mahsulotlari kodlariga avtomatik "mutaxassis tekshirsin" bayrog'i |
| A17 | Manzil davlati talablari (pestitsid qoldig'i, import ruxsatnomasi, yorliq) | — | **Odam kerak** | — | Lex.uz doirasidan tashqarida, **tasdiqlanmagan**. YuklaGo "xaridordan import talablarini so'rang" shablonini bersin, qarorni o'zi chiqarmasin |

### 5B. Reeksport (EK 11)

| # | Vazifa | Asos | Holat | Spec / dizaynda | Nima qo'shish kerak |
|---|---|---|---|---|---|
| B1 | Rejim shartlari: identifikatsiya; ilgari import qilingan tovar ishlatilmagan va o'zgarmagan | L2 (33-modda) | **Yo'q** | §3 Phase 2, Y22 → Y18 | Rejim savollarida "ilgari import qilinganmi, ishlatilganmi" tarmog'i; qo'llab-quvvatlanmasa brokerga |
| B2 | Hujjatlar: BYD va kuzatuv hujjatlari; ruxsat hujjatlarini bojxona o'zi tekshiradi | L2 (34-modda) | **Yo'q** | — | Phase 2'da hujjatlar shabloni |
| B3 | 3 ish kunida tranzit deklaratsiyasi, aks holda vaqtincha saqlash | L2 (32-modda) | **Yo'q** | Y8'da yo'q | Y8'ga "reeksport → 3 ish kuni" soati (ish kunlari kalendari bilan) |
| B4 | Importda to'langan boj va soliqni qaytarish (2 yil, ishlatilmagan) | L2 (35-modda) | **Odam kerak** | §3 "duty drawback must not be described…" | Muhim: 35-modda **qaytarishni nazarda tutadi** (shartli). "Qaytarish imkoniyati bo'lishi mumkin — broker yoki huquqshunos tekshirsin" yozuvi; summa hisoblanmasin |
| B5 | Reeksportda kelib chiqish va fitosanitariya hujjatlari | L16 (994 reeksportni ham qamraydi) | **Yo'q** | — | Reeksport fito-sertifikati turi bor deb ko'rinadi, lekin faqat nrm.uz manbasida (**tasdiqlanmagan**) |

### 5C. Vaqtincha olib kirish (IM 42) va vaqtincha olib chiqish (EK 12)

| # | Vazifa | Asos | Holat | Spec / dizaynda | Nima qo'shish kerak |
|---|---|---|---|---|---|
| C1 | Rejimni tanlash (ko'rgazma, uskuna, ijara, lizing) | L3 | **Yo'q** | Y2 va `pg08.txt`da tarmoq yo'q | Rejim savollari. Hozir xavf bor: foydalanuvchi IM 40 bilan to'liq boj to'lab yuboradi |
| C2 | Shartlar: identifikatsiya, ruxsatnoma, o'zgarmas holat; taqiqlangan toifalar (xom ashyo, sarf materiallari, chiqindi va h.k.) | L3 (62-modda) | **Yo'q** | — | Taqiq ro'yxati bo'yicha "mumkin emas" qoidasi |
| C3 | Hujjatlar: BYD, kuzatuv hujjatlari, kontrakt (ijara, lizing) | L3 (63-modda) | **Yo'q** | — | Hujjat shabloni |
| C4 | Muddat 2 yil, uzaytirish holatlari, muddat o'tgan kunning ertasigacha tugallash | L3 (64, 69-moddalar) | **Yo'q** | Y8'da yo'q | Y8: "vaqtincha olib kirish tugashiga 60/30/7 kun qoldi" eslatmalari (eslatma oraliqlari mahsulot qarori, qonuniy muddat emas) |
| C5 | To'liq shartli ozod qilish (VM 212 ro'yxati) yoki davriy to'lov (oyiga 5%) | L3 (65, 66-moddalar) | **Yo'q** | Y11 faqat import formulasi | Engine'ga davriy to'lov formulasi. VM 212 ro'yxati tarif mutaxassisi tomonidan yuklansin |
| C6 | To'lov ta'minoti (kafolat) hajmi va shakli | — | **Odam kerak** | — | Ta'minot qoidalari bu auditda o'qilmadi (**tasdiqlanmagan**) → broker |
| C7 | ATA karneti | L11 (ATA tranzit deklaratsiyasi sifatida) | **Odam kerak** | — | Tushuntirish matni va brokerga yo'naltirish |
| C8 | Vaqtincha olib chiqish (2 yil) va reimport (3 yil) | L4 | **Yo'q** | §3 Phase 3 "Re-import" | Eksport oqimida "qaytib keladimi?" savoli bo'lsa EK 12 tavsiya qilinsin |

### 5D. Qayta ishlash: hududda (IM 51) va hududdan tashqarida (EK 61)

| # | Vazifa | Asos | Holat | Spec / dizaynda | Nima qo'shish kerak |
|---|---|---|---|---|---|
| D1 | Bojxonadan qayta ishlash ruxsatnomasini olish | L5, L6 | **Odam kerak** | §3 Phase 2; persona "Manufacturers" (§2) | Rejim aniqlansa, darhol brokerga. YuklaGo ariza uchun hujjatlar ro'yxatini tayyorlasin |
| D2 | Chiqish normasi (texnologik hujjatlar asosida) | L5 (76-modda) | **Odam kerak** | — | Norma hech qachon LLM tomonidan taklif qilinmasin. Faqat foydalanuvchi va mutaxassis kiritadi |
| D3 | Identifikatsiya usuli, qoldiq va chiqindilar | L5 (72, 74, 79-moddalar) | **Odam kerak** | — | Paketda maydon sifatida |
| D4 | Muddatlar: ruxsatnoma 2 yil (5 yilgacha); tashqarida uzaytirish arizasi kamida 1 oy oldin | L5, L6 | **Yo'q** | Y8'da yo'q | Y8 soatlari |
| D5 | Rejimni tugallash va qayta ishlash mahsulotini hisobga olish | 80-modda (sarlavha) | **Odam kerak** | — | Kelajakda "norma bo'yicha xom ashyo sarfi" jadvali (kuzatuv vositasi sifatida) |
| D6 | Yig'im: bir deklaratsiya uchun BHMning 25 foizi | L10 | **Yo'q** | Y11 faqat qiymat bandlari | Engine'ga qat'iy stavka qatori |
| D7 | E-kontrakt: qayta ishlash mahsuloti eksporti | L13 (VM 283'da eslatilgan) | **Yo'q** | — | Phase 2 checklistiga |

### 5E. Tranzit (TR 80)

| # | Vazifa | Asos | Holat | Spec / dizaynda | Nima qo'shish kerak |
|---|---|---|---|---|---|
| E1 | Kim deklarant: odatda tashuvchi | `deklarant-jarayoni.md` (30-qator) | **Yo'q** | Persona — tovar egasi (§2) | Tranzit — ekspeditor va tashuvchi ishi. YuklaGo uni "tushuntir + yo'naltir" bilan cheklasin. Deklarant qoidasining Kodeksdagi moddasi bu auditda alohida o'qilmadi |
| E2 | Tranzit deklaratsiyasi "E-Tranzit" yoki us-uz.gov.uz orqali | L11 | **Yo'q** | §9 7-band: "role of us-uz.gov.uz" ochiq savol | Ochiq savolni yopish mumkin: VM 737 bu ikki tizimni nomlaydi |
| E3 | TIR daftarchasi va ATA karneti | L11 | **Odam kerak** | — | Tushuntirish va brokerga yo'naltirish |
| E4 | To'lov ta'minoti (qonunchilikdagi ro'yxat bo'yicha) | L7 (117-modda) | **Odam kerak** | — | Ro'yxatning o'zi bu auditda o'qilmadi (**tasdiqlanmagan**) |
| E5 | Tranzit ruxsatnomalari (shu jumladan veterinariya tranziti) | L7, L19 | **Yo'q** | — | Go/no-go'ni tranzitga moslash |
| E6 | Muddatlar: havo 3 kun; yer va suv 1000 km uchun 15 kun | L7 (120-modda) | **Yo'q** | Y8'da yo'q | Y8: masofa va transport turiga qarab soat |
| E7 | Yig'im 25% BHM, o'zgartirish 10% BHM | L10 | **Yo'q** | Y11 | Engine qatorlari |
| E8 | NCTSga o'xshash elektron tranzit | L11 | **Yo'q** | — | O'zbekistonda bu vazifani E-Tranzit bajaradi. "NCTS" nomi ishlatilmasin (ekvivalentlik **tasdiqlanmagan**) |

### 5F. Nazoratdagi tovarlar (sertifikatlar, ruxsatnomalar, Asl belgisi, litsenziya, ikki xil maqsad)

| # | Vazifa | Asos | Holat | Spec / dizaynda | Nima qo'shish kerak |
|---|---|---|---|---|---|
| F1 | Yagona darchadagi ruxsat hujjatlari (bojxona o'zi tekshiradi) | L1 | **Qamralgan** (import) | Y7, `pg12.txt` "Yagona darcha orqali ruxsatnoma · Rasmiy ro'yxat" | Eksport, reeksport va tranzitga ham kengaytirish |
| F2 | Muvofiqlik sertifikati (import) | — | **Qamralgan** | `pg12.txt`; javob tushuntiruvchi 44-grafa misoli (`all.txt`) | Yaxshi. Ro'yxat manbasi `[v2 spec, "Ruxsatnomalar manbalari"]` bo'sh havola — to'ldirilsin |
| F3 | Asl belgisi: importda AIKni BYDga yozish | L21 | **Qisman** | Y7 marking bayrog'i; `pg12.txt` "Raqamli markirovka … talab qilinmaydi" | Markirovkalanadigan tovarda "AIK raqami" majburiy maydoni va operatordan AIK so'rash qadami. Ayrim guruhlar uchun BYDdan keyin 5 kun ichida operatorga xabarnoma talabi bor (VM 23-son matnida), lekin qaysi guruhlarga tegishli — **tasdiqlanmagan** |
| F4 | Maxsus tovarlar litsenziyasi | — | **Odam kerak** | Y7 "licensed … escalate", Y18 | Yo'naltirish to'g'ri. Litsenziya ro'yxati manbasi nomlansin (PF-5215 bu auditda o'qilmadi — **tasdiqlanmagan**) |
| F5 | Eksport nazorati va ikki xil maqsadli tovarlar | L20 | **Odam kerak** | §3, Y7 "dual-use → escalate"; dizaynda dron misoli brokerga (`all.txt`) | Yo'naltirish to'g'ri. "Oxirgi foydalanuvchi harbiy bo'lishi mumkinmi?" catch-all savoli qo'shilsin |
| F6 | Importdagi veterinariya va fito ruxsatnomalari | L19, L17 | **Qisman** | Y7 umumiy | Import muddatlari (VM 148, 4-bob) go/no-go'ga |
| F7 | Kvotalar | — | **Odam kerak** | §3 "quotas" | Hozirgi kvotalar **tasdiqlanmagan**. Faqat brokerga yo'naltirish |

**Sanoq (52 vazifa):** Qamralgan 4 (A5, A14, F1, F2); Qisman 11; Yo'q 22; Odam kerak 15.

---

## 6. Odam (broker yoki mutaxassis) kerak bo'lgan holatlar va spec ularni to'g'ri yo'naltiradimi

Specdagi yo'naltirish sabablari (Y18, §6 12-qadam): past ishonch, qo'llab-quvvatlanmagan rejim, nazoratdagi tovar, bahsli qiymat, hal qilinmagan hujjat ziddiyati, foydalanuvchi xohishi. Dizayndagi "Brokerga topshirish" tugmasi har ekranda bor (`pg26.txt`, `design-rationale.md` §3). Bu **yaxshi asos**.

**Muammo:** yo'naltirish faqat tizim rejimni **bilgan** taqdirda ishlaydi. Rejimni aniqlovchi savol yo'q, shuning uchun "qo'llab-quvvatlanmagan rejim" sababi deyarli hech qachon ishga tushmaydi.

| Holat | Nega odam kerak | Spec yo'naltiradimi? |
|---|---|---|
| Qayta ishlash ruxsatnomasi va chiqish normasi (D1–D5) | Texnologik hujjat va bojxona bilan kelishuv | Qisman: "unsupported regime" orqali, lekin rejim aniqlanmaydi |
| Reeksportda boj va soliqni qaytarish (B4) | 49-bob tartibi, shartlarni isbotlash | Yo'q: spec hatto "qaytarish yo'q" degan taassurot beradi |
| Vaqtincha olib kirishda ta'minot, ATA, uzaytirish (C6, C7) | Kafolat va ariza | Yo'q (rejim aniqlanmaydi) |
| Tranzit, TIR, ta'minot (E1, E3, E4) | Tashuvchi va ekspeditor ishi | Yo'q |
| Bahsli TIF TN (masalan, to'qimachilik aralash tolalari) | Dastlabki qaror (VM 55: BHMning 75 foizi) yoki ekspertiza | Ha: Y10 dastlabki qaror yo'lini taklif qiladi |
| Litsenziya, ikki xil maqsad, kvota (F4, F5, F7) | Ruxsat beruvchi organ | Ha: Y7 va Y18 |
| Paxta va strategik tovar eksporti (A16) | Cheklovlar tasdiqlanmagan | Yo'q: alohida bayroq yo'q |
| Manzil davlati talablari va fumigatsiya (A9, A17) | Lex.uz doirasidan tashqarida | Yo'q |
| Eksportda Asl belgisi (A15) | Tartib aniq emas | Yo'q |
| Fitosanitariya laboratoriya xulosasi salbiy chiqsa | Karantin inspektori qarori | Yo'q: javob tushuntiruvchida (Y19) bunday shablon yo'q |

**Tavsiya:** Y18'ga "rejimga xos sabablar" ro'yxati qo'shilsin va broker paketida **tuzilgan sabab kodi** bo'lsin (hozir `pg26.txt`da faqat erkin matnli "Sabab (broker uchun eslatma)" maydoni bor).

---

## 7. Ustuvor 7 ta kamchilik va aniq tuzatish

1. **Rejimni aniqlovchi savollar yo'q** (A1, C1, B1).
   *Tuzatish:* "Yangi yuk" (`pg08.txt`) ekraniga 4–5 savoldan iborat daraxt qo'shilsin: yo'nalish → tovar qaytadimi → ilgari import qilinganmi → qayta ishlanadimi → O'zbekistondan faqat o'tadimi. Natija 2773-son kodiga (10/11/12/40/41/42/51/61/80) bog'lansin. Qo'llab-quvvatlanmagan kod chiqsa, oddiy tilda tushuntirish va brokerga paket. Bu Phase 2'ni qurmasdan turib xavfsizlikni oshiradi.

2. **Eksport yo'li faqat nomda bor** (A2–A8; `pg08.txt`dagi `[v2 spec, "Eksport"]` bo'sh havola; Y21 "Medium").
   *Tuzatish:* specga "Eksport (EK 10)" bo'limi yozilsin: hujjatlar, E-kontrakt (L13/L14), kelib chiqish (L16), fito (L17), vet (L19), qadoq (L18), valyuta (L12). Dizaynda 3 ta ekran: eksport go/no-go, eksport hujjatlari, tushum soati. Y21 Phase 1 bilan bir xil ustuvorlikka ko'tarilsin, yoki §3 "Phase 1 = faqat import" deb halol yozilsin.

3. **Valyuta tushumi soati yo'q** (A12).
   *Tuzatish:* Y8'ga "eksport rasmiylashtirilgan sanadan 180 kun" soati. 180+45 (kichik tadbirkorlik uchun 180+90) kunda qizil ogohlantirish. Jarima foizlari (5/10/35%) faqat L12 havolasi bilan ko'rsatilsin. Meva-sabzavot eksportchisi uchun "nohalol eksportchilar reyestri" xavfi (L14) shu soat yonida ko'rsatilsin.

4. **Fito, vet va kelib chiqish sertifikatlari rasmiy muddatlarsiz** (A6–A9).
   *Tuzatish:* go/no-go'da eksport bloki: kelib chiqish (1 ish kuni, O'zbekekspertiza), vet ruxsatnoma (2 ish kuni, yillik) va vet sertifikat (7 ish kuni), fito (har bir turkum). Sertifikat qachon kerakligi yuk chiqish sanasidan orqaga sanalsin. Tez buziladigan yuk uchun "yig'im-terimdan oldin tayyorlang" eslatmasi. Tasdiqlanmagan muddatlar (fito arizasi) ko'rsatilmasin.

5. **Hisoblash engine'i faqat import formulasini biladi** (C5, D6, E7, B4).
   *Tuzatish:* §8.3'ga qatorlar qo'shilsin: tranzit va qayta ishlash uchun 25% BHM (L10); tranzit deklaratsiyasini o'zgartirish 10% BHM; vaqtincha olib kirishda davriy to'lov oyiga 5% (L3). Reeksportda qaytarish summasi **hisoblanmasin**, faqat "qaytarish imkoniyati bor, broker tekshirsin" deyilsin.

6. **Rejimlarga xos muddat soatlari yo'q** (B3, C4, D4, E6).
   *Tuzatish:* Y8 ro'yxatiga qo'shilsin: reeksport → tranzit deklaratsiyasi 3 ish kuni (32-m.); vaqtincha olib kirish 2 yil va ertasi kuni tugallash (64, 69-m.); vaqtincha olib chiqish 2 yil (39-m.); reimport 3 yil (59-m.); qayta ishlash ruxsatnomasi 2 yil, tashqarida uzaytirish arizasi kamida 1 oy oldin (47, 75-m.); tranzit havo 3 kun, yer 1000 km uchun 15 kun (120-m.). Phase 2'gacha bu soatlar "kuzatuv" sifatida ham foydali: foydalanuvchi deklaratsiyani broker orqali bersa ham, muddatni YuklaGo eslatadi.

7. **Asl belgisi va nazorat qoidalari faqat bayroq darajasida** (F3, A15, F5).
   *Tuzatish:* markirovkalanadigan tovarda "AIK raqami" maydoni va "AIKsiz IM 40 qabul qilinmaydi" bloki (L21). Ikki xil maqsad uchun catch-all savoli (L20). Markirovkalangan tovar eksportida "Odam kerak". Rasmiy guruh ro'yxati Asl belgisi operatoridan sanali holda yuklansin (spec §8.5 talabi bilan bir xil).

**Qo'shimcha tezkor tuzatishlar:**
- Mock portalda faqat "IM 40" bor, eksport stsenariysi qo'shilsin.
- Spec §9 7-banddagi "role of us-uz.gov.uz" ochiq savoli VM 737 bilan yopilsin.
- Spec §3'dagi "duty drawback" iborasi 35-modda (reeksportda qaytarish) bilan muvofiqlashtirilsin.

---

## 8. Strategik variantlar

**Variant A — "Import + oddiy eksport" (halol Phase 1).**
Faqat IM 40 va EK 10 to'liq qilinadi. Fokus — meva-sabzavot va to'qimachilik eksportchisi: E-kontrakt, kelib chiqish, fito/vet, 180 kun. Qolgan hamma rejimlar savollar orqali aniqlanadi va brokerga beriladi.
*Afzalligi:* tez, lex.uz bilan to'liq tasdiqlangan qoidalar, fermer va eksportchi segmenti ochiladi.
*Kamchiligi:* "barcha rejimlar" vizyoni kechikadi.

**Variant B — "Broker bilan birga" (Phase 2 rejimlari uchun).**
Reeksport, vaqtincha olib kirish, qayta ishlash va tranzitda YuklaGo paket, muddat soatlari va hisob-kitoblarni tayyorlaydi. Deklaratsiyani litsenziyali hamkor broker beradi va imzolaydi.
*Afzalligi:* §9 2-banddagi "YuklaGo o'zi broker faoliyatimi?" xavfini kamaytiradi; murakkab ishlar sifatli bajariladi; brokerlar raqib emas, kanal bo'ladi.
*Kamchiligi:* hamkorlik shartnomalari va daromad taqsimoti kerak.

**Variant C — "Rejim majburiyatlari kuzatuvchisi".**
Maxsus rejimlarni to'ldirish o'rniga, rejimdan **keyingi** majburiyatlarni kuzatish: vaqtincha olib kirish muddati, qayta ishlash ruxsatnomasi va norma bo'yicha sarf, reeksport muddati, valyuta tushumi.
*Afzalligi:* ed2 avtomatlashtirishga bog'liq emas (huquqiy xavf past), har oy qaytib keladigan foydalanuvchi, deklaratsiyani kim berganidan qat'i nazar ishlaydi.
*Kamchiligi:* "brokerni almashtiradi" degan bosh g'oyadan chetroq.

**Tavsiya:** A + C birga. B esa qayta ishlash va tranzit uchun hamkorlik sifatida.

---

## 9. Tasdiqlanmagan da'volar (bu auditda lex.uz'da tasdiqlay olmadim)

- Reeksport tovarini "deklaratsiya qabul qilingandan **6 oy** ichida" olib chiqish talabi. Bu ibora 32-modda sahifasida uchraydi, lekin yangi tahrir 218-modda muddatlariga havola beradi. Qaysi biri amalda ekani **tasdiqlanmagan**.
- Vaqtincha olib kirishda ta'minot (kafolat) hajmi va shakli; VM 212-son ro'yxatining amaldagi tarkibi (qaror nomi Kodeks izohida bor, matni o'qilmadi).
- Tranzitda faqat ta'minot bilan o'tadigan tovarlar ro'yxati (117-modda ishora qiladi, ro'yxat o'qilmadi).
- Tranzitda deklarant tashuvchi ekani — `deklarant-jarayoni.md`dan olingan, Kodeks moddasi alohida tekshirilmadi.
- Fitosanitariya sertifikati arizasini ko'rib chiqish muddati, eksportdan necha kun oldin xabar berish talabi (qidiruv xulosasida "30 kun / 15 kun" deyilgan, lex.uz matnida topilmadi).
- Reeksport fitosanitariya sertifikati turi (faqat nrm.uz'da ko'rindi).
- Meva-sabzavot uchun hozirgi minimal eksport narxlari ro'yxati va PQ-107 ning amaldagi holati.
- Tez buziladigan eksport uchun "yashil yo'lak" yoki tez yo'lak qoidasi.
- Paxta tolasi va paxta mahsulotlari eksportiga cheklovlar.
- Yevropa Ittifoqi GSP+ uchun REX (ro'yxatdan o'tgan eksportchi) talabi (YeI qoidasi, lex.uz emas).
- Kelib chiqish sertifikati narxi (yangilikda "0,2–1,9 BHM" deyilgan, Nizom ilovasi o'qilmadi).
- Eksportda Asl belgisi kodlarini aylanmadan chiqarish tartibi; importdagi "5 kunlik xabarnoma" qaysi tovar guruhlariga tegishli ekani.
- Maxsus tovarlar litsenziyasi tartibi (PF-5215, 2017) va hozirgi kvotalar.
- PF-228 bo'yicha "5% gacha tushmagan summa debitorlik hisoblanmaydi" qoidasi (customs.uz'da bor, lex.uz'da o'qilmadi).
- E-kontraktga kiritish har qanday holatda majburiymi (customs.uz "har qanday turdagi shartnoma, invoys ham" deydi; lex.uz'da faqat yuqoridagi xususiy bandlar o'qildi).
- Eksportda QQS 0% shartlari (Soliq kodeksi 258-modda) va VM 605 11-band (eksport deklaratsiyasi muddati) — spec manbalari, bu auditda qayta ochilmadi.
- O'zbekistonda NCTSga to'liq ekvivalent tizim bor-yo'qligi (E-Tranzit mavjud, ekvivalentlik tasdiqlanmagan).

---

## 10. Spec va dizayn ichidagi ziddiyatlar

1. §3 "Phase 1 = import + eksport", Y21 esa "Medium, importdan keyin". Dizaynda eksport ekrani yo'q.
2. `pg08.txt` `[v2 spec, "Eksport"]` va `pg12.txt` `[v2 spec, "Ruxsatnomalar manbalari"]`ga havola beradi — specda bunday bo'limlar yo'q.
3. Spec §3 "duty drawback"ni ehtiyotkorlik bilan rad etadi, lekin Bojxona kodeksi 35-moddasi reeksportda shartli qaytarishni nazarda tutadi. Mahsulot matni "qaytarish yo'q" demasin, "broker tekshirsin" desin.
4. Spec §9 7-band us-uz.gov.uz rolini ochiq savol deydi; VM 737 uni tranzit deklaratsiyasi kanali sifatida nomlaydi.
5. Shapkadagi muddat soati (`pg02.txt`: "Deklaratsiya: 9 kun · Saqlash: [N] kun") faqat importga mos. Eksport yukida (YG-0402, `all.txt`) qaysi soat ko'rinishi belgilanmagan.

*Hisobot oxiri.*

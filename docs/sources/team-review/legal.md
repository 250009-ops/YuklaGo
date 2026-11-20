# YuklaGo — huquqiy ko'rib chiqish (legal review)

*Tayyorlandi: 2026-yil 18-noyabr; yangilandi: 2026-yil 19-noyabr (xavfsizlik jamoasining 3 ta eslatmasi tekshirildi), Toshkent vaqti (UTC+5). Rol: "Bojxona Huquq va IT Integratsiya".*
*Bu yuridik xulosa emas. Har bir modda lex.uz'dagi joriy matndan shu kuni o'qildi. Tekshira olmaganim **aniq emas** deb belgilangan.*
*Ko'rib chiqilgan fayllar: `/workspace/hackathon/yuklago-spec-v2.md`, `/workspace/hackathon/design-v0.1/design-rationale.md`, `/workspace/hackathon/design-v0.1/yuklago-web-ui-v0.1.pdf` (28 bet), xavfsizlik jamoasining `/workspace/yuklago-security/legal.md` fayli. `team-review/` papkasida xavfsizlik jamoasining fayli yo'q edi, shuning uchun ularning `/workspace/yuklago-security/legal.md` fayliga moslashtirdim (pastdagi "Xavfsizlik jamoasi savollariga javoblar" va "Kelishuv / farqlar" bo'limlari).*

---

## Xulosa

| Savol | Hukm | Asosiy manba |
|---|---|---|
| 1. Foydalanuvchining **o'z** ed2 kabinetini u ko'rib turganida avtomatik to'ldirish, imzoni u o'zi qo'yadi | **Shartli ruxsat / kulrang zona.** Taqiqlovchi norma topilmadi, lekin ruxsat beruvchi rasmiy qoida ham yo'q. Haqiqiy kabinet faqat quyidagi shartlar bilan va Bojxona qo'mitasidan yozma javob olingandan keyin. Demoda — faqat mock. | BK 275-modda; VM 605-son 15-, 28-bandlar; ERI qonuni 27-modda; 560-II 12-modda; JK 278-2, 278-3; MJtK 155-1 |
| 2. Pulli deklaratsiya tayyorlash broker faoliyatimi? | **Dastur (SaaS), unda deklarant o'zi to'ldirib, o'z ERI'si bilan imzolab o'zi yuborsa — ehtimol broker emas (aniq emas). YuklaGo yoki uning xodimi mijoz nomidan rasmiylashtirsa, imzolasa, yuborsa yoki mijozning ro'yxatiga broker/ishonchli shaxs bo'lib kirsa — bu broker faoliyati.** Broker xabarnoma tartibida ishlaydi. Xabarnomasiz ishlasa 20 BHM jarima bor. | BK 15, 277-moddalar; ZRU-701 3-ilova 35-poz., 4-ilova III 28-poz.; VM 847-son 32-ilova |
| 3. Shaxsga doir ma'lumot va xorijiy LLM | 2026-yil 27-martdan O'zbekistonda saqlash **majburiyati** faqat biometrik, genetik va telekom abonentlari ma'lumotlariga tegishli. Qolgan ma'lumotni chet elga uzatish: (a) VM 415-son ro'yxatidagi davlatga mumkin — asos ZRU-547 15-modda 2-qismi (VM 415 4-band 1-xatboshi faqat xalqaro kelishuv asosidagi tizimlar uchun); AQSh — faqat DPF kompaniyalari uchun, OpenAI va Anthropic DPF'da yo'q (tasdiqlandi, 19.11.2026); oddiy uzatish uchun vakolatli organni xabardor qilish talabi topilmadi, faqat sizib chiqishda 24/72 soat; (b) aks holda subyektning roziligi bilan yoki vakolatli organ shartlari bajarilganda. MJtK 46-2 matni eski, lekin u blanket norma va qonun talabiga tayanadi. Amalda yangi ZRU-547 tahriri qo'llanadi. Baribir O'zbekistonda hosting + redaksiya + rozilik tavsiya etiladi. | ZRU-547 15, 20, 26, 27-1-moddalar; ZRU-1125; VM 415-son; MJtK 46-2; ZRU-682 18-modda |
| 4. Spec va dizayndagi muddat/javobgarlik matnlari | Asosiy muddatlar to'g'ri: 15 kalendar kun, 60/10 kun, 30 kun, 3/8 soat, 1 ish kuni, 3 yil. Bir nechta xato bor: "vakolatli mutaxassis sifatida ro'yxatdan o'tgan", "227-22 og'ir holatlarda", "277–281-moddalar", PF-5414 havolasi 404. Rozilik va LLM bildirishnomasi ekranlari yo'q. | BK 85, 206, 248, 261, 262, 266-moddalar; VM 605-son 11, 11-1, 15-bandlar |

**Eng muhim 5 ta tuzatish:** (1) "Tez" rejimni haqiqiy kabinet uchun olib tashlash yoki imzodan oldin to'liq ko'rib chiqishni majburiy qilish; (2) "vakolatli mutaxassis sifatida ro'yxatdan o'tgan" → "kabinetingizdagi TIF ishtirokchilari ro'yxatiga siz kiritgan shaxs"; (3) muddat ekranida manba: "BK 261-modda — 15 kalendar kun, kechiktirmay" va hisoblash izohi; (4) shaxsiy ma'lumot va xorijiy AI uchun rozilik ekrani qo'shish; (5) hech bir joyda "rasmiylashtirib beramiz", "broker o'rnini bosamiz", "siz uchun topshiramiz" demaslik.

---

## 1. ed2.customs.uz'ni avtomatlashtirish (foydalanuvchining o'z kabineti, o'z ERI'si)

**Nimalar tasdiqlandi:**
- Deklarant elektron deklaratsiya uchun bojxona axborot tizimlaridan foydalanishga haqli. U hujjat loyihalarini ham tayyorlay oladi (BK 275-modda). [lex.uz/docs/2876354](https://lex.uz/docs/2876354)
- Kim imzolaydi: "TEDni imzolash vakolatiga ega jismoniy shaxs (ERI kaliti egasi)" — ma'lumotlarni o'z ERI'si bilan tasdiqlovchi shaxs (VM 605-son Nizomi, 28-band). Deklaratsiyani "deklaratsiyalovchi shaxs" o'z ERI'si bilan tasdiqlab, BQ YaAAT orqali yuboradi (15-band). [lex.uz/docs/3844549](https://lex.uz/docs/3844549)
- ERI qonuni: kalit egasi yopiq kalit xavfsizligi uchun "barcha mumkin bo'lgan choralarni ko'rishi" va kalitdan boshqalar foydalanayotganini bilsa, darhol xabar berishi shart. Yuridik shaxsda kalitdan foydalanishga rahbar mas'ul (ZRU-793, 27-modda). "Kalitni berish taqiqlanadi" degan so'zma-so'z norma topmadim, lekin 27-modda mazmunan kalitni boshqaga berishga yo'l qo'ymaydi. [lex.uz/docs/6234904](https://lex.uz/docs/6234904)
- Axborot resursidan ma'lumot olish tartibini resurs egasi belgilaydi; resursga kirish tartibi va shartlarini ega foydalanuvchiga bepul taqdim etadi (560-II, 12-modda). [lex.uz/docs/82956](https://lex.uz/docs/82956)
- Jinoiy: JK 278-2 (ruxsatsiz foydalanish, oqibat bilan), 278-3 (ruxsatsiz kirish uchun maxsus dastur/qurilma tayyorlash yoki tarqatish), 278-4 (bila turib yolg'on axborot kiritish, katta zarar bilan), 278-5, 278-6, 278-7 — hammasi mavjud. Ma'muriy: MJtK 155-1 — "foydalanishga ruxsati bo'lgan shaxs"ning belgilangan foydalanish qoidalarini buzishi, axborot yo'q qilinishi/modifikatsiyasiga olib kelsa. [JK](https://lex.uz/docs/111453), [MJtK](https://lex.uz/docs/97664)
- ed2 uchun e'lon qilingan foydalanish shartlari yoki uchinchi tomon dasturini taqiqlovchi qoida — **topilmadi** (xavfsizlik jamoasi ham topmagan; yo'qligini isbotlab bo'lmaydi → aniq emas).

**Mantiq:** foydalanuvchi o'z kabinetiga o'zi kiradi va o'zi imzolaydi. YuklaGo esa uning kompyuterida, uning ko'z o'ngida maydonlarga yozadi. Bu holat "ruxsatsiz foydalanish"ga (278-2) mantiqan to'g'ri kelmaydi, chunki ruxsatli shaxs o'z sessiyasida ishlaydi. Xavf uch joyda: (a) himoyani chetlab o'tish (captcha, token tekshiruvi, rate-limit) → 278-3; (b) sayt egasi keyin "avtomatlashtirish taqiqlanadi" desa → 155-1 (foydalanuvchiga); (c) noto'g'ri ma'lumot yozilib qolsa → BK 276, MJtK 227-22 (deklarantga).

**Hukm: shartli ruxsat (kulrang zona).** Shartlar:
1. Kirish (login) va imzoni **faqat foydalanuvchi** o'zi bajaradi. Har bir deklaratsiya alohida imzolanadi. "Hammasini bir marta imzolash" degan funksiya yo'q.
2. ERI fayli, PIN, parol, sessiya cookie'lari YuklaGo'da saqlanmaydi, serverga yuborilmaydi, avtomatika ularni kiritmaydi (ERI qonuni 27-modda).
3. Imzo tugmasidan oldin foydalanuvchi **butun** qoralamani ko'radi va "ko'rib chiqdim" deb belgilaydi. Shuning uchun "Tez" rejim haqiqiy kabinetda ishlamasin, yoki imzodan oldin majburiy to'liq xulosa sahifasi ko'rsatilsin.
4. Yashirin oyna, fon rejimi, foydalanuvchi yo'qligida ishlash yo'q. Inson tezligiga yaqin, cheklangan so'rovlar. Captcha, token yoki boshqa himoyani chetlab o'tish **mutlaqo yo'q** (JK 278-3).
5. Sahifa o'zgarsa — to'xtash ("fail closed"); hech qachon taxmin bilan yozmaslik (278-4: "bila turib yolg'on axborot").
6. Ish faqat foydalanuvchining o'z kompyuterida bo'ladi. Uchinchi shaxs kabinetiga xizmat sifatida kirish yo'q (bu 2-savolga tegadi).
7. Bojxona qo'mitasiga rasmiy so'rov yuborish (xat loyihasi pastda). Javob kelguncha ommaviy demoda — faqat mock portal.
8. Agar Bojxona qo'mitasi taqiqlasa yoki texnik bloklasa — darhol "nusxalash yordamchisi" va XML eksportga o'tish.

---

## 2. Pulli tayyorlash broker faoliyatimi?

**Ta'rif (BK 15-modda):** "bojxona brokeri — bojxona rasmiylashtiruvi bo'yicha operatsiyalarni deklarantning yoki vakolatli shaxsning **topshirig'iga binoan va uning nomidan shartnoma asosida** amalga oshiradigan O'zbekiston yuridik shaxsi". **BK 277-modda:** broker faoliyati — bojxona operatsiyalarini deklarant topshirig'i bilan va uning nomidan amalga oshirish; munosabatlar shartnoma asosida. Brokerning 281–282-moddalardagi huquq va majburiyatlarini shartnoma bilan cheklab bo'lmaydi (277-modda). Diqqat: 278–280- va 283-moddalar 2018-yilda ZRU-494 bilan kuchini yo'qotgan. [lex.uz/docs/2876354](https://lex.uz/docs/2876354)

**Bojxona kodeksida "bojxona vakili" degan alohida atama topmadim.** Kodeksdagi atamalar: "bojxona brokeri" va "bojxona rasmiylashtiruvi bo'yicha mutaxassis" (284-modda: broker yoki boshqa yuridik shaxs bilan mehnat shartnomasi tuzib, uning nomidan ishlaydigan jismoniy shaxs).

**Amaliy mexanizm (VM 605-son, 15-band):** deklarant TIF ishtirokchisi kabinetida ro'yxatga **"ishonch bildirgan shaxs, bojxona brokeri yoki o'z shtatidagi mutaxassis"**ni va ularning vakolat muddatini kiritadi. Shu ro'yxatdagi shaxs TEDni o'z ERI'si bilan imzolab yuboradi. [lex.uz/docs/3844549](https://lex.uz/docs/3844549)

**Xabarnoma tartibi (tasdiqlandi):**
- ZRU-701, 3-ilova, 35-pozitsiya: "Bojxona brokeri faoliyatini boshlaganlik yoki tugatganlik to'g'risida xabarnoma" — Bojxona qo'mitasiga. 4-ilova III bo'lim 28-pozitsiya: xabardor qilmasdan ishlaganlik yoki yolg'on ma'lumot bergani uchun jarima — **20 BHM**. [lex.uz/docs/5511879](https://lex.uz/docs/5511879) (ZRU-956 bilan kiritilgan: [lex.uz/docs/7093753](https://lex.uz/docs/7093753))
- VM 847-son, 32-ilova (broker faoliyati pasporti, 2025-yil 18-martdan): yig'im 0,5 BHM; talablar — 1000 BHM ta'minot, Bojxona qo'mitasi tizimida shaxsiy kabinet, mijoz bilan shartnoma, shtatda **ikki va undan ortiq** mutaxassis, ishga olish/bo'shatishni 5 kun ichida xabar qilish, har 2 yilda malaka sertifikati (*2025-yil 1-oktabrdan*). [lex.uz/docs/7274716](https://lex.uz/docs/7274716)

**Chegara — qaysi nuqtada broker bo'ladi (mening tahlilim, aniq emas):**

| Model | Baho |
|---|---|
| Foydalanuvchi YuklaGo dasturini ishlatadi; o'zi kiradi, ko'radi, o'z ERI'si bilan imzolaydi va yuboradi; YuklaGo faqat dastur uchun haq oladi | **Broker emas (ehtimol).** "Deklarant nomidan operatsiya"ni YuklaGo bajarmaydi — deklarantning o'zi bajaradi (BK 275; 611-II 11-modda: jo'natuvchi — rekvizitlarda ko'rsatilgan va yuborayotgan shaxs) |
| YuklaGo xodimi mijoz kompyuterini masofadan boshqarib, uning o'rniga to'ldiradi yoki "Yuborish"ni bosadi | **Xavfli — broker faoliyatiga juda yaqin** |
| YuklaGo yoki xodimi mijozning TIF ro'yxatiga "ishonchli shaxs"/broker/mutaxassis sifatida kiritiladi va o'z ERI'si bilan imzolaydi | **Broker faoliyati** → xabarnoma, 2+ mutaxassis, 1000 BHM ta'minot |
| "Biz siz uchun rasmiylashtiramiz" deb xizmat sotish (natija uchun haq) | **Broker faoliyati** sifatida qaralishi ehtimoli yuqori |
| Paketni mijozning o'zi tanlagan brokerga uzatish | Broker emas. Lekin paketda shaxsiy ma'lumot bo'lsa → rozilik kerak (ZRU-547 28-modda) |

ZRU-956 muqaddimasida qonun chiqaruvchi aynan "tajribasi yo'q shaxslarni shartnomasiz jalb qilish" holatlarini muammo deb ko'rsatgan. Demak, nazorat organi chegaraviy modellarga qattiq qarashi mumkin. [lex.uz/docs/7093753](https://lex.uz/docs/7093753)

**YuklaGo qanday tuzilsin:** (1) Shartnoma — **dasturiy ta'minotdan foydalanish litsenziyasi/obuna** (SaaS), "bojxona xizmati" emas. (2) Narx — dastur funksiyalari uchun, "chiqarilgan yuk uchun" emas. (3) YuklaGo xodimlari hech qachon mijoz ro'yxatida bo'lmaydi va mijoz uchun imzolamaydi. (4) Masofaviy boshqaruv yo'q; yordam — faqat tushuntirish. (5) To'liq xizmat kerak bo'lsa — xabarnoma bergan hamkor broker orqali, mijoz u bilan alohida shartnoma tuzadi. (6) Matnda: "dastur", "yordamchi", "o'zingiz topshirasiz"; ishlatilmaydi: "broker o'rnini bosadi", "rasmiylashtirib beramiz", "deklarantingiz".

*Spec tanqidi:* `yuklago-spec-v2.md` 9-qatordagi "takes over the broker's main role" iborasi ommaviy matnda xavfli. Ichki hujjatda qolishi mumkin, tashqarida — "brokersiz o'zingiz topshirishga yordam beradi".

---

## 3. Shaxsga doir ma'lumotlar va xorijiy LLM (OpenAI, Anthropic, Google)

### 3.1 Joriy matnlar (o'zim o'qidim)
- **ZRU-547, 27-1-modda (ZRU-1125 tahririda, 27.03.2026):** O'zbekistonda saqlash **shart**: (1) biometrik, (2) genetik ma'lumotlar, (3) O'zbekistonda ishlayotgan telekom operatorlari foydalanuvchilarining ma'lumotlari. Boshqa shaxsga doir ma'lumot chet elda saqlanishi va ishlanishi mumkin, agar: davlat "bir xil himoya" ro'yxatida bo'lsa; yoki operator vakolatli organ talablariga mos standart shartnoma shartlari / majburiy korporativ qoidalarni qabul qilgan bo'lsa; yoki ro'yxatdagi xalqaro standartlarga rioya qilsa. [lex.uz/docs/4396419](https://lex.uz/docs/4396419), [ZRU-1125: lex.uz/docs/8099215](https://lex.uz/docs/8099215)
- **15-modda (transchegaraviy uzatish):** "bir xil himoya"ni ta'minlovchi davlatlarga uzatiladi. Boshqa davlatlarga — subyekt roziligi bilan (va yana ikki istisno). [lex.uz](https://lex.uz/docs/4396419)
- **VM 415-son (29.07.2026, 03.08.2026dan kuchda):** 49 davlat ro'yxati. **AQSh — faqat EU-US Data Privacy Framework doirasidagi kompaniyalar uchun** (izoh *). Xitoy yo'q (Gonkong bor), Rossiya bor, Irlandiya va boshqa Yevropa Ittifoqi davlatlari bor. Ro'yxatda yo'q davlatga uzatish — vakolatli organ belgilagan shartlar bajarilganda. Sizib chiqish bo'lsa — 24 soatda xabar, 72 soatda batafsil ma'lumot. Standart shartnoma shartlariga talablar uch oy ichida tasdiqlanishi kerak edi (holati aniq emas). [lex.uz/docs/8369688](https://lex.uz/docs/8369688)
- **VM 415, 4-band — to'g'ri o'qish (2026-11-19 da qayta tekshirildi; xavfsizlik jamoasi o'qishi tasdiqlandi):** 4-bandning **1-xatboshisi** faqat *"Рўйхатга киритилган давлатларга халқаро келишувлар асосида ташкил этилган ахборот тизимлари орқали"* uzatishni tartibga soladi: bunday uzatish "қўшимча рухсатномаларсиз ва ваколатли давлат органини хабардор қилмасдан ... автоматик тарзда" bo'ladi. Bu xatboshi **bizning tijorat bulutimizga (Google Cloud va h.k.) taalluqli emas** — u xalqaro kelishuv asosidagi tizimlar uchun. Shuning uchun bizning uzatish asosimiz — **ZRU-547 15-modda 2-qismi** ("бир хилда ҳимоя қилинишини таъминловчи чет давлатлар ҳудудига") va 27-1-modda 3-qismi (davlat ro'yxatda), ro'yxatning o'zi esa VM 415 ilovasi. AQSh uchun — faqat DPF qatnashchisi bo'lgan kompaniya (* izoh). 2-xatboshi — ro'yxatda **yo'q** davlatlar: vakolatli organ belgilagan huquqiy, tashkiliy va texnik shartlar bajarilganda. 3-xatboshi — sizib chiqish: 24 soat / 72 soat.
- **Vakolatli organni oldindan xabardor qilish shartmi?** ZRU-547 15-moddasida ham, VM 415 da ham ro'yxatdagi davlatga **oddiy (sizib chiqishsiz) uzatish uchun xabarnoma yoki ruxsat talabi topilmadi**. Majburiy xabar faqat **sizib chiqish** holatida (VM 415, 4-band 3-xatboshi: 24/72 soat). 1-xatboshidagi "xabardor qilmasdan" iborasidan teskari xulosa chiqarib ("boshqa hollarda xabar shart") bo'lmaydi — buni belgilovchi norma topilmadi (**aniq emas**, lekin talab yo'q deb hisoblaymiz). Diqqat: vakolatli organ nomi ikki xil — VM 415 3-band: *Ichki ishlar vazirligi huzuridagi Migratsiya va personallashtirish departamenti*; lex.uz'dagi ZRU-547 8-modda matnida hali *Vazirlar Mahkamasi huzuridagi Davlat personallashtirish markazi* deb yozilgan (qaysi biri joriy nomi — aniq emas).
- **Subyektni xabardor qilish (ZRU-547 23-modda 2-qism, tasdiqlandi):** shaxsga doir ma'lumot **uchinchi shaxsga** berilsa, mulkdor/operator subyektni **3 kun ichida yozma** xabardor qiladi. LLM provayderi "uchinchi shaxs"mi yoki biz uchun ishlov beruvchi "operator"mi — qonunda alohida "protsessor" tushunchasi yo'q (4-modda: subyekt, mulkdor, operator, uchinchi shaxs) — **aniq emas**. Konservativ yechim: rozilik ekranida provayder nomi va mamlakatini yozma (elektron) ko'rsatish va uni jurnalga yozish.
- **26-modda:** biometrik ma'lumot — subyektning anatomik va fiziologik xususiyatlarini tavsiflovchi ma'lumot. Shaxsni aniqlash uchun ishlatiladigan biometrik ma'lumotga faqat subyekt roziligi bilan ishlov beriladi. [lex.uz](https://lex.uz/docs/4396419)

### 3.2 ZRU-547 27-1 va MJtK 46-2 — qaysi biri ustun?
- **MJtK 46-2 (birinchi qism, ZRU-726 tahririda, 31.01.2022dan):** hali ham "fuqarolarning shaxsga doir ma'lumotlariga ishlov berilayotganda jismonan O'zbekiston hududida joylashgan texnik vositalarda hamda davlat reyestrida ro'yxatdan o'tkazilgan bazalarda ... yig'ish, tizimlashtirish va saqlashga oid **talablarga** rioya etmaslik" uchun jarima: fuqarolarga 7 BHM, mansabdorlarga 50 BHM. **Ikkinchi qism (ZRU-1115, 21.01.2026):** sun'iy intellekt texnologiyalari yordamida shaxsga doir ma'lumotlarga qonunga xilof ishlov berish yoki ularni tarqatish — 50–100 BHM va qurollar musodarasi. [lex.uz/docs/97664](https://lex.uz/docs/97664) — xavfsizlik jamoasining da'vosi **tasdiqlandi**.
- **ZRU-1125 MJtKga o'zgartirish kiritmagan.** Uning 1-moddasi faqat ZRU-547ning 3-, 20- va 27-1-moddalarini o'zgartiradi. 3-moddasi faqat Vazirlar Mahkamasiga hukumat qarorlarini moslashtirishni topshiradi. [lex.uz/docs/8099215](https://lex.uz/docs/8099215)
- **Tahlil:**
  1. 46-2 — **blanket (havolaki) norma**: u o'zi talab o'rnatmaydi, "talablarga rioya etmaslik"ni jazolaydi. Talabning mazmunini ZRU-547 belgilaydi. 27.03.2026dan "barcha fuqarolar ma'lumoti O'zbekistonda" degan talab qonunda yo'q. Demak, buzilishi mumkin bo'lgan talab ham yo'q. Amalda 46-2 1-qismi faqat qolgan talablarga (biometrik/genetik/telekom + reyestr) tatbiq etiladi.
  2. **Lex posterior:** ZRU-682 18-moddasi — teng kuchli hujjatlar o'rtasida tafovut bo'lsa, keyinroq qabul qilingani qo'llanadi. Kodeks ham qonun (ZRU-682 9-modda: qonunlar kodeks shaklida ham qabul qilinishi mumkin). Kodeksga umumiy ustunlik beruvchi normani ZRU-682 da topmadim. ZRU-1125 (2026) ZRU-726 tahriridan (2021) keyin. [lex.uz/docs/5378966](https://lex.uz/docs/5378966)
  3. **Lex specialis:** ma'lumot saqlash joyi bo'yicha maxsus moddiy norma — ZRU-547 27-1. MJtK — javobgarlik bo'yicha umumiy kodeks.
  4. ZRU-682 18-modda 6-qismi: inson va davlat organlari munosabatlaridagi qonunchilik ziddiyatlari va noaniqliklari **inson foydasiga** talqin qilinadi. [lex.uz/docs/5378966](https://lex.uz/docs/5378966)
- **Xulosa:** amalda **ZRU-547 ning yangi 27-1-moddasi ustun**. MJtK 46-2 1-qismining "jismonan O'zbekistonda" iborasi eskirgan, lekin matndan olib tashlanmagan. Tekshiruvchi uni so'zma-so'z qo'llashga urinish xavfi (amaliyot xavfi) qoladi — **aniq emas**. Shuning uchun konservativ yo'l: asosiy baza va fayllar O'zbekistonda. Bundan tashqari, 46-2 **2-qismi (AI)** to'liq amalda va bizga bevosita tegishli: noqonuniy (masalan, rozilik yoki asossiz) AI ishlovi — 50–100 BHM.

### 3.3 Davlat reyestrida ro'yxatdan o'tish (20-modda)
- 20-modda **mavjud**. Uning birinchi qismi ZRU-1125 bilan o'zgargan: davlat reyestrida ro'yxatdan o'tishi lozim bo'lgan bazalar — **27-1-moddaning ikkinchi qismiga ko'ra O'zbekistonda saqlanishi shart bo'lganlar** (biometrik, genetik, telekom). Ro'yxatdan o'tish ariza berish orqali, xabardor qilish yo'li bilan amalga oshiriladi. [lex.uz/docs/4396419](https://lex.uz/docs/4396419)
- **YuklaGo uchun:** invoys, shartnoma, STIR/JShShIR, pasport rekvizitlari — biometrik emas. Demak, reyestrda ro'yxatdan o'tish **majburiy emas**, agar biz biometrik ma'lumotga ishlov bermasak. **Aniq emas:** pasport/ID skaneridagi **foto** "biometrik ma'lumot" hisoblanadimi (26-modda ta'rifi keng). Yechim: pasport rasmini saqlamaslik — faqat matnli rekvizitlarni olish, rasmni kesib tashlash yoki umuman so'ramaslik. Yuz tanish funksiyasi bo'lmasin.

### 3.4 Yuridik shaxs hujjati va jismoniy shaxs ma'lumoti
- Kompaniya nomi, STIR, summa, tovar, og'irlik — shaxsga doir ma'lumot emas (ZRU-547 faqat jismoniy shaxs ma'lumotini himoya qiladi). Lekin invoys/CMR/shartnomada **rahbar F.I.Sh., imzo, telefon, haydovchi ismi va pasporti, JShShIR, YaTT ma'lumotlari** bo'ladi — bular shaxsga doir ma'lumot.
- Tijorat siri alohida masala (ZRU-547 emas) — mijoz bilan shartnomada maxfiylik bandi kerak.

### 3.5 Amaliy choralar (tartib bo'yicha)
1. Baza va fayllar O'zbekistondagi serverda (default).
2. LLMga yuborishdan **oldin** redaksiya: ism, JShShIR, pasport, telefon, imzo, muhr va haydovchi ma'lumotlarini maska qilish. Tovar va summa qatorlari qoladi.
3. Provayder tanlash: VM 415 ro'yxatidagi yurisdiksiyada ishlov berish (masalan, Yevropa Ittifoqi mintaqasi) yoki DPF'da qatnashuvchi AQSh kompaniyasi. Google LLC DPF ro'yxatida faol ([dataprivacyframework.gov](https://www.dataprivacyframework.gov/participant/5780.Google)). **OpenAI va Anthropic DPF ro'yxatida yo'q — tasdiqlandi:** rasmiy DPF API (`POST https://dpfapi.azurewebsites.net/api/participants`, dataprivacyframework.gov/list sahifasi ishlatadigan so'rov) orqali 2026-11-19 00:45 (Toshkent vaqti) da "OpenAI", "Open AI", "Anthropic" bo'yicha Active va Inactive holatlarda qidirildi — **0 natija**; nazorat uchun "Google" — 1 natija (OrganizationId 5780). Xavfsizlik jamoasining 2026-11-18 dagi natijasi bilan bir xil. Cheklov: boshqa yuridik nom ostida qatnashish 100% istisno qilinmagan. Demak, OpenAI/Anthropic API'siga AQShda to'g'ridan-to'g'ri uzatish VM 415 * shartini bajarmaydi.
4. Ro'yxatda yo'q yurisdiksiya bo'lsa — **alohida, aniq rozilik** (15-modda) va vakolatli organ shartlari (VM 415, 4-band).
5. Rozilik tasdiqlanadigan shaklda (21-modda): checkbox + vaqt + versiya jurnali.
6. "No training / zero retention" sozlamasi, DPA shartnomasi.
7. Keyinchalik: OCR'ni lokal yoki O'zbekistondagi modelda bajarish.
8. AI faqat tavsiya beradi, qarorni foydalanuvchi qabul qiladi (ZRU-547 24-modda; xavfsizlik jamoasi tahlili bilan mos).

**Rozilik matni namunasi (UI):**
> "Hujjatlaringizdagi matnni o'qish uchun ular [provayder nomi, davlat] serverlarida qayta ishlanadi. Yuborishdan oldin ism, pasport, JShShIR va telefon raqamlarini yashiramiz. Ma'lumotlar model o'qitishga ishlatilmaydi va [N] kundan keyin o'chiriladi. Asosiy bazamiz O'zbekistonda. ☐ Roziman (rozilikni istalgan payt Sozlamalarda qaytarib olishingiz mumkin)."

---

## 4. Spec va dizayndagi muddat va javobgarlik matnlari

### 4.1 Tasdiqlangan haqiqiy muddatlar (lex.uz)
| Muddat | Qoida | Manba |
|---|---|---|
| Import deklaratsiyasi | Tovar kelib tushadigan bojxona organiga tovar taqdim etilgan kundan **15 kalendar kundan kechiktirmay** (BK 22, 23, 25-boblaridagi holatlar bundan mustasno). Oxirgi kun bojxona ishlamaydigan kunga to'g'ri kelsa — navbatdagi ish kuni | BK 261-modda; VM 605 Nizomi 11-band |
| Eksport deklaratsiyasi | Tovar amalda olib chiqilgunga qadar | BK 261; VM 605 11-band |
| Transport vositasi | Transport vositasi uchun alohida 3 soatlik muddat bor (yo'nalish tafsiloti — 261-modda matnidan tekshiring) | BK 261-modda |
| Vaqtincha saqlash | Ko'pi bilan **60 kalendar kun** (177-moddada boshqacha bo'lmasa); tez buziladigan tovar — **10 kalendar kun**. Muddatni vakolatli shaxs belgilaydi | BK 85-modda |
| Qisqa BYD (vaqtincha saqlash uchun) | Tovar taqdim etilgan kundan keyingi ish kunidan kechiktirmay (tashuvchi/vakolatli shaxs) | BK 86-modda |
| Dastlabki deklaratsiya | Qabul qilingandan 30 kalendar kun ichida tovar taqdim etilmasa — berilmagan hisoblanadi | BK 262-modda |
| Dastlabki axborot | Tovar amalda kelgunga qadar internet orqali (avto, temir yo'l, havo) | BK 206-modda |
| Rasmiylashtirish | Deklaratsiya qabul qilingan va hamma hujjat berilgan kundan **1 ish kuni** (xavfni boshqarish choralari va boshqa organlar vaqti kirmaydi) | BK 248-modda 4-qism |
| Elektron TED | Past xavf — **3 soat**, o'rta — **8 soat** (o'zgartirish kerak bo'lmasa; ish vaqtidan tashqari topshirilganda istisno), qolgan holatlar — umumiy muddat | VM 605 15-band (VM 700-son tahriri, 08.02.2026dan) |
| BYDni o'zgartirish/bekor qilish | Qabul qilingandan 3 yil ichida | BK 266-modda |
| Dastlabki qaror yig'imi | BHMning 75 foizi | [VM 55-son](https://lex.uz/docs/7357270) |

**Kun hisobi bo'yicha aniq emas:** "taqdim etilgan kundan eʼtiboran 15 kun" — 1-kun taqdim etilgan kunmi yoki ertasimi? Dizayndagi misolda 13.11 → 27.11 (taqdim etilgan kun 1-kun deb olingan). Agar ertasidan sanalsa, muddat 28.11.2026 — shanba, ya'ni bojxona ishlamasa, keyingi ish kuniga suriladi. **Tavsiya:** UI har doim **erta (konservativ) sanani** ko'rsatsin va "kechiktirmay" desin.

### 4.2 UI va spec matnlarini tuzatish jadvali

| # | Joy | Hozirgi matn (iqtibos) | Baho | Manba | Tavsiya etilgan matn (UZ) |
|---|---|---|---|---|---|
| 1 | PDF 4-bet (landing) | "2018-yil 1-iyuldan tadbirkor deklaratsiyani internet orqali oʻz nomidan topshirishi mumkin. Broker majburiy emas — lekin murakkab holatda unga oʻtish imkoni doim bor." | To'g'ri (kichik aniqlik kerak) | VM 605 1-band; BK 258, 274 | "2018-yil 1-iyuldan tashqi savdo ishtirokchisi deklaratsiyani internet orqali brokersiz, oʻz nomidan topshirishi mumkin. Oddiy holatda broker majburiy emas; murakkab holatda brokerga oʻtishingiz mumkin." |
| 2 | PDF 6-bet (tayyorgarlik) | "Boshqa shaxs imzolasa, u bojxonada vakolatli mutaxassis sifatida roʻyxatdan oʻtgan boʻlishi kerak: [shartlar — v2 spec]" | **Noto'g'ri / noaniq** | VM 605 15-band; BK 284 | "Agar siz emas, boshqa odam imzolasa, uni kabinetingizdagi TIF ishtirokchilari roʻyxatiga oʻzingiz kiritasiz (ishonch bildirgan shaxs, broker yoki shtatingizdagi mutaxassis) va vakolat muddatini belgilaysiz." |
| 3 | PDF 7-bet | "Deklaratsiyani topshirish muddati · 27.11.2026 … Yuk kelgan yoki taqdim etilgan sanadan hisoblanadi. Manba: [qonun moddasi]" | Qoida to'g'ri, manba bo'sh; "yuk kelgan" — noaniq | BK 261; VM 605 11-band | "Import deklaratsiyasi: tovar bojxona organiga taqdim etilgan kundan 15 kalendar kundan kechiktirmay. Manba: Bojxona kodeksi 261-modda. Oxirgi kun dam olish kuniga toʻgʻri kelsa — keyingi ish kuni. Biz erta sanani koʻrsatamiz." |
| 4 | PDF 8-bet | "Yetib keldi / bojxonaga taqdim etildi — muddatlar boshlangan boʻlishi mumkin" | To'g'ri | BK 261, 85 | O'zgarishsiz; qo'shish: "Taqdim etilgan sanani ombor dalolatnomasidan tekshiring." |
| 5 | PDF 9-bet | "Vaqtincha saqlash (bojxona ombori) [N] kun qoldi … [Saqlash muddati — v2 spec]" | To'ldirilmagan | BK 85 | "Vaqtincha saqlash: odatda 60 kalendar kungacha (tez buziladigan tovar — 10 kun). Aniq muddat omborga joylashtirishda belgilanadi — omborni tekshiring. Manba: BK 85-modda." |
| 6 | PDF 9-bet | "Muddat oʻtsa: [oqibatlar — v2 spec]" | To'ldirilmagan | MJtK 227-10 2-qism (tasdiqlandi: deklaratsiyani belgilangan muddatda bermaslik — 3 BHM jarima) | "Muddatida topshirmasangiz, jarima bor (MJtK 227-10-modda). Muddat yaqin boʻlsa, brokerga oʻtishni oʻylab koʻring." |
| 7 | PDF 9-bet | "Eslatma: 5, 2 va 1 kun qolganda SMS va Telegram orqali." | Huquqiy da'vo emas; OK | — | Xabarda shaxsiy ma'lumot va summa yozilmasin: "YG-0412: deklaratsiya muddatiga 2 kun qoldi." |
| 8 | PDF 1 va 4-betlar | "Siz imzolaysiz — javobgarlik sizda qoladi." | Asosan to'g'ri | BK 276; VM 605 28-band | "Deklaratsiyani siz (yoki siz vakolat bergan shaxs) imzolaysiz. Maʼlumotlar toʻgʻriligi uchun deklarant — sizning kompaniyangiz javob beradi." |
| 9 | PDF 4-bet | "imzo qoʻygan shaxs qonun oldida javob beradi" | Qisman to'g'ri: majburiyat deklarantda, jarima fuqaro/mansabdorga | BK 276; MJtK 227-22 | "Deklaratsiyadagi xato uchun deklarant va imzo qoʻygan shaxs javob berishi mumkin." |
| 10 | PDF 4 va 10-betlar | "Bojxona aynan shu summani undirishini kafolatlamaydi va farqni toʻlamaydi" / "YuklaGo farqni qoplamaydi" | To'g'ri (siyosat) | FK 332, 333; spec §7 | O'zgarishsiz. Oferta bilan mos bo'lsin (6-javobga qarang). |
| 11 | PDF 1-bet | "Ochiq rasmiy topshirish API topmadik." | To'g'ri | Bu ish; ed1 xizmat pasporti | O'zgarishsiz. |
| 12 | PDF 5-bet futer | "mustaqil xizmat. Davlat organi emas, bojxona bilan rasmiy hamkorlik yoʻq." | To'g'ri | — | O'zgarishsiz. |
| 13 | PDF 17-bet | "Tez — Boʻlimlar orasida toʻxtamaydi. Kirish va imzoda baribir toʻxtaydi." | **Huquqiy xavf** (ko'rmasdan imzolash) | BK 276; ZRU-547 24-modda | Haqiqiy kabinetda yo'q. Mockda: "Tez (faqat mashq)". Haqiqiyda imzodan oldin majburiy: "Barcha 48 maydonni koʻrib chiqdim." |
| 14 | PDF 17-bet | "Hozircha yoqilmagan: rasmiy saytni avtomatik toʻldirishning huquqiy masalasi hal qilinmoqda." | To'g'ri | 1-bo'lim | O'zgarishsiz. |
| 15 | PDF 14 va 15-betlar | "Bu majburiy rasmiy tasnif emas; deklaratsiyani imzolaganda kod uchun men javob beraman." / "Kabinetda imzolasam, deklaratsiya uchun men javob beraman." | To'g'ri | BK 276; VM 55 (dastlabki qaror) | Qo'shish: "Majburiy tasnif kerak boʻlsa — bojxonadan dastlabki qaror soʻrash mumkin (yigʻim BHMning 75 %)." |
| 16 | PDF 26-bet | Broker paketi: "6 ta asl hujjat … Himoyalangan havola 7 kun amal qiladi" | Huquqiy da'vo yo'q; shaxsiy ma'lumot uchinchi shaxsga uzatiladi | ZRU-547 28-modda | Yuborishdan oldin: "Paketda shaxsiy maʼlumotlar bor. Ularni [broker] bilan ulashishga roziman." |
| 17 | Hamma ekran | Rozilik / LLM bildirishnomasi **yo'q** | Yetishmaydi | ZRU-547 15, 21; MJtK 46-2 2-qism | 3.5-bo'limdagi rozilik matnini qo'shish. |
| 18 | spec 101-qator | "low risk generally 3 hours, medium 8 hours, other cases generally 1 working day … — Article 248" | Raqamlar to'g'ri, manba aralash | VM 605 15-band; BK 248 | "3 soat / 8 soat — VM 605-son 15-band (08.02.2026dan); umumiy muddat 1 ish kuni — BK 248-modda." |
| 19 | spec 306, 382-qatorlar | "Customs Code Articles 274 and 277–281" / "broker (Arts. 15 and 277–281)" | **Noaniq** — 278–280 kuchini yo'qotgan | BK (ZRU-494) | "BK 15, 277, 281, 282, 284-moddalar". |
| 20 | spec 315-qator; 392-qator | "Article 227-22 includes confiscation and fines measured in BHM in serious cases" | **Noto'g'ri nuance** — 1-qismning o'zida tovar musodarasi + jarima (fuqarolarga 5–10 BHM, mansabdorlarga 7–15 BHM) | MJtK 227-22 | "MJtK 227-22: notoʻgʻri deklaratsiya — tovar musodarasi va jarima." |
| 21 | spec 389-qator | PF-5414 havolasi `https://lex.uz/docs/-3688185` | **Havola 404** | — | Manba sifatida VM 605-son 1-bandini bering: lex.uz/docs/3844549 |
| 22 | spec 199-qator (Y1) | "authorised-specialist registration" | Noaniq | VM 605 15-band | "TIF ishtirokchilari roʻyxatiga imzolovchini kiritish". |
| 23 | spec 9-qator | "takes over the broker's main role" | Ommaviy matnda xavfli | BK 15, 277 | Tashqi matnda: "oddiy holatda brokersiz oʻzingiz topshirishga yordam beradi". |
| 24 | spec 157-qator | "15 calendar days (Art. 261); … 60 days, 10 days (Art. 85); … 30 days (Art. 262); export … (Res. 605 cl. 11)" | **To'g'ri** | BK 85, 261, 262; VM 605 11-band | Qo'shish: BK 261 istisnolari (22, 23, 25-boblar) va dam olish kuni qoidasi. |
| 25 | spec 160-qator | "packing list is not on the official mandatory list in Resolution No. 605 clause 11-1" | **To'g'ri** ("o'rov varag'i bundan mustasno") | VM 605 11-1-band | O'zgarishsiz. |
| 26 | spec 312-qator | Personal-data tavsifi | **To'g'ri**, endi tasdiqlandi | ZRU-1125; VM 415 | "[OPEN]"ni olib tashlab, VM 415 (AQSh faqat DPF) ni qo'shish. |

---

## Xavfsizlik jamoasi savollariga javoblar

**1) BK 15 va 277: foydalanuvchi o'zi imzolab yuboradigan model broker faoliyatidan tashqaridami? Qaysi nuqtada broker bo'ladi?**
Ehtimol tashqarida (aniq emas). Broker — deklarant **nomidan va topshirig'i bilan, shartnoma asosida** bojxona operatsiyalarini **o'zi** bajaradigan yuridik shaxs (BK 15, 277). Broker bo'ladigan nuqta: YuklaGo (yoki xodimi) TEDni mijoz nomidan shakllantirib, **o'z ERI'si bilan imzolasa yoki yuborsa**; mijozning TIF ro'yxatiga broker/ishonchli shaxs sifatida kiritilsa (VM 605 15-band); masofadan mijoz o'rniga "Yuborish"ni bossa; "rasmiylashtirib beramiz" deb natija uchun haq olsa. Dastur faqat to'ldirib, foydalanuvchi o'zi imzolab yuborsa — operatsiya deklarantniki. [BK](https://lex.uz/docs/2876354), [VM 605](https://lex.uz/docs/3844549)

**2) ed2 uchun e'lon qilinmagan foydalanish shartlari yoki ichki qoidalar bormi? Rasmiy so'rov kerakmi?**
E'lon qilingan qoida topilmadi (aniq emas). Ichki reglament borligini tashqaridan bilib bo'lmaydi. 560-II 12-moddaga ko'ra resurs egasi foydalanish tartibini belgilaydi va kirish shartlari haqidagi ma'lumotni foydalanuvchiga bepul beradi — demak, so'rashga asos bor. **Ha, rasmiy so'rov yuborish tavsiya etiladi** (loyiha pastda). [lex.uz/docs/82956](https://lex.uz/docs/82956)

**3) Rasmiy integratsiya kanali (API, e-BYuD, my.gov.uz) bormi? VM 605 nimani talab qiladi?**
Ochiq REST/SOAP API topilmadi. Rasmiy yo'l: maxsus dasturda XML formatdagi BYD/BDT tayyorlab, USB-token ERI bilan kirib yuklash ([ed1 xizmat pasporti](https://ed1.customs.uz/PersonCabinet/template/property/ted_proper.jsp)). e-BYuD 4 ning joriy yuklab olish joyi — aniq emas. VM 605 Nizomi bo'yicha:
- elektron deklaratsiya YaAAT (yoki "us-uz.gov.uz") bilan vakolatli organ tizimlarining o'zaro almashinuvi orqali o'tadi (14-band);
- ruxsatnomalar "Yagona darcha"da bo'lmasa, TED qabul qilinmaydi (15-band, 1-bosqich);
- deklarant TIF ro'yxatiga imzolovchilarni kiritadi; hujjatlar "E-arxiv"ga ERI bilan joylanadi; TEDni deklaratsiyalovchi shaxs o'z ERI'si bilan imzolab, BQ YaAAT orqali yuboradi (15-band);
- TEDning elektron shaklini Bojxona qo'mitasi tasdiqlab, rasmiy saytiga joylaydi (13-band) — bu XML sxemasini so'rash uchun asos;
- imzolovchi — ERI kaliti egasi bo'lgan jismoniy shaxs (28-band).
Uchinchi tomon dasturlari uchun ochiq integratsiya qoidasi Nizomda yo'q. [lex.uz/docs/3844549](https://lex.uz/docs/3844549)

**4) ZRU-547 27-1 (ZRU-1125) yoki MJtK 46-2 — amalda qaysi biri? 20-modda bo'yicha reyestr shartmi?**
Ikkala matn ham tasdiqlandi. ZRU-1125 MJtKni o'zgartirmagan. 46-2 1-qismi blanket norma, u ZRU-547 talablariga tayanadi. Lex posterior (ZRU-682 18-modda) va "noaniqlik inson foydasiga" qoidasi (18-modda 6-qism) bo'yicha amalda **yangi 27-1** qo'llanadi. 46-2 so'zma-so'z qo'llanish xavfi qoladi (aniq emas), shuning uchun O'zbekistonda hosting saqlanadi. **20-modda mavjud**; reyestr faqat O'zbekistonda saqlanishi shart bo'lgan bazalar (biometrik/genetik/telekom) uchun majburiy. Biometrikka ishlov bermasak — **majburiy emas**. Pasport fotosi masalasi — aniq emas. Batafsil: 3.2–3.3-bo'limlar. [ZRU-547](https://lex.uz/docs/4396419), [ZRU-1125](https://lex.uz/docs/8099215), [MJtK](https://lex.uz/docs/97664), [ZRU-682](https://lex.uz/docs/5378966)

**5) Biz 611-II 13-modda bo'yicha "axborot vositachisi"mizmi?**
Ehtimol **yo'q**, agar YuklaGo imzolangan elektron hujjatni yubormasa va uzatmasa. 13-modda: axborot vositachisi — shartnoma asosida **elektron hujjatlar aylanishi bilan bog'liq xizmat** ko'rsatuvchi shaxs. 14-moddaga ko'ra hujjat jo'natuvchi yoki uning axborot vositachisi tomonidan yuborilgan hisoblanadi. Imzo va yuborish ed2 da foydalanuvchining o'zi tomonidan bo'ladi. Agar kelajakda YuklaGo imzolangan XML/paketni saqlasa yoki uzatsa (masalan, brokerga), vositachi deb qaralishi mumkin. Unda asosiy majburiyat — hujjat mazmunini o'zgartirmaslik (13-modda). Aniq emas. [lex.uz/docs/165074](https://lex.uz/docs/165074)

**6) AI to'lovni noto'g'ri hisoblasa, ofertada javobgarlikni qanday cheklash mumkin?**
- Qonuniy chegaralar: **qasddan** buzish uchun javobgarlikni oldindan cheklash yoki istisno qilish haqidagi kelishuv haqiqiy emas (FK 333-modda oxirgi qism). Qo'shilish shartnomasida yoki kreditor iste'molchi-fuqaro bo'lgan shartnomada, qonun bilan javobgarlik hajmi belgilangan bo'lsa, javobgarlikni cheklash kelishuvi haqiqiy emas (FK 332-modda). [FK](https://lex.uz/docs/111189)
- Iste'molchilar huquqlari qonuni: iste'molchi huquqlarini cheklovchi, qonunchilikka zid shartlar haqiqiy emas (221-I, 21-modda). **Lekin** "iste'molchi" — **shaxsiy, foyda bilan bog'liq bo'lmagan** maqsadda xizmat buyurtma qiluvchi **fuqaro** (1-modda). YuklaGo'ning asosiy foydalanuvchilari — MChJ va YaTTlar (tijorat maqsadi), ular odatda iste'molchi emas. Jismoniy shaxs foydalanuvchilar uchun 21-modda to'liq qo'llanadi. [lex.uz/docs/4704](https://lex.uz/docs/4704)
- Bojxona oldidagi majburiyat baribir deklarantda (BK 276). Oferta faqat YuklaGo va foydalanuvchi o'rtasidagi munosabatni tartibga soladi.
- **Namunaviy matn (oferta):**
  > "5.1. YuklaGo — deklaratsiya tayyorlashda yordamchi dastur. Hisob-kitoblar taxminiy boʻlib, sanasi koʻrsatilgan rasmiy jadvallarga asoslanadi. Bojxona toʻlovlarining yakuniy miqdorini bojxona organi belgilaydi.
  > 5.2. Deklaratsiyadagi maʼlumotlarning toʻgʻriligi va bojxona toʻlovlarini toʻgʻri hisoblash uchun Ozbekiston Respublikasi Bojxona kodeksining 276-moddasiga muvofiq deklarant javob beradi. Foydalanuvchi har bir qiymatni imzolashdan oldin tekshiradi va tasdiqlaydi.
  > 5.3. YuklaGo bojxona organi undirgan summa bilan dastur hisobi oʻrtasidagi farqni qoplamaydi.
  > 5.4. Tadbirkorlik faoliyati doirasida foydalanuvchi oldidagi YuklaGo javobgarligi, qonunchilikda boshqacha belgilanmagan boʻlsa, foydalanuvchi oxirgi [12] oyda toʻlagan obuna haqi bilan cheklanadi. Bu cheklov YuklaGoning qasddan qilgan harakatlariga nisbatan qoʻllanilmaydi.
  > 5.5. Foydalanuvchi isteʼmolchi (jismoniy shaxs) boʻlsa, ushbu boʻlim uning qonunchilikda belgilangan huquqlarini cheklamaydi."
  Yurist ko'rib chiqishi kerak (ayniqsa 5.4 band).

**7) ZRU-701 va VM 847 (18.12.2024) matnlarini tekshirish.**
**Tasdiqlandi.** ZRU-701 3-ilova 35-pozitsiya: "Bojxona brokeri faoliyatini boshlaganlik yoki tugatganlik to'g'risida xabarnoma" → Bojxona qo'mitasi. 4-ilova III bo'lim 28-pozitsiya: xabarnomasiz ishlash yoki yolg'on ma'lumot uchun jarima — 20 BHM ([lex.uz/docs/5511879](https://lex.uz/docs/5511879)). VM 847-son 32-ilova "Bojxona brokeri faoliyati pasporti" (31 va 32-ilovalar 2025-yil 18-martdan kuchda): "Litsenziya" AT yoki Yagona portal orqali; yig'im — BHMning 50 foizi; talablar — 1000 BHM ta'minot (sug'urta faqat bojxona bilan axborot almashadigan sug'urtachi orqali), shaxsiy kabinet, shartnoma, 2+ mutaxassis, 5 kun ichida xodim o'zgarishini xabar qilish, har 2 yilda malaka sertifikati (*2025-yil 1-oktabrdan*) ([lex.uz/docs/7274716](https://lex.uz/docs/7274716)). *Eslatma:* ZRU-701 da elektron tijorat operatorlari (savdo platformasi, buyurtma agregatori, striming) uchun ham xabarnoma bor (3-ilova 38-poz.) — YuklaGo bularga o'xshamaydi, lekin aniq emas.

**8) Kiberxavfsizlik qonuni ZRU-764 bizga taalluqlimi?**
Qisman, ehtimol ha (aniq emas). Qonun mavjud: ZRU-764, 15.04.2022 ([lex.uz/docs/5960604](https://lex.uz/docs/5960604)). "Kiberxavfsizlik subyekti" — milliy axborot resurslariga ega bo'lish, ulardan foydalanish va **elektron axborot xizmatlari ko'rsatish** bilan bog'liq huquq va majburiyatlarga ega yuridik shaxs yoki YaTT (3-modda). YuklaGo onlayn xizmat ko'rsatuvchi yuridik shaxs sifatida shu ta'rifga tushishi mumkin. Unda 16-modda 2-qismidagi majburiyatlar qo'llanadi. **To'liq ro'yxat (2026-11-19 da lex.uz'da qayta o'qildi; xavfsizlik jamoasining `security.md` 1.6 jadvali bilan solishtirildi — hammasi tasdiqlandi):**
  1. ma'lumotlarning noqonuniy tarqalishi, o'g'irlanishi, yo'qolishi, yaxlitligi buzilishi, bloklanishi, qalbakilashtirilishi va ruxsatsiz kirishning oldini olish, aniqlansa — o'z vaqtida choralar ko'rish;
  2. ruxsatsiz kirish natijasida tizim o'zgartirilsa yoki yo'q qilinsa — tezkor tiklash;
  3. kiberxavfsizlik hodisalari va kiberjinoyatlar haqida **vakolatli organni xabardor qilish**, raqamli izlar yo'qolishining oldini olish, tahlil va tergov uchun kerakli ma'lumotlarni **doimiy saqlash**;
  4. kiberxavfsizlik obyektlarini muhofaza qilish va **xavfsiz ishlash monitoringi bo'yicha ma'lumotlarni vakolatli organ bilan almashish**;
  5. vakolatli organ belgilagan **kiberxavfsizlik talablariga rioya** qilish;
  6. hodisalarga javob mexanizmlari va **kiberxavfsizlikni ta'minlash bo'linmasining ishlashini** ta'minlash; bo'linma bo'lmasa — **faqat vakolatli organ ruxsati bilan** belgilangan tartibda autsorsing;
  7. monitoringning tashkiliy-texnik tadbirlari uchun vakolatli organga **monitoring tizimlariga va (yoki) kiberxavfsizlik obyektlariga kirish huquqini berish**.
  Vakolatli organ — **Davlat xavfsizlik xizmati** (ZRU-764, 11-modda). Hodisa haqida xabar berish **muddati** 16-moddada yo'q (aniq emas). 7-band bo'yicha: bu YuklaGo serverlari va monitoring tizimlariga taalluqli; foydalanuvchining ERI kaliti bizda yo'q, shuning uchun unga taalluqli emas. "Muhim axborot infratuzilmasi" (6-bob) toifasiga tushishimiz ehtimoli past — tоifalashtirish tartibi tekshirilmadi.

---

## Bojxona qo'mitasiga rasmiy so'rov — xat loyihasi (YUBORILMAGAN)

**Holat (2026-11-19):** jamoa bu xatni **yubormaydi**. Rasmiy organlar bilan Sarvarbek o'zi bog'lanadi (spec v3, DEC-14). Quyidagi loyiha unga **resurs** sifatida qoladi; matnni u o'z nomidan o'zgartirib ishlatishi mumkin.

*Kimga:* O'zbekiston Respublikasi Iqtisodiyot va moliya vazirligi huzuridagi Bojxona qo'mitasi (yuborish kanali — rasmiy pochta manzili yoki my.gov.uz murojaati; manzil va kanal **aniq emas**, yuborishdan oldin customs.uz saytidan tekshiring). *Kimdan:* YuklaGo jamoasi ([tashkilot nomi, STIR, rahbar F.I.Sh., manzil, telefon]).

> **Mavzu: Tovarlarni elektron deklaratsiyalash tizimi (ed2.customs.uz) bilan uchinchi tomon dasturiy taʼminotidan foydalanish tartibi toʻgʻrisida**
>
> Hurmatli Bojxona qoʻmitasi!
>
> Biz tashqi savdo ishtirokchilari uchun bojxona yuk deklaratsiyasini tayyorlashga yordam beruvchi "YuklaGo" dasturini ishlab chiqmoqdamiz. Dastur hujjatlardan maʼlumotlarni oʻqiydi, TIF TN kodini taklif qiladi, bojxona toʻlovlarini rasmiy stavkalar boʻyicha taxminiy hisoblaydi va qoralamani tekshiradi. Deklaratsiyani deklarantning oʻzi yoki u TIF ishtirokchilari roʻyxatiga kiritgan shaxs oʻz elektron raqamli imzosi bilan imzolaydi va yuboradi (Vazirlar Mahkamasining 2018-yil 31-iyuldagi 605-son qarori bilan tasdiqlangan Nizomning 15 va 28-bandlari). Dastur ERI kalitlari va parollarni saqlamaydi.
>
> Bojxona kodeksining 275-moddasi hamda "Axborotlashtirish toʻgʻrisida"gi Qonunning 12-moddasiga asoslanib, quyidagilar boʻyicha rasmiy tushuntirish berishingizni soʻraymiz:
> 1. "Tovarlarni elektron deklaratsiyalash" tizimi (ed2.customs.uz) uchun tasdiqlangan foydalanish qoidalari yoki reglament bormi? Ular qayerda eʼlon qilingan?
> 2. Deklarant oʻz kompyuterida, oʻz kabinetida va oʻz nazorati ostida maydonlarni avtomatik toʻldiruvchi dasturdan foydalanishi mumkinmi (imzoni deklarantning oʻzi qoʻyadi)? Bunday foydalanishga cheklov yoki texnik talablar bormi?
> 3. Uchinchi tomon dasturlari uchun rasmiy integratsiya kanali (API, test muhiti, shartnoma asosida ulanish) mavjudmi? Unga ulanish tartibi qanday?
> 4. Nizomning 13-bandiga muvofiq tasdiqlangan TED elektron shakli (XML sxemasi, XSD) va BYD/BDT tayyorlash dasturining joriy versiyasi qayerda eʼlon qilingan?
> 5. Deklarant oʻzi foydalanadigan dasturni ishlab chiqish va unga obuna sotish Bojxona kodeksining 15 va 277-moddalari maʼnosida bojxona brokeri faoliyati hisoblanmasligini tasdiqlay olasizmi?
>
> Javobingizni yozma ravishda berishingizni soʻraymiz. Qoʻshimcha maʼlumot yoki namoyish kerak boʻlsa, tayyormiz.
>
> Hurmat bilan,
> [F.I.Sh., lavozim, imzo, sana]

---

## Xavfsizlik jamoasi bilan kelishuv / farqlar

**Kelishamiz:** o'z kabineti + o'z ERI'si = asosiy model; ERI serverga — qizil chiziq; broker chegarasi BK 15/277; 27-1 toraygan; MJtK 46-2 eski matnni saqlaydi; JK 278-1..278-7 va MJtK 155-1 bo'yicha xavflar; "imzolangandan keyin hech narsa o'zgartirilmaydi"; Bojxona qo'mitasiga so'rov (endi uni Sarvarbek o'zi yuboradi, jamoa emas — DEC-14); XML + foydalanuvchi o'zi yuklashi — eng kam xavfli model.

**Qo'shimcha / farq:**
1. ZRU-701 va VM 847 endi **tasdiqlandi** (ular "ochilmadi" degan edi). 4-ilovadagi "20" — yig'im emas, **jarima** (20 BHM). Yig'im — 0,5 BHM (VM 847).
2. 46-2 bo'yicha xulosa: bu "ziddiyat" emas, blanket normaning mazmuni o'zgargani. Amalda 27-1 ustun. Lekin hosting bo'yicha konservativ tavsiya bir xil.
3. Yangi omil: **VM 415-son** (49 davlat; AQSh faqat DPF). Bu xorijiy LLM tanlovini bevosita belgilaydi.
4. 46-2 **2-qismi (AI, 50–100 BHM)** — bizning AI quvurimiz uchun eng to'g'ridan-to'g'ri jarima xavfi. Rozilik va redaksiya shart.
5. Pasport fotosi biometrik bo'lishi mumkin (26-modda) → foto saqlamaslik; aks holda 27-1 lokalizatsiya va 20-modda reyestr majburiy bo'ladi.
6. Ko'pchilik foydalanuvchi tadbirkor → iste'molchilar qonuni ular uchun odatda qo'llanmaydi; FK 332/333 qo'llanadi.
7. ERI qonunida "kalitni berish taqiqlanadi" degan so'zma-so'z norma yo'q; asos — 27-moddadagi xavfsizlik majburiyati.
8. **2026-11-19 dagi 3 ta eslatma tekshirildi — uchalasi ham to'g'ri:** (a) VM 415 4-band 1-xatboshi faqat xalqaro kelishuv asosidagi tizimlar uchun, bizning asos — ZRU-547 15-modda 2-qism; legal.md shunga ko'ra tuzatildi (3.1). Oddiy uzatish uchun vakolatli organga xabar berish talabi topilmadi. (b) OpenAI/Anthropic DPF'da yo'q — DPF API orqali o'zim qayta tekshirdim, **tasdiqlandi**. (c) ZRU-764 16-modda 7 ta majburiyati — lex.uz bilan mos, Q8 javobiga to'liq qo'shildi; vakolatli organ — DXX (11-modda).
9. Qo'shimcha topilma: ZRU-547 23-modda 2-qismi — uchinchi shaxsga berilganda subyektga 3 kun ichida yozma xabar (3.1).

---

## Aniq emas

- ed2 uchun e'lon qilinmagan ichki reglament yoki avtomatlashtirish taqiqi bor-yo'qligi.
- Dastur (SaaS) modeli broker faoliyati emasligi — rasmiy tushuntirish yo'q; sud yoki bojxona amaliyoti topilmadi.
- 15 kunlik muddatni sanash usuli (taqdim etilgan kun hisobga kiradimi).
- MJtK 46-2 1-qismini tekshiruvchilar amalda qanday qo'llashi.
- Pasport/ID fotosi 26-modda bo'yicha "biometrik ma'lumot"mi.
- VM 415 4-bandidagi standart shartnoma shartlariga talablar tasdiqlanganmi; ro'yxatda yo'q davlatga uzatish uchun vakolatli organ shartlari qanday.
- ~~OpenAI va Anthropic DPF ro'yxatida yo'qligi~~ — **tasdiqlandi** (rasmiy DPF API, 2026-11-19; 3.5-bo'lim). Qolgan savol: model egasi DPF'da bo'lmasa, uning modeli Yevropa Ittifoqi mintaqasidagi bulut provayderi orqali ishlatilishi VM 415 talabini qondiradimi — aniq emas.
- LLM provayderi ZRU-547 bo'yicha "uchinchi shaxs"mi yoki "operator"mi (23-modda 3 kunlik xabar talabi uchun).
- Kiberxavfsizlik hodisasi haqida DXXga xabar berish muddati va shakli (ZRU-764 16-moddada yo'q).
- ZRU-547 vakolatli organining joriy nomi (VM 415 3-band va ZRU-547 8-modda matni farq qiladi).
- 605-son qarordagi "us-uz.gov.uz" tizimi nima (domen hozir boshqa portalni ochadi).
- e-BYuD 4 / TED XML sxemasining joriy rasmiy joylashuvi.
- ZRU-764 bo'yicha YuklaGo "kiberxavfsizlik subyekti"mi; muhim axborot infratuzilmasi toifalashtirilishi.
- PF-5414 matni (spec'dagi havola 404; men faqat VM 605 1-bandidagi bayonni ko'rdim).
- 1 BHM = 440 000 so'm (PF-115) — men tekshirmadim.
- Bojxona qo'mitasiga yozma murojaat yuboriladigan rasmiy manzil/kanal.

## Manbalar (2026-11-18 da ochildi; VM 415 4-band, ZRU-547 15/23-moddalar, ZRU-764 11/16-moddalar va DPF API 2026-11-19 da qayta tekshirildi)
- Bojxona kodeksi: https://lex.uz/docs/2876354 (15, 85, 86, 206, 248, 258, 261, 262, 266, 274–277, 281, 282, 284-moddalar)
- VM 605-son qarori (o'zbekcha joriy matn): https://lex.uz/docs/3844549 (Nizom 11, 11-1, 13, 14, 15, 28, 29-bandlar)
- VM 700-son (06.11.2025) — 605-son o'zgarishlari manbasi (605 matnidagi izohlar orqali)
- VM 55-son: https://lex.uz/docs/7357270
- ZRU-701: https://lex.uz/docs/5511879 ; ZRU-956: https://lex.uz/docs/7093753 ; VM 847-son: https://lex.uz/docs/7274716
- ZRU-547: https://lex.uz/docs/4396419 ; ZRU-1125: https://lex.uz/docs/8099215 ; VM 415-son: https://lex.uz/docs/8369688
- MJtK: https://lex.uz/docs/97664 (46-2, 155-1, 227-10, 227-22, 227-27) ; JK: https://lex.uz/docs/111453 (278-1..278-7)
- ZRU-793 (ERI): https://lex.uz/docs/6234904 ; 611-II: https://lex.uz/docs/165074 ; 560-II: https://lex.uz/docs/82956
- ZRU-764: https://lex.uz/docs/5960604 ; ZRU-682: https://lex.uz/docs/5378966
- FK (1-qism): https://lex.uz/docs/111189 (332, 333) ; 221-I: https://lex.uz/docs/4704 (1, 21)
- DPF: https://www.dataprivacyframework.gov/participant/5780.Google ; rasmiy API: https://dpfapi.azurewebsites.net/api/participants (POST)
- ed1 xizmat pasporti: https://ed1.customs.uz/PersonCabinet/template/property/ted_proper.jsp

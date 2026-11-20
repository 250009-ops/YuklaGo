# YuklaGo web UI v0.1 — UX + UI sharhi

**Kimga:** hakaton jamoasi, Sarvarbek, UI/UX va Brend Dizayner  
**Nima ko‘rildi:** `yuklago-spec-v2.md`, `design-v0.1/design-rationale.md`, `yuklago-web-ui-v0.1.pdf` (28 sahifa, har biri `pdftoppm` bilan PNG qilib ko‘zdan kechirildi), avvalgi mobil prototip `/workspace/yuklago-design/`.  
**Sana:** 18-noyabr 2026, Toshkent vaqti (UTC+5).  
**Bu huquqiy maslahat emas.**

---

## 1. Uch qatorli xulosa

Dizaynning **mantiqi yaxshi**: manba-chiplari, “o‘zim topshira olamanmi?”, yo‘l varaqasi, kabinetni ko‘z oldida to‘ldirish, ERI da to‘xtash va brokerga paket — v2 spetsifikatsiyaga mos.  
Lekin **ko‘rinishi hozir professional-rasmiy emas**: o‘zbek yozuvidagi oʻ/gʻ harflari deyarli har yerda bo‘shliq va qo‘shtirnoqqa bo‘linib ketgan, [N] / [v2 spec] / [X] % joyi to‘ldirilmagan, ba’zi sahifalar yarmi bo‘sh, “Rasmiy” deb qo‘yilgan raqamlarning biri v2 qoidasiga mos kelmaydi.  
Sababning bir qismi dizayn qarorida ham bor: “davlatdek ko‘rinmasin” deyilgan, lekin natija **jilovsiz beige-maket** bo‘lib qolgan. Kerak bo‘lgani — *davlat sayti emas, lekin jiddiy moliyaviy vosita*.

**Hisob (28 ta taxta):** Saqlash **4** · Tuzatish **19** · Qayta qilish **5**.

---

## 2. Sahifama-sahifa jadval

*Tipografik oʻ/gʻ xatosi deyarli barcha matnli sahifada bor. Uni global P0 deb oldim; pastdagi “muammo”larda asosan shu sahifaga xos narsalar yozilgan. “Saqlash” — tuzilma yaxshi, global yozuv tuzatilgach asosan shu holatda qolishi mumkin.*

| # | Ekran | Hukm | Asosiy muammolar |
| --- | --- | --- | --- |
| 01 | Dizayn tizimi (“Calm ledger”) | **Tuzatish** | G‘oya kuchli (chiplar, ikonka+so‘z, mashq vs haqiqiy). Lekin namuna matnda ham “O ‘ zingiz”, “To ‘ lovlar”, “so ‘ m” buzilgan — tizimning o‘zi yozuvni isbotlamagan. “Layout and breakpoints” bloki taxta pastidan kesilgan. “Must never look official” jumlasi *davlat bilan adashtirmaslik* uchun to‘g‘ri, lekin *jiddiylikni* ham olib tashlagan. Beige qog‘oz (#F6F5F1) + 48 px display — jurnal, kabinet emas. |
| 02 | Umumiy shapka + yuk sarlavhasi (komponent) | **Tuzatish** | “Saqlash: **[N] kun**” deyarli barcha yuk ekranida takrorlanadi — tugallanmagan maketdek. Navigatsiyada “Xabarni tushunish” asosiy menyuda; bu keyingi qadam vositasi, doimiy bo‘lim emas. Ikki qatorli shapka qabul qilinadi, lekin zichligi va ierarxiyasi Stripe/my.gov.uz darajasida emas. |
| 03 | Yuk bosqichlari relsi (komponent) | **Saqlash** | Guruhlash to‘g‘ri: to‘lashdan oldin / jo‘natishdan oldin / yetib kelgach. Holatlar (bajarilgan, diqqat, keyingi, o‘chiq) tushunarli. Brokerga chiqish doim ko‘rinadi. Faqat yozuv va “Istalgan bosqichda…” kulrang qutisi biroz zaif. |
| 04 | Landing (yuqori) | **Qayta qilish** | Bosh sarlavha buzilgan: “Deklaratsiyani o ‘ zingiz topshiring”. Marketing-jurnal uslubi (katta serifssiz display, yumshoq fon). Sahifa “Bitta yuk — uch bosqich” o‘rtasida uzilgan, pastki qism 05-ga tushgan. “Qanday ishlaydi / nima qilmaydi” mazmuni yaxshi, lekin kartalar zich, ierarxiya yotiq. Bu birinchi taassurot — hozir ishonch uyg‘otmaydi. |
| 05 | Landing pastki + kirish | **Qayta qilish** | Taxtaning yarmi bo‘sh oq maydon — “tugallanmagan PDF” taassuroti. Kirish faqat telefon maydoni; SMS kodi, xato, bo‘sh holat, qayta yuborish yo‘q. Broker bloki chapda zaif, kirish o‘ngda — ikkalasi ham “kichik karta”. Footer ixcham, lekin “mustaqil xizmat” yozuvi ham buzilgan yozuvda. Kirish oqimini alohida, to‘liq ekran qiling. |
| 06 | Yo‘lni tanlash + “O‘zim topshira olamanmi?” | **Tuzatish** | Mantiq v2 ga juda mos (posilka / yo‘lovchi / tijorat; ERI, kabinet, kim imzolaydi). O‘ngdagi xulosa relsi yaxshi. Lekin “Qoidalar — **[v2 spec]**”, “**[shartlar — v2 spec]**” matnda qolgan. Tanlangan “Yo‘q” tugmasi qora — brend petreli bilan nomuvofiq. Matn zich, lekin bu ekran uchun joiz. |
| 07 | Bosh sahifa | **Tuzatish** | “Diqqat kerak” + muddat soati + yuklar jadvali — to‘g‘ri tuzilma. “Manba: **[qonun moddasi]**” va o‘ngda “**[N] kun**” vaqtinchalik saqlash — ko‘zga tashlanadigan joyda chizilmagan maydon. Jadval yengil, summalar kichik, “Jami, so‘m” ustuni zaif. ERI hali tayyor emas banneri yaxshi. Bo‘sh / yuklanish / xato holatlari yo‘q. |
| 08 | Yangi yuk | **Tuzatish** | Bosqichli forma + o‘ng rels aniq. “Qoralama avtomatik saqlanadi” ishonch beradi. “Qoidalar — **[v2 spec, «Eksport»]**” va `6xxxxxxxxx.html` havolasi namuna ekanini yomon yashiradi. Radio-qatorlar yaxshi. |
| 09 | Yuk ish maydoni (umumiy holat) | **Tuzatish** | Keyingi qadam banneri tushunarli. Lekin muddat blokida ochiq qoldirilgan matn: “**[Muddat uzunligi va qonun moddasi — v2 spec]**”, “**[oqibatlar — v2 spec]**”, “**[N] kun qoldi · tugaydi [sana]**”, saqlash paneli bo‘sh/qora chiziq. V2 da bu raqamlar bor: 15 kalendar kun (261-modda), saqlash odatda 60 kun, tez buziladigan 10 kun (85-modda). “So‘nggi harakatlar” yaxshi. |
| 10 | Kelib tushgan narx (yuqori) | **Tuzatish** | Eng muhim ish ekranlaridan. Chiplar, bo‘linish, kod ta’siri, kargo solishtiruvi — to‘g‘ri. Lekin sahifa 11-ga kesilgan. “Rasmiy · 01.11.2026” yozuvi ostidagi **yig‘im 310 000 so‘m** v2 qoidasiga mos emas: 01.09.2026 dan 1 BHM = 440 000 so‘m, bu yuk ~4 300 USD (10 000 dan ichida) → 1 BHM. “Rasmiy” deb qo‘yilgan noto‘g‘ri raqam ishonchni sindiradi. 10 % boj ham NOTARIF da tekshirilmaguncha “Rasmiy” bo‘lmasligi kerak. |
| 11 | Narx davomi: kargo, imtiyoz, shartnoma/bank | **Qayta qilish** | Bu alohida ekran emas — 10-ning pastki parchasi, ostida katta bo‘sh oq maydon. “Boj **[X] %** o‘rniga **[Y] %**”, “**[shakl nomi]**”, “**[shartlar — v2 spec]**”, “**[v2 spec, «Bank»]**” mijoz ko‘radigan maketda qolgan. Imtiyozni “maslahat bermaymiz” deb to‘g‘ri cheklagan; shu blokni 10-ga qo‘shib, raqamlarsiz lekin toza qiling. |
| 12 | Jo‘natishdan oldin ruxsatnomalar | **Tuzatish** | Yashil “Jo‘natish mumkin” + ro‘yxat yaxshi. “Hali jo‘natmang” va “YuklaGo qo‘llab-quvvatlamaydi” variantlari ham ko‘rsatilgan — bu qimmatli. Lekin “To‘plamadi” qatorlarda faqat “—” bor, ikonka+so‘z yo‘q (“Shart emas” kerak). “Ro‘yxatlar: **[v2 spec]**”, “**[ruxsat turi — v2 spec]**”, fayl nomi `sertifikat_UZ_xxxx.pdf` — tugallanmagan. |
| 13 | Hujjatlar: o‘qish va solishtirish | **Saqlash** | Eng yaxshi ekran: invoys rasmi + ajratilgan maydon, “ishonch past”, hujjatlararo tekshiruv, sotuvchi nomi farqi. Tuzilmani saqlang. Qo‘shing: bo‘sh holat, o‘qib bo‘lmaydigan rasm, OCR xatosi, yuklanish. Shapkada baribir [N] bor. |
| 14 | TIF TN kodi | **Tuzatish** | “Taklif, rasmiy tasnif emas” + tasdiq ro‘yxati + qo‘lda kiritish xatosi — to‘g‘ri. “Rasmiy nomi: **[TIF TN ro‘yxatidagi matn — …]**” qavs ichida qolgan. “Qanchalik ishonchli” paneli raqamsiz — haddan tashqari ishonch berishi mumkin. Muqobil kodlar `xxx x` va “+3 068 800 so‘m” rasmiy farqdek ko‘rinadi. |
| 15 | To‘lovlar va qoralama tekshiruvi | **Tuzatish** | Yuqorida to‘siq/ogohlantirish, 47-grafa jadvali, 48 maydon, javobgarlik belgisi — v2 dagi “imzodan oldin ko‘rish” ni yaxshi beradi. “Rasmiylashtirish yig‘imi” asosida “**[asos]**” turibdi. 16-sahifaga kesilgani sabab asosiy tugma ko‘rinmaydi. 310 000 yig‘im shu yerda ham. |
| 16 | Qoralama pastki (tugmalar parchasi) | **Qayta qilish** | Faqat ikki tugma va izoh, qolgani bo‘sh oq. 15-ga qo‘shilsin. “Ochilmaydi: 1 ta to‘siq” yozuvi to‘g‘ri g‘oya — lekin shu holda sahifa professional ko‘rinmaydi. |
| 17 | Kabinetni to‘ldirish — boshlash | **Tuzatish** | Uch yo‘l (mashq / haqiqiy hali yo‘q / o‘zim yozaman), 6 qadam, tezlik, pauza, “kalitingiz faqat sizda” — v2 va brifga mos, saqlashga arziydi. 18-ga kesilgan. Tugma ranglari (qora / pushti / petrel) aralash. |
| 18 | Mashqni boshlash tugmasi (parcha) | **Qayta qilish** | Bitta pushti tugma va bitta qator, qolgani bo‘sh. 17-ga qo‘shilsin. |
| 19 | Avtomatlashtirish: yozilmoqda | **Tuzatish** | Ikki panel (kabinet oynasi + YuklaGo relsi) to‘g‘ri. Lekin mashq belgisi haddan oshgan: pushti tasma + ramka + diagonal suv belgisi + pushti URL — bir skrinshotda to‘rtta signal, “o‘yin / Figma maketi” dek. “**Prototip: jonli to‘ldirishni ko‘rsatish**” tugmasi mahsulotda qolgan. Kabinetdagi “Imzolash va yuborish” to‘ldirish davomida faol ko‘rinadi — xavfli. 28/48 yozilgan deyilgan, lekin ko‘rinadigan maydonlarning ko‘pi bo‘sh. |
| 20 | Avtomatlashtirish: pauza / tahrir | **Tuzatish** | Interaksiya juda yaxshi: to‘xtadi, farqni ko‘rsatadi, qoralamani yangilash yoki qaytarish, davom / bitta maydon / qolganini o‘zim. Tuzilmani saqlang; vizual shovqinni 19 bilan birga kamaytiring. Ko‘p bir xil kenglikdagi tugmalar ierarxiyani yuvadi. |
| 21 | ERI: “Endi sizning navbatingiz” | **Tuzatish** | Qora rels + sariq “sizning navbatingiz” + 4 qadam + “bizda parol maydoni yo‘q” — to‘g‘ri ishonch usuli. **Jiddiy xato:** “Bu oyna kabinetniki. YuklaGo bu yerga yozmaydi” yozuvi modal **tagida** qolgan, deyarli o‘qilmaydi. Modal “Kalit paroli” maydonini YuklaGo oynasida ko‘rsatadi — odam “parolni shu yerga kiritaman” deb o‘ylashi mumkin. Bu yorliq modal ustida, katta va doim ko‘rinadigan bo‘lsin. |
| 22 | Avtomatlashtirish: xato | **Tuzatish** | “Hech narsa yuborilmagan, qoralama imzolanmagan” + 27/1/20 hisob + qayta urinish / qo‘lda / broker — v2 dagi muvaffaqiyatsizlik modeliga mos. Saqlang, vizualni 19 bilan bir xillashtiring. |
| 23 | Sessiya yakuni va yozuv | **Saqlash** | “Siz / YuklaGo” vaqt chizig‘i, maydonlar jadvali, “parol va kalit yozilmaydi”, PDF / yordamga ulashish — kuchli ishonch artefakti. Kichik: jadvalda 48 dan faqat 3 qator ko‘rinadi (namuna ekanini yozing). |
| 24 | Topshirilgach: holat va xabarni tushunish | **Tuzatish** | Ruscha kabinet matnini o‘zbekcha tushuntirish — foydali va v2 ga mos. “Jonli ma’lumot yo‘q” halol. Lekin chap rels hali ham “Hujjatlar: 1 maydon”, “Kabinetni to‘ldirish: tekshiruvdan keyin” deb turibdi — 23-da allaqachon imzolangan. Holatlar zanjiri sinadi. “UZ.xxxxx.xxxxx” joyi. |
| 25 | Mahsulotlar kutubxonasi | **Tuzatish** | Jadval + o‘ng panel + stavka o‘zgarishi ogohlantirishi to‘g‘ri. “boj **[x] %**. Yangi: **[y] %**” va kodlar `9401 xx xxx x` tasdiqlangan kutubxonada “buzilgan ma’lumot” dek. Bo‘sh kutubxona holati yo‘q. |
| 26 | Brokerga topshirish | **Saqlash** | “O‘z brokeringizga paket, biz tanlamaymiz, kalit kirmaydi” — to‘g‘ri model (v2 Y18 va avvalgi prototip bilan mos). Ichidagi ro‘yxat aniq. Qo‘shing: yuborilgach muvaffaqiyat, havola muddati o‘tgan, xato. Asosiy tugma qora — boshqa ekranlardagi petrel bilan zid. |
| 27 | Sozlamalar: xavfsizlik va jurnal | **Tuzatish** | Kirish sessiyalari, jurnal, ma’lumotni yuklab olish / o‘chirish — yaxshi. Lekin “ERI va kabinet” menyuda bor, alohida ekrani ko‘rinmaydi (faqat qora banner). Yuqori menyudan “Xabarni tushunish” yo‘qolgan; DK belgisi boshqa sahifalardagidan farq qiladi. |
| 28 | Mobil to‘plam (4 ta telefon) | **Tuzatish** | Yo‘nalish to‘g‘ri: muddat birinchi, narx yig‘iq, kamera bilan tekshiruv, kabinet **telefonda emas** + kompyuterga havola (v2 va avvalgi prototip bilan mos). Lekin bu to‘liq oqim emas: onboarding, yo‘l varaqasi, qoralama xatolari, broker, kutubxona, kirish, bo‘sh/xato holatlari yo‘q. Pastki tab (Bosh / Yuklar / Suratga olish / Narx) veb menyudan farq qiladi — ona tizimda kelishilishi kerak. Yozuv xatosi telefonda ham bor. |

---

## 3. Kesishgan muammolar: nima uchun “norasmiy” ko‘rinadi

### 3.1 Yozuv — birinchi taassurotni buzadi
O‘zbek lotinida oʻ va gʻ (U+02BB) deyarli har sarlavhada shunday chiqadi: “o ‘ zim”, “to ‘ lov”, “jo ‘ natish”, “so ‘ m”. Bu o‘quvchiga *xato yozilgan e’lon* dek tuyuladi, davlat yoki bank xizmati dek emas. Rationale IBM Plex ni aynan shu harf uchun tanlagan; eksport qilingan PDF da shrift ishlamagan yoki belgi bo‘shliq + qo‘shtirnoq sifatida kiritilgan. **Bu bitta tuzatish butun mahsulotni boshqacha ko‘rsatadi.**

### 3.2 Joyi to‘ldirilmagan matnlar
Ko‘rib chiqish taxtasida hali ham turibdi: `[N] kun`, `[qonun moddasi]`, `[v2 spec]`, `[shartlar — v2 spec]`, `[X] %` / `[Y] %`, `[asos]`, `[sana]`, `xxxx`, `xxx x`. Dizayner spec fayliga kira olmaganini rationale da yozgan. Tushunarli. Lekin v2 da muddatlar allaqachon bor (15 kun — 261-modda; 60/10 kun — 85-modda; dastlabki deklaratsiya 30 kun — 262-modda). CEO ko‘radigan taxtada qavs qoldirish — “bu hali o‘yin” degan signal.

### 3.3 “Rasmiy” yorlig‘i ostidagi raqam
Ishonch tizimining yuragi — “Rasmiy · sana” chipi. Shu chip ostida yig‘im **310 000 so‘m** (01.11.2026). V2: 01.09.2026 dan 1 BHM = **440 000 so‘m**; 10 000 USD gacha tizma — 1 BHM. Namuna yukning bojxona qiymati taxminan 4 300 USD. Demak 310 000 “rasmiy” bo‘la olmaydi (eski BHM yoki xato). 10 % boj ham NOTARIF dan tasdiqlanmaguncha “Rasmiy” deb yozilmasin. Noto‘g‘ri “rasmiy” raqam — oddiy bo‘sh joydan ham yomonroq.

### 3.4 Rang, typografik ohang, bezak
Iliq qog‘oz fon, katta display shrift, yumshoq soyasiz kartalar, pushti-magenta chiziqli “MASHQ” ramkasi — bu *dizayn portfoliosi*, *bojxona-moliya vositasi* emas. Payme, Click, Stripe, my.gov.uz — ko‘proq oq/sovuq fon, qat’iy jadval, katta lekin tiniq summa, kam bezak. “Davlat bayrog‘i va muhri yo‘q” — to‘g‘ri (YuklaGo mustaqil). “Professional ko‘rinmasin” — noto‘g‘ri o‘qilgan vazifa.

### 3.5 Ikonka va holat
Tizim “rang hech qachon yolg‘iz emas” deydi — bu to‘g‘ri. Amalda ruxsatnoma ro‘yxatidagi “To‘plamadi” qatorlar faqat “—” bilan qolgan. Ba’zi tugmalar petrel, ba’zilari qora, mashq tugmasi pushti. “DK” avatari sahifadan sahifaga o‘zgaradi.

### 3.6 Ma’lumot jadvallari
To‘lov va grafa jadvallari g‘oya jihatidan to‘g‘ri, lekin: monoton 14–15 px, yomon ierarxiya (jami qator kam ajraladi), tabular raqamlar ba’zan ishlaydi ba’zan yo‘q, kesilgan sahifada “Jami” yoki CTA ko‘rinmaydi. Professional kabinetda jadval — asosiy asar, fon emas.

### 3.7 Ishonch signallari va manba/sana
Chiplar — v0.1 ning eng yaxshi ixtirosi, saqlansin. Hozir ularni buzadigan narsa: chiziq ostidagi noaniq raqam, [manba] qavslari, landingda kesilgan ishonch bloklari. “YuklaGo davlat organi emas” footeri kerak, lekin u ham tiniq yozuvda, ixcham tasmada bo‘lsin — har sahifada buzilgan kichik qator sifatida emas.

### 3.8 Avtomatlashtirish ekranlari
Mantiq v2 §8.2 va brif §4 ga yaqin: ko‘z oldida yozish, pauza, qayta o‘qish, login/imzoda to‘xtash, yozuv. **Vizual** esa mashq rejimini “bo‘yama chiziq” bilan haddan oshirishgan. Stripe’dagi “Test mode” — bitta tasma, sayt o‘zi jiddiy qoladi. Bu yerda to‘rt qavatli signal + maket kabinetdagi “Imzolash va yuborish” tugmasi to‘ldirish vaqtida yonib turadi. “Prototip: …” tugmasi mahsulotga tushib qolgan.

### 3.9 ERI topshirig‘i
Eng muhim ishonch lahzasi. Qora rels va 4 qadam yaxshi. Lekin kabinetning imzo oynasi YuklaGo ichida parol maydoni ko‘rsatadi, ogohlantirish esa modal orqasida yashirin. Foydalanuvchi qo‘rquvi (brif): “ERI parolini so‘rashadi yoki bulutga olishadi.” Hozirgi kompozitsiya shu qo‘rquvni kuchaytirishi mumkin. Kerak: avval to‘liq ekran “Endi siz”, keyin kabinet oynasi alohida, YuklaGo hech narsa yozmayotgani **modal ustida** turadi.

### 3.10 Holatlar qamrovi
Ko‘rsatilgani: ba’zi xato (kod topilmadi, avtomatik to‘xtash, qoralamada to‘siq), mashq vs haqiqiy (haqiqiy o‘chiq), ruxsatnoma uchun 3 variant. Ko‘rsatilmagani yoki juda zaif: bo‘sh ro‘yxat, yuklanish, tarmoq xatosi, OCR umuman o‘qiy olmaslik, SMS xato/qayta yuborish, broker havolasi muddati o‘tgan, 24-sahifada relsning eski holati, sozlamalarda ERI ekranining o‘zi.

### 3.11 Mobil vs veb
28-sahifa yo‘nalishi to‘g‘ri (imzo telefonda emas). Lekin bu 4 ta kadra — to‘liq mobil mahsulot emas. Vebda chap rels + shapka, telefonda boshqa tab tuzilmasi. Buni bir IA qilib kelishish kerak. Avvalgi prototip (`/workspace/yuklago-design/`) dan olinadigan narsa: katta bosiladigan nuqta, svetofor doim ikonka+matn, “namuna” yorlig‘i rasmiy bo‘lmagan raqamda, muddatni birinchi darajali obyekt qilish. V0.1 dagi chiplar va “kabinet faqat kompyuterda” esa avvalgi prototipdan **kuchliroq** — shularni saqlang.

### 3.12 Taxta sifati (PDF o‘zi)
28 sahifaning 4 tasi (05, 11, 16, 18) asosan bo‘sh. 04–05, 10–11, 15–16, 17–18 bir ekranning teshib qo‘yilgan qismlari. Bunday taqdimot o‘zi “norasmiy” baho beradi, dizayn g‘oyasi yaxshi bo‘lsa ham.

---

## 4. Solishtirish: nimalarni olish mumkin

Faqat ishonchli bilgan andozalar. Statistikani o‘ylab topmadim.

**GOV.UK Design System.** Oq fon, qat’iy shrift shkalasi, kam bezak, “Start now” tipidagi aniq asosiy tugma, *inset text* va *warning text* (yorqin chiziq + qisqa ogohlantirish), *notification banner*. Holat hech qachon faqat rang bilan emas. YuklaGo landing va xato/ogohlantirishlari shu jiddiylikka yaqinlashsin — bayroq rangisiz ham bo‘ladi.

**Stripe Dashboard.** Oq/kulrang ish maydoni, chap menyu, zich lekin tiniq jadvallar, voqealar jurnali. “Test mode” — bitta tushunarli tasma; asosiy interfeys o‘zgarib ketmaydi. Mashq kabineti uchun shu andoza: bitta “MASHQ REJIMI” tasmasi, to‘rt qavatli pushti chiziq emas. To‘lov tafsiloti kabi: summa katta, qatorlar manbali, “jami” aniq ajraladi.

**Wise (va xuddi shu oiladagi pul o‘tkazma ekranlari).** Katta summa, “siz to‘laysiz / u oladi” kabi ochiq bo‘linish, kurs yonida sana/vaqt. Kelib tushgan narx shu andozaga yaqin, lekin hozir jami ba’zan kesiladi yoki kichik yozuvda qoladi. Telefonda 28-sahifadagi katta “≈ 67 823 600” — to‘g‘ri yo‘l; vebda ham shu darajada bo‘lsin.

**Revolut.** Kartali, katta balans, kam so‘z. Bosh sahifa “Xayrli tong” dan keyin darhol *nima qilish kerak* ni (muddat, to‘siq) Wise/Revolut kabi katta raqam + bitta harakat bilan ko‘rsatsin; hozir jadval biroz yassi.

**Estoniya e-Tax / e-Residency (umumiy andoza).** Imzo alohida davlat/ID moduliga topshiriladi; xizmat o‘zi parol so‘ramaydi, “endi imzo sizda” aniq to‘xtaydi. YuklaGo ERI lahzasi shu kabi: avval to‘liq “navbatingiz”, keyin kabinetning o‘z oynasi, YuklaGo chetda.

**Singapore Singpass (umumiy andoza).** Autentifikatsiya — brendli, adashtirib bo‘lmaydigan topshiriq (ilova / QR), xizmat ichidagi oddiy parol formasiga o‘xshamaydi. ERI handoff ham shu darajada ajralib tursin.

**my.gov.uz.** Rasmiy portal, jiddiy o‘zbek matn, ERI/e-IMZO orqali xizmatlar. YuklaGo ko‘k “davlat shapkasini” nusxa qilmasin (mustaqil ekanini yo‘qotadi). Olinaveradigan narsa: formal ohang, toza forma, imzo qadami alohida ekanligi.

**Payme va Click.** O‘zbek foydalanuvchisi shu yerda pul tasdiqlashga o‘rganan: oq karta, tiniq so‘m, telefon + SMS kirish, “tasdiqlash” lahzasi jiddiy. Kirish, jami to‘lov va “imzoladim” tasdiqini shu odatiy ishonch ritmida qiling — bezaksiz, katta raqam, bir aniq tugma.

**Avvalgi YuklaGo mobil prototipdan.** Svetofor = ikonka + so‘z; rasmiy bo‘lmagan raqam = “namuna” / “taxmin”; muddat — alohida soat, manba bilan; broker = paketi o‘z odamiga, bozor emas. V0.1 buni asosan olgan; endi yozuv va “Rasmiy” intizomi yetishmayapti.

---

## 5. Navbat va tokenlar

### P0 — hozir tuzatilmasa, “professional emas” bahosi qoladi

1. **O‘zbek yozuvi.** Barcha oʻ/gʻ ni bo‘shliqsiz U+02BB (ʻ) bilan qayta tering. U+0027 / U+2018 / U+2019 / U+02BC ni UI matnda U+02BB ga normalizatsiya qiling. Shrift: **Onest** (IBM Plex Sans emas). PDF/ekranda 16 px va 32 px da tekshirib chiqing.
2. **Qavslarni olib tashlang.** `[N]`, `[v2 spec]`, `[qonun moddasi]`, `[X] %`, `[asos]`, `xxxx` — demo taxtasida qolmasin. Muddatlarni v2 dan qo‘ying: deklaratsiya 15 kalendar kun (261-modda, 605-son 11-band); vaqtinchalik saqlash odatda 60 kun, tez buziladigan 10 kun (85-modda); dastlabki deklaratsiya odatda 30 kun (262-modda). Tekshirilmagan joyda “hozircha ko‘rsatmaymiz” deb yozing, qavs qo‘ymang.
3. **“Rasmiy” raqamlarni tekshiring.** Yig‘im 310 000 vs 1 BHM = 440 000 (PF-115, 01.09.2026). 10 % boj va 8539 52 000 0 — faqat NOTARIF / rasmiy jadval tasdiqlasa “Rasmiy · sana”. Aks holda “namuna” yoki “—” + “Stavka topilmadi”.
4. **Kesilgan taxtalarni yig‘ing.** 04+05, 10+11, 15+16, 17+18 — bir ekran, bo‘sh oq maydonsiz. CEO taqdimoti shu holda ham “tugallanmagan” ko‘rinadi.
5. **ERI handoff.** “Bu oyna kabinetniki, YuklaGo yozmaydi” — modal *ustida* yoki yonida, hech qachon orqasida. YuklaGo yuza qismida parol/kalit maydoni ko‘rinmasin.

### P1 — keyingi iteratsiya (jiddylik va to‘liqlik)

6. Mashq rejimi: brend andozasi — bitta grafit tasma (`#E8EBF1`, matn `#14152B`) + «MASHQ» yorlig‘i (`#3A4256` / oq) va kabinet URL qatoridagi kichik yorliq. Namuna: `/workspace/yuklago-brand/export/practice-banner.png`. Magenta chiziq, suv belgisi, pushti shapkani olib tashlang.
7. Mahsulotdagi “Prototip: jonli to‘ldirishni ko‘rsatish” tugmasini olib tashlang.
8. To‘ldirish paytida kabinetdagi “Imzolash va yuborish” ni xavfsiz qiling (o‘chiq yoki “hali bosmang” yozuvi).
9. To‘lov/grafa jadvallari: tabular raqam, “Jami” qatori ajratilgan, manba chipi qator yonida.
10. Bo‘sh / yuklanish / xato holatlari: bosh sahifa, hujjat yuklash, kirish (SMS), broker havolasi, kutubxona.
11. 24-sahifa relsini sessiya yakunidan keyin yangilang.
12. Sozlamalarda “ERI va kabinet” ning o‘z ekrani.
13. Mobil to‘plamni asosiy yo‘l bo‘yicha to‘ldiring (onboarding, yo‘l varaqasi, qoralama, broker).
14. Tugmalar: asosiy indigo `#2E2BA0`, ikkinchi oq + `#C5CCD8` + siyoh, vayron qiluvchi `#C0362C`. Qora, pushti, petrel, za’faron to‘ldirma yo‘q.
15. Landingni qayta: oq/sovuq fon, to‘g‘ri o‘zbek sarlavha, to‘liq sahifa, kamroq “jurnal”, ko‘proq “vosita”.

### P2 — keyinroq

16. Ruscha matn bilan qator uzunligini qayta tekshirish (rationale dagi 15–25 %).
17. “Xabarni tushunish” ni asosiy menyudan kontekstga ko‘chirish.
18. Ishonch paneli metodologiyasini yozish yoki olib tashlash.
19. Relsdagi “Shart emas” holatini ikonka+so‘z bilan yopish.
20. Harakat (motion) ni kam, 120–180 ms, `prefers-reduced-motion` bilan — rationale dagi qoida yaxshi, ekranlarda deyarli ko‘rinmaydi.

### Brend javoblari qo‘llandi

Brend Dizayner `brand.md` §4 va `brand-tokens.json` da javob berdi (CEO tasdiqlamaguncha yakuniy emas, lekin qurish uchun xavfsiz). Ohang: **jiddiy fintech** (Stripe / Wise / bank ilovalari), **davlat sayti emas**, Payme/Click kabi o‘ynoqi emas. Asosiy rang — indigo `#2E2BA0`; petrel `#0B5563` chiqarildi. Shrift — **Onest 400–700**, so‘m uchun `tabular-nums`. Logo — yo‘nalish **B «Varaq»**, so‘z belgisi bitta so‘z, bitta rang («YuklaGo»). Mashq rejimi — neytral grafit tasma (`#E8EBF1`, yorliq `#3A4256`).

Quyidagi UI tokenlari shu javoblardan olingan. Mashina o‘qiladigan fayl: `/workspace/hackathon/team-review/ui-tokens.json`. Kontrastlar WCAG 2.1 bo‘yicha **qayta hisoblandi** (18.11.2026).

### Shrift shkalasi (Onest)

Oilasi: `Onest, 'Noto Sans', system-ui, sans-serif`. Vaznlar: 400 / 500 / 600 / 700. oʻ/gʻ uchun U+02BB; IBM Plex Sans ishlatilmasin (U+02BB 0,60 em — «O ʻ zingiz»). Tekshiruv: `/workspace/yuklago-brand/font-test.png`. So‘m summalari — Onest + `font-variant-numeric: tabular-nums`, **mono emas**. JetBrains Mono faqat TIF TN, grafa raqami va URL uchun.

| Rol | O‘lcham / qator | Vazn | Qayerda |
| --- | --- | --- | --- |
| Display | 36 / 40, −0,02 em | 700 | Faqat tashqi landing |
| H1 | 28 / 34, −0,015 em | 700 | Ekran sarlavhasi |
| H2 | 20 / 28 | 600 | Bo‘lim |
| H3 | 16 / 24 | 600 | Karta sarlavhasi |
| Matn | 16 / 24 | 400 | Asosiy o‘qish |
| Izoh | 13 / 20 | 400 | Manba, yordam, chiplar |
| Summa | 14 / 20, tabular | 600 | Jadvallardagi so‘m (katta jami ham tabular) |
| Kod | 14 / 20, mono | 400 | TIF TN, grafa, URL |

### Oraliq to‘ri

Asos — **8 px**. Qator: 4, 8, 12, 16, 24, 32, 48, 64. Sahifa ichki bo‘shlig‘i 24–32, karta ichi 16–20. Bosiladigan nuqta kamida 48 px. Burchaklar: xs 4, sm 6, md 10, lg 14, xl 20, pill 999. Tasodifiy «letter» bo‘shliqlar yo‘q.

### Rang rollari

| Rol | Token | Hex | Ishlatilishi |
| --- | --- | --- | --- |
| Asosiy harakat | `brand.primary` | `#2E2BA0` | Tugma, havola, fokus halqasi. Hover `#24218A`, bosilgan `#1C1A70`, ustidagi matn oq `#FFFFFF` (10,66:1, AAA). |
| Tint | `brand.tint` | `#ECEBFA` | Tanlangan rels, yengil fon. Ustida `muted` qo‘yilmasin (qarang: kontrast). |
| Fon / sirt / botiq | `bg.canvas` / `surface` / `sunken` | `#F5F5FA` / `#FFFFFF` / `#EEEFF5` | Iliq beige yo‘q. |
| Siyoh | `text.ink` | `#14152B` | Asosiy matn, oqda 17,92:1 (AAA). |
| Ikkinchi / xira | `text.secondary` / `muted` | `#525570` / `#5E6178` | `muted` faqat oq yoki canvas ustida (AA). Sunken/tint ustida `secondary` yoki `ink`. |
| Chiziq | `border.line` / `strong` / `focusRing` | `#E1E2EC` / `#C5CCD8` / `#2E2BA0` | Fokus — indigo. Odatiy input chizig‘i zaif — pastdagi ogohlantirish. |
| Aksent (za’faron) | `brand.accent` | `#F5B43C` | **Faqat** logo burmasi (indigo ustida) va «Endi sizning navbatingiz». Tugma, havola, ogohlantirish **emas**. |
| Tugmalar | primary / secondary / destructive | indigo + oq; oq + `#C5CCD8` + siyoh; `#C0362C` + oq | Qora, pushti, petrel, za’faron to‘ldirma yo‘q. |

### Holat ranglari — doim ikonka + so‘z

Har bir holat matn rangi o‘z fonida WCAG AA (4,5:1) dan o‘tadi. Qattiq (solid) tugmada oq matn ham AA.

| Holat | Rol | Matn / fon / chiziq | Ikonka | So‘z | fg/bg | oq ustida fg | solid ustida oq |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Go | success | `#12795A` / `#E7F5EF` / `#B7DFCC` | Tekshirilgan doira | Tasdiqlangan, Yaxshi, Tayyor | **4,79:1 AA** | 5,37:1 AA | 5,37:1 AA |
| Caution | warning | `#A35C00` / `#FFF4E0` / `#F0D3A0` | Uchburchak | Diqqat, Tekshiring | **4,71:1 AA** (tor, lekin o‘tadi) | 5,14:1 AA | 5,14:1 AA |
| Stop | error | `#C0362C` / `#FDECEA` / `#F3C1BC` | X doira | Toʻsiq, Toʻxtang, Yetishmayapti | **4,83:1 AA** | 5,52:1 AA | 5,52:1 AA |
| Info | info | `#2457A6` / `#EAF1FB` / `#C3D5EF` | i doira | Maʼlumot | **6,18:1 AA** | 7,03:1 AAA | 7,03:1 AAA |
| Sizning navbatingiz | yourTurn | za’faron `#F5B43C` + oq matn, fon `#14152B` | Kalit / navbat belgisi | Endi sizning navbatingiz | za’faron/ink **9,79:1 AAA**; oq/ink 17,92:1 AAA | — | To‘liq sariq ekran qilmang |

Holat chiziqlari (`border`) o‘z fonlarida ~1,3:1 — bu yetarli emas, shuning uchun **ikonka va so‘z shart**. Rang yoki chiziq yolg‘iz signal bo‘lmasin.

### Mashq tasmasi (practice banner)

Namuna: `/workspace/yuklago-brand/export/practice-banner.png`.

- Ilovaning **eng tepasida bitta** grafit tasma: fon `#E8EBF1`, pastki chiziq `#C5CCD8`, matn `#14152B` (**15,01:1 AAA**).
- Yorliq: fon `#3A4256`, oq matn (**10,03:1 AAA**), so‘z **«MASHQ»**.
- Matn (UZ): «Mashq rejimi — bu haqiqiy bojxona kabineti emas. Hech narsa bojxonaga yuborilmaydi.» Havola: «Haqiqiy rejim haqida» (`#2E2BA0` tasma ustida **8,93:1 AAA**).
- Matn (RU): «УЧЕБНЫЙ РЕЖИМ — это не настоящий кабинет таможни. Ничего не отправляется.»
- Kabinet manzil qatorida ham kichik «MASHQ» yorlig‘i — skrinshot kesilsa ham ko‘rinsin. `mashq.yuklago.uz` — to‘rtinchi, jimgina signal.
- **Olib tashlanadi:** pushti-magenta chiziq, diagonal suv belgisi, pushti URL.

### Kontrast va qulaylik — Brend Dizaynerga ogohlantirish

Mustaqil hisob (WCAG 2.1). Brend bergan juftliklar (tugma, siyoh, holat fg/bg, mashq tasmasi, «navbatingiz») tasdiqlandi va AA/AAA dan o‘tadi. Uchta muammo:

1. **Za’faron `#F5B43C` och fonda yaroqsiz.** Oqda **1,83:1**, canvasda **1,68:1** — oddiy va katta matn uchun ham FAIL; alohida ikonka/grafika uchun ham 3:1 (WCAG 1.4.11) dan past. Oq matn za’faron ustida ham **1,83:1 FAIL**. **To‘g‘ri joy:** za’faron ink `#14152B` ustida 9,79:1 (AAA); indigo `#2E2BA0` ustida 5,83:1 (AA) — Varaq burmasi shu yerda, shu holatda saqlansin. Yorug‘ shapkada alohida za’faron ikonka yoki za’faron tugma (oq yozuv bilan) qilmang.
2. **`muted` `#5E6178` botiq va tint ustida AA dan o‘tmaydi.** Sunken `#EEEFF5` da **4,35:1**, tint `#ECEBFA` da **4,24:1** (kerak 4,5). Oqda 4,99 va canvasda 4,60 — o‘tadi. Botiq karta yoki indigo tint ustida `secondary` `#525570` (6,33 / 6,17) yoki `ink` ishlating.
3. **Input chizig‘i juda och.** `border.line` oqda 1,29:1, `border.strong` 1,62:1 — maydonning yagona ko‘rinadigan cheti sifatida 3:1 yetmaydi. Fokus halqasi `#2E2BA0` yaxshi (10,66:1). Hozircha UI tavsiyasi (brend tokenida yo‘q): `#84899A` (oqda 3,48:1, canvasda 3,21:1). Tasdiqlashingizni kutamiz.

Logo fayllari: `/workspace/yuklago-brand/export/` (lockup, mark, favicon, app icon). `theme_color`: `#2E2BA0`. So‘z belgisini qayta terilmasin.

---

## 6. Qisqa xulosa jamoa uchun

G‘oya va axborot arxitekturasi v2 yo‘lidagi yaxshi birinchi o‘tish. Sarvarbekning “rasmiy-professional emas” degan bahosi asosan **yozuv**, **joyi to‘ldirilmagan qavslar**, **kesilgan taxtalar**, **“Rasmiy” ostidagi shubhali raqam** va **beige + pushti maket ohangi** dan keladi — ekranlarning mantiqidan emas. P0 ni tuzatsangiz, ko‘p ekranlar saqlanib, jiddiy vosita kabi o‘qilishi mumkin.

Brend tomoni endi B «Varaq» + indigo + Onest ni tavsiya qildi. Keyingi UI iteratsiya shu tokenlarga (`ui-tokens.json`) tayanilsin; za’faronni och fonga matn yoki ikonka qilib qo‘ymang.

### Brend qarorlari (2026-11-18, Brend Dizayner tasdiqladi)
1. Za’faron faqat aksent/bezak: och fonda matn yoki alohida ikonka sifatida ishlatilmaydi, za’faron ustida oq matn ham bo‘lmaydi. Faqat ink `#14152B` yoki indigo `#2E2BA0` ustida qo‘llanadi.
2. `muted` endi `#5E6178`: sunken ustida 5,16:1, tint ustida 5,59:1, oq ustida 6,07:1, ya’ni hamma joyda AA dan o‘tadi.
3. `border.input = #84899A` tasdiqlandi va inputning yagona cheti shu rangda bo‘ladi. `line` va `strong` faqat bezak chiziqlari sifatida qoladi.
Yakuniy brend B ("Varaq") tasdiqlangan. Yakuniy spetsifikatsiya `/workspace/yuklago-brand/final/` da bo‘ladi.

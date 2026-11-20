# YuklaGo — mobil va kompyuter (jamoaviy ko‘rib chiqish)

**Kimga:** jamoa / CEOga qisqa yo‘l xaritasi.
**Asos:** `yuklago-spec-v2.md` (§8.1–8.2, Y3, Y8–Y9, Y14–Y20), dizayn v0.1 (`design-v0.1/yuklago-web-ui-v0.1.pdf`, 28 ta taxta + `design-rationale.md`), `ARCHITECTURE.md` qoidalari, va hozir ishlab turgan mobil PWA (`apps/web-mobile-ui`, schemas v0.1).

Bu hujjat huquqiy maslahat emas. Dizayndagi summalar (masalan, ≈ 67 823 600 so‘m, «9 kun») — **maket namunasi**, qonuniy hisob emas. Muddat moddalari dizaynda ham `[v2 spec]` deb ochiq qoldirilgan.

---

## 1. Nima telefonda, nima faqat kompyuterda

Spec v2 aniq aytadi: **uchta mijoz** — veb, desktop, mobil — bir backend. **Kabinetni to‘ldirish faqat desktopda.** Telefon USB-token bilan imzo qo‘ymaydi. Telegram-bot **mahsulot yuzasi emas** (eslatma kanali bo‘lishi mumkin — 4-bo‘lim).

| Funksiya | Mobil | Desktop / katta veb | Nega |
| --- | --- | --- | --- |
| Hujjatni suratga olish (ko‘p sahifa, kamera, sifat maslahati) | **Ha — asosiy joy** | Ha, lekin asosan PDF / fayl yuklash | Yo‘lda invoys va CMR ni telefon bilan olish oson. ERI / tokenni hech qachon suratga olmaslik kerak. |
| Sotib olishdan oldin yakuniy narx (Y3) | **Ha** | **Ha** | Qaror pul ketishidan oldin, ko‘pincha telefonda chiqadi. Hisobni UI yoki LLM emas, dvigatel qiladi; har bir rasmiy raqamda manba va sana bo‘ladi. Transport — taxmin (`≈`). |
| Deklaratsiya holati (Y19) | **Ha** (matn joylash yoki xabar suratini olish) | **Ha** | Rasmiy jonli API yo‘q. Bu «tushuntirish», ed2 ning o‘zi emas. |
| Muddat soati (Y8) | **Ha** | **Ha** | Arzon va ochiq API shart emas. Sanash serverda; telefon faqat ko‘rsatadi va eslatadi. |
| Bildirishnomalar (muddat, stavka o‘zgarishi) | **Ha** (PWA Web Push + ixtiyoriy Telegram/SMS) | Ha (brauzer) | iOS da cheklov bor — 3-bo‘lim. |
| Mahsulot kutubxonasi (Y20) | **Ha** (kartalar) | **Ha** (jadval ham bo‘ladi) | Takroriy tovar. Eski kod xato ko‘paytiradi — «qayta tekshirish» belgisi ko‘rinishi shart. |
| «Kompyuterga yuborish» (ERI qadamlari) | **Faqat havola / eslatma** | **Ha — to‘ldirish va imzo** | ERI odatda USB token. Telefon tokenni ushlamaydi, parol so‘ramaydi, kalitni yuklamaydi. |
| Kabinetni avtomatik to‘ldirish (Y14–Y16), pauza, jurnal | **Yo‘q** | **Faqat desktop** (mashq portali vebda ham, lekin katta ekranda) | Ikki panelli oyna, 1024 px, token plagini — telefonda buziladi. |

**Spec v2 va dizayn nimalarni «kompyuter» deb oladi — telefonda ishlamaydi:**

- Y14–Y16 va §8.2: ed2.customs.uz ni ichki brauzerda ochish, maydon yozish, Space bilan pauza, ERI kirish/imzo. Bu YuklaGo Desktop.
- Dizayn **p-18**: «Mashq sessiyasini boshlash — **Kompyuter kerak: kamida 1024 px ekran.** ERI tokenini shu kompyuterga ulang.»
- Dizayn **p-19…p-22**: chapda kabinet oynasi, o‘ngda YuklaGo relsi. Telefonda sig‘maydi.
- Dizayn **p-03 / p-09**: chapdagi bosqich relsi + yuqoridagi uzun yuk sarlavhasi (p-02). Tor ekranda yo‘qoladi yoki barmoqqa noqulay.
- Dizayn **p-07, p-15, p-25, p-27**: keng jadvallar (yuklar, 47-grafa to‘lovlari, 48 maydonli qoralama, mahsulot kutubxonasi, xavfsizlik jurnali).
- Dizayn **p-27**: «Bu kompyuter · Chrome, Windows» — token shu qurilmada.

Hozirgi mobil PWA da bu chiziq allaqachon bor: imzo ekrani egasini o‘z kabinetiga yo‘llaydi, ERI yuklanmaydi. Dizayn **p-28** dagi «Kompyuter uchun havolani yuborish» — shu yo‘lning to‘g‘ri davomi.

---

## 2. Dizayn v0.1 ni mobil uchun nima o‘zgartirish kerak

Dizayn «web, desktop, mobile» deb yozilgan, lekin taxtalarning ko‘pi **keng ish stoli**. Mobil uchun bitta yig‘iq lavha bor: **p-28** (4 ta telefon: bosh, narx, surat+tekshiruv, kabinet o‘rniga havola). Bu yaxshi boshlanish, lekin yetarli emas.

Umumiy qoidalar (barcha ekran):

- Tugma va tab **kamida 44×44 px**.
- Jadval → **karta**. Chap rels → **pastki tab** (p-28 dagi yo‘nalish).
- Asosiy tugma **pastda yopishqoq** (sticky CTA); kontent uning ostida yo‘qolmasin.
- Uzun so‘m («67 823 600») — raqam alohida qatorda, mono shrift, qisqartirmaslik. Yonida manba/sana chipi **kesilmasin**, pastga tushsin.
- Har bir pul raqamida **manba, sana** va kerak bo‘lsa **namuna / taxminiy / ≈ taxmin / mock (MASHQ)** yorlig‘i kichik ekranda ham ko‘rinsin.
- Oflayn va sekin tarmoq: «saqlangan namuna», «yuborilmadi — qayta urinib ko‘ring». Hozirgi taxtalarda bu holat yo‘q.

**Taxta bo‘yicha:**

| Taxta (PDF sahifa) | Ekran | Mobil uchun o‘zgarish |
| --- | --- | --- |
| **p-01** | Dizayn tizimi | Chip’lar (Rasmiy · sana, ≈ Taxmin, Taklif…) tor joyda ikki qator bo‘lsin. Hozirgi PWA yashil/namuna uslubini keyin shu tizimga (petrol, IBM Plex) birlashtirish kerak. |
| **p-02** | Yuk sarlavhasi (umumiy komponent) | Muddatlar + «Brokerga topshirish» bir qatorda sig‘maydi. Pastga yoki qisqa kartaga tushiring. |
| **p-03** | Chap bosqich relsi | Telefonda chapga qo‘ymang. Holatni bitta «keyingi qadam» kartasi va pastki tab bilan bering. |
| **p-04** | Landing | Ikki ustunli hisobni bitta ustunga yig‘ing; CTA pastda yopishqoq. |
| **p-05** | Kirish (SMS kod) | Ikki kartani ustma-ust qo‘ying. Tugma 44 px. ERI paroli so‘ralmasligi haqidagi yozuv **saqlansin** — bu to‘g‘ri. |
| **p-06** | Yo‘l tanlash / «O‘zim topshira olamanmi?» | Savol variantlari katta, barmoqqa qulay bo‘lsin (hozirgi PWA dagi kabi). |
| **p-07** | Bosh sahifa | «Yuklar» jadvali kartalarga o‘tsin (p-28 dagi kabi). Yuqori tab (Bosh, Yuklar, Mahsulotlar, Xabarni tushunish) telefon uchun haddan tashqari ko‘p — pastki 4 tab. |
| **p-08** | Yangi yuk sehrgari | Qadamlar vertikal; «Keyingi» pastda yopishqoq. |
| **p-09** | Yuk ish maydoni + muddatlar | Relsiz. Bitta katta muddat (daysLeft serverdan). «Eslatma: SMS va Telegram» ni sozlama sifatida qoldiring. `[N] kun` ni UI da o‘ylab to‘ldirmang — backend / mutaxassis beradi. |
| **p-10** | Kelib tushgan narx | p-28 dagi yig‘iq kartaga o‘ting. Pastki «Kod boshqacha bo‘lsa» va kargo **jadvali** kartaga aylansin. «Rasmiy · 01.11.2026» chipi raqam ostida to‘liq ko‘rinsin. |
| **p-11** | Imtiyoz + E-kontrakt | Tejash summasini o‘ylab yozmang (spec Y5). Uzun matn va so‘rov shablonini varaqda aylantirish oson bo‘lsin. |
| **p-12** | Jo‘natishdan oldin (ruxsatnomalar) | Yashil/sariq/qizil ro‘yxat allaqachon karta — yaxshi. Chap relsni olib tashlang. |
| **p-13** | Hujjatlar | «Yuklash yoki suratga olish» — asosiy CTA. Ko‘p sahifa (1/n), kamera (`capture=environment`), sifat: qorong‘i, blur, qirqilgan chet, «tokenni suratga olmang». O‘ngdagi maydon ro‘yxati surat ostida, bir-bir. Oflayn: rasm qurilmada qolsin, keyin yuborilsin. |
| **p-14** | TIF TN kodi | Taklif + tasdiq katta tugma; «bu rasmiy qaror emas» yozuvi yashirilmasin. |
| **p-15** | To‘lovlar va qoralama (47-grafa + 48 maydon) | Ikkala **jadvalni** xato/qator kartalariga bo‘ling (hozirgi PWA qoralama ekrani kabi). Sticky: «To‘siqni tuzatish» / «Kompyuterga yuborish». |
| **p-16** | Darvoza (to‘ldirish yopiq) | Sabab qisqa; keyingi tugma pastda. |
| **p-17 / p-18** | Kabinetni boshlash | Telefonda p-18 dagi 1024 px ogohligi o‘rniga **p-28**: «Bu qadam kompyuterda» + havola. «Mashqni shu yerda ochish» ni telefondan olib tashlang. |
| **p-19…p-22** | To‘ldirish, pauza, ERI navbati, xato | **Faqat desktop.** p-21 dagi «ERI bilan imzolash» oynasi — **kabinetniki (maket)**, YuklaGo formasi emas. Uni telefon UI ga ko‘chirmang: bu kalit/parol so‘rashga o‘xshab ketadi. |
| **p-23** | Sessiya jurnali | Telefonda qisqa lenta; CSV/PDF — «kompyuterda ochish». Parol/PIN yozilmasin (allaqachon to‘g‘ri aytilgan). |
| **p-24** | Topshirilgandan keyin / xabarni tushunish | Xabar suratini olish + matn joylash — mobilga mos. «Jonli bojxona lenti» deb ko‘rsatilmasin. |
| **p-25** | Mahsulotlar kutubxonasi | Jadval + o‘ng panel → ro‘yxat kartalari. «Stavka o‘zgargan bo‘lishi mumkin» belgisi katta va ochiq qolsin. |
| **p-26** | Brokerga topshirish | Telegram/havola tugmalari 44 px; «kalit ketmaydi» yozuvi qolsin. |
| **p-27** | Sozlamalar | Jadvalni ro‘yxat qiling. Eslatma ruxsati (Web Push) va «bu qurilma — telefon, ERI yo‘q» aniq aytilsin. |
| **p-28** | Mobil yig‘ma (4 telefon) | Yo‘nalish to‘g‘ri. Yetishmaydi: Mahsulotlar va Muddat tab yoki ularga kirish; ko‘p sahifali kamera; oflayn holat; tab yozuvlari kichik — 44 px qiling. Hozirgi PWA tablar (Bosh, Narx, Muddat, Tovarlar) bilan kelishib oling. |

---

## 3. Stek taklifi

### Variant A — tavsiya (hakaton va yaqin muddat)
**Bitta Next.js 15 App Router ilova, o‘rnatiladigan PWA** (allaqachon `/workspace/yuklago/apps/web-mobile-ui` da qurilgan, schemas v0.1 ulangan, `next start` ishlayapti). Telefon va veb bir kod. Kameraga `<input capture>`, muddat, narx, kutubxona, «namuna / taxminiy» yorliqlari bor.

Eslatma: **Web Push** (PWA) + ixtiyoriy **Telegram-bot faqat eslatma uchun** (muddat, stavka o‘zgarishi). Bu mahsulotning o‘zi Telegram emas — spec §8.1 dagi chiziqni buzmaydi, lekin jamoa tasdiqlasin.

**iOS haqida ochiq gap:** Web Push **faqat** ilova Home Screen ga o‘rnatilganda ishlaydi, va **iOS 16.4+** kerak. Oddiy Safari ichida ochilsa, push bo‘lmaydi. Android da osonroq. Shuning uchun faqat brauzer pushiga tayanmang — Telegram/SMS zaxira bo‘lsin.

Desktop kabinet (Y14) keyin shu backend ustiga **alohida desktop qobiq** (masalan, Electron yoki Tauri) bilan qo‘shiladi. Telefon kabinetni ochmaydi.

### Variant B — hakatondan keyin, kerak bo‘lsa native
**Expo / React Native** yoki **Flutter** — agar bular og‘irlasha boshlasa: iOS da ishonchli push, yaxshi kamera (ko‘p sahifa, chiroq, nishon), App Store / Play orqali tarqatish, fon eslatmalari. Narx: ikkinchi kod bazasi, do‘kon tekshiruvi, uzoqroq chiqarish.

### Variant C — hozir ikkala bazani yozish
PWA + native bir vaqtda. Hakaton uchun og‘ir, sekin, tavsiya etilmaydi.

**Xulosa:** hakatonda **A**. Native ni faqat foydalanuvchi «o‘rnatilgan PWA + Telegram eslatma yetarli emas» deb chiqsa, keyin boshlang.

---

## 4. Ochiq savollar va xavflar

1. **ERI chizig‘i.** ARCHITECTURE va spec v2 bir xil: kalit yuklanmaydi, saqlanmaydi, o‘rniga imzolanmaydi. p-21 maket oynasi kabinet ichida qolishi shart. Agar kimdir shu formani telefonga qo‘ysa — bu qoida buziladi.
2. **LLM pul hisoblamaydi.** Spec Y11 / §8.4 buni tasdiqlaydi. Dizayn chiplarida «Rasmiy» va «≈ taxmin» bor — to‘g‘ri. Hech qayerda model «jami ni o‘zi sanasin» deyilmasin.
3. **Telegram.** Spec: bot mahsulot yuzasi emas. Dizayn p-09: «SMS va Telegram orqali eslatma». Jamoa: eslatmagina yoki umuman yo‘q?
4. **Dizayn tizimi ikkita.** v0.1 — petrol, IBM Plex, «Rasmiy / ≈ Taxmin». Hozirgi PWA — yashil, «namuna / taxminiy». Hakaton demosida bittasini tanlang, keyin birlashtiring.
5. **Huquqiy ochiq savol:** haqiqiy ed2 ni avtomatlashtirish. Telefonda bu yo‘q; demo — faqat MASHQ. «Biz bojxonaga avtomatik topshiramiz / sizning o‘rniga imzolaymiz» deb aytilmasin.
6. **Dizayn maket raqamlari** (9 kun, 67,8 mln so‘m, 5 480 000 boj) qonun emas. Muddat matni `[v2 spec]` da qolgan — to‘ldirish mutaxassis ishi, UI o‘zi sanamasin.
7. **p-28 tablar** (Bosh, Yuklar, Suratga olish, Narx) va PWA tablar (Bosh, Narx, Muddat, Tovarlar) hali kelishilmagan.
8. **Oflayn / yomon tarmoq** dizaynda yo‘q — yo‘lda hujjat olish shu yerda sindishi mumkin.


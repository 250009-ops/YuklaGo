# YuklaGo — Rollar, ruxsatlar va audit (3 rol)

Sana: 2026-11-19 (Toshkent vaqti). Asos: `yuklago-spec-v3.md` (topildi), `security.md`, `legal.md`. Yuridik xulosa emas. Iqtiboslar faqat 2026-11-18/19 da o'zim ochgan lex.uz sahifalaridan.

## 1. Rollar
1. **Foydalanuvchi / Egasi** — yagona mijoz roli. O'zi bajaradi:
   - hujjat yuklash va tayyorlash, kod va to'lovlarni tasdiqlash;
   - to'lash (o'z bankida, spec Y28);
   - imzolash va yuborish — ed2 da, o'z ERI si bilan (spec Y16).
   - ed1 dagi imzolovchi ro'yxati setup'da bir marta tekshiriladi (3-bo'lim).
2. **YuklaGo Support** — Egasining roziligi bilan, muddatli sessiya orqali kiradi. Faqat maskalangan ma'lumotni ko'radi, har bir harakati logga yoziladi.
3. **YuklaGo Admin** — tariflar, kalendar, konfiguratsiya va feature flag'lar bilan ishlaydi (spec AC-8.1c, AC-13.1b). Mijoz hujjatlariga kirish yo'q.

## 2. Ruxsatlar matritsasi
| Harakat | Egasi | Support | Admin |
|---|---|---|---|
| Ko'rish — hujjatlar va qoralama | ✓ | Faqat aktiv rozilik davomida, **maskalangan** ko'rinishda | ✕ |
| Ko'rish — maskalanmagan shaxsga doir ma'lumot (F.I.Sh., JShShIR, pasport, telefon) | ✓ | ✕ | ✕ |
| Tahrirlash / tayyorlash | ✓ | ✕ (faqat izoh yoki tavsiya qoldiradi) | ✕ |
| Imzolash / yuborish (ed2) | ✓ — faqat ed2 da, lokal E-IMZO bilan | ✕ | ✕ |
| To'lash | ✓ — o'z bankida | ✕ | ✕ |
| Eksport (audit paketi, PDF/CSV, o'z logi) | ✓ — step-up bilan | ✕ (maskalanmagan eksport yo'q) | ✕ |
| Konfiguratsiya (tariflar, kalendar, tolerance, flag'lar) | ✕ (faqat o'z hisobi sozlamalari) | ✕ | ✓ — logga yoziladi |
| AI roziligi berish / qaytarib olish | ✓ | ✕ | ✕ |
| Support'ga kirish ruxsatini berish / bekor qilish | ✓ | ✕ | ✕ |
| Audit logni o'qish | ✓ — o'zinikini | Faqat o'z sessiyasiniki | Faqat konfiguratsiya logi |

## 3. Imzolovchi tekshiruvi (VM 605, 15-band)
- **15-band, 2-bosqich** (https://lex.uz/docs/3844549, VM 700 tahririda, 08.02.2026 dan):
  > "декларант ТИФ иштирокчиси кабинети орқали рўйхатдан ўтган ҳолда ТИФ иштирокчилари рўйхатига ишонч билдирган шахс, божхона брокери ёки ўз штат бирлигида бўлган божхона расмийлаштируви бўйича мутахассиси тўғрисидаги маълумотларни ҳамда ... ТЭДни тақдим этиш ваколат муддатларини киритади"

  Xuddi shu bandda: "Декларацияловчи шахс ... ТЭДни шакллантиради, ўз ЭРИси билан тасдиқлаб, БҚ ЯААТ орқали ... юборади".
- 28-band: imzolovchi — ERI kaliti egasi bo'lgan jismoniy shaxs.
- **Setup'da bir marta tekshiriladi:** Egasi ed1 ro'yxatini o'zi tasdiqlaydi. YuklaGo kabinetni o'qimaydi (CABINET_STATUS_READ=off).
- **Tekshiruv o'tmasa:** Y14/Y16 qulflanadi, sabab "imzolovchi ro'yxatda emas" deb ko'rsatiladi (AC-1.2).
- **Qayta tekshiruv:** E-IMZO ko'rsatgan sertifikat egasi o'zgarsa yoki ed1 vakolat muddati tugasa.

## 4. Vazifalarni ajratish (SoD) qoidalari
1. **Xodimlar hech qachon imzolamaydi, yubormaydi va to'lamaydi.** Mijozning ed1 ro'yxatiga kirmaydi (spec R38, AC-1.4). Aks holda broker faoliyati xavfi paydo bo'ladi (BK 15, 277 — https://lex.uz/docs/2876354).
2. **ERI faqat Egasining qurilmasida:** kalit, PIN va parol o'qilmaydi va saqlanmaydi (ZRU-793 27-modda — https://lex.uz/docs/6234904).
3. **Support va Admin — alohida xodim akkauntlari**, bitta odamda ikkala rol bo'lmaydi. Xodim akkauntlarida majburiy 2FA.
4. **Hech kim o'ziga Support kirishini bera olmaydi.** Kirish faqat Egasining roziligi bilan ochiladi:
   - sabab ko'rsatiladi;
   - muddat belgilanadi (standart 24 soat), muddat o'tgach avtomatik yopiladi;
   - Egasi istalgan payt bekor qiladi.
   Asos: ZRU-547 28-modda — subyekt roziligisiz oshkor qilmaslik (https://lex.uz/docs/4396419).
5. **Admin mijoz ma'lumotini ochadigan flag'ni yoqa olmaydi:**
   - bunday flag'lar (masalan, maskalashni o'chirish, CABINET_STATUS_READ, ED2_LIVE_AUTOMATION) ikki kishi tasdig'i bilan yoqiladi — ulardan biri mas'ul shaxs;
   - yoqish logga yoziladi.
   Asos: ZRU-547 27-modda (maxfiylik choralari) va 31-modda (zarur va yetarli tarkib; mas'ul bo'linma yoki mansabdor shaxsni belgilash).
6. **Egasi uchun step-up:** to'lov va imzo bosqichiga o'tish, eksport va hisobni o'chirishda qayta SMS-kod so'raladi.
7. **Yangi qurilmadan kirish** bo'lsa, Egasiga darhol xabar boradi va sessiyani o'chirish imkoni beriladi.
8. **Bitta rol xavfi:** akkaunt o'g'irlansa, to'liq nazorat begona qo'liga o'tadi. 6–7-qoidalar shu xavfni kamaytiradi.

## 5. Audit qoidalari
- **Nima yoziladi:**
  - kim (Egasi / Support / Admin), qachon, qayerdan (qurilma);
  - nima qilingan — maydon, qiymat hashi, manba, qayta o'qish natijasi;
  - rozilik berish va bekor qilish, Support sessiyalari, konfiguratsiya va flag o'zgarishlari, eksportlar, kirishlar.
- **Nima yozilmaydi:** parol, PIN, kalit, login va imzo oynalari.
- **Tamper-evident:** append-only, hash-zanjir; eksportda oxirgi hash ko'rsatiladi.
- **Kim o'qiydi:**
  - Egasi — o'z logini;
  - Support — faqat o'z sessiyasini;
  - Admin — faqat konfiguratsiya logini;
  - mas'ul shaxs — hodisa yuz berganda.
- **Saqlash:**
  - to'liq qiymatlar qurilmada qoladi, serverga faqat hash boradi (engineering.md);
  - server logi O'zbekistonda, belgilangan muddat bilan (taklif: 3 yil — tasdiqlanmadi);
  - ZRU-764 16-modda bo'yicha raqamli izlarni saqlash (https://lex.uz/docs/5960604; taalluqliligi aniq emas).
- **Eksport:** Egasi o'z logini PDF yoki CSV ko'rinishida yuklab oladi.

## 6. Spec v3 dagi bo'shliqlar (PM uchun)
1. Rollar bo'limi yo'q — 3 rol va ushbu matritsa §6.5 ga qo'shilsin.
2. Support kirish oqimi (rozilik, muddat, maskalash, log) uchun AC yo'q.
3. Admin uchun "mijoz ma'lumotiga kirish yo'q" chegarasi va ikki kishilik flag tasdig'i AC-8.1c/AC-13.1b da aytilmagan.
4. Step-up tasdiq (to'lov/imzo/eksport) va yangi qurilma xabari AC sifatida yo'q.
5. Sertifikat o'zgarishi yoki ed1 vakolat muddati tugashida qayta tekshiruv yo'q — Y1 faqat setup'ni qamraydi.
6. **Imzolovchi Egasi bo'lmasa** (shtatdagi mutaxassis): bitta mijoz roli akkauntni birgalikda ishlatishga olib keladi. Qaror kerak: mutaxassis imzoni o'z qurilmasida, o'z ERI si bilan qo'yadi, lekin akkaunt Egasiniki — PM/CEO.
7. ZRU-547 31-modda bo'yicha mas'ul shaxs tayinlanmagan.
8. Audit log serverga yuklash (automation.md Q7) va saqlash muddati ochiq.
9. 15-band ro'yxatga "ишонч билдирган шахс" ni ham kiritadi, lekin 2-banddagi "декларацияловчи шахс" ta'rifida u yo'q. U imzolay oladimi — **tasdiqlanmadi** (spec R3/PC-5 bilan mos).

## Q-21. Sertifikat maydonlari orqali imzolovchi o'zgarishini avtomatik aniqlash

**Javob: HA, shartlar bilan.** Faqat **ochiq sertifikat** maydonlari o'qiladi. Yopiq kalit, parol va PIN ishlatilmaydi.

**Faktlar (o'zim ochdim, 2026-11-19):**
- **ZRU-793 3-modda** (https://lex.uz/docs/6234904): ochiq kalit — "ахборот тизимининг ҳар қандай фойдаланувчиси учун очиқ"; sertifikat — ochiq kalit yopiq kalitga mosligini tasdiqlovchi elektron hujjat. Ya'ni sertifikat tekshiruvchi tomonlarga ko'rsatish uchun mo'ljallangan.
- **ZRU-793 24-modda** — sertifikatda ko'rsatiladi:
  - jismoniy shaxsning F.I.Sh. va **shaxsiy identifikatsiya raqami (JShShIR/PINFL)**;
  - yuridik shaxsning nomi, manzili va **identifikatsiya raqami (STIR)**;
  - seriya raqami va amal qilish muddati;
  - ochiq kalit;
  - foydalanish maqsadi;
  - registratsiya markazi.
- **E-IMZO API**: ed2 o'zi yuklaydigan `e-imzo-client.js` (https://ed2.customs.uz/eri_new/e-imzo-client.js). Bu E-IMZO ishlab chiqaruvchisining rasmiy hujjati emas — rasmiy hujjat **tasdiqlanmadi**.
  - `list_all_certificates` (pfx plugin) va token ro'yxati **parolsiz**, lokal qaytaradi: `serialNumber`, `validTo`, `CN`, `TIN` (INN/UID), `PINFL`, `O`.
  - Parol faqat keyingi `load_key` bosqichida so'raladi.
- **ZRU-547** (https://lex.uz/docs/4396419):
  - **4-modda** — shaxsga doir ma'lumot: "муайян жисмоний шахсга тааллуқли бўлган ёки уни идентификация қилиш имконини берадиган" ma'lumot. → PINFL, F.I.Sh. va YaTT STIR shaxsga doir ma'lumot. Yuridik shaxs STIR i — emas (legal.md 3.4).
  - **19-modda** — hajm va xususiyat maqsadga mos bo'lishi kerak; ishlov berish "идентификация қилишга йўл қўйиладиган шаклда ёки эгасизлантирилган тарзда"; maqsad o'zgarsa — yangi rozilik.
  - **21-modda** — rozilik uning olinganini tasdiqlash mumkin bo'lgan shaklda olinadi.
  - **PINFL saqlash bo'yicha alohida qoida** ZRU-547 da topilmadi. Boshqa aktlarda bormi — **tasdiqlanmadi**.

**Dizayn (tavsiya):**
1. **O'qish.** Faqat imzolovchini tekshirish maqsadida o'qiladi: `PINFL`, `TIN`, `serialNumber`, `validTo`. `CN` faqat ekranda ko'rsatish uchun, saqlanmaydi.
   - Faqat `list_all_certificates` / token ro'yxati chaqiriladi. `load_key` va imzolash funksiyalari YuklaGo kodida **taqiqlangan** (deny-list, spec AC-16.2 kabi).
   - ⚠ YuklaGo ilovasi E-IMZO ga o'zi ulanishi uchun **o'z domeni uchun E-IMZO API kaliti** kerak. Olish tartibi **tasdiqlanmadi**. ed2 JS dagi `localhost`/`127.0.0.1` kalitlarini qayta ishlatish mumkin emas — bu aylanib o'tish bo'ladi.
   - ed2 sahifasi DOM idan o'qilmaydi (CABINET_STATUS_READ=off).
   - Bu security.md 1.1 dagi "Desktop E-IMZO ga o'zi ulanmaydi" qoidasiga istisno: faqat ro'yxat funksiyasi uchun. security.md shunga mos yangilanadi.
2. **Taqqoslash — PM taklifiga tuzatish.**
   - "Lokal taqqoslash + server kalitli HMAC" birga ishlamaydi: HMAC kaliti klientga berilsa, sir bo'lmay qoladi.
   - PINFL 14 xonali va tuzilmali, shuning uchun oddiy tuzli (salted) hashni oflayn brute-force qilish mumkin — **HMAC shart**.
   - **Tavsiya: serverda taqqoslash.** Klient PINFL/STIR ni TLS orqali `signer-check` endpoint'iga yuboradi. Server uni xotirada `HMAC-SHA256(KMS kaliti O'zbekistonda, akkaunt_id ‖ qiymat)` ga aylantiradi va saqlangan hash bilan solishtiradi. Javob: `match` / `mismatch`. Raw qiymat diskka yozilmaydi va logga tushmaydi.
3. **Saqlash.** Faqat quyidagilar saqlanadi:
   - PINFL va STIR ning HMAC'i, sertifikat seriya raqamining HMAC'i;
   - `validTo` — muddat eslatmasi uchun;
   - maskalangan ko'rinish: PINFL `••••••••••1234`, ism bosh harflari.
   - Yuridik shaxs STIR i to'liq ko'rsatilishi mumkin (u shaxsga doir ma'lumot emas).
4. **Log** (raw qiymatlarsiz): `signer_match`, `signer_mismatch`, `cert_changed`, `cert_expiring`, `cert_expired`. Har birida vaqt, qurilma va seriya raqami hashi.
   - `mismatch` bo'lsa, Y14/Y16 qulflanadi va Egasiga xabar boradi (4-bo'lim, 7-qoida).
5. **Rozilik qatori** (setup ekranida, Y32 rozilik versiyasiga qo'shiladi):
   > "Imzolovchi oʻzgarmaganini tekshirish uchun ERI sertifikatingizdagi JShShIR va STIRni oʻqiymiz. Ular faqat shifrlangan hash koʻrinishida saqlanadi. Kalit va parolingizga tegmaymiz."
6. **"Men imzolovchiman" bir bosishli tasdig'i: saqlanadi, lekin faqat 2 holatda:**
   - (a) **setup'da** — YuklaGo ed1 ro'yxatini o'qimaydi, shuning uchun "bu sertifikat egasi ed1 ro'yxatida, vakolat muddati amalda" degan tasdiqni faqat foydalanuvchi bera oladi (VM 605 15-band; spec AC-1.2);
   - (b) **mismatch yoki yangi sertifikatdan keyin** qayta tasdiq.
   - Har sessiyadagi tasdiq **olib tashlanadi** — uning o'rnini avtomatik tekshiruv bosadi.

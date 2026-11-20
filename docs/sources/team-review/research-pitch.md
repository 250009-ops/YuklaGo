# YuklaGo — team review: trust, interviews, and pitch

**Prepared:** 18 November 2026, Tashkent time (UTC+5).  
**For:** hackathon team / CEO. **Not legal advice.** No figures here are market facts; UI amounts are labelled sample data in the design, and interview boxes are empty until a real person states a number.

**Sources opened this turn**

- `/workspace/hackathon/yuklago-spec-v2.md` (Product Specification v2)
- `/workspace/hackathon/yuklago-web-design-brief.md`
- `/workspace/hackathon/design-v0.1/design-rationale.md`
- `/workspace/hackathon/design-v0.1/yuklago-web-ui-v0.1.pdf` — 28 boards; text extracted; pages rendered at 110 dpi to `/tmp/yg-shots/`
- `/workspace/yuklago/intervyu-skriptlari.md` — trimmed below, not replaced
- Earlier process/competitor notes only for terminology (`deklarant-jarayoni.md`, `raqobatchilar.md`), not as new evidence

Page numbers below refer to that PDF.

---

## 1. Short verdict

The product thinking is unusually careful for a hackathon: provenance chips, a plain “what we don’t do” block, no payment guarantee, no ST-1 routing tip, no named-competitor attacks, a clearly marked practice cabinet, and a hard stop at ERI. That is the right trust architecture.

What a small importer and a judge actually *see* first is weaker. Uzbek typography is broken across the boards (`oʻ` / `gʻ` render as `o ' z`, so the hero reads “Deklaratsiyani o ' zingiz topshiring”). Several screens still show `[v2 spec]`, `[N] kun`, and `[qonun moddasi]`. PDF pages 16 and 18 are cut off. And the hero promise — “Deklaratsiyani o‘zingiz topshiring” plus filling “bojxona kabinetingizni ko‘z oldingizda” — sits next to a screen that says real `ed2.customs.uz` fill is **not enabled**, because the legal question is still open. Honesty on that screen is a strength; leaving the landing as if self-filing is already live is the main reason the “no broker needed” line is hard to believe today.

---

## 2. Through a small importer’s eyes

**What would feel trustworthy**

- The landing (p.4) speaks in ordinary steps — before paying, before shipping, after arrival — and says in plain language that the person who signs is legally responsible.
- Numbers on the sample “kelib tushgan narx” card are tagged *Invoysdan*, *≈ taxmin*, or *Rasmiy* with a date. The design system (p.1) makes that a rule, not decoration.
- Cargo compare (p.10–11) does not invent a “typical $/kg”. It asks for the user’s own quote and warns: the comparison is only fair if everything is in the kargo price; ask in whose name the declaration is filed, and whether you get copies of the customs documents.
- Preference (p.11) is an entitlement check, not a routing tip: “Faqat tovaringiz allaqachon mos keladigan imtiyozni ko‘rsatamiz. Yuk yo‘nalishini o‘zgartirish bo‘yicha maslahat bermaymiz.”
- Broker hand-off is always in the header (“Brokerga topshirish”). It is framed as a normal exit, not a failure (p.26): the checked pack goes with the job.
- Settings and the ERI hand-off (p.17, p.21, p.27) repeat: YuklaGo never asks for the key or password; if someone asks in YuklaGo’s name, that is fraud.

**What would make them doubt — with screen evidence**

1. **The site cannot write their language cleanly.** On p.4 the hero is “Deklaratsiyani o ' zingiz topshiring”; the primary button is “Ro ' yxatdan o ' tish”; “so‘m” becomes “so ' m”. The same gap appears on the type scale (p.1, “O ' zingiz topshiring”), home (p.7, “g ' iloflari”, “To ' siq”), code (p.14), and cabinet (p.17, “Kabinetni to ' ldirish”). A shop owner in Abu Saxiy will read this as careless, or as a tool not really made for Uzbek.
2. **“File it yourself” arrives before they have the official keys.** Home (p.7) already warns: “O‘zingiz topshirish uchun ERI tokeni va kabinetga kirish hali tayyor emas.” Path choice (p.6) is honest that YuklaGo does not issue ERI or open the cabinet. For someone who today only uses kargo, that is a different, heavier life (YaTT/company, USB token, `ed2.customs.uz`) than the hero line suggests.
3. **The scary true sentence may send them back to kargo.** “Imzo qo‘ygan shaxs qonun oldida javob beradi” (p.4) and the code tick “deklaratsiyani imzolaganda kod uchun men javob beraman” (p.14) are legally right. Without a broker or a kargo firm in the middle, many first-time importers will hear: if this is wrong, it is on me. The design does not yet have interview proof that they will accept that trade.
4. **Unfinished legal text inside a live-looking workspace.** Home (p.7) shows “Manba: [qonun moddasi]”, “Saqlash: [N] kun”, and “Muddat uzunligi faqat rasmiy manbadan olinadi: [v2 spec, “Muddatlar”]”. Contract/bank (p.11) still has “[shartlar — v2 spec]”. A user will not trust a deadline that is a placeholder.
5. **Real cabinet fill is off.** “Qayerga to‘ldiramiz?” (p.17) offers: practice portal `mashq.yuklago.uz`; real `ed2.customs.uz` via Desktop — “Hozircha yoqilmagan: rasmiy saytni avtomatik to‘ldirishning huquqiy masalasi hal qilinmoqda”; or manual copy-assist. If they came for “we fill your customs cabinet in front of you,” the working path today is a rehearsal site or typing it themselves.

---

## 3. Through a hackathon judge’s eyes

**What looks official-grade**

- A complete design system with a clear brand idea (“calm ledger, not a cockpit”), no flag colours, no seals, and an explicit line that YuklaGo is an independent tool and must never look official (p.1; footer p.5: “mustaqil xizmat. Davlat organi emas…”).
- Interaction depth that is rare in a weekend demo: field-level read-back, pause-on-click, mock vs real markings (magenta hatch, “MASHQ REJIMI · HAQIQIY BOJXONA KABINETI EMAS”, diagonal watermark — p.19–22), a failure state that stops and says “Hech narsa yuborilmagan. Kabinetdagi qoralama imzolanmagan” (p.22), and a session log that labels each line “Siz” or “YuklaGo” and lists what is never recorded (p.23).
- Limits are written in the UI, not only in a spec: no payment guarantee (p.4, p.10), code is a suggestion not a binding classification (p.14), no live customs feed (p.7, p.24), no invented kargo tariff (p.10).

**What would make a judge doubt — with screen evidence**

1. **Same typography break, at display size, on the first slide they will photograph.** If the national-language headline is cracked, “official-grade” is a hard sell, no matter how good the system page is.
2. **The distinctive filing feature is a mock.** Spec v2’s differentiator is a desktop app that fills the user’s own `ed2.customs.uz` cabinet and stops at ERI. P.17 says that mode is not enabled, pending a legal decision. A judge who has seen InCustoms / DeklarantUZ will ask what is *demonstrably* different *today*. The honest answer is: pre-purchase landed cost, cargo compare from the user’s quote, a go/no-go before shipping, and a *practice* cabinet-fill. That is a real story. Claiming “no broker needed, we file in the official cabinet” is not, yet.
3. **The PDF is not presentation-ready.** Pages 16 and 18 are almost empty: p.16 is only the cropped tail of the payments/review screen (“Ochilmaydi: 1 ta to‘siq bor (38-grafa)…”); p.18 is only the tail of the cabinet-start screen. Placeholders (`[v2 spec]`, `[N]`, `[kelishuv nomi]`, `[TIF TN ro‘yxatidagi matn]`, `[ERI beruvchi markaz va manzil — v2 spec]` on p.6) will read as unfinished homework if left in a demo.
4. **Hero copy overreaches the build.** “Kabinetingizni ko‘z oldingizda to‘ldiradi” (p.4) is present tense. The only cabinet a judge can be shown is `mashq.yuklago.uz`.
5. **No customer proof yet.** Spec v2 already flags the kargo-replaces-BYD path as a hypothesis to confirm in interviews, and names a proof point that is not in hand (reproduce one accepted declaration’s payments to the so‘m). A judge will notice the absence.

Do not show p.16, p.18, or any board still carrying `[v2 spec]` / `[N] kun` in a judged demo. Fix typography before screenshots go on a slide.

---

## 4. Risky claims and safer wording

None of the boards criticise DeklarantUZ, InCustoms, or LexPort (they are not named in the UI). No payment-guarantee slogan appears; the old idea is explicitly refused (p.4, p.10). Preference copy does not advise shipping via a third country. Those are clean.

The risks that *are* on the boards:

| Where | What it says now | Why it is risky | Safer wording |
| --- | --- | --- | --- |
| Landing “Nima qilmaydi” (p.4) | “Davlat xizmati emas. **Bojxona bilan rasmiy ulanish yo‘q** — ochiq rasmiy topshirish API topmadik.” | Spec v2’s required wording is “We found no public filing API.” Absence is not proved at 100%. “Rasmiy ulanish yo‘q” sounds like a settled fact, and can be heard as either an over-claim or as “this product is unofficial, so I should not use it.” | “Davlat xizmati emas, bojxona bilan rasmiy hamkor emasmiz. Ochiq rasmiy topshirish API sini topmadik — shu bois kabinetni sizning kompyuteringizda, ko‘z oldingizda to‘ldirish yo‘lini quryapmiz.” The footer on p.5 (“rasmiy hamkorlik yo‘q”) is already closer to this. |
| Hero (p.4) and path card (p.6) | “Deklaratsiyani o‘zingiz topshiring”; “tayyorlash va o‘z kabinetingizda topshirish.” | Sounds like the official filing path is live. P.17 says real-cabinet automation is not enabled. | “Deklaratsiya qoralamasini tayyorlaymiz va kabinetni to‘ldirishda yonida turamiz. Imzo — faqat sizda. Haqiqiy kabinetni avtomatik to‘ldirish hozircha mashq rejimida; huquqiy savol hali ochiq.” |
| Landing (p.4) | “2018-yil 1-iyuldan… Broker majburiy emas.” | Legally grounded (PF-5414) and the sentence does add “murakkab holatda unga o‘tish imkoni doim bor.” Still easy to hear as “you will not need a broker.” | Keep the legal fact, soften the pitch: “Qonunan broker majburiy emas. Oddiy yo‘lda o‘z nomingizdan topshirishingizga yordam beramiz; murakkab yoki noaniq bo‘lsa, tekshirilgan to‘plamni brokerga berasiz.” |
| Landing “Nima qiladi” (p.4) | “Qaysi sertifikat, ruxsatnoma yoki markirovka kerakligini pul to‘lashdan oldin aytadi.” | A complete, always-right permit list is not evidenced in this review. A miss after the user has shipped is worse than silence. | “Shu kod uchun hozirgi ro‘yxatdagi sertifikat va ruxsatnomalarni ko‘rsatamiz. Ro‘yxat to‘liq bo‘lmasligi mumkin — jo‘natishdan oldin tekshiring.” |
| Any demo of p.10–11, p.7 | Sample totals such as ≈ 67 823 600 so‘m, kargo side 72 053 100, course 12 650 so‘m/$, duty 10%. | Design rationale states all figures are layout sample data. Fine if the card stays labelled “namuna.” Dangerous if spoken as market or official averages. | Always say “namuna hisob, hozircha misol.” Never quote these as research. Kargo totals only from a number the user typed. |
| Pitch vs competitors | (Not on the boards, but a likely spoken risk.) | Spec v2 §1 / competitors paragraph: do not criticise InCustoms, LexPort, or DeklarantUZ. | Position by **when** and **who**, not by attacking names. Example: “Deklaratsiya qoralamasi bo‘yicha bozorda allaqachon vositalar bor. Bizning urg‘u — to‘lashdan oldin jami narx, jo‘natishdan oldin yetishmayotgan hujjat, keyin kabinetni ko‘z oldida to‘ldirish. Imzo egada.” |

Do not add, anywhere: a payment guarantee, ST-1 / “Qozog‘iston orqali” routing advice, “API yo‘q” as a proof, government affiliation, or a slight on named tools.

---

## 5. Focused interview questions

Trimmed from `/workspace/yuklago/intervyu-skriptlari.md`. Mom Test: last real shipment, numbers only if they state them, no “YuklaGo-ni olarmidingiz?”, no legal or routing advice. 15–20 minutes, Telegram or phone, record only with permission. If they do not remember a figure, leave the field blank.

Target: 2–3 kichik importchi, 2–3 broker/deklarant. The one research question: will they file their own BYD, what stops them, do they trust a suggested code if liability stays with them, and what kargo-per-kg vs BYD actually cost last time.

### 5.1 Kirish (ikkala segment)

> Assalomu alaykum, [ism]. Men [ismingiz], YuklaGo jamoasidan. Biz kichik tadbirkorlar deklaratsiyani o‘zlari topshiradimi, yoki kargo va broker orqali ketadimi — shuni tushunmoqchimiz. Hozir hech narsa sotmaymiz, maslahat ham bermaymiz. 15–20 daqiqa, oxirgi yukingiz haqida gaplashsak bo‘ladimi? Yozib olsam maylimi? Ismingizni ruxsatsiz chiqarmaymiz.

### 5.2 Kichik importchilar (2–3 kishi)

Qizdirish: nima sotasiz, qancha vaqtdan beri, asosan Xitoymi yoki Turkiyami?

**1. Oxirgi yuk.** Qachon, nima, qayerdan, taxminan necha kg? Tovarga o‘zi qancha to‘ladingiz?  
Qayd: sana ______ ; tur va og‘irlik ______ ; tovar narxi ______

**2. Qaysi yo‘l.** Shu yuk kargo (kg bo‘yicha, eshikdan-eshikkacha) bilan keldimi, o‘zingiz BYD (deklaratsiya, ba’zan GTD) topshirdingizmi, broker orqalimi, yoki aralash? Nega aynan shu yo‘l?  
*Probe:* Bu yo‘lni kim aytdi? Boshqa yo‘lni o‘sha paytda ko‘rib chiqdingizmi?

**3. Pul va vaqt.** Kargo bo‘lsa — kilogramiga qancha, bu narxga nima kirdi? Boj, QQS, yig‘im alohida ketdimi, qancha, qachon bildingiz? Brokerga murojaat qilgan bo‘lsangiz — nima qilib berdi, qancha oldi? Buyurtmadan qo‘lingizga yetguncha necha kun?  
Qayd: kargo ______ $/kg ; bojxona to‘lovlari ______ ; broker haqi ______ ; vaqt ______ kun

**4. O‘zi topshirish — o‘tmish.** Biror marta bojxona deklaratsiyasini o‘zingiz topshirib ko‘rganmisiz, yoki kabinetni ochib ko‘rganmisiz? Nima bo‘ldi?  
*Probe:* ERI (USB kalit), tashqi savdo kabineti, yoki “o‘zim qilaman” deb o‘ylab, keyin brokerga yoki kargoga qaytgan paytingiz bormi? Nima to‘sqinlik qildi — vaqt, tushunmovchilik, qo‘rquv, hujjat, pulmi? (Yo‘l ko‘rsatmang.)

**5. Kod va ishonch.** Oxirgi yukda tovar kodini (TIF TN / HS) kim tanladi — kargo, broker, o‘zingiz, yoki hech kim aytmadimi? Sizga kodni “tekshirib tasdiqlang, imzolaganingizdan keyin javobgarlik sizda” desalar, oxirgi yukingizda shuni qilgan bo‘larmidingiz — yo qilmasdingiz? Nega?  
Bu savol ehtiyot: avval nima *qilganini* eshiting, keyin tasdiq haqida so‘rang. “AI aniq topadi” demang.

**6. Javobgarlik.** Oxirgi yukda xato, kechikish, ushlanib qolish yoki olib qo‘yish bo‘lganmi? Kim javob berdi, qancha zarar tegdi? Sizningcha, deklaratsiyada xato bo‘lsa, tuzatish yoki jarima kimning zimmasida bo‘ladi?  
Qayd: holat ______ ; zarar ______ ; ular aytgan javobgar ______

**7. Kargo yoki o‘z BYD — solishtirish.** Shu oxirgi yukni o‘zingiz rasmiylashtirganingizda (yoki aksincha, kargo bilan) arzonroq yoki qimmatroq bo‘lardi deb hisoblaganmisiz? Qanday raqamlarga qarab shunday dedingiz? Hujjatlar kimning nomiga chiqqani, nusxasi sizda qolgan-qolmagani esingizdami?

**8. Oxirida, yumshoq.** Sotib olishdan oldin “jami qancha bo‘ladi” yoki kabinetni ko‘z oldingizda to‘ldirish uchun avval kimgadir pul to‘laganmisiz? To‘lagan bo‘lsangiz — kimga, qancha, nima uchun?  
“Bizning vositani sotib olarmidingiz?” demang.

Yakun: rahmat, yana bir do‘konchi yoki brokerni tanishtira olasizmi, keyinroq yozishga ruxsat.

### 5.3 Brokerlar va deklarantlar (2–3 kishi)

Qizdirish: qancha vaqtdan beri, asosan qanday mijoz (kichik do‘kon, kargo, yirikroq firma)?

**1. Oxirgi hafta.** Taxminan nechta deklaratsiya? Nechtasi kichik tadbirkor yoki Instagram/Telegram sotuvchisi?  
Qayd: jami ______ ; kichik ______

**2. Mijoz qaysi yo‘ldan keladi.** Kichik mijozlar odatda o‘z kontrakti bilan keladimi, yoki kargo orqalimi? Kargo yo‘lini tanlaganlar sizga qachon keladi?  
*Probe:* Oxirgi kargo orqali kelgan yukda qanday qiyinchilik bo‘ldi — hujjat, egasi, qiymat, kod, vazn?

**3. “O‘zim topshiraman.”** Mijoz o‘zi topshiraman deb urinib, keyin sizga qaytgan holat oxirgi marta qachon bo‘ldi? Nima to‘sqinlik qilganini aytishdi — ERI, kabinet, kod, qo‘rquv, vaqt, hujjatmi? O‘zi muvaffaqiyatli topshirgan kichik mijozingiz bormi, nima yordam bergan?

**4. Kod va ishonch.** Oxirgi kichik yukda kodni kim tanladi? Mijoz sizga “dastur yoki sayt shu kodni aytdi” deb kelganmi? Kelgan bo‘lsa, to‘g‘ri chiqdimi, yo qayta tuzatdingizmi? Mijoz kodni o‘zi tasdiqlashni xohlaydimi, yoki “siz biling, men javob bermayman” deydimi?

**5. Javobgarlik.** Sizning shartnomangizda xato bo‘lsa kim javob beradi, deb mijozga nima deysiz? Oxirgi yilda yo‘qotish, olib qo‘yish yoki uzoq ombor bo‘ldimi, zarar taxminan qancha, kim ko‘tardi?  
O‘zingiz qonun tushuntirmang — ularning amaliyotini yozing.

**6. Haq va vaqt.** Oxirgi uchta kichik ishda xizmat haqingiz aniq qancha bo‘ldi, ish qancha vaqt oldi?  
Qayd: haq ______ / ______ / ______ ; vaqt ______

**7. Vositalar (neytral).** Hozir nima ishlatasiz — AIS Deklarant, Deklarant Plyus, VED-Deklarant, InCustoms, DeklarantUZ, faqat ed2.customs.uz? Nima uchun shu? Nimasida qiynalasiz? Tanqid qilmang, nomini yomonlamang.

**8. Oxirida.** Mijoz sizga kelishidan oldin hisob-kitob yoki qoralama olib kelganmi? Tekshirilgan to‘plam (hujjat, kod taklifi, to‘lovlar, ochiq savollar) kelsa, oxirgi ishingizda bundan foydalaningizmi? Bunday oldindan ish uchun alohida haq olganmisiz, qancha?  
Mahsulotni sotmang.

Yakun: rahmat, yana bir deklarant yoki kichik importchini tanishtirish, keyin yozishga ruxsat.

### 5.4 Qayd (har suhbatdan keyin bitta qator)

| Segment | Sana | Shahar | Yo‘l (kargo/BYD/aralash) | Oxirgi yuk turi va og‘irligi | Kargo narxi $/kg | Bojxona to‘lovlari | Broker haqi | Vaqt | O‘zi BYD topshirganmi / nima to‘sqinlik qildi | Kodga ishonch / javobgarlikni kimda deb biladi | Eng katta og‘riq | Vositalar | To‘lashga tayyorlik | Iqtibos |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## 6. Pitch storyline

Spine: **problem → product → honest limitation → proof → 3-minute demo.**  
All proof lines marked `[INTERVIEW — not yet collected]` or `[PROOF — not yet in hand]` must stay visibly empty until real evidence exists. Do not fill them with sample UI numbers.

### 6.1 Problem (say this)

Kichik o‘zbek importchi Xitoy yoki Turkiyadan tovar oladi va jami xarajatni — boj, QQS, yig‘im, yo‘l, yetishmayotgan sertifikat — ko‘pincha yuk chegaraga yetganda biladi. Qonunan 2018-yil 1-iyuldan broker majburiy emas: tadbirkor o‘z nomidan, internet orqali, o‘z ERI kaliti bilan topshirishi mumkin. Amalda yo‘l og‘ir: kod, hujjat, `ed2.customs.uz`, USB-token. Shuning uchun ko‘p odam kg bo‘yicha kargoga yoki brokerga o‘tadi.

`[INTERVIEW — not yet collected: oxirgi yukda yo‘l (kargo / BYD / broker); qachon jami narxni bilishgan; nima to‘sqinlik qilgan.]`

### 6.2 Product (say this)

YuklaGo — kichik importchi va eksportchi o‘zi topshirishi uchun platforma. To‘lashdan oldin, oddiy o‘zbekchada, jami taxminiy narxni manbasi bilan ko‘rsatadi. Jo‘natishdan oldin qaysi hujjat yetishmasligini aytadi. Keyin tekshirilgan qoralama tuzadi va **foydalanuvchining o‘z kompyuterida** kabinet maydonlarini ko‘z oldida to‘ldiradi. **Kirish va imzoda to‘xtaydi.** Kalit va parol qurilmadan chiqmaydi. Murakkab bo‘lsa, ishni tekshirilgan to‘plam bilan brokerga berish oddiy yo‘l — muvaffaqiyatsizlik emas.

Bozorda deklaratsiya qoralamasini va’da qiladigan vositalar allaqachon bor. Biz ularni tanqid qilmaymiz. Farqimiz — **qachon** yordam berishimiz: sotib olishdan oldin, jo‘natishdan oldin, keyin kabinetda.

### 6.3 Honest limitation (say this, do not skip)

Imzo va javobgarlik egada qoladi. Taklif qilingan kod — majburiy tasnif emas. Hisob — sanasi ko‘rsatilgan rasmiy jadvallardan, lekin bojxona undiradigan summa farq qilishi mumkin; YuklaGo farqni qoplamaydi. Davlat xizmati emasmiz, rasmiy hamkor emasmiz. Ochiq rasmiy topshirish API sini topmadik. **Haqiqiy `ed2.customs.uz` ni avtomatik to‘ldirishning huquqiy savoli ochiq; bugungi namoyish — aniq belgilangan mashq kabineti, yoki qo‘lda nusxalash.** Yuk yo‘nalishini o‘zgartirib imtiyoz olish haqida maslahat bermaymiz.

### 6.4 Proof point (only what you actually have)

1. **Calculation proof (preferred).** `[PROOF — not yet in hand: bitta qabul qilingan, maxfiylashtirilgan deklaratsiyaning to‘lovlarini so‘miga qadar qayta hisoblash; har bir qatorda manba va sana. Ikkinchi variant: NOTARIF / rasmiy jadval skrinshoti yonma-yon.]`
2. **Interview proof.** `[INTERVIEW — not yet collected: 2–3 importchi + 2–3 broker; kargo vs BYD raqamlari; o‘zi topshirishga nima to‘sqinlik qilgani; javobgarlik haqida iqtibos.]`
3. **Do not use as proof:** the prototype totals (≈ 67 823 600 so‘m and the rest). They are layout samples.

Until 1 or 2 is real, say: “Hozircha bu gipoteza. Shu hafta importchi va brokerlar bilan oxirgi yuk raqamlarini yig‘yapmiz; hisobni rasmiy jadval bilan tekshiramiz.”

### 6.5 Three-minute demo outline

Announce at the start: all shipments and amounts on screen are **namuna**; typography should already be fixed; skip any board with `[v2 spec]` or a cut-off page (p.16, p.18). Do not open real `ed2.customs.uz` automation. Do not compare named competitors.

| Time | What you show | What you say |
| --- | --- | --- |
| **0:00–0:25** | Landing (p.4), but *after* typography is fixed. Point to “Nima qiladi / Nima qilmaydi,” not only the hero. | One-sentence problem. Then: we help you file in your own name, step by step. We do not sign, we do not keep the key, we do not guarantee the customs total. |
| **0:25–0:55** | Landed-cost screen (p.10). Tap a *Rasmiy* chip and an *≈ taxmin* chip. If you show cargo compare (p.11), type a fictional quote only as “foydalanuvchi kiritgan narx,” or skip the totals. | Before you pay the supplier, here is a dated official-table estimate plus freight marked as an estimate. We never invent a typical kargo rate. |
| **0:55–1:20** | TIF TN screen (p.14): suggestion, “majburiy tasnif emas” tick, confirm, broker link still visible. Optional: one missing-permit card from home (p.7) *if* placeholders are removed. | The code is a suggestion you confirm. If you sign, you are responsible. If you are not sure, you can hand the pack to a broker — that is a normal path. |
| **1:20–1:40** | Cabinet start (p.17): three options. Linger on “Haqiqiy kabinet — hozircha yoqilmagan” and “Mashq portali.” | Honest limitation, out loud: real-cabinet automation is a legal question still open. What we can show now is the practice cabinet, clearly marked, or copy-assist. |
| **1:40–2:35** | Practice fill (p.19–21): “YuklaGo yozmoqda,” read-back, pause when the user clicks (p.20), then the ink/yellow rail “Endi sizning navbatingiz” and the cabinet’s own sign dialog labelled “Bu oyna kabinetniki. YuklaGo bu yerga yozmaydi” (p.21). Optional 10 seconds on the stop/error state (p.22): nothing sent, draft unsigned. | This is how filling works: in front of you, every value already confirmed, stop at login and sign. We do not type in the sign window. |
| **2:35–3:00** | Session log (p.23) or broker pack (p.26), then black screen / logo. | Log: who did what; passwords and keys are never recorded. If the case is complex, the checked pack goes to your broker. Close with the proof you actually have, or with the open interview/calculation promise — not with a slogan. |

If time is cut to two minutes: keep 0:00–0:25, 0:25–0:55, 1:20–1:40, and 1:40–2:35. The limitation and the ERI hand-off are not optional.

---

## 7. What to fix before a judged demo

1. Repair `oʻ` / `gʻ` (U+02BB) spacing in the embedded font so Uzbek words are readable. This is the first trust problem.
2. Replace every `[v2 spec]`, `[N] kun`, `[qonun moddasi]`, `[kelishuv nomi]`, and official HS text placeholder — or drop that board from the demo.
3. Do not export cut-off pages (p.16, p.18) into the leave-behind PDF.
4. Align landing present-tense “kabinetni to‘ldiradi” with p.17’s “hozircha yoqilmagan,” using the safer wording in §4.
5. Soften “rasmiy ulanish yo‘q” to the spec’s API sentence plus “mustaqil xizmat / rasmiy hamkor emasmiz.”
6. Run the interviews in §5 and the calculation proof in §6.4 *before* treating self-filing as a validated story.

# YuklaGo: declarant review of spec v2 and web design v0.1

**Reviewer role:** practising Uzbekistan declarant (bojxona rasmiylashtiruvi bo'yicha mutaxassis).
**Reviewed:**
- `/workspace/hackathon/yuklago-spec-v2.md` (all sections);
- `/workspace/hackathon/design-v0.1/design-rationale.md`;
- `/workspace/hackathon/design-v0.1/yuklago-web-ui-v0.1.pdf` (all 28 boards; text extracted and read board by board).

**Date:** 18.11.2026. Live checks were done at about 03:30 Tashkent time (UTC+5).

**Rules I followed:**
- Every legal claim links to lex.uz or a customs.uz service.
- Anything I could not confirm is marked **[UNVERIFIED]**.
- Anything that is my own reading of a rule, not the text itself, is marked **[INFERENCE]**.
- All money figures are either quoted from the design's own sample data or labelled **misol uchun** (example only).
- Practice knowledge that has no written source is marked **[PRACTICE]**.

**Board numbers** refer to PDF pages:

| Board | Screen |
|---|---|
| p1 | Design system |
| p2–3 | Shipment header and stage rail |
| p4 | Landing page |
| p5 | Login |
| p6 | Path choice and readiness check |
| p7 | Home |
| p8 | New shipment |
| p9 | Shipment overview / deadlines |
| p10–11 | Landed cost, preference, contract and bank |
| p12 | Permits ("Joʻnatishdan oldin") |
| p13 | Documents |
| p14 | TIF TN code |
| p15–16 | Payments and draft review |
| p17–18 | Cabinet-fill setup |
| p19–22 | Mock fill session (filling, paused, hand-off to sign, error) |
| p23 | Session log |
| p24 | After filing / message explainer |
| p25 | Product library |
| p26 | Broker hand-off |
| p27 | Settings |
| p28 | Mobile |

---

## 0. Verdict in five lines

1. The trust model is right and should be kept. That means provenance chips, "only *Siz tasdiqladingiz* values go into the cabinet", stopping before login and signing, and never touching the key or password.
2. The payment engine would produce wrong money today. It ignores the **extra duty when there is no certificate of origin** (in force from 28.02.2026). It builds the customs value from the wrong freight leg and the wrong exchange-rate date. It has no model for combined "X %, but not less than Y USD/kg" rates. Several sample figures that wear the **Rasmiy** (official) chip do not match the official tables.
3. The flow is missing three steps a real filing cannot skip:
   - **pre-funding customs payments** before or at acceptance;
   - the **declaring-persons list and E-arxiv** set-up in the participant cabinet (TIF ishtirokchisi kabineti);
   - the **Yagona darcha** permit gate.
4. The BYUD (GTD) draft and the mock cabinet have wrong grafa meanings: **43, 45, 46, 36 and "B" vs "C"**. They also leave out grafas the instruction makes compulsory for IM40.
5. "ed2" is real. ed2.customs.uz is the live e-declaration system with ERI login. But part of the set-up the flow needs (the declaring-persons list, payment reconciliation) lives on **ed1.customs.uz/PersonCabinet**. Export goes through **cargo.customs.uz**.

---

## 1. "ed2" vs ed1 vs ed.customs.uz: what I found (checked live 18.11.2026, about 03:36 Tashkent)

| Host | Result | What it is |
|---|---|---|
| `https://ed2.customs.uz/` | HTTP 200. The page is titled "ed2.customs.uz" and reads "Avtomatlashtirilgan axborot tizimi · Tovarlarni elektron deklaratsiyalash · Davom etish uchun ERI kalitingizni kompyuterga ulang". You choose a key type: **PFX (sertifikat fayli)**, **USB-TOKEN** or **BAIK-TOKEN**. The page loads `/eri_new/e-imzo-client.js` and `e-imzo.js`. The phone shown is (99 855) 502-76-00 (1108). | The **e-declaration system** (BYUD filing). Login needs the E-IMZO client on the user's computer. This is the right target for "Kabinetni to'ldirish". |
| `https://ed1.customs.uz/PersonCabinet/` | HTTP 200. Titled "Шахсий кабинет – ТИФ қатнашчисининг шахсий кабинети". It lists these services: Товарларни электрон декларациялаш; **"Экспорт уч қадам" (cargo.customs.uz)**; **Декларацияловчи шахслар рўйхати**; БЮД status online; **Божхона тўловлари бўйича солиштирув далолатномалари**; payment-guarantee applications; marking check; Е-ОМБОР; and others. It links to my.gov.uz services 127 and 207. | The **foreign-trade participant cabinet** (TIF ishtirokchisining shaxsiy kabineti). This is where the set-up from VMQ 605 cl. 15, stage 2 happens. |
| `https://ed.customs.uz` | The TLS handshake failed (unexpected EOF). Plain HTTP returned 500. | Not a usable site. Do not reference it. |
| `https://cargo.customs.uz` | HTTP 401 (needs login). | The export "3 steps" filing service, linked from ed1. |
| `https://contract.customs.uz` | HTTP 200, titled "E-CONTRACT". | Contract registration. |

**Live counter on ed1, today 00:00–03:36 (a tiny sample, not an average):**
- 84 BYUD sent;
- 22 (26.19 %) returned for errors;
- 16 (19.05 %) uploaded but not sent or registered;
- 40 registered but not yet cleared;
- 5 cleared;
- 6 correction forms (BDT) sent.

The page also states that **about 21,205 errors are found in BYUDs per day on average**. Yesterday's snapshot (17.11, about 02:15) showed 36 of 76 (47 %) returned. Source: https://ed1.customs.uz/PersonCabinet/

**Fix:**
- Keep "ed2.customs.uz" as the filing target.
- Add ed1.customs.uz/PersonCabinet as a separate, named destination for the one-time set-up and for payment reconciliation.
- Add cargo.customs.uz for export.
- Write in the spec that the legal names are "BQ YAAAT" / "us-uz.gov.uz" (VMQ 605 cl. 14, as amended by VMQ 393 of 20.07.2026, https://lex.uz/uz/docs/-3844549). Write that the domain names are what we observed live. The domain can change, and the planned single platform is due 01.09.2027 (PQ-122 cl. 16a, https://lex.uz/docs/-7452043). So the desktop app needs a remote-config URL list, not a hard-coded host.

---

## 2. The real IM40 path, and where YuklaGo stands

Legal basis for each step:
- Customs Code (BK), https://lex.uz/docs/2876354
- VMQ 605 (Nizom), https://lex.uz/uz/docs/-3844549

| # | Real step | Basis | In YuklaGo? |
|---|---|---|---|
| 0 | Contract signed. For a contract with payments, it is registered in the Unified electronic information system of foreign trade operations (E-kontrakt). Its ID goes into **grafa C, item 1**. | BK art. 243; Yo'riqnoma 2773, grafa C (https://lex.uz/uz/docs/-2924955) | p11 "E-kontrakt" exists, but the spec still says "[UNVERIFIED] whether mandatory". See I7. |
| 1 | Before paying: HS code, rates, permits, **origin certificate**. | BK 363–366, 300¹ | Partly. Origin is shown only as a "preference" topic. See **C1**. |
| 2 | Permit bodies enter permits and certificates into **Yagona darcha**. Without them the TED is **not accepted**. All permits go through Yagona darcha only, from 01.10.2025. | VMQ 605 cl. 15, stage 1; PQ-122 cl. 17 | p12 checks "lists", not Yagona darcha records. See **C8**. |
| 3 | The carrier submits **advance information** before arrival. This is **mandatory** for road, rail and air. | BK 206 part 3 | Missing. See I4. |
| 4 | Arrival is confirmed. The carrier gives a **short BYUD** (qisqa BYUD) by the next working day. The goods go to temporary storage (max 60 days; 10 for perishables). | BK 85, 226; VMQ 605 cl. 6–8 | p9 has a "[N] kun" placeholder. See **C7**. |
| 5 | **One-time cabinet set-up:** the declarant puts its broker, in-house specialist or trusted person into the **declaring-persons list** with an authority period. It uploads documents to **E-arxiv**, signed with ERI, and gets special numbers. | VMQ 605 cl. 15, stage 2 | Missing. See **C4**. |
| 6 | **Pre-fund customs payments** to the customs personal treasury account. Payment is due before or at acceptance. | BK 327, 334 | Missing. See **C5**. |
| 7 | The declaring person builds the TED in ed2, signs with **their own ERI**, and sends. Format-logic control (format-mantiqiy nazorat) runs: on error the TED is auto-returned; otherwise it is registered. | VMQ 605 cl. 15, stage 3 | Core of p17–23. |
| 8 | Acceptance within 3 h, otherwise automatic. Risk corridor (green / yellow / red / blue). Processing: low risk 3 h, medium 8 h, otherwise 1 working day, not counting risk-management measures and other state controls. | VMQ 605 annex (VMQ 700 ed.); PQ-122 cl. 15; BK 248 | p24 has no corridor or inspection states. See I9. |
| 9 | Release (can be automatic). Correction form (BDT) if needed; amendments allowed within 3 years. | BK 266, 271 | Partly. p24 handles "Qaytarildi" only. |
| 10 | After release: archive, marking, post-clearance audit, origin certificate supplied within 1 year → recalculation. | BK 366 | Missing. See C1. |

---

## 3. Findings

### CRITICAL (blocks a correct or legal filing, or produces wrong money)

**C1. The extra duty for a missing or doubtful certificate of origin is absent everywhere.**
- **Screens:** p10–11 landed cost and "Imtiyozli stavka"; p12 permits; p15 payments (grafa 47); p25 product library.
- **What is wrong:** From **28.02.2026**, BK art. 300¹ adds an extra customs duty on goods from countries without most-favoured-nation (MFN) treatment, or **whose origin is not established**:
  - +5 % if the base ad valorem rate is up to 10 %;
  - +10 % if it is 10–20 %;
  - +15 % if it is 20–30 %;
  - +20 % if it is 30 % or more.

  Art. 366 (new edition) says that when the certificate of origin is **missing or doubtful**, this extra duty applies. If a proper certificate is supplied **within 1 year** of placement under the regime, MFN or free-trade treatment can be restored and the overpaid amount refunded (https://lex.uz/docs/2876354, arts. 300¹, 366).

  The design treats the origin certificate only as a way to get a *lower* rate ("Imtiyoz topilmadi" for China). In practice, for a Chinese LED lamp without a certificate, the bill goes **up**.
- **Size of the error (misol uchun, using the design's own inputs):** customs value (CV) 54,800,000 so'm at a 15 % base rate (see C2) → extra duty +10 % = **5,480,000** so'm, plus the VAT on it. **[INFERENCE]** The extra duty is a customs duty, so I treat it as part of the import VAT base (Tax Code art. 254, https://lex.uz/docs/4674902).
- **Unclear wording:** the band boundaries say "up to 10 %" and "from 10 to 20 %". It is unclear which band a rate of exactly 10 %, 20 % or 30 % falls in. **[UNVERIFIED]** Ask customs or a lawyer, and show both values until this is resolved.
- **Fix:**
  1. Add a required "Kelib chiqish sertifikati" row to p12 and p13, with three outcomes: *bor (form, number, date)* / *yetkazib beruvchi beradi* / *yo'q*.
  2. In the payments engine, add an `origin_status` input. It drives a new 47 line, "Qo'shimcha bojxona boji (BK 300¹)", with its own Rasmiy chip pointing to art. 300¹.
  3. On p10, put a side-by-side "sertifikat bilan / sertifikatsiz" total *before the user pays the supplier*. This is the single most valuable "before paying" insight.
  4. Generate the supplier request text in EN/ZH/TR (p11 already has the pattern).
  5. Fill grafa 44 with code **701** plus the certificate number and date (Yo'riqnoma 2773, grafa 44 "ж").
  6. Add a post-release reminder: "sertifikatni 1 yil ichida taqdim etsangiz — qayta hisob va qaytarish (BK 366)".
  7. Spec §8.3 and §11: add 300¹/366 to the rules engine and to the legal references.

**C2. The payment engine lacks combined and specific rates, and the sample figures wear the "Rasmiy" chip but are wrong.**
- **Screens:** p4 landing calculator; p10; p14 alternative codes; p15; p28 mobile.
- **What is wrong:**
  - **Duty rate.** In PQ-3818 Annex 1 (https://lex.uz/docs/3802363, edition I hold as of 16.02.2026, PQ-58), heading **853952 "Светодиодли (LED) лампалар" is 15 %**, not 10 %. The alternative on p14, *9405 42 …*, is shown at 15 %. But the 9405 42 rows I read (…420012/19/32/33/39) carry "10 %, but not less than 0.5 USD/kg". **[UNVERIFIED]** I may be mapping the rows wrongly, so recheck that mapping.
  - **Combined rates.** Many lines are combined ("X %, лекин ҳар бир кг/дона учун Y АҚШ долларидан кам бўлмаган миқдорда"). Examples: lamps 8539 21 92 "30 %, but not less than 0.12 USD per piece"; furniture 9403 "15 %, but not less than 0.4 USD/kg". The engine and the formula on p10 show only "× %". BK art. 293 allows ad valorem, specific and mixed rates.
  - **Customs fee.** The fee is shown as **310,000** "Rasmiy". Under VMQ 55 (https://lex.uz/docs/7357270) a CV under 10,000 USD pays **1 BHM**. The design's sample CV is 54,800,000 / 12,650 ≈ 4,332 USD, so the fee is 1 BHM. From 01.09.2026 the BHM is **440,000 so'm** (PF-115, https://www.lex.uz/uz/docs/-8283656). 310,000 matches no BHM value.
  - **Why it matters:** if these placeholders reach a demo, the "Rasmiy" chip makes a wrong number look official. That is the exact failure the design system was built to prevent.
- **Fix:**
  1. Build the rate table straight from the PQ-3818 annex text, keeping the edition date and the row text.
  2. Model `rate = max(ad_valorem × CV, specific × quantity × CB rate)` wherever "кам бўлмаган" appears. Show both legs and say which one won.
  3. Compute the fee from the VMQ 55 bands × the BHM in force on the acceptance date. Convert CV to USD at the CB rate on that date to pick the band.
  4. Design rule: a **placeholder must never carry the Rasmiy chip**. Use a "Namuna" (sample) chip in boards.
  5. Rebuild the p10 and p15 sample with real figures before any demo.

**C3. The customs value is built wrong: wrong freight leg, no insurance, wrong exchange-rate date.**
- **Screens:** p10 ("Transport Shenzhen → Toshkent ≈ 6,200,000" added in full); p15 ("Bojxona qiymatiga transport kiradi: 6,200,000"); p19–21 grafa 45/46 in the mock.
- **What is wrong:**
  - Under the transaction-value method, the price is increased by costs **up to the place where goods enter the customs territory** (BK 304 "а"). Art. 304 also says "Ушбу моддада кўрсатилмаган харажатларни битим нархига қўшишга йўл қўйилмайди" (costs not listed may not be added). Costs inside Uzbekistan are excluded when they are shown separately (BK 305). Additions are proved by invoices and payment orders (BK 304). With FOB Shenzhen, you add freight, insurance and loading **to the Uzbek border**, not to Tashkent.
  - The board uses the "MB kursi · 01.10.2026". The rate that counts is the CB rate **on the day the declaration is accepted** (BK 326; the grafa 46 instruction says the same).
- **Fix:**
  1. Split the freight input into "chegaragacha" and "chegaradan keyin", with an evidence upload. The forwarder's invoice must show the split, or the whole amount goes in (warn about this).
  2. Add an insurance line ("≈ Taxmin" until a policy is uploaded).
  3. Keep the 01.10 rate only on the *before-paying estimate* screen, labelled. On p15 and in the cabinet fill, use a "kurs: qabul qilingan kundagi MB kursi — imzolash kuni tekshiring" (check on signing day) warning, and re-quote on the filing day.
  4. Show the valuation method explicitly in the draft (method 1 = transaction value, BK 301–305). Do not put it in grafa 43 (see C6).

**C4. The cabinet set-up is under-modelled: the declaring-persons list, E-arxiv, the ed1/ed2 split, the E-IMZO client.**
- **Screens:** p6 readiness ("3 · Tashqi savdo ishtirokchisi kabineti — ed2.customs.uz", "4 · Kim imzolaydi?"); p17–18 fill set-up; p26 broker hand-off; p27 settings "ERI va kabinet".
- **What is wrong:** VMQ 605 cl. 15, stage 2 requires the **declarant** to do three things through the participant cabinet:
  1. Enter into the participant list who may submit the TED: a **trusted person** (ishonch bildirgan shaxs), a **customs broker**, or the declarant's **own staff specialist** (o'z shtat birligidagi mutaxassis). Each comes with an **authority period**.
  2. Upload the supporting documents to **E-arxiv**, signed with ERI. Each gets an automatic **special number**, which is then referenced in the TED. Documents that are not in E-arxiv must be attached and ERI-signed with the TED.
  3. Give that special number to the broker or specialist, who can then see only those documents.

  On ed1 this is the service "Декларацияловчи шахслар рўйхати" (https://ed1.customs.uz/PersonCabinet/), which links to my.gov.uz service 207. **[UNVERIFIED]** that service 207 is exactly this registration. p6 says only "Boshqa shaxs imzolasa… vakolatli mutaxassis sifatida ro'yxatdan o'tgan bo'lishi kerak: [shartlar — v2 spec]".
- **Fix:**
  1. p6: split the step into three checks, each with "Bor / Yo'q / Bilmayman":
     - (a) "ed2.customs.uz ga ERI bilan kira olaman (E-IMZO dasturi o'rnatilgan, kalit turi: PFX / USB-token / BAIK-token)";
     - (b) "ed1 kabinetida deklaratsiyalovchi shaxslar ro'yxatida imzolovchi bor, vakolat muddati: [sana]";
     - (c) "E-arxivdan foydalana olaman".
  2. Add an **"E-arxiv" step** between Documents (p13) and Cabinet fill (p17). It is user-driven, like the cabinet fill: the user uploads and signs. YuklaGo records the special numbers and writes them into grafa 44.
  3. p26 broker hand-off: add "Brokerni ed1 ro'yxatiga kiriting (vakolat muddati bilan) va E-arxiv maxsus raqamlarini bering". Without this the broker cannot file under your name.
  4. Fill the placeholder "[shartlar — v2 spec]" with the three allowed categories from VMQ 605 cl. 15.
  5. p27: add "vakolat muddati tugaydi: [sana]" and an ERI certificate-expiry reminder.

**C5. There is no payment step, and the status flow has the wrong order.**
- **Screens:** p3 and p9 stage rail; p15–16; p24 status bar ("Yuborildi → Qaytarildi → To'lovlar → Chiqarildi"); p7 home.
- **What is wrong:**
  - Customs payments are paid **before or at acceptance** of the declaration (BK 327).
  - The payer may transfer **advance funds** to the customs body's **personal treasury account** (shaxsiy g'azna hisobvarag'i). These count as customs payments only once the payer instructs it; filing the declaration is such an instruction (BK 334).
  - If the funds are not there, a green-corridor filing still stalls. **[PRACTICE]**
  - Reconciliation of the balance is an ed1 service, "Божхона тўловлари бўйича солиштирув далолатномалари".
  - Grafa 47 also carries the payment method code "ТУ": **БН** (bank, non-cash) / **КТ** (cash) (Yo'riqnoma 2773, grafa 47).
- **Fix:**
  1. Add a stage "To'lovni tayyorlash" before "Kabinetni to'ldirish". It shows the total from p15, the official treasury details (link to customs.uz, never typed by us), and a check: "avans qoldig'i ≥ jami (ed1 solishtirma dalolatnomasidan)".
  2. Block "Kabinetni to'ldirish" with a **warning** (not a blocker) if the user has not confirmed funding.
  3. Re-order p24 to: Yuklangan → Yuborildi → **Ro'yxatga olindi** / Qaytarildi (format-mantiqiy nazorat) → **Qabul qilindi** → Yo'lak (yashil / sariq / qizil / ko'k) → [Ko'rik] → Chiqarildi. Show payments as a precondition, not a stage after rejection.
  4. Add a "BDT (tuzatish shakli)" branch.

**C6. The grafa meanings in the draft and the mock cabinet are wrong or incomplete.**
- **Screens:** p15 draft table ("48 maydon"); p17 field groups ("grafa 44, 47, **B**"); p19–22 mock (43 "Baholash usuli", 36 "Imtiyoz", 45 in so'm, 46 "4332,02").
- **What is wrong (Yo'riqnoma 2773, https://lex.uz/uz/docs/-2924955):**
  - **Grafa 43 (IM40)** is **not** the valuation method. It is "**0**" if the consignee imports goods *not* for its own needs, and "**1**" if for its own needs. The mock writes "1" under "Baholash usuli". For LED lamps bought for resale, that would be a **wrong declaration**; the correct value is 0.
  - **Grafa 45** holds the customs value **in the contract currency**, in the right-hand box (here CNY), rounded to 2 decimals. The mock writes 54800000,00 (so'm).
  - **Grafa 46** is the statistical value **in thousand USD**, brought to **CIP/CIF Uzbek border** terms, 3 decimals, at the CB rate on the acceptance day. The mock writes "4332,02"; the format should be "4,332" (thousand USD).
  - **Grafa 36** is **not** in the IM40 list of grafas the declarant fills. Preferences and exemptions are declared in **grafa 44 under code 6xx** with the legal basis. **[UNVERIFIED]** whether the current ed2 web form still shows a box 36, so check it on the live form.
  - **"B" vs "C":** the IM40 list ends with **«С»**. Item 1 of С is the **contract ID in the Unified electronic information system of foreign trade operations**. «В» ("Ҳисоб-китоб тафсилотлари") belongs to other parts of the instruction.
  - **Missing compulsory IM40 grafas:** the declarant fills 1, 2, 3, 5, 7 (post code), 8, 9, 11, 12, 13, 14, 15, 15a, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 54, С (Yo'riqnoma 2773, cl. 24). The draft table and the p17 group labels leave out, among others:
    - 9 (person responsible for financial settlement);
    - 11 (trading country);
    - 15/15a (country of dispatch);
    - 18/21/25/26 (transport);
    - 23 (rate);
    - 24 (nature of transaction);
    - 28 (bank data);
    - 29 (border post);
    - 30 (location of goods: warehouse, licence);
    - **37** (7-digit procedure code: current regime, previous regime, movement feature);
    - **40** (previous document: the BYUD/"ГТД" that placed the goods under the previous regime, with item no., gross, net, supplementary quantity);
    - 48 (deferral);
    - 49 (warehouse);
    - 50 (trusted person);
    - 54 (place, date, declaring person).
  - **Grafa 44** is not free text. Each document carries a **classifier code**, for example 220 invoice, 301 contract, 417 conformity certificate, 701 origin certificate, 6xx exemption basis. E-arxiv special numbers belong here too (VMQ 605 cl. 15).
- **Fix:**
  1. Make the grafa map a versioned data file per regime (IM40, EK10), generated from Yo'riqnoma 2773 and checked against the live ed2 form (field IDs plus labels).
  2. The draft review (p15) must show *all* declarant grafas, grouped, with empty compulsory ones as blockers.
  3. The mock cabinet must use the same map; a wrong mock teaches the wrong thing.
  4. Add a *format-logic pre-check* with rules such as: 35 ≥ 38; 12 = Σ45; 22 = Σ42; 46 rounding; 33 is 10 digits and active; 34 is consistent with 44/701.

**C7. Deadline clocks are placeholders, and the consequences are missing.**
- **Screens:** p2 header ("Saqlash: [N] kun"); p7 home ("Manba: [qonun moddasi]"); p9 ("[Muddat uzunligi…]", "[oqibatlar]"); p26.
- **What is wrong:** the facts the design needs are all available:

  | Clock | Length | Basis |
  |---|---|---|
  | Import BYUD filing | **15 calendar days** from the day goods are presented to the destination customs body | BK 261; VMQ 605 cl. 11 |
  | Export BYUD | **before goods actually leave** | VMQ 605 cl. 11 |
  | Short BYUD by carrier | by the next working day after presentation | VMQ 605 cl. 8 |
  | Temporary storage | **≤ 60 calendar days**, **10** for perishables, counted from the day the goods acquire that status | BK 85 |
  | Preliminary declaration | lapses if goods are not presented within **30 days** | BK 262 |
  | Late declaration or documents | **3 BHM** fine, recorded **automatically** via the unified system (YAAAT) | MJtK 227¹⁰ part 2, art. 17² (https://lex.uz/uz/docs/-97664) |
  | Late payment | penalty interest (penya) of **1/300 of the refinancing rate per day** | BK 349 |
  | Origin certificate | may be supplied **within 1 year** → recalculation | BK 366 |
  | Corrections | possible **within 3 years** | BK 266 |

- **Day counting:** p9 shows presentation 13.11.2026 and deadline 27.11.2026, which counts the presentation day as day 1. If counting starts the next day, the 15th day is 28.11 (a Saturday). **[UNVERIFIED]** the counting rule and the weekend roll-over. Keep the **conservative** date (27.11) and label "ehtiyot sanasi".
- **Fix:** fill all placeholders from this table with article links. Add a "Muddat o'tsa" box: 3 BHM automatic fine, and goods stuck in storage with warehouse costs. Add the preliminary-declaration 30-day clock when the user chooses that path (see I1).

**C8. Yagona darcha is a hard gate, but the design checks "lists" instead.**
- **Screens:** p12 ("'Yagona darcha' orqali ruxsatnoma — Bu kod uchun ruxsatnoma topilmadi"); p13; p24 (rejection example "44-grafada muvofiqlik sertifikati yo'q").
- **What is wrong:**
  - Under VMQ 605 cl. 15, stage 1, if the permit bodies have **not entered** the permit or certificate into the Yagona darcha customs information system, **the system does not accept the TED**.
  - From 01.10.2025, import, export and transit permits go through Yagona darcha only (PQ-122 cl. 17).
  - Clearance finishes only after veterinary, phytosanitary, ecological and other controls, and once permit documents are confirmed (BK 248).
  - Having a PDF certificate (p12 "sertifikat_UZ_xxxx.pdf") is therefore not enough. It must exist **in the system** under the right STIR, HS code and validity period.
  - Relief: certain certificates and permits for identical goods under one contract can be issued once for up to 1 calendar year (PQ-122). This is good for repeat imports (p25 library).
- **Fix:**
  1. Change the p12 requirement row to "Sertifikat Yagona darchada ro'yxatdan o'tganmi?", with a user-confirmed check (number, date, validity, HS code match) and a link to customs.uz/singlewindow.
  2. Add an "amal qilish muddati / qaysi shartnoma" field so it can be reused.
  3. Treat "Topilmadi" carefully: our lists are not the legal list. Wording: "biz tekshirgan ro'yxatlarda topilmadi — bu ruxsat kerak emas degani emas".

**C9. The legal footing of the real-cabinet fill and of the "vakolatli mutaxassis" is not settled in the UI.**
- **Screens:** p4 landing; p6 "Kim imzolaydi?"; p17 "Haqiqiy kabinet · hozircha yoqilmagan"; p26.
- **What the law says:**
  - **Self-filing by the owner is legal.** Since 01.07.2018, foreign-trade participants may fill and submit BYUDs over the Internet without a broker (VMQ 605 cl. 1, in force, https://lex.uz/uz/docs/-3844549).
  - When the declarant submits in its own name, it has the specialist's rights and duties.
  - **The person who signs the TED with ERI is the responsible person** (VMQ 605 cl. 28).
  - The declarant's duties are in BK 274 and 276.
  - **The broker** is a legal entity acting on the declarant's instruction under contract; its liability cannot be limited by contract (BK 277). It must provide security of 1000 BHM (BK 282).
  - Broker activity is **notification-based** (O'RQ-956). The VMQ 847 passport (https://lex.uz/docs/-7274716) requires all of:
    - a legal entity;
    - **2 or more staff specialists**;
    - **1000 BHM** security (insurance or bank guarantee);
    - a cabinet in the customs system;
    - qualification certificates, required from 01.10.2025;
    - a notification fee of **50 % of BHM**, sent via the "Litsenziya" system or my.gov.uz;
    - debts repaid within 10 days;
    - customs informed of staff changes within 5 days.
  - MJtK 227²⁷ fines broker officials 5–10 BHM (10–20 BHM if repeated).
- **Risk:** **[INFERENCE]** If YuklaGo (as a company) performs customs operations *on behalf of* declarants, it risks being treated as unnotified broker activity. That includes filling fields in the official system on a server, or staff completing filings. The present design, where the user's own desktop fills fields the user confirmed in the user's own session, and the user logs in, signs and presses send, is the defensible line.
- **Fix:**
  1. Keep "signer is responsible" (p4, p15), but cite **VMQ 605 cl. 28**, not a generic claim.
  2. p6 "Vakolatli mutaxassis": replace with "Xodimingiz (shtatda) / Broker / Ishonch bildirilgan shaxs — ed1 ro'yxatida bo'lishi shart".
  3. Never offer "YuklaGo specialist files for you" unless the company files a broker notification under VMQ 847.
  4. Get a written legal opinion on automating ed2 before enabling the real cabinet (the spec already flags this; keep it as a release gate).
  5. Terms of service: YuklaGo is software, the user is the declarant, and YuklaGo does not pay customs differences. This text already exists; keep it.

### IMPORTANT (wrong or missing, but a workaround exists)

**I1. The 20 % preliminary-declaration discount is official.** The spec forbids publishing it, but the VMQ 55 annex footnote says verbatim: "Товарлар бўйича дастлабки декларациялаш амалга оширилганда божхона йиғимининг 20% миқдорида чегирма тақдим этилади". It also says the fee is charged once for preliminary, temporary, incomplete and periodic declarations (https://lex.uz/docs/7357270).
- **Screens:** spec §8.5 table, §11 "claims not to use", p8 "Yo'lda" option, p10.
- **Fix:**
  1. Correct the spec.
  2. Add a "Dastlabki deklaratsiya" path when the shipment is "Yo'lda" (p8): file before arrival, with the 30-day lapse clock (BK 262).
  3. Show "yig'im −20 %" with the Rasmiy chip. Misol uchun: 1 BHM 440,000 → 352,000.

**I2. PF-5414 is repealed, and the spec link is dead.** `https://lex.uz/docs/-3688185` returns 404. PF-5414 is at https://lex.uz/docs/3680571 and **lost force on 01.04.2025**.
- **Screens:** p4 ("2018-yil 1-iyuldan…"); spec appendix.
- **Fix:** cite VMQ 605 cl. 1 and BK 274 instead.

**I3. ERI facts: key types, issuer, local client.**
- **What I found:**
  - ed2 accepts **PFX file keys, USB-TOKEN and BAIK-TOKEN** through E-IMZO (observed live).
  - ERI keys are distributed by **"Yangi texnologiyalar ilmiy-axborot markazi" AJ** (VMQ 605 cl. 26), which fills p6's placeholder "[ERI beruvchi markaz]".
  - p6 and p18 speak of a "Bojxona ERI tokeni (USB)". A standard E-IMZO key may be enough. **[UNVERIFIED]** whether customs accepts any E-IMZO key, or only one tied to the company director or specialist and registered in the cabinet.
- **Fix:**
  1. Reword to "ERI kaliti (E-IMZO: PFX fayl yoki token)".
  2. Add "E-IMZO dasturi o'rnatilgan va ishlayapti" to readiness.
  3. The desktop embedded browser must let ed2's E-IMZO client reach the local E-IMZO module. Test this first; it is the most likely technical blocker.

**I4. Advance information and arrival steps are missing.** BK 206 part 3: authorised persons **must** submit advance information on goods arriving by road, rail or air **before arrival**, online, and are responsible for its accuracy. The carrier also files the short BYUD (VMQ 605 cl. 8), and the transit declaration number later goes into grafa 40.
- **Screens:** p8 "Yuk hozir qayerda?"; p9.
- **Fix:** add a "Yo'lda" checklist: "Tashuvchi dastlabki ma'lumot yubordimi? Tranzit deklaratsiya raqami? Qaysi postga keladi?" Store these for grafa 29, 30 and 40.
- **Correction to my own Lesson 1:** Lesson 1 said advance information is mostly a right. Art. 206 part 3 makes it mandatory for these transport modes.

**I5. The invoice check should test the 12 mandatory fields, not 11 "read" fields.** VMQ 605 Annex 1a (from 07.01.2025, via VMQ 630, https://www.lex.uz/uz/docs/-7138545) requires:
1. seller name, address, STIR;
2. **buyer name, address, STIR, phone**;
3. **HS code of at least 6 digits**;
4. **country of origin**;
5. name, brand, model, article and technical description;
6. invoice value;
7. gross weight;
8. net weight;
9. **number of packages**;
10. **quantity in the supplementary unit**;
11. **Incoterms 2010** term;
12. **contract number and date**.

The sample invoice on p13 lacks several of these (buyer STIR and phone, HS code, origin, packages, contract reference).
- **Screen:** p13.
- **Fix:** add an "Invoys talablarga mosmi? 12/12" checklist with missing items as warnings, and a supplier-request text. Packing list: keep it optional. It is explicitly *not* required (cl. 11¹), so do not block on it.

**I6. Incoterms version.** The rules say "Inkoterms — 2010". Most Chinese invoices now say Incoterms 2020.
- **Screen:** p13, p15 grafa 20.
- **Fix:** map 2020 terms to the grafa 20 code and flag DPU/DAT differences. **[UNVERIFIED]** how ed2 handles 2020 terms.

**I7. Treat E-kontrakt as required for paid contracts.** Grafa С item 1 needs the contract's ID in the Unified electronic information system of foreign trade operations, and BK 243 compares that system against the BYUD.
- **Screen:** p11.
- **Fix:** turn "Qachon talab qilinadi: [shartlar]" into "To'lovli tashqi savdo shartnomasi uchun — ID С-grafaga yoziladi". **[INFERENCE]** Exceptions (gratuitous supplies, no contract) are covered by the grafa 45 wording; ask a lawyer.

**I8. The rejection explainer needs a real taxonomy and a BDT path.**
- **Screen:** p24.
- **Fix:** see §6. Add the "BDT (tuzatish shakli)" route with its fee (25 % of BHM per VMQ 55), and the rule that a BYUD can be withdrawn before release (BK 266).

**I9. Corridors, inspection and fees after filing are not shown.**
- **Screens:** p24, p9.
- **What to show:**
  - corridors: green / yellow / red / blue (PQ-122 cl. 15);
  - timing: low 3 h, medium 8 h (VMQ 605, VMQ 700 ed.); otherwise 1 working day, not counting risk-management and other controls (BK 248);
  - the post must be notified within 30 minutes of arrival (cl. 6);
  - inspection fee 25 % of BHM per hour (2 BHM per hour out of hours); out-of-hours fee 25 %, not charged on auto-cleared BYUDs; storage fees (all VMQ 55).
- **Fix:** add these states to the status and the "what could still cost money" box.

**I10. Multi-item shipments.** All boards show one item ("Tovar 1").
- **Fix:**
  - support N items: grafas 31–47 repeat per item, grafa 3 holds extra sheets, grafa 5 the item count;
  - split freight across items by value share (BK 304);
  - charge the fee once per BYUD on the total CV.

**I11. HS-code screen: add the advance-ruling route.** BK 369–372: a preliminary decision is binding for 1 year, and its fee is 75 % of BHM (VMQ 55).
- **Screen:** p14 "Ishonchim komil emas".
- **Fix:** offer "Dastlabki qaror so'rash" next to "Broker bilan maslahatlashaman". Also show the nomenclature edition (TIF TN per PQ-181 of 14.05.2025) beside "rasmiy ro'yxatda bor".

**I12. The export (EK10) flow is a stub.** See §7.
- **Screens:** p8 ("Eksport tanlansa… [v2 spec, 'Eksport']"); p7 row YG-0402; p25.

**I13. Liability messaging needs the actual exposure.**
- **Screens:** p4, p15, p16.
- **Fix:** where the user ticks "men javob beraman", list the real consequences in plain words, with links:
  - misdeclaration fines (MJtK 227⁸, 227¹⁰, 227²², 227²⁵, 227²⁶): 3–15 BHM, with confiscation possible under 227¹⁹ and 227²²;
  - a criminal route for smuggling (Criminal Code 182).

  This is honest and protects the company.

### NICE-TO-HAVE

- **N1.** Use the ed1 live counters (sent / returned / cleared, about 21k errors a day) in the pitch, cited and dated, instead of unverified broker statistics.
- **N2.** Show the band edge in the payments view: "bojxona qiymati 10,000 $ ga yaqin — keyingi diapazonda yig'im 1.5 BHM".
- **N3.** Grafa 31: auto-compose the description from brand, model, article and technical parameters, as Annex 1a item 5 requires, and add the package count.
- **N4.** Grafa 41: fill the supplementary unit from the TIF TN row (for example "dona") and validate the quantity.
- **N5.** Product library (p25): store the permit or certificate validity per contract (PQ-122 one-year reuse), and the origin-certificate status per supplier.
- **N6.** Settings (p27): an ERI expiry reminder and a "vakolat muddati" (authority period) expiry reminder.
- **N7.** Russian copy: use official RU terms (ГТД/ДТ, «графа», «декларирующее лицо», «Единое окно»).
- **N8.** Use a holiday calendar for working-day rules (short BYUD, 1-working-day processing).

---

## 4. Screen-by-screen walk-through

| Board | Screen | Declarant notes | Findings |
|---|---|---|---|
| p1 | Design system | Excellent trust primitives. Add a **"Namuna"** chip for sample data so placeholders never show "Rasmiy". The "Mock vs real" frame names ed2.customs.uz correctly. | C2 |
| p2–3 | Header and rail | The rail lacks the **E-arxiv**, **To'lov (avans)** and **Yagona darcha** checkpoints. "Saqlash: [N] kun" should be 60/10 days (BK 85). | C4, C5, C7, C8 |
| p4 | Landing | The calculator uses 10 % and 310,000 under "Rasmiy" (both wrong; see C2). It has no origin-certificate line. The 2018 right should cite VMQ 605 cl. 1, not PF-5414. | C1, C2, I2 |
| p5 | Login | Fine. Keep "ERI paroli hech qachon so'ralmaydi". | — |
| p6 | Path choice and readiness | Add E-IMZO client, key types, the ed1 declaring-persons list with authority period, E-arxiv, and the ERI issuer (VMQ 605 cl. 26). Replace "vakolatli mutaxassis" with the 3 legal categories. | C4, C9, I3 |
| p7 | Home | Deadline source placeholders; see the C7 table. Add a "To'lov tayyormi?" card. | C5, C7 |
| p8 | New shipment | The "Yo'lda" option should offer **preliminary declaration (−20 % fee)**. Export choice: see §7. | I1, I4, I12 |
| p9 | Overview / deadlines | 27.11 is the conservative count; label it. Fill the consequences (3 BHM auto fine, penya). | C7 |
| p10 | Landed cost | Freight only to the border, plus insurance. Rate date. Combined rates. 15 % for 853952. Origin-certificate toggle with and without. Fee = 1 BHM (440,000 from 01.09.2026). | C1, C2, C3 |
| p11 | Preference, contract, bank | "Imtiyoz topilmadi" hides the bigger risk (the 300¹ surcharge). E-kontrakt → grafa С. | C1, I7 |
| p12 | Permits | Check that permits exist **in Yagona darcha**, not only "in lists". Add an origin-certificate row. | C8, C1 |
| p13 | Documents | 12-field invoice check; packing list optional; contract number on the invoice; FOB vs Incoterms 2010. | I5, I6 |
| p14 | TIF TN code | The alternative-code rates look swapped against the tariff table. Add the advance ruling (75 % BHM, binding 1 year). | C2, I11 |
| p15–16 | Payments and draft | Grafa 47 needs extra-duty and combined-rate lines and the ТУ code. The CV fix is C3. The draft must show all IM40 grafas (37, 40, С…). The blocker logic is good. | C1–C3, C6 |
| p17–18 | Fill set-up | Groups say "B"; it should be «С». Add a "funds ready" precondition and an E-arxiv numbers precondition. | C5, C6 |
| p19–22 | Mock session | 43 ≠ valuation method (for resale it is 0); 45 in contract currency; 46 in thousand USD; 36 likely not an IM40 field. The pause, hand-off and failure UX is very good. | C6 |
| p23 | Session log | Good. Add the grafa list version and the ed2 page version (DOM hash) to the log for disputes. | N |
| p24 | After filing | Wrong order of states; add registered / accepted / corridor / inspection / BDT. Use the real rejection taxonomy (§6). | C5, I8, I9 |
| p25 | Library | Good re-check on tariff change. Store origin and permit validity. | N5 |
| p26 | Broker hand-off | Add: list the broker in ed1 with an authority period and share the E-arxiv numbers; a broker contract (BK 277) is needed. | C4, C9 |
| p27 | Settings | Add ERI expiry and authority-period expiry. | N6 |
| p28 | Mobile | Same number issues as p10 and p15. | C2 |

---

## 5. IM40 BYUD grafa map: what goes where (Yo'riqnoma 2773, ch. 5, cl. 24–25)

Source: https://lex.uz/uz/docs/-2924955. The e-form was renewed from 11.03.2024 (https://www.customs.uz/page/byud-va-bdtning-elektron-shakllari). **Check field IDs on the live ed2 form.**

| Grafa | Name | Content and YuklaGo source |
|---|---|---|
| 1 | Declaration type | **IM 40** (EK 10 for export). |
| 2 | Exporter / sender | Seller from the invoice; must match the contract. |
| 3 | Extra sheets | Needed when there is more than one item. |
| 5 | Total items | Count of 32 entries. |
| 7 | Registration number | Assigned by the system; the declarant enters the **post code**. |
| 8 | Importer / consignee | Company name, address, STIR (profile). |
| 9 | Person responsible for financial settlement | Usually the importer; from the profile. |
| 11 | Trading country | Country of the seller (contract). |
| 12 | Total customs value | Σ45 converted as the form requires. |
| 13 | (in the fill list) | **[UNVERIFIED]** content in the current e-form. |
| 14 | Declarant / broker | The declarant or broker, plus the signer. |
| 15 / 15a | Country of dispatch / code | From the CMR / airway bill. |
| 18 | Transport at departure | Vehicle number(s) from the CMR. |
| 19 | Container | 0 or 1. |
| 20 | Delivery terms | Incoterms code plus place (see I6). |
| 21 | Transport at the border | From the CMR / transit declaration. |
| 22 | Currency and total invoice value | Contract currency, Σ42. |
| 23 | Exchange rate | **CB rate on the acceptance day.** |
| 24 | Nature of transaction | Classifier code. |
| 25 / 26 | Transport mode at the border / inland | Classifier codes. |
| 28 | Financial and bank data | Bank details. |
| 29 | Border customs | Post of entry. |
| 30 | Location of goods | Temporary-storage warehouse and its licence. |
| 31 | Packages and description | Marks, number and type of packages, full technical description. |
| 32 | Item no. | 1…N. |
| 33 | Goods code | 10-digit TIF TN code. |
| 34 | Origin country code | From the origin certificate or invoice (drives C1). |
| 35 | Gross weight (kg) | 3 decimals. |
| 37 | Procedure | **7-digit code**: current regime + previous regime + feature. |
| 38 | Net weight (kg) | 3 decimals. |
| 39 | Quota | Only for quota goods. |
| 40 | Previous document | Previous BYUD/"ГТД" number, item, weights, quantity. |
| 41 | Supplementary unit | Per the TIF TN row. |
| 42 | Invoice value | Contract currency. |
| 43 | Own needs flag | **0 = not for own needs, 1 = own needs.** |
| 44 | Documents | Classifier code + number + date for each document; E-arxiv special numbers. |
| 45 | Customs value | **Contract currency**, 2 decimals. |
| 46 | Statistical value | **Thousand USD**, CIF/CIP border basis, 3 decimals. |
| 47 | Payment calculation | Per payment type: code, base (so'm), rate, sum, **ТУ = БН/КТ**. |
| 48 | Deferral | If granted. |
| 49 | Warehouse | If applicable. |
| 50 | Trusted person | If applicable. |
| 54 | Place, date, declaring person | Filled by the declaring person. |
| С | Contract ID | Item 1 = contract ID in the foreign-trade operations system, plus other items per the instruction. |

**EK10 differences (export chapter of 2773):**
- grafa 1 = EK 10;
- 17/17a = destination country;
- 43 has export-specific meaning (cl. 48, 51 describe it) — **[UNVERIFIED]** the exact codes, read them before building export;
- payments are usually fees only.

---

## 6. Typical rejection and return reasons (for the p24 explainer and the pre-check)

Official signal: about **21,205 errors a day** are found in BYUDs (ed1 counter text). Today's sample: 22 of 84 returned; yesterday's: 36 of 76.

Recurring reasons in practice **[PRACTICE — not an official list; validate against real ed2 messages before shipping]**:

1. Permit or certificate **not in Yagona darcha**, or for a different HS code or STIR (VMQ 605 cl. 15 stage 1).
2. Grafa 44 is missing a required document code: conformity 417, origin 701, contract 301, exemption basis 6xx, or the E-arxiv number.
3. Grafa С contract ID missing, or the contract is not registered in E-kontrakt / the foreign-trade system, or the goods, quantity or price do not match the contract (BK 243).
4. HS code inactive or wrong length; code vs description mismatch; marking (Asl belgisi) required but missing.
5. Arithmetic or format errors: 12 ≠ Σ45; 22 ≠ Σ42; 38 > 35; rounding in 35, 38, 45, 46; wrong exchange rate in 23.
6. Customs value below the risk profile, or freight and insurance not added (valuation queries; BK 301–305).
7. Insufficient advance funds for the payments in 47 (BK 327, 334).
8. Wrong previous document in 40 (transit or temporary-storage reference) or wrong procedure code in 37.
9. Signer not in the declaring-persons list, or the authority period has expired (VMQ 605 cl. 15 stage 2).
10. Invoice missing Annex 1a fields (buyer STIR, origin, Incoterms, contract number).

**Pre-check:** encode reasons 2–5, 8, 9 and 10 as blocking rules on p15 before "Kabinetni to'ldirish".

---

## 7. Export (EK10): gaps

The current design only says "kelib chiqish sertifikati, fitosanitar talablar va valyuta tushumi bosqichlari qo'shiladi" (p8), and shows YG-0402 (dried apricots to Turkey) as "Topshirildi".

| Need | Basis | Fix |
|---|---|---|
| Declare **before goods actually leave** (no 15-day clock). | VMQ 605 cl. 11 | Export clock: "yuk chiqib ketishidan oldin". |
| Export filing goes via **"Экспорт уч қадам" (cargo.customs.uz)**, listed on ed1. | ed1 service list | Add the second filing target and a separate field map. **[UNVERIFIED]** whether ed2 also accepts EK10. |
| Export regime = Uzbek goods leave without an obligation to return; the goods must leave in the state they were in when the BYUD was registered. | BK 29–30 | Warn if the load changes after filing (re-packing, mixed lots). |
| The documents list is set by the Cabinet of Ministers; customs **checks permits itself** in its information system. | BK 31; VMQ 605 cl. 11¹ | Phytosanitary certificate for dried fruit must be in Yagona darcha. |
| Certificate of origin for the *buyer's* preference (GSP+, CIS FTA, …). | BK 363–364 | Optional step, "importer requests it". **[UNVERIFIED]** the issuing body and procedure. |
| VAT 0 % on export needs proof: contract, export BYUD, transport documents with the border-crossing mark (or the electronic customs-to-tax feed). | Tax Code 260–261 (https://lex.uz/docs/4674902) | Post-release checklist: "QQS 0 % uchun hujjatlar". |
| Export proceeds and receivables are monitored (ed1 has "overdue receivables" and "unfair fruit-and-vegetable exporters list"). | ed1 services; BK 243 | Reminder: "valyuta tushumi muddati". **[UNVERIFIED]** the current statutory term; do not show a number until verified. |
| Fees use the same VMQ 55 bands; duties are usually none. | VMQ 55; tariff | Payments view: "eksport — odatda faqat yig'im". **[UNVERIFIED]** the export-duty list. |

---

## 8. Corrections to spec v2 (claim → status)

| Spec claim | Status | Source |
|---|---|---|
| Cabinet = ed2.customs.uz | **Partly right.** ed2 = e-declaration with ERI login. The participant cabinet (declaring persons, reconciliation) = ed1/PersonCabinet. Export = cargo.customs.uz. | live check, §1 |
| PF-5414 gives the right to file without a broker | **Repealed 01.04.2025; link 404.** Cite VMQ 605 cl. 1. | https://lex.uz/docs/3680571; https://lex.uz/uz/docs/-3844549 |
| Processing low 3 h / medium 8 h / otherwise 1 working day (art. 248) | **Correct.** Art. 248 excludes risk-management and other-agency time. | BK 248; VMQ 605 annex |
| Temporary storage 60 days / 10 perishable (art. 85) | **Correct.** Counted from the day the goods acquire that status. | BK 85 |
| Art. 206 advance cargo information | **Correct, and stronger:** mandatory for road, rail and air before arrival (part 3, from 03.05.2022). | BK 206 |
| VMQ 605 cl. 11: 15 days; export before leaving | **Correct.** | VMQ 605 cl. 11 |
| VMQ 847 broker: legal entity, ≥2 specialists, 1000 BHM security, via license.gov.uz | **Correct.** Also: cabinet required; qualification certificates from 01.10.2025; fee 50 % of BHM; debt cleared in 10 days. | https://lex.uz/docs/-7274716 |
| Art. 266 three-year amendment window | **Correct.** Also: withdrawal before release. | BK 266 |
| "Do not publish 20 % preliminary discount" | **Wrong:** it is in the VMQ 55 footnote. | https://lex.uz/docs/7357270 |
| Packing list not mandatory | **Correct** (cl. 11¹ excludes the packing list). | https://www.lex.uz/uz/docs/-7138545 |
| E-kontrakt "[UNVERIFIED] whether mandatory" | **Effectively needed** for paid contracts: the contract ID goes into grafa С. | 2773 grafa С; BK 243 |
| (missing) Extra duty without origin certificate | **Add:** BK 300¹, 366 from 28.02.2026. | BK |
| (missing) Pre-funding / payment timing | **Add:** BK 327, 334. | BK |
| (missing) E-arxiv and declaring-persons list | **Add:** VMQ 605 cl. 15 stage 2. | VMQ 605 |

---

## 9. Open uncertainties (to verify before build)

1. Band boundaries of art. 300¹ at exactly 10 %, 20 % and 30 %.
2. Whether the art. 300¹ duty enters the VAT base (my inference: yes).
3. Day counting for the 15-day clock (is the presentation day day 1?) and the weekend roll-over.
4. Whether ed2 accepts any E-IMZO key, or only keys of persons registered in the declaring-persons list for that STIR (likely the latter for signing; confirm). Also whether the embedded browser can talk to the local E-IMZO module.
5. Whether the current ed2 e-form still has grafa 36 and 13, and their labels.
6. The exact mapping of the 9405 42 tariff rows; the current PQ-3818 edition after 16.02.2026.
7. Whether my.gov.uz service 207 is the declaring-persons registration (ed1 links it).
8. Export: issuer of origin certificates, the currency-proceeds term, any export duties, and whether EK10 can be filed in ed2 or only in cargo.customs.uz.
9. Incoterms 2020 handling in grafa 20.
10. Legal status of automated filling of ed2 from the user's own computer (release gate).

---

## 10. Sources

- Customs Code (O'RQ-400), current text: https://lex.uz/docs/2876354
  - arts. 29–31, 85, 206, 243, 248, 261, 262, 266, 274, 276, 277, 282, 293, 300¹, 301–305, 326, 327, 334, 349, 363–366, 369–372.
- VMQ 605 (declaration procedure Nizom, as amended by VMQ 630, 700, 393): https://lex.uz/uz/docs/-3844549. VMQ 630 (cl. 11¹ and Annex 1a): https://www.lex.uz/uz/docs/-7138545
- Yo'riqnoma 2773 (BYUD filling instruction): https://lex.uz/uz/docs/-2924955
- VMQ 55 (customs fees, 20 % preliminary discount): https://lex.uz/docs/7357270
- VMQ 847 (broker notification passport): https://lex.uz/docs/-7274716
- PQ-3818 (tariff): https://lex.uz/docs/3802363
- PQ-122 (corridors, Yagona darcha, single platform): https://lex.uz/docs/-7452043
- BHM 440,000 from 01.09.2026 (PF-115): https://www.lex.uz/uz/docs/-8283656
- Tax Code (VAT 12 %, import VAT base, export confirmation): https://lex.uz/docs/4674902
- MJtK (administrative fines): https://lex.uz/uz/docs/-97664
- O'RQ-956 (broker by notification): https://www.lex.uz/acts/7093753
- PF-5414 (repealed 01.04.2025): https://lex.uz/docs/3680571
- Live official systems:
  - https://ed2.customs.uz/
  - https://ed1.customs.uz/PersonCabinet/
  - https://cargo.customs.uz
  - https://contract.customs.uz
  - https://notarif.customs.uz/notarif/
  - https://www.customs.uz/page/byud-va-bdtning-elektron-shakllari
- Background: Lesson 1 (`/workspace/bojxona/dars-01-import.md`). Its note on advance information should be corrected per BK 206 part 3.

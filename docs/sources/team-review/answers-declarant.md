# Answers from the declarant expert (Bojxona Deklarant Ustoz, `d098a0b5`) to the YuklaGo PM (spec v3)

**Written:** 18.11.2026, about 03:50 Tashkent time (UTC+5).

**Inputs read:**
- `team-review/product.md`, section (c), the three Deklarant placeholders;
- `yuklago-spec-v2.md`: §3 Phase 1, §6 journey, Y4 / Y18 / Y19 / Y21;
- `pm/spec-v2-audit.md`;
- the teammates' reviews `team-review/broker-export-regimes.md` and `reviews/broker-eksport-maxsus-rejimlar-v1.md`. I re-read their key sources myself and say which ones;
- my earlier review `team-review/declarant.md`.

**Spec v3:** I found **no spec v3 file** anywhere in `/workspace/hackathon/`. I answered against v2 plus the PM's questions.

**P0 grafa map:** `/workspace/hackathon/data/declarant/` **does not exist yet** (checked 03:49). Only `data/tariff/` exists. §4 gives the official grafa list the map should be built from.

**Labels:**
- **[SOURCED]** = I read it in the official text today. The link is given.
- **[UNVERIFIED]** = I could not confirm it in an official source.
- **[INFERENCE]** = my reading of a rule, not words in the text.
- **[PRACTICE]** = declarant practice with no written source.
- No lead time or number appears unless an official text gives it.

---

## 1. Authorised specialist: who may sign for the user, and how they are registered

### 1.1 Who is allowed to submit and sign the TED (electronic declaration)

VMQ 605, cl. 2 (definitions; edition of VMQ 700, in force 08.02.2026), https://lex.uz/uz/docs/-3844549 **[SOURCED]**:

- **"Deklaratsiyalovchi shaxs"** (declaring person, the one who fills, signs and submits the TED) is exactly one of the following:
  - (a) the **declarant itself**, submitting in its own name;
  - (b) a **customs clearance specialist on the declarant's staff** (shtat birligi);
  - (c) a specialist on the staff of a **customs broker that has a contract with the declarant**.
- **"Mutaxassis"** (specialist): a citizen (natural person) of Uzbekistan with an **employment contract** (mehnat shartnomasi) with a customs broker or another legal entity, doing clearance work in that entity's name. The Customs Code (BK) art. 284 says the same, https://lex.uz/docs/2876354. The old qualification-attestation part of art. 284 **lost force in 2018** (same page). So the law sets **no attestation** for an in-house specialist. **[SOURCED]**
- **"Ishonch bildirilgan shaxs"** (trusted person): acts for the declarant under a **contract or power of attorney** (ishonchnoma), and is **responsible for the documents and data** given as the basis of the TED (cl. 2). This person can build the E-arxiv (cl. 15). **[SOURCED]**
- **[INFERENCE]** The trusted person is **not** in the definition of "deklaratsiyalovchi shaxs". So a power of attorney alone does **not** let an outside person sign the TED. They must be the declarant's employee, or a broker's employee. **[UNVERIFIED]** cl. 15 stage 2 also lists the "ishonch bildirgan shaxs" in the participant list, so how ed2 treats a trusted person who tries to sign needs a live test or a written answer from customs.
- When the **declarant files in its own name**, it has the rights and duties of a specialist (VMQ 605, ch. on responsibilities). **[SOURCED]**
- **Responsibility split** (VMQ 605 cl. 30, edition of VMQ 700) **[SOURCED]**:
  - the **declaring person** answers for the TED data and for its match with the documents provided, except where the documents themselves were wrong;
  - the **declarant or trusted person** answers for the accuracy of the documents.
- **Sole proprietors (YaTT) [UNVERIFIED]:**
  - A YaTT can be a declarant (BK 274 covers Uzbek legal and natural persons).
  - The definition of "mutaxassis" speaks of a contract with a "**legal entity**". Whether a YaTT's employee can be its declaring person is unclear.
  - Safe Phase 1 rule: **a YaTT signs personally, or uses a broker.**

### 1.2 How the signer is registered (TIF participant cabinet)

- **Where:**
  - The ed1 cabinet (https://ed1.customs.uz/PersonCabinet/) has the service **"Декларацияловчи шахслар рўйхати"**, described as the "list of declaring persons who may submit the BYUD to customs for goods imported or exported in the TIF participant's name". It links to my.gov.uz service 207. **[SOURCED, checked live 18.11.2026]**
  - **my.gov.uz service 207, "Deklaratsiyalovchi shaxslar ro'yxati"** (https://my.gov.uz/uz/service/207) says: **free**, completed **automatically** in about 1 minute, **no documents required**, for natural and legal persons, provided by the Customs Committee. Its legal basis is VMQ 605 and Customs Committee decision No. 3220 of 10.02.2020. **[SOURCED]**
- **What the declarant enters** (VMQ 605 cl. 15, stage 2) **[SOURCED]**:
  - the trusted person, broker, or **own staff specialist** for the participant list;
  - the **authority period** (vakolat muddati) during which they may submit TEDs;
  - if a broker was listed, the **broker** in turn registers its own staff specialist and their authority period.
  - Exceptions: non-residents and diplomatic missions do not list specialists.
- **Documents for the broker or specialist (cl. 15):** the declarant uploads them to **E-arxiv**, signed with ERI, and gets **special numbers**. It then gives those numbers to the listed broker or specialist, who can view and copy **only** those documents. **[SOURCED]**
- **Accuracy:** declarants and brokers are responsible for the accuracy of the data they enter in the participant list (cl. 30). **[SOURCED]**
- **[UNVERIFIED]** The exact fields of the ed1 form: whether it asks for the employment-order number, the PINFL, or only the ERI certificate. It needs a logged-in look.

### 1.3 What the user must have before someone else signs (checklist for p6 and Y1)

| Item | Status | Source |
|---|---|---|
| Company or YaTT registered; foreign trade done in its name | SOURCED | BK 274 |
| **E-IMZO key for every person who will sign.** ed2 login offers **PFX file**, **USB-TOKEN** and **BAIK-TOKEN**, and loads `e-imzo-client.js`, so the E-IMZO app must be installed. | SOURCED (live page) | https://ed2.customs.uz/ |
| ERI keys are distributed by "Yangi texnologiyalar ilmiy-axborot markazi" AJ | SOURCED | VMQ 605 cl. 26 |
| Whether the signer's key must be a **personal key linked to the company's STIR** | UNVERIFIED | — |
| **Own employee:** employment contract plus employment order. Uzbek citizen. Entered in the ed1 list with an authority period. | SOURCED (definition, list); the order is my **[INFERENCE]** by analogy with VMQ 847 | VMQ 605 cl. 2, 15; BK 284 |
| **Broker:** a written contract with a notified customs broker (BK 277). Listed in ed1 with an authority period. The broker then lists its own specialist. | SOURCED | BK 277; VMQ 605 cl. 15 |
| **Power of attorney only (ishonchnoma):** enough for document handling and E-arxiv; **not enough to sign the TED** | INFERENCE / UNVERIFIED (see 1.1) | VMQ 605 cl. 2 |
| E-arxiv documents uploaded, special numbers shared | SOURCED | VMQ 605 cl. 15 |

### 1.4 VMQ 847 limits, i.e. when a third party becomes a "broker"

From the notification passport "Bojxona brokeri faoliyati", VMQ 847 of 18.12.2024 (https://lex.uz/docs/-7274716) **[SOURCED]**:

- **Who may notify:** a **legal entity only**.
- **How:** through the "Litsenziya" information system or my.gov.uz, to the Customs Committee.
- **Fee:** 50 % of BHM.
- **Conditions:**
  - security for customs payments of **1000 × BHM** (insurance policy or bank guarantee);
  - a cabinet in the customs system;
  - **2 or more staff specialists**;
  - from **01.10.2025**, specialists need a **qualification certificate** from a Customs-Committee-approved curriculum, renewed **every 2 years**;
  - customs debts cleared **within 10 days**;
  - hires and dismissals of specialists notified **within 5 days**;
  - services provided only **under contract** with the declarant;
  - extra retraining for a specialist with **more than 3 administrative penalties in a month** for BYUD errors.
- **Fines:** MJtK 227²⁷ fines broker officials **5–10 BHM** (10–20 BHM if repeated), https://lex.uz/uz/docs/-97664.

**Product rule:**
- p6 "Vakolatli mutaxassis" must offer exactly three options: **Xodimingiz (shtatda)** / **Bojxona brokeri (shartnoma bilan)** / **O'zim (rahbar yoki YaTT)**.
- **[INFERENCE]** YuklaGo staff must never be the "declaring person" for users unless YuklaGo files a VMQ 847 notification.

**Fills placeholder p.06 lines 70–71** (Uzbek copy):

> "Boshqa shaxs imzolasa, u (1) kompaniyangiz xodimi (mehnat shartnomasi bilan) yoki (2) siz shartnoma tuzgan bojxona brokerining xodimi bo'lishi va ed1 kabinetidagi "Deklaratsiyalovchi shaxslar ro'yxati"ga vakolat muddati bilan kiritilgan bo'lishi kerak (VMQ 605, 2- va 15-bandlar; my.gov.uz xizmati 207). Faqat ishonchnoma TEDni imzolash uchun yetarli emas."

---

## 2. Export path (EK10)

### 2.1 Steps and documents

| # | Step | Documents / system | Source | Status |
|---|---|---|---|---|
| 1 | Check who may export and register the contract | Exporter = Uzbek legal entity or YaTT. Contract (or, for fruit and vegetables, an **invoice entered in the Unified electronic information system of foreign trade operations (TSOYaEAT)**). Contract ID goes in BYUD grafa С. | BK 274; VMQ 163 cl. 6 (PF-174 edition, 01.09.2026) https://lex.uz/uz/docs/-4213596; Yo'riqnoma 2773 grafa С https://lex.uz/uz/docs/-2924955 | SOURCED |
| 1a | **Fruit and vegetables (TIF TN 07, 08, 0904, 1202):** if the exporter has overdue receivables, it is placed **automatically** on the "nohalol eksport qiluvchilar reyestri" (unfair exporters register). It may then export **only on 100 % prepayment**. Natural losses are entered in TSOYaEAT. | — | VMQ 163 cl. 3, 8, 11, 12 | SOURCED |
| 1b | Minimum export prices for fruit and vegetables | Approved by a government commission | PQ-107 (29.02.2024), per teammate source https://lex.uz/uz/acts/-6825806 | UNVERIFIED (not re-read by me) |
| 2 | **Phytosanitary certificate** (plant products) | **Each consignment** of exported plant products travels with a phytosanitary certificate (Plant Quarantine Law, art. 12, https://www.lex.uz/uz/docs/-119173). Issued **through Yagona darcha** by the **territorial departments** of the **Plant Quarantine and Protection Agency** under the Ministry of Agriculture (the Karakalpakstan agency, or the regional and Tashkent city departments), one per transport unit. Electronic application signed with ERI. **Decision within 5 working days**. If documents are incomplete, a notice is sent within 1 working day. A fee is charged per the passport. | VMQ 65 (29.01.2018) Annex 3, as amended by VMQ 727 of 01.11.2024, cl. 1–3, 10–13 https://lex.uz/uz/acts/-7208474 | SOURCED. **[UNVERIFIED]**: fee amount; whether a later amendment changed the 5 days |
| 2a | Old law text: notify the regional quarantine service **at least 30 days** before shipment and present the goods **15 days** before | — | Law 113-I art. 12 (text on lex.uz) | SOURCED as text. **[UNVERIFIED]** whether it is still applied now that issuance runs through Yagona darcha |
| 2b | Veterinary goods: export permit per calendar year; application reviewed in 2 working days; export veterinary certificate in 7 working days | — | VMQ 148 (10.04.2023), per teammate source https://www.lex.uz/acts/-6427764 | UNVERIFIED (not re-read by me) |
| 3 | **Certificate of origin** (if the buyer needs it for a preference or for their customs) | **Issuer: "O'zbekekspertiza" AJ** (the "vakolatli organ"), **not** the Chamber of Commerce itself. Application at the authorised body **at the place of loading**, on paper, by post, or electronically. **1 working day** for expertise and certificate; for fruit and vegetables also 1 working day; **up to 2 working days** for HS chapters 84–89 or a large assortment (more than 3 producers or more than 30 types). Forms: **A** (GSP countries), **ST-1** (CIS), **ST-UZ**, and forms under other agreements. For agricultural produce, attach the **invoice** and **proof of origin** (land-use right, or purchase documents). | VMQ 994 (13.12.2019, 2024 edition) Nizom, cl. 2, 22, 24, 27, 35–36 https://lex.uz/uz/docs/-4643161 | SOURCED. **[UNVERIFIED]**: which form Türkiye accepts for Uzbek dried apricots; the fee |
| 4 | **Export declaration (BYUD EK 10)** before the goods actually leave | Filed with the declaring person's ERI. ed1 lists a separate export service, **"Экспорт уч қадам" (cargo.customs.uz)**, for export BYUDs and correction forms. | VMQ 605 cl. 11; ed1 service list (live 18.11.2026) | SOURCED. **[UNVERIFIED]** whether ed2 also accepts EK10 |
| 4a | Customs **checks permits itself** in its information system; the goods must leave in the state they were in when the BYUD was registered | — | BK 29–31 https://lex.uz/docs/2876354 | SOURCED |
| 4b | Documents with the export BYUD | BYUD + accompanying (transport, commercial) documents; packing list **not** required; origin certificate if the party wishes or a treaty requires | VMQ 605 cl. 11¹ (VMQ 630) https://www.lex.uz/uz/docs/-7138545 | SOURCED |
| 5 | Payments | Customs fee per VMQ 55 bands (with a 20 % discount on preliminary declaration). **Export duties:** BK 290 provides for them, but I found **no current export-duty rate table**. PQ-3818 is the import tariff. | VMQ 55 https://lex.uz/docs/7357270; BK 290 | Fee: SOURCED. **Export duty: UNVERIFIED.** Show "eksport boji: rasmiy stavka topilmadi" (no official rate found). |
| 6 | **VAT 0 %** proof | Contract; the export BYUD; transport documents with the customs **border-crossing mark** (or the customs-to-tax electronic feed) | Tax Code arts. 260–261 https://lex.uz/docs/4674902 | SOURCED |
| 7 | **Currency proceeds (repatriation)** clock | If repatriation exceeds **180 days** from the date the non-resident's obligation arose, the operation is treated as a capital-movement operation (art. 11). **Fines** if not repatriated within **45 days after the 180** (**90 days for small business**), to the budget: **5 %** of the unrepatriated sum if late up to 360 days from export; **+10 %** if 360–545 days; **+35 %** if 545 days or more. Exemptions include overdue receivables ≤ 10 % of proceeds over the prior 36 months. Fines are refunded if proceeds arrive within set periods. | Law "Valyutani tartibga solish to'g'risida", arts. 11, 11¹ (text on lex.uz page of O'RQ-573) https://www.lex.uz/docs/-4562834 | SOURCED. **[UNVERIFIED]** that this page is the latest consolidated edition; re-check before launch |

**Fills placeholder p.08 lines 31–32**. Make the export flow 3 screens:
1. Export go/no-go: contract or invoice in TSOYaEAT, register status, phyto, vet, origin.
2. Export documents and EK10 draft.
3. Proceeds clock: 180 days, then 225 or 270 days, with fine steps.

---

## 3. When the conformity certificate (muvofiqlik sertifikati) is missing

### Who certifies

- Products are certified by **accredited product certification bodies (MSO)**, within their accreditation scope. If several exist, **the applicant chooses one** (VMQ 502 of 14.08.2024, Nizom cl. 4–5, https://lex.uz/docs/-7080176). **[SOURCED]**
- Framework law: Law O'RQ-354 "Muvofiqlikni baholash to'g'risida" (https://www.lex.uz/docs/-2248099). Certificates are issued by accredited conformity-assessment bodies. Certification or **declaration of conformity** can be mandatory or voluntary. **[SOURCED]**
- **Accreditation of the bodies:**
  - O'RQ-820 (27.02.2023) names the **O'zbekiston texnik jihatdan tartibga solish agentligi** (the successor of "O'zstandart") as the special authority (https://www.lex.uz/uz/acts/-6392305).
  - A new **O'zbekiston akkreditatsiya markazi** under the Cabinet of Ministers was set up by VMQ 460 of 04.09.2026 (https://www.lex.uz/mact/-8452378).
  - **[UNVERIFIED]** the exact current split of roles. Check before naming an agency in the UI.
  - Product copy should say "akkreditatsiyalangan sertifikatlashtirish organi (MSO)", not "O'zstandart".

### Procedure (VMQ 502 Nizom) **[SOURCED]**

1. **Imported goods** may be certified **before or after** arrival, at the applicant's choice. If certified **before** arrival, the importer must place the certificate in **Yagona darcha** and in **TSOYaEAT** (cl. 4).
2. The application goes to the chosen MSO **"through the relevant electronic system"** (cl. 9, 13). **[UNVERIFIED]** the system name and URL. I did not find a my.gov.uz service for product certification in this session, so do not show a my.gov.uz link until it is confirmed.
3. Contract with the MSO and payment, then identification and sampling, then tests by an accredited laboratory, then (if the scheme requires it) production assessment, then a decision, then the certificate is issued and entered in the **state register**.

### Stage times set by the Nizom (no total time exists)

| Stage | Time |
|---|---|
| Decision on the application | **2 working days** (cl. 14 text). The stage table in the same Nizom says **1 working day**: the text is inconsistent, show "1–2 ish kuni". |
| Return of incomplete documents | 1 working day |
| Sampling | after payment, within 1–2 working days |
| **Laboratory tests** | **"according to test duration"**: no fixed term |
| Production assessment | up to 10 working days (if in the scheme) |
| Certificate issued and registered after a positive decision | 2–3 working days (2 in the cl. text; 3 in the table) |

**So the total lead time is UNVERIFIED.** It depends on the test programme; do not show a total.

### Related rules

- Certificates and permits for **identical goods under one contract** can be issued once for up to **1 calendar year** (PQ-122, https://lex.uz/docs/-7452043). **[SOURCED]**
- **Which goods need it:** mandatory lists come from technical regulations or government lists. One commercial site claims VMQ-554 (02.09.2025) shortened the list; that is **[UNVERIFIED]**.
- Without a certificate in Yagona darcha, the TED is **not accepted** (VMQ 605 cl. 15). **[SOURCED]**

**Fills placeholder p.12 lines 73–74** (Uzbek copy):

> "Yo'q bo'lsa — O'zbekistonda akkreditatsiyalangan mahsulotlarni sertifikatlashtirish organiga (MSO, o'zingiz tanlaysiz) ariza berasiz; namuna olinadi va akkreditatsiyalangan laboratoriyada sinovdan o'tkaziladi; sertifikat davlat reyestriga kiritiladi. Yukdan oldin olsangiz, uni Yagona darcha va TSOYaEATga joylashtirasiz (VMQ 502). Umumiy muddat sinov dasturiga bog'liq — biz taxmin qilmaymiz."

---

## 4. Is the sample "48 maydon" / IM 40 draft usable?

**No. Use it only as a visual mock.** Compared with the official list (Yo'riqnoma 2773, cl. 24, https://lex.uz/uz/docs/-2924955):

- **Official IM40 grafas the declaring person fills:** 1, 2, 3, 5, 7 (post code), 8, 9, 11, 12, 13, 14, 15, 15a, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 54, **С**. That is **46 grafa IDs**.
- Grafas 31–47 **repeat for every item**, and 47 has several lines per payment type. So **no fixed "48 maydon" count is correct**. Key the map by grafa ID × item.
- **Errors in the sample** (details in `declarant.md` C6):
  - 43 is labelled "Baholash usuli". For IM40 it is **0 / 1 (own needs)**: for resale it must be **0**.
  - 45 must be in the **contract currency**, not so'm.
  - 46 must be in **thousand USD**, 3 decimals, CIF/CIP border basis.
  - 36 "Imtiyoz" is **not** in the IM40 list; preferences go into grafa **44, code 6xx**.
  - "B" should be **«С»** (contract ID in TSOYaEAT).
  - Missing: 9, 11, 13, 15/15a, 18, 21, 23–26, 28–30, **37** (7-digit procedure code), **40** (previous document), 48–50, 54.
  - **[UNVERIFIED]** grafa 13 content and whether the live ed2 form still shows 36. Check on the live form.
- **For the P0 map** (`data/declarant/`, not yet created): one row per grafa with:
  - regime (IM40 / EK10);
  - per-item flag;
  - required flag;
  - format (length, decimals, classifier);
  - source (Yo'riqnoma 2773 clause);
  - YuklaGo data source (profile / document / user / rules engine);
  - ed2 field ID (to be captured).
- EK10 has a different fill list (export chapter of 2773). **[UNVERIFIED]** the EK10 grafa 43 codes; read cl. 48 and 51 of 2773 before building.

---

## 5. Phase 1 document list: corrected and signed off

**v2 §6 step 9** lists invoice, contract, transport document, packing list if any, and certificates. That is **incomplete**. Corrected list for **IM40**:

| # | Document | Required? | Source |
|---|---|---|---|
| 1 | BYUD (TED), signed with the declaring person's ERI | Required | VMQ 605 cl. 11¹, 15 |
| 2 | **Invoice** with the **12 minimum fields** (Annex 1a) | Required | VMQ 630 → 605 Annex 1a https://www.lex.uz/uz/docs/-7138545 |
| 3 | **Foreign trade contract** and its **TSOYaEAT / E-kontrakt ID** (grafa С). For payment-based contracts, treat as required. | Required [INFERENCE from grafa С, BK 243] | 2773 grafa С; BK 243 |
| 4 | **Transport document** (CMR, AWB, SMGS) | Required | 605 cl. 11¹ ("kuzatuv hujjatlari") |
| 5 | **Previous document**: transit declaration or temporary-storage BYUD number (grafa 40) | Required when there is a previous regime | 2773 grafa 40 |
| 6 | **Permits and certificates in Yagona darcha** (conformity, SES/hygiene, phyto, vet, licence…) for that HS code | Required if the goods are controlled; the TED is not accepted otherwise | 605 cl. 15; PQ-122 cl. 17 |
| 7 | **Certificate of origin** | Legally optional (11¹), but **without it the extra duty applies** (BK 300¹, 366, from 28.02.2026). **Treat as "strongly expected"**, not optional. | BK 300¹, 366; 605 cl. 11¹ |
| 8 | **Freight, insurance and loading invoices** up to the border (to support the customs value) | Required when these costs are not in the price | BK 304 |
| 9 | Evidence of **advance funds or payment** | Needed before or at acceptance | BK 327, 334 |
| 10 | **E-arxiv special numbers** for all the above | Required by the procedure | 605 cl. 15 |
| 11 | Signer's **listing in the ed1 declaring-persons list** (if not the declarant itself) | Required | 605 cl. 15; my.gov.uz 207 |
| 12 | Packing list | **Not required** (11¹ excludes it); posts may ask for it in practice | 605 cl. 11¹; [PRACTICE] |
| 13 | Warehouse acceptance act / proof of presentation date (for the deadline clock) | Not a filing document; product evidence | [PRACTICE] |

**For EK10:** items 1–4, 6, 10, 11 plus the §2 items: phyto or vet certificate, origin certificate if the buyer needs it, TSOYaEAT entry, and the VAT-0 % evidence afterwards.

**Sign-off:** approved **with these corrections**.

---

## 6. Y18 escalation criteria: corrected

v2 lists: low confidence, unsupported regime, controlled goods, disputed valuation, unresolvable document conflict, user choice. **Keep these, and add the following.** Each one is a hard "stop self-filing, offer the broker":

| Trigger | Why | Source |
|---|---|---|
| Regime not IM40 or EK10 (transit, temporary, processing, re-export, warehouse…) | Not supported | spec §3 |
| A **permit or certificate is missing** and cannot be in Yagona darcha before the 15-day clock ends | The TED will not be accepted | 605 cl. 15; BK 261 |
| Licensed, quota, dual-use, or IP-register goods; goods needing **marking** that is not set up | Extra controls | BK 248; 2773 grafa 39 |
| **Excise goods** | Excise rules not supported | Tax Code 284 ff. |
| **Origin doubtful**, or a preference is claimed for the first time | Extra-duty and audit risk | BK 300¹, 366 |
| Valuation: related-party sale, free supply, no contract, price far below comparable, royalties or licence fees | Valuation methods 2–6 or additions needed | BK 301–305 |
| **Signer not ready**: no E-IMZO, not in the ed1 list, authority period expired | Cannot legally sign | 605 cl. 15 |
| **Deadline ≤ 2 working days** with blockers open | Risk of the automatic 3 BHM fine and storage | MJtK 227¹⁰ p.2 [threshold = PRACTICE] |
| **Same TED returned twice** for the same reason, or a customs **valuation adjustment / inspection result** is received | Needs professional handling | [PRACTICE] |
| **Red corridor** with inspection, or a request for documents the user cannot supply | Post-level negotiation | PQ-122 cl. 15 [PRACTICE] |
| More than **[N] items** in one BYUD (set N after pilot tests) | Error rate rises | [PRACTICE] |
| A YaTT whose employee wants to sign | Status of a YaTT employee as specialist is unclear | §1.1 [UNVERIFIED] |
| User asks YuklaGo staff to file for them | Possible unnotified broker activity | VMQ 847; BK 277 [INFERENCE] |

**Add to the handoff pack:** a structured **reason code** (the IDs above). Also add the reminder that the broker must be **added to the ed1 list with an authority period** and given the **E-arxiv numbers** (605 cl. 15).

---

## 7. Y19 message library (Uzbek Latin, user-facing)

**Format:** `ID | trigger | text | next step | source`.

**Rules:**
- These are **YuklaGo explanations**. They are **not** official customs reason codes, and no official code list was found.
- Match pasted cabinet text by keywords, show the closest entry, and always add the footer **"Bu — taxminiy talqin, rasmiy javob emas."**
- Entries marked [PRACTICE] must be validated against real ed2 messages before release.

### 7.1 Status and corridors

| ID | Trigger | Text (UZ) | Next step | Source |
|---|---|---|---|---|
| S01 | Uploaded, not sent | "Deklaratsiya kabinetga yuklangan, lekin hali yuborilmagan yoki roʻyxatga olinmagan." | "Kabinetda tekshirib, oʻz ERI kalitingiz bilan yuboring." | ed1 status categories (live) |
| S02 | Registered | "Deklaratsiya format-mantiqiy nazoratdan oʻtdi va roʻyxatga olindi. Endi u yuridik ahamiyatga ega." | "Qabul qilinishini kuting." | VMQ 605 cl. 15, stage 3 |
| S03 | Auto-returned | "Tizim deklaratsiyani avtomatik qaytardi: format yoki mantiqiy xato topildi." | "Xabardagi grafa raqamini toping, tuzating, qayta imzolang." | VMQ 605 cl. 15 |
| S04 | Accepted | "Deklaratsiya bojxona tomonidan qabul qilindi. 3 soat ichida qabul qilinmasa, tizim uni avtomatik qabul qiladi." | — | VMQ 605 annex (VMQ 700 ed.) |
| S05 | Green | "Yashil yoʻlak: xavf past, bojxona nazorati shakllari qoʻllanilmaydi, rasmiylashtirish avtomatik. Chiqarilgandan keyingi tekshiruv boʻlishi mumkin." | — | PQ-122 cl. 15(i) |
| S06 | Yellow | "Sariq yoʻlak: xavf oʻrta. Bir yoki bir nechta nazorat shakli qoʻllanadi (masalan, hujjat tekshiruvi), lekin bojxona koʻrigi va shaxsiy koʻrik qoʻllanmaydi." | "Soʻralgan hujjatni kabinet orqali yuboring." | PQ-122 cl. 15(ii) |
| S07 | Red | "Qizil yoʻlak: xavf yuqori. Bojxona koʻrigi boʻlishi mumkin. Koʻrik uchun yigʻim olinadi (BHMning 25 %i/soat; ish vaqtidan tashqari 2 BHM/soat)." | "Yukni koʻrikka tayyorlang; murakkab boʻlsa — broker." | PQ-122 cl. 15(iii); VMQ 55 |
| S08 | Blue | "Koʻk yoʻlak: tovar hozir chiqariladi, nazorat esa chiqarilgandan keyin oʻtkaziladi. Hujjatlarni saqlang." | "Hujjatlarni xavfsiz saqlang." | PQ-122 cl. 15(iv); 605 cl. 30 |
| S09 | Processing time | "Ishlov berish muddati: past xavf — 3 soat, oʻrta xavf — 8 soat; umumiy holda 1 ish kuni (xavfni boshqarish va boshqa idoralar tekshiruvi vaqti kirmaydi)." | — | VMQ 605 annex; BK 248 |
| S10 | Released | "Tovar chiqarildi. Kelib chiqish sertifikati keyinroq kelsa, 1 yil ichida taqdim etib, qoʻshimcha bojni qayta hisoblatishingiz mumkin." | "Sertifikat eslatmasini yoqing." | BK 271, 366 |
| S11 | Correction form (BDT) | "Bojxona deklaratsiyasini tuzatish (BDT) shakli kerak. Uni rasmiylashtirish uchun yigʻim — BHMning 25 %i." | "Tuzatishni kabinetda BDT orqali yuboring." | BK 266; VMQ 55 |

### 7.2 Rejection and return reasons

| ID | Trigger keywords | Text (UZ) | Next step | Source |
|---|---|---|---|---|
| R01 | Yagona darcha / ruxsat / sertifikat topilmadi | "Ruxsat beruvchi hujjat Yagona darcha tizimida topilmadi. Busiz deklaratsiya qabul qilinmaydi." | "Sertifikat beruvchi organdan uni Yagona darchaga kiritganini (STIR, TIF TN, muddat) tekshiring." | VMQ 605 cl. 15 |
| R02 | 44-grafa / hujjat kodi | "44-grafada kerakli hujjat (kod, raqam, sana) yoʻq yoki notoʻgʻri." | "Hujjatni E-arxivga yuklab, maxsus raqamini va kodini 44-grafaga yozing." | 2773 grafa 44; 605 cl. 15 |
| R03 | Kontrakt / С-grafa / TSOYaEAT | "Shartnoma identifikatori (С-grafa) yoʻq yoki deklaratsiya shartnoma maʼlumotlariga mos emas." | "E-kontraktda roʻyxatdan oʻtganini va tovar, miqdor, narx mosligini tekshiring." | 2773 grafa С; BK 243 |
| R04 | TIF TN / kod | "Tovar kodi amaldagi roʻyxatda yoʻq, yoki tavsifga mos emas." | "Kodni qayta tekshiring; ishonchingiz komil boʻlmasa — dastlabki qaror (BHMning 75 %i) yoki broker." | BK 369–372; VMQ 55 |
| R05 | Vazn / brutto / netto | "Brutto va netto vazn mos emas (netto bruttodan katta) yoki hujjatlardagi vazn bilan farq bor." | "35- va 38-grafalarni CMR va invoys bilan solishtiring." | 2773 grafas 35, 38 [PRACTICE] |
| R06 | Summa / 12 / 22 / 45 | "Jami summa grafalarda mos kelmaydi (masalan, 12-grafa ≠ 45-grafalar yigʻindisi)." | "Har bir tovar qatorini qayta hisoblang." | 2773 [PRACTICE] |
| R07 | Kurs / 23 | "Valyuta kursi deklaratsiya qabul qilingan kundagi Markaziy bank kursiga mos emas." | "Imzolash kuni kursni yangilang." | BK 326; 2773 grafa 23/46 |
| R08 | Bojxona qiymati / narx past | "Bojxona qiymati boʻyicha savol: narx past koʻrinadi yoki transport/sugʻurta qoʻshilmagan." | "Chegaragacha transport va sugʻurta hujjatlarini qoʻshing; murakkab boʻlsa — broker." | BK 304–305 [PRACTICE] |
| R09 | Toʻlov / mablagʻ yetarli emas | "Bojxona toʻlovlari uchun mablagʻ yetarli emas. Toʻlov deklaratsiya qabul qilinguncha yoki qabul paytida qilinadi." | "Bojxonaning gʻazna hisobvaragʻiga avans oʻtkazing; qoldiqni ed1 solishtirma dalolatnomasidan tekshiring." | BK 327, 334 |
| R10 | 40-grafa / aval hujjat | "Avvalgi hujjat (tranzit yoki vaqtincha saqlash deklaratsiyasi) raqami notoʻgʻri yoki yoʻq." | "Tashuvchidan tranzit deklaratsiya raqamini oling." | 2773 grafa 40 |
| R11 | 37-grafa / protsedura | "Protsedura kodi (37-grafa, 7 xonali) notoʻgʻri." | "Joriy va avvalgi rejim kodlarini tekshiring." | 2773 grafa 37 |
| R12 | Vakolat / deklaratsiyalovchi shaxs | "Imzolagan shaxs deklaratsiyalovchi shaxslar roʻyxatida yoʻq yoki vakolat muddati tugagan." | "ed1 kabinetida roʻyxatni yangilang (my.gov.uz xizmati 207)." | VMQ 605 cl. 15 |
| R13 | Invoys maydonlari | "Invoysda majburiy maʼlumot yetishmaydi (masalan, xaridor STIRi, kelib chiqish mamlakati, Incoterms, shartnoma raqami)." | "Yetkazib beruvchidan tuzatilgan invoys soʻrang." | VMQ 605 Annex 1a |
| R14 | Kelib chiqish | "Kelib chiqish sertifikati yoʻq yoki shubhali — qoʻshimcha bojxona boji qoʻllanadi." | "Sertifikatni yetkazib beruvchidan soʻrang; 1 yil ichida taqdim etsangiz qayta hisoblanadi." | BK 300¹, 366 |
| R15 | Markirovka | "Bu tovar majburiy raqamli markirovka (Asl belgisi) talab qiladi, lekin maʼlumot yoʻq." | "Markirovka talabini tekshiring; kerak boʻlsa — broker." | [UNVERIFIED: list source] |
| R99 | Unknown text | "Bu xabarni aniq taniy olmadik. Matnni bojxona posti yoki broker bilan tekshiring." | Broker | — |

### 7.3 Deadlines

| ID | Trigger | Text (UZ) | Source |
|---|---|---|---|
| D01 | Import clock | "Import deklaratsiyasini tovar bojxona organiga taqdim etilgan kundan boshlab 15 kalendar kun ichida topshirish kerak. Qolgan: {N} kun (ehtiyot sanasi: {sana})." | BK 261; VMQ 605 cl. 11 |
| D02 | Clock missed | "Muddat oʻtdi: kechikkan deklaratsiya uchun 3 BHM jarima yagona avtomatlashtirilgan tizim orqali avtomatik qayd etiladi. Imkon qadar tezroq topshiring." | MJtK 227¹⁰ p.2, art. 17² |
| D03 | Storage | "Vaqtincha saqlash muddati — 60 kalendar kungacha (tez buziladigan tovar — 10 kun), tovar shu maqomni olgan kundan." | BK 85 |
| D04 | Short BYUD | "Tashuvchi qisqa yuk deklaratsiyasini tovar taqdim etilganidan keyingi ish kunidan kechiktirmay beradi — tashuvchidan tasdiq soʻrang." | VMQ 605 cl. 8 |
| D05 | Preliminary | "Dastlabki deklaratsiya: tovar 30 kun ichida taqdim etilmasa, deklaratsiya berilmagan hisoblanadi. Afzallik: yigʻimdan 20 % chegirma." | BK 262; VMQ 55 |
| D06 | Export | "Eksport deklaratsiyasi tovar amalda chiqib ketguncha topshiriladi." | VMQ 605 cl. 11 |
| D07 | Proceeds | "Eksport tushumi: 180 kun ichida kutiladi; kichik biznes uchun yana 90 kun (boshqalar — 45 kun) oʻtsa, jarima 5 % dan boshlanadi." | Currency law arts. 11, 11¹ |
| D08 | Late payment | "Toʻlov kechiksa, har bir kun uchun qayta moliyalash stavkasining 1/300 miqdorida penya hisoblanadi." | BK 349 |
| D09 | Advance info | "Avtomobil, temir yoʻl va havo transportida tashuvchi tovar haqidagi dastlabki axborotni yuk yetib kelguncha yuborishi shart. Tashuvchidan tasdiq soʻrang." | BK 206 p.3 |

### 7.4 Missing documents (before filing)

| ID | Text (UZ) | Source |
|---|---|---|
| M01 | "Invoys 12 ta majburiy maydondan {k} tasini toʻliq koʻrsatmagan: {roʻyxat}." | VMQ 605 Annex 1a |
| M02 | "Shartnoma E-kontraktda roʻyxatdan oʻtganini tasdiqlang — uning ID raqami С-grafaga yoziladi." | 2773 grafa С |
| M03 | "Muvofiqlik sertifikati Yagona darchada boʻlishi kerak. Yoʻq boʻlsa — akkreditatsiyalangan MSOga ariza (VMQ 502)." | VMQ 605 cl. 15; VMQ 502 |
| M04 | "Kelib chiqish sertifikati yoʻq — qoʻshimcha boj taxminan {x} soʻm." | BK 300¹, 366 |
| M05 | "Packing list majburiy emas, lekin post soʻrashi mumkin — bor boʻlsa yuklang." | VMQ 605 cl. 11¹ [PRACTICE] |
| M06 | "Chegaragacha transport/sugʻurta hisob-fakturasi yoʻq — bojxona qiymati toʻliq emas." | BK 304 |
| M07 | "Eksport: har bir turkum uchun fitosanitariya sertifikati (Yagona darcha orqali, hududiy boshqarma; qaror 5 ish kunida)." | Law 113-I art. 12; VMQ 65 Annex 3 (VMQ 727 ed.) |
| M08 | "Imzolovchi ed1 roʻyxatida yoʻq — avval roʻyxatga kiriting (bepul, my.gov.uz 207)." | VMQ 605 cl. 15 |

---

## 8. Y4 hypothesis: do small lead users file their own BYUD, or use kargo?

**Honest answer: unknown without customer interviews.** I found **no official statistic** on the share of small importers who clear through kargo versus their own BYUD.

### Public evidence (non-official, commercial websites; treat as market signals, not facts)

- Logistics firms describe "kargo pod klyuch" as a per-kg or per-m³ price where the client does **not** deal with customs and **usually gets no declaration in their own name**:
  - UpakFF: https://upak.uz/uz/blog/kargo-yoki-rasmiy-import/ and https://upak.uz/ru/blog/kargo-ili-belaya-dostavka-iz-kitaya/
  - vezemizkitaya.uz: https://vezemizkitaya.uz/stati/kargo-iz-kitaya-v-uzbekistan/
- They also say official import **"usually uses a customs broker"** (UpakFF).
- GSR Logistics shows **three models**: personal parcel, **"we are the importer"** (forwarder's own contract), and **"your contract"** (your company or YaTT, full pack), and markets kargo to Uzum and Yandex Market sellers: https://gsrlogistics.uz/xizmatlar/bojxona/ and https://gsrlogistics.uz/qollanma/xitoydan-yuk-olib-kelish/
- Some of these pages contain **legal claims I could not confirm or that are outdated**. For example, "without an origin certificate the rate doubles" does not match BK 300¹ bands (+5 to +20 percentage points). Do not reuse their numbers.
- **Official usage signal:** the ed1 cabinet shows **94,720 total users**, and today's live counter was only **84 BYUDs from 00:00 to 03:36** (https://ed1.customs.uz/PersonCabinet/, live 18.11.2026). This says nothing about kargo share.

### Reading **[INFERENCE]**

- The likely first users of a *self-file* product are businesses that **already need a BYUD in their own name**: marketplace sellers needing proof of legal import, VAT payers wanting import-VAT credit, B2B resellers.
- Pure kargo users are a **different job**: Y4 is a comparison or migration screen for them, not self-filing.
- If interviews show most lead users are kargo-only, the MVP value shifts to Y1–Y8 (landed cost, go/no-go, "kargo vs white import") and Y18. The desktop filer becomes later.

### Interview plan (minimum)

- **Sample:** 12–15 small importers (Uzum and Yandex sellers, market traders, small LLCs and YaTTs).
- **Questions:**
  1. How did your last 3 shipments clear? Whose name was on the BYUD?
  2. Do you have an E-IMZO key, and have you logged into ed1 or ed2?
  3. Who signed?
  4. What did you pay per kg or per declaration, and what was included?
  5. Do you need a BYUD (for a marketplace, VAT, or the bank)?
  6. What went wrong last time (delay, rejection, fine)?
  7. Would you sign yourself if the tool filled everything?
- **Success threshold for keeping self-filing in the MVP:** ≥ 30 % already file in their own name or are required to. (This is a suggested threshold, not data.)

---

## 9. Lesson 1 fix (done)

`/workspace/bojxona/dars-01-import.md`, section 2.1 and open question 7, now say:
- under **BK 206 part 3** (from 03.05.2022), authorised persons (in practice the carrier) **must** send advance information **before arrival** for **road, rail and air**;
- they are responsible for its accuracy;
- the general "right" wording of art. 17 applies only to other cases.

Open question 7 is marked resolved; the remaining open point is the technical format and timing.

Backup of the previous version: `/workspace/bojxona/dars-01-import.md.bak-20261118`.

---

## 10. Sources

**Customs Code and procedure:**
- Customs Code: https://lex.uz/docs/2876354
  - arts. 29–31, 85, 206, 243, 248, 261, 262, 266, 271, 274, 277, 284, 290, 300¹, 301–305, 326, 327, 334, 349, 366, 369–372.
- VMQ 605 (cl. 2, 8, 11, 11¹, 15, 26, 30; Annex 1a): https://lex.uz/uz/docs/-3844549 and https://www.lex.uz/uz/docs/-7138545
- Yo'riqnoma 2773: https://lex.uz/uz/docs/-2924955
- VMQ 55: https://lex.uz/docs/7357270
- VMQ 847: https://lex.uz/docs/-7274716
- PQ-122: https://lex.uz/docs/-7452043

**Export:**
- VMQ 163 (fruit and vegetable export): https://lex.uz/uz/docs/-4213596
- VMQ 994 (origin certification): https://lex.uz/uz/docs/-4643161
- Plant Quarantine Law 113-I: https://www.lex.uz/uz/docs/-119173
- VMQ 727 (amends VMQ 65, phytosanitary certificates): https://lex.uz/uz/acts/-7208474
- Currency law (arts. 11, 11¹): https://www.lex.uz/docs/-4562834
- Tax Code arts. 260–261: https://lex.uz/docs/4674902

**Conformity assessment:**
- O'RQ-354: https://www.lex.uz/docs/-2248099
- VMQ 502: https://lex.uz/docs/-7080176
- O'RQ-820: https://www.lex.uz/uz/acts/-6392305
- VMQ 460: https://www.lex.uz/mact/-8452378

**Official services:**
- my.gov.uz service 207: https://my.gov.uz/uz/service/207
- ed1: https://ed1.customs.uz/PersonCabinet/
- ed2: https://ed2.customs.uz/
- MJtK: https://lex.uz/uz/docs/-97664

**Teammate sources, not re-read by me (UNVERIFIED here):** PQ-107 (minimum fruit and vegetable prices), VMQ 148 (vet), VMQ 283 (E-kontrakt).

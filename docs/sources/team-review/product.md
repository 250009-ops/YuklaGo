# YuklaGo design-v0.1 — product review (core features, sources, placeholders)

**Reviewer:** Product (team-review)  
**Date:** 18 November 2026, Asia/Tashkent (UTC+5)  
**Sources of truth:** `/workspace/hackathon/yuklago-spec-v2.md` (product rules). Design: `/workspace/hackathon/design-v0.1/yuklago-web-ui-v0.1.pdf` (28 pages) and `/workspace/hackathon/design-v0.1/design-rationale.md`. Raster crops of the same boards: `/workspace/hackathon/review/p-01.png` … `p-28.png`, plus `hi2-02.png`, `hi10-10.png`, `hi18-18.png`.  
**This folder was empty** when the audit started; this file is the product review.

**Rules used.** Never invent numbers, rates, deadlines, or legal references. Design-rationale line 4 already states that all figures, rates, codes, dates, and deadline lengths on the boards are **layout sample data**, and that spec v2 was not available to the designer. A “Rasmiy” chip on a sample number is **not** an official source. Line numbers for the PDF are from `pdftotext -layout` of each page (page 1 of the PDF = `yuklago-web-ui-v0.1.pdf` p.01).

**Experts who must fill placeholders**

| Expert | ID |
| --- | --- |
| Bojxona Deklarant Ustoz (deklarant workflow, documents) | `d098a0b5` |
| TIF TN va Bojxona To‘lovlari Mutaxassisi (classification, rates, payments) | `3d549ef3` |
| Bojxona Huquq va IT Integratsiya (regimes, deadlines, legal basis, e-gov integration) | `449f71e6` |

---

## (a) Core features in spec v2 checked against design-v0.1

Core = the 13 features without which, per spec v2, YuklaGo is not a complete self-filing product for the lead user.

**Rating:** **present** = a dedicated, usable screen (or clearly designed state) covers the feature’s required behaviour; **partial** = the idea is visible but a required rule, client, or state is missing or contradicted; **missing** = no board covers it.

| ID | Core feature | Rating | Where it appears (PDF page / review crop / rationale) | Notes |
| --- | --- | --- | --- | --- |
| Y1 | “Can I file this myself?” onboarding | present | p.06 (`review/p-06.png`) “2 · Yoʻlni tanlash” + “3 · Oʻzim topshira olamanmi?”; also the home warning on p.07 and ERI/cabinet status on p.27 Sozlamalar | Checks ERI token, cabinet access, and who signs (owner vs vakolatli mutaxassis). Does not issue ERI. Official issuer/address is still a placeholder. |
| Y3 | Pre-purchase landed cost | present | p.10–11 (`review/p-10.png`, `p-11.png`, highlight `hi10-10.png`); also a marketing sample on p.04 and a compact phone layout on p.28 | Structure matches v2 (goods, freight as ≈ taxmin, duty, VAT, fee, source/date chips, alternative-code effect, no guarantee). **The official numbers on the board are sample data** (see §b and §d). |
| Y7 | Pre-shipment go / no-go | present | p.12 (`review/p-12.png`) “Bu tovarni joʻnatsa boʻladimi?”; home blocker for YG-0415 and drone escalate on p.07 and p.12 | Red/green list, “do not ship yet,” broker path for a kvadrokopter. Permit source lists, control type, and certification organ remain placeholders. |
| Y9 | Document reading (OCR / LLM) | present | p.13 (`review/p-13.png`) Hujjatlar; phone capture on p.28 | “Biz oʻqiymiz — siz manba bilan solishtirasiz.” Invoice / shartnoma / CMR / packing list / sertifikat / ombor dalolatnomasi. Handwritten net weight is left unconfirmed — matches “errors must be visible and correctable.” |
| Y10 | TIF TN suggestion with official-list validation | present | p.14 (`review/p-14.png`) TIF TN kodi | Suggestion + reason + alternatives + “not a binding classification” + user confirm + reject-if-not-on-list empty state. Official name text is a placeholder. Duty effect of the alternative code is sample data. |
| Y11 | Deterministic payment engine | partial | Breakdown on p.10 and again on p.15 “Bojxona toʻlovlari (47-grafa)”; missing-rate state on p.15 (“Stavka topilmadi… Taxmin qilmaymiz… kabinetni toʻldirish ochilmaydi”) | The **behaviour** (tables not LLM; refuse if missing; source/date chips) is designed. The **data** is not: fee **310,000** soʻm is labelled Rasmiy while `[asos]` is empty, and v2’s only stated band example is 1 BHM = 440,000 UZS. Duty 10% / 15% is not in v2. See gap G1. |
| Y12 | Declaration draft | partial | p.15 draft table “Deklaratsiya qoralamasi · 48 maydon”; PDF-qoralama link; fill-session field map on p.17 | A reviewable draft exists, but it is a **sample 48-field / IM 40** extract, not a v2-specified official form. Unsupported-regime handling is only implied via Y18, not shown as a draft-blocked state for an unsupported regime. See gap G2. |
| Y13 | Review screen (“customs eye”) | present | p.15–16 (`review/p-15.png`, `p-16.png`) “Toʻlovlar va qoralama tekshiruvi” | Blocker (38-grafa net weight unconfirmed) and warning (2-grafa name mismatch). Cabinet fill stays disabled until blockers are cleared and the responsibility statement is ticked. Matches Y13 and the Y16 gate. |
| Y14 | Desktop embedded-cabinet fill | partial | p.17–22 (`review/p-17.png`…`p-22.png`); rationale §4. Real cabinet labelled “Hozircha yoqilmagan” and “needs YuklaGo Desktop.” | The viewport + rail pattern is designed and is described as client-agnostic (desktop would embed the browser). The **desktop app chrome itself is not a separate board**. Real-cabinet automation is correctly disabled pending the legal question. See gap G3. |
| Y15 | Visible, pausable, logged actions | present | p.19 running, p.20 paused, p.22 failed; session record on p.23; speed modes and pause (including Space and click-in-cabinet) on p.17 | Visible fill, pause, take over (“Oʻzim yozaman”), log without secrets. Speed modes (Qadam-baqadam / Oddiy / Tez, including a 3-second section pause) are a design addition not specified in v2; they do not contradict it. |
| Y16 | Stop at ERI; secrets stay on the device | present | p.17 steps 2 and 5; p.21 “Endi sizning navbatingiz”; p.27 “Bu yerda kalit, parol yoki sertifikat yuklash joyi yoʻq”; landing/login copy on p.05 | Stops at login and sign; no password field in YuklaGo; fraud warning; mock sign is clearly the cabinet’s dialog. Aligns with v2. |
| Y17 | Mock customs portal | present | p.17 choice “Mashq portali”; p.18 start strip (`hi18-18.png`); p.19–22 MASHQ frame (magenta hatch, MASHQ pill, mashq.yuklago.uz, UZ/RU watermark, header band) | Visually distinct from ed2.customs.uz. Rationale and p.17 also offer a web **copy-assist** mode, which v2 does not name; it is a reasonable web substitute and is not the same as driving the real cabinet. |
| Y18 | Escalate to a broker | present | Persistent “Brokerga topshirish” in the shipment header (component p.02 / `hi2-02.png`); full handoff on p.26; drone example on p.07 and p.12 | Framed as a normal option, pack preserved. XML is not offered, which matches Y18 / Y24 (XML only after a real sample is validated). |

**Core summary:** present 10, partial 3 (Y11, Y12, Y14), missing 0.

Non-core but designed (for context, not in the count above): Y2 path choice (p.06), Y4 kargo comparison (p.10–11), Y5 preference entitlement (p.11), Y6 E-kontrakt / bank (p.11, placeholders), Y8 deadline clocks (p.07, p.09 — sources still placeholder; storage `[N]`), Y19 reply-explainer (p.24), Y20 library and rate-change (p.25, rates `[x]` / `[y]`), Y21 export only as a new-shipment option / list row / library card (not a full path). **Not designed:** Y22 later regimes, Y23 audit of past declarations, Y24 official XML, Y25 1C/accounting, Y26 corridor / LC packs.

---

## (b) Every screen — real rule / data source, or “none”

“None” means the board has no official instrument, article, or dated official table behind the legal or money values it shows (or those values are acknowledged placeholders / layout samples). Brand and interaction-only boards are marked “none (UI only).”

| PDF page | Review crop | Screen / board | Rule or data source |
| --- | --- | --- | --- |
| 01 | `p-01.png` | Design system — “Calm ledger, not a cockpit” | none (UI only). Example chips and “48 maydon” are sample. |
| 02 | `p-02.png`, `hi2-02.png` | Shared component: shipment header | **none** for `Saqlash: [N] kun`. `Deklaratsiya: 9 kun · 27.11` is layout sample; v2 already has Art. 261 / 605 clause 11 (15 calendar days) but the board does not cite it. |
| 03 | `p-03.png` | Shared component: shipment stage rail | none (IA only). Stage labels follow the brief / v2 journey, not a legal article. |
| 04 | `p-04.png` | Landing — “Qanday ishlaydi” + sample landed cost | **none** for the money sample (duty 5 480 000, VAT 7 233 600, etc.). Product limits in the copy (user signs, no official partnership) match v2 wording, not a numbered act on the board. |
| 05 | `p-05.png` | Landing continued — broker option + YuklaGo account login | none (UI / trust copy). SMS login is for the YuklaGo account, not ERI — consistent with v2, no legal table. |
| 06 | `p-06.png` | Path choice + “Oʻzim topshira olamanmi?” | **none until filled.** Placeholders: `[v2 spec, “Yoʻl tanlash” boʻlimi]`, `[ERI beruvchi markaz va manzil — v2 spec]`, `[shartlar — v2 spec]` (authorised specialist). v2 requires official sources and forbids inventing office addresses or fees. |
| 07 | `p-07.png` | Home — “Bosh sahifa,” deadlines first | **none on the board.** `Manba: [qonun moddasi]`; `Muddat uzunligi… [v2 spec, “Muddatlar”]`; a `[N]` slot. v2 already contains the filing and storage clocks, but they are not wired here. |
| 08 | `p-08.png` | New shipment — “Yangi yuk” | **none until filled.** Export extra steps point at `[v2 spec, “Eksport”]`. |
| 09 | `p-09.png` | Shipment hub — “Umumiy holat” / muddatlar | **none on the board.** `[Muddat uzunligi va qonun moddasi — v2 spec’dan]`, `[oqibatlar — v2 spec]`, `[Saqlash muddati — v2 spec]`, `[N]`, `[sana]`. Reminder cadence “5, 2 va 1 kun” + “SMS va Telegram” is **not in v2**. |
| 10 | `p-10.png`, `hi10-10.png` | Kelib tushgan narx (landed cost) | **none that can be used as official.** Chips say “Rasmiy” / “MB” but placeholders remain (`[Rasmiy hujjat nomi]`, `[Rasmiy manba]`). Duty **10%**, fee **310,000**, FX 1 754,51 and (on p.11) 12 650 soʻm/$ are **layout samples**. VAT **12%** is a rate v2 sources to Tax Code Art. 258, but the board does not print that citation. Kargo rates are correctly user-entered (none invented). |
| 11 | `p-11.png` | Landed-cost continuation: kargo result, imtiyoz, shartnoma va bank | **none until filled.** `[kelishuv nomi]`, `[x] %`, `[y] %`, `[shakl nomi]`, `[shartlar — v2 spec]` (E-kontrakt), `[v2 spec, “Bank”]`. “No routing advice” matches v2 Y5 as a product rule. |
| 12 | `p-12.png` | Go / no-go — “Bu tovarni joʻnatsa boʻladimi?” | **none until filled.** `[v2 spec, “Ruxsatnomalar manbalari”]`, `[ruxsat turi — v2 spec]`, `[organ va tartib — v2 spec]`. |
| 13 | `p-13.png` | Hujjatlar (upload and check) | none as a legal table. Document types are consistent with v2 journey (invoice, contract, CMR, packing list, certificates). v2’s official list (605 clause 11-1, Annex 1a) is not quoted on the board. |
| 14 | `p-14.png` | TIF TN kodi | **none until filled** for the official name: `[TIF TN roʻyxatidagi matn — “yorugʻlik diodli (LED) lampalar”]`. Code **8539 52 000 0** and alternative **9405 42 xxx x** / **15%** are sample until the tariff specialist validates them against PQ-181 / NOTARIF. The “must exist on the official list” behaviour matches Y10. |
| 15 | `p-15.png` | Toʻlovlar va qoralama tekshiruvi | **none that can be used as official** for money lines. `[asos]` under the 310,000 fee. “Rasmiy · 01.11.2026” chips sit on sample duty / VAT / fee. Declaration type **IM 40** and “48 maydon” are not in v2. The missing-rate refusal state matches Y11. |
| 16 | `p-16.png` | Review footer / gate (fill disabled) | none (interaction). Gate rule matches Y13 / Y16 (no fill while a blocker remains and the responsibility tick is off). |
| 17 | `p-17.png` | Kabinetni toʻldirish — start, mock vs real vs copy-assist | none (product / legal-limit copy). Real cabinet “huquqiy masalasi hal qilinmoqda” matches v2 §9.1. “48 maydon” count is still sample. |
| 18 | `p-18.png`, `hi18-18.png` | Mock session start strip | none (UI only). |
| 19 | `p-19.png` | Automation — running (MASHQ) | none (UI / mock). 28/48 fields is sample. |
| 20 | `p-20.png` | Automation — paused / user interrupted | none (UI / mock). |
| 21 | `p-21.png` | Automation — ERI hand-off (“Endi sizning navbatingiz”) | none (UI / legal-limit copy, consistent with Y16). |
| 22 | `p-22.png` | Automation — failed (field not found) | none (UI). Fail-closed copy matches v2 (“fail visibly when a field cannot be found”). |
| 23 | `p-23.png` | Session record after mock session | none (audit log). Correctly states secrets are not recorded. Header still has `Saqlash: [N] kun`. |
| 24 | `p-24.png` | Topshirilgandan keyin + reply-explainer | none for the example rejection text (it is a demo message, and the board correctly says this is not a live official feed and not an official answer). Matches Y19. Header `[N]` remains. |
| 25 | `p-25.png` | Mahsulotlar kutubxonasi | **none until filled** for the rate-change example: `Avvalgi hisob: boj [x] %. Yangi: [y] %.` Codes with `xx` masks are samples. Behaviour (needs re-confirm before reuse) matches Y20. |
| 26 | `p-26.png` | Brokerga topshirish | none (handoff UX). Matches Y18 (PDF / structured pack, not XML). Header `[N]` remains. |
| 27 | `p-27.png` | Sozlamalar — ERI va kabinet, no key upload | none (security UX). Matches Y16. |
| 28 | `p-28.png` | Phone layouts (home, compact landed cost, capture, automation-not-on-phone) | **none** for compact money / deadline samples. Automation replaced by a status / “send to computer” message, which matches v2 (signing stays on a device that can hold the token). |

---

## (c) Every `[v2 spec]`, `[N]`, `[manba]` placeholder

**About `[manba]`.** `design-rationale.md:4` says bracketed text like `[manba]` / `[v2 spec]` marks a value spec v2 must supply. The **literal token `[manba]` does not appear** in the PDF text. Closest tokens are `[Rasmiy manba]`, `[Rasmiy hujjat nomi]`, `[qonun moddasi]`, and `[asos]`. Those are listed below. The instructional phrase `[ the site renders as itself ]` on p.01 line 110 is a design note, not a v2 fill-in, and is omitted from the expert queue.

Multiline tokens were reconstructed where a `[` opens on one line and closes on the next. Repeated header `Saqlash: [N] kun` is listed at every occurrence, but it is **one** expert question.

### Bojxona Huquq va IT Integratsiya (`449f71e6`)

| Placeholder | Quote (collapsed spaces) | File:line | What to fill |
| --- | --- | --- | --- |
| `[v2 spec, “Yoʻl tanlash” boʻlimi]` | “Kamida bittasiga “ha” — odatda tijorat yuki. Qatʼiy qoidalar: [v2 spec, “Yoʻl tanlash” boʻlimi].” | `design-v0.1/yuklago-web-ui-v0.1.pdf` p.06 line 31 | Legal tests for personal parcel / passenger / commercial BYD, including whether a non-entrepreneur can import commercially. |
| `[ERI beruvchi markaz va manzil — v2 spec]` | “ERI ni rasmiy markazdan olasiz: [ERI beruvchi markaz va manzil — v2 spec].” | same PDF p.06 line 50 | Official ERI issuer name and address only. v2 forbids inventing office addresses or fees. |
| `[qonun moddasi]` | “Manba: [qonun moddasi]” | same PDF p.07 line 20 | Legal source for the import-declaration clock shown on home. v2 already names Art. 261 and Resolution No. 605 clause 11 — confirm current text and wire the citation; do not invent a different period. |
| `[v2 spec, “Muddatlar”]` | “Muddat uzunligi faqat rasmiy manbadan olinadi: [v2 spec, “Muddatlar”].” | same PDF p.07 line 31 | Same clocks family (Y8). Confirm which clocks may appear on home and with which articles. |
| `[Muddat uzunligi va qonun moddasi — v2 spec’dan]` | “Rasmiy manba    [Muddat uzunligi va qonun moddasi — v2 spec’dan]. Muddat oʻtsa: [oqibatlar — v2 spec].” | same PDF p.09 line 35 | Length + article for the filing clock on the shipment hub. |
| `[oqibatlar — v2 spec]` | same sentence as the previous row | same PDF p.09 line 35 | Legal consequence of missing that deadline. |
| `[N]` and `[sana]` (storage clock) | Header: “Saqlash: [N] kun”; body: “[N] kun qoldi · tugaydi [sana]”; “Rasmiy manba    [Saqlash muddati — v2 spec].” | Header `[N]`: p.02 line 5; p.09 line 5; p.10 line 5; p.12 line 5; p.13 line 5; p.14 line 5; p.15 line 5; p.17 line 5; p.23 line 5; p.24 line 5; p.26 line 5. Body: p.09 line 38 (`[N]`, `[sana]`); p.09 line 42 (`[Saqlash muddati — v2 spec]`). Also a `[N]` in a deadline slot on p.07 line 26 (“Joʻnatishdan oldin: muvofiqlik sertifikati yoʻq … [N]”) — confirm whether this is the storage clock misaligned, or a non-statutory lead time (if the latter, leave blank: v2 Y7 says do not invent lead times). | v2 already states temporary storage generally up to 60 days, 10 days for perishables (Art. 85). Confirm current text, when the clock starts, and the end-date rule. Do not invent warehouse fees (the board already refuses to guess those). |
| `[shartlar — v2 spec]` (E-kontrakt) | “Qachon talab qilinadi: [shartlar — v2 spec]. Siz “roʻyxatdan oʻtgan” deb belgiladingiz, 01.10.” | same PDF p.11 line 36 | When E-kontrakt registration is required. v2 marks mandatory scope [UNVERIFIED]. |
| `[v2 spec, “Bank”]` | “Bank soʻraydigan hujjatlar va muddatlar: [v2 spec, “Bank”]. Biz muddatlarni oʻzimizdan qoʻshmaymiz.” | same PDF p.11 line 41 | Bank / currency-proceeds documents and deadlines, from current lex.uz only. |

### Bojxona Deklarant Ustoz (`d098a0b5`)

| Placeholder | Quote | File:line | What to fill |
| --- | --- | --- | --- |
| `[shartlar — v2 spec]` (vakolatli mutaxassis) | “Boshqa shaxs imzolasa, u bojxonada vakolatli mutaxassis sifatida roʻyxatdan oʻtgan boʻlishi kerak: [shartlar — v2 spec].” (split across two lines) | same PDF p.06 lines 70–71 | How an authorised specialist is registered in the TIF participant cabinet, and what the user must have before someone else may sign. Legal basis should be checked with `449f71e6`. |
| `[v2 spec, “Eksport”]` | “Eksport tanlansa: kelib chiqish sertifikati, fitosanitar talablar va valyuta tushumi bosqichlari qoʻshiladi. Qoidalar — [v2 spec, “Eksport”].” (split: p.08 lines 31–32) | same PDF p.08 lines 31–32 | Export-side steps and documents for the new-shipment path. Currency-proceeds and 0% VAT conditions also need `449f71e6`; GSP+ only if an official export list supports it (Y21). |
| `[organ va tartib — v2 spec]` | “Yoʻq boʻlsa — Oʻzbekistonda sertifikatlash: [organ va tartib — v2 spec].” (split: p.12 lines 73–74) | same PDF p.12 lines 73–74 | Official organ and procedure when a muvofiqlik sertifikati is missing. Do not invent lead times. |

### TIF TN va Bojxona To‘lovlari Mutaxassisi (`3d549ef3`)

| Placeholder | Quote | File:line | What to fill |
| --- | --- | --- | --- |
| `[Rasmiy hujjat nomi]` | “Tovar qiymati … 48 600 000 … [Rasmiy hujjat nomi] · tahrir 01.11.2026 ·” (layout also ties this column to the 8539 52 row) | same PDF p.10 line 32 | Official instrument name and edition for the tariff / conversion source actually used. If no official row is ready, do not leave a “Rasmiy” chip on sample numbers. |
| `[Rasmiy manba]` | “Transport Shenzhen → Toshkent … ≈ 6 200 000 … [Rasmiy manba] · 01.11.2026” | same PDF p.10 line 40 | Freight is an estimate in v2; a “Rasmiy manba” on an estimate is the wrong chip. Supply a real official source only for official lines (duty, VAT, fee, dated CBU rate). |
| `[kelishuv nomi]`, `[x]`, `[y]`, `[shakl nomi]` | “Kelib chiqishi Turkiya: tovar [kelishuv nomi] boʻyicha imtiyozga mos koʻrinadi” / “Boj [x] % oʻrniga [y] % boʻlishi mumkin — agar yetkazib beruvchi kelib chiqish sertifikati ([shakl nomi]) bersa.” | same PDF p.11 lines 22–23 | Only if the goods **already** qualify. Do not invent a routing-style example. If no official entitlement exists for the Turkey example, keep the “imtiyoz topilmadi” state and do not fill rates. |
| `[x]`, `[y]` (library) | “Avvalgi hisob: boj [x] %. / Yangi: [y] %.” | same PDF p.25 lines 30–31 | Dated official duty before/after for a saved code, or remove the worked rate-change example from the demo. |
| `[v2 spec, “Ruxsatnomalar manbalari”]` | ““Topilmadi” — biz tekshirgan rasmiy roʻyxatlarda yoʻq degani. Roʻyxatlar: [v2 spec, “Ruxsatnomalar manbalari”].” | same PDF p.12 line 54 | Official permit and Asl Belgisi list sources to load, with edition dates. |
| `[ruxsat turi — v2 spec]` | “Tovar nazoratda: [ruxsat turi — v2 spec].” | same PDF p.12 line 66 | Control / permit type for the kvadrokopter (dron) example, or change the example to a goods group that is confirmed. |
| `[TIF TN roʻyxatidagi matn — “yorugʻlik diodli (LED) lampalar”]` | “Rasmiy nomi: [TIF TN roʻyxatidagi matn — “yorugʻlik diodli (LED) lampalar”]” | same PDF p.14 line 27 | Official nomenclature text for the confirmed code, from the dated official list. The words in quotes are a designer hint, not an official name. |
| `[asos]` | “Rasmiylashtirish yigʻimi … — … [asos] … Rasmiy · 01.11.2026 … 310 000” | same PDF p.15 line 47 | Legal basis for the processing fee, from current Resolution No. 55. **Do not keep 310,000 as if it were official** until this specialist signs the band and the BHM amount. v2’s only stated example is 1 BHM = 440,000 UZS for the “up to 10,000” USD band, using a value inside the band (e.g. 9,500 USD). |

### Rationale (class of placeholders, not extra tokens)

| Quote | File:line | Owner |
| --- | --- | --- |
| “Bracketed text like [manba] / [v2 spec] marks a value Product Spec v2 must supply.” | `design-v0.1/design-rationale.md:4` | All three experts, as assigned above |
| “Fill every [v2 spec] placeholder: deadline lengths and articles, the ERI issuer, E-kontrakt conditions, permit source lists, export steps.” | `design-v0.1/design-rationale.md:69` | Deadlines / ERI / E-kontrakt → `449f71e6`; permit lists → `3d549ef3`; export steps → `d098a0b5` (with `449f71e6` on legal conditions) |

**Placeholder counts (unique questions, not header repeats):** Huquq `449f71e6` **9** (path choice; ERI issuer; home filing-clock article; muddatlar list; hub length + article; consequences of missing a deadline; storage length / end date, including all header `[N]` repeats; E-kontrakt conditions; bank documents and deadlines). TIF TN `3d549ef3` **8** (official document name; official source chip; Turkey preference example as one quartet; library `[x]` / `[y]`; permit lists; control type; official TIF TN name; fee basis). Deklarant `d098a0b5` **3** (authorised specialist conditions; export steps; certification organ / procedure). Total unique questions: **20**.

Occurrence count of the `[N]` token in the PDF extract: **13** (11 header repeats + p.07 line 26 + p.09 line 38). `[x]` / `[y]`: 2 pages each (p.11 and p.25).

---

## (d) Core-feature gap list, with testable acceptance criteria

No numbers are invented below. Where v2 already states a figure, the criterion points at that figure and requires the current lex.uz text to be re-checked before the UI is labelled “Rasmiy.”

### G1 — Y11: official payment lines are still sample data wearing “Rasmiy” chips (partial)

**Gap.** Landed cost (p.10) and review (p.15) show duty 10%, alternative 15%, fee 310,000 soʻm, and CBU-lookalike FX as if official, while `[asos]`, `[Rasmiy hujjat nomi]`, and `[Rasmiy manba]` are empty. v2 Y11: if a rate is missing, the engine refuses; every official number carries source, URL where known, and as-of date. v2 also forbids a 10,000 USD boundary example and offers 9,500 USD → 1 BHM only as an *inside-band* illustration (1 BHM = 440,000 UZS from PF-115, as written in v2).

**Acceptance criteria**

- Given a demo shipment whose duty, excise, VAT, or Resolution No. 55 fee row has not been signed off by `3d549ef3` with an official source and as-of date, the UI shows “—” / “Stavka topilmadi” / “Tasdiqlanmagan” and **does not** place a “Rasmiy” chip or a soum amount on that line.
- Given a signed-off official row, the on-screen amount, source name, URL (if known), and as-of date match that row exactly, and a second run with the same inputs and the same rule-set version produces the same output (v2 §8.3).
- The processing-fee line is either hidden/refused or computed from the current Resolution No. 55 text this specialist cites; the sample **310,000** does not appear in a demo or pitch as an official fee.
- The language model is not invoked to compute, round, or invent any of those amounts (unit or pipeline test).
- VAT 12% is shown as official only with Tax Code Article 258 (or the current lex.uz text the legal role confirms) as the source; the base composition is the one the payments specialist confirms, not a remembered formula.

### G2 — Y12: no practitioner-approved declaration draft (partial)

**Gap.** The only draft is a sample “48 maydon” table with typ **IM 40** and a short grafa list. v2 does not define a 48-field form or IM 40. Unsupported regimes must not receive a half-empty draft (they go to Y18).

**Acceptance criteria**

- Given a Phase 1 import (or export) pack the user has confirmed, the draft contains every field `d098a0b5` has signed off as the minimum review set for that regime, each with a source chip, and no field count or regime code that this expert has not approved (including “48 maydon” and “IM 40” until approved).
- Given a regime that is not in the supported Phase 1 set, the product does not open a half-empty draft; it explains the regime in plain Uzbek and offers Y18 (v2 §3 and Y12).
- XML is not produced until Y24’s “real accepted sample” condition is met.

### G3 — Y14: real-cabinet path and desktop client are designed in pattern only (partial)

**Gap.** Web mock + copy-assist are designed; real ed2 automation is correctly disabled; there is no separate desktop-app board. v2: the desktop app is the only client that drives a customs cabinet; public demos use the mock until `449f71e6` answers the legal question.

**Acceptance criteria**

- In any public or recorded demo, the cabinet frame is the mock (MASHQ marks visible on both halves of a screenshot) and the real-cabinet option stays disabled or behind an explicit “not enabled — legal question pending” state.
- Real-cabinet automation cannot be turned on without an approval recorded by `449f71e6`.
- When real-cabinet mode is eventually enabled, it runs only in the desktop app, on a machine the user controls, in a visible embedded browser, and it stops at ERI login and at sign (already designed on p.17 and p.21).
- If a cabinet field cannot be mapped, the session fails closed, nothing is submitted, and the unsigned state is stated plainly (already designed on p.22).

### G4 — Y1: official setup facts are still placeholders (present screen, blocked content)

**Gap.** Onboarding exists, but the ERI issuer/address and authorised-specialist conditions are empty. v2: use official sources; do not invent office addresses or fees; YuklaGo does not issue ERI.

**Acceptance criteria**

- The onboarding screen names an ERI issuer and address only if `449f71e6` has supplied them from an official page; otherwise the screen links to an official landing page without inventing a street address or a fee.
- Conditions under which a vakolatli mutaxassis may sign are the wording signed off by `d098a0b5` / `449f71e6`. No YuklaGo-issued ERI is offered.

### G5 — Y7: go / no-go lists have no official source loaded (present screen, blocked content)

**Gap.** The red/green list is designed, but list sources, control type, and certification organ are placeholders. v2: maintain official lists; do not invent lead times; controlled goods beyond the supported set → Y18.

**Acceptance criteria**

- For a supported demo code, every permit / certificate / Asl Belgisi row is either “required” or “not required” according to official lists `3d549ef3` has dated, with the list name visible, or the row is “topilmadi” / escalate — never a guessed lead time.
- A goods item marked controlled beyond the supported set (the drone example, once `[ruxsat turi]` is confirmed, or another confirmed example) cannot continue to self-file; Y18 is the next step.

### G6 — Y8 clocks on the hub / home: v2 already has the rules, the boards do not (adjacent to Core, blocks trust on every Core screen)

**Gap.** Almost every shipment screen carries `Saqlash: [N] kun`, and the filing-clock legal source is still a placeholder, even though v2 already states Art. 261 / 605 clause 11 (15 calendar days) and Art. 85 (generally 60 days, 10 days for perishables). Reminder copy invents “5, 2 va 1 kun” and “Telegram,” which v2 does not specify (reminders are web and mobile; no Telegram bot).

**Acceptance criteria**

- The persistent header and the hub clock show a filing deadline only with the length and article `449f71e6` confirms from current lex.uz (v2’s starting point is 15 calendar days, Art. 261 and 605 clause 11).
- The storage clock is filled from the confirmed Art. 85 rule (including the perishable variant when that fact is known) or stays “—” if the start date or the goods class is unknown — never a blank `[N]` next to a “Rasmiy manba” label.
- Reminder channels and cadences that are not in v2 (Telegram; 5 / 2 / 1 days) are removed until a product decision and a legal check are recorded.
- Consequences of a missed deadline (`[oqibatlar]`) are shown only in the wording `449f71e6` signs off; otherwise the clock shows the date without inventing a penalty.

### G7 — Proof point for the whole Core payment + code path is still outstanding

**Gap.** v2 §1: “Proof point to seek (not yet in hand). Reproduce the payments of one real, accepted, redacted declaration exactly, to the soum, with source and date on every line.” Without this, Y10 + Y11 + Y13 cannot be demonstrated as evidential.

**Acceptance criteria**

- Before a public calculation is presented as “verified,” the team has a redacted accepted declaration (or a dated official NOTARIF screenshot next to the same calculation, the allowed second-best in v2) whose duty, excise (or “not applicable” with the named act), VAT, and Resolution No. 55 fee the engine reproduces to the soum, each line carrying source and date.
- That gold case is the only “verified” example in the demo. All other codes stay “sample” or “stavka topilmadi.”

### G8 — Formal acceptance criteria are missing in spec v2 itself

**Gap.** None of the 13 Core features has a written AC section in the spec (audit rating: all partial or, for later non-core IDs, no). This review’s G1–G7 are the minimum testable bar for the demo; they do not replace a specialist-signed AC sheet.

**Acceptance criteria**

- A short AC sheet exists for Y1, Y3, Y7, Y9, Y10, Y11, Y12, Y13, Y14, Y15, Y16, Y17, and Y18, signed by the owning expert(s), containing only sourced figures or an explicit “refuse / don’t show” rule — no remembered rates.

---

## Counts for the report-back

- Core features vs design: **13** checked — **present 10, partial 3, missing 0**.
- Screens / boards inventoried: **28** PDF pages (24 design boards in the rationale, with some journeys split across pages and four component / phone / strip pages).
- Unique placeholder questions to fill: **Huquq `449f71e6` — 9; Deklarant `d098a0b5` — 3; TIF TN `3d549ef3` — 8.** Header `[N]` repeats are one storage question, not 13 questions.
- Core gaps with AC: **8** (G1–G8).

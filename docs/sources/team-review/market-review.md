# YuklaGo market size — pitch-jury review

**Reviewed:** `/workspace/hackathon/market/market-size.md` (draft dated 19 November 2026, Tashkent time; also `market-size.pdf`, `model.py`).  
**This review written:** 19 November 2026, Tashkent time (UTC+5).  
**Not legal advice.** No figure below is invented. If a number was not found in a source that was actually opened, it is marked **topilmadi**. Quotes are from pages or official PDFs opened this turn.

Independent evidence was gathered first, then the draft was opened and each cited URL was checked where the page could be retrieved as text or PDF.

---

## 1. Verdict

The draft is serious work: it labels **[SOURCED] / [DERIVED] / [ASSUMPTION]**, the main official trade totals check out, and most of the arithmetic on its own inputs is correct. A jury should still not put the headline **1.36 trillion so'm / $114 M TAM** or the year-3 **5.0 bn so'm / $420 k SOM** on a slide as measured facts.

The biggest source problem is that the draft never uses the later, fuller Customs figure for **2025 cargo declarations (1 million 153 thousand)**, and the “**>1 500 customs brokers**” claim (F9) sits on a JavaScript customs.uz page whose article body could not be extracted and confirmed here. The biggest number problem is valuing **every** declaration at a **1 200 000 so'm** outside-broker fee, while cheaper Prom.uz listings exist, the in-house vs broker vs kargo split is unknown, and the pitch line “small firms account for about a third” does not match the draft’s own ~48 % maths. SME **value** share is not YuklaGo’s customer count. Recommended SOM framing: a **scenario identity**, not a single forecast.

---

## 2. Independent evidence (opened this turn)

FX used only when converting the draft: **1 USD = 11 980.36 so'm** on 19.11.2026. CBU JSON: `https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/2026-11-19/` — `"Rate":"11980.36"`, `"Date":"19.11.2026"`. This matches the draft’s rate.

### 2.1 Foreign-trade participants / importers

| Item | Figure | Source, date | Exact quote / note |
|---|---|---|---|
| Participants, exporters, importers, 2024 | **~34.9 thousand** participants; **7.8 thousand** exporters; **27.1 thousand** importers of goods and services | Official bulletin *Tashqi iqtisodiy faoliyat*, Jan–Dec 2024, downloaded from stat.uz dropfiles (Uzbek file opened). Same figures in the Russian file. | «2024 yilning yanvar-dekabr oylarida O‘zbekiston Respublikasi tashqi savdo aylanmasi ishtirokchilari soni qariyb 34,9 mingtaga yetdi (… 805 taga kamaydi). Shundan eksportyorlar soni 7,8 mingta (…) ni tashkil etgan bo‘lsa, 27,1 ming (…) importyorlar tomonidan tovar va xizmatlar import qilindi.» |
| Importers in Tashkent city, 2024 | **45.2 %** of importers | Same bulletin | «eng ko‘p importyorlar Toshkent shahriga to‘g‘ri kelgan bo‘lsa (jamiga nisbatan 45,2 %)» |
| Participants, 2025 | **topilmadi** | 2025 year-end FTT press release (stat.uz, 21.01.2026 PDF) was opened; it has turnover, not a 2025 headcount. | A 2025 participant count would belong in the same annual FEA bulletin on stat.uz / siat.stat.uz, once published. |
| “14 mingga yaqin TIF qatnashchilari” who received benefits in 2025 | **~14 thousand** — this is **not** the total participant count | Daryo, 30.12.2025, citing Customs: https://daryo.uz/2025/12/30/ozbekistonda-bir-yillik-bojxona-tushumlari-miqdori-malum-qilindi/ | «14 mingga yaqin tashqi iqtisodiy faoliyat qatnashchilariga … imtiyoz va preferensiyalar qo‘llangan.» |

### 2.2 Import declarations (BYD)

| Item | Figure | Source, date | Quote |
|---|---|---|---|
| Cargo declarations, Jan–Oct 2025 | **>946 thousand** (+12 %) | Kun.uz, 14.11.2025, Customs briefing: https://kun.uz/ru/news/2025/11/14/tamojyenniki-presekli-nezakonnyy-tovarooborot-pochti-na-1-trln-sumov | «За отчётный период было оформлено свыше 946 тыс. таможенных грузовых деклараций (+12%).» The piece is a 10-month report; one earlier sentence on vehicles is “январь–август” — a jury may ask, but the declarations line is in the 10-month framing. |
| Cargo declarations, full year 2025 | **1 million 153 thousand** | UZA, 25.08.2026, Customs press conference: https://uza.uz/oz/posts/inson-omilisiz-rasmiylashtirilgan-deklaratsiyalar-eksportda-42-foizni-importda-esa-13-foizni-tashkil-etgan_899924 | «2017-yilda 464 mingta deklaratsiya rasmiylashtirilgan bo‘lsa, 2025-yilda ushbu ko‘rsatkich 1 million 153 mingtaga yetgan.» **The draft does not use this number.** |
| Jan–Jul 2026, all declarations | **715 thousand** | Same UZA article, 25.08.2026 | «2026-yilning yetti oyida esa 715 mingta deklaratsiya rasmiylashtirilgan.» |
| Jan–Jul 2026, import / export | **397 thousand** import; **206 thousand** export | Same | «206 mingta eksport deklaratsiyasining 94 foizi, 397 mingta import deklaratsiyasining 87 foizi soddalashtirilgan tartibda rasmiylashtirilgan.» Here the grammar is unambiguous: 397k is the **import total**, not the simplified subset. |
| 2025 simplified counts | Export **301 thousand (94 %)**; import **581 thousand (88 %)** | Daryo, 30.12.2025 (link above) | «Eksportda 94 foiz, ya’ni 301 mingta, importda esa 88 foiz, 581 mingta deklaratsiya soddalashtirilgan tartibda rasmiylashtirildi.» The natural reading is that 301k **is** the 94 % (simplified), so total export ≈ 301k / 0.94 and total import ≈ 581k / 0.88. That is how the draft builds D1. It is reasonable, but not as clean as the 2026 UZA wording. A jury can ask for the Customs original. |
| Full-year 2025 import declarations as a single official total | **topilmadi** as a standalone Customs table | Would be in a Customs Committee yearbook / open-data GTD release, or a press release that states “import deklaratsiyalari soni” for the whole year, not only the simplified share. | The D1 figure (~660 k) is derived, not published as such. |
| Share of declarations filed by small / individual importers (by **count**) | **topilmadi** | SIAT publishes SME **value** shares, not declaration counts. | See §2.3. |

### 2.3 Small / individual importers (value, not count)

| Item | Figure | Source, date | Quote / caveat |
|---|---|---|---|
| SME share of imports of goods (works, services), 2025 | **53.6 %** (2024: **49.8 %**; 2026-Q2 YTD: **51.8 %**) | Official SIAT, updated 27.10.2026: https://siat.stat.uz/data/276/ | Table, Uzbekistan row: 2024 = 49.8, 2025 = 53.6, 2026-Q2 = 51.8. Methodology: SME import value ÷ total import value × 100. |
| SME import **value**, 2025 | **25 390.3 million USD** | Official SIAT: https://siat.stat.uz/data/430/ | 2025 = 25390.3. Check: 25 390.3 / 47 354.5 ≈ 53.6 %, consistent with 2025 total imports. |
| SME share of exports, 2025 | **36.6 %** (2024: **34.1 %**; 2026-Q2 YTD: **47.2 %**) | Official SIAT: https://siat.stat.uz/data/402/ | Table matches F5. Q2 2026 is year-to-date, not a new annual rate; Q1 was 49.6, Q3 YTD 47.0. Do not treat 47.2 % as the new SAM input. |
| “Kichik tadbirkorlik subyektlari” | Official statistical category (small-business entities: typically YaTT, microfirms and small enterprises under the statutory thresholds) | SIAT metadata on the same pages | **This is not** “Instagram/Telegram resellers” or “kargo users.” A small firm can import a production line. Using 53.6 % as YuklaGo’s SAM share is an assumption, not a persona match. |
| Share of **jismoniy shaxs** commercial importers, or of kargo users who never file a BYD | **topilmadi** | Would need Customs microdata (declarations by declarant type) or a survey / interviews. | |

### 2.4 Imports from China and Turkey (value)

These are **goods and services** in the official FTT country tables, not a consumer-goods subset.

| Period | China | Turkey | Total imports | Source |
|---|---|---|---|---|
| 2025, full year | **14 755.9 million USD** (31.2 %); news rounding **$14.8 bn** | **1 888.1 million USD** (4.0 %); news rounding **$1.9 bn** | **$47.4 bn** FTT imports, of which goods **42 083.9 million USD**, services **5 270.6 million USD** | Stat press release PDF, 21.01.2026: `/tmp/market-src/ftt-2025-uz.txt` from https://stat.uz/img/news/press-reliz-uzb_p58093.pdf (opened). Country news: https://stat.uz/en/press-center/news-of-committee/66797-zbekiston-importidagi-top-10-davlatlar-5 (11.02.2026): «China - 14.8 billion; … Turkey - 1.9 billion.» Quote from the PDF: «Tovarlar importi … 42 083,9 mln AQSH dollarini tashkil etdi. Xizmatlar importi esa 5 270,6 mln AQSH dollariga yetdi.» And: «Xitoy (31,2 %), … Turkiya (4,0 %).» |
| 2025 exports, for D3 | Exports **33 812.3**; services exports **9 760.4**; non-monetary gold **9 900.1** | | | Same PDF: «shu jumladan: nomonetar oltin 7 480,6  9 900,1»; «Xizmatlar 7 571,7  9 760,4». |
| Jan–Aug 2026 | China imports **11 194.6** million; Türkiye **1 241.6** | Total imports **34.5 bn** | | Stat EN press release: https://stat.uz/img/news/press_release_eng_p14832.pdf (opened). |

China’s 31.2 % includes a large machinery-and-transport block in the national import mix (the same 2025 release: machinery and transport equipment **33.8 %** of imports). That is **not** automatically YuklaGo’s 1688/clothing sweet spot.

### 2.5 Customs brokers (count)

| Item | Figure | Source | Note |
|---|---|---|---|
| National count of notified / operating brokers | **topilmadi (confirmed quote)** | Draft F9 cites https://customs.uz/news/bozhhona-qomitasi-raisining-birinchi-orinbosari-tadbirkorlar-bilan-ochiq-muloqot-otkazdi | The URL exists (HTTP 200). The page is a JavaScript shell; curl/WebFetch returned no article body, so the sentence «1 500 dan ortiq bojxona brokeri» was **not independently confirmed**. Do not put “1 500+” on a slide until someone pastes the visible paragraph and date. A licence.gov.uz extract or a Customs open register would be the proper official source. |
| Legal regime | Notification, not a licence | Consistent with O‘RQ-956 / team legal notes; draft cites https://www.lex.uz/uz/acts/-7093753 | Fine as legal background, not a headcount. |
| ATB members | Draft says **~102–120**. Not used here as a national total. | https://atb.uz/chleny-atb-2/reestr-atb/ | Association members are a **subset**. A raw HTML pattern count is not a clean official headcount. |

### 2.6 Broker / declarant fees (list prices, not an official tariff or an average)

There is **no official** “one declaration = X so'm” tariff. Team file `deklarant-jarayoni.md` already warned not to pitch Prom.uz ads as official.

| Listing | Price | Date on the page | URL | Note |
|---|---|---|---|---|
| BESTBROKER, Prom.uz | **412 000 so'mdan** | Updated **22.07.2026** | https://www.prom.uz/uz/ads/tamozenno-deklarirovanye-tovarov-dlya-importaeksporta/ | «412 000 so'mdan». An advertisement, bundle of services, not a measured average. **The draft omits this lower listing.** |
| GellionPrime, Prom.uz | **540 000 so'm** (page title) | Updated **20.03.2025** | https://www.prom.uz/uz/ads/deklarirovanie-gruzov-1/ | Older listing. |
| BROX / bbbx.uz | IM40/EK10: **880 000** (1–4 lines, 2 BHM), **1 320 000** (5–10), **1 760 000** (11–20), **2 200 000** (21–100); HS class. **440 000**; certificate **1 320 000** | Page shows 1 BHM = 440 000 so'm (so post-01.09.2026). Opened 19.11.2026. | https://bbbx.uz/ | Matches F10. The same page also shows a sample “total” **2 640 000** if classification + certificate are added. |
| UIA | IM40 / IM41 / IM42 / EK10 / EK11 / EK12: **5 BHM** (= **2 200 000** at current BHM); transit TR80 **3 BHM** | Opened 19.11.2026; no tariff-update date on the page. | https://uia.uz/ru/plans/tamozhenno-oformleniye-gruzov/ | Matches F11. |
| Import Eksport Broker, tovar.uz | IM-40 **1 236 000** UZS/unit | Price dated **10.06.2025** | https://tovar.uz/service/1342 | Matches F12, but the page also says **«Услуги больше нет в наличии»**. Stale and possibly pre-new-BHM. Do not treat as a current offer. |

**Typical fee:** topilmadi as a market average or official tariff. A pitch-safe statement is a **range of current list prices** (at least 412 000 “from”, then 880 000–2 200 000 on named broker sites), plus “actual invoices vary; we have not sampled regional or Telegram prices.”

### 2.7 Cargo per-kg, China → Tashkent (company listings, not official statistics)

Only published offer pages, with their own dates. These are **not** a national average. The draft has **no cargo section**; that is a gap for YuklaGo’s lead user.

| Firm | Rate | What is in the price | Date | URL |
|---|---|---|---|---|
| Door to Door (d2d.uz) | Avto **$5.5/kg from** (Tashkent and regions, 15–18 days); seriya/brend avto **$6.5/kg**; air **$9.49/kg from** (4–7 days) | Company FAQ on the homepage. Times from arrival at their China warehouse. | Page opened 19.11.2026 (no “updated on” stamp on the landing FAQ; a related blog on the same site uses CBU rates dated 26.09.2026). | https://d2d.uz/uz/ |
| GSR Logistics | Avto **consolidation billed in $/m³ from 110 $/m³**, not per kg, except density ≥ 1 000 kg/m³ at **0.55 $/kg**; air **from 9 $/kg**. Example: 300 kg / 1.2 m³ ≈ **216 $** (180 $/m³). Duty, VAT, insurance **extra**. Minimum **1 m³** for avto. | «Taxminiy narx · Yangilangan: 2026-yil 8-sentabr» | 8.09.2026 | https://gsrlogistics.uz/narxlar/ |

A single “typical $/kg” for all China→Tashkent cargo **topilmadi**. Light parcel kargo (d2d-style) and wholesale consolidation (m³ tables) are different products. Neither listing is a Customs or stat.uz figure.

### 2.8 Other draft facts checked

- **F1 ($81.2 / 33.8 / 47.4 bn, 2025):** confirmed on https://stat.uz/en/press-center/news-of-committee/66432-2025-jilda-zbekistonning-tash-i-savdo-ajlanmasi-81-mlrd-dollardan-oshdi-4 (22.01.2026) and the 21.01.2026 PDF (81 166.8 / 33 812.3 / 47 354.5 million USD).
- **F13 InCustoms 125 000 / 5×300 000:** not re-trialled this turn; consistent with team file `raqobatchilar.md` (17.11.2026, site copy). Still a website price, not a usage statistic.
- **F15 e-commerce 22.7 trn so'm, ~1.5×:** confirmed, UzDaily 21.02.2026 citing NAPP: https://www.uzdaily.uz/en/online-sales-in-uzbekistan-reach-227-trillion-soums-in-2025/. This does **not** say those sellers import directly.
- **F14 WTO “31 of 34 deals; join in 2027”:** the cited WTO page (1.11.2026), https://www.wto.org/english/news_e/news26_e/acc_01nov26_545_e.htm, was opened. It says most bilateral market-access talks are completed and “important work remained.” It does **not** state “31 of 34” or a 2027 accession date. Those numbers, if used, must come from the Daryo article (not re-opened as the carrier of that exact count) or be dropped from the slide.

---

## 3. Draft source and arithmetic check

### 3.1 What holds

- F1, F2 goods/services/gold, F3 (2024 headcount and 45.2 %), F4, F5 annual shares, F6’s “>946 k” and 6 % / 45 % auto-clearance, F10–F12 list prices (with the tovar.uz caveat), CBU FX, and the **internal arithmetic** of TAM / SAM / SOM **given the draft’s inputs**.
- Worked examples (base, 11 980.36 so'm/$):
  - D1: 581 000 / 0.88 + 301 000 / 0.94 ≈ **660 k + 320 k = 980 k**. Correct on that reading.
  - D2: 946 000 × 12/10 = **1.135 million**. Correct as a *mechanical* annualisation of a “greater than” 10-month figure, but superseded by the 1 153 000 full-year figure above.
  - D3: 42.08 + (33.81 − 9.76) = **66.13 bn**. Correct. Gold ~$9.9 bn is in the same PDF.
  - TAM base: 1.135 m × 1 200 000 = **1.362 trn so'm** ≈ **$114 M**. Correct.
  - SME decls: (660 k × 1.135/0.980) × 0.536 + (320 k × 1.135/0.980) × 0.366 ≈ **545 k**. Correct.
  - SAM decls: 545 k × 0.75 × 0.70 ≈ **286 k**. Correct.
  - SAM value: 286 k × 1 200 000 ≈ **343 bn** (draft 344 bn). Fine.
  - YuklaGo SAM: 286 k × 220 000 ≈ **63 bn**. Correct.
  - Year-3 decls: 286 k × 1.1³ × 6 % ≈ **22.8–22.9 k**. Correct if 10 % SAM growth and 6 % share are accepted.
  - Y3 revenue: 22.9 k × 220 000 ≈ **5.04 bn so'm** ≈ **$420 k**. Correct.
  - “Saved” 980 000 × 22.9 k ≈ **22.4 bn so'm**. Arithmetic only — not an observed saving.
  - 22.9 k / 14 ≈ **1 635** businesses. Arithmetic only.

### 3.2 What does not hold, or overreaches

1. **Pitch line vs table.** «Small firms account for about a **third** of that» is wrong on the draft’s own numbers: 545 k / 1 135 k ≈ **48 %**. «**80 %** of their filings are plain IM40/EK10» does not match the SAM table, which uses **75 %** and also excludes excise, licensed, vet/phyto and marked goods — not only the regime code.
2. **D2 should yield to 1 153 000.** Using 1.135 m understates 2025 volume slightly (~1.6 %). More important: a later Customs press figure exists and should replace the 10-month extrapolation.
3. **Fee of 1 200 000 as “typical / conservative.”** BBBX’s own 5–10 line tariff is **1 320 000**, not 1.2 m. Prom.uz shows **from 412 000** (July 2026) and 540 000. UIA is **2 200 000**. There is no evidence that 1.2 m is the mean, median, or SME mode. Calling it conservative is not supported once the cheaper ads are included.
4. **TAM assumes every declaration “costs market price,”** including in-house declarants and any filing bundled into a kargo invoice. The draft caveats this in §9.2; the headline $114 M does not.
5. **SME value share ≠ declaration count.** The draft flags this as an assumption and even says it is “probably conservative” because SMEs file smaller, more frequent shipments. That direction is **unknown**. SMEs might also file fewer formal BYDs if they use kargo. Either way, 53.6 % is a value share of **all** SME imports (including services and capital goods), not YuklaGo’s ICP.
6. **Stacked SAM filters (75 % × 70 %)** have no interview evidence (`research-pitch.md` still marks interviews as not collected). 70 % “PC + E-IMZO + willing to self-file” is doing a lot of work.
7. **SOM assumes live `ed2.customs.uz` automation from year 1** (§9.6). Spec v2 and the design itself say real-cabinet fill is an open legal question; the working demo is a practice portal. That is not a small caveat for a self-filing revenue model.
8. **F9 (1 500+ brokers) and F14 (31/34, join 2027)** are not confirmed from the official pages opened this turn (see §2.5 and §2.8).
9. **tovar.uz listing is marked unavailable** and is 17 months older than the pitch date.
10. **Top-down “agreement within ~15 %”** is partly circular: the 0.17 % intensity is back-solved from the same bottom-up TAM, then compared with a 0.20 % assumption that was chosen nearby.

---

## 4. Hardest jury questions (and honest answers)

**Q1. How many of the 1.1 million declarations actually pay an outside broker?**  
Honest answer: We do not know. Customs has not published the split between broker, in-house specialist, and owner-filed TED. Kargo users may never see a separate broker invoice. Our TAM is “if every declaration were valued at a published broker list price,” not observed spend.

**Q2. Why is 53.6 % of import *value* your customer share, and why does the slide say “about a third”?**  
Honest answer: 53.6 % is the official 2025 share of imports of goods, works and services by statutory small-business entities (SIAT). It is not the share of declaration counts, and it is not the share of 1688/Turkey resellers. Our own SAM maths give about **48 %** of declarations after we apply that value share as a proxy — the “third” line is a mistake and should be removed. The YuklaGo persona is a subset we have not yet measured.

**Q3. Can you file in the official cabinet today, and does the $420 k year-3 SOM assume a permission you do not have?**  
Honest answer: Today we can show a clearly marked practice cabinet and a manual copy-assist. Automatic filling of `ed2.customs.uz` is an open legal question. The $420 k path assumes that mode is on from year 1. If it is not, we are closer to a draft-and-checklist tool, and pricing would have to compete with InCustoms-style draft fees, not with a 1.2 million so'm broker invoice.

**Q4. Is 1.2 million so'm really the market fee?**  
Honest answer: It is a mid-point we chose among three named Tashkent lists (880 k–2.2 m). Other public ads start at 412 k so'm. There is no official tariff and no survey average. Regional and Telegram prices were not sampled.

**Q5. What do small importers actually pay today — kargo per kg, or a BYD + broker fee?**  
Honest answer: That is the open interview question. Public kargo *offers* (not averages) include about **$5.5/kg from** for auto parcels (d2d.uz, page read 19.11.2026) and consolidation from **110 $/m³** (GSR, 8.09.2026), with duty/VAT often extra. Until importers tell us which path they used on their last shipment, we should not fold kargo spend into broker TAM or assume they will switch to self-filing.

**Q6. Where is the 2025 foreign-trade participant count, and is 1 630 customers “5 % of 34.9 k” meaningful?**  
Honest answer: 34.9 k is **2024**. We did not find a 2025 headcount in the year-end FTT release. 1 630 / 34.9 k is only a sanity ratio on a stale denominator, and 14 declarations per firm is an assumption.

**Q7. China is 31 % of imports — is that your market?**  
Honest answer: 31.2 % (China) and 4.0 % (Turkey) are 2025 shares of **total** imports of goods and services, including machinery and transport equipment. We do not have a published count of small, repeat consumer-goods declarations on those routes.

**Q8. If year-3 revenue is only about $420 k in your own base case — or less in a conservative case — why is this a venture-scale opportunity?**  
Honest answer: That is a fair reading of our *base* SOM at 6 % of an already filtered SAM, at 220 k so'm per declaration. The $114 M TAM is not “our revenue.” The opportunity is larger only if conversion, live cabinet fill, and price are all at the high end — none of which is measured yet. We should show a range, not a single $420 k as if it were booked.

---

## 5. Recommended bottom-up SOM (assumptions labelled)

Keep the draft’s identity, but start from **sourced** declaration counts, show a **fee range**, and do **not** headline a single year-3 revenue.

**Step A — volume (sourced / lightly derived)**

- 2025 cargo declarations: **1 153 000** [SOURCED, UZA 25.08.2026].
- 2025 import declarations: **≈ 660 000** [DERIVED from Daryo 30.12.2025, 581 000 / 0.88; grammar risk, see §2.2].
- 2026 import run-rate: 397 000 × 12/7 ≈ **681 000** [DERIVED from UZA Jan–Jul 2026; ASSUMPTION that the seven-month pace holds].

**Step B — who might be in scope (all ASSUMPTION after this line)**

- Statutory SME **value** share (53.6 %) may be used only as a **loose upper-bound proxy**, with the caveat in §2.3.
- Further cuts (ordinary IM40, not excise/licensed, not already cleared inside a kargo contract, has or will obtain ERI, willing to self-file) are **not measured**. Until interviews, any figure after Step A is a scenario, not a SAM “fact.”
- The draft’s 75 % × 70 % on a scaled 545 k SME-proxy stock → **286 k** should be labelled **optimistic / untested**, not “the SAM.”

**Step C — price (ASSUMPTION)**

- YuklaGo fee is **not in the spec**. 180–250 k so'm per IM40 is a proposal. InCustoms’ published draft/XML packs (125 k / 5×300 k) are a visible floor if live cabinet fill is off.
- Do not convert “customer savings” with a 1.2 m broker fee as if it were paid.

**Step D — year-3 capture (ASSUMPTION)**

- 2 %, 6 % and 12 % are scenarios. 10 % a year SAM growth is a scenario (trade grew 20.7 % in 2025; declarations +12 % in the 10-month 2025 briefing; WTO timing is not a signed date on the WTO page we opened).

**Scenario table (for the slide; every column after volume is an assumption)**

| Scenario | Fit stock (decls / yr) | Y3 share | Price (so'm) | Y3 revenue |
|---|---|---|---|---|
| Tight / interview-pending (kargo still dominates; no live official fill) | 50 000 [A] | 3 % [A] | 180 000 [A] | **0.27 bn so'm (~$23 k)** |
| Mid (some self-file with copy-assist / practice path) | 100 000 [A] | 4 % [A] | 220 000 [A] | **0.88 bn so'm (~$73 k)** |
| Draft base, if 286 k growing 10 %/yr, 6 %, live ED2 | ~381 000 [A, draft] | 6 % [A] | 220 000 [A] | **5.0 bn so'm (~$420 k)** — *upside, not the forecast* |

The 50 000 and 100 000 stocks are **illustrative assumption bands**, not new research. They exist to stop the $420 k from standing alone. Replace them the moment interviews give a real self-file / kargo / broker split.

**Pitch wording that survives a jury**

> In 2025 Uzbekistan’s customs authorities processed **1.15 million** cargo declarations (Customs, quoted by UZA, 25.08.2026). Official statistics count **about 27 100 importers** in 2024, and statutory small businesses made up **53.6 % of import value** in 2025 — a value share, not yet a count of YuklaGo-fit filings. Published broker *list* prices in Tashkent run from a few hundred thousand so'm to about **2.2 million** per IM40; there is no official average, and many small buyers use per-kilogram kargo instead. We will price below those list fees. How many of those declarations we can win, and whether we may fill the official cabinet automatically, are still open. Our year-3 revenue is a **scenario**, not a booking: from tens of thousands of dollars in a tight case to about **$0.4 million** only if the draft’s conversion and live-cabinet assumptions all hold.

---

## 6. What to change in the draft before the pitch

1. Replace D2 with **1 153 000** (2025) and mention **397 000** import declarations in Jan–Jul 2026; keep D1 as a derived 2025 import estimate with the Daryo wording shown.
2. Correct or delete “about a third” and “80 % IM40/EK10.”
3. Show a **fee range** that includes Prom.uz **412 000 from** (22.07.2026) and BBBX/UIA; stop calling 1 200 000 “conservative typical.”
4. Move $114 M TAM and $420 k SOM out of the headline, or put the assumption tags on the same line.
5. Add a kargo path (sourced offers, dated) and say the lead user’s current spend may not be a broker fee at all.
6. Do not cite “1 500+ brokers” or “31 of 34 / join WTO in 2027” until the exact official sentence is on file.
7. Do not assume live ED2 automation in the base SOM.
8. Keep the SOURCED / DERIVED / ASSUMPTION labels — they are the draft’s best habit. Apply them to the pitch line as strictly as to the table.

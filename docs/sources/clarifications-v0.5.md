---
title: "YuklaGo web UI v0.5: clarifications"
subtitle: "Screen corrections against the v0.5 boards. This is not a spec v4. Spec v3 still applies. Each item lists the page, what is wrong, the exact fix and a priority."
---

**Reviewed:** `source-v0.5.pdf` (29 pages, rendered and read page by page; text extracted). It was checked against `simplify-brief-v0.4.md`, `clarifications-v0.2/v0.3.md`, `yuklago-spec-v3.md` (§6A, DEC-29), `team-review/roles-rbac.md`, `roles-legal.md`, `v0.4-uiux.md` and `declarant-v3-check.md`, and the Varaq brand files.

**Verdict:** **not ready yet.** The simplification works: there are 5 screens to "Imzoladim", one primary button per screen and short copy. Numbers, chips, the MASHQ banner and the header are right. Six blockers remain. All of them concern roles, consent or legal lines. Each is a copy fix or a missing sheet, not a redesign.

# Passed (keep exactly as is)

- **Simplicity targets.** The clean path is 5 screens to "Imzoladim" (p7 → p8/9 → p10 → p11 → p13–16). Every clean-path screen has 1 filled button, and body copy is under 60 words. Article numbers appear only in chips. The stepper has 5 stages. Exceptions are cards on the same screen (p10). The fill rail is ≤ 25 words, and "Oddiy" sits behind a settings icon.
- **Numbers.** CV 54 800 000; duty 15 % = 8 220 000; VAT 7 562 400; fee 440 000 (1 BHM); total ≈ 16 222 400; landed ≈ 71 022 400 / 77 160 000 without a certificate (+6 137 600); pre-arrival 352 000 (p20). The code is 8539 52 000 9 in display text, and raw `8539520009` appears only where it is written into the cabinet. Grafa 34 = 156 ("CN" no longer appears anywhere). Grafa 44 = 202 · 220 · 301 · 417 · 701. "16, 17 va 36-grafalar IM 40da boʻsh qoladi" (p22). The grafa counts are 13 + 12 + 16 + 5 = 46, and 45/46 are consistent with the FX.
- **Must-stay-visible lines that are present:** "Brokersiz, oʻzingiz topshirasiz — tez va tushunarli" (p5); "Tasdiqlayman — kod uchun men javob beraman" (p10); the attestation tick (p11); "Taklif, qonun emas" (p10); "≈ Taxmin" with source chips; "Topshiring 27.11 · chegara 28.11 · post taqvimi tasdiqlanmagan" in the shipment header; the MASHQ banner and watermark only on mock surfaces (p13–16), and none in real mode (p17); "Tayyor — asoschi tasdiqlagach yoqiladi"; the anti-fraud line; "YuklaGo izohi, rasmiy kod emas" (p26); "YuklaGo — mustaqil xizmat, davlat organi emas".
- **Banned phrases:** none appear on a product surface. They appear only in the p1 "Ishlatmang" column, which is intended.
- **Header and language (v0.3 and v0.4 items):** one header everywhere, with the globe, the current language and a chevron. The open menu has a tick and opens downward without covering buttons (p24). RU shows "Русский" (p29), mobile shows globe + "UZ", and the settings "Til" row is synced. There is one avatar style. "Brokerga berish" moved to the ⋯ menu (p25). The "Sabab" chips wrap correctly (p23). English "No-go" is replaced by "Taqiqlangan" in the UI.
- **Brand.** Onest and JetBrains Mono are used. Indigo #2E2BA0 is the only button colour. Saffron appears only in the logo fold and the your-turn panel. The logo files and clear space match the brand sheet. Uzbek uses U+02BB (ʻ) consistently. The only "o'" is the intentional wrong example on p1.
- **Admin** correctly never appears in the client UI.

# Blockers

**B1 · p6 "Bir martalik sozlash", card 3/5 — the role picker is back.**
*Wrong:* "Kim imzolaydi?" offers **Men / Shtatdagi mutaxassis / Broker mutaxassisi**. The CEO decision (DEC-29, uiux S4 P0) is one client role: the account user is the signer.
*Fix:* replace the card with the S4 check, titled **"Siz imzolaysiz"**, with no choices. It shows (a) the ERI from step 2 and (b) "ed1 roʻyxatidamisiz?" (Ha, kiritilganman / Hali yoʻq) plus the authority end date (one date field, or "muddatsiz"). Keep these lines visible on the card:
- "Imzolovchi — deklaratsiyalovchi shaxslar roʻyxatiga kiritilgan shaxs."
- "Faqat oʻz ERI kalitingiz bilan imzolang. Boshqa odamning kalitini ishlatmang."
- "Brokersiz, oʻzingiz topshirasiz."
- For non-directors (a small "Rahbar emasman" link that reveals one line, not a choice): "Direktor ed1 → TIF ishtirokchilari roʻyxati orqali sizni qoʻshishi kerak."

Also draw the **S5 signer-change card**, shown once when a new certificate appears: "Imzolovchi oʻzgardi. Yangi imzolovchi ed1 roʻyxatiga kiritilganmi?" (Ha / Yoʻq). It is warn-only; "Yoʻq" locks filing until S4 passes. Step-up SMS applies (B3).

**B2 · All signed-in screens, plus p18, p19 and p27 — YuklaGo Support (Yordam xizmati) has no surface.**
*Wrong:* "Yordam" does not appear anywhere. There is no help link in the header, none on blocker or error cards, no support-access consent sheet and no actor names in the security log. Role 2 of 3 is undrawn.
*Fix:*
1. Add a text link **"Yordam"** in the header (from p5 on) and in the ⋯ overflow of every blocker and error card (p18 error, p19 cards).
2. Draw the **"Yordam xizmatiga ruxsat"** sheet. It has the reason (select); the duration (default **24 soat**, then it closes by itself); "Maʼlumotlaringiz yashirilgan holda koʻrinadi"; "Istalgan payt bekor qilish"; "Bu ruxsat xavfsizlik jurnalida yoziladi"; and the line "Yordam xizmati faqat siz ruxsat bergan muddatda, yashirilgan maʼlumotni koʻradi. Imzolamaydi, yubormaydi, toʻlamaydi." The primary button is "Ruxsat berish", which leads to step-up SMS (B3).
3. In Settings → Xavfsizlik (p27), add the "Yordam xizmatiga kirish" row (state, time left, "Bekor qilish") and show the log with actors **Siz / YuklaGo / Yordam xizmati**.

Never write "Support" or "Admin" in the client UI.

**B3 · p27 and p5 — the step-up SMS sheet is missing.**
*Wrong:* there is no "Tasdiqlash uchun SMS kodni kiriting" sheet. "Yuklab olish" and "Hisobni oʻchirish" (p27) act directly.
*Fix:* draw one reusable bottom sheet: the title "Tasdiqlash uchun SMS kodni kiriting", the masked number, 6 boxes, "Qayta yuborish", one primary "Tasdiqlash", and a one-line reason that changes per trigger. Show it for exactly these 5 triggers: (1) a new device sign-in, (2) a signer change (S5), (3) support access (B2), (4) full data export ("Yuklab olish"), (5) account deletion. Never show it for payment or signing. Annotate the sheet "count: excluded from the 15 actions".

**B4 · p16, p17 (your turn) and p29 RU — the signing line is missing.**
*Wrong:* the your-turn panel says "Kabinetda oʻzingiz bosing", but the must-stay-visible line (roles-legal B4 item 2) is absent.
*Fix:* add one line under the heading "Endi sizning navbatingiz": **"Siz oʻzingiz imzolab, oʻzingiz yuborasiz — faqat oʻz ERI kalitingiz bilan."** In RU: "Вы сами подписываете и отправляете — только своим ключом ЭЦП." It does not count toward the 60 words.

**B5 · p7 "Hujjatlarni yuklang" — documents are processed before consent.**
*Wrong:* six files already show "Tanildi" (recognised) while the consent box below is unticked. Consent must come before the first upload or processing (AC-32.1, ZRU-547 art. 21).
*Fix:* on the first shipment, show the consent card **above** the drop zone. Keep the drop zone disabled ("Avval rozilikni belgilang") until the tick is set. Returning users don't see the card. If you keep the order, file rows must read "Yuklandi" (queued, not read) until the tick is set, and "Tanildi" appears only after it.

**B6 · p9, p10 (ed1 card), p19 ("Koʻrib chiqish yopiq") and p25 — the block state lacks the signer-listed wording.**
*Wrong:* these screens say "Imzolovchi ed1 roʻyxatida emas" / "Imzolovchini ed1 roʻyxatiga kiriting". §4a item 7 requires the exact wording in the block state.
*Fix:* on the p10 blocker card, add the line "Imzolovchi deklaratsiyalovchi shaxslar roʻyxatiga kiritilgan shaxs boʻlishi kerak." The row label "Imzolovchini ed1 roʻyxatiga kiriting" can stay as is.

# Polish

**P1 · p2 (overview) — the action counter undercounts, and the stage names differ.**
*Wrong:* "14 amal" leaves out 3 taps: "Tekshirishni boshlash" (p7), "Javob berish" (p9) and "Ilovani ochish" (p12). That makes about 17 in total, over the ≤ 15 target. The p2 cards say "Savollar" and "Tayyor", but the stepper says "Tekshiruv" and "Holat".
*Fix:*
- Start the check automatically after upload for returning users (consent already given).
- Show question 1 inline under the result, with no "Javob berish" hop.
- Let "Kompyuterda toʻldirish" deep-link straight into the app. The modal appears only if the app doesn't open.

Then recount honestly. Use the same 5 stage names on p2 as on the stepper.

**P2 · p5 (landing) — two filled buttons.**
*Wrong:* the header "Kirish" and the hero "Boshlash" are both filled.
*Fix:* make the header "Kirish" an outline button and keep "Boshlash" as the only primary. Also change "Siz faqat imzolaysiz." to "Siz oʻzingiz imzolab, oʻzingiz yuborasiz." (The user also saves, sends and pays, so "faqat" overclaims.)

**P3 · p9, p11, p18, p22, p25 — the total assumes an origin certificate that isn't uploaded.**
*Wrong:* the story has no origin certificate (p9 asks for it; 701 has no number), yet the total of 16 222 400 and "Qoʻshimcha boj BK 300¹ · 0" assume one.
*Fix:* while the certificate is missing, add a small chip "sertifikat bilan" next to the total. On p22, the 300¹ row reads "0 · sertifikat bilan (sertifikatsiz +6 137 600)". The numbers stay unchanged.

**P4 · p25 — the code status says "Tasdiqlangan".**
*Fix:* change it to "Siz tasdiqladingiz" (v0.3 rule: "Tasdiqlangan" implies an authority).

**P5 · p10 — the source chip "Rasmiy roʻyxat · 18.11.2026" uses the reserved word "Rasmiy".**
*Fix:* change it to "TIF TN · 18.11.2026". "Rasmiy" is reserved for specialist-confirmed, gold-proven rates (brand sheet).

**P6 · p24 (home).**
*Wrong:* the "Faol · 5" segment is ink-filled, and the brand allows no black buttons. The "Jami, soʻm" column shows the landed cost, which is easy to confuse with "Toʻlovlar".
*Fix:* make the selected segment indigo-tint with indigo text, and rename the column "Kelib tushgan narx, soʻm".

**P7 · p18 (session end).**
*Fix:*
- Draw the session-recovery state "Qayerdan davom etamiz?" (the app closed, the network dropped or the device changed), with one primary "Davom ettirish" (uiux P8).
- In the error overflow, list "Yordam" (B2).
- On the payment card, add "Kabinetdagi 47-grafa summasini toʻlang" next to the ≈ amount.
- Set the placeholder in JetBrains Mono (it currently falls back to DejaVu Sans Mono).

**P8 · p17 (real mode, your turn) — a tooltip covers the controls.**
*Wrong:* the E-IMZO tooltip covers the cabinet's "Saqlash / Imzolash va yuborish" buttons.
*Fix:* move it above the form or into the right panel.

**P9 · p28 (mobile home) — the attention list doesn't match web.**
*Wrong:* mobile shows 2 items, and web (p24) shows 3; YG-0409 "Taqiqlangan" is missing.
*Fix:* show the same 3 items (v0.3 rule: the same state on web and mobile).

**P10 · p19 (state cards).**
*Fix:* change the designer label "NO-GO" to "TAQIQLANGAN". In the empty state, change "qolganini biz qilamiz" to "qolganini tekshirib, tayyorlaymiz" (an overclaim; the user signs and sends).

**P11 · p29 RU and p6 — copy fixes.**
*Fix:*
- "Ввоз · Разрешён" → "Ввоз · Запрета нет". "Разрешён" sounds like an official permit; Uzbek says "Mumkin".
- "вес нетто — от руки" → "вес нетто — рукописная цифра".
- Use non-breaking hyphens in "E-IMZO" and "e-imzo.soliq.uz", which currently break across lines on p6 and p29.

# Not an issue (don't change)

- Raw `8539520009` in the fill rail and cabinet fields: this is intended (v0.3 rule).
- Liberation fonts inside the mock and real cabinet schemes and the invoice crops: these are intended, because they must not look like YuklaGo.
- Grafa 36 has no field in the mock cabinet form: this is fine, because p22 states that it stays empty.
- p6 "Hali yoʻq" (ed1) lets set-up continue with a clear warning, and filing stays blocked later: this meets uiux P10.

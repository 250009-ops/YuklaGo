---
title: "YuklaGo — Product UI v1.0 · Figma review"
subtitle: "Read-only review of the Figma file against the screen hand-off. Polish gaps are recorded so the build follows the hand-off where a frame is wrong."
---

**File:** YuklaGo — Product UI v1.0 (`MJCyZ6SiNj6HdesKbwxDcM`). Reviewed read-only; nothing in the file was changed.
**Method:** full metadata of all 12 pages, about 12 000 text nodes scanned for copy, variables and tokens read, and 38 frames checked by screenshot (UZ, RU, practice and real, the consoles, the flows and the prototype).

# Verdict: ready with polish

All six v0.5 blockers (B1–B6) are fixed. All 64 screen IDs are present, there are no banned phrases, the data values match the spec, and MASHQ appears only where it is allowed. Nothing in the file blocks the build. There are **0 blockers** and **15 polish items**. Fix the top four first:

1. **P-01:** the language dropdown reads "Oʻzbekcha" on every RU frame.
2. **P-02:** the must-show line is missing on the C-10 code card.
3. **P-03:** the X- state frames use a different page shell.
4. **P-08:** the frames have no spec annotations, and the 14 actions have not been counted.

| Count | Value |
|---|---|
| Screen IDs in the spec / found / missing / extra | 64 / 64 / 0 / 0 |
| Top-level UZ frames (pages 03–08) | 268 (219 client, 49 console) |
| RU frames (page 11) | 206 |
| UZ frames with no RU twin | 16 (15 "overflow / help menu open" variants and S-02 "duration menu open") |
| RU frames with no UZ twin | 3 (C-10 62:40928, 62:41038, 62:41148) |
| Prototype frames / flow boards | 78 / 4 |
| v0.5 blockers B1–B6 fixed | 6 / 6 |
| Issues: blocker / polish | 0 / 15 |

# v0.5 blocker fixes

| # | Required | Where checked | Result |
|---|---|---|---|
| B1 | No role picker. C-05 "Siz imzolaysiz" with "Ha, kiritilganman" / "Hali yoʻq". S-03 new-signer card that warns only. | C-05 15:2863, S-03 15:15124 | Fixed |
| B2 | "Yordam" in every header and in the ⋯ menus. S-02 consent sheet: 24 soat (standart), masked, revocable, logged, "Ruxsat berish". | All sampled headers, S-02 15:14976, the help-menu-open frames | Fixed (see P-11 for layout polish) |
| B3 | S-01 SMS step-up for 5 triggers, plus wrong-code and locked states; never on payment or signing. | S-01 15:14598 and its 7 states | Fixed |
| B4 | D-05 your-turn panel: ink background, saffron rule, the signing line in UZ and RU, "Imzoladim". | D-05 15:12011, RU 21:28977 | Fixed |
| B5 | C-09 consent before any document is read; dropzone disabled until ticked. | C-09 15:3537, RU 21:20504 | Fixed |
| B6 | The wording "…deklaratsiyalovchi shaxslar roʻyxatiga kiritilgan shaxs…" on C-10 and X-02. | C-10 15:4846, 15:5997; X-02 15:15999 | Fixed |

# Polish gaps in the Figma file

Every item below is **polish** unless it says otherwise. They are ordered by impact.

**P-01 · The RU language dropdown shows "Oʻzbekcha"** (high).
Page `11 RU`, every client frame: for example C-01 21:19047, C-08 21:20348, C-09 21:20504, C-10 21:21296, C-15 21:25578 and S-01 21:31562. On C-08 21:20348 the open menu ticks "Русский ✓", but the trigger still reads "Oʻzbekcha". This fails checklist line "RU closed state drawn".
*Fix:* in the Header / Language dropdown component, bind the trigger label to a string variable (UZ "Oʻzbekcha", RU "Русский") so that every RU frame updates. Do the same for the mobile "UZ" pill, which should read "RU" in RU.

**P-02 · The must-show line #1 is missing on the C-10 code card.**
Page `03 Client web`: "C-10 / Check / result + Q1 / UZ" 15:4329, the Q1 states, prototype frame 23:1243 and RU 21:21296. The card has the button but not the line.
*Fix:* add "Kodni siz tanlaysiz va javob berasiz." under the confidence line and above the button. In RU: "Код выбираете вы и отвечаете за него." It is already correct on C-12.

**P-03 · The X- state frames use a different page shell from the C- screens.**
Page `06 Sheets & states`: X-01a/b/c (for example X-01b 15:15930), X-02 15:15999, X-07a/b/c (for example 15:16223) and their RU twins. Four things differ:
- the header nav shows "Bosh sahifa" as active instead of "← Yuklar";
- there is no shipment header card with the deadline chip and stepper;
- the card is left-aligned and 512 wide instead of sitting in the centred 720 column;
- the blocker cards have a × close and no status edge.

*Fix:*
- rebuild them on the C-10 shipment template, with the header card and stepper;
- place the card in the 720 column;
- remove the × (blockers are not dismissible);
- give stop cards a 1 px #C0362C border and a 4 px left edge (caution #A35C00 for warnings);
- keep the ⋯ (Yordam) button next to the primary inside the card, not below it.

**P-04 · The X-07c title and amount are wrong.**
"X-07c" 15:16223 and its RU twin. The page title reads "Eksport", but the case is YG-0417 · Paxta futbolkalar, an import before arrival.
*Fix:*
- set the header to "YG-0417 · IM 40 · import / Paxta futbolkalar";
- set "352 000 soʻm" in the 28 px bold amount style, with the green delta chip as on C-11.

**P-05 · The S-01 and D-01 step-up sheets have a duplicate heading.**
S-01, all states (15:14598 … mobile), and D-01 / new device 15:10220. Under the sheet title "Tasdiqlash uchun SMS kodni kiriting" there is a second heading, "SMS kodni kiriting". On D-01 the reason "Yangi qurilmadan kirish." sits under the button. RU S-01 21:31562 has lost the shield icon and the boxed close button.
*Fix:*
- delete the second heading;
- put the reason line directly under the title;
- on D-01, move the reason above the code field;
- copy the icon and the close button from the UZ frame into RU.

**P-06 · Designer notes are drawn inside product frames.**
Page `04 Desktop app`, the real-mode frames (for example D-03 real 15:11142), and their RU twins. The pane contains "Sxema. Bu yerda ed2.customs.uz sahifasi oʻz koʻrinishida ochiladi; YuklaGo faqat faol maydon halqasini qoʻshadi."
*Fix:*
- move the text to a sticky outside the frame;
- inside the frame keep only the ed2 URL, "Rasmiy sayt · YuklaGo emas", the schematic and the active-field ring.

**P-07 · Source chips are stacked one per line and lose their styling in RU.**
C-10 totals 15:4329, C-12 right card 15:7495, C-14 15:8280 and C-15 15:8611. The chips (PQ-181 · 16.02.2026, Namuna, sertifikat bilan, …) each fill a full row. RU C-01 21:19047 shows the chips as plain text, and RU C-15 21:25578 drops the PQ-181 chip.
*Fix:*
- lay the chips out in one wrapping row (gap 8, hug width);
- re-link the RU instances to the Chip component;
- restore the PQ-181 chip in RU C-15.

**P-08 · There are no per-frame spec annotations, and the happy-path action count is unverified.**
Hand-off §8.6 asks for a small sticky outside every frame that gives:
- the body word count;
- the primary action;
- the stage;
- the must-show lines present.

The "Design review — …" labels above the frames (for example 29:4871) are review notes, not these stickies. Flow 01 23:6219 states "14-action target not independently audited", and the cover 23:6336 still says "NOT RELEASE SIGN-OFF".
*Fix:*
- add the spec stickies;
- number the 14 user actions (1–14) on the prototype frames 23:1087 … and give the total on Flow 01;
- confirm that the C-12 sections need no extra clicks;
- remove the review-note labels and the "not sign-off" text once the stickies are in.

**P-09 · Frame names break the `ID / Name / State / Lang` pattern.**
- 15 frames have a fifth segment, for example 55:22885 "D-04 / Paused / practice · field changed / UZ / overflow open". The others are 55:23032, 55:23168, 55:23311, 55:23443, 55:23588, 55:23740, 55:24296, 55:24387, 55:24477, 55:24578, 55:24680, 55:24774, 55:24862 and 55:25025.
- 62:40928 "C-10 / Deadline Urgent / RU" and 62:41038 "C-10 / Deadline Passed / RU" have no State slot and no UZ twin. 62:41148 "C-10 / Netto / support comment visible / RU" has no UZ twin.
- The "Repair Rnn / …" frames on `10 Prototype` carry no screen ID.

*Fix:*
- fold the extra segment into the State slot, for example "D-04 / Paused / practice · field changed · overflow open / UZ";
- rename the C-10 frames to "C-10 / Check / deadline urgent / RU" (and the same for the others), and add their UZ twins on page 03;
- add the RU twins for the 15 menu-open frames and for "S-02 / … / duration menu open" (55:24192);
- give the repair frames their screen IDs, or move them to an archive page.

**P-10 · The C-05 progress indicator is wrong.**
C-05 15:2863 (and the other set-up steps C-03 to C-06) show "3 / 4" with a single short bar.
*Fix:* draw 4 equal segments (completed and current in #2E2BA0, the rest #E1E2EC) next to the "3 / 4" label.

**P-11 · The S-02 fixed line and facts need visual weight.**
S-02 15:14976 and its RU twin.
*Fix:*
- put the fixed line in a tint box (#ECEBFA, radius 10);
- give each of the 4 facts a 16 px icon (eye-off for masked, clock for 24 soat, undo for revocable, list for logged).

**P-12 · The AD-05 confirm sheet is missing a line, and a caption is in the wrong place.**
AD-05 15:18019.
*Fix:*
- add "Bu bayroq mijoz maʼlumotiga taʼsir qiladi." above "DPO tasdigʻi kerak";
- move the caption "Asoschi kaliti — faqat asoschi yoqadi" into the ED2_LIVE_AUTOMATION row, not under the table.

**P-13 · The D-02 practice waiting state shows the wrong cabinet view.**
"D-02 / Cabinet login / practice · waiting" 15:10304. The mock cabinet shows the declaration form before login.
*Fix:* until the "logged in" state, show the mock cabinet's E-IMZO login view, with the MASHQ banner and watermark kept.

**P-14 · Some RU copy is left untranslated.**
RU C-10 frames (for example 21:21296): the file caption "invoice_GM-2611.pdf · 1-bet".
*Fix:* change it to "invoice_GM-2611.pdf · стр. 1". Also search the RU page for any remaining "-bet", "soʻm" or "kun" strings, and use "сум" and "дн." instead.

**P-15 · The C-10 "Sizdan kerak" list styling is incomplete.**
C-10 result frames, for example 15:4329.
*Fix:*
- give each blocking row the red "Toʻsiq" badge (stop tint);
- show the saving as an amber chip, "≈ 6 137 600 soʻm tejaydi", rather than plain text.

# What passed

- **Coverage:** all 64 IDs are present, with every state the spec lists. The consoles (SP, AD) are UZ only, as specified, and every client ID has RU frames.
- **Banned and reserved words:** none of the §5.2 phrases appear, in UZ or RU. There is no "Tasdiqlangan", "Разрешён", "NO-GO" or "100% kafolat", and no Support/Admin wording in the client UI. "Rasmiy" appears only in "Rasmiy sayt · YuklaGo emas" and "rasmiy kod emas".
- **Characters:** U+02BB is used in every oʻ/gʻ, and there are no ASCII apostrophes in the copy.
- **Must-show lines:** present on C-12 ("Kodni siz tanlaysiz…"), C-15 ("Oʻz hisobingizdan toʻlaysiz. YuklaGo toʻlamaydi."), D-05 (the signing and anti-fraud lines) and the C-01 footer. C-10 is the exception (see P-02).
- **Data:** the checked values all match the spec:
  - totals and costs: 16 222 400; 71 022 400; 54 800 000 / 8 220 000 / 7 562 400 / 440 000;
  - code and certificate: 8539 52 000 9; PQ-181 · 16.02.2026;
  - weights and count: 412 vs 425 kg ("farq 13 kg", "Taklif, qonun emas"); 398;
  - dates and numbers: 27.11 / 28.11; MASHQ-000127; 26001/19112026/0001234;
  - C-11: 72 600 ¥ ≈ 9 800 000, 1,5 BHM = 660 000; X-07c: 352 000;
  - the D-05 grafa values.
- **MASHQ:** it appears only on practice D- frames (banner, pill, URL, watermark) and in the allowed practice rows on C-12 and C-13. The real D- frames have no banner and use the ed2 URL with "Rasmiy sayt · YuklaGo emas".
- **Tokens:** the variables match the spec:
  - colours: brand/primary #2E2BA0, accent #F5B43C, plus the practice and status sets;
  - type styles: Onest and JetBrains Mono;
  - radius 10 / 14 / 20, and the space scale.
  
  Saffron appears only in the logo and the D-05 panel. Indigo is the only button colour.
- **Buttons:** every sampled frame (sheets and errors included) has exactly one filled primary.
- **Happy path:** C-09 → C-10 → C-12 → D-02/03 → D-05 → C-15 is 5 screens to "Imzoladim" (Flow 01 23:6219). The action count still needs to be annotated (P-08).
- **Consoles:**
  - SP-03 is read-only and masked, with a redacted document preview, a watermark, and no edit, export or sign controls.
  - AD-05 shows the 🔒 DPO flags and the second-approver flow ("Tasdiqqa yuborish").
- **Other screens:**
  - C-20 security log: every row names the actor.
  - D-01 on a new device: no "Davom etish" shortcut.
  - D-07 recovery screen: present.
  - M-01: shows the same 3 items as web.

# Coverage table

Frame counts include the state variants found on the UZ pages (03–08) and on page 11 RU.

| ID | UZ frames | RU frames | States drawn (UZ) | Result |
|---|---|---|---|---|
| C-01 | 2 | 2 | default, narrow stacked | OK |
| C-02 | 8 | 8 | phone empty, phone filled, sending, code partial, code entered, wrong code, too many attempts, new device | OK |
| C-03 | 5 | 5 | empty, looking up, found, not found, network error | OK |
| C-04 | 3 | 3 | Ha selected, Yoʻq selected, no-key result | OK |
| C-05 | 5 | 5 | nothing selected, Ha + date, Hali yoʻq, Rahbar emasman expanded, past date | OK |
| C-06 | 4 | 4 | default, downloading, installed, non-Windows | OK |
| C-07 | 2 | 2 | default, ed1 caution | OK |
| C-08 | 5 | 5 | default, language menu open, empty, loading | OK |
| C-09 | 8 | 8 | returning user, first time unticked, ticked no files, uploading, reading, recognised, file error | OK |
| C-10 | 41 | 42 | progress, all checks done, result + Q1, default, answered, zero exceptions, Q1 answered, partial failure, offline, blocked, error | OK · 2 RU-only frames to fix (P-09) |
| C-11 | 2 | 2 | default, lines expanded | OK |
| C-12 | 7 | 7 | unticked not viewed, all viewed ticked, locked blockers, no ERI, real available | OK |
| C-13 | 1 | 1 | fallback only | OK |
| C-14 | 3 | 3 | default, menu open, session recovery | OK |
| C-15 | 6 | 6 | filled, empty number, wrong format, paid, copy toast | OK |
| C-16 | 6 | 6 | document requested, submitted only, registered, released, rejected | OK |
| C-17 | 2 | 2 | default, sent | OK |
| C-18 | 3 | 3 | one product, empty, search no result | OK |
| C-19 | 3 | 3 | default, help access open, avatar menu open | OK |
| C-20 | 7 | 7 | help open, help closed, help expired, filter Yordam xizmati, no other devices, log empty, log loading | OK |
| D-01 | 3 | 3 | app · known device, app · new device, app · web signed out | OK |
| D-02 | 7 | 7 | practice · logged in, practice · waiting, real · waiting, real · logged in, practice · wrong company, real · wrong company | OK |
| D-03 | 8 | 8 | practice · 27 of 46, practice · 46 of 46, real · 27 of 46, practice · read-back mismatch, real · read-back mismatch, real · 46 of 46 | OK |
| D-04 | 2 | 2 | practice · field changed, real · field changed | OK |
| D-05 | 14 | 14 | practice · waiting for Saqlash, practice · saved, practice · E-IMZO open, practice · signed and sent, real · waiting for Saqlash, real · saved, real · E-IMZO op… | OK |
| D-06 | 2 | 2 | practice · default, real · default | OK |
| D-07 | 6 | 6 | practice · recovery, real · recovery, practice · stopped, real · stopped, practice · menu open, real · menu open | OK |
| M-01 | 1 | 1 | default | OK |
| M-02 | 1 | 1 | default | OK |
| M-03 | 1 | 1 | default | OK |
| M-04 | 2 | 2 | default, link sent | OK |
| S-01 | 8 | 8 | new device, signer change, help access, full export, deletion, wrong code, locked, mobile · mobile | OK |
| S-02 | 5 | 4 | default, dropdown open, done, mobile · mobile, duration menu open | RU missing 'duration menu open' |
| S-03 | 5 | 5 | default, locked after No, other person, authority expiry, mobile · mobile | OK |
| S-04 | 2 | 2 | banner, phone notification · mobile | OK |
| S-05 | 4 | 4 | all data, audit only, log only, mobile · mobile | OK |
| S-06 | 3 | 3 | empty, typed, mobile · mobile | OK |
| I-01 | 3 | 3 | default, default · mobile | OK |
| I-02 | 3 | 3 | default, default · mobile | OK |
| I-03 | 3 | 3 | default, default · mobile | OK |
| I-04 | 2 | 2 | default | OK |
| I-05 | 2 | 2 | default, default · mobile | OK |
| I-06 | 3 | 3 | default, default · mobile | OK |
| X-01a | 1 | 1 | default | OK |
| X-01b | 1 | 1 | default | OK |
| X-01c | 1 | 1 | default | OK |
| X-02 | 2 | 2 | 3 open, 1 open | OK |
| X-03 | 1 | 1 | default | OK |
| X-04 | 1 | 1 | default | OK |
| X-05 | 1 | 1 | default | OK |
| X-06 | 2 | 2 | skeleton, skeleton · mobile | OK |
| X-07a | 1 | 1 | default | OK |
| X-07b | 1 | 1 | default | OK |
| X-07c | 1 | 1 | default | See P-04 |
| X-08a | 1 | 1 | server error | OK |
| X-08b | 1 | 1 | session expired | OK |
| SP-01 | 6 | 0 | login, 2FA, wrong password, wrong code, locked, refused | OK (UZ only, as specified) |
| SP-02 | 3 | 0 | list, empty, loading | OK (UZ only, as specified) |
| SP-03 | 3 | 0 | default, field with no data, expired overlay | OK (UZ only, as specified) |
| SP-04 | 4 | 0 | compose, sent, failed, client card | OK (UZ only, as specified) |
| SP-05 | 2 | 0 | list, empty | OK (UZ only, as specified) |
| SP-06 | 2 | 0 | client revoked, expired | OK (UZ only, as specified) |
| AD-01 | 6 | 0 | login, 2FA, refused, wrong password, wrong code, locked | OK (UZ only, as specified) |
| AD-02 | 5 | 0 | table, edit sheet, missing source, saved, conflict | OK (UZ only, as specified) |
| AD-03 | 3 | 0 | month, add sheet, missing source | OK (UZ only, as specified) |
| AD-04 | 3 | 0 | table, editing, saved and logged | OK (UZ only, as specified) |
| AD-05 | 5 | 0 | table, confirm sheet, pending, approved, rejected | OK (UZ only, as specified) |
| AD-06 | 4 | 0 | pending, approved, rejected, self-approval blocked | OK (UZ only, as specified) |
| AD-07 | 2 | 0 | table, filter by area | OK (UZ only, as specified) |

# Key screenshots

Every screenshot sits in `key-shots/`. The full set of 38 is in `shots/`.

![P-01 · RU C-08: the menu ticks Русский but the trigger reads Oʻzbekcha (21:20348)](key-shots/RU-C-08_21-20348.png)

![P-02 · C-10 result + Q1: the code card lacks "Kodni siz tanlaysiz va javob berasiz." (15:4329)](key-shots/C-10_15-4329.png)

![P-03 / P-04 · X-07c: a different shell and the title "Eksport" (15:16223)](key-shots/X-07c_15-16223.png)

![P-03 · X-02: left-aligned card, × close, "Bosh sahifa" nav (15:15999)](key-shots/X-02_15-15999.png)

![P-05 · S-01: duplicate heading (15:14598)](key-shots/S-01_15-14598.png)

![P-06 · D-03 real: a designer note inside the frame (15:11142)](key-shots/D-03-real_15-11142.png)

![Passed · D-05 your-turn panel, B4 (15:12011)](key-shots/D-05_15-12011.png)

![Passed · C-09 consent before upload, B5 (15:3537)](key-shots/C-09_15-3537.png)

![P-08 · Flow 01: "14-action target not independently audited" (23:6219)](key-shots/Flow01_23-6219.png)

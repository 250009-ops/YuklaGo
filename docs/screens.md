# Screen map

64 screen IDs. Routes are the client or console path. Sheets and system states are overlays on the parent route, not separate products.

Figma, view only: https://www.figma.com/design/MJCyZ6SiNj6HdesKbwxDcM/YuklaGo-%E2%80%94-Product-UI-v1.0

Copy is in the screen hand-off (`docs/sources/yuklago-designer-handoff.md`) and in `packages/i18n/locales/`. This page names the route, the states, and the API. It does not restate every string.

Global client rules: "Yordam" in the header and in the overflow of every blocker. "Brokerga berish" only in the shipment overflow, except X-01c where it is the secondary link. Deadline chip once, in the shipment header. One primary button. Stepper names in `docs/i18n.md`.

Happy path: C-08 → C-09 → C-10 → C-12 → D-02/D-03 → D-05 "Imzoladim" → C-15 → C-16. Clean-path screens to "Imzoladim": C-09, C-10, C-12, D-02/D-03 (one window), D-05.

## Client web

| ID | Route | States | API |
|---|---|---|---|
| C-01 | `/` | default, narrow | None. Sample card uses `contracts/calc/golden-yg0412.json`, chip Namuna. "Boshlash" and "Kirish" go to C-02. Header "Kirish" is outline. "Batafsil" opens I-03 |
| C-02 | `/sign-in` | phone empty, phone filled, sending, code partial, code entered, wrong code, too many attempts, new device | `requestOtp`, `verifyOtp`. New device uses the same OTP with reason line, then `verifyStepUp` trigger `NEW_DEVICE`. Locked 10 minutes |
| C-03 | `/setup/stir` | empty, looking up, found, not found, network error | `lookupStir`. Not a cabinet scrape. Unknown STIR is an error state, not a guessed company |
| C-04 | `/setup/eri` | Ha, Yoʻq, no-key result | `saveEriStatus`. No-key state names the issuer "Yangi texnologiyalar" ilmiy-axborot markazi and the three channels. No address and no fee (AC-1.1) |
| C-05 | `/setup/signer` | nothing selected, Ha + date, Hali yoʻq, Rahbar emasman expanded, past date | `saveSigner`. Title "Siz imzolaysiz". No role picker. Lines in must-show 6, 7, 9. Past date is a field error. Hali yoʻq lets set-up continue and locks fill later |
| C-06 | `/setup/desktop` | default, downloading, installed, non-Windows | Static download URLs. Non-Windows explains macOS is next and offers the extension fallback |
| C-07 | `/setup/done` | default, ed1 caution | `completeSetup`. Caution when ed1 is "Hali yoʻq" |
| C-08 | `/` signed in | default, language menu, empty (X-03), loading (X-06) | `listShipments`. Segment "Faol" is indigo tint, not ink. Column "Kelib tushgan narx, soʻm". Demo rows YG-0412, YG-0415, YG-0417, YG-0418, YG-0402. YG-0409 is the attention list, not a normal row |
| C-09 | `/shipments/new` | returning, first time unticked, ticked no files, uploading, reading, recognised, file error (X-04) | `putConsent` before `uploadDocument` and `enqueueRead`. Unticked: files are not read. `getJob` then C-10 |
| C-10 | `/shipments/{id}/check` | progress, checks done, result + Q1, answered, zero exceptions, partial failure, offline (X-05), blocked, error (X-08) | `getShipment`, `getCalc`, `listFindings`, `listQuestions`, `answerQuestion`, `confirmCode`, `putEarxiv`, `getJob`. Must-show line 1 on the code card. Chip "TIF TN · 18.11.2026". Totals from the golden fixture, chip "sertifikat bilan" while 701 is missing. Primary "Koʻrib chiqishga oʻtish" only when blockers are closed |
| C-11 | `/shipments/{id}/lines` | default, lines expanded | `getCalc`, `getShipment`. YG-0418. Fee 660 000. Freight shares sum to ≈ 9 800 000 |
| C-12 | `/shipments/{id}/review` | unticked not viewed, all viewed ticked, locked (X-02), no ERI, real-mode flag off | `getDraft`, `attestDraft`, `listFindings`. User opens every section (DEC-7). Real row shows "Tayyor — asoschi tasdiqlagach yoqiladi". Primary "Kompyuterda toʻldirish" deep-links `yuklago://fill/{id}` |
| C-13 | `/shipments/{id}/open-desktop` | fallback only | `createFillSession` not started until the app opens. Shown when the protocol does not open. Extension install is the secondary path |
| C-14 | `/shipments/{id}` | default, menu open, session recovery | `getShipment`, `getClocks`, `listFindings`. Resume point. Overflow: I-04, I-05, C-17, S-02, delete |
| C-15 | `/shipments/{id}/session` | number empty, wrong format, filled, paid, copy toast | `putRegistration`, `markSigned` already done on the desktop. Manual "Toʻladim" in the overflow. It does not call a bank. Must-show line 15. Hint "Kabinetdagi 47-grafa summasini toʻlang" |
| C-16 | `/shipments/{id}/status` | document requested, submitted only, registered, released, rejected | `explainMessage`, `getShipment`. User pastes the customs text. Chip "YuklaGo izohi, rasmiy kod emas". No match offers C-17. Corridor text uses R36 and R11 as information, not a countdown |
| C-17 | `/shipments/{id}/broker` | default, sent | `createHandoff`, share link. Owner sees the field list first. Optional, never the default path (AC-31.1) |
| C-18 | `/products` | one product, empty, search no result | `listProducts`. Full 10-digit codes only. Rate-change flag when the loaded table changes. Wording "YuklaGo jadvali yangilandi", not an official feed |
| C-19 | `/settings` | default, help row, avatar menu | `getMe`, `patchMe`, `getConsent`. Language row matches the header. No key upload. "ERI va kabinet" explains the desktop app version and the allow-list, and the extension version |
| C-20 | `/settings/security` | help open, help closed, help expired, filter Yordam xizmati, no other devices, log empty, log loading | `listDevices`, `revokeDevice`, `listAudit`, `revokeGrant`. Actors on every row: Siz / YuklaGo / Yordam xizmati. Admin is not a client-visible actor name. "Yordam xizmatiga kirish" opens S-02 |

## Desktop

Custom protocol `yuklago://`. Window 1440 × 900. Practice and real are both states of D-02–D-07. Practice has the MASHQ banner. Real does not, and shows "Rasmiy sayt · YuklaGo emas" when ed2 is loaded.

| ID | Route | States | API |
|---|---|---|---|
| D-01 | app sign-in | known device, new device, web signed out | `requestOtp`, `verifyOtp`, `verifyStepUp` `NEW_DEVICE`. No "Davom etish" shortcut |
| D-02 | fill / login | practice waiting, practice logged in, real waiting, real logged in, practice wrong company, real wrong company | `getFillSession`. Engine idle until the user has passed the cabinet login. Wrong company compares the public STIR HMAC and stops (AC-1.13). Practice waiting shows the mock login view, not the form |
| D-03 | fill / running | practice 27 of 46, practice 46 of 46, real 27, real 46, read-back mismatch both targets | `appendFillEvents` with hashes. Field count comes from the mapping. Demo is 46 for one IM40 item |
| D-04 | fill / paused | practice field changed, real field changed | Local diff. "Qoralamani ham yangilash" writes back only after the user confirms, via `attestDraft` on the changed grafa |
| D-05 | fill / your turn | practice and real × waiting for Saqlash, saved, E-IMZO open, signed and sent | No API click for sign or send. `markSigned` when the user presses "Imzoladim" on the rail. Must-show lines 2 and 11. Save click stays off |
| D-06 | fill / no e-imzo | practice, real | None beyond the session. Offers the extension fallback. `DESKTOP_EIMZO_COMPAT` is [UNVERIFIED] |
| D-07 | fill / recovery | practice and real × recovery, stopped, menu open | `getFillSession`. Primary "Davom ettirish" or "Qayta urinish". "Yordam" in the overflow opens S-02 |

## Mobile shell

Same API as the web. Width 390. No route offers a password, a key upload, or a sign button (AC-M1). Filing steps show M-04 only (AC-M2).

| ID | Route | States | API |
|---|---|---|---|
| M-01 | `/` | default | `listShipments`. The same three attention items as the web home, including YG-0409 Taqiqlangan |
| M-02 | `/shipments/{id}/questions/{qid}` | default | `answerQuestion`. Demo: net weight 398, handwritten, packing list agrees |
| M-03 | `/shipments/{id}/result` | default | `getCalc`. Golden totals, Namuna, PQ-181 · 16.02.2026, sertifikat bilan, deadline chip |
| M-04 | `/shipments/{id}/continue` | default, link sent | Creates a desktop link. Does not start a fill on the phone |

## Sheets

| ID | Host | States | API |
|---|---|---|---|
| S-01 | any of the five triggers | new device, signer change, help access, full export, deletion, wrong code, locked, mobile | `requestStepUp`, `verifyStepUp`. Never mounted on pay or sign. Not counted in the 14-action path |
| S-02 | header Yordam, blocker overflow, C-20 | default, duration menu, done, mobile | `createGrant` after S-01 trigger `SUPPORT_ACCESS`. Durations 24 (default), 4, 72. Scope defaults to the current shipment. Must-show line 13 |
| S-03 | D- window and next web visit | default, locked after Yoʻq, other person, authority expiry, mobile | `saveSigner` or lock. "Ha" goes through S-01 `SIGNER_CHANGE`. "Yoʻq" locks fill. Other-person variant does not switch account |
| S-04 | other sessions | banner, phone notification | `revokeDevice` via "Sessiyani tugatish" |
| S-05 | C-19 / C-20 | all data, audit only, log only, mobile | `requestExport`. Step-up only for "Barcha maʼlumotlar" |
| S-06 | C-19 | empty, typed, mobile | User types "OʻCHIRISH" / "УДАЛИТЬ", then S-01 `ACCOUNT_DELETION`, then `requestDeletion` |

## Info layers

| ID | Opens from | API |
|---|---|---|
| I-01 | "Tarkibi" | `getCalc`. Rows: duty 8 220 000, 300¹ 0 with the without-certificate note, excise 0, VAT 7 562 400, fee 440 000, total ≈ 16 222 400 Namuna |
| I-02 | deadline chip | `getClocks`. Explains +14 and +15. Does not say 24:00 |
| I-03 | C-01 "Batafsil", S-02 | Static. Does: read, suggest a code, calculate, fill. Does not: log in, sign, send, pay, store the ERI key |
| I-04 | C-12 and the overflow | `getDraft`. Includes the empty 16, 17, 36 line for IM40 |
| I-05 | overflow | `requestExport` of one pack. No step-up. Caption: the broker pack is this pack |
| I-06 | any source chip | `getSource` or a static record. "YuklaGo izohi, rasmiy matn emas." Link to lex.uz |

## System states

These are cards on the parent screen. They still have one primary and "Yordam" in the overflow, except where the table says otherwise.

| ID | Parent | Behaviour | API |
|---|---|---|---|
| X-01 | C-10 | States: (a) IMEI blocker, upload a list the user provides, `uploadDocument`. (b) Taqiqlangan, VMQ 658, YG-0409, no primary, secondary "Yukni yopish" only, no broker exit, `deleteShipment`. (c) "Rasmiy stavka topilmadi", fill locked, secondary "Brokerga berish", `getCalc` completeness refused | `uploadDocument`, `deleteShipment`, `getCalc` |
| X-02 | C-12 | Review locked. Demo: netto, E-arxiv 417 and 701, ed1 list. The ed1 row uses the declaring-persons wording | `listFindings` |
| X-03 | C-08 | Empty. "qolganini tekshirib, tayyorlaymiz" | `listShipments` empty |
| X-04 | C-09 | File unreadable | `uploadDocument` error |
| X-05 | C-10 | Offline. Answers kept on device | Replay `answerQuestion` when online |
| X-06 | lists | Skeletons | None |
| X-07 | Check, when the router needs a card | States: (a) regime question only if the text suggests the goods return, 12 vs 10, `patchShipment`. (b) EK10 checklist for YG-0402, phyto, origin certificate, own-production question for grafa 43, export duty "rasmiy stavka topilmadi", `getShipment`, `listFindings`. (c) pre-arrival for YG-0417, amount 352 000, not an export, `choosePreArrival` | `patchShipment`, `getShipment`, `listFindings`, `choosePreArrival` |
| X-08 | any | States: (a) server error, data kept, retry the last call. (b) session expired | `getSession` returns 401, then C-02 |

## Support console

Origin: the console app. Uzbek only. No edit, export, sign, send, pay, or cabinet control, including disabled ones.

| ID | Route | States | API |
|---|---|---|---|
| SP-01 | `/staff/sign-in` | login, 2FA, wrong password, wrong code, locked, refused (admin account) | `staffLogin`, `staffVerifyTotp` |
| SP-02 | `/support/grants` | list, empty, loading | `listMyGrants`. No client search. Empty: "Hozircha ochiq ruxsat yoʻq. Ruxsatni faqat mijoz beradi." |
| SP-03 | `/support/grants/{id}` | masked, field empty, expired overlay | `getGrantMasked`. Watermark on previews. Timer in the top bar |
| SP-04 | panel on SP-03 | compose, sent, failed, and the client card it produces | `postComment`. Does not change the draft |
| SP-05 | `/support/sessions` | list, empty | `listSupportSessions`. This staff member only |
| SP-06 | same as SP-03 when closed | client revoked, expired | Next `getGrantMasked` returns ended. Content cleared |

## Admin console

Uzbek only. No clients nav.

| ID | Route | States | API |
|---|---|---|---|
| AD-01 | `/staff/sign-in` tag ADMIN | login, 2FA, refused (support account), wrong password, wrong code, locked | `staffLogin`, `staffVerifyTotp` |
| AD-02 | `/admin/tariffs` | table, edit sheet, missing source, saved, conflict | `listTariffs`, `putTariff`. Source and date required. Demo row `8539 52 000 9`, 15%, PQ-181, 16.02.2026, Faol |
| AD-03 | `/admin/calendar` | month, add sheet, missing source | `listCalendar`, `postCalendar`. AC-8.1c |
| AD-04 | `/admin/tolerances` | table, editing, saved and logged | `listTolerances`, `putTolerance`. Label "Taklif, qonun emas" is not editable |
| AD-05 | `/admin/flags` | table, confirm sheet, pending, approved, rejected | `listFlags`, `requestFlagChange`. 🔒 opens "Bu bayroq mijoz maʼlumotiga taʼsir qiladi. DPO tasdigʻi kerak." `ED2_LIVE_AUTOMATION` shows "Asoschi kaliti — faqat asoschi yoqadi" |
| AD-06 | `/admin/approvals` | pending, approved, rejected, self-approval blocked | `listApprovals`, `decideApproval`. Visible only when `isDpo`. Requester cannot approve themselves |
| AD-07 | `/admin/journal` | table, filter by area | `listConfigLog`. Config rows only |

## Count

C-01–C-20 (20), D-01–D-07 (7), M-01–M-04 (4), S-01–S-06 (6), I-01–I-06 (6), X-01–X-08 (8, with X-01 split into a/b/c and X-08 into a/b as states, not extra IDs), SP-01–SP-06 (6), AD-01–AD-07 (7). Total 64.

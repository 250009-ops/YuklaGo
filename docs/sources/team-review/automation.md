# YuklaGo: cabinet automation review (feasibility, stack, mock portal, design changes)

*18 Nov 2026, Tashkent (UTC+5). Inputs: `yuklago-spec-v2.md` (§6 step 13, §7 Y14–Y17, §8.1–8.2, §9), `design-v0.1/design-rationale.md` §4 plus the automation boards in `yuklago-web-ui-v0.1.pdf`, `/workspace/yuklago/ARCHITECTURE.md` §6.4, §8 and §9. All measurements come from the working prototype in `/workspace/yuklago/autofill/` (README, `runner/out/report.json`). Not legal advice.*

**Verdict.** On a page whose structure we control (the mock), the core is feasible and fast. A real-ed2 fill is **unverified**. We have never seen the live markup, and the legal question is still open. For the demo, ship the mock with a browser extension and keep a recorded Playwright video as backup. After the hackathon, the filing client should be the extension, not a desktop app.

---

## 1. Feasibility and speed, feature by feature

**What the prototype proves.** It fills 78 fields: 33 header fields, 3 goods lines × 10 fields, and 15 FX and payment fields. It adds goods rows by itself. The extension and the runner share one fill engine (`extension/lib/filler.js`) and one declarative mapping (`mappings/mock-ed2.json`).

| Run | Result | Time |
|---|---|---|
| Playwright runner, headed, "orta" (200 ms per field, 8 ms per character) | 78/78 filled, 0 mismatches, 0 blocked, 0 not found | **23.4 s** |
| Extension (MV3, unpacked, real `chrome.*` APIs), same speed, including a ~2 s pause/resume | 78/78, 0 mismatches | 25.4 s |
| "tez" (40 ms per field, whole value at once) | 78/78 | **3.3 s** |
| Guard test: hostile mapping aimed at the ERI PIN, the .pfx input, sign, submit and the modal OK | 7/7 actions blocked, mock event journal empty | n/a |
| Read-back test: the page quietly cuts the STIR to 7 digits | mismatch detected and the field marked red | n/a |

| Feature (spec / design) | Status | Notes and risks |
|---|---|---|
| **Fill the cabinet in front of the user** (Y14, design §4) | ✅ on the mock. ❓ on real ed2 | The engine types with real `input`/`change` events, and the mock's live totals react to them. Real ed2 adds unknowns: **selectors not captured**, possible **iframes** (need `allFrames` plus host permission per origin), **tabbed or multi-page forms** (need "open tab / wait for selector" steps), **custom widgets** (searchable select, date pickers and server-side TN or counterparty lookups need adapters), and **server latency**, which will dominate total time more than typing does. |
| **Read-back verification** (design: "every value is read back after it is typed; a mismatch stops the session") | ✅ partly | The prototype re-reads **all** fields at the end and flags mismatches. The design wants a **per-field** read-back that stops on the first mismatch, which is a small change (read after blur plus ~150 ms). It also needs **type-aware normalisation**: ed2 may show "18 450,00" for 18450.00 or reformat dates. Comparing strict strings would cause false stops. |
| **Pause / take-over** (Y15, design "Interrupt") | ✅ basic. ⏳ the rest | Built: Pauza / Davom / To'xtatish in the panel (tested: progress froze at 7/78). **Not built but feasible:** pause on Space, and pause on any *real* click or keypress in the cabinet. We can tell real input from ours because our events have `isTrusted=false` and the user's have `true`. **Detecting a user edit and offering "Qoralamani ham yangilash"** needs a channel from the extension back to the YuklaGo web app (`externally_connectable` messaging or backend sync). That channel does not exist yet. |
| **Speed modes** | ⚠️ naming mismatch | The prototype has *typing speeds* (sekin / orta / tez). The design has *control modes*: **Qadam-baqadam** (wait after each field), **Oddiy** (full speed plus a 3 s summary at the end of each section) and **Tez**. All three are easy to build. Oddiy needs `section` tags in the mapping. We should adopt the design's modes and keep one hidden "taqdimot" typing speed for stage demos. Expect roughly 25–30 s for 48 fields in Oddiy (5 sections × 3 s, plus fill time). |
| **ERI stop** (Y16) | ✅ | Hard rules in the engine: it never clicks anything named or labelled ERI / imzo / E-IMZO / sign / submit / yuborish, or anything inside such a section. It never touches `type=password`, `type=file` or `.pfx/.p12/.key` inputs. A mapping that contains such a field is refused. At the end it highlights the sign button without clicking it ("Tayyor. Endi ERI bilan o'zingiz imzolang"). It makes no network calls and uses no `chrome.storage`; the handoff stays in panel memory only. |
| **Login stop** | ⏳ | The mock has no login page yet. In extension mode the user simply logs in first in their own browser. The extension only acts once the declaration page matches its mapping. |

**Unverified or risky assumptions in the spec and design**
- **Real ed2 selectors and layout.** Unknown. They must be captured by the owner in a real logged-in session; `mappings/ed2-real.TODO.json` documents how. No guessing (spec §9.8: fail closed).
- **E-IMZO / token.** We never call it. Unverified: whether its signing dialog is a page modal or a native OS window, and whether E-IMZO works inside a *non-browser* host (Electron/Tauri). The second point is the main technical risk of the desktop-app plan. The design's outside label "Bu oyna kabinetniki" can't be placed reliably over a native dialog.
- **Anti-bot.** Our events have `isTrusted=false`. If ed2 ignores untrusted input, the only browser-side fallback is the `chrome.debugger` permission, which produces trusted input but shows a yellow "being debugged" bar. Playwright sets `navigator.webdriver`, which is detectable. That is one more reason not to use Playwright against the real site.
- **Session expiry and captcha.** Unknown. The engine must treat "page no longer matches the mapping" (for example a redirect to login) as a stop, and treat any captcha as "your turn".
- **"Saqlash" (save draft).** The guard currently allows clicking it. We need a policy decision (see §4 questions).
- **Legal.** Whether automating ed2 is allowed (spec §9.1), possible broker-activity exposure (§9.2), and Chrome Web Store policy for gov-site automation are all open. Public demos stay on the mock.

## 2. Stack decision

| | **MV3 browser extension** | Electron + Playwright | Tauri + system webview | Server-side Playwright |
|---|---|---|---|---|
| ERI / E-IMZO | Stays in the user's own browser, where it already works | Embedded Chromium; E-IMZO compatibility ❓ | WebView2/WebKit; E-IMZO compatibility ❓ | ❌ the token is a USB device on the user's PC; the server can't sign |
| Passwords and keys seen by YuklaGo | Never (guard, narrow host permissions) | The app controls the whole page, so users must trust it | Same as Electron | ❌ would need credentials on the server, which breaks Y16 |
| Install friction | Low (Web Store or unpacked; Chrome, Edge, other Chromium browsers ❓) | High (~100 MB, code signing, SmartScreen, auto-update) | Medium (~10 MB, signing) | None for the user |
| Trusted input / anti-bot | Untrusted events; `chrome.debugger` as fallback | Trusted (CDP), but detectable as automation | Untrusted (JS injection) | Detectable |
| Matches the design's "viewport + rail" | Rail = side panel; the real URL bar is the browser's own | Yes, exactly | Yes | n/a |
| Mobile | ❌ | ❌ | ❌ | ❌ (signing needs the token anyway) |
| Built today | ✅ working, tested | Runner only (demo recording) | ❌ | ❌ |

- **Demo (19 Nov): the MV3 extension on the mock.** The YuklaGo panel sits beside the mock tab. The Playwright recording (`autofill/demo/toldirish-demo.mp4`) is the stage fallback. Optionally, the web team can embed the same mock in an iframe inside the web app and run the same `filler.js` on it, which gives the exact two-pane board look with no install.
- **After the hackathon: the extension as the only filing client.** It keeps ERI and E-IMZO in the browser where they already work, has the smallest attack surface and the lowest install friction, and auto-updates through the store. Consider Tauri or Electron only if the extension route is blocked, for example by ed2 rejecting untrusted input or by enterprise browser policy. Rule out server-side Playwright. Mobile stays a status-and-handoff view, as the design already says.

## 3. Mock ed2 portal for the demo

**Pages and sections.** Built items are marked ✅, missing ones ⏳.
1. ⏳ **Simulated login** ("DEMO SIGNER", no password stored), so the "stop at login, your turn" beat can be shown.
2. ⏳ **Declarations list** with a "Yangi deklaratsiya" button.
3. ✅ **Import declaration form (IM 40)** in 7 sections: type, regime and post; parties (grafa 2, 8, 14); contract, invoice and Incoterms; transport and countries; goods lines with an add-row button (31–45); FX and payments (23, 47); sign zone. ⏳ Convert the sections to the design's **tabs** (Umumiy / Tomonlar / Transport / Tovar N / To'lovlar) so tab navigation gets exercised.
4. ✅ **Simulated signing modal** with an inert password and key-file field that the filler is proven not to touch. ⏳ After submit, a status page showing the number `DEMO/26111/0000123` (currently only a browser alert).
5. ⏳ **Presenter panel** (hidden route) to choose the scenario and reset.

**Labels.** Today: a permanent red banner reading "DEMO / NAMUNA — bu ed2.customs.uz emas", violet colours, no logos, 127.0.0.1. The design wants a magenta hatched frame, a **MASHQ** pill, `mashq.yuklago.uz`, and a diagonal UZ/RU watermark. ARCHITECTURE §9 says `demo-ed2.yuklago.uz`. **Pick `mashq.yuklago.uz` and the design's four marks, and keep the "bu ed2.customs.uz emas" text.**

**Scenarios.** Chosen with `?scenario=` or the presenter panel.

| Scenario | What happens | Status |
|---|---|---|
| **Green** | Full fill → read-back OK → stop → user signs (simulated) → registered → "released (simulated)" | ✅ up to the stop. ⏳ after submit |
| **Returned with error** | Format/logic check returns e.g. "44-grafa: muvofiqlik sertifikati yo'q" → feeds the Y19 reply-explainer board | ⏳ |
| **Read-back mismatch** | The page silently reformats or truncates a field (STIR) → the fill stops on that field | ✅ in a test (`runner/test-guard.js`). ⏳ as a presenter toggle |
| **Field not found** | "Layout v2" renames grafa 33 → design failure screen ("33-grafani topa olmadim") | ⏳ (the engine already reports not-found) |
| Yellow / red channel, payment pending → paid | ARCHITECTURE §9 state machine | ⏳ (optional) |

**How it connects.** The YuklaGo web app exports `handoff.v1` JSON (ARCHITECTURE §6.4; sample in `autofill/samples/`), and the extension panel loads it from a file or paste (✅). ⏳ Next: the web app sends the pack directly to the extension (`externally_connectable`), so there is no file juggling and draft edits can sync back. For the **status webhook** (`POST /api/mock-ed2/status`, §9 step 8), the mock must become a small server instead of a static site. The webhook must stay **mock-only**: the design rightly says YuklaGo gets no live data from customs, so in real mode the status comes from the user via Y19 paste or photo. Label webhook-driven statuses "mashq holati".

## 4. Changes to the automation-mode screens, and open questions

| Screen (PDF board) | Change |
|---|---|
| **Kabinetni to'ldirish: choose target** (Mashq / Haqiqiy / O'zim) | Replace "ed2.customs.uz · YuklaGo Desktop orqali" with "**YuklaGo kengaytmasi** orqali, o'z brauzeringizda". Add a check that the extension is installed and its version. Step 1 becomes "**Avval kabinetga o'zingiz kiring**" (YuklaGo does not open the login page). |
| **Session setup** (tezlik, 48 maydon, "Mashq sessiyasini boshlash") | Keep Qadam-baqadam / Oddiy / Tez. Show the mapping version ("xarita: mashq v1"). Make the field count dynamic (48 for 1 goods line; the prototype has 78 for 3). Keep the gate "only Siz tasdiqladingiz values"; the handoff JSON must then carry a per-field `confirmed` flag that the filler enforces (it doesn't today). |
| **Live fill** (28/48, "YuklaGo yozmoqda", per-field ✓) | In real mode the rail becomes the **side panel** and the viewport is the user's own tab. The in-page overlay stays limited to the ring, the tag and ✓, as the prototype already does. Each ✓ must mean a per-field read-back with normalisation. |
| **Paused / "Siz o'zgartirdingiz"** | Define the trigger: a real click or keypress inside the cabinet (not scrolling). Mark "Qoralamani ham yangilash" as dependent on the extension ↔ web channel. For the demo, show it on the mock only or hide it. |
| **ERI hand-off** ("Endi sizning navbatingiz") | Keep. Move "Bu oyna kabinetniki…" into the rail, because we can't label a native E-IMZO window. The mock's own sign dialog (with "Kalit paroli") must stay inert and clearly fake. |
| **Failure** ("33-grafani topa olmadim") | Fine. Map the tally to the engine's report (filled + verified / mismatch / not found / blocked). The "how to delete the partial cabinet draft" text for real ed2 is unknown, so mark it [v2 spec]. |
| **Session record** | Decide whether written **values** are stored, and where. The spec says "value category"; the design shows full values. Store locally by default and upload only on "Yordam xizmatiga ulashish" with consent. Label "Kabinet ko'rsatgan raqam" as user-confirmed. |
| **Mobile "telefonda emas"** and **Settings / security log** | Keep. In Settings, add "Kengaytma: v0.1 · ruxsatlar: faqat mashq.yuklago.uz (ed2 keyin)". |
| **Mock vs real note** | Change "needs YuklaGo Desktop" to "needs the YuklaGo extension; real mode is off until the legal question is answered". |

**Spec v2 edits:** §8.1/§8.2/Y14 change the filing client from desktop app to MV3 extension (desktop becomes a fallback option). Y15 adds per-field read-back, normalisation, and the interrupt rules. Y17 adds the scenario list, the domain `mashq.yuklago.uz`, and the webhook as mock-only. §6.4 handoff.v1 adds per-field provenance and confirmation plus `section` tags.

**Open questions for the team**
1. **Legal:** who asks a customs lawyer, and ideally the Customs Committee, whether user-supervised ed2 automation is allowed, and by when? Until then, is real mode hidden or shown as disabled?
2. **Real selectors:** who has a real ERI and cabinet and can record the ed2 declaration pages (with screenshots and DevTools) in a supervised session, without submitting anything?
3. **E-IMZO:** what does signing look like on ed2 today (page modal or native window, Windows only?). Does ed2 accept untrusted input events?
4. **"Saqlash" (save draft):** may the automation click it, or is that also "your turn"?
5. **Browsers to support:** Chrome and Edge only, or also other Chromium browsers common in UZ? Do we ship to the Chrome Web Store, or unpacked/enterprise only for the pilot?
6. **Demo look:** extension side panel next to the mock tab, the web app with an embedded mock iframe, or both?
7. **Log retention:** where do session logs with declaration values live (device or UZ server), and for how long?

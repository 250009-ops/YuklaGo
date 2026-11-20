# ed2 automation

DEC-23, DEC-28, spec §7, ADR 0002, ADR 0007. The fill engine is `packages/fill`. Electron and the MV3 extension host it. The server stores hashes.

## What is automated

| Step | Who |
|---|---|
| Read documents and propose fields | Worker via the AI port, then the user confirms |
| Suggest a code from the official list | AI port, user confirms. The stub suggests `8539520009` only if that code is in the allowed list |
| Calculate payments | `packages/calc` |
| Build the draft | API, from the grafa map |
| Open the cabinet | Desktop app. It does not type the password |
| Log in | User, on the cabinet origin |
| Type fields | Engine, visibly, one field at a time |
| Click Saqlash | Off unless `AUTOMATION_SAVE_DRAFT_CLICK` is on (Q-2, default off) |
| Sign, send, pay | User. Engine stops |
| Status | User pastes or types it. `CABINET_STATUS_READ` is off |

## Window

Two panes at ≥ 1024 px: cabinet view and a 360 px rail. The view shows the real URL. While filling, the rail says "YuklaGo toʻldirmoqda". Practice sessions show the MASHQ banner on every D- screen. Real sessions do not.

Practice domain: `mashq.yuklago.uz`. Banner copy:

- UZ pill "MASHQ". "Mashq rejimi — bu haqiqiy bojxona kabineti emas. Hech narsa bojxonaga yuborilmaydi."
- RU pill "УЧЕБНЫЙ РЕЖИМ". "Это не настоящий кабинет таможни. Ничего не отправляется."

Graphite only (`#E8EBF1` / `#C5CCD8` / `#14152B` / `#3A4256`). No magenta, hazard yellow, or saffron on the banner.

The mock has no password and no file input. Its sign control is inert during fill. After the user presses the practice "Imzoladim" on the rail, the mock may show a registration number `MASHQ-000127`. That number is practice data.

Real mode, flag off: the rail says "Tayyor — asoschi tasdiqlagach yoqiladi" and offers a field-by-field copy guide. The embedded view does not load ed2.

Real mode, flag on: the view loads `https://ed2.customs.uz` (EK10 target is `cargo.customs.uz` while `EXPORT_EK10_TARGET` says so, and that target is [UNVERIFIED]). A domain not on the allow-list replaces the view with a full stop screen.

## Mapping engine

Inputs:

- A confirmed draft: only fields with provenance `user_confirmed` or `official` may be typed. Suggestions are not typed.
- A mapping document keyed by grafa id, regime, and target (`mock` or `ed2` or `cargo`).

The mock mapping is written against `services/mock-cabinet`, whose fields follow `data/declarant/grafa-map.json` (IM40) or `grafa-map-ek10.json` (EK10). The ed2 mapping ships empty. Selectors are recorded in the Q-6 session (blocked: needs a key holder, written consent, nothing submitted). Guessing a selector is a defect.

Each mapping entry:

```json
{
  "grafa": "34",
  "target": "mock",
  "regime": "IM40",
  "selector": "[data-grafa='34']",
  "widget": "text",
  "normalise": "digits",
  "deny": false
}
```

`widget` is `text`, `select`, `date`, or `tab`. Unknown widgets fail closed.

The engine refuses a mapping that mentions a password, file input, or a control whose accessible name matches the deny list: sign, submit, pay, ERI, E-IMZO, imzo, yuborish, toʻlash, login, kirish. A unit test loads a hostile mapping and expects every action blocked.

## Loop

1. Wait until the page matches the mapping's ready selector. A login URL means stop and show D-02 "Endi sizning navbatingiz".
2. For each field, scroll it into view, focus it, type with input events, blur, wait 150 ms, read the value back.
3. Normalise before compare (spaces, comma decimals, date order). Mismatch stops on that field (D-03 read-back state).
4. A trusted click or keypress in the cabinet (`isTrusted === true`) pauses within the current field (D-04). Events the engine dispatched are untrusted. Do not use the Chrome debugger protocol to forge trusted events against ed2. That is a bypass (R58).
5. Field not found, or the page no longer matches: D-07 "Sessiya toʻxtadi".
6. Captcha, any unexpected modal: stop, user's turn.
7. After the last field: D-05. Highlight the cabinet's own sign control. Do not click it.

Speed on the live cabinet is step-by-step or ordinary (human-paced, about a field at a time, with a short pause at the end of each section). "Tez" is mock-only.

Space pauses only when focus is in the rail. Space inside a cabinet field types a space and also counts as user input, which pauses.

## Safety stops

D-05 copy, always visible, not counted in the 60-word body cap:

- "Endi sizning navbatingiz"
- "Siz oʻzingiz imzolab, oʻzingiz yuborasiz — faqat oʻz ERI kalitingiz bilan."
- "YuklaGo parol yoki kalit soʻramaydi. Soʻrashsa — firibgarlik."

The panel background is ink `#14152B` with a saffron rule. Saffron is not used anywhere else except the logo fold.

E-IMZO missing: D-06, then the extension fallback. `DESKTOP_EIMZO_COMPAT` and `DESKTOP_EIMZO_SIGNING` stay unverified until AC-14.8 passes on that OS.

## Local log and server hashes

The desktop log stores grafa, value, source, time, and read-back result. It does not store keystrokes from the login or sign dialog. On "Sessiyani tugatish" the profile and the log's secret-adjacent cache are wiped. The user can export the local log.

The server receives `FillEvent` rows with `valueHash` only. Uploading full session values is open (Q-5). Do not upload them.

## Extension fallback

Host permissions: mock origin always. ed2, ed1, and cargo only when the flag is on. The side panel is the rail. The same `packages/fill` code runs. The same deny list runs.

## Build acceptance (AC-14.8)

On Windows, then macOS, a key holder logs in to the mock and to ed2 with PFX, USB-TOKEN, and BAIK-TOKEN, and the signing dialog opens in the app window. Nothing is submitted. If the dialog does not open, that OS release must already switch to the extension and say so. This test is not run in CI.

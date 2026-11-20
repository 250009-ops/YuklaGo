# YuklaGo — brand review and 3 identity directions

*18 Nov 2026, Tashkent time (UTC+5). Brand designer. Inputs: `yuklago-spec-v2.md`, `design-v0.1/design-rationale.md`, `design-v0.1/yuklago-web-ui-v0.1.pdf` (28 pages, viewed with pdftoppm), `team-review/uiux.md`, the earlier mobile prototype (`/workspace/yuklago-design/`) and `apps/web-mobile-ui` tokens.*

**CEO summary (3 lines)**
1. v0.1 looks "unofficial" because of five fixable things: a warm beige "accountant's ledger" palette, a stock parcel icon as the logo, magenta hazard hatching on the demo, monospace money, and a font (IBM Plex Sans) whose oʻ/gʻ apostrophe is 0.6 em wide, so every Uzbek headline reads "O ʻ zingiz".
2. We made 3 new identities (logo, palette, type, app icon), all bank/fintech grade with no state emblems, seals or flag colours. Boards are in `/workspace/yuklago-brand/boards/`.
3. Recommendation: **B "Varaq"**, an indigo declaration-sheet mark with the Onest font. Files ready to drop in are in `/workspace/yuklago-brand/export/`, and tokens are in `team-review/brand-tokens.json`.

> **Update 18 Nov 2026, 03:50+ (Tashkent, UTC+5): direction B "Varaq" is approved and final.** The source of truth is now `/workspace/yuklago-brand/final/`:
> - `brand-guidelines.md` and `brand-sheet.png`
> - `logo/` (SVG, PNG, favicon `.ico`, app icons, and a new small-size mark for 16–32 px)
> - `tokens/` (`brand-tokens.json`, `tokens.css`, Tailwind v4 and v3 snippets, `contrast-report.md`)
> - `type-specimen.png` and `mock-mode-specimen.png`
>
> `team-review/brand-tokens.json` is now a copy of `final/tokens/brand-tokens.json` (v1.0; naming aligned with `ui-tokens.json`). Changes agreed with UI/UX:
> 1. Saffron `#F5B43C` is decorative only, used on ink (9.79:1) or indigo (5.83:1). It is never text or a standalone icon on white or canvas, and never carries white text.
> 2. `text.muted` is now `#5E6178` (6.07:1 on white, ≥ 5.16:1 on canvas, sunken and tint).
> 3. New `border.input` `#84899A` (3.48:1 on white) for any input whose outline is its only boundary. `line` and `strong` are decorative dividers only.
>
> Where older sections below disagree, the final files win.

---

## 1. Diagnosis: why v0.1 doesn't look official

Page numbers are PDF pages of `yuklago-web-ui-v0.1.pdf`.

**Palette**
- **p1, design system ("Calm ledger, not a cockpit").** The brief itself sets the wrong target: "a careful accountant's desk, not fintech or government". Warm paper `#F6F5F1` plus amber `#9A5B00` and brown-ish attention tones read as a paper notebook. Banks, Stripe and GOV.UK all use white or cool grey surfaces. Beige also lowers perceived contrast and makes screenshots look yellowed.
- **p20–p21, mock cabinet.** Magenta `#A3157A` diagonal hatching around the whole viewport, a full-width magenta "MASHQ REJIMI" band, a diagonal "MASHQ · HAQIQIY EMAS" watermark and a pink URL bar make four signals at once. This is the vocabulary of hazard tape and sandboxes. In demo screenshots, which are exactly what judges see, the loudest thing on screen says "fake".
- **p21.** A large yellow-on-black panel (`#F5C518` on ink) reads as a caution sign. Keeping a reserved "your turn" colour is a good idea, but at full-panel size it becomes construction signage.
- **Mixed action colours.** Per the UI/UX review (boards 06, 17 and 26), primary buttons are black on some screens, petrol on others and pink on the practice start. With no single action colour, the product has no brand authority.

**Logo**
- **p1 and every header (p7, p20).** The mark is an isometric cube in a rounded petrol square, which is effectively the stock "package" UI icon. It says "parcel / courier / kargo", the very category we must not be confused with. It is also unownable: dozens of logistics apps use it.
- The wordmark is IBM Plex Sans with "Go" switched to petrol. That is a default font with a colour toggle, with no drawing in it. At 16 px in the header the brand is effectively invisible.

**Type**
- **Root cause of the oʻ/gʻ bug (measured).** In IBM Plex Sans, U+02BB (ʻ) has an advance width of **0.60 em, wider than the letter "o" (0.56 em)**. Onest and Inter use about 0.26 em. That is why p1 ("O ʻ zingiz topshiring", "To ʻ lovlar"), p7 ("O ʻ zingiz topshirish uchun…") and p20 ("To ʻ xtadim") all show a gap on both sides of the apostrophe. The proof is `/workspace/yuklago-brand/font-test.png`. Broken Uzbek is the single strongest "amateur" signal to an Uzbek reader.
- **p7 and p20.** Money is set in IBM Plex Mono ("≈ 67 823 600"). That reads as a developer console, not a bank statement. Use tabular figures of the UI font instead.

**Layout and finish**
- **p7.** Visible placeholders ("[N] kun", "Manba: [qonun muddati]", "[v2 spec]") and 10–11 px pills give a draft or prototype feel.
- **p1 and the landing boards (per UI/UX).** Boards are cut off or half empty, and a 48 px display headline on beige reads as a magazine, not a cabinet.
- Brand presence is only a 16 px header logo. There is no confident use of a brand colour anywhere (no hero, no primary surfaces), so nothing says "institution".

## 2. The 3 directions

All three use a white or cool-grey surface, one confident primary colour that passes AA with white text, a hand-built SVG mark with an outlined wordmark, and a mono version and app icon that work at 16 px.

**How all three avoid state cues.** None uses a circle or rosette (seal), a wreath, the Humo bird, a crescent, stars, the coat of arms or the flag stripes. None uses flag blue `#0099B5` or flag green `#1EB53A` as the brand system. There is no "Rasmiy" or "Oʻzbekiston Respublikasi" wording and no my.gov.uz or customs.uz layout. The marks are letter or object monograms, which is how private companies brand.

### A — "Yoʻl" (Route). Runner-up
- **Idea.** Two lanes (import and export) merge into one forward stem, forming a "Y". The left lane joins the right with a precise gap.
- **Palette.** Primary `#0A6650`, dark `#062F27`, accent `#2BD49A`. Neutrals `#0F1A17` / `#4A5853` / `#DCE3E0` / `#F2F5F4` / `#FFFFFF`. Status: success `#12805C`, warning `#A65A0A`, error `#C42B2B`, info `#2457A6`. White on primary: 6.9:1.
- **Type.** Manrope ExtraBold for the wordmark only (it has no U+02BB), Inter for the UI.
- **Why trustworthy.** It is the strongest silhouette at 16 px, and the green reads as money and "cleared". It is closest to the current app token `#0B6B4F`, so it is the cheapest migration.
- **Risks.** Green is crowded among Uzbek banks. A green primary collides with green "Tasdiqlangan" status.
- Board: `/workspace/yuklago-brand/boards/board-A-yol.png`

### B — "Varaq" (Sheet). **Recommended**
- **Idea.** A declaration sheet with a folded corner. A knocked-out "Y" runs its right arm into the fold, saying "your document, ready to send". Indigo is signing-ink blue. Saffron appears only in the fold and at the "your turn to sign" moment.
- **Palette.** Primary `#2E2BA0`, dark `#14143F`, accent `#F5B43C`. Neutrals `#14152B` / `#525570` / `#E1E2EC` / `#F5F5FA` / `#FFFFFF`. Status: success `#12795A`, warning `#A35C00`, error `#C0362C`, info `#2457A6`. White on primary: **10.7:1**.
- **Type.** Onest for the wordmark (SemiBold 680, outlined) and the whole UI (400/500/600/700, tabular numerals).
- **Why trustworthy.** The mark literally depicts the product, a declaration, not a parcel. Indigo plus white is Stripe or bank-grade, and it stays clear of the green, amber and red status colours.
- **Risks.** It can drift toward a generic "file" icon, so always keep the Y and the fold together. Indigo sits near Uzum's violet but is much deeper and bluer. At 16 px the fold becomes a small yellow dot (acceptable).
- Board: `/workspace/yuklago-brand/boards/board-B-varaq.png`

### C — "Ramka" (Frame)
- **Idea.** Two interlocking corner brackets (you and YuklaGo) frame one block of goods. It is square and stamp-like but deliberately not round, so it cannot read as a seal.
- **Palette.** Primary graphite `#15191E`, secondary `#0B6E68`, accent `#14A89D`. Neutrals `#59626B` / `#E1E4E7` / `#F4F5F6`. Status: success `#147A4F`, warning `#A0570B`, error `#BF2F2F`. White on secondary: 6.1:1.
- **Type.** Unbounded Medium wordmark ("yuklago", lowercase), Inter Tight for the UI.
- **Why trustworthy.** It is the most premium and neutral option, with no association to any bank or state brand.
- **Risks.** The mark resembles a "screenshot/crop" icon, and Unbounded feels a bit startup-ish. Turquoise is closer to flag blue, so never pair it with green and white stripes.
- Board: `/workspace/yuklago-brand/boards/board-C-ramka.png`

Side-by-side comparison: `/workspace/yuklago-brand/boards/overview-ABC.png`

## 3. Recommendation

Go with **B "Varaq"**:
1. It is the only mark that says "customs declaration", where the others are generic route or frame marks. It also directly replaces the v0.1 parcel, which said "courier".
2. Indigo keeps action and status colours separate. Option A's green primary would fight the green "Tasdiqlangan" chips.
3. One font (Onest) covers wordmark, UI, Latin, Cyrillic and a correct narrow ʻ. This fixes the P0 typography bug at its root.

Pick A instead only if the team strongly wants to keep green continuity with the current code. In that case, move the success colour away from the brand green.

---

## 4. Answers for UI/UX

These answer the five questions in `uiux.md` §5. Tokens are in `team-review/brand-tokens.json`.

**(1) Tone. Decided:** YuklaGo is a **serious financial tool, bank/fintech grade** (references: Stripe Dashboard, Wise, Uzbek bank apps). It is **not a government site** (no state look, emblems or seals; we are independent) and **not playful like Payme/Click** (no mascots, no bright gradients, no emoji tone). Write in plain, calm Uzbek; the seriousness comes from colour, type and alignment, not from bureaucratic language.

**(2) Primary colour. Petrol `#0B5563` is retired.** It is replaced by **indigo `#2E2BA0`** (hover `#24218A`, pressed `#1C1A70`, tint `#ECEBFA`, dark `#14143F`). Full token set:
- **Background:** canvas `#F5F5FA`, surface `#FFFFFF`, sunken `#EEEFF5`
- **Text:** ink `#14152B` (17.9:1), secondary `#525570`, muted `#5E6178` (6.07:1 on white; was #6B6E87), link `#2E2BA0`
- **Lines and focus:** line `#E1E2EC` and strong `#C5CCD8` are decorative dividers only; **input `#84899A`** (3.48:1) is for any input outline; focus ring `#2E2BA0`
- **Status (each one also gets an icon and a word):**

  | Status | fg | bg | border |
  | --- | --- | --- | --- |
  | Success | `#12795A` | `#E7F5EF` | `#B7DFCC` |
  | Warning | `#A35C00` | `#FFF4E0` | `#F0D3A0` |
  | Error | `#C0362C` | `#FDECEA` | `#F3C1BC` |
  | Info | `#2457A6` | `#EAF1FB` | `#C3D5EF` |

  Every fg/bg pair is at least 4.7:1.
- **Your turn (ERI login/sign):** bg `#14152B`, accent `#F5B43C`, text `#FFFFFF`. Use it at panel-header or button scale only, never as a full-screen yellow.
- **Saffron rule:** `#F5B43C` is decorative only, on ink (9.79:1) or indigo (5.83:1). It is never text or a standalone icon on white or canvas (1.83/1.68:1), and never carries white text.
- **Buttons:** one primary (indigo), one secondary (white with a `#C5CCD8` border and ink text), one destructive (`#C0362C`). No black or pink buttons.
- **Flag colours:** none of them are in the brand system.

**(3) Font.** Use **Onest** (Google Fonts, OFL), weights 400/500/600/700, `font-variant-numeric: tabular-nums` for soʻm amounts. Mono (JetBrains Mono) is only for TIF TN codes, grafa IDs and URLs.
- **Test:** `/workspace/yuklago-brand/font-test.png` (plus `@2x` and `.html`) renders "Oʻzbekiston, gʻaltak, bojxona toʻlovi" at 32 px and 16 px in Onest, Inter, IBM Plex Sans, Noto Sans and Manrope (control), including the ‘ U+2018 and ' U+0027 fallbacks.
- **Results:** Onest, Inter and Noto Sans are tight and crisp. IBM Plex Sans breaks ("O ʻ zbekiston") because its U+02BB is 0.60 em wide.
- **Rule:** store and display U+02BB. Normalise U+0027, U+2018, U+2019 and U+02BC to U+02BB in UI copy, and accept all of them in search and input.
- **Fallback stack:** `Onest, 'Noto Sans', system-ui, sans-serif`.

**(4) Logo status.** Direction **B "Varaq"** is recommended and pending Sarvarbek's yes.
- The wordmark is **one word in one colour, "YuklaGo"**. Drop the v0.1 "Yukla" ink + "Go" petrol split.
- Always use the outlined SVGs; never retype the wordmark.
- Files are in `/workspace/yuklago-brand/export/`:
  - `favicon.ico` (16/32/48) and `favicon-16.png` / `favicon-32.png` / `favicon-48.png` / `favicon.svg`
  - `app-icon-512.png`, `app-icon-192.png`, `app-icon-180.png` (= `apple-touch-icon.png`), `app-icon-1024.png`, `app-icon-maskable-512.png`
  - `mark*.svg`, `lockup-horizontal*.svg`, mono black/white
  - `palette.json`
- **Manifest:** set `theme_color` to `#2E2BA0`. The background colour can stay light.

**(5) Practice/demo mode.** Remove the magenta hatch frame, the diagonal watermark, the magenta band and the pink URL. Replace them with **one calm banner** pinned at the very top of the app, plus a small "MASHQ" pill in the cabinet's URL bar so any screenshot crop still shows it.
- **Tokens:** banner bg `#E8EBF1`, bottom border `#C5CCD8`, text `#14152B` (15:1), pill bg `#3A4256` with white text (10:1), optional 3 px `#3A4256` frame rule and a 4 % horizontal watermark. It is neutral graphite, deliberately not a brand or status colour. Final specimen: `/workspace/yuklago-brand/final/mock-mode-specimen.png`.
- **Copy (UZ):** pill **"MASHQ"**, then "**Mashq rejimi** — bu haqiqiy bojxona kabineti emas. Hech narsa bojxonaga yuborilmaydi." Link: "Haqiqiy rejim haqida".
- **Copy (RU):** "УЧЕБНЫЙ РЕЖИМ — это не настоящий кабинет таможни. Ничего не отправляется."
- **Sample:** `/workspace/yuklago-brand/export/practice-banner.png`
- Keep the `mashq.yuklago.uz` domain as the fourth, passive signal.

## 5. Files
- Boards:
  - `/workspace/yuklago-brand/boards/board-A-yol.png`
  - `/workspace/yuklago-brand/boards/board-B-varaq.png`
  - `/workspace/yuklago-brand/boards/board-C-ramka.png`
  - `/workspace/yuklago-brand/boards/overview-ABC.png`
- Per-direction SVG/PNG sets: `/workspace/yuklago-brand/A-yol/`, `B-varaq/`, `C-ramka/`
- Recommended export: `/workspace/yuklago-brand/export/`
- Uzbek explainer for Sarvarbek: `/workspace/yuklago-brand/brand-options.md`
- Font proof: `/workspace/yuklago-brand/font-test.png`
- Tokens: `/workspace/hackathon/team-review/brand-tokens.json`

**Spec v2 copy guard:** brand lines must not say "we file for you", "automatic filing" or "replaces the broker". The safe tagline used on the boards is "Bojxona deklaratsiyasini oʻzingiz topshiring".

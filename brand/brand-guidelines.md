# YuklaGo brand guidelines v1.0, direction B "Varaq"

*Approved 18 Nov 2026 (Tashkent, UTC+5). Source of truth: `final/tokens/brand-tokens.json`. One-page summary: `final/brand-sheet.png`.*

**Tone.** YuklaGo is a serious financial tool, at the level of a bank or fintech product.
- It is not a government site.
- It is not a playful wallet app like Payme or Click.

The tone comes from colour, type and alignment, never from emblems.

## 1. Logo

The mark is a declaration sheet with a folded corner. A knocked-out "Y" runs its right arm into the fold. The wordmark "YuklaGo" is Onest at weight 680, outlined, and always one word in one colour.

| Asset | When to use |
|---|---|
| `logo/svg/lockup-horizontal-*.svg` | Default (headers, documents) |
| `logo/svg/lockup-stacked-*.svg` | Square spaces, splash screens, social avatars |
| `logo/svg/mark-*.svg` | Mark alone at 40 px and larger |
| `logo/svg/mark-small-*.svg` and `lockup-horizontal-small-*.svg` | **16–32 px** (favicon, tabs, compact headers) |
| `logo/favicon/*`, `logo/app-icon/*` | Browser and app platforms. Set `theme_color` to `#2E2BA0` |

Each logo comes in four colour variants:
- `color` (on white or canvas)
- `on-dark` (on indigo-950 `#14143F` or ink `#14152B`)
- `mono-black`
- `mono-white`

**Small-size mark.** At 16–32 px the tile *is* the sheet. The fold is bigger (24/64), the Y is thicker (12/64), and there are no hairline gaps. In colour the Y is painted white, so the mark also works on dark browser tabs. The mono version keeps a 3.5/64 gap around the fold.

**Clear space.** Keep at least x = ¼ of the mark's height on every side of the logo, which is about the size of the fold. The SVG artboards are cropped tight, so add this space yourself.

**Minimum sizes.**
| Asset | Minimum |
|---|---|
| Full mark | 40 px |
| Small mark | 16 px |
| Horizontal lockup | 32 px tall (use the `-small` lockup from 20 to 32 px) |
| Stacked lockup | 64 px wide |
| Print | Lockup ≥ 25 mm wide |

**Don't:**
- Stretch, skew, rotate or outline the logo, or add shadows or gradients.
- Recolour it outside the four variants, split "Yukla" and "Go" into two colours, or retype the wordmark.
- Put it inside a circle, ring, rosette, wreath or star frame, or anything else that reads as a **seal or stamp of the state**.
- Pair it with the **Uzbek flag colours or stripes**, the coat of arms, the Humo bird, a crescent or stars, or the my.gov.uz or customs.uz layouts and logos.
- Place it on busy photos or on saffron.

## 2. Colour

**Usage ratio on a screen:**
| Colour | Share |
|---|---|
| White and canvas | ~60 % |
| Ink and neutrals | ~25 % |
| Indigo (actions, links, brand moments) | ~10 % |
| Status colours | ~3 % |
| Saffron | ≤ 2 % |

**Core colours:**
| Token | Hex | Use |
|---|---|---|
| brand.primary (primary-700) | `#2E2BA0` | Primary buttons, links, focus, brand surfaces |
| primary-800 / 900 | `#24218A` / `#1C1A70` | Hover / pressed |
| brand.tint (primary-50) | `#ECEBFA` | Selected rows, tinted surfaces |
| brand.dark (primary-950) | `#14143F` | Dark brand surfaces |
| brand.accent (saffron) | `#F5B43C` | **Decorative only** (see the rule below) |
| text.ink / secondary / muted | `#14152B` / `#525570` / `#5E6178` | Text |
| bg.canvas / surface / sunken | `#F5F5FA` / `#FFFFFF` / `#EEEFF5` | Backgrounds |
| border.line / strong | `#E1E2EC` / `#C5CCD8` | **Decorative dividers only** |
| border.input | `#84899A` | Any control whose outline is its only boundary (3.48:1) |

**Status colours** (fg / bg / border):
| Status | fg | bg | border |
|---|---|---|---|
| go (success) | `#12795A` | `#E7F5EF` | `#B7DFCC` |
| caution (warning) | `#A35C00` | `#FFF4E0` | `#F0D3A0` |
| stop (error) | `#C0362C` | `#FDECEA` | `#F3C1BC` |
| info | `#2457A6` | `#EAF1FB` | `#C3D5EF` |

Always show status as an icon plus a word, never colour alone.

**Saffron rule.** `#F5B43C` is decorative or accent only, and appears only on ink `#14152B` (9.79:1) or indigo `#2E2BA0` (5.83:1). Examples are the logo fold and the "Endi sizning navbatingiz" (your turn) moment at ERI sign.
- Never use it for text or a standalone icon on white or canvas (1.83 / 1.68:1).
- Never put white text on saffron.
- Never use it to fill a button or as a warning colour. Warnings use caution `#A35C00`.

**No flag-colour system.** Brand colours never form the flag combination (blue `#0099B5` + white + green `#1EB53A` + red rules).

**Contrast.** Every recommended text/background pair meets WCAG AA (≥ 4.5:1), and every UI boundary meets ≥ 3:1. The build asserts this. The full list is in `tokens/contrast-report.md`. Key pairs:
| Pair | Ratio |
|---|---|
| White on primary | 10.66:1 |
| Ink on white | 17.92:1 |
| Muted on white / canvas / sunken / tint | 6.07 / 5.59 / 5.29 / 5.16:1 |
| Status fg on status bg | 4.71–6.18:1 |
| Practice pill (white text on pill bg) | 10.03:1 |

On the primary scale, steps 500–950 take white text and steps 50–300 take ink text. **Step 400 takes neither**, so use it for graphics only.

## 3. Type

**Fonts.** Onest (Google Fonts, OFL) at weights 400/500/600/700. JetBrains Mono only for TIF TN codes, grafa IDs and URLs.

**Money.** Always use `font-variant-numeric: tabular-nums`.

| Token | px / line height | Weight | Use |
|---|---|---|---|
| display | 40/48, −0.02em | 700 | Landing page only |
| h1 | 28/36, −0.015em | 700 | Screen title |
| h2 | 22/30 | 600 | Section |
| h3 | 18/26 | 600 | Card title |
| bodyLg | 18/28 | 400 | Intro text |
| body | 16/24 | 400 | Default |
| bodySm | 14/20 | 400 | Tables |
| label | 14/20 | 500 | Labels (600 on buttons) |
| caption | 13/18 | 400 | Sources, help |
| overline | 12/16, +0.06em, uppercase | 600 | Pills |
| amountXl | 32/40 | 700, tnum | Total to pay |
| amount | 16/24 | 600, tnum | Line amounts |
| code | 14/20, mono | 400 | Codes, URLs |

**The oʻ / gʻ rule.**
- **Content:** always use U+02BB (ʻ) in oʻ, gʻ, Oʻ and Gʻ. The tutuq belgisi (as in maʼlumot) is U+02BC (ʼ).
- **When a user types it:** after o, O, g or G, replace `'` (U+0027), `‘` (U+2018), `’` (U+2019), `ʼ` (U+02BC) and `` ` `` with U+02BB. Regex: `/([oOgG])['\u2018\u2019\u02BC`]/g → "$1\u02BB"`.
- **Search:** fold every variant to U+02BB before comparing.
- **Font:** never use IBM Plex Sans. Its U+02BB is 0.60 em wide and renders "O ʻ zingiz".

Proof: `final/type-specimen.png` (with 16 px rows; `@2x` for zoom) and `../font-test.png`.

## 4. Practice (mock) mode

Practice mode uses **one calm, neutral signal**, specimen in `final/mock-mode-specimen.png`:

1. **Banner.** Pinned at the very top of the app, always visible and not dismissible. Background `#E8EBF1`, bottom border `#C5CCD8`, text `#14152B` (15:1), link `#2E2BA0`.
   - **UZ:** pill "MASHQ", then "**Mashq rejimi** — bu haqiqiy bojxona kabineti emas. Hech narsa bojxonaga yuborilmaydi." Link: "Haqiqiy rejim haqida".
   - **RU:** pill "УЧЕБНЫЙ РЕЖИМ", then "Это не настоящий кабинет таможни. Ничего не отправляется." Link: "О реальном режиме".
2. **Pill.** Background `#3A4256` with white text (10:1), 12/16 px, weight 600, uppercase. It appears in the banner and in the mock cabinet's URL bar.
3. **Optional rule.** A 3 px `#3A4256` top border on the mock cabinet frame, plus an optional horizontal watermark ("MASHQ · УЧЕБНЫЙ РЕЖИМ" in ink at 4 % opacity). Never diagonal.
4. **Domain.** `mashq.yuklago.uz` acts as a passive fourth signal.

**Never use** magenta or pink, hazard yellow, diagonal hatching, a diagonal watermark, or brand or status colours for practice mode. None of these elements appear in real mode.

## 5. Radius, spacing and shadow

- **Radius:**
  | Element | Radius |
  |---|---|
  | Chips | 6 |
  | Buttons and inputs | 10 |
  | Cards | 14 |
  | Sheets and modals | 20 |
  | Pills | 9999 |
  | App icon | 22.5 % |
- **Spacing:** a 4 px base with steps 4, 8, 12, 16, 20, 24, 32, 40, 48, 64 and 80. Page padding is 24–32 and card padding 16–20.
- **Shadows:** xs, sm, md and lg, all ink-tinted at 6–12 % (see the tokens). The focus ring is 2 px `#2E2BA0` with a 2 px offset.

## 6. Files
- `logo/`: `svg/`, `png/`, `favicon/` (`.ico` 16/32/48 plus 16/24/32/48 PNGs and an SVG), `app-icon/` (1024/512/192/180, `apple-touch-icon.png`, maskable 512/192).
- `tokens/`: `brand-tokens.json`, `tokens.css`, `tailwind.v4.css`, `tailwind.config.snippet.js`, `contrast-report.md`.
- `type-specimen.png`, `mock-mode-specimen.png`, `brand-sheet.png` (each with an `@2x` version).
- Build scripts: `build_final.py`, `tokens_build.py`, `sheets.py`, `sheet_brand.py`.

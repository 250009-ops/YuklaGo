# Design system

Brand name: Varaq. Do not redraw the logo. Files are in `brand/` and `packages/tokens/`. Guidelines: `brand/brand-guidelines.md`.

Visual reference, view only:

https://www.figma.com/design/MJCyZ6SiNj6HdesKbwxDcM/YuklaGo-%E2%80%94-Product-UI-v1.0

Implement from screen ID, copy, and states (`docs/screens.md`). The Figma review (`docs/sources/figma-review-v1.0.md`) found no blockers and 15 polish gaps. Where a frame disagrees with the spec or the screen hand-off, follow the spec. Known frame mistakes to avoid copying:

- RU frames that still show the language control as "Oʻzbekcha" (review P-01). The closed RU state reads "Русский".
- C-10 code card missing "Kodni siz tanlaysiz va javob berasiz." (P-02). The line is required.
- X- frames that drop the shipment header (P-03). Blocker cards sit in the shipment column and are not dismissible.
- X-07c titled as export while YG-0417 is a pre-arrival import (P-04).
- Saffron used as text or as a button fill. Saffron is the logo fold and the D-05 panel only.

## Tokens

Import `packages/tokens/tokens.css`. Tailwind v4 theme: `packages/tokens/tailwind.v4.css`.

| Token | Value | Use |
|---|---|---|
| brand primary / hover / pressed | `#2E2BA0` / `#24218A` / `#1C1A70` | The only filled button colour |
| on primary | `#FFFFFF` | |
| tint | `#ECEBFA` | |
| accent saffron | `#F5B43C` | Logo fold and D-05 only |
| ink / secondary / muted | `#14152B` / `#525570` / `#5E6178` | Muted text is not used on sunken or tint (contrast) |
| canvas / surface / sunken | `#F5F5FA` / `#FFFFFF` / `#EEEFF5` | |
| destructive | `#C0362C` | Account deletion primary on S-06 |
| go / caution / stop / info | `#12795A` / `#A35C00` / `#C0362C` / `#2457A6` | Always icon plus word |
| your-turn | ink background, saffron rule | D-05 only |
| practice banner | graphite set in the token file | D- screens in practice only |

Type: Onest for UI, JetBrains Mono for codes, grafa ids, and URLs. Scale from the token file: display 36/40, h1 28/34, h2 20/28, h3 16/24, body 16/24, caption 13/20. Amounts 14/20 with tabular numerals.

Space: 4, 8, 12, 16, 24, 32, 48, 64. Tap target at least 48 px. Radius: 4, 6, 10, 14, 20, pill.

Motion 120–180 ms. Honour `prefers-reduced-motion`.

## Components

Build `packages/ui` against these states. Names are the product names, not a second visual language.

- Button: primary, outline, text, destructive. One primary per view.
- Header: logo, nav, language menu (globe, current language, chevron, check on the open item), "Yordam", avatar. Signed-out header on C-01. "← Yuklar" on shipment screens.
- Stepper: five stages, same names in `docs/i18n.md`.
- Deadline chip: once, in the shipment header. "Topshiring 27.11 · chegara 28.11 · post taqvimi tasdiqlanmagan" on the demo.
- Source chip: act and date. Wraps. Does not stack one chip per full row.
- Status: icon and word. Tasdiqlangan is not used for a user confirmation.
- MASHQ banner: pinned, not dismissible, practice D- screens only.
- Sheets S-01–S-06 and info layers I-01–I-06: one component each, with the states in `docs/screens.md`.
- Console shell: ink top bar, no saffron. Left nav as in the screen hand-off for SP- and AD-.

## Layout

- Web: 1440 wide. Shipment content column about 720 px centred.
- Desktop fill: 1440 × 900, cabinet plus 360 px rail.
- Mobile: 390 × 844. One primary pinned to the bottom. Tables become cards.
- Console: 1440.

## Logo

Use the SVG files in `packages/tokens/logo`. Do not retype the wordmark. Clear space and minimum size are in `brand/brand-guidelines.md`. The title-bar mark is at least 16 px. No flag colours, seals, or emblems beside the logo.

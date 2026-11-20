# ADR 0007 — Live ed2 automation is the founder's switch

## Status

Accepted. DEC-24, PC-1.

## Context

No statute was found that bans or permits user-supervised automation of ed2. Huquq's reading is a conditional grey zone: the user logs in and signs with their own key, every field is visible, nothing is hidden, and no protection is bypassed (560-II art. 12). Doing it wrongly risks JK 278-2–278-4 and MJtK 155-1. The letter to the Customs Committee stays unsent. The founder talks to the officials.

## Decision

- `ED2_LIVE_AUTOMATION` defaults off. Copy while off: "Tayyor — asoschi tasdiqlagach yoqiladi".
- Turning it on needs the founder's confirmation and the DPO as second approver. An Admin cannot enable it alone.
- Until it is on, demos and the live path use the mock cabinet, plus a printable field-by-field guide for the real cabinet.
- The conditions (own login, own key, visible fill, no bypass) apply in both modes.
- "Tez" exists only on the mock (DEC-7).
- Clicking "Saqlash" is off (`AUTOMATION_SAVE_DRAFT_CLICK`, Q-2 still open).

## Consequences

- CI and pitch videos hit `mashq.yuklago.uz` only.
- Selectors for real ed2 are not guessed. They are recorded in the supervised Q-6 session, which is blocked until a key holder volunteers. The mapping file ships empty for `ed2`.

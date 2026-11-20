# Open questions

Copied from spec §11 and §3A.1 so the builder does not "close" them in the UI. Owners are the spec's owners. Nothing here is a timeline.

| Id | Question | Owner | How the product behaves until it is answered |
|---|---|---|---|
| Q-1 | Live ed2 automation and broker-activity status with the Customs Committee. The letter stays unsent | Hakathon CEO, with the founder | `ED2_LIVE_AUTOMATION` off. Mock and copy guide |
| Q-2 | May the engine click Saqlash? | CEO | `AUTOMATION_SAVE_DRAFT_CLICK` off. D-05 asks the user |
| Q-3 | Browsers and store versus unpacked extension | CEO | Extension documented as sideload fallback |
| Q-4 | Reminder channel | CEO | Web push and auth SMS. No Telegram product |
| Q-5 | May full session values be uploaded? | CEO and Huquq | Hashes only on the server |
| Q-6 | Live grafa and selector check. Blocked | CEO coordinates. Deklarant runs it | Flags in §3A.1. No guessed selectors. No demo claims on grafas 33, 41, 45, 47 |
| Q-7 | E-IMZO dialog shape on ed2 | Deklarant | AC-14.8. Fallback is the extension |
| Q-8 | Google Cloud DPA. Re-check VMQ 415 for DE/NL | Huquq | Live adapter stays off. Stub does not send data |
| Q-9 | Offer clauses 5.1–5.5 | Huquq | Do not present a draft clause as final |
| Q-10 | ZRU-764 art. 16 applicability, body, deadline | Huquq | Runbook says unverified. 3-year audit retention stays a proposal |
| Q-11 | Tariff flags (band edges, rounding, 300¹, kg, lists) | TIF TN | Flags default as in §3A.1. UI shows the uncertainty |
| Q-12 | Deklarant flags (EK10 target, fees, Set C) | Deklarant | No demo claim |
| Q-13 | Huquq flags (start day, storage, E-kontrakt penalty, bank list) | Huquq | Show both dates. Do not show an unsourced penalty |
| Q-14 | Gold case PE-22. Blocked | CEO coordinates. Deklarant compares | Demo stays "namuna" |
| Q-15 | Y4 interviews | CEO | Screen stays P2 and labelled taxminiy |
| Q-16 | Pilot value for max items per declaration | Deklarant | `MAX_ITEMS_PER_BYUD_N` unset. Warn above a pilot value only after it is set |
| Q-17 | Mobile tabs and offline capture | CEO | M-01–M-04 as drawn. Offline is X-05 for answers already on device |
| Q-21 warn-only | Spec applies warn-only and notes the CEO may still confirm it | CEO | Implement warn-only, as AC-1.18 states |

Closed in the spec, do not reopen in the product: Q-C1, Q-C2, Q-18, Q-19, Q-20, and the decision to turn auto-detect on (`CERT_PUBLIC_FIELDS_AUTODETECT`).

PC-1 through PC-16 in spec Appendix A are the legal gates. The behaviour column there is what the software does. PC-15 (named responsible person) blocks launch, not the demo build.

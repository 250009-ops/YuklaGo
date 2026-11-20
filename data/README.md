# Expert data

These files are inputs to the engines. Do not retype their numbers into components.

| Path | Use |
|---|---|
| `declarant/grafa-map.json` | IM40 draft and mock mapping. 46 grafa ids |
| `declarant/grafa-map-ek10.json` | EK10 draft. 45 grafa ids |
| `declarant/deadlines.json` | The 15 user clocks |
| `declarant/tolerances.json` | Proposal thresholds, not statute |
| `declarant/demo-sets/` | Synthetic sets A, B, and C with answer keys. Do not file them |
| `tariff/fees.json` | VMQ 55 bands and other fees |
| `tariff/tariff_demo.json` | Ten demo codes, including `8539520009` at 15% |
| `tariff/tiftn_codes_pq181_annex1.csv` | Official-list codes the engine may accept |
| `tariff/rules.md` | Narrative rules beside the JSON |

`declarant/_build/` is the script that produced the JSON. It is provenance, not a runtime dependency.

Demo totals for the screens are also fixed in `contracts/calc/golden-yg0412.json`. If a calculation change moves those totals, the screens and the hand-off have to change in the same review. Until PE-22, nothing here is "verified".

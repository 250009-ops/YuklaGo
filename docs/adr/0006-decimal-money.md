# ADR 0006 — Decimal money and provenance

## Status

Accepted. PE-19, PE-21, engineering review §1.3.

## Decision

- Persist money as `DECIMAL`. Transport it as strings. Never as JSON numbers.
- Every amount has a provenance: `official`, `estimate`, `document`, `user_confirmed`, `suggestion`, `missing`, or `sample`.
- A derived amount inherits the weakest input. A SOURCED rate may be "Rasmiy". The soʻm amount that multiplies that rate by an estimated customs value is "≈ Taxmin".
- Rounding of payment sums to the whole soʻm is [UNVERIFIED]. The flag `ROUNDING_MODE` defaults to half-up to the whole soʻm and the trace prints the mode. Grafa 45 to 2 decimals and grafa 46 to 3 decimals are SOURCED (Instruction 2773 cl. 25, sub-points 40–42).

## Consequences

- The golden fixture `contracts/calc/golden-yg0412.json` is the regression test for the demo screen.
- Totals on C-10, C-12, C-15, M-03, and I-01 use that fixture and the chip "Namuna" until PE-22.

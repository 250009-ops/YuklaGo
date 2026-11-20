# ADR 0004 — AI is a port, not a feature of this build

## Status

Accepted.

## Context

The product needs document reading, HS suggestions, and clarifying questions to feel complete. The founder will integrate the model. This build must still run the demo end to end.

## Decision

- Interfaces, job names, and result tables are in `contracts/ai/`.
- `AI_ADAPTER=stub` is the default. The stub returns the YG-0412 demo fields and does not call a network model.
- The worker is the only process that may call `AiPorts`. Routes enqueue a job and then read the result tables.
- Masking runs in Uzbekistan before any live call and fails closed.
- Calc, deadlines, tolerances, and go/no-go do not use the port.

## Consequences

- Swapping in Gemini is a new class behind the same interface plus `AI_ADAPTER=live`. HTTP shapes stay stable.
- Do not add a model SDK dependency while the adapter is `stub`.

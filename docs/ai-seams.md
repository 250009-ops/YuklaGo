# AI seams

The founder integrates the model. This repository defines the door and ships a stub so every screen works without one.

Read `contracts/ai/README.md`, `ports.ts`, `jobs.ts`, and `stub-adapter.ts`. ADR 0004.

## Ports

| Port | Job name | Result table | Stub behaviour |
|---|---|---|---|
| `PiiMasker` | runs inside the worker before any other job | not a table | Regex for PINFL-shaped and phone-shaped text. Identity-image hint fails closed |
| `DocumentClassifier` | `document.classify` | `Extraction` | Returns `INVOICE` |
| `FieldExtractor` | `document.extract` | `ExtractedField` | YG-0412 invoice fields, including net weight at confidence 0.55 so C-10 can ask the question |
| `HsCodeSuggester` | `hs.suggest` | `HsSuggestion` | `8539520009` if the caller passed that code in `allowedCodes` |
| `ClarifyingQuestionGenerator` | `questions.generate` | `ClarifyingQuestion` | First row of the specialist table the caller passed. It does not write a new question |
| `MessageParaphraser` | `message.paraphrase` | display string only | Returns the library text, or "Nomaʼlum xabar" |
| `DisplayTranslator` | `text.translate` | not written to a grafa | Returns the input unchanged |

Go/no-go, duty, VAT, the fee, deadlines, and tolerances are not ports.

## Where the founder wires the live adapter

1. Add `services/api/src/modules/ai/live-adapter.ts` implementing `AiPorts`.
2. Register it in the module provider when `AI_ADAPTER=live`.
3. Call Gemini only through Google Cloud, region Germany or the Netherlands (DEC-15). Do not call the OpenAI or Anthropic APIs.
4. Keep masking in front of the call. On `ok: false`, set the job to `FAILED_CLOSED` and do not open a socket.
5. Reject an extracted number that is not in the masked source.
6. Reject an HS code that is not in `allowedCodes`.
7. Do not send certificate HMACs.

The HTTP API does not change. Clients keep polling `GET /v1/ai/jobs/{jobId}` and then read fields from the shipment.

## Queue

Queue name `ai` (BullMQ). Envelope: `contracts/ai/jobs.ts`. The worker re-checks consent before it runs. No consent, or withdrawn consent, ends the job `FAILED_CLOSED` with `NO_CONSENT`.

`AiJob` stores ids and status. It does not store model request text or page bytes.

## Demo path with the stub

C-09 tick consent → upload the six sample filenames → worker runs classify and extract with the stub → C-10 shows the LED result, the low-confidence net weight, the missing certificate, and the three blockers. No outbound call. Tests assert the process makes no connection except to Postgres, Redis, and object storage on localhost.

## What not to build

- An OCR service, a vision SDK, or a hosted model key in `.env.example` beyond the empty `AI_LIVE_*` placeholders.
- A model that returns a duty amount, a freight quote, a yield norm, or a comparable price (AC-35.3, AC-22.3).
- Automatic confirmation of an HS code (AC-10.3).
- Risk "reasoning" that overrides `RequirementRule` or a BLOCK finding.

# AI seams (founder-integrated)

YuklaGo does not ship a model. These files are the only door.

| File | What it is |
|---|---|
| `ports.ts` | The interfaces. Document classification, field extraction, HS suggestion, clarifying questions, message paraphrase, display translation, and PII masking. |
| `jobs.ts` | The BullMQ job names and envelopes. |
| `stub-adapter.ts` | Returns the YG-0412 demo fields. No network call. |

## Where results live

| Job | Table (Prisma model) |
|---|---|
| `document.classify`, `document.extract` | `Extraction`, `ExtractedField` |
| `hs.suggest` | `HsSuggestion` |
| `questions.generate` | `ClarifyingQuestion` |
| `message.paraphrase` | Not a model output column. The API returns the library row. A paraphrase, if stored, is a display string on the response and is labelled "YuklaGo izohi, rasmiy kod emas". |
| `text.translate` | Not written into `DraftField`. Display only. |

`AiJob` stores status, adapter name, and refs. It does not store model request text, page images, or raw personal data. Masked model output is kept 30 days (`Extraction.rawKeptUntil`), then deleted. User-confirmed values stay with the shipment.

## How the founder swaps in a real model

1. Implement `AiPorts` in `services/api/src/modules/ai/live-adapter.ts`.
2. Call Gemini only through Google Cloud, EU region (Germany or the Netherlands). Do not call the OpenAI or Anthropic APIs directly (DEC-15). The Google Cloud DPA is [PENDING: Huquq].
3. Register the class where the API reads `AI_ADAPTER`. `stub` stays the default. `live` selects the new class. The HTTP routes do not change.
4. Mask on the Uzbekistan server before the call. If `PiiMasker.mask` returns `ok: false`, enqueue nothing and surface "qoʻlda kiriting".
5. Reject any extractor number that is not present in the masked source (`NUMBER_NOT_IN_SOURCE`).
6. Reject any HS code that is not in `allowedCodes` (`CODE_NOT_IN_LIST`).
7. Do not send certificate HMACs, PINFL, or passport images.

Go/no-go, duty, VAT, the fee, and deadlines are deterministic. They are not AI jobs. A model must not compute them.

Risk reasoning is not a port. Corridor and permit results come from `RequirementRule` rows and the flags in spec §3A.1. If the founder later wants a model to draft a comment, it goes through `MessageParaphraser` and cannot change a finding.

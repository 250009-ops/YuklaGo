# Documents, storage, and privacy

DEC-6, DEC-15, Y32, ADR 0005. This is not a privacy-policy draft for publication. The offer text is [PENDING: Huquq] (Q-9).

## Consent before reading

C-09, first shipment: the consent card is above the drop zone. The zone stays disabled until the box is ticked ("Avval rozilikni belgilang"). The box starts unticked. Returning users with a current consent do not see the card.

The consent text states, in 40 words or fewer, plus the ERI purpose line which is extra and not in that cap (AC-1.20):

- Processing by Google Gemini in the EU (Germany or the Netherlands) when the live adapter is on.
- Personal data is masked on a server in Uzbekistan first.
- Masked model output is kept 30 days.
- Passport and ID images are not stored.
- The stub adapter does not send documents anywhere. Say that when `AI_ADAPTER=stub`, so the consent is not a false claim. When the founder turns the live adapter on, the consent version changes and the user ticks again.

Store `ConsentRecord` with version, time, and a hash of the text (ZRU-547 art. 21). Withdrawal is in Settings. After withdrawal, new AI jobs are not enqueued. Already confirmed field values stay.

The ERI purpose line, shown with the consent:

"Imzolovchi oʻzgarmaganini tekshirish uchun ERI sertifikatingizdagi JShShIR va STIRni oʻqiymiz. Ular faqat shifrlangan hash koʻrinishida saqlanadi. Kalit va parolingizga tegmaymiz."

## Object storage

- Bucket in Uzbekistan. SSE encryption. TLS in transit.
- Key pattern: `companies/{companyId}/shipments/{shipmentId}/{documentId}`.
- The API returns a short-lived download URL to the owner only. Support never receives that URL. Support receives a rendered, masked preview.
- Checksum SHA-256 stored on the document row.
- Accepted types: PDF, JPG, PNG. Password-protected files fail with X-04.
- A classifier or a human reviewer that suspects a passport or ID image deletes the object and does not enqueue a job (AC-9.3). There is no face matching.

## Masking

The stub masker in `contracts/ai/stub-adapter.ts` replaces 14-digit PINFL-shaped numbers and `+998` phones. The founder replaces it with a stronger masker behind `PiiMasker`. Failure, or low confidence, is fail-closed: nothing is sent, the user sees "qoʻlda kiriting" (AC-32.3, AC-9.2).

Company STIR of an LLC is not personal data under the legal review's reading, but it is still masked before a model call because the model does not need it. A YaTT STIR is personal data.

The token-to-value table stays in Uzbekistan. It is not in `AiJob.inputRef`.

## Retention

| Data | Retention |
|---|---|
| Confirmed shipment fields and files | Kept with the shipment. After close, the owner can delete. Account deletion removes them |
| Masked model output | 30 days (`rawKeptUntil`), then the worker deletes it |
| Consent records | Kept after withdrawal so consent can be proved |
| Server audit log | `AUDIT_LOG_RETENTION_YEARS` default 3, proposal, not law, 🔒 |
| OTP codes | Hash only, deleted when consumed or expired |

Do not copy a "12 months after close" figure into the UI as if it were statute. The security review suggested 12 months as a product proposal. It is not in the spec as a decided rule. The owner controls deletion.

## Breach

Runbook, one page in the operator wiki when it exists:

- VMQ 415: 24 hours to notice a cross-border leak, 72 hours for the details, if that path is in use.
- ZRU-764 art. 16 applicability, the body to notify, and the deadline are [UNVERIFIED] (Q-10). Treat the duties as applicable in practice, as the security review did, and do not state a deadline the statute has not been shown to set.
- MJtK 46-2 part 2: unlawful processing of personal data using AI, 50–100 BHM. Mitigation is consent, masking, purpose limitation, and no model while the adapter is stub.

## Sharing with a broker

Y31 is optional. The owner sees who receives which fields before a share link is created. The link is token-hashed, 7 days, revocable, open count stored. A one-time code is required in addition to the link (security review G11). YuklaGo is not a party to the broker contract.

## Support and admin

Described in `docs/auth-rbac.md`. Admin has no route to objects. A test requests a document id with an admin token and expects 403.

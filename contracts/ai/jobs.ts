/**
 * Queue contract for founder-owned AI work.
 *
 * Transport: BullMQ on Redis, queue name `ai`.
 * The API enqueues. The worker calls AiPorts. The worker never imports a
 * model SDK; the live adapter does, and only the founder changes that file.
 *
 * Job names are stable. Do not rename them when the model changes.
 */

export const AI_QUEUE = "ai";

export type AiJobName =
  | "document.classify"
  | "document.extract"
  | "hs.suggest"
  | "questions.generate"
  | "message.paraphrase"
  | "text.translate";

export type AiJobEnvelope<T> = {
  jobId: string;
  name: AiJobName;
  enqueuedAt: string;
  /** Account that consented. The worker re-checks consent and fails closed. */
  accountId: string;
  shipmentId: string | null;
  /** Object keys and ids. Never file bytes, never raw PII. */
  input: T;
};

export type ClassifyInput = { documentId: string };
export type ExtractInput = { documentId: string; kind: string | null };
export type SuggestInput = { goodsItemId: string };
export type QuestionsInput = { goodsItemId: string; heading: string };
export type ParaphraseInput = { pastedText: string; locale: "uz" | "ru" };
export type TranslateInput = { text: string; from: "uz" | "ru"; to: "uz" | "ru"; shipmentId: string };

export type AiJobResult = {
  jobId: string;
  status: "SUCCEEDED" | "FAILED_CLOSED" | "CANCELLED";
  /** Table the worker wrote. The HTTP API reads that table, not the model. */
  storedIn:
    | "extractions"
    | "hs_suggestions"
    | "clarifying_questions"
    | "message_paraphrases"
    | null;
  storedId: string | null;
  errorCode:
    | "NO_CONSENT"
    | "MASK_FAILED"
    | "IDENTITY_IMAGE"
    | "NUMBER_NOT_IN_SOURCE"
    | "CODE_NOT_IN_LIST"
    | "ADAPTER_ERROR"
    | null;
};

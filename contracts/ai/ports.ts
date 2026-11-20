/**
 * Founder-owned AI ports.
 *
 * YuklaGo ships these interfaces and a stub adapter. The founder's team
 * implements the live adapter and registers it. Nothing in apps/ or
 * services/api may call a model SDK except through these ports.
 *
 * Hard rules (spec Y9, Y10, Y11, Y32, §6.3):
 * - The payment engine never calls these ports.
 * - A port never returns a money amount that was not already in its input.
 * - Raw PINFL, passport numbers, personal names, phones, signatures, seals,
 *   driver details and IBANs are masked on a Uzbekistan server before a
 *   live call. Certificate HMACs are never sent.
 * - If masking fails, the job ends FAILED_CLOSED and the user types the field.
 * - Passport and ID images are rejected before a job is enqueued.
 * - The user confirms every HS code. A port must not set chosenCode.
 */

export type Locale = "uz" | "ru";

export type MaskToken = {
  token: string;
  /** Class only. The value stays in the Uzbekistan token vault, not here. */
  class: "PERSON" | "PINFL" | "PHONE" | "PASSPORT" | "IBAN" | "SIGNATURE" | "STIR";
};

export type MaskResult =
  | { ok: true; maskedText: string; tokens: MaskToken[]; pagesKept: number[] }
  | { ok: false; reason: "LOW_CONFIDENCE" | "IDENTITY_IMAGE" | "NO_CONSENT" };

export interface PiiMasker {
  /** Deterministic first. The founder may add a NER model behind this same port. */
  mask(input: {
    documentId: string;
    text: string;
    pageImageRefs: string[];
  }): Promise<MaskResult>;
}

export type DocumentKind =
  | "INVOICE"
  | "PACKING_LIST"
  | "CMR"
  | "AWB"
  | "BILL_OF_LADING"
  | "RAIL_BILL"
  | "CONTRACT"
  | "ORIGIN_CERTIFICATE"
  | "CONFORMITY"
  | "WAREHOUSE_ACT"
  | "FREIGHT_INVOICE"
  | "PERMIT"
  | "OTHER";

export interface DocumentClassifier {
  classify(input: {
    documentId: string;
    maskedPageRefs: string[];
  }): Promise<{ kind: DocumentKind; confidence: number }>;
}

export type ExtractedFieldDraft = {
  name: string;
  value: string | null;
  confidence: number;
  page: number | null;
  bbox: [number, number, number, number] | null;
  sourceSnippet: string | null;
};

export interface FieldExtractor {
  /**
   * Returns fields from an already-masked document.
   * Must not invent amounts. Every numeric value must appear in the masked text.
   */
  extract(input: {
    documentId: string;
    kind: DocumentKind;
    maskedText: string;
    maskedPageRefs: string[];
  }): Promise<{ fields: ExtractedFieldDraft[] }>;
}

export type HsCandidate = {
  code10: string;
  officialNameUz: string;
  /** Deterministic signals, not the model's self-score. The stub uses fixtures. */
  signals: { name: string; detail: string }[];
};

export interface HsCodeSuggester {
  /**
   * Candidates MUST be a subset of the codes the caller passes in
   * (the official list slice). The port must not invent a code.
   */
  suggest(input: {
    goodsItemId: string;
    description: string;
    allowedCodes: { code10: string; officialNameUz: string }[];
  }): Promise<{ candidates: HsCandidate[] }>;
}

export interface ClarifyingQuestionGenerator {
  /**
   * Prefer the specialist question table. The live model may only
   * paraphrase a row from that table, never invent a new legal test.
   */
  questions(input: {
    goodsItemId: string;
    heading: string;
    table: { id: string; promptUz: string; promptRu: string }[];
  }): Promise<{ questionIds: string[] }>;
}

export interface MessageParaphraser {
  /**
   * Library first. If libraryId is null, return the unknown-message template.
   * Do not invent a grafa or a next step.
   */
  paraphrase(input: {
    libraryId: string | null;
    libraryTextUz: string;
    libraryTextRu: string;
    locale: Locale;
  }): Promise<{ text: string; disclaimer: "YuklaGo izohi, rasmiy kod emas" }>;
}

export interface DisplayTranslator {
  /** Display only. Output must not be written into a grafa. */
  translate(input: { text: string; from: Locale; to: Locale }): Promise<{ text: string }>;
}

export interface AiPorts {
  masker: PiiMasker;
  classifier: DocumentClassifier;
  extractor: FieldExtractor;
  hs: HsCodeSuggester;
  questions: ClarifyingQuestionGenerator;
  paraphraser: MessageParaphraser;
  translator: DisplayTranslator;
}

/** Wire format the API uses to choose an adapter. Default is stub. */
export type AiAdapterName = "stub" | "live";

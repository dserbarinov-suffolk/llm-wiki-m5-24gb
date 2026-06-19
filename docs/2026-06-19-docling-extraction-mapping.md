# Docling PDF Adapter - TDD (2026-06-19)

## Context & Problem

`DoclingExtractor` is the PDF adapter that uses Docling to read a `RawSource`.
`DocumentModel` is the structured document record that `DoclingExtractor` creates.
`DocumentElement` is one body, furniture, table, picture, code, or text item from `DocumentModel`.
`SourceSection` is one heading-scoped group of `DocumentElement` records.
`SourceChunk` is one token-bounded piece of one `SourceSection`.
`SourceSectionBuilder` is the component that creates `SourceSection` records from `DocumentModel`.
`SourceChunker` is the component that creates `SourceChunk` records from `SourceSection`.
`ExtractedUnit` is the domain object that feeds `PagePlan`.
`PagePlan` is the plan object that chooses wiki page writes.
`TextLayerPdf` is a PDF that passes the scanned-PDF text coverage check.
`ScannedPdf` is a PDF that fails the scanned-PDF text coverage check.
`ScannedPdfError` is the error for a PDF without usable embedded text.
`CorporateCaBundle` is `$HOME/.local/etc/corp-ca.pem`.
`ModelCache` is the user's Docling and Hugging Face model cache.
`PyMuPdfPipeline` is the PDF pipeline that uses `pymupdf4llm`, TOC page spans, and chunk packing.
`PyMuPdfPipeline` created a JavaScript Allonge chunk that mixed `Object.assign`, `Why?`, and `A Warm Cup`.
Docling preserves heading context and page provenance.
`SourceSectionBuilder` and `SourceChunker` must map Docling output into domain objects.

## Goals

- Use Docling as the default PDF extraction adapter.
- Map Docling output into `DocumentModel`, `DocumentElement`, `SourceSection`, and `SourceChunk`.
- Create `ExtractedUnit` records only from `SourceChunk`.
- Preserve page provenance from Docling in every `SourceChunk`.
- Exclude table-of-contents and furniture content from `ExtractedUnit`.
- Verify JavaScript Allonge separates `Object.assign`, `Why?`, and `A Warm Cup`.
- Document the corporate CA environment variables required for Hugging Face downloads.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not solve scanned whole-document OCR.
- This TDD does not add image interpretation.
- This TDD does not change `PagePlan`.
- This TDD does not change `WikiStructure`.
- This TDD does not add human review during ingest.
- This TDD does not add a new folder taxonomy.

Forbidden approaches:

- Do not feed Docling `HybridChunker` output directly into `ExtractedUnit`.
- Do not create `ExtractedUnit` records from table-of-contents content.
- Do not merge two `SourceSection` records into one `SourceChunk`.
- Do not use exported Markdown as the authority when `DocumentModel` contains the same data.
- Do not disable TLS verification for Hugging Face downloads.
- Do not require a remote Docling service.
- Do not require all `DocumentElement` records in one model context.

## Requirements

- `DoclingExtractor` must use Docling standard PDF conversion for PDF `RawSource` records.
- `DoclingExtractor` must use `do_ocr = false` for `TextLayerPdf`.
- `DoclingExtractor` must refuse `ScannedPdf` with `ScannedPdfError`.
- `DoclingExtractor` must retain `RawSource.source_locator` and source hash in `DocumentModel`.
- `SourceSectionBuilder` must set `DocumentElement.body_state = table_of_contents` for table-of-contents content.
- `SourceSectionBuilder` must exclude every `DocumentElement` where `body_state != body` from `SourceSection`.
- `SourceChunker` must split oversized `SourceSection` records without crossing a `SourceSection` boundary.
- `SourceChunker` must preserve code blocks and tables as indivisible units when they fit the token budget.
- Each `ExtractedUnit` must map from exactly one `SourceChunk`.
- `ExtractedUnit.heading_path` must equal `SourceChunk.heading_path`.
- `ExtractedUnit.locator` must render from `SourceChunk.page_start` and `SourceChunk.page_end`.
- `manifest.json` must persist the extractor name.
- `manifest.json` must persist one chunk record per `SourceChunk`.
- The cache must persist `document_model.json` and `source_sections.json`.

## Invariants

- `RawSource` remains immutable.
- `raw/` remains source evidence.
- `wiki/` remains generated knowledge.
- `ExtractedUnit` remains the only extraction object that `PagePlan` consumes.
- `Evidence` remains required for generated claims.
- `IngestRun` remains unattended.
- `IngestTopology` remains serial.
- `PageMetadata.PageId` remains page identity.
- `PagePath` remains a `WikiStructure` projection.
- `chunk_file(cache_dir, chunk_id)` remains the text source for one `ExtractedUnit`.

## Proposed Architecture

The PDF pipeline changes its extraction and section boundaries.
The planning and writing pipeline keeps the `ExtractedUnit` boundary.
Docling creates `DocumentModel`.
`SourceSectionBuilder` maps `DocumentModel` into heading-scoped `SourceSection` records.
`SourceChunker` maps each `SourceSection` into one or more `SourceChunk` records.
The session maps `SourceChunk` records into `ExtractedUnit` records.

```
+-----------+     +------------------+     +---------------+
| RawSource |---->| DoclingExtractor |---->| DocumentModel |
+-----------+     +------------------+     +-------+-------+
                                                   |
                                                   v
+-----------+     +------------------+     +---------------+
| PagePlan  |<----| ExtractedUnit    |<----| SourceChunk   |
+-----------+     +------------------+     +-------+-------+
                                                   ^
                                                   |
                                           +---------------+
                                           | SourceSection |
                                           +---------------+
```

`DoclingExtractor` owns Docling conversion and Docling pipeline options.
`DocumentModel` stores the structured extraction output.
`SourceSectionBuilder` removes elements where `body_state != body` and builds `SourceSection`.
`SourceChunker` creates budgeted `SourceChunk` records without crossing sections.
`ExtractedUnit` keeps the page-planning contract.
`PagePlan` chooses wiki page targets and writes.

## Key Interactions

`TextLayerPdf` flow:

```
RawSource -> scanned check -> DoclingExtractor -> DocumentModel
DocumentModel -> SourceSectionBuilder -> SourceSection
SourceSection -> SourceChunker -> SourceChunk -> manifest.json
SourceChunk -> ExtractedUnit -> PagePlan
```

Precondition: `RawSource.source_format` is `pdf`.
Function: the components create `DocumentModel`, `SourceSection`, and `SourceChunk`.
Postcondition: `PagePlan` receives `ExtractedUnit` records with one heading path each.

## Data Model

| Object | Contract | Required fields |
|---|---|---|
| `DocumentModel` | One extracted document with source identity, extractor identity, and ordered elements. | `source_locator`, `source_hash`, `extractor_name`, `extractor_version`, `elements`. |
| `DocumentElement` | One extracted item with kind, body state, text, markdown, heading path, and page span. | `element_id`, `element_kind`, `body_state`, `heading_path`, `page_start`, `page_end`, `text`, `markdown`. |
| `SourceSection` | One heading-scoped body section with ordered elements and page span. | `section_id`, `heading_path`, `page_start`, `page_end`, `elements`, `text`. |
| `SourceChunk` | One token-bounded part of one `SourceSection`. | `chunk_id`, `source_section_id`, `heading_path`, `page_start`, `page_end`, `text`, `token_estimate`. |
| `ExtractedUnit` | The page-planning input created from one `SourceChunk`. | `unit_id`, `raw_source`, `locator`, `heading_path`, `text`, `extraction_status`, `source_hash`. |

`DocumentElement.element_kind` values are `heading`, `paragraph`, `code_block`, `table`, `list_item`, `picture`, and `furniture`.
`DocumentElement.body_state` values are `body`, `furniture`, and `table_of_contents`.
`DocumentModel.extractor_name` is `docling`.

## APIs / Interfaces

- `llmwiki ingest <source>.pdf` uses `DoclingExtractor` by default.
- `llmwiki ingest <source>.pdf --reextract` rebuilds `DocumentModel`, `SourceSection`, `SourceChunk`, `manifest.json`, and chunk files.
- `ensure_extracted` returns `ExtractionResult`.
- `ExtractionResult.manifest.chunks` represents `SourceChunk` records.
- `chunk_file(cache_dir, chunk_id)` contains `SourceChunk.text`.
- `manifest.json` adds `extractor_name`.
- `document_model.json` stores `DocumentModel`.
- `source_sections.json` stores `SourceSection` records.
- The setup documentation must list `SSL_CERT_FILE`, `REQUESTS_CA_BUNDLE`, and `CURL_CA_BUNDLE` for Python Hugging Face clients.

## Behavior & Domain Rules

Rule: `SourceSection` controls semantic boundaries.

- Input: a PDF range with headings `Object.assign`, `Why?`, and `A Warm Cup`.
  Expected outcome: `SourceSectionBuilder` creates three `SourceSection` records.
- Input: `Object.assign` text followed by `Y Combinator` text under `Why?`.
  Expected outcome: the `Object.assign` `SourceSection` does not contain `Y Combinator`.
- Input: `Why?` text followed by string-literal text under `A Warm Cup`.
  Expected outcome: the `Why?` `SourceSection` does not contain string-literal content.

Rule: `SourceChunk` never crosses a `SourceSection`.

- Input: one small `SourceSection`.
  Expected outcome: `SourceChunker` emits one `SourceChunk`.
- Input: one oversized `SourceSection`.
  Expected outcome: `SourceChunker` emits multiple `SourceChunk` records with the same `source_section_id`.
- Input: two small adjacent `SourceSection` records.
  Expected outcome: `SourceChunker` emits separate `SourceChunk` records.

Rule: `body_state != body` content does not become source evidence.

- Input: Docling emits a table of contents under heading `CONTENTS`.
  Expected outcome: `SourceSectionBuilder` sets `body_state = table_of_contents`.
- Input: Docling emits a repeated page footer.
  Expected outcome: `SourceSectionBuilder` sets `body_state = furniture`.
- Input: `SourceSectionBuilder` emits `SourceSection` records.
  Expected outcome: no `SourceSection` includes `table_of_contents` or `furniture` elements.

Rule: page provenance flows through every object.

- Input: Docling reports `Object.assign` elements on pages 198 through 200.
  Expected outcome: the related `SourceChunk` has `page_start = 198` and `page_end = 200`.
- Input: the session creates an `ExtractedUnit` from that `SourceChunk`.
  Expected outcome: `ExtractedUnit.locator = p.198-200`.

Rule: code and tables keep their element boundary.

- Input: one code block fits within the token budget.
  Expected outcome: `SourceChunker` keeps the code block in one `SourceChunk`.
- Input: one table fits within the token budget.
  Expected outcome: `SourceChunker` keeps the table in one `SourceChunk`.
- Input: one code block exceeds the token budget.
  Expected outcome: `SourceChunker` emits one oversized `SourceChunk` and records an extraction warning.

Rule: the pipeline uses secure model downloads.

- Input: the corporate CA bundle exists at `$HOME/.local/etc/corp-ca.pem`.
  Expected outcome: setup docs instruct the user to set Python CA environment variables to that path.
- Input: Hugging Face access fails with a certificate error.
  Expected outcome: the error message names the CA bundle requirement.

## Acceptance Criteria

Milestone 1: pure mapping tests.

- Unit tests cover `DocumentModel`, `DocumentElement`, `SourceSection`, and `SourceChunk`.
- Unit tests prove `SourceSectionBuilder` creates separate sections for `Object.assign`, `Why?`, and `A Warm Cup`.
- Unit tests prove `SourceSectionBuilder` excludes `table_of_contents` and `furniture`.
- Unit tests prove `SourceChunker` does not merge adjacent `SourceSection` records.
- Unit tests prove `SourceChunker` splits one oversized `SourceSection` without changing heading path.
- Unit tests prove `SourceChunk` maps to `ExtractedUnit`.

Milestone 2: Docling adapter tests.

- Tests use a fake Docling conversion result for unit coverage.
- Tests prove `DoclingExtractor` passes `do_ocr = false` for `TextLayerPdf`.
- Tests prove `ScannedPdf` still raises `ScannedPdfError`.
- Tests prove `manifest.json` records `extractor_name = docling`.
- Tests prove `document_model.json` and `source_sections.json` are written under the source cache.
- Tests prove cache hits do not run Docling again.

Milestone 3: live JavaScript Allonge verification.

- `uv run pytest` passes.
- `uv run ruff check` passes.
- `uv run mypy src` passes.
- `uv run --project harness llmwiki ingest javascriptallonge.pdf --reextract` completes after Docling models exist in `ModelCache`.
- The JavaScript Allonge cache contains `document_model.json`, `source_sections.json`, `manifest.json`, and chunk files.
- The JavaScript Allonge manifest contains separate chunk records for `Object.assign`, `Why?`, and `A Warm Cup`.
- The `Object.assign` chunk text does not contain `Y Combinator`.
- The `Why?` chunk text does not contain `A Warm Cup`.
- The observation report still lists planned writes, created pages, enriched pages, and final page paths.

Milestone 4: documentation.

- Setup docs mention `SSL_CERT_FILE=$HOME/.local/etc/corp-ca.pem`.
- Setup docs mention `REQUESTS_CA_BUNDLE=$HOME/.local/etc/corp-ca.pem`.
- Setup docs mention `CURL_CA_BUNDLE=$HOME/.local/etc/corp-ca.pem`.
- Setup docs state that TLS verification must remain enabled.

## Cross-Cutting Concerns

Error handling:
The pipeline stops before `PagePlan` when Docling conversion fails.
The pipeline reports missing model files and certificate failures as extraction errors.

Observability:
The cache stores `document_model.json`, `source_sections.json`, `manifest.json`, chunk files, `page_plan.json`, and `observation.md`.
The final ingest log mentions the observation report path.

Performance:
`DoclingExtractor` uses no OCR for `TextLayerPdf`.
`SourceChunker` keeps model inputs bounded by section splits and `SourceChunk.token_estimate`.

## Reference Implementations

- PDF pipeline pattern: `harness/src/llmwiki/pdf/pipeline.py`.
- PDF chunking pattern: `harness/src/llmwiki/pdf/chunking.py`.
- PDF manifest pattern: `harness/src/llmwiki/pdf/manifest.py`.
- PDF adapter boundary: `harness/src/llmwiki/pdf/extractor.py`.
- Session mapping to `ExtractedUnit`: `harness/src/llmwiki/runtime/session.py`.
- PDF tests: `harness/tests/test_pdf_pipeline.py`.

## Alternatives Considered

- Keep `pymupdf4llm` as the default extractor.
  Rejected because it produced chunks that crossed semantic headings.
- Use Docling exported Markdown plus regex heading parsing.
  Rejected because `DocumentModel` has structured element and provenance data.
- Use Docling `HybridChunker` chunks as `ExtractedUnit`.
  Rejected because this would skip the `SourceSection` and `SourceChunk` contract.
- Enable Docling OCR for `TextLayerPdf`.
  Rejected because JavaScript Allonge does not need it and no-OCR conversion is faster.
- Disable TLS verification for Hugging Face downloads.
  Rejected because `CorporateCaBundle` solves the failure securely.

## Halt Conditions

- If Docling cannot provide page provenance for text elements, stop and ask.
- If Docling requires a remote service for local PDF extraction, stop and ask.
- If implementation needs TLS verification disabled, stop and ask.
- If JavaScript Allonge cannot separate `Object.assign`, `Why?`, and `A Warm Cup`, stop and report the extracted objects.
- If the implementation must change `PagePlan`, stop and ask.
- If the implementation must change `WikiStructure`, stop and ask.

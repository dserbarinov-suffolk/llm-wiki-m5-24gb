# Open Questions Awaiting Experimentation

Decisions deliberately deferred until a greater variety of sources exists —
per-source tuning now would be premature optimization. Each entry names the
experiment that resolves it. Resolved entries move to the bottom with the
outcome, so this file doubles as a decision log.

| # | Question | From | Experiment that resolves it | Status |
|---|---|---|---|---|
| 1 | **Figure-OCR thresholds.** Confidence ≥0.5 + ≥12 chars let photo noise through: on the first live extraction, 18 of 35 coffee-photo images passed (shop signage, an Italian newspaper) alongside exactly one genuine text-bearing figure (p.24, partial-functions notation). Damage is bounded by the `unverified` marker, but the signal-to-noise is poor. | PDF ingestion design | Ingest a screenshot/diagram-heavy PDF; measure precision/recall of `usable_text` filters; consider language/coherence heuristics only if the marker proves insufficient in practice. | Open — live data gathered 2026-06-11 |
| 2 | **Wiki churn / page granularity at book scale.** First live evidence (chunk 3): left unconstrained, the model gave every term a page (`undefined`, `nan`, ...) and exhausted its iteration budget before `finish_chunk`. Mitigated with a selectivity rule in the map prompt ("chapter page + at most 3 others") and a bigger iteration budget; whether the resulting granularity is *good* still needs the full-ingest review. | PDF ingestion design | Inspect the wiki and per-chunk transcripts after the first full `javascriptallonge.pdf` ingest; run `lint`; count rewrites per page and thin pages. | Open — live evidence 2026-06-11 |
| 3 | **Digest growth.** 20 chunks × ≤1.5K-char notes ≈ 30K chars (~7.5K tokens) approaches the integrate run's budget. | PDF ingestion design | Check the integrate transcript for compaction events; if phase ≥2 fires, add a two-stage reduce or lower the note cap. | Open |
| 4 | **Code-block extraction fidelity.** pymupdf4llm renders this book's code as italic/list fragments rather than fenced blocks; v1 ships the library defaults (the model summarizes, it doesn't need runnable code). Span-level font-aware fencing is designed but unbuilt. | PDF ingestion design | Read the chapter source pages after the full ingest: does the model misread code concepts because of mangled formatting? Only build custom span extraction if yes. | Open |
| 5 | **Scanned-PDF OCR quality.** Apple Vision returns plain text without layout; code-dense scans would lose indentation. The whole-document OCR path ships as detection + clean error. | PDF ingestion design | Acquire a scanned prose PDF; wire the existing TextRecognizer port to page rasters; judge readability. | Open — blocked on a real scanned source |
| 6 | **Header/footer and Leanpub-styling artifacts.** Page headers ("The first sip: Basic Functions 28") survive extraction and land mid-chunk. | PDF ingestion design | Human pass over 2–3 chapter source pages after ingest; if the model quotes headers as content, add deterministic repeated-line stripping. | Open |
| 7 | **Index scaling.** The flat index works at tens of pages; a few book ingests could push it past what the model scans well. | Local LLM-Wiki system design | Watch query quality as the page count grows past ~100; qmd (BM25/vector) is the designated upgrade. | Open |
| 8 | **Per-run server lifecycle.** Each CLI invocation loads the 8.4 GB model (~20–30 s). A 20-chunk ingest amortizes it (one boot per command), but bursts of queries do not. | Local LLM-Wiki system design | Measure actual boot overhead share across a week of usage before building a persistent-server mode (forge SlotWorker). | Open |
| 9 | **Terminal-in-batch swallows sibling failures.** Live (chunk 5): the model batched `write_page×3 + finish_chunk` in one turn; one write failed (invalid name `IIFE`) but `finish_chunk` succeeded, so the run ended before the model saw the error — page silently missing, notes over-claim. This is documented forge behavior (ADR-005). Mitigated with a system-prompt rule (finish tools only in a turn of their own); lint's "concepts mentioned but lacking a page" review is the catch-all. | Observed live, 2026-06-11 | Watch whether the prompt rule holds across future ingests; if violations recur, propose an upstream forge option (block terminal in mixed batches) rather than wrapping the runner. | Open — mitigated |

## Resolved

| # | Question | Outcome |
|---|---|---|
| R1 | Can the 14B reliably finish multi-step ingests? | Yes with forge's stack plus per-operation retry nudges that name the terminal tool (live failure 2026-06-10, fixed and regression-tested). |
| R2 | `embed_images` for PDF figures? | Rejected on measurement: one page went 258 → ~165K tokens (2026-06-11; see PDF ingestion design, Alternatives). |
| R3 | Is `javascriptallonge.pdf` text-layer or scanned? | Text: ~1,150 chars/page median; classifier margin is wide (2026-06-11). |

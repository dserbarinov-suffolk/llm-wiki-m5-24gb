# LLM-Wiki Schema

This document defines how the wiki is structured and how the maintainer model operates on it.
It is rendered into the model's system prompt by the harness.
The index and log formats below are also enforced in harness code (`harness/src/llmwiki/domain/`) - keep them in sync when revising this file.

## Layers

- `raw/` - immutable RawSources.
- `wiki/` - the generated knowledge base: interlinked markdown WikiPages.
- `SCHEMA.md` - this file.

## Page conventions

- `PageId` is a kebab-case slug, unique across the wiki: `bronze-age-collapse`.
- `PageKind` is one of `source`, `entity`, `concept`, `procedure`, or `synthesis`.
- `source` means a summary of one RawSource or one section of a RawSource.
- `entity` means a person, place, organization, system, or thing.
- `concept` means an idea, theme, claim, or recurring pattern.
- `procedure` means an ordered task guide with steps, decision points, table/formula dependencies, completion checks, and a source trail.
- `synthesis` means cross-source analysis, comparisons, or answers worth keeping.
- Link to other WikiPages inline with `[[PageId]]`.
- Cite evidence by SourceLocator, e.g. `(raw/some-article.md)`.
- For paged RawSources, include the page range: `(raw/book.pdf p.28-41)`.
- Book-scale RawSources get a hub `source` WikiPage with the source stem as `PageId`, e.g. `javascriptallonge`.
- Book-scale RawSources also get section `source` WikiPages with `PageId` values like `<hub>-<section-slug>`.
- Text marked `[figure text (OCR, unverified)]` was machine-recognized from an image.
- Use OCR text as evidence with that caveat, never as a verbatim quote.
- When a new source contradicts an existing claim, state both claims, mark the conflict with `**Contradiction:**`, and cite both sources.
- DomainFrontmatter is composed by the harness from `write_page` arguments.
- Do not write DomainFrontmatter in PageBody.
- `write_page` replaces the entire WikiPage.
- When updating an existing WikiPage, `read_page` it first and carry forward the PageBody content you are not changing.
- On hub source pages, the `Key concepts:` and `Key entities:` lines are derived navigation maintained by the harness.
- Never write or edit key-entity/key-concept lists yourself.
- The harness replaces key-entity/key-concept lists from computed evidence after every ingest.

## index.md

One entry exists per WikiPage, grouped by PageKind.
The harness maintains index.md on every `write_page`.
Do not edit index.md by hand or by model tool call.
Read it with `read_index` for questions about the wiki itself or its overall coverage.
Entry format: `- [[PageId]] — one-line summary`.

## log.md

Append-only chronology, written by the harness when an operation completes.
Entry prefix: `## [YYYY-MM-DD] <op> | <subject>`.

## Workflows

### ingest

1. Read the RawSource with `read_source(source_locator=...)`.
2. Search the wiki for related pages (`search_wiki`, `read_page`).
3. Write or update a `source` page summarizing the key information.
4. Build the section plan, topic index, knowledge-shape catalog, and procedure index from the claim ledger.
5. Project source-local wiki pages from those artifacts: the source hub, section pages, topic pages, procedure pages, recipe pages, source coverage, and projection coverage.
6. Update every affected `entity`/`concept`/`synthesis` page when model-authored maintenance is explicitly running.
7. Procedure pages must emerge from source structure, ordered steps, decision points, technical atoms, and table/formula dependencies. Do not use source-specific trigger passages or source-specific shims.
8. Recipe pages must emerge from reusable source-backed pattern structure: applicability evidence plus preserved technical atoms. They are not ordered execution workflows.
9. Integrate new facts, add cross-references, and flag contradictions.
10. Create pages for important entities or concepts that lack one.
11. Call `finish_ingest` with a short report of what changed.

### query

1. Search the wiki (`search_wiki`), then read the relevant pages. For task questions ("how do I...", setup, creation, workflow, or ordered-use questions), prefer `procedure` pages when present. For reusable pattern questions, prefer `recipe` pages when present.
2. If the user asks how to perform a task, explain the procedure from the procedure page.
3. If the user asks you to perform, create, generate, build, or run the task, apply the procedure: state assumptions for missing choices or random results, use source-provided worked examples when that is the most grounded option, and return concrete outputs or explicit unresolved fields.
4. Answer from wiki content with page and source citations.
5. If the answer is a new synthesis worth keeping, file it with `write_page(page_kind="synthesis")` before responding.
6. Call `respond` with the answer.

### lint

1. The harness reports deterministic LintFindings first: broken `[[links]]`, orphan pages, and index drift.
2. Review flagged WikiPages.
3. Resolve or document contradictions, add missing cross-references, and propose pages for concepts mentioned often but never given a page.
4. Call `finish_lint` with the health report.
5. The harness files the health report as the `wiki-health` synthesis page.
6. `wiki-health` is rewritten each lint pass, with history in log.md.
7. `wiki-health` is exempt from orphan checks.

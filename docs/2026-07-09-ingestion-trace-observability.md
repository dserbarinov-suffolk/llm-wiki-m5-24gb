# Ingestion Trace Observability TDD (2026-07-09)

## Context & Problem

The ingest pipeline writes durable artifacts for source plans, source structure, ledgers, topic state, page projections, staged pages, lint runs, publish runs, and provenance audits.
Those artifacts support root cause analysis, but an agent must know the pipeline before it can use them.
Experiments need one source-neutral trace that shows each stage input, output, decision, count, metric, and finding.

## Goals

- Write one `ingestion-trace.json` artifact for each source ingest.
- Show each major ingest stage in source order.
- Show each stage precondition result and postcondition result.
- Show stage counts, decisions, findings, and artifact pointers.
- Let engineers add or remove metric groups without changing the trace schema.
- Let `llmwiki inspect-ingest` read the trace without model calls.
- Keep raw sources immutable and wiki markdown disposable.

## Non-Goals & Forbidden Approaches

_Non-goals_:

- This design does not change page projection rules.
- This design does not change topic state admission.
- This design does not create a metrics database.
- This design does not compare two ingests.
- This design does not make generated wiki markdown canonical.

_Forbidden approaches_:

- Do not read generated wiki markdown to build the trace.
- Do not add source-specific metric branches.
- Do not branch on source titles, source phrases, or malformed source text.
- Do not make metric provider failure mutate accepted ledger state.
- Do not add compatibility reads for retired projection artifacts.

## Requirements

- The ingest pipeline must write `ingestion-trace.json` into the source ledger artifact directory.
- The portable artifact set must include `ingestion-trace-artifact`.
- The trace must use deterministic JSON serialization.
- The trace must include a stable artifact id and fingerprint.
- The trace must include every stage listed in this document.
- Each trace stage must include input artifact kinds and output artifact kinds.
- Each trace stage must include precondition checks and postcondition checks.
- Each trace stage must include summary counts when the source artifacts contain countable records.
- Each metric group must name one provider id.
- Each metric group must name the artifact kinds it read.
- The trace builder must accept a sequence of metric providers.
- A metric provider must return metrics and findings.
- A metric provider must not read files.
- A metric provider must not write files.
- A metric provider must not mutate domain records.
- The CLI must print the full trace summary by default.
- The CLI must print one stage when the caller passes `--stage`.
- The CLI must print canonical JSON when the caller passes `--json`.

## Invariants

- Raw sources remain immutable.
- The Ledger remains canonical accepted state.
- The Archive remains canonical source-derived artifact state.
- The Wiki remains generated markdown.
- The trace remains derived state.
- The trace never decides page admission.
- The trace never repairs pages.
- The trace never changes source artifacts.
- Metric providers use reusable source and domain categories.
- Production logic follows the Universal Standard.

## Proposed Architecture

```text
Ingest Pipeline
  |
  v
Artifact Bundle
  |
  v
Trace Builder ---- Metric Providers
  |
  v
Ingestion Trace Artifact
  |
  v
Artifact Writer
  |
  v
Inspect CLI
```

`Ingest Pipeline` creates source artifacts, ledger artifacts, topic state artifacts, and page projection artifacts.
`Artifact Bundle` passes parsed artifacts to the trace builder.
`Trace Builder` creates ordered trace stages and invokes metric providers.
`Metric Providers` compute one metric group from declared artifact inputs.
`Ingestion Trace Artifact` stores stages, metrics, findings, artifact pointers, and summary counts.
`Artifact Writer` writes the trace with the other source ledger artifacts.
`Inspect CLI` reads the trace and prints a human summary or JSON.

## Key Interactions

### Ingest Writes A Trace

```text
Session
  -> Ingest Pipeline: build source ledger
  -> Artifact Bundle: collect portable artifacts
  -> Trace Builder: build trace from artifacts
  -> Metric Providers: compute metric groups
  -> Artifact Writer: write ingestion-trace.json
  -> Artifact Writer: write portable-artifact-set.json
```

### Engineer Inspects A Trace

```text
Engineer
  -> Inspect CLI: inspect-ingest source.pdf
  -> WikiStore: read ingestion-trace.json
  -> Inspect CLI: render ordered stage summary
  -> Engineer: print counts, decisions, checks, findings
```

### Engineer Inspects One Stage

```text
Engineer
  -> Inspect CLI: inspect-ingest source.pdf --stage topic-state
  -> WikiStore: read ingestion-trace.json
  -> Inspect CLI: select stage topic-state
  -> Engineer: print checks, counts, metrics, findings
```

## Data Model

`IngestionTraceArtifact` records one source ingest trace.
It has source locator, source hash, run id, artifact format, artifact id, fingerprint, stages, metric groups, artifact pointers, and summary counts.

`IngestionTraceStage` records one pipeline stage.
It has stage id, label, input artifact kinds, output artifact kinds, precondition checks, postcondition checks, decisions, summary counts, and finding ids.

`IngestionTraceCheck` records one stage check.
It has check id, status, subject kind, subject id, and message.
Allowed statuses are `passed`, `warning`, and `failed`.

`IngestionMetricGroup` records metrics from one provider.
It has provider id, metric group id, source artifact kinds, metrics, and findings.

`IngestionMetric` records one measured value.
It has metric id, metric kind, value, unit, subject kind, and subject id.

`IngestionTraceFinding` records one diagnostic result.
It has finding id, severity, stage id, reason, subject kind, subject id, and message.
Allowed severities are `blocking`, `warning`, and `info`.

## APIs / Interfaces

`build_ingestion_trace` builds an `IngestionTraceArtifact` from parsed ingest artifacts and metric providers.

`IngestionMetricProvider` computes one `IngestionMetricGroup` from parsed artifacts.

`ingestion_trace_artifact_to_json` serializes an `IngestionTraceArtifact`.

`ingestion_trace_artifact_from_json` parses an `IngestionTraceArtifact`.

`llmwiki inspect-ingest <source>` prints the ordered trace summary.

`llmwiki inspect-ingest <source> --stage <stage-id>` prints one stage.

`llmwiki inspect-ingest <source> --json` prints the trace JSON.

## Behavior & Domain Rules

Rule: The trace builder records required stages in a fixed order.

- Input: artifacts include source plan, claim ledger, topic state, and page projection.
  Expected outcome: the trace includes stages from source plan through provenance audit.
- Input: a blocked write has no page projection artifact.
  Expected outcome: the page projection stage records a failed postcondition and the blocked diagnostic pointer.
- Input: a stage artifact is missing.
  Expected outcome: the stage records a failed postcondition and the trace still serializes.

Rule: Metric providers are optional extensions.

- Input: no metric providers.
  Expected outcome: the trace contains stages and no metric groups.
- Input: one provider returns page count metrics.
  Expected outcome: the trace contains one metric group for that provider.
- Input: the same provider is removed.
  Expected outcome: the trace omits that metric group and keeps the same schema.

Rule: The inspect CLI reads traces only.

- Input: `inspect-ingest javascriptallonge.pdf`.
  Expected outcome: the CLI reads `ingestion-trace.json` and prints stage summaries.
- Input: `inspect-ingest javascriptallonge.pdf --stage topic-state`.
  Expected outcome: the CLI prints only the topic-state stage.
- Input: `inspect-ingest missing.pdf`.
  Expected outcome: the CLI reports that no trace exists for that source.

## Acceptance Criteria

Milestone 1: Trace Domain Records

- Unit tests validate `IngestionTraceArtifact` fingerprinting.
- Unit tests validate allowed check statuses.
- Unit tests validate allowed finding severities.
- Unit tests validate deterministic JSON round trip.

Milestone 2: Trace Builder

- Unit tests build a trace from synthetic parsed artifacts.
- Unit tests prove required stages appear in fixed order.
- Unit tests prove missing stage inputs create findings.
- Unit tests prove a synthetic metric provider can be added without changing trace records.
- Unit tests prove removing a provider removes its metric group without breaking trace parsing.

Milestone 3: Ingest Integration

- `uv run llmwiki ingest javascriptallonge.pdf` writes `ingestion-trace.json`.
- `uv run llmwiki ingest "Sword World RPG - Complete Edition.pdf"` writes `ingestion-trace.json`.
- Each portable artifact set includes `ingestion-trace-artifact`.
- Each trace includes `topic-state` and `page-projection` stages.
- Each trace excludes retired artifacts.

Milestone 4: Inspect CLI

- `uv run llmwiki inspect-ingest javascriptallonge.pdf` prints ordered stage summaries.
- `uv run llmwiki inspect-ingest javascriptallonge.pdf --stage topic-state` prints topic-state counts, gaps, and findings.
- `uv run llmwiki inspect-ingest javascriptallonge.pdf --json` prints canonical trace JSON.

Milestone 5: Full Verification

- `uv run ruff check harness/src/llmwiki harness/tests` passes.
- `uv run mypy harness/src/llmwiki` passes.
- `uv run pytest harness/tests -q` passes.
- `uv run llmwiki graph --check` passes.
- `uv run llmwiki lint` passes or reports only non-deterministic quality review work.

## Cross-Cutting Concerns

Observability:
The trace gives deterministic observability for ingest experiments.
It records counts, decisions, checks, findings, and artifact pointers.

Error handling:
The trace builder records missing optional artifact inputs as findings.
It records missing required artifact inputs as failed postconditions.

Portability:
The trace uses canonical JSON and portable artifact pointers.
Other LLM-Wiki implementations can consume the trace without local file paths.

## Reference Implementations

- Artifact fingerprints: `harness/src/llmwiki/domain/ledger/canonical.py`
- Portable artifact sets: `harness/src/llmwiki/domain/ledger/artifacts.py`
- Artifact bundle writing: `harness/src/llmwiki/runtime/ledger_artifact_bundle.py`
- Staged flow records: `harness/src/llmwiki/domain/ledger/staged_contracts.py`
- CLI command routing: `harness/src/llmwiki/cli.py`

## Alternatives Considered

- Use `log.md`: rejected because logs do not preserve structured stage data.
- Use provenance audit only: rejected because provenance audit runs after publish.
- Use ad hoc `jq` recipes: rejected because agents must remember the pipeline.
- Store metrics in a database: rejected because local source artifacts are sufficient.
- Compute trace from wiki pages: rejected because wiki markdown is generated output.

## Halt Conditions

- If implementation needs generated wiki markdown to build the trace, stop and redesign.
- If implementation changes page projection admission, stop and split that work into another TDD.
- If implementation needs source-specific metric logic, stop and redesign the metric provider.
- If implementation needs compatibility reads for retired artifacts, stop and remove that dependency.
- If implementation cannot serialize the trace deterministically, stop and fix the artifact contract first.

"""Domain objects that describe wiki operations without filesystem effects."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import PurePosixPath

from llmwiki.domain.pages import (
    LOCAL_FLAT_STRUCTURE,
    PAGE_CATEGORIES,
    PageMetadata,
    WikiPage,
    WikiStructure,
)


def _source_format(source_locator: str) -> str:
    suffix = PurePosixPath(source_locator).suffix.lower().lstrip(".")
    if suffix == "md":
        return "markdown"
    return suffix or "unknown"


@dataclass(frozen=True)
class RawSource:
    source_locator: str
    source_format: str
    source_content: str = ""
    source_assets: tuple[str, ...] = ()
    immutable: bool = True

    @classmethod
    def from_locator(cls, source_locator: str) -> RawSource:
        return cls(source_locator=source_locator, source_format=_source_format(source_locator))


@dataclass(frozen=True)
class SourceBundle:
    raw_sources: tuple[RawSource, ...]

    def __post_init__(self) -> None:
        if not self.raw_sources:
            raise ValueError("SourceBundle requires at least one RawSource.")

    @classmethod
    def one(cls, raw_source: RawSource) -> SourceBundle:
        return cls(raw_sources=(raw_source,))


@dataclass(frozen=True)
class Schema:
    schema_id: str = "local-llm-wiki"
    page_kinds: tuple[str, ...] = PAGE_CATEGORIES
    page_metadata_fields: tuple[str, ...] = (
        "PageId",
        "PageKind",
        "Summary",
        "Sources",
        "Updated",
    )
    page_contracts: str = ""


@dataclass(frozen=True)
class ExtractionPrompt:
    instruction_text: str
    output_page_kinds: tuple[str, ...] = PAGE_CATEGORIES
    uncertainty_policy: str = "Use cited evidence and preserve contradictions."


@dataclass(frozen=True)
class Evidence:
    raw_source: RawSource
    locator: str = ""
    wiki_page: str = ""
    claim: str = ""


@dataclass(frozen=True)
class CrossReference:
    from_page: str
    to_page: str
    link_text: str = ""
    inbound_link_state: str = "linked"


@dataclass(frozen=True)
class Claim:
    statement: str
    claim_status: str = "supported"
    evidence: tuple[Evidence, ...] = ()
    wiki_page: str = ""


@dataclass(frozen=True)
class SourcePlan:
    raw_source: RawSource
    source_classification: str
    ingest_disposition: str
    target_page_metadata: PageMetadata | None = None
    target_page_paths: tuple[str, ...] = ()
    expected_wiki_pages: tuple[str, ...] = ()
    handling_notes: str = ""


@dataclass(frozen=True)
class IngestRun:
    source_bundle: SourceBundle
    wiki_structure: WikiStructure = LOCAL_FLAT_STRUCTURE
    schema: Schema = field(default_factory=Schema)
    extraction_prompt: ExtractionPrompt = field(
        default_factory=lambda: ExtractionPrompt("Apply the local ingest workflow.")
    )
    ingest_topology: str = "serial"
    source_plans: tuple[SourcePlan, ...] = ()
    wiki_pages: tuple[WikiPage, ...] = ()
    cross_references: tuple[CrossReference, ...] = ()
    evidence: tuple[Evidence, ...] = ()

    def __post_init__(self) -> None:
        if self.ingest_topology != "serial":
            raise ValueError("Local LLM-Wiki supports only serial IngestRun topology.")


@dataclass(frozen=True)
class QueryRun:
    user_question: str
    relevant_wiki_pages: tuple[str, ...] = ()
    answer_wiki_page: str = ""
    evidence: tuple[Evidence, ...] = ()
    cross_references: tuple[CrossReference, ...] = ()


@dataclass(frozen=True)
class LintFinding:
    finding_type: str
    wiki_page: str = ""
    claim: str = ""
    cross_reference: str = ""
    resolution_runs: tuple[str, ...] = ()


@dataclass(frozen=True)
class LintRun:
    lint_findings: tuple[LintFinding, ...] = ()
    suggested_query_runs: tuple[QueryRun, ...] = ()
    suggested_raw_sources: tuple[RawSource, ...] = ()
    wiki_pages: tuple[str, ...] = ()

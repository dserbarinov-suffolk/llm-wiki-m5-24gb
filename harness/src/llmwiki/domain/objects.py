"""Domain objects that describe wiki operations without filesystem effects."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import PurePosixPath

from llmwiki.domain.pages import (
    LOCAL_FLAT_STRUCTURE,
    PageMetadata,
    WikiPage,
    WikiStructure,
)
from llmwiki.domain.schema import PAGE_KINDS, PAGE_METADATA_FIELDS


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
class PageBodyContract:
    contract_id: str
    match_page_kinds: tuple[str, ...]
    required_sections: tuple[str, ...] = ()
    required_markdown_shape: str = "prose"
    min_claim_bullets: int = 0
    coverage_policy: str = ""
    max_words: int = 0
    max_source_word_ratio: float = 0.0
    max_copied_ngram_ratio: float = 1.0
    required_link_policy: str = "none"
    required_citation_policy: str = "none"
    required_uncertainty_policy: str = "none"


@dataclass(frozen=True)
class ResolvedPageBodyContract:
    contract_id: str
    required_sections: tuple[str, ...] = ()
    required_markdown_shape: str = "prose"
    min_claim_bullets: int = 0
    coverage_policy: str = ""
    max_words: int = 0
    max_source_word_ratio: float = 0.0
    max_copied_ngram_ratio: float = 1.0
    required_link_page_ids: tuple[str, ...] = ()
    required_source_citations: tuple[str, ...] = ()
    required_uncertainty_terms: tuple[str, ...] = ()


@dataclass(frozen=True)
class PageBodyFinding:
    finding_type: str
    detail: str


@dataclass(frozen=True)
class SourcePlanContractSelection:
    contract_id: str
    match_page_kinds: tuple[str, ...] = ()
    page_ids: tuple[str, ...] = ()
    max_words_override: int = 0
    max_source_word_ratio_override: float = 0.0
    max_copied_ngram_ratio_override: float = 0.0


def default_page_body_contracts() -> tuple[PageBodyContract, ...]:
    return (
        PageBodyContract(
            contract_id="source-summary",
            match_page_kinds=("source",),
            required_sections=("Source record", "Key supported claims"),
            required_markdown_shape="claim-bullets",
            min_claim_bullets=3,
            coverage_policy="main-supported-claims-and-explicit-limits",
            max_words=160,
            max_source_word_ratio=0.65,
            max_copied_ngram_ratio=0.50,
            required_link_policy="planned-related-pages",
            required_citation_policy="all-raw-sources",
            required_uncertainty_policy="preserve-source-uncertainty",
        ),
        PageBodyContract(
            contract_id="entity-page",
            match_page_kinds=("entity",),
            required_markdown_shape="prose",
            max_words=320,
            max_copied_ngram_ratio=0.80,
            required_link_policy="planned-related-pages",
            required_citation_policy="all-raw-sources",
            required_uncertainty_policy="preserve-source-uncertainty",
        ),
        PageBodyContract(
            contract_id="concept-page",
            match_page_kinds=("concept",),
            required_markdown_shape="prose",
            max_words=320,
            max_copied_ngram_ratio=0.80,
            required_link_policy="planned-related-pages",
            required_citation_policy="all-raw-sources",
            required_uncertainty_policy="preserve-source-uncertainty",
        ),
        PageBodyContract(
            contract_id="synthesis-page",
            match_page_kinds=("synthesis",),
            required_markdown_shape="prose",
            max_words=500,
            max_copied_ngram_ratio=0.80,
            required_link_policy="planned-related-pages",
            required_citation_policy="all-raw-sources",
            required_uncertainty_policy="preserve-source-uncertainty",
        ),
    )


def default_page_body_contract_by_page_kind() -> tuple[tuple[str, str], ...]:
    return (
        ("source", "source-summary"),
        ("entity", "entity-page"),
        ("concept", "concept-page"),
        ("synthesis", "synthesis-page"),
    )


def default_resolved_page_body_contract() -> ResolvedPageBodyContract:
    return ResolvedPageBodyContract(contract_id="default")


@dataclass(frozen=True)
class Schema:
    schema_id: str = "local-llm-wiki"
    page_kinds: tuple[str, ...] = PAGE_KINDS
    page_metadata_fields: tuple[str, ...] = PAGE_METADATA_FIELDS
    page_body_contracts: tuple[PageBodyContract, ...] = field(
        default_factory=default_page_body_contracts
    )
    page_body_contract_by_page_kind: tuple[tuple[str, str], ...] = field(
        default_factory=default_page_body_contract_by_page_kind
    )
    page_contracts: str = ""


@dataclass(frozen=True)
class ExtractionPrompt:
    instruction_text: str
    output_page_kinds: tuple[str, ...] = PAGE_KINDS
    uncertainty_policy: str = "Use cited evidence and preserve contradictions."


@dataclass(frozen=True)
class Evidence:
    raw_source: RawSource
    locator: str = ""
    page_id: str = ""
    claim: str = ""


@dataclass(frozen=True)
class CrossReference:
    from_page_id: str
    to_page_id: str
    link_text: str = ""
    inbound_link_state: str = "linked"


@dataclass(frozen=True)
class Claim:
    statement: str
    claim_status: str = "supported"
    evidence: tuple[Evidence, ...] = ()
    page_id: str = ""


@dataclass(frozen=True)
class SourcePlan:
    raw_source: RawSource
    source_classification: str
    ingest_disposition: str
    planned_page_write_ids: tuple[str, ...] = ()
    page_body_contract_selections: tuple[SourcePlanContractSelection, ...] = ()
    handling_notes: str = ""


@dataclass(frozen=True)
class ExtractedUnit:
    unit_id: str
    raw_source: RawSource
    locator: str
    heading_path: str
    text: str
    extraction_status: str
    source_hash: str = ""


@dataclass(frozen=True)
class CandidateClaim:
    claim_id: str
    statement: str
    evidence: Evidence
    confidence: float = 1.0


@dataclass(frozen=True)
class CandidateTopic:
    topic_id: str
    label: str
    candidate_claims: tuple[str, ...] = ()


@dataclass(frozen=True)
class CandidateEntity:
    entity_id: str
    label: str
    candidate_claims: tuple[str, ...] = ()


@dataclass(frozen=True)
class TopicCluster:
    cluster_id: str
    label: str
    extracted_units: tuple[str, ...]
    candidate_claims: tuple[str, ...] = ()
    candidate_topics: tuple[str, ...] = ()
    candidate_entities: tuple[str, ...] = ()


@dataclass(frozen=True)
class WikiMatch:
    page_id: str
    score: float
    match_reason: str
    page_excerpt: str = ""


@dataclass(frozen=True)
class ClaimComparison:
    candidate_claim: str
    existing_claim: str
    relation: str
    page_id: str = ""


@dataclass(frozen=True)
class ProjectionMetadata:
    page_metadata: PageMetadata
    page_path: str


@dataclass(frozen=True)
class PlannedPageWrite:
    write_id: str
    action: str
    page_metadata: PageMetadata
    extracted_units: tuple[str, ...] = ()
    evidence: tuple[Evidence, ...] = ()
    wiki_matches: tuple[WikiMatch, ...] = ()
    claim_comparisons: tuple[ClaimComparison, ...] = ()
    projection: ProjectionMetadata | None = None
    existing_page_id: str = ""
    resolved_page_body_contract: ResolvedPageBodyContract = field(
        default_factory=default_resolved_page_body_contract
    )


@dataclass(frozen=True)
class PagePlan:
    plan_id: str
    source_bundle: SourceBundle
    extracted_units: tuple[ExtractedUnit, ...]
    candidate_claims: tuple[CandidateClaim, ...]
    candidate_topics: tuple[CandidateTopic, ...]
    candidate_entities: tuple[CandidateEntity, ...]
    topic_clusters: tuple[TopicCluster, ...]
    wiki_matches: tuple[WikiMatch, ...]
    claim_comparisons: tuple[ClaimComparison, ...]
    planned_writes: tuple[PlannedPageWrite, ...]


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
    page_plan: PagePlan | None = None

    def __post_init__(self) -> None:
        if self.ingest_topology != "serial":
            raise ValueError("Local LLM-Wiki supports only serial IngestRun topology.")


@dataclass(frozen=True)
class QueryRun:
    user_question: str
    relevant_page_ids: tuple[str, ...] = ()
    answer_page_id: str = ""
    evidence: tuple[Evidence, ...] = ()
    cross_references: tuple[CrossReference, ...] = ()


@dataclass(frozen=True)
class LintFinding:
    finding_type: str
    page_id: str = ""
    claim: str = ""
    cross_reference: str = ""
    resolution_runs: tuple[str, ...] = ()


@dataclass(frozen=True)
class LintRun:
    lint_findings: tuple[LintFinding, ...] = ()
    suggested_query_runs: tuple[QueryRun, ...] = ()
    suggested_raw_sources: tuple[RawSource, ...] = ()
    page_ids: tuple[str, ...] = ()

    @property
    def is_clean(self) -> bool:
        return not self.lint_findings

    @property
    def broken_links(self) -> dict[str, tuple[str, ...]]:
        grouped: dict[str, list[str]] = {}
        for finding in self.lint_findings:
            if finding.finding_type == "broken link":
                grouped.setdefault(finding.page_id, []).append(finding.cross_reference)
        return {page_id: tuple(links) for page_id, links in grouped.items()}

    @property
    def orphan_pages(self) -> tuple[str, ...]:
        return tuple(
            finding.page_id
            for finding in self.lint_findings
            if finding.finding_type == "orphan page"
        )

    @property
    def missing_from_index(self) -> tuple[str, ...]:
        return tuple(
            finding.page_id
            for finding in self.lint_findings
            if finding.finding_type == "missing from index"
        )

    @property
    def stale_index_entries(self) -> tuple[str, ...]:
        return tuple(
            finding.page_id
            for finding in self.lint_findings
            if finding.finding_type == "stale index entry"
        )

    def render(self) -> str:
        if self.is_clean:
            return "No deterministic issues found (links, orphans, and index are consistent)."
        sections: list[str] = []
        if self.broken_links:
            lines = [
                f"- {page_id} links to missing page(s): {', '.join(targets)}"
                for page_id, targets in sorted(self.broken_links.items())
            ]
            sections.append("Broken [[links]] (target page does not exist):\n" + "\n".join(lines))
        if self.orphan_pages:
            sections.append(
                "Orphan pages (no inbound links from any other page):\n"
                + "\n".join(f"- {page_id}" for page_id in self.orphan_pages)
            )
        if self.missing_from_index:
            sections.append(
                "Pages missing from index.md:\n"
                + "\n".join(f"- {page_id}" for page_id in self.missing_from_index)
            )
        if self.stale_index_entries:
            sections.append(
                "index.md entries whose page does not exist:\n"
                + "\n".join(f"- {page_id}" for page_id in self.stale_index_entries)
            )
        return "\n\n".join(sections)

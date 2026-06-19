"""Global ingest planning: extracted units -> page plan.

This module is pure domain logic. It uses deterministic sparse text
embeddings, nearest-neighbor matching, and a small agglomerative clustering
pass so planning never depends on fitting a full source or full wiki into a
model context.
"""

from __future__ import annotations

import json
import math
import re
from collections import Counter
from dataclasses import asdict
from pathlib import Path

from llmwiki.domain.objects import (
    CandidateClaim,
    CandidateEntity,
    CandidateTopic,
    ClaimComparison,
    Evidence,
    ExtractedUnit,
    PagePlan,
    PlannedPageWrite,
    ProjectionMetadata,
    RawSource,
    ResolvedPageBodyContract,
    Schema,
    SourceBundle,
    SourceClaim,
    SourceClaimGroup,
    SourcePlanContractSelection,
    SourceSummaryPlan,
    TopicCluster,
    WikiMatch,
)
from llmwiki.domain.page_body_contracts import (
    contract_by_id,
    contract_for_page_kind,
    resolve_page_body_contract,
)
from llmwiki.domain.pages import PageMetadata, WikiStructure, parse_page, slugify

_TOKEN_RE = re.compile(r"[a-z][a-z0-9-]{2,}")
_HEADING_RE = re.compile(r"^#{1,6}\s+(.+)$", re.MULTILINE)
_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
_SOURCE_PAGE_BONUS = 0.15
_MATCH_THRESHOLD = 0.12
_CLUSTER_THRESHOLD = 0.18
_MAX_SOURCE_UNITS_PER_WRITE = 1
_MAX_SOURCE_CHARS_PER_WRITE = 6_000
_MAX_SOURCE_SUMMARY_CLAIMS = 5

_ROLE_PATTERNS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("uncertainty", (r"\bmay\b", r"\bmight\b", r"\bpossible\b", r"\bsuggest\w*\b", r"\bunknown\b")),
    (
        "negative-evidence",
        (r"\bno\b.+\bfound\b", r"\bnot\b.+\bfound\b", r"\bdoes not\b", r"\bwithout\b"),
    ),
    ("limitation", (r"\blimit\w*\b", r"\bunless\b", r"\bexcept\b", r"\bonly\b")),
    ("method", (r"\bused\b", r"\busing\b", r"\bstudy\b", r"\banalys\w*\b", r"\btest\w*\b")),
    ("evidence", (r"\bevidence\b", r"\binscription\w*\b", r"\bcitation\b", r"\brecord\b")),
    ("provenance", (r"\bfrom\b", r"\borigin\w*\b", r"\bretrieved\b", r"\bdiscovered\b")),
    ("temporal", (r"\b\d{3,4}\b", r"\bbc\b", r"\bad\b", r"\byear\b", r"\bcentur\w*\b")),
    ("quantitative", (r"\b\d+\b", r"\bat least\b", r"\bmore than\b", r"\broughly\b")),
    (
        "function",
        (r"\btrack\w*\b", r"\bpredict\w*\b", r"\badvance\b", r"\bshow\w*\b", r"\bcould\b"),
    ),
    ("mechanism", (r"\bconsists\b", r"\bgear\w*\b", r"\bcase\b", r"\bcrank\b", r"\bthrough\b")),
    ("comparison", (r"\bmatched\b", r"\bsurpass\w*\b", r"\bcompared\b", r"\bthan\b")),
    ("relationship", (r"\blink\w*\b", r"\bconnect\w*\b", r"\bbetween\b", r"\bwith\b")),
    ("requirement", (r"\bmust\b", r"\brequire\w*\b", r"\bshall\b", r"\bshould\b")),
    ("procedure", (r"\bturn\w*\b", r"\bstep\b", r"\bprocess\b", r"\bworkflow\b")),
    ("definition", (r"\bdefined as\b", r"\bmeans\b", r"\brefers to\b")),
    ("identity", (r"\bis\b", r"\bare\b", r"\bknown as\b", r"\bdescribed as\b")),
    ("attribute", (r"\bhas\b", r"\bhave\b", r"\bcontains\b", r"\bhoused\b", r"\bsize\b")),
    ("open-question", (r"\bopen question\b", r"\bunclear\b", r"\bunresolved\b")),
)

_ROLE_WEIGHTS = {
    "uncertainty": 0.33,
    "negative-evidence": 0.34,
    "limitation": 0.31,
    "method": 0.27,
    "function": 0.30,
    "mechanism": 0.25,
    "provenance": 0.22,
    "temporal": 0.18,
    "identity": 0.22,
    "definition": 0.22,
    "comparison": 0.20,
    "evidence": 0.20,
    "quantitative": 0.16,
}

_STOP_WORDS = frozenset(
    {
        "about",
        "after",
        "also",
        "and",
        "are",
        "because",
        "before",
        "between",
        "book",
        "but",
        "can",
        "chapter",
        "code",
        "does",
        "each",
        "from",
        "function",
        "have",
        "into",
        "javascript",
        "page",
        "pages",
        "raw",
        "section",
        "source",
        "that",
        "the",
        "their",
        "this",
        "through",
        "use",
        "using",
        "when",
        "where",
        "with",
    }
)


def build_page_plan(
    *,
    plan_id: str,
    source_bundle: SourceBundle,
    raw_source: RawSource,
    extracted_units: tuple[ExtractedUnit, ...],
    existing_pages: dict[str, str],
    wiki_structure: WikiStructure,
    today: str,
    schema: Schema | None = None,
    source_plan_contract_selections: tuple[SourcePlanContractSelection, ...] = (),
) -> PagePlan:
    resolved_schema = schema or Schema()
    source_claims = _source_claims(extracted_units, resolved_schema)
    source_claim_groups = _source_claim_groups(source_claims)
    candidate_claims = _candidate_claims_from_source_claims(source_claims)
    candidate_topics = _candidate_topics(extracted_units, candidate_claims)
    candidate_entities = _candidate_entities(extracted_units, candidate_claims)
    topic_clusters = _topic_clusters(
        extracted_units, candidate_claims, candidate_topics, source_claim_groups
    )
    wiki_matches = _wiki_matches(extracted_units, existing_pages, raw_source.source_locator)
    claim_comparisons = _claim_comparisons(candidate_claims, wiki_matches)
    planned_writes = _planned_writes(
        raw_source=raw_source,
        extracted_units=extracted_units,
        existing_pages=existing_pages,
        wiki_matches=wiki_matches,
        claim_comparisons=claim_comparisons,
        wiki_structure=wiki_structure,
        today=today,
        schema=resolved_schema,
        source_plan_contract_selections=source_plan_contract_selections,
        source_claims=source_claims,
        source_claim_groups=source_claim_groups,
    )
    return PagePlan(
        plan_id=plan_id,
        source_bundle=source_bundle,
        extracted_units=extracted_units,
        source_claims=source_claims,
        source_claim_groups=source_claim_groups,
        candidate_claims=candidate_claims,
        candidate_topics=candidate_topics,
        candidate_entities=candidate_entities,
        topic_clusters=topic_clusters,
        wiki_matches=wiki_matches,
        claim_comparisons=claim_comparisons,
        planned_writes=planned_writes,
    )


def build_markdown_page_plan(
    *,
    plan_id: str,
    source_bundle: SourceBundle,
    raw_source: RawSource,
    source_text: str,
    existing_pages: dict[str, str],
    wiki_structure: WikiStructure,
    today: str,
    schema: Schema | None = None,
    source_plan_contract_selections: tuple[SourcePlanContractSelection, ...] = (),
) -> PagePlan:
    resolved_schema = schema or Schema()
    title = _document_title(source_text, raw_source.source_locator)
    unit = ExtractedUnit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="document",
        heading_path=title,
        text=source_text,
        extraction_status="ok",
    )
    extracted_units = (unit,)
    source_claims = _source_claims(extracted_units, resolved_schema)
    source_claim_groups = _source_claim_groups(source_claims)
    candidate_claims = _candidate_claims_from_source_claims(source_claims)
    candidate_topics = _candidate_topics(extracted_units, candidate_claims)
    candidate_entities = _candidate_entities(extracted_units, candidate_claims)
    topic_clusters = _topic_clusters(
        extracted_units, candidate_claims, candidate_topics, source_claim_groups
    )
    wiki_matches = _wiki_matches(extracted_units, existing_pages, raw_source.source_locator)
    claim_comparisons = _claim_comparisons(candidate_claims, wiki_matches)
    planned_writes = _markdown_planned_writes(
        raw_source=raw_source,
        title=title,
        source_text=source_text,
        extracted_units=extracted_units,
        existing_pages=existing_pages,
        wiki_matches=wiki_matches,
        wiki_structure=wiki_structure,
        today=today,
        schema=resolved_schema,
        source_plan_contract_selections=source_plan_contract_selections,
        source_claims=source_claims,
        source_claim_groups=source_claim_groups,
    )
    return PagePlan(
        plan_id=plan_id,
        source_bundle=source_bundle,
        extracted_units=extracted_units,
        source_claims=source_claims,
        source_claim_groups=source_claim_groups,
        candidate_claims=candidate_claims,
        candidate_topics=candidate_topics,
        candidate_entities=candidate_entities,
        topic_clusters=topic_clusters,
        wiki_matches=wiki_matches,
        claim_comparisons=claim_comparisons,
        planned_writes=planned_writes,
    )


def page_plan_to_json(plan: PagePlan) -> str:
    return json.dumps(asdict(plan), indent=2, ensure_ascii=False)


def observation_report(plan: PagePlan) -> str:
    enriched = sum(1 for write in plan.planned_writes if write.action == "enrich-existing")
    created = sum(1 for write in plan.planned_writes if write.action == "create-new")
    contradictions = sum(1 for item in plan.claim_comparisons if item.relation == "contradiction")
    deferred = sum(1 for write in plan.planned_writes if write.action == "defer")
    paths = "\n".join(
        f"- `{write.page_metadata.page_id}` -> "
        f"`{write.projection.page_path if write.projection else ''}`"
        for write in plan.planned_writes
    )
    return (
        "# Ingest Observation Report\n\n"
        f"- ExtractedUnits: {len(plan.extracted_units)}\n"
        f"- TopicClusters: {len(plan.topic_clusters)}\n"
        f"- Pages enriched: {enriched}\n"
        f"- Pages created: {created}\n"
        f"- Contradictions: {contradictions}\n"
        f"- Deferrals: {deferred}\n\n"
        "## Final Page Paths\n\n"
        f"{paths}\n"
    )


def planned_write_message(
    write: PlannedPageWrite,
    units: dict[str, ExtractedUnit],
    source_claims: dict[str, SourceClaim] | None = None,
) -> str:
    unit_blocks = []
    for unit_id in write.extracted_units[:_MAX_SOURCE_UNITS_PER_WRITE]:
        unit = units[unit_id]
        unit_blocks.append(
            f"<unit id='{unit.unit_id}' locator='{unit.locator}' heading='{unit.heading_path}'>\n"
            f"{_truncate(unit.text, _MAX_SOURCE_CHARS_PER_WRITE)}\n</unit>"
        )
    matches = "\n".join(
        f"- [[{match.page_id}]] score={match.score:.3f} reason={match.match_reason}"
        for match in write.wiki_matches[:5]
    )
    evidence = ", ".join(
        f"raw/{item.raw_source.source_locator} {item.locator}".strip() for item in write.evidence
    )
    contract = write.resolved_page_body_contract
    required_sections = ", ".join(contract.required_sections)
    required_links = ", ".join(f"[[{page_id}]]" for page_id in contract.required_link_page_ids)
    required_citations = ", ".join(contract.required_source_citations)
    required_uncertainty = ", ".join(contract.required_uncertainty_terms)
    source_summary_plan = _source_summary_plan_message(write, source_claims or {})
    update_instruction = (
        "For source pages, write a compact replacement from the supplied evidence. "
        "Do not read or preserve existing source-page content.\n"
        if write.page_metadata.page_kind == "source"
        else "If the target page already exists, read_page it first and preserve useful content.\n"
    )
    contract_guidance = _page_body_contract_guidance(write)
    return (
        "Execute this PlannedPageWrite only. Do not create or update any other page. /no_think\n\n"
        f"Action: {write.action}\n"
        f"Target PageId: {write.page_metadata.page_id}\n"
        f"Target PageKind: {write.page_metadata.page_kind}\n"
        f"Target PagePath: {write.projection.page_path if write.projection else ''}\n"
        f"Summary: {write.page_metadata.summary}\n"
        f"Evidence: {evidence}\n"
        f"ResolvedPageBodyContract: {contract.contract_id}\n"
        f"Required sections: {required_sections or 'none'}\n"
        f"Required markdown shape: {contract.required_markdown_shape}\n"
        f"Minimum claim bullets: {contract.min_claim_bullets or 'none'}\n"
        f"Coverage policy: {contract.coverage_policy or 'none'}\n"
        f"Max words: {contract.max_words or 'none'}\n"
        f"Max source word ratio: {contract.max_source_word_ratio or 'none'}\n"
        f"Max copied n-gram ratio: {contract.max_copied_ngram_ratio}\n"
        f"Required PageBody links: {required_links or 'none'}\n"
        f"Required source citations: {required_citations or 'none'}\n"
        f"Required uncertainty terms: {required_uncertainty or 'none'}\n\n"
        f"{source_summary_plan}"
        f"{update_instruction}"
        f"{contract_guidance}"
        f"{_planned_write_call_instruction(write)}"
        "The PagePlan supplies PageId, PageKind, PageMetadata, and PagePath.\n\n"
        "Write only claims supported by the supplied ExtractedUnit text. "
        "Preserve uncertainty instead of turning may, possibly, or suggests into certainty. "
        "Write a compact source summary, not a transcript. Prefer concise sections and bullets.\n\n"
        f"WikiMatches:\n{matches or '- none'}\n\n"
        f"{chr(10).join(unit_blocks)}"
    )


def _planned_write_call_instruction(write: PlannedPageWrite) -> str:
    if write.source_summary_plan is None:
        return "Call write_page with page_body for the target page. "
    return (
        "Call write_page with source_record_text and claim_bullets for the target page. "
        "Each claim_bullets item must include bullet_text and covered_source_claims. "
    )


def _source_summary_plan_message(
    write: PlannedPageWrite, source_claims: dict[str, SourceClaim]
) -> str:
    plan = write.source_summary_plan
    if plan is None:
        return ""
    claims = []
    for claim in _source_summary_selected_claims(write, source_claims):
        roles = ", ".join(claim.claim_role_tags) or "unlabeled"
        claims.append(
            f"- {claim.source_claim_id} [{roles}] {claim.statement} "
            f"({claim.evidence.raw_source.source_locator} {claim.evidence.locator})".strip()
        )
    return (
        f"SourceSummaryPlan: {plan.source_summary_plan_id}\n"
        f"SelectedSourceClaims: {', '.join(plan.selected_source_claims)}\n"
        f"RequiredClaimRoleTags: {', '.join(plan.required_claim_role_tags) or 'none'}\n"
        f"RequiredSourceClaimGroups: {', '.join(plan.required_source_claim_groups) or 'none'}\n"
        f"RequiredSourceCitations: {', '.join(plan.required_source_citations) or 'none'}\n"
        "Selected source claim details:\n"
        f"{chr(10).join(claims) or '- none'}\n\n"
        "Cover every SelectedSourceClaim in claim_bullets.covered_source_claims. "
        "Each claim_bullets.bullet_text must include one RequiredSourceCitation. "
        "Do not print SourceClaim ids in source_record_text or bullet_text.\n\n"
    )


def _source_summary_selected_claims(
    write: PlannedPageWrite, source_claims: dict[str, SourceClaim]
) -> tuple[SourceClaim, ...]:
    plan = write.source_summary_plan
    if plan is None:
        return ()
    return tuple(
        source_claims[claim_id]
        for claim_id in plan.selected_source_claims
        if claim_id in source_claims
    )


def _page_body_contract_guidance(write: PlannedPageWrite) -> str:
    contract = write.resolved_page_body_contract
    if contract.contract_id != "source-summary":
        return ""
    citation = contract.required_source_citations[0] if contract.required_source_citations else ""
    link = (
        f"[[{contract.required_link_page_ids[0]}]]"
        if contract.required_link_page_ids
        else f"[[{write.page_metadata.page_id}]]"
    )
    uncertainty = (
        " Use one source uncertainty term in a claim bullet, such as "
        f"{', '.join(contract.required_uncertainty_terms[:3])}."
        if contract.required_uncertainty_terms
        else ""
    )
    return (
        "For ResolvedPageBodyContract source-summary, replace the whole PageBody with "
        "a short paraphrase under 120 words.\n"
        "Coverage policy main-supported-claims-and-explicit-limits means the bullets "
        "cover the source's central supported claims plus explicit uncertainty, gaps, "
        "or non-confirmations when present.\n"
        "For technical sources, cover what the thing is, what it does, and what the "
        "source does not fully confirm.\n"
        "Use this exact shape with three to five concise bullets:\n"
        "## Source record\n"
        f"Source record for {link}. ({citation})\n\n"
        "## Key supported claims\n"
        f"- One short claim identifying the source subject in your own words. ({citation})\n"
        f"- One short claim covering a central function, behavior, or finding. ({citation})\n"
        f"- One short claim preserving uncertainty, gaps, or non-confirmations when present."
        f"{uncertainty} "
        f"({citation})\n\n"
        "Do not copy long source sentences or distinctive phrases.\n"
    )


def _source_claims(
    units: tuple[ExtractedUnit, ...],
    schema: Schema,
) -> tuple[SourceClaim, ...]:
    claims: list[SourceClaim] = []
    allowed_roles = {role.tag_name for role in schema.claim_role_tags}
    for unit in units:
        for idx, sentence in enumerate(_claim_sentences(unit.text), start=1):
            role_tags = tuple(role for role in _claim_role_tags(sentence) if role in allowed_roles)
            evidence = Evidence(
                raw_source=unit.raw_source,
                locator=f"{unit.locator} s.{idx}".strip(),
                claim=sentence,
            )
            claims.append(
                SourceClaim(
                    source_claim_id=f"source-claim-{unit.unit_id}-{idx:04d}",
                    statement=sentence,
                    evidence=evidence,
                    extracted_unit_id=unit.unit_id,
                    source_span=evidence.locator,
                    claim_role_tags=role_tags,
                    claim_salience=_claim_salience(sentence, role_tags),
                    claim_certainty=_claim_certainty(role_tags),
                    subject_terms=_top_terms(sentence, 4),
                )
            )
    return tuple(claims)


def _claim_sentences(text: str) -> tuple[str, ...]:
    paragraphs: list[str] = []
    current_lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            if current_lines:
                paragraphs.append(" ".join(current_lines))
                current_lines = []
            continue
        if stripped.startswith("#"):
            if current_lines:
                paragraphs.append(" ".join(current_lines))
                current_lines = []
            continue
        current_lines.append(stripped)
    if current_lines:
        paragraphs.append(" ".join(current_lines))
    sentences: list[str] = []
    for paragraph in paragraphs:
        for sentence in _SENTENCE_RE.split(paragraph):
            normalized = " ".join(sentence.split()).strip()
            if len(_tokens(normalized)) >= 3:
                sentences.append(normalized)
    return tuple(sentences)


def _claim_role_tags(statement: str) -> tuple[str, ...]:
    lowered = statement.lower()
    roles = [
        role
        for role, patterns in _ROLE_PATTERNS
        if any(re.search(pattern, lowered) for pattern in patterns)
    ]
    return tuple(dict.fromkeys(roles))


def _claim_salience(statement: str, role_tags: tuple[str, ...]) -> float:
    role_score = max((_ROLE_WEIGHTS.get(role, 0.12) for role in role_tags), default=0.08)
    length_score = min(len(_tokens(statement)) / 80, 0.18)
    return round(min(1.0, 0.38 + role_score + length_score), 3)


def _claim_certainty(role_tags: tuple[str, ...]) -> str:
    if "uncertainty" in role_tags:
        return "uncertain"
    if "negative-evidence" in role_tags:
        return "negative-evidence"
    return "supported"


def _candidate_claims_from_source_claims(
    source_claims: tuple[SourceClaim, ...],
) -> tuple[CandidateClaim, ...]:
    return tuple(
        CandidateClaim(
            claim_id=f"claim-{claim.source_claim_id}",
            statement=claim.statement,
            evidence=claim.evidence,
            confidence=claim.claim_salience,
        )
        for claim in source_claims
    )


def _source_claim_groups(
    source_claims: tuple[SourceClaim, ...],
) -> tuple[SourceClaimGroup, ...]:
    grouped: dict[str, list[SourceClaim]] = {}
    for claim in source_claims:
        label = _primary_claim_group_label(claim)
        grouped.setdefault(label, []).append(claim)
    result = []
    for label, claims in grouped.items():
        roles = tuple(sorted({role for claim in claims for role in claim.claim_role_tags}))
        extracted_units = tuple(dict.fromkeys(claim.extracted_unit_id for claim in claims))
        result.append(
            SourceClaimGroup(
                source_claim_group_id=f"source-claim-group-{slugify(label)}",
                label=label,
                source_claims=tuple(claim.source_claim_id for claim in claims),
                extracted_units=extracted_units,
                claim_role_tags=roles,
                claim_salience=round(max(claim.claim_salience for claim in claims), 3),
            )
        )
    return tuple(sorted(result, key=lambda group: (-group.claim_salience, group.label)))


def _primary_claim_group_label(claim: SourceClaim) -> str:
    for role in (
        "uncertainty",
        "negative-evidence",
        "limitation",
        "function",
        "mechanism",
        "method",
        "provenance",
        "identity",
        "temporal",
        "requirement",
        "procedure",
    ):
        if role in claim.claim_role_tags:
            return role
    return claim.subject_terms[0] if claim.subject_terms else "general"


def _source_summary_plan(
    *,
    page_id: str,
    contract: ResolvedPageBodyContract,
    source_claims: tuple[SourceClaim, ...],
    source_claim_groups: tuple[SourceClaimGroup, ...],
) -> SourceSummaryPlan | None:
    if contract.contract_id != "source-summary" or not source_claims:
        return None
    claims_by_id = {claim.source_claim_id: claim for claim in source_claims}
    selected: list[SourceClaim] = []

    def add_role_claim(*roles: str) -> None:
        candidates = [
            claim
            for claim in source_claims
            if any(role in claim.claim_role_tags for role in roles) and claim not in selected
        ]
        if candidates:
            selected.append(max(candidates, key=lambda claim: claim.claim_salience))

    add_role_claim("identity", "definition")
    add_role_claim("function", "mechanism", "procedure", "requirement")
    add_role_claim("provenance", "temporal", "method", "evidence")
    add_role_claim("limitation", "negative-evidence", "uncertainty", "open-question")
    add_role_claim("method", "evidence", "comparison", "quantitative")

    for group in source_claim_groups:
        if len(selected) >= _MAX_SOURCE_SUMMARY_CLAIMS:
            break
        if any(claim.source_claim_id in group.source_claims for claim in selected):
            continue
        group_claims = [claims_by_id[claim_id] for claim_id in group.source_claims]
        selected.append(max(group_claims, key=lambda claim: claim.claim_salience))

    min_claims = min(contract.min_claim_bullets or 3, len(source_claims))
    for claim in sorted(source_claims, key=lambda item: -item.claim_salience):
        if len(selected) >= max(min_claims, min(_MAX_SOURCE_SUMMARY_CLAIMS, len(source_claims))):
            break
        if claim not in selected:
            selected.append(claim)

    selected_ids = tuple(claim.source_claim_id for claim in selected[:_MAX_SOURCE_SUMMARY_CLAIMS])
    selected_roles = tuple(sorted({role for claim in selected for role in claim.claim_role_tags}))
    selected_groups = tuple(
        group.source_claim_group_id
        for group in source_claim_groups
        if any(claim_id in group.source_claims for claim_id in selected_ids)
    )
    return SourceSummaryPlan(
        source_summary_plan_id=f"source-summary-plan-{page_id}",
        page_id=page_id,
        selected_source_claims=selected_ids,
        required_claim_role_tags=selected_roles,
        required_source_claim_groups=selected_groups,
        required_source_citations=contract.required_source_citations,
        coverage_policy=contract.coverage_policy,
    )


def _candidate_topics(
    units: tuple[ExtractedUnit, ...], claims: tuple[CandidateClaim, ...]
) -> tuple[CandidateTopic, ...]:
    counts: Counter[str] = Counter()
    for unit in units:
        counts.update(_tokens(unit.heading_path + " " + unit.text))
    topics = []
    for term, _ in counts.most_common(24):
        related = tuple(claim.claim_id for claim in claims if term in _tokens(claim.statement))
        topics.append(
            CandidateTopic(topic_id=f"topic-{term}", label=term, candidate_claims=related)
        )
    return tuple(topics)


def _candidate_entities(
    units: tuple[ExtractedUnit, ...], claims: tuple[CandidateClaim, ...]
) -> tuple[CandidateEntity, ...]:
    labels: Counter[str] = Counter()
    for unit in units:
        labels.update(re.findall(r"\b[A-Z][A-Za-z0-9]+(?:\s+[A-Z][A-Za-z0-9]+){0,2}\b", unit.text))
    entities = []
    for label, _ in labels.most_common(16):
        entity_id = f"entity-{slugify(label)}"
        entities.append(
            CandidateEntity(
                entity_id=entity_id,
                label=label,
                candidate_claims=tuple(
                    claim.claim_id for claim in claims if label in claim.statement
                ),
            )
        )
    return tuple(entities)


def _topic_clusters(
    units: tuple[ExtractedUnit, ...],
    claims: tuple[CandidateClaim, ...],
    topics: tuple[CandidateTopic, ...],
    source_claim_groups: tuple[SourceClaimGroup, ...],
) -> tuple[TopicCluster, ...]:
    clusters = [([unit], _embedding(unit.heading_path + " " + unit.text)) for unit in units]
    while True:
        best: tuple[int, int, float] | None = None
        for i, (_, emb_a) in enumerate(clusters):
            for j in range(i + 1, len(clusters)):
                score = _cosine(emb_a, clusters[j][1])
                if best is None or score > best[2]:
                    best = (i, j, score)
        if best is None or best[2] < _CLUSTER_THRESHOLD:
            break
        i, j, _ = best
        merged_units = clusters[i][0] + clusters[j][0]
        clusters[i] = (merged_units, _embedding(" ".join(unit.text for unit in merged_units)))
        del clusters[j]
    result = []
    for idx, (cluster_units, _) in enumerate(clusters, start=1):
        text = " ".join(unit.heading_path + " " + unit.text for unit in cluster_units)
        label = _top_terms(text, 1)[0] if _top_terms(text, 1) else cluster_units[0].heading_path
        unit_ids = tuple(unit.unit_id for unit in cluster_units)
        related_source_claim_groups = tuple(
            group.source_claim_group_id
            for group in source_claim_groups
            if set(group.extracted_units) & set(unit_ids)
        )
        result.append(
            TopicCluster(
                cluster_id=f"cluster-{idx}",
                label=label,
                extracted_units=unit_ids,
                candidate_claims=tuple(
                    claim.claim_id
                    for claim in claims
                    if any(_claim_id_mentions_unit(claim.claim_id, unit_id) for unit_id in unit_ids)
                ),
                candidate_topics=tuple(topic.topic_id for topic in topics if topic.label == label),
                source_claim_groups=related_source_claim_groups,
            )
        )
    return tuple(result)


def _claim_id_mentions_unit(claim_id: str, unit_id: str) -> bool:
    return f"source-claim-{unit_id}-" in claim_id


def _wiki_matches(
    units: tuple[ExtractedUnit, ...],
    existing_pages: dict[str, str],
    source_locator: str,
) -> tuple[WikiMatch, ...]:
    page_embeddings = {page_id: _embedding(text) for page_id, text in existing_pages.items()}
    matches: list[WikiMatch] = []
    for unit in units:
        unit_embedding = _embedding(unit.heading_path + " " + unit.text)
        for page_id, page_embedding in page_embeddings.items():
            score = _cosine(unit_embedding, page_embedding)
            if source_locator in existing_pages[page_id]:
                score += _SOURCE_PAGE_BONUS
            if score >= _MATCH_THRESHOLD:
                matches.append(
                    WikiMatch(
                        page_id=page_id,
                        score=round(score, 6),
                        match_reason=f"nearest-neighbor:{unit.unit_id}",
                        page_excerpt=_excerpt(existing_pages[page_id]),
                    )
                )
    return tuple(sorted(matches, key=lambda item: (-item.score, item.page_id)))


def _claim_comparisons(
    claims: tuple[CandidateClaim, ...], matches: tuple[WikiMatch, ...]
) -> tuple[ClaimComparison, ...]:
    # Deterministic placeholder relation until a model/NLI check is introduced.
    comparisons = []
    for claim in claims:
        for match in matches[:3]:
            if _cosine(_embedding(claim.statement), _embedding(match.page_excerpt)) > 0.2:
                comparisons.append(
                    ClaimComparison(
                        candidate_claim=claim.claim_id,
                        existing_claim=match.page_excerpt,
                        relation="overlap",
                        page_id=match.page_id,
                    )
                )
                break
    return tuple(comparisons)


def _planned_writes(
    *,
    raw_source: RawSource,
    extracted_units: tuple[ExtractedUnit, ...],
    existing_pages: dict[str, str],
    wiki_matches: tuple[WikiMatch, ...],
    claim_comparisons: tuple[ClaimComparison, ...],
    wiki_structure: WikiStructure,
    today: str,
    schema: Schema,
    source_plan_contract_selections: tuple[SourcePlanContractSelection, ...],
    source_claims: tuple[SourceClaim, ...],
    source_claim_groups: tuple[SourceClaimGroup, ...],
) -> tuple[PlannedPageWrite, ...]:
    writes: list[PlannedPageWrite] = []
    source_stem = slugify(Path(raw_source.source_locator).stem)
    matches_by_unit = _matches_by_unit(wiki_matches)
    units_by_target: dict[str, list[ExtractedUnit]] = {}
    for unit in extracted_units:
        page_id = _target_source_page(unit, existing_pages, matches_by_unit.get(unit.unit_id, ()))
        units_by_target.setdefault(page_id, []).append(unit)
    for page_id, target_units in units_by_target.items():
        first_unit = target_units[0]
        metadata = PageMetadata(
            page_id=page_id,
            page_kind="source",
            summary=f"{first_unit.heading_path} from raw/{raw_source.source_locator}.",
            sources=tuple(
                f"raw/{raw_source.source_locator} {unit.locator}".strip() for unit in target_units
            ),
            updated=today,
            domain=source_stem,
            category_path="source-sections",
            source_id=raw_source.source_locator,
        )
        path = str(wiki_structure.render_path(metadata))
        matches = tuple(
            match for unit in target_units for match in matches_by_unit.get(unit.unit_id, ())
        )
        contract = _resolved_page_body_contract(
            schema=schema,
            selections=source_plan_contract_selections,
            page_id=page_id,
            page_kind=metadata.page_kind,
            required_source_citations=metadata.sources,
        )
        target_source_claims = tuple(
            claim
            for claim in source_claims
            if claim.extracted_unit_id in {unit.unit_id for unit in target_units}
        )
        target_source_claim_groups = tuple(
            group
            for group in source_claim_groups
            if set(group.extracted_units) & {unit.unit_id for unit in target_units}
        )
        writes.append(
            PlannedPageWrite(
                write_id=f"write-{page_id}",
                action="enrich-existing" if page_id in existing_pages else "create-new",
                page_metadata=metadata,
                extracted_units=tuple(unit.unit_id for unit in target_units),
                evidence=tuple(
                    Evidence(raw_source=raw_source, locator=unit.locator) for unit in target_units
                ),
                wiki_matches=matches,
                claim_comparisons=tuple(
                    item for item in claim_comparisons if item.page_id == page_id
                ),
                projection=ProjectionMetadata(page_metadata=metadata, page_path=path),
                existing_page_id=page_id if page_id in existing_pages else "",
                resolved_page_body_contract=contract,
                source_summary_plan=_source_summary_plan(
                    page_id=page_id,
                    contract=contract,
                    source_claims=target_source_claims,
                    source_claim_groups=target_source_claim_groups,
                ),
            )
        )
    hub_metadata = PageMetadata(
        page_id=source_stem,
        page_kind="source",
        summary=f"Hub page for raw/{raw_source.source_locator}.",
        sources=(f"raw/{raw_source.source_locator}",),
        updated=today,
        domain=source_stem,
        category_path="sources",
        source_id=raw_source.source_locator,
    )
    hub_contract = _resolved_page_body_contract(
        schema=schema,
        selections=source_plan_contract_selections,
        page_id=source_stem,
        page_kind=hub_metadata.page_kind,
        required_source_citations=hub_metadata.sources,
    )
    writes.append(
        PlannedPageWrite(
            write_id=f"write-{source_stem}-hub",
            action="enrich-existing" if source_stem in existing_pages else "create-new",
            page_metadata=hub_metadata,
            extracted_units=tuple(unit.unit_id for unit in extracted_units),
            evidence=(Evidence(raw_source=raw_source),),
            wiki_matches=tuple(wiki_matches[:8]),
            projection=ProjectionMetadata(
                page_metadata=hub_metadata,
                page_path=str(wiki_structure.render_path(hub_metadata)),
            ),
            existing_page_id=source_stem if source_stem in existing_pages else "",
            resolved_page_body_contract=hub_contract,
            source_summary_plan=_source_summary_plan(
                page_id=source_stem,
                contract=hub_contract,
                source_claims=source_claims,
                source_claim_groups=source_claim_groups,
            ),
        )
    )
    return tuple(writes)


def _markdown_planned_writes(
    *,
    raw_source: RawSource,
    title: str,
    source_text: str,
    extracted_units: tuple[ExtractedUnit, ...],
    existing_pages: dict[str, str],
    wiki_matches: tuple[WikiMatch, ...],
    wiki_structure: WikiStructure,
    today: str,
    schema: Schema,
    source_plan_contract_selections: tuple[SourcePlanContractSelection, ...],
    source_claims: tuple[SourceClaim, ...],
    source_claim_groups: tuple[SourceClaimGroup, ...],
) -> tuple[PlannedPageWrite, ...]:
    subject_page_id = slugify(Path(raw_source.source_locator).stem)
    source_page_id = _markdown_source_page_id(subject_page_id, existing_pages)
    source_citation = f"raw/{raw_source.source_locator}"
    uncertainty_terms = _uncertainty_terms(source_text)
    unit_ids = tuple(unit.unit_id for unit in extracted_units)
    source_metadata = PageMetadata(
        page_id=source_page_id,
        page_kind="source",
        summary=f"Source summary for {title}.",
        sources=(source_citation,),
        updated=today,
        domain=subject_page_id,
        category_path="sources",
        source_id=raw_source.source_locator,
    )
    subject_metadata = PageMetadata(
        page_id=subject_page_id,
        page_kind="entity",
        summary=_summary_from_title(title),
        sources=(source_citation,),
        updated=today,
        domain=subject_page_id,
        category_path="entities",
        source_id=raw_source.source_locator,
    )
    source_contract = _resolved_page_body_contract(
        schema=schema,
        selections=source_plan_contract_selections,
        page_id=source_page_id,
        page_kind=source_metadata.page_kind,
        required_link_page_ids=(subject_page_id,),
        required_source_citations=(source_citation,),
        required_uncertainty_terms=uncertainty_terms,
    )
    subject_contract = _resolved_page_body_contract(
        schema=schema,
        selections=source_plan_contract_selections,
        page_id=subject_page_id,
        page_kind=subject_metadata.page_kind,
        required_link_page_ids=(source_page_id,),
        required_source_citations=(source_citation,),
        required_uncertainty_terms=uncertainty_terms,
    )
    return (
        PlannedPageWrite(
            write_id=f"write-{source_page_id}",
            action="enrich-existing" if source_page_id in existing_pages else "create-new",
            page_metadata=source_metadata,
            extracted_units=unit_ids,
            evidence=(Evidence(raw_source=raw_source, locator="document"),),
            wiki_matches=tuple(wiki_matches[:5]),
            projection=ProjectionMetadata(
                page_metadata=source_metadata,
                page_path=str(wiki_structure.render_path(source_metadata)),
            ),
            existing_page_id=source_page_id if source_page_id in existing_pages else "",
            resolved_page_body_contract=source_contract,
            source_summary_plan=_source_summary_plan(
                page_id=source_page_id,
                contract=source_contract,
                source_claims=source_claims,
                source_claim_groups=source_claim_groups,
            ),
        ),
        PlannedPageWrite(
            write_id=f"write-{subject_page_id}",
            action="enrich-existing" if subject_page_id in existing_pages else "create-new",
            page_metadata=subject_metadata,
            extracted_units=unit_ids,
            evidence=(Evidence(raw_source=raw_source, locator="document"),),
            wiki_matches=tuple(wiki_matches[:5]),
            projection=ProjectionMetadata(
                page_metadata=subject_metadata,
                page_path=str(wiki_structure.render_path(subject_metadata)),
            ),
            existing_page_id=subject_page_id if subject_page_id in existing_pages else "",
            resolved_page_body_contract=subject_contract,
        ),
    )


def _resolved_page_body_contract(
    *,
    schema: Schema,
    selections: tuple[SourcePlanContractSelection, ...],
    page_id: str,
    page_kind: str,
    required_link_page_ids: tuple[str, ...] = (),
    required_source_citations: tuple[str, ...] = (),
    required_uncertainty_terms: tuple[str, ...] = (),
) -> ResolvedPageBodyContract:
    selection = _source_plan_contract_selection(selections, page_id, page_kind)
    contract = (
        contract_by_id(schema, selection.contract_id)
        if selection
        else contract_for_page_kind(schema, page_kind)
    )
    return resolve_page_body_contract(
        contract,
        required_link_page_ids=required_link_page_ids,
        required_source_citations=required_source_citations,
        required_uncertainty_terms=required_uncertainty_terms,
        selection=selection,
    )


def _source_plan_contract_selection(
    selections: tuple[SourcePlanContractSelection, ...],
    page_id: str,
    page_kind: str,
) -> SourcePlanContractSelection | None:
    for selection in selections:
        if page_id in selection.page_ids:
            return selection
    for selection in selections:
        if page_kind in selection.match_page_kinds:
            return selection
    return None


def _document_title(source_text: str, source_locator: str) -> str:
    match = _HEADING_RE.search(source_text)
    if match:
        return match.group(1).strip()
    return Path(source_locator).stem.replace("-", " ").replace("_", " ").strip()


def _markdown_source_page_id(subject_page_id: str, existing_pages: dict[str, str]) -> str:
    source_page_id = f"{subject_page_id}-source"
    if source_page_id not in existing_pages:
        return source_page_id
    return source_page_id


def _summary_from_title(title: str) -> str:
    return f"Facts about {title} from an ingested RawSource."


def _uncertainty_terms(text: str) -> tuple[str, ...]:
    term_patterns = (
        ("may", r"\bmay\b"),
        ("might", r"\bmight\b"),
        ("possible", r"\bpossible\b|\bpossibly\b"),
        ("suggest", r"\bsuggest\w*\b"),
        ("uncertain", r"\buncertain\b"),
        ("unknown", r"\bunknown\b"),
        ("unconfirmed", r"\bunconfirmed\b"),
        ("verify", r"\[verify\]"),
    )
    lowered = text.lower()
    return tuple(label for label, pattern in term_patterns if re.search(pattern, lowered))


def _target_source_page(
    unit: ExtractedUnit, existing_pages: dict[str, str], matches: tuple[WikiMatch, ...]
) -> str:
    stem = slugify(Path(unit.raw_source.source_locator).stem)
    default_page = slugify(f"{stem}-{unit.heading_path}")
    if default_page in existing_pages:
        return default_page
    source_matches = [
        match
        for match in matches
        if _page_kind(match.page_id, existing_pages) == "source" and match.page_id != stem
    ]
    for match in source_matches:
        if _same_section_identity(unit.heading_path, match.page_id):
            return match.page_id
    return default_page


def _same_section_identity(heading: str, page_id: str) -> bool:
    heading_terms = set(_tokens(heading))
    if not heading_terms:
        return False
    page_terms = set(page_id.split("-"))
    required_overlap = min(2, len(heading_terms))
    return len(heading_terms & page_terms) >= required_overlap


def _matches_by_unit(matches: tuple[WikiMatch, ...]) -> dict[str, tuple[WikiMatch, ...]]:
    grouped: dict[str, list[WikiMatch]] = {}
    for match in matches:
        if ":" not in match.match_reason:
            continue
        unit_id = match.match_reason.split(":", 1)[1]
        grouped.setdefault(unit_id, []).append(match)
    return {key: tuple(value[:5]) for key, value in grouped.items()}


def _page_kind(page_id: str, existing_pages: dict[str, str]) -> str:
    try:
        return parse_page(existing_pages[page_id]).page_kind
    except Exception:
        return ""


def _embedding(text: str) -> dict[str, float]:
    counts = Counter(_tokens(text))
    norm = math.sqrt(sum(value * value for value in counts.values()))
    if not norm:
        return {}
    return {key: value / norm for key, value in counts.items()}


def _cosine(a: dict[str, float], b: dict[str, float]) -> float:
    if not a or not b:
        return 0.0
    small, large = (a, b) if len(a) <= len(b) else (b, a)
    return sum(value * large.get(key, 0.0) for key, value in small.items())


def _tokens(text: str) -> tuple[str, ...]:
    return tuple(t for t in _TOKEN_RE.findall(text.lower()) if t not in _STOP_WORDS)


def _top_terms(text: str, limit: int) -> tuple[str, ...]:
    return tuple(term for term, _ in Counter(_tokens(text)).most_common(limit))


def _first_statement(text: str) -> str:
    cleaned = " ".join(
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.startswith("#") and not line.startswith("!")
    )
    for sentence in _SENTENCE_RE.split(cleaned):
        if 40 <= len(sentence) <= 300:
            return sentence
    return _truncate(cleaned, 220)


def _excerpt(text: str) -> str:
    body = text.split("---", 2)[-1] if text.startswith("---") else text
    return _truncate(" ".join(body.split()), 240)


def _truncate(text: str, limit: int) -> str:
    cleaned = text.strip()
    return cleaned if len(cleaned) <= limit else cleaned[: limit - 1].rstrip() + "…"

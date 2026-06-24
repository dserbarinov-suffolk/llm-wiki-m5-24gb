"""Candidate selection and deterministic checks for claim-support audits."""

from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping, Sequence

from llmwiki.domain.citations import SourceInventory, inspect_citations
from llmwiki.domain.claim_support import (
    DEFAULT_CLAIM_SUPPORT_SAMPLE_STRATEGY,
    DEFAULT_MAX_CLAIM_SUPPORT_CLAIMS,
    ClaimSupportCandidate,
    ClaimSupportCategory,
    ClaimSupportFinding,
    ClaimSupportSampleStrategy,
    ClaimSupportSelection,
)
from llmwiki.domain.claim_support_evidence import ClaimSupportEvidenceIndex
from llmwiki.domain.claim_support_sampling import (
    claim_support_risk_tags,
    claim_support_sample_coverage,
    sample_claim_support_candidates,
)
from llmwiki.domain.evidence_locator_index import canonicalize_evidence_text
from llmwiki.domain.evidence_locators import (
    locator_match_for_citation,
    source_range_finding,
)
from llmwiki.domain.evidence_registry import EvidenceRegistry
from llmwiki.domain.pages import PageError, parse_page
from llmwiki.domain.system_pages import SYSTEM_PAGES

_TERM_RE = re.compile(r"[a-z][a-z0-9-]{2,}")
_SCOPE_SHIFT_RE = re.compile(
    r"\b("
    r"(?:have(?:n't| not)|has(?:n't| not)|had(?:n't| not))\s+encountered\b.{0,80}\byet\b"
    r"|not\s+encountered\b.{0,80}\byet\b"
    r"|fourth\s+possibility\b"
    r"|we(?:'ll| will)\s+(?:see|encounter|discuss|return\s+to)\b.{0,80}\blater\b"
    r")",
    re.IGNORECASE,
)


def select_claim_support_candidates(
    page_texts: Mapping[str, str],
    inventory: SourceInventory,
    registries: Sequence[EvidenceRegistry],
    source_summary_artifacts: Sequence[object] = (),
    *,
    max_claims: int = DEFAULT_MAX_CLAIM_SUPPORT_CLAIMS,
    source: str = "",
    sample_strategy: ClaimSupportSampleStrategy = DEFAULT_CLAIM_SUPPORT_SAMPLE_STRATEGY,
    page_ids: Sequence[str] = (),
    claim_contains: str = "",
) -> ClaimSupportSelection:
    if max_claims < 1:
        raise ValueError("max_claims must be at least 1.")
    if sample_strategy not in ("ordered", "stratified"):
        raise ValueError("sample_strategy must be 'ordered' or 'stratified'.")
    source_path = _source_path_filter(source)
    filters = _CandidateFilters(frozenset(page_ids), claim_contains.strip().lower())
    index = ClaimSupportEvidenceIndex(registries)
    summary_candidates = _source_summary_artifact_candidates(
        page_texts, inventory, source_summary_artifacts, index, source_path, filters
    )
    summary_keys = {(candidate.page_id, candidate.claim_text) for candidate in summary_candidates}
    prose_candidates = _prose_candidates(
        page_texts, inventory, index, source_path, summary_keys, filters
    )
    discovered = (*summary_candidates, *prose_candidates)
    selected: list[ClaimSupportCandidate] = []
    blocked: list[ClaimSupportCandidate] = []
    audited: list[ClaimSupportCandidate] = []
    findings: list[ClaimSupportFinding] = []
    sample_order = sample_claim_support_candidates(discovered, sample_strategy=sample_strategy)
    for candidate in sample_order:
        if len(selected) >= max_claims:
            break
        audited.append(candidate)
        candidate_findings = _deterministic_findings(candidate, inventory, index)
        findings.extend(candidate_findings)
        if candidate_findings:
            blocked.append(candidate)
        else:
            selected.append(candidate)
    return ClaimSupportSelection(
        candidates=tuple(selected),
        blocked_candidates=tuple(blocked),
        deterministic_findings=tuple(findings),
        candidate_count=len(discovered),
        max_claims=max_claims,
        sample_strategy=sample_strategy,
        sample_coverage=claim_support_sample_coverage(
            discovered, tuple(audited), sample_strategy=sample_strategy
        ),
    )


class _CandidateFilters:
    def __init__(self, page_ids: frozenset[str], claim_contains: str) -> None:
        self.page_ids = page_ids
        self.claim_contains = claim_contains

    def accepts(self, page_id: str, claim_text: str, context: str) -> bool:
        if self.page_ids and page_id not in self.page_ids:
            return False
        if self.claim_contains:
            haystack = f"{claim_text}\n{context}".lower()
            if self.claim_contains not in haystack:
                return False
        return True


def _source_summary_artifact_candidates(
    page_texts: Mapping[str, str],
    inventory: SourceInventory,
    artifacts: Sequence[object],
    index: ClaimSupportEvidenceIndex,
    source_path: str,
    filters: _CandidateFilters,
) -> tuple[ClaimSupportCandidate, ...]:
    candidates: list[ClaimSupportCandidate] = []
    seen: set[tuple[str, str, tuple[str, ...]]] = set()
    page_counts: dict[str, int] = {}
    for artifact in artifacts:
        source_locator = str(getattr(artifact, "source_locator", ""))
        if source_path and _source_path(source_locator) != source_path:
            continue
        page_id_hint = str(getattr(artifact, "page_id_hint", ""))
        draft = getattr(artifact, "draft", None)
        for bullet in getattr(draft, "claim_bullets", ()):
            covered_claims = tuple(
                str(item) for item in getattr(bullet, "covered_source_claims", ())
            )
            evidence_ids = index.evidence_ids_for_claims(covered_claims)
            page_id = index.page_id_for_evidence(evidence_ids) or page_id_hint
            if page_id not in page_texts:
                continue
            bullet_text = str(getattr(bullet, "bullet_text", ""))
            report = inspect_citations(page_id, bullet_text, inventory)
            if (
                source_path
                and report.citations
                and not any(citation.source_path == source_path for citation in report.citations)
            ):
                continue
            citations = tuple(citation.raw_text for citation in report.citations)
            evidence_ids = tuple(
                dict.fromkeys(
                    (
                        *evidence_ids,
                        *index.evidence_ids_for_citations(page_id, report.citations),
                    )
                )
            )
            claim_text = _claim_text_from_citations(bullet_text, citations)
            if not _is_claim_like(claim_text) or not filters.accepts(
                page_id, claim_text, bullet_text
            ):
                continue
            key = (page_id, claim_text, covered_claims)
            if key in seen:
                continue
            seen.add(key)
            page_counts[page_id] = page_counts.get(page_id, 0) + 1
            candidates.append(
                ClaimSupportCandidate(
                    candidate_id=f"claim-support-summary-{_slug(page_id)}-{page_counts[page_id]}",
                    page_id=page_id,
                    claim_text=claim_text,
                    page_context=bullet_text,
                    citation_texts=citations,
                    source_claim_ids=covered_claims,
                    evidence_ids=evidence_ids,
                    evidence_excerpts=index.excerpts_for_claim(evidence_ids, claim_text, limit=5),
                    candidate_kind="source-summary",
                    risk_tags=claim_support_risk_tags(claim_text),
                )
            )
    return tuple(candidates)


def _prose_candidates(
    page_texts: Mapping[str, str],
    inventory: SourceInventory,
    index: ClaimSupportEvidenceIndex,
    source_path: str,
    summary_keys: set[tuple[str, str]],
    filters: _CandidateFilters,
) -> tuple[ClaimSupportCandidate, ...]:
    candidates: list[ClaimSupportCandidate] = []
    for page_id in sorted(page_texts):
        if page_id in SYSTEM_PAGES:
            continue
        body = _body(page_id, page_texts[page_id])
        section = ""
        for line_number, line in enumerate(body.splitlines(), start=1):
            stripped = line.strip()
            if stripped.startswith("## "):
                section = stripped.removeprefix("## ").strip().lower()
                continue
            if "raw/" not in line or stripped.startswith("#"):
                continue
            report = inspect_citations(page_id, line, inventory)
            if not report.citations:
                continue
            if source_path and not any(c.source_path == source_path for c in report.citations):
                continue
            citations = tuple(citation.raw_text for citation in report.citations)
            claim_text = _claim_text_from_citations(line, citations)
            if not _is_claim_like(claim_text) or (page_id, claim_text) in summary_keys:
                continue
            if not filters.accepts(page_id, claim_text, line):
                continue
            evidence_ids = index.evidence_ids_for_citations(page_id, report.citations)
            candidates.append(
                ClaimSupportCandidate(
                    candidate_id=f"claim-support-prose-{_slug(page_id)}-{line_number}",
                    page_id=page_id,
                    claim_text=claim_text,
                    page_context=line.strip(),
                    citation_texts=citations,
                    source_claim_ids=(),
                    evidence_ids=evidence_ids,
                    evidence_excerpts=index.excerpts_for_claim(evidence_ids, claim_text, limit=5),
                    candidate_kind=_candidate_kind_for_section(section),
                    risk_tags=claim_support_risk_tags(claim_text),
                )
            )
    return tuple(candidates)


def _deterministic_findings(
    candidate: ClaimSupportCandidate,
    inventory: SourceInventory,
    index: ClaimSupportEvidenceIndex,
) -> tuple[ClaimSupportFinding, ...]:
    findings: list[ClaimSupportFinding] = []
    report = inspect_citations(candidate.page_id, candidate.page_context, inventory)
    for citation_finding in report.findings:
        findings.append(
            _finding(
                candidate,
                "missing-evidence",
                f"{citation_finding.code}: {citation_finding.message}",
            )
        )
    if not candidate.evidence_ids:
        findings.append(_finding(candidate, "missing-evidence", "No EvidenceRecord matched."))
    for citation in report.citations:
        registry = index.registry_for_source(citation.source_path)
        if registry is None:
            continue
        range_finding = source_range_finding(citation, registry)
        if range_finding is not None:
            findings.append(_finding(candidate, "source-range", range_finding.message))
        _, locator_finding = locator_match_for_citation(citation, registry)
        if locator_finding is not None:
            findings.append(_finding(candidate, "locator-mismatch", locator_finding.message))
        if citation.evidence_text and citation.line_range is None:
            copied = canonicalize_evidence_text(citation.evidence_text)
            excerpts = " ".join(index.excerpts(candidate.evidence_ids))
            if copied and copied not in canonicalize_evidence_text(excerpts):
                findings.append(
                    _finding(
                        candidate,
                        "copied-evidence",
                        "Copied evidence text mismatches EvidenceRecord excerpts.",
                    )
                )
    findings.extend(_scope_shift_findings(candidate))
    return tuple(findings)


def _scope_shift_findings(candidate: ClaimSupportCandidate) -> tuple[ClaimSupportFinding, ...]:
    if candidate.candidate_kind != "source-summary" or not candidate.evidence_excerpts:
        return ()
    excerpt_texts = tuple(_excerpt_text(excerpt) for excerpt in candidate.evidence_excerpts)
    claim_terms = _terms(candidate.claim_text)
    if not claim_terms:
        return ()
    for index, excerpt in enumerate(excerpt_texts):
        if _SCOPE_SHIFT_RE.search(excerpt) is None:
            continue
        prior_text = " ".join(excerpt_texts[:index])
        shifted_text = " ".join(excerpt_texts[index:])
        prior_overlap = len(claim_terms & _terms(prior_text))
        shifted_overlap = len(claim_terms & _terms(shifted_text))
        if shifted_overlap >= max(2, prior_overlap + 1):
            return (
                _finding(
                    candidate,
                    "support-verdict",
                    "Evidence crosses a source-scope transition before the strongest "
                    "matching support; this source-summary claim may be importing a "
                    "later or different case.",
                ),
            )
    return ()


def _claim_text_from_citations(line: str, citation_texts: Sequence[str]) -> str:
    claim = line
    for citation_text in citation_texts:
        claim = claim.replace(f"({citation_text})", "").replace(citation_text, "")
    return re.sub(r"\s+", " ", claim).strip(" -|")


def _is_claim_like(claim_text: str) -> bool:
    text = claim_text.strip()
    if not text:
        return False
    label = text.lower().strip(" :")
    return not (
        label in {"citation", "citations", "cite", "source", "sources"}
        or label.startswith("cited in")
        or (label.startswith("see ") and " for " in label)
    )


def _candidate_kind_for_section(section: str) -> str:
    return "source-summary" if section == "key supported claims" else "prose-line"


def _excerpt_text(excerpt: str) -> str:
    _evidence_id, separator, text = excerpt.partition(":")
    return text.strip() if separator else excerpt


def _terms(text: str) -> frozenset[str]:
    return frozenset(_TERM_RE.findall(text.lower()))


def _body(page_id: str, text: str) -> str:
    try:
        return parse_page(text).page_body
    except PageError:
        return text


def _source_path_filter(source: str) -> str:
    if not source:
        return ""
    return _source_path(source.removeprefix("raw/"))


def _source_path(source_locator: str) -> str:
    return source_locator if source_locator.startswith("raw/") else f"raw/{source_locator}"


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "claim"


def _finding(
    candidate: ClaimSupportCandidate,
    category: ClaimSupportCategory,
    message: str,
    evidence_id: str = "",
) -> ClaimSupportFinding:
    seed = f"{candidate.candidate_id}:{category}:{message}:{evidence_id}"
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()[:16]
    return ClaimSupportFinding(
        finding_id=f"claim-support-finding-{digest}",
        candidate_id=candidate.candidate_id,
        page_id=candidate.page_id,
        severity="blocker",
        category=category,
        message=message,
        evidence_id=evidence_id,
    )

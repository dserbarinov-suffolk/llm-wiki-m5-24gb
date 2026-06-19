"""PageBodyContract resolution and validation."""

from __future__ import annotations

import re
from collections import Counter

from llmwiki.domain.objects import (
    PageBodyContract,
    PageBodyFinding,
    ResolvedPageBodyContract,
    Schema,
    SourcePlanContractSelection,
)

_WORD_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)?")
_BULLET_RE = re.compile(r"^\s*[-*]\s+\S+", re.MULTILINE)
_UNCERTAINTY_PATTERNS = {
    "may": r"\bmay\b",
    "might": r"\bmight\b",
    "possible": r"\bpossible\b|\bpossibly\b",
    "suggest": r"\bsuggest\w*\b",
    "uncertain": r"\buncertain\b",
    "unknown": r"\bunknown\b",
    "unconfirmed": r"\bunconfirmed\b",
    "verify": r"\[verify\]",
}
_COPIED_NGRAM_SIZE = 8


def contract_for_page_kind(schema: Schema, page_kind: str) -> PageBodyContract:
    contract_id = dict(schema.page_body_contract_by_page_kind).get(page_kind)
    contracts = {contract.contract_id: contract for contract in schema.page_body_contracts}
    if contract_id and contract_id in contracts:
        return contracts[contract_id]
    for contract in schema.page_body_contracts:
        if page_kind in contract.match_page_kinds:
            return contract
    return PageBodyContract(contract_id=f"{page_kind}-page", match_page_kinds=(page_kind,))


def contract_by_id(schema: Schema, contract_id: str) -> PageBodyContract:
    for contract in schema.page_body_contracts:
        if contract.contract_id == contract_id:
            return contract
    raise ValueError(f"No PageBodyContract with contract_id {contract_id!r}.")


def resolve_page_body_contract(
    contract: PageBodyContract,
    *,
    required_link_page_ids: tuple[str, ...] = (),
    required_source_citations: tuple[str, ...] = (),
    required_uncertainty_terms: tuple[str, ...] = (),
    selection: SourcePlanContractSelection | None = None,
) -> ResolvedPageBodyContract:
    max_words = selection.max_words_override if selection and selection.max_words_override else 0
    max_source_word_ratio = (
        selection.max_source_word_ratio_override
        if selection and selection.max_source_word_ratio_override
        else 0.0
    )
    max_copied_ngram_ratio = (
        selection.max_copied_ngram_ratio_override
        if selection and selection.max_copied_ngram_ratio_override
        else 0.0
    )
    return ResolvedPageBodyContract(
        contract_id=contract.contract_id,
        required_sections=contract.required_sections,
        required_markdown_shape=contract.required_markdown_shape,
        min_claim_bullets=contract.min_claim_bullets,
        coverage_policy=contract.coverage_policy,
        max_words=max_words or contract.max_words,
        max_source_word_ratio=max_source_word_ratio or contract.max_source_word_ratio,
        max_copied_ngram_ratio=max_copied_ngram_ratio or contract.max_copied_ngram_ratio,
        required_link_page_ids=required_link_page_ids,
        required_source_citations=required_source_citations,
        required_uncertainty_terms=required_uncertainty_terms,
    )


def validate_page_body(
    page_body: str,
    contract: ResolvedPageBodyContract,
    source_text: str = "",
) -> tuple[PageBodyFinding, ...]:
    findings: list[PageBodyFinding] = []
    findings.extend(_section_findings(page_body, contract))
    findings.extend(_markdown_shape_findings(page_body, contract))
    findings.extend(_grounding_findings(page_body, contract))
    findings.extend(_length_findings(page_body, source_text, contract))
    findings.extend(_copy_findings(page_body, source_text, contract))
    return tuple(findings)


def render_page_body_findings(
    findings: tuple[PageBodyFinding, ...],
    contract: ResolvedPageBodyContract,
) -> str:
    rendered = "\n".join(f"- {finding.finding_type}: {finding.detail}" for finding in findings)
    return (
        f"PageBody violates ResolvedPageBodyContract '{contract.contract_id}'.\n"
        f"{rendered}\n"
        "Replace the whole PlannedPageWrite PageBody and satisfy every finding.\n"
        "Do not append fixes to the rejected PageBody.\n"
        "For source-summary, write a short paraphrase with the required sections, "
        "enough claim bullets, and coverage of the source's main supported claims."
    )


def _section_findings(
    page_body: str, contract: ResolvedPageBodyContract
) -> tuple[PageBodyFinding, ...]:
    normalized_body = page_body.lower()
    return tuple(
        PageBodyFinding("RequiredSections", f"missing section {section!r}")
        for section in contract.required_sections
        if section.lower() not in normalized_body
    )


def _markdown_shape_findings(
    page_body: str, contract: ResolvedPageBodyContract
) -> tuple[PageBodyFinding, ...]:
    if contract.required_markdown_shape != "claim-bullets":
        return ()
    bullet_count = len(_BULLET_RE.findall(page_body))
    min_bullets = contract.min_claim_bullets or 2
    if bullet_count >= min_bullets:
        return ()
    return (
        PageBodyFinding(
            "RequiredMarkdownShape",
            f"expected at least {min_bullets} markdown bullet claims",
        ),
    )


def _grounding_findings(
    page_body: str, contract: ResolvedPageBodyContract
) -> tuple[PageBodyFinding, ...]:
    findings: list[PageBodyFinding] = []
    for page_id in contract.required_link_page_ids:
        if f"[[{page_id}]]" not in page_body:
            findings.append(PageBodyFinding("RequiredLinkPageIds", f"missing [[{page_id}]]"))
    for citation in contract.required_source_citations:
        if citation not in page_body:
            findings.append(PageBodyFinding("RequiredSourceCitations", f"missing {citation}"))
    if contract.required_uncertainty_terms and not _preserves_uncertainty(
        page_body, contract.required_uncertainty_terms
    ):
        terms = ", ".join(contract.required_uncertainty_terms)
        findings.append(
            PageBodyFinding(
                "RequiredUncertaintyTerms",
                f"missing at least one source uncertainty term: {terms}",
            )
        )
    return tuple(findings)


def _length_findings(
    page_body: str,
    source_text: str,
    contract: ResolvedPageBodyContract,
) -> tuple[PageBodyFinding, ...]:
    page_words = len(_words(page_body))
    findings: list[PageBodyFinding] = []
    if contract.max_words and page_words > contract.max_words:
        findings.append(
            PageBodyFinding("MaxWords", f"{page_words} words exceeds {contract.max_words}")
        )
    source_words = len(_words(source_text))
    if (
        source_words >= contract.max_words > 0
        and contract.max_source_word_ratio
        and page_words / source_words > contract.max_source_word_ratio
    ):
        findings.append(
            PageBodyFinding(
                "MaxSourceWordRatio",
                f"{page_words}/{source_words} exceeds {contract.max_source_word_ratio:.2f}",
            )
        )
    return tuple(findings)


def _copy_findings(
    page_body: str,
    source_text: str,
    contract: ResolvedPageBodyContract,
) -> tuple[PageBodyFinding, ...]:
    if not source_text or contract.max_copied_ngram_ratio >= 1.0:
        return ()
    source_ngrams = set(_ngrams(_words(source_text), _COPIED_NGRAM_SIZE))
    body_ngrams = _ngrams(_words(page_body), _COPIED_NGRAM_SIZE)
    if not source_ngrams or not body_ngrams:
        return ()
    copied = sum(count for ngram, count in Counter(body_ngrams).items() if ngram in source_ngrams)
    ratio = copied / len(body_ngrams)
    if ratio <= contract.max_copied_ngram_ratio:
        return ()
    return (
        PageBodyFinding(
            "MaxCopiedNGramRatio",
            f"{ratio:.2f} exceeds {contract.max_copied_ngram_ratio:.2f}",
        ),
    )


def _preserves_uncertainty(page_body: str, terms: tuple[str, ...]) -> bool:
    lowered = page_body.lower()
    return any(
        re.search(_UNCERTAINTY_PATTERNS.get(term, rf"\b{re.escape(term)}\b"), lowered)
        for term in terms
    )


def _words(text: str) -> tuple[str, ...]:
    return tuple(match.group(0).lower() for match in _WORD_RE.finditer(text))


def _ngrams(words: tuple[str, ...], size: int) -> tuple[tuple[str, ...], ...]:
    if len(words) < size:
        return ()
    return tuple(tuple(words[idx : idx + size]) for idx in range(len(words) - size + 1))

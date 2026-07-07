"""Projection lint rules for staged wiki pages."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.projection_navigation_closure import (
    generated_page_navigation_findings,
)
from llmwiki.domain.ledger.staged_contracts import (
    ProjectionLintFinding,
    SourcePlan,
    StagedWikiPage,
    StagedWikiPageSet,
)

_RELATED_LINE = re.compile(r"^\s*-\s+\[\[[a-z0-9-]+]]")


def body_contract_findings(page: StagedWikiPage) -> tuple[ProjectionLintFinding, ...]:
    findings: list[ProjectionLintFinding] = []
    in_related = False
    lines = page.page.page_body.splitlines()
    for line in lines:
        if line == "## Related pages":
            in_related = True
            continue
        if line.startswith("## ") and in_related:
            in_related = False
        if in_related and _RELATED_LINE.match(line) and " - " not in line:
            findings.append(
                _finding(
                    "blocking",
                    "related-link-reason-missing",
                    page.page_id,
                    "visible related link has no reason",
                )
            )
    if "**Atom:**" in page.page.page_body and '<a id="atom-' not in page.page.page_body:
        findings.append(
            _finding(
                "blocking",
                "technical-atom-anchor-missing",
                page.page_id,
                "rendered technical atom has no stable anchor",
            )
        )
    return tuple(findings)


def navigation_closure_findings(
    source_plan: SourcePlan, staged_page_set: StagedWikiPageSet
) -> tuple[ProjectionLintFinding, ...]:
    page_bodies = {page.page_id: page.page.page_body for page in staged_page_set.pages}
    page_families = {page.page_id: page.page_family for page in staged_page_set.pages}
    return tuple(
        _finding("blocking", finding.finding_type, finding.page_id, finding.message)
        for finding in generated_page_navigation_findings(
            source_page_id=source_plan.source_page_id,
            page_bodies=page_bodies,
            page_families=page_families,
        )
    )


def _finding(severity: str, finding_type: str, page_id: str, message: str) -> ProjectionLintFinding:
    return ProjectionLintFinding(severity, finding_type, page_id, message)

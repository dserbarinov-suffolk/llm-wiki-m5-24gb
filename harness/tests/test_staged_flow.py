from dataclasses import replace

from llmwiki.application.source_artifacts import build_canonical_ledger_source
from llmwiki.domain.ledger.staged_flow import (
    accepted_pages,
    build_lint_run,
    build_publish_run,
    build_source_plan,
    build_staged_page_set,
)
from llmwiki.domain.objects import Schema
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.runtime.ledger_pipeline import build_source_ledger
from llmwiki.runtime.ledger_segmentation import ChunkText, segment_chunks

_HASH = "a" * 64


def test_staged_pages_publish_only_after_lint_accepts_them() -> None:
    source_plan = build_source_plan(
        source_locator="src.pdf",
        source_hash=_HASH,
        source_page_id="src",
    )
    page = _page("src", "source", "source-manifest")
    staged = build_staged_page_set(source_plan, (page,))
    lint_run = build_lint_run(
        source_plan=source_plan,
        staged_page_set=staged,
        upstream_write_decision="write-authoritative-page",
    )
    publish_run = build_publish_run(source_plan, staged, lint_run)

    assert lint_run.status == "accepted"
    assert publish_run.status == "published"
    assert publish_run.accepted_page_ids == ("src",)
    assert accepted_pages(staged, publish_run) == (page,)


def test_staged_pages_block_unplanned_page_family_before_publish() -> None:
    source_plan = build_source_plan(
        source_locator="src.pdf",
        source_hash=_HASH,
        source_page_id="src",
    )
    restricted = replace(source_plan, allowed_page_families=("source-manifest",))
    page = _page("src-topic", "concept", "topic-concept")
    staged = build_staged_page_set(restricted, (page,))
    lint_run = build_lint_run(
        source_plan=restricted,
        staged_page_set=staged,
        upstream_write_decision="write-authoritative-page",
    )
    publish_run = build_publish_run(restricted, staged, lint_run)

    assert lint_run.status == "blocked"
    assert lint_run.findings[0].finding_type == "page-family-not-planned"
    assert publish_run.status == "blocked"
    assert publish_run.accepted_page_ids == ()
    assert accepted_pages(staged, publish_run) == ()


def test_staged_pages_block_generated_page_without_inbound_route() -> None:
    source_plan = build_source_plan(
        source_locator="src.pdf",
        source_hash=_HASH,
        source_page_id="src",
    )
    source = _page("src", "source", "source-manifest")
    recipe = _page("src-recipe-rin", "recipe", "recipe-pattern")
    staged = build_staged_page_set(source_plan, (source, recipe))
    lint_run = build_lint_run(
        source_plan=source_plan,
        staged_page_set=staged,
        upstream_write_decision="write-authoritative-page",
    )

    assert lint_run.status == "blocked"
    assert any(
        finding.finding_type == "generated-page-has-no-inbound-route"
        and finding.page_id == "src-recipe-rin"
        for finding in lint_run.findings
    )


def test_staged_pages_accept_generated_page_with_inbound_route() -> None:
    source_plan = build_source_plan(
        source_locator="src.pdf",
        source_hash=_HASH,
        source_page_id="src",
    )
    source = _page(
        "src",
        "source",
        "source-manifest",
        body="# src\n\n## Recipes\n\n- [[src-recipe-rin]] - recipe pattern: Rin.\n",
    )
    recipe = _page("src-recipe-rin", "recipe", "recipe-pattern")
    staged = build_staged_page_set(source_plan, (source, recipe))
    lint_run = build_lint_run(
        source_plan=source_plan,
        staged_page_set=staged,
        upstream_write_decision="write-authoritative-page",
    )

    assert lint_run.status == "accepted"


def test_source_ledger_persists_stage_artifacts_from_real_pipeline() -> None:
    chunks = (
        ChunkText(
            "unit-1",
            "p.1",
            "Root",
            "# Root\n\nA meter has a dial.",
        ),
    )
    segment_inputs, profiles = segment_chunks(
        chunks, source_locator="src.pdf", source_hash=_HASH, schema=Schema()
    )
    canonical_source = build_canonical_ledger_source(
        source_locator="src.pdf",
        source_hash=_HASH,
        segment_inputs=segment_inputs,
        profiles=profiles,
    )
    result = build_source_ledger(
        source_locator="src.pdf",
        source_hash=_HASH,
        evidence_registry_hash="evidence-registry-hash",
        canonical_source=canonical_source,
        today="2026-07-02",
    )

    assert result.source_plan.source_locator == "src.pdf"
    assert result.extraction_result.claim_ledger_id
    assert result.staged_page_set.source_plan_id == result.source_plan.source_plan_id
    assert result.lint_run.source_plan_id == result.source_plan.source_plan_id
    assert result.publish_run.status == "published"
    assert result.wiki_page is not None
    for filename in (
        "source-plan.json",
        "extraction-result.json",
        "staged-pages.json",
        "lint-run.json",
        "publish-run.json",
        "assertion-graph-source-artifact.json",
    ):
        assert filename in result.artifact_files
    member_kinds = {
        member.portable_artifact_kind for member in result.portable_artifact_set.members
    }
    assert "source-plan-artifact" in member_kinds
    assert "publish-run-artifact" in member_kinds
    assert "assertion-graph-source-artifact" in member_kinds


def _page(
    page_id: str, page_kind: str, page_family: str, *, body: str | None = None
) -> WikiPage:
    metadata = PageMetadata(
        page_id=page_id,
        page_kind=page_kind,
        page_family=page_family,
        summary=f"{page_id} summary.",
        sources=("raw/src.pdf",),
        projection_coverage_pointer=f"{page_id}@abc",
    )
    return WikiPage.from_metadata(metadata, body or f"# {page_id}\n")

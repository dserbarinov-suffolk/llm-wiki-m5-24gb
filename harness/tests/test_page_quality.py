from llmwiki.domain.assertion_graph import (
    Assertion,
    AssertionKind,
    AssertionStatus,
    PageCoverageRecord,
    PageProjection,
    ProjectionPolicy,
    RenderedRelatedLink,
    SourceUnit,
    SourceUnitKind,
    TechnicalAtom,
    TechnicalAtomKind,
    TopicKind,
    TopicState,
)
from llmwiki.domain.assertion_graph.source import ParseStatus
from llmwiki.domain.page_quality import build_page_quality_report

_HASH = "a" * 64


def test_narrow_source_local_page_scores_good() -> None:
    units = _units(3, page=10)
    assertions = (_assertion("ast_one", units[0].id),)
    topic = _topic("tps_good", tuple(unit.id for unit in units), ("ast_one",))
    page = _page(
        "good-page",
        "tps_good",
        (
            PageCoverageRecord(
                coverage_id="cov_1",
                page_section="Statements",
                support_record_id="ast_one",
                rendered_text="A bounded claim.",
            ),
        ),
        (
            RenderedRelatedLink(
                target_page_id="next-page",
                relation_label="next-step",
                description="Next source-supported procedure step",
                support_record_ids=("ast_one",),
            ),
        ),
    )

    report = build_page_quality_report(
        source_locator="source.pdf",
        source_hash=_HASH,
        pages=(page,),
        topics=(topic,),
        assertions=assertions,
        atoms=(),
        source_units=units,
    )

    record = report.page_quality_records[0]
    assert record.overall_quality_band in {"good", "exemplary"}
    assert record.source_locality_score >= 0.85
    assert record.page_shape_fit >= 0.85
    assert record.walkability_score >= 0.85


def test_broad_procedure_catalog_scores_bad() -> None:
    units = _units(140, page=40)
    topic = _topic(
        "tps_bad",
        tuple(unit.id for unit in units),
        ("ast_bad",),
        family="broad-topic",
        kind=TopicKind.CONCEPT,
    )
    page = _page(
        "bad-page",
        "tps_bad",
        tuple(
            PageCoverageRecord(
                coverage_id=f"cov_{index}",
                page_section="Procedure",
                support_record_id="tps_bad",
                rendered_text="fragment",
            )
            for index in range(140)
        ),
        (),
        body="# Bad\n\n## Procedure\n\n- They act.",
        family="broad-topic",
    )

    report = build_page_quality_report(
        source_locator="source.pdf",
        source_hash=_HASH,
        pages=(page,),
        topics=(topic,),
        assertions=(_assertion("ast_bad", units[0].id),),
        atoms=(),
        source_units=units,
    )

    record = report.page_quality_records[0]
    assert record.overall_quality_band in {"bad", "suspect"}
    assert record.source_locality_score < 0.4
    assert record.topic_boundary_cohesion < 0.4
    assert record.page_shape_fit < 0.4


def test_partial_technical_atom_lowers_integrity() -> None:
    units = _units(2, page=20)
    atom = TechnicalAtom(
        id="tat_table",
        atom_kind=TechnicalAtomKind.TABLE,
        evidence_span_ids=("evs_table",),
        exact_payload="broken table text",
        parse_status=ParseStatus.PARTIAL,
        source_order=1,
        provenance_activity_ids=("prv_atom",),
    )
    topic = _topic(
        "tps_atom",
        tuple(unit.id for unit in units),
        (),
        atoms=("tat_table",),
    )
    page = _page(
        "atom-page",
        "tps_atom",
        (
            PageCoverageRecord(
                coverage_id="cov_atom",
                page_section="Technical atoms",
                support_record_id="tat_table",
                rendered_text="broken table text",
            ),
        ),
        (),
    )

    report = build_page_quality_report(
        source_locator="source.pdf",
        source_hash=_HASH,
        pages=(page,),
        topics=(topic,),
        assertions=(),
        atoms=(atom,),
        source_units=units,
    )

    assert report.page_quality_records[0].technical_atom_integrity_rate == 0.45


def _units(count: int, *, page: int) -> tuple[SourceUnit, ...]:
    return tuple(
        SourceUnit(
            id=f"su_unit_{index}",
            source_locator="source.pdf",
            source_hash=_HASH,
            source_order=index,
            kind=SourceUnitKind.PARAGRAPH,
            text=f"Source unit {index}.",
            page_span=(page + index // 40, page + index // 40),
        )
        for index in range(count)
    )


def _assertion(assertion_id: str, unit_id: str) -> Assertion:
    return Assertion(
        id=assertion_id,
        kind=AssertionKind.SOURCE_CLAIM,
        subject="Bounded topic",
        predicate="has",
        object_value="a source-backed claim",
        status=AssertionStatus.ACCEPTED,
        confidence=1.0,
        source_unit_ids=(unit_id,),
        evidence_span_ids=("evs_claim",),
        provenance_activity_ids=("prv_assertion",),
    )


def _topic(
    topic_id: str,
    unit_ids: tuple[str, ...],
    assertion_ids: tuple[str, ...],
    *,
    atoms: tuple[str, ...] = (),
    family: str = "topic-concept",
    kind: TopicKind = TopicKind.CONCEPT,
) -> TopicState:
    return TopicState(
        id=topic_id,
        topic_key=topic_id,
        label=topic_id,
        topic_kind=kind,
        accepted_assertion_ids=assertion_ids,
        accepted_technical_atom_ids=atoms,
        source_unit_ids=unit_ids,
        projection_policy=ProjectionPolicy(page_kind="concept", page_family=family),
    )


def _page(
    page_id: str,
    topic_id: str,
    coverage: tuple[PageCoverageRecord, ...],
    links: tuple[RenderedRelatedLink, ...],
    *,
    body: str = "# Good\n\n## Statements\n\n- A bounded claim.",
    family: str = "topic-concept",
) -> PageProjection:
    return PageProjection(
        id=f"pgp_{page_id.replace('-', '_')}",
        topic_state_id=topic_id,
        page_id=page_id,
        page_kind="concept",
        page_family=family,
        page_body=body,
        coverage_records=coverage,
        source_locators=("source.pdf",),
        rendered_related_links=links,
    )

from llmwiki.domain.ledger.builder import SegmentInput, build_claim_ledger, default_schema_bundle
from llmwiki.domain.ledger.extraction import ExtractedUnitProfile
from llmwiki.domain.ledger.features import profile_unit
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment
from llmwiki.domain.ledger.source_records import add_source_records_to_structure
from llmwiki.domain.ledger.structure_build import build_structure
from llmwiki.pdf.document import SourceUnitBlock


def _segment(order: int, text: str, kind: str = "heading") -> SourceSegment:
    return SourceSegment(
        segment_id=f"seg-{order}",
        source_range_id=f"range-{order}",
        source_locator="synthetic.pdf",
        source_hash="abc",
        heading_path="Document",
        structure_node_id="",
        source_order=order,
        text=text,
        segment_kind=kind,
        evidence_ids=(f"ev-{order}",),
    )


def _structured_heading(
    order: int, text: str, heading_level: int, *, heading_path: str | None = None
) -> SourceSegment:
    path = heading_path or text
    block = SourceUnitBlock(
        element_id=f"element-{order}",
        block_kind="heading",
        heading_path=path,
        page_start=order,
        page_end=order,
        text=text,
        heading_level=heading_level,
    )
    return SourceSegment(
        segment_id=f"seg-{order}",
        source_range_id=f"range-{order}",
        source_locator="synthetic.pdf",
        source_hash="abc",
        heading_path=path,
        structure_node_id="",
        source_order=order,
        text=f"# {text}",
        segment_kind="heading",
        evidence_ids=(f"ev-{order}",),
        source_blocks=(block,),
    )


def test_structure_build_records_parent_child_and_sibling_relations() -> None:
    plan = build_structure(
        "abc",
        "synthetic.pdf",
        (
            _segment(1, "# Parent"),
            _segment(2, "## First Child"),
            _segment(3, "First body", "paragraph"),
            _segment(4, "## Second Child"),
        ),
    )

    first = next(node for node in plan.nodes if node.heading_text == "First Child")
    second = next(node for node in plan.nodes if node.heading_text == "Second Child")

    assert first.parent_structure_node_id == second.parent_structure_node_id
    assert any(
        relation.source_structure_node_id == first.structure_node_id
        and relation.target_structure_node_id == second.structure_node_id
        and relation.relation_kind == "next-sibling"
        for relation in plan.relations
    )
    assert any(
        relation.source_structure_node_id == second.structure_node_id
        and relation.target_structure_node_id == first.structure_node_id
        and relation.relation_kind == "previous-sibling"
        for relation in plan.relations
    )


def test_structure_build_uses_source_numbering_when_heading_depth_is_flat() -> None:
    plan = build_structure(
        "abc",
        "synthetic.pdf",
        (
            _segment(1, "# 1 Parent Process"),
            _segment(2, "# 1.1 Choose Inputs"),
            _segment(3, "Input body", "paragraph"),
            _segment(4, "# 1.2 Compute Result"),
            _segment(5, "Result body", "paragraph"),
            _segment(6, "# 2 Other Process"),
        ),
    )

    parent = next(node for node in plan.nodes if node.heading_text == "1 Parent Process")
    first = next(node for node in plan.nodes if node.heading_text == "1.1 Choose Inputs")
    second = next(node for node in plan.nodes if node.heading_text == "1.2 Compute Result")
    other = next(node for node in plan.nodes if node.heading_text == "2 Other Process")

    assert first.parent_structure_node_id == parent.structure_node_id
    assert second.parent_structure_node_id == parent.structure_node_id
    assert other.parent_structure_node_id != parent.structure_node_id


def test_structure_build_reconciles_split_numbered_heading_path() -> None:
    plan = build_structure(
        "abc",
        "synthetic.pdf",
        (
            _structured_heading(
                1,
                "1.4 Character Creation",
                1,
                heading_path="1.4 > Character Creation",
            ),
            _structured_heading(
                2,
                "1.4.1 Choose a Race",
                3,
                heading_path="1.4 > Character Creation > 1.4.1 Choose a Race",
            ),
            _structured_heading(
                3,
                "1.4.2 Determine Ability Scores",
                3,
                heading_path="1.4 > Character Creation > 1.4.2 Determine Ability Scores",
            ),
            _structured_heading(
                4,
                "1.4.9 Filling Out the Character Sheet",
                1,
                heading_path="1.4 > Character Creation > 1.4.9 Filling Out the Character Sheet",
            ),
            _structured_heading(5, "1.5 Next Procedure", 1),
        ),
    )

    parent = next(node for node in plan.nodes if node.heading_text == "1.4 Character Creation")
    race = next(node for node in plan.nodes if node.heading_text == "1.4.1 Choose a Race")
    scores = next(
        node for node in plan.nodes if node.heading_text == "1.4.2 Determine Ability Scores"
    )
    sheet = next(
        node for node in plan.nodes if node.heading_text == "1.4.9 Filling Out the Character Sheet"
    )
    next_procedure = next(node for node in plan.nodes if node.heading_text == "1.5 Next Procedure")

    assert race.parent_structure_node_id == parent.structure_node_id
    assert scores.parent_structure_node_id == parent.structure_node_id
    assert sheet.parent_structure_node_id == parent.structure_node_id
    assert next_procedure.parent_structure_node_id != parent.structure_node_id
    assert any(
        relation.source_structure_node_id == race.structure_node_id
        and relation.target_structure_node_id == scores.structure_node_id
        and relation.relation_kind == "next-sibling"
        for relation in plan.relations
    )


def test_structure_build_reconciles_generic_numbered_descendants() -> None:
    plan = build_structure(
        "abc",
        "synthetic.pdf",
        (
            _structured_heading(1, "2.7 Primary Operation", 1),
            _structured_heading(2, "2.7.1 Prepare Input", 1),
            _structured_heading(3, "2.7.2 Produce Output", 3),
            _structured_heading(4, "2.8 Adjacent Operation", 3),
            _structured_heading(5, "3 Different Operation", 1),
        ),
    )

    parent = next(node for node in plan.nodes if node.heading_text == "2.7 Primary Operation")
    prepare = next(node for node in plan.nodes if node.heading_text == "2.7.1 Prepare Input")
    produce = next(node for node in plan.nodes if node.heading_text == "2.7.2 Produce Output")
    adjacent = next(node for node in plan.nodes if node.heading_text == "2.8 Adjacent Operation")
    different = next(node for node in plan.nodes if node.heading_text == "3 Different Operation")

    assert prepare.parent_structure_node_id == parent.structure_node_id
    assert produce.parent_structure_node_id == parent.structure_node_id
    assert adjacent.parent_structure_node_id != parent.structure_node_id
    assert different.parent_structure_node_id != parent.structure_node_id


def test_structure_build_closes_unnumbered_container_from_numbered_child_prefix() -> None:
    plan = build_structure(
        "abc",
        "synthetic.pdf",
        (
            _structured_heading(1, "Alpha Procedure", 1),
            _structured_heading(2, "4.6.1 First Step", 2),
            _segment(3, "First body", "paragraph"),
            _structured_heading(4, "4.6.2 Second Step", 2),
            _segment(5, "Second body", "paragraph"),
            _structured_heading(6, "4.7 Next Procedure", 3),
            _segment(7, "Next body", "paragraph"),
        ),
    )

    alpha = next(node for node in plan.nodes if node.heading_text == "Alpha Procedure")
    first = next(node for node in plan.nodes if node.heading_text == "4.6.1 First Step")
    second = next(node for node in plan.nodes if node.heading_text == "4.6.2 Second Step")
    next_procedure = next(node for node in plan.nodes if node.heading_text == "4.7 Next Procedure")

    assert first.parent_structure_node_id == alpha.structure_node_id
    assert second.parent_structure_node_id == alpha.structure_node_id
    assert next_procedure.parent_structure_node_id != alpha.structure_node_id


def test_structure_build_prefers_structured_heading_depth_over_markdown_depth() -> None:
    plan = build_structure(
        "abc",
        "synthetic.pdf",
        (
            _structured_heading(1, "Parent", 1),
            _structured_heading(2, "Child", 2),
            _segment(3, "Child body", "paragraph"),
        ),
    )

    parent = next(node for node in plan.nodes if node.heading_text == "Parent")
    child = next(node for node in plan.nodes if node.heading_text == "Child")

    assert child.parent_structure_node_id == parent.structure_node_id
    assert child.depth == 2
    assert child.structure_node_kind == "section"


def test_bound_number_marker_does_not_trap_later_top_level_heading() -> None:
    plan = build_structure(
        "abc",
        "synthetic.pdf",
        (
            _structured_heading(1, "2.3.4", 3),
            _structured_heading(2, "Nested Topic", 3, heading_path="2.3.4 Nested Topic"),
            _segment(3, "Nested body", "paragraph"),
            _structured_heading(4, "New Major Topic", 1),
        ),
    )

    nested = next(node for node in plan.nodes if node.heading_text == "2.3.4 Nested Topic")
    major = next(node for node in plan.nodes if node.heading_text == "New Major Topic")

    assert major.parent_structure_node_id != nested.structure_node_id


def test_clean_top_level_heading_path_resets_stale_nested_stack() -> None:
    plan = build_structure(
        "abc",
        "synthetic.pdf",
        (
            _structured_heading(1, "2.3 Parent", 1),
            _structured_heading(2, "2.3.4 Nested Topic", 3),
            _structured_heading(3, "New Major Topic", 1, heading_path="New Major Topic"),
        ),
    )

    nested = next(node for node in plan.nodes if node.heading_text == "2.3.4 Nested Topic")
    major = next(node for node in plan.nodes if node.heading_text == "New Major Topic")

    assert major.parent_structure_node_id != nested.structure_node_id


def test_numbering_still_preserves_proven_descendants_after_marker_binding() -> None:
    plan = build_structure(
        "abc",
        "synthetic.pdf",
        (
            _structured_heading(1, "2.3 Parent", 1),
            _structured_heading(2, "2.3.4", 3),
            _structured_heading(3, "Nested Topic", 3, heading_path="2.3.4 Nested Topic"),
            _structured_heading(4, "2.3.4.1 Detail", 4),
        ),
    )

    nested = next(node for node in plan.nodes if node.heading_text == "2.3.4 Nested Topic")
    detail = next(node for node in plan.nodes if node.heading_text == "2.3.4.1 Detail")

    assert detail.parent_structure_node_id == nested.structure_node_id


def test_source_records_create_sibling_nodes_from_repeated_generic_labels() -> None:
    segments = (
        _segment(1, "# Catalog"),
        _segment(2, "[ Alpha ]", "paragraph"),
        _segment(3, "Metric=1 Cost=2 Alpha detail.", "paragraph"),
        _segment(4, "[ Beta ]", "paragraph"),
        _segment(5, "Metric=3 Cost=4 Beta detail.", "paragraph"),
    )
    heading_plan = build_structure("abc", "synthetic.pdf", segments)
    plan = add_source_records_to_structure("abc", "synthetic.pdf", segments, heading_plan)

    catalog = next(node for node in plan.nodes if node.heading_text == "Catalog")
    alpha = next(node for node in plan.nodes if node.heading_text == "Alpha")
    beta = next(node for node in plan.nodes if node.heading_text == "Beta")

    assert alpha.structure_node_kind == "record"
    assert beta.structure_node_kind == "record"
    assert alpha.parent_structure_node_id == catalog.structure_node_id
    assert beta.parent_structure_node_id == catalog.structure_node_id
    assert plan.node_for_segment["seg-3"] == alpha.structure_node_id
    assert plan.node_for_segment["seg-5"] == beta.structure_node_id


def test_source_records_bound_catalog_run_after_container_record_heading() -> None:
    segments = (
        _segment(1, "# 《 Staves and Wands 》 [ Ice Blaze Wand ]"),
        _segment(2, "Rarity=12 Form=Wand Powers=Ice blades.", "paragraph"),
        _segment(3, "[ Staff of Sorcery ]", "paragraph"),
        _segment(4, "Rarity=18 Form=Staff Powers=Ancient magic.", "paragraph"),
        _segment(5, "[ Crystal Orb of Clairvoyance ]", "paragraph"),
        _segment(6, "Rarity=15 Form=Orb Powers=Shows distant places.", "paragraph"),
    )
    heading_plan = build_structure("abc", "synthetic.pdf", segments)
    plan = add_source_records_to_structure("abc", "synthetic.pdf", segments, heading_plan)

    ice = next(node for node in plan.nodes if node.heading_text == "Ice Blaze Wand")
    staff = next(node for node in plan.nodes if node.heading_text == "Staff of Sorcery")
    orb = next(node for node in plan.nodes if node.heading_text == "Crystal Orb of Clairvoyance")

    assert plan.node_for_segment["seg-2"] == ice.structure_node_id
    assert plan.node_for_segment["seg-4"] == staff.structure_node_id
    assert plan.node_for_segment["seg-6"] == orb.structure_node_id


def test_source_records_do_not_promote_isolated_bracket_phrase() -> None:
    segments = (
        _segment(1, "# Notes"),
        _segment(2, "[ Aside ]", "paragraph"),
        _segment(3, "This is just one isolated aside.", "paragraph"),
    )
    heading_plan = build_structure("abc", "synthetic.pdf", segments)
    plan = add_source_records_to_structure("abc", "synthetic.pdf", segments, heading_plan)

    assert not any(node.structure_node_kind == "record" for node in plan.nodes)


def test_source_records_do_not_promote_repeated_bracket_fragments_without_record_shape() -> None:
    segments = (
        _segment(1, "# Examples"),
        _segment(2, "[ Alpha ]", "paragraph"),
        _segment(3, "This paragraph mentions Alpha without structured fields.", "paragraph"),
        _segment(4, "[ Beta ]", "paragraph"),
        _segment(5, "This paragraph mentions Beta without structured fields.", "paragraph"),
    )
    heading_plan = build_structure("abc", "synthetic.pdf", segments)
    plan = add_source_records_to_structure("abc", "synthetic.pdf", segments, heading_plan)

    assert not any(node.structure_node_kind == "record" for node in plan.nodes)


def test_source_records_do_not_promote_dotted_code_identifiers() -> None:
    segments = (
        _segment(1, "# API Examples"),
        _segment(2, "[ Namespace.member ]", "paragraph"),
        _segment(3, "Input=Value Output=Result", "paragraph"),
        _segment(4, "[ Namespace.member ]", "paragraph"),
        _segment(5, "Input=Value Output=Result", "paragraph"),
    )
    heading_plan = build_structure("abc", "synthetic.pdf", segments)
    plan = add_source_records_to_structure("abc", "synthetic.pdf", segments, heading_plan)

    assert not any(node.structure_node_kind == "record" for node in plan.nodes)


def test_claim_ledger_owns_repeated_record_claims_by_record_node() -> None:
    inputs = (
        SegmentInput(_segment(1, "# Catalog")),
        SegmentInput(_segment(2, "[ Alpha ]", "paragraph")),
        SegmentInput(
            _segment(3, "Metric=1 Cost=2 Alpha supports the first outcome.", "paragraph"),
            (
                SegmentClaim(
                    "claim-alpha",
                    "Alpha supports the first outcome.",
                    certainty="supported",
                    evidence_ids=("ev-3",),
                ),
            ),
        ),
        SegmentInput(_segment(4, "[ Beta ]", "paragraph")),
        SegmentInput(
            _segment(5, "Metric=3 Cost=4 Beta supports the second outcome.", "paragraph"),
            (
                SegmentClaim(
                    "claim-beta",
                    "Beta supports the second outcome.",
                    certainty="supported",
                    evidence_ids=("ev-5",),
                ),
            ),
        ),
    )
    result = build_claim_ledger(
        source_locator="synthetic.pdf",
        source_hash="abc",
        evidence_registry_hash="registry",
        segments=inputs,
        profiles=_profiles(inputs),
        schema=default_schema_bundle(),
    )

    alpha = next(
        node for node in result.document_structure.structure_nodes if node.heading_text == "Alpha"
    )
    beta = next(
        node for node in result.document_structure.structure_nodes if node.heading_text == "Beta"
    )

    alpha_entries = [
        entry
        for entry in result.ledger.entries
        if alpha.structure_node_id in entry.structure_node_ids
    ]
    beta_entries = [
        entry
        for entry in result.ledger.entries
        if beta.structure_node_id in entry.structure_node_ids
    ]

    assert alpha_entries
    assert beta_entries
    assert all("Beta" not in entry.source_text for entry in alpha_entries)
    assert all("Alpha" not in entry.source_text for entry in beta_entries)


def _profiles(inputs: tuple[SegmentInput, ...]) -> dict[str, ExtractedUnitProfile]:
    return {
        item.segment.segment_id: profile_unit(
            extracted_unit_id=item.segment.segment_id,
            source_range_id=item.segment.source_range_id,
            text=item.segment.text,
            evidence_ids=item.segment.evidence_ids,
        )
        for item in inputs
    }

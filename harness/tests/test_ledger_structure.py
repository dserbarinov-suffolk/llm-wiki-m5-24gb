from llmwiki.domain.ledger.segments import SourceSegment
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

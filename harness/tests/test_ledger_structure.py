from llmwiki.domain.ledger.segments import SourceSegment
from llmwiki.domain.ledger.structure_build import build_structure


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

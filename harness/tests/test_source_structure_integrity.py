from llmwiki.domain.ledger.source_structure_integrity import (
    HeadingCandidate,
    heading_admission,
    source_structure_integrity_report,
    structure_node_can_drive_pages,
)
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode


def test_heading_admission_accepts_clean_structural_heading() -> None:
    decision = heading_admission(
        HeadingCandidate("h1", "3.2 Configure Output", 2, 14.0, 9.0)
    )

    assert decision.admitted
    assert decision.admission_kind == "trusted-heading"


def test_heading_admission_demotes_record_shaped_label_without_domain_terms() -> None:
    decision = heading_admission(
        HeadingCandidate(
            "h1",
            "Luma Rate=2 Cost=4 Range=near Duration=short",
            1,
            14.0,
            9.0,
        )
    )

    assert not decision.admitted
    assert decision.admission_kind == "record-label"
    assert "field-dense" in decision.reason_codes


def test_heading_admission_demotes_bracket_wrapped_record_label() -> None:
    decision = heading_admission(HeadingCandidate("h1", "[ Luma ]", 1, 14.0, 9.0))

    assert not decision.admitted
    assert decision.admission_kind == "record-label"
    assert "bracket-wrapped-label" in decision.reason_codes


def test_heading_admission_demotes_delimiter_fragment_without_domain_terms() -> None:
    decision = heading_admission(
        HeadingCandidate("h1", "[ Change Shape", 1, 14.0, 9.0)
    )

    assert not decision.admitted
    assert decision.admission_kind == "fragment"


def test_structure_node_with_record_shape_cannot_drive_pages() -> None:
    node = StructureNode(
        "n1",
        "section",
        "[ Luma ] Rate=2 Cost=4 Range=near",
        "r1",
        "synthetic.pdf",
        1,
        1,
        "root",
    )

    assert not structure_node_can_drive_pages(node)


def test_integrity_report_warns_when_numbered_heading_escapes_nearest_numbered_ancestor() -> None:
    structure = DocumentStructure(
        "root",
        (
            _node("root", "root", "Manual", 0, 0, ""),
            _node("n1", "heading", "2.3.4 Nested Topic", 3, 1, "root"),
            _node("n2", "section", "2.4.1 Sibling Topic", 2, 2, "n1"),
        ),
    )

    report = source_structure_integrity_report(structure)

    assert any(
        finding.structure_node_id == "n2"
        and "number path is not a descendant" in finding.message
        for finding in report.findings
    )


def test_integrity_report_warns_when_top_level_heading_is_under_numbered_subsection() -> None:
    structure = DocumentStructure(
        "root",
        (
            _node("root", "root", "Manual", 0, 0, ""),
            _node("n1", "heading", "2.3.4 Nested Topic", 3, 1, "root"),
            _node("n2", "chapter", "New Major Topic", 1, 2, "n1"),
        ),
    )

    report = source_structure_integrity_report(structure)

    assert any(
        finding.structure_node_id == "n2"
        and "Top-level heading" in finding.message
        for finding in report.findings
    )


def test_integrity_report_accepts_valid_numbered_descendant() -> None:
    structure = DocumentStructure(
        "root",
        (
            _node("root", "root", "Manual", 0, 0, ""),
            _node("n1", "heading", "2.3 Parent", 1, 1, "root"),
            _node("n2", "heading", "2.3.4 Nested Topic", 3, 2, "n1"),
            _node("n3", "heading", "2.3.4.1 Detail", 4, 3, "n2"),
        ),
    )

    report = source_structure_integrity_report(structure)

    assert not report.findings


def _node(
    node_id: str,
    kind: str,
    heading: str,
    depth: int,
    order: int,
    parent: str,
) -> StructureNode:
    return StructureNode(
        node_id,
        kind,
        heading,
        f"range-{order}",
        "synthetic.pdf",
        order,
        depth,
        parent,
    )

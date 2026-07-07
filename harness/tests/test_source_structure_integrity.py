from llmwiki.domain.ledger.source_structure_integrity import (
    HeadingCandidate,
    heading_admission,
    structure_node_can_drive_pages,
)
from llmwiki.domain.ledger.structure import StructureNode


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

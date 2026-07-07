from llmwiki.domain.ledger.builder import (
    LedgerBuildResult,
    SegmentInput,
    build_claim_ledger,
    default_schema_bundle,
)
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.features import profile_unit
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.section_navigation import section_links_for_topics, section_page_id
from llmwiki.domain.ledger.section_pages import build_section_pages
from llmwiki.domain.ledger.section_planning import PageTarget, SectionGroundedPlan
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.ledger.topic_models import SourceTopic

_HASH = "abcdef1234567890"


def test_section_pages_roll_up_descendants_and_link_source_siblings() -> None:
    structure = DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode("chapter", "chapter", "1.4 Meter Setup", "r1", "source.pdf", 1),
            StructureNode(
                "field-sheet",
                "section",
                "Filling out the Reading Sheet",
                "r2",
                "source.pdf",
                2,
                parent_structure_node_id="chapter",
            ),
            StructureNode(
                "lab-sheet",
                "section",
                "Filling out the Reading Sheet",
                "r3",
                "source.pdf",
                3,
                parent_structure_node_id="chapter",
            ),
        ),
    )
    ledger = _ledger(
        _entry("entry-field", "field-sheet", "Write field totals on the sheet."),
        _entry("entry-lab", "lab-sheet", "Write lab fields on the sheet."),
    )
    pages = build_section_pages(
        ledger,
        structure,
        section_plan=_section_plan(structure, "chapter", "field-sheet", "lab-sheet"),
        source_page_id="source",
        source_locator="source.pdf",
        today="2026-06-29",
        topics=(
            SourceTopic(
                topic_key="filling-reading-sheet",
                label="Filling out the Reading Sheet",
                page_kind="concept",
                match_terms=("filling", "reading", "sheet"),
                entry_ids=("entry-field", "entry-lab"),
                atom_ids=(),
                from_heading=True,
                salience=5.0,
            ),
        ),
    )

    by_id = {page.page_id: page.page_body for page in pages}
    chapter = structure.node("chapter")
    field = structure.node("field-sheet")
    lab = structure.node("lab-sheet")
    assert chapter is not None
    assert field is not None
    assert lab is not None
    chapter_id = section_page_id("source", structure, chapter)
    field_id = section_page_id("source", structure, field)
    lab_id = section_page_id("source", structure, lab)

    assert "# 1.4 Meter Setup" in by_id[chapter_id]
    assert "## Statements by subsection" not in by_id[chapter_id]
    assert "Write field totals on the sheet." not in by_id[chapter_id]
    assert "Write lab fields on the sheet." not in by_id[chapter_id]
    assert f"[[{field_id}]] - narrower source section" in by_id[chapter_id]
    assert f"[[{lab_id}]] - narrower source section" in by_id[chapter_id]

    assert "# 1.4 Meter Setup / Filling out the Reading Sheet" in by_id[field_id]
    assert f"[[{chapter_id}]] - broader source section: 1.4 Meter Setup" in by_id[field_id]
    assert (
        "[[source-filling-reading-sheet]] - topic hub: opens the topic page for "
        "Filling Reading Sheet" in by_id[field_id]
    )
    assert (
        f"[[{lab_id}]] - next source section: "
        "1.4 Meter Setup / Filling out the Reading Sheet" in by_id[field_id]
    )
    assert "same source heading" not in by_id[field_id]


def test_section_pages_do_not_import_same_named_table_from_sibling_branch() -> None:
    result = _build_result(
        [
            ("heading", "# First Branch", []),
            ("heading", "## Shared Matrix", []),
            (
                "table-block",
                "Shared Matrix\nValue Meaning\n1 First branch value\n2 First branch option",
                [],
            ),
            ("heading", "# Second Branch", []),
            ("heading", "## Shared Matrix", []),
            (
                "paragraph",
                "The second branch describes a separate matrix.",
                ["The second branch describes a separate matrix."],
            ),
        ]
    )

    first = _node_by_path(result.document_structure, ("First Branch", "Shared Matrix"))
    second = _node_by_path(result.document_structure, ("Second Branch", "Shared Matrix"))
    assert first is not None
    assert second is not None
    pages = build_section_pages(
        result.ledger,
        result.document_structure,
        section_plan=_section_plan(
            result.document_structure,
            first.structure_node_id,
            second.structure_node_id,
        ),
        source_page_id="source",
        source_locator="source.pdf",
        today="2026-06-29",
    )
    by_id = {page.page_id: page.page_body for page in pages}

    assert (
        "First branch value" in by_id[section_page_id("source", result.document_structure, first)]
    )
    assert (
        "First branch value"
        not in by_id[section_page_id("source", result.document_structure, second)]
    )
    assert (
        "## Technical atoms"
        not in by_id[section_page_id("source", result.document_structure, second)]
    )


def test_section_pages_roll_unpromoted_leaf_into_promoted_parent_only() -> None:
    structure = DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode("chapter", "chapter", "Process", "r1", "source.pdf", 1),
            StructureNode(
                "thin-step",
                "heading",
                "Thin Step",
                "r2",
                "source.pdf",
                2,
                parent_structure_node_id="chapter",
            ),
            StructureNode(
                "major-step",
                "section",
                "Major Step",
                "r3",
                "source.pdf",
                3,
                parent_structure_node_id="chapter",
            ),
        ),
    )
    ledger = _ledger(
        _entry("entry-thin", "thin-step", "The thin step has one supporting statement."),
        _entry("entry-major", "major-step", "The major step has its own page evidence."),
    )

    pages = build_section_pages(
        ledger,
        structure,
        section_plan=_section_plan(structure, "chapter", "major-step"),
        source_page_id="source",
        source_locator="source.pdf",
        today="2026-06-29",
    )

    by_id = {page.page_id: page.page_body for page in pages}
    chapter = structure.node("chapter")
    major = structure.node("major-step")
    assert chapter is not None
    assert major is not None
    chapter_body = by_id[section_page_id("source", structure, chapter)]
    major_body = by_id[section_page_id("source", structure, major)]

    assert "The thin step has one supporting statement." in chapter_body
    assert "The major step has its own page evidence." not in chapter_body
    assert "The major step has its own page evidence." in major_body
    assert all("thin-step" not in page_id for page_id in by_id)


def test_promoted_parent_does_not_render_promoted_child_table_atom() -> None:
    result = _build_result(
        [
            ("heading", "# Parent Section", []),
            ("heading", "## Child Matrix", []),
            (
                "table-block",
                "Child Matrix\nValue Meaning\n1 Child-only value\n2 Child-only option",
                [],
            ),
        ]
    )
    parent = _node_by_path(result.document_structure, ("Parent Section",))
    child = _node_by_path(result.document_structure, ("Parent Section", "Child Matrix"))
    assert parent is not None
    assert child is not None

    pages = build_section_pages(
        result.ledger,
        result.document_structure,
        section_plan=_section_plan(
            result.document_structure,
            parent.structure_node_id,
            child.structure_node_id,
        ),
        source_page_id="source",
        source_locator="source.pdf",
        today="2026-06-29",
    )
    by_id = {page.page_id: page.page_body for page in pages}

    parent_body = by_id[section_page_id("source", result.document_structure, parent)]
    child_body = by_id[section_page_id("source", result.document_structure, child)]
    assert "Child-only value" not in parent_body
    assert "Child-only value" in child_body
    assert "narrower source section" in parent_body


def test_sparse_topic_links_to_matching_source_section_hub() -> None:
    structure = DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode("magic", "chapter", "Basic Rules of Magic", "r1", "source.pdf", 1),
        ),
    )
    plan = _section_plan(structure, "magic")
    topic = SourceTopic(
        topic_key="magic",
        label="Magic",
        page_kind="concept",
        match_terms=("magic",),
        entry_ids=("entry-magic",),
        atom_ids=(),
        from_heading=False,
        salience=1.0,
    )

    links = section_links_for_topics(plan, structure, source_page_id="source", topics=(topic,))

    assert "magic" in links
    assert any(link.label == "Basic Rules of Magic" for link in links["magic"])


def _entry(entry_id: str, node_id: str, text: str) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=f"statement-{entry_id}",
        ledger_entry_kind="claim",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="source.pdf",
        source_hash="sourcehash",
        source_range_id=f"range-{entry_id}",
        evidence_ids=(f"ev-{entry_id}",),
        source_text=text,
        structure_node_ids=(node_id, "chapter", "root"),
        normalized_text=text,
        subject=text,
        predicate="is",
        object_value=text,
        polarity="positive",
        claim_force="asserted",
    )


def _ledger(*entries: LedgerEntry) -> ClaimLedger:
    return ClaimLedger(
        claim_ledger_id="ledger",
        source_locator="source.pdf",
        source_hash="sourcehash",
        evidence_registry_hash="registry",
        source_profile=SourceProfile(
            source_locator="source.pdf",
            unit_count=1,
            accepted_entry_count=len(entries),
            claim_count=len(entries),
            event_count=0,
            concept_count=0,
            relationship_count=0,
            atom_kind_counts={},
            feature_signal_means={},
        ),
        source_family_assignment=SourceFamilyAssignment(
            labels=(FamilyLabelScore("general-prose", 1.0),),
            assignment_confidence=1.0,
        ),
        entries=entries,
        technical_atoms=(),
        technical_atom_contexts=(),
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )


def _section_plan(structure: DocumentStructure, *node_ids: str) -> SectionGroundedPlan:
    targets: list[PageTarget] = []
    for index, node_id in enumerate(node_ids, start=1):
        node = structure.node(node_id)
        assert node is not None
        targets.append(
            PageTarget(
                page_target_id=f"target-{index}",
                topic_key=node_id,
                label=node.heading_text,
                page_kind="concept",
                structure_node_id=node.structure_node_id,
                source_range_id=node.source_range_id,
                concept_keys=(),
                entry_ids=(),
                atom_ids=(),
                attached_evidence=(),
            )
        )
    return SectionGroundedPlan(
        "section-plan",
        "fingerprint",
        "source.pdf",
        "sourcehash",
        tuple(targets),
        (),
    )


def _build_result(specs: list[tuple[str, str, list[str]]]) -> LedgerBuildResult:
    inputs: list[SegmentInput] = []
    profiles = {}
    for order, (kind, text, claims) in enumerate(specs, start=1):
        segment = SourceSegment(
            segment_id=f"seg-{order:03d}",
            source_range_id=f"sr-{order:03d}",
            source_locator="source.pdf",
            source_hash=_HASH,
            heading_path="H",
            structure_node_id="",
            source_order=order,
            text=text,
            segment_kind=kind,
            evidence_ids=(f"ev-{order:03d}",),
        )
        claim_records = tuple(
            SegmentClaim(
                f"claim-{order}-{index}", claim, (), "eligible", "supported", segment.evidence_ids
            )
            for index, claim in enumerate(claims)
        )
        inputs.append(SegmentInput(segment, claim_records))
        profiles[segment.segment_id] = profile_unit(
            extracted_unit_id=segment.segment_id,
            source_range_id=segment.source_range_id,
            text=text,
            evidence_ids=segment.evidence_ids,
        )
    return build_claim_ledger(
        source_locator="source.pdf",
        source_hash=_HASH,
        evidence_registry_hash="registry",
        segments=tuple(inputs),
        profiles=profiles,
        schema=default_schema_bundle(),
    )


def _node_by_path(structure: DocumentStructure, path: tuple[str, ...]) -> StructureNode | None:
    for node in structure.structure_nodes:
        if structure.label_path(node.structure_node_id) == path:
            return node
    return None

from llmwiki.domain.ledger.atoms import TechnicalAtom, WorkedExamplePayload
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry, SourceStatement
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.procedure_pages import render_procedure_page
from llmwiki.domain.ledger.procedures import plan_procedure_guides
from llmwiki.domain.ledger.section_planning import PageTarget, SectionGroundedPlan
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode


def test_conditional_branch_becomes_typed_decision_point() -> None:
    guide = _single_guide(
        _entry("choose", "choose", "First, choose the input value.", role_tags=("procedure",)),
        _entry(
            "branch",
            "choose",
            "If the input value is unavailable, choose a fallback value.",
            condition_scope="conditional",
            condition_text="If the input value is unavailable, choose a fallback value.",
            role_tags=("requirement",),
        ),
        _entry("record", "record", "Finally, record the output.", role_tags=("procedure",)),
    )

    assert [point.decision_kind for point in guide.decision_points] == ["branch"]
    assert "If the input value is unavailable" in render_procedure_page(guide, "book")


def test_conditional_worked_example_is_not_a_decision_point() -> None:
    guide = _single_guide(
        _entry("choose", "choose", "First, choose the input value.", role_tags=("procedure",)),
        _entry(
            "example",
            "choose",
            "If the sample roll is high, this sample output is unusually strong.",
            condition_scope="conditional",
            condition_text="If the sample roll is high, this sample output is unusually strong.",
            role_tags=("worked-example", "quantitative"),
        ),
        _entry("record", "record", "Finally, record the output.", role_tags=("procedure",)),
    )

    assert guide.decision_points == ()


def test_example_atom_with_except_is_not_a_decision_point() -> None:
    guide = _single_guide(
        _entry("choose", "choose", "First, choose the input value.", role_tags=("procedure",)),
        _entry(
            "example",
            "choose",
            "This sample output is average except for one excellent attribute.",
            role_tags=("quantitative", "identity"),
            range_id="range-example",
        ),
        _entry("record", "record", "Finally, record the output.", role_tags=("procedure",)),
        atoms=(_worked_example_atom("range-example"),),
    )

    assert all("sample output" not in point.outcome_text for point in guide.decision_points)
    assert "## Decision Points" not in render_procedure_page(guide, "book")


def test_contextual_decision_projection_includes_previous_source_statement() -> None:
    guide = _single_guide(
        _entry(
            "setup",
            "choose",
            "Do not use the heavy option.",
            range_id="range-00001",
            role_tags=("requirement",),
        ),
        _entry("choose", "choose", "First, choose the input value.", role_tags=("procedure",)),
        _entry("inspect", "choose", "Inspect the input value.", role_tags=("procedure",)),
        _entry("label", "choose", "Label the input value.", role_tags=("procedure",)),
        _entry(
            "tail-branch",
            "choose",
            (
                "When choosing an option, since you are not using the heavy option, "
                "choose the light option."
            ),
            range_id="range-00002",
            condition_scope="conditional",
            condition_text="When choosing an option",
            role_tags=("requirement",),
        ),
        _entry("record", "record", "Finally, record the output.", role_tags=("procedure",)),
        source_statements=(
            SourceStatement("statement-setup", "range-00001", "Do not use the heavy option."),
            SourceStatement(
                "statement-tail-branch",
                "range-00002",
                (
                    "When choosing an option, since you are not using the heavy option, "
                    "choose the light option."
                ),
            ),
        ),
    )

    rendered = render_procedure_page(guide, "book")

    assert "Do not use the heavy option. When choosing an option" in rendered


def test_unresolved_reference_conditions_are_not_decision_points() -> None:
    guide = _single_guide(
        _entry("choose", "choose", "First, choose the input value.", role_tags=("procedure",)),
        _entry(
            "fragment",
            "choose",
            "As long as you choose that, use the same output.",
            condition_scope="conditional",
            condition_text="As long as you choose that",
            role_tags=("requirement",),
        ),
        _entry("record", "record", "Finally, record the output.", role_tags=("procedure",)),
    )

    assert guide.decision_points == ()


def _single_guide(
    *entries: LedgerEntry,
    atoms: tuple[TechnicalAtom, ...] = (),
    source_statements: tuple[SourceStatement, ...] = (),
):
    structure = _structure()
    guides = plan_procedure_guides(
        _ledger(*entries, atoms=atoms, source_statements=source_statements),
        structure,
        source_page_id="book",
        section_plan=_section_plan(structure),
    )
    assert len(guides) == 1
    return guides[0]


def _structure() -> DocumentStructure:
    return DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "book.pdf", "root", "book.pdf", 0),
            StructureNode("workflow", "section", "1 Create Output", "r1", "book.pdf", 1),
            StructureNode(
                "choose",
                "section",
                "1.1 Choose Input",
                "r2",
                "book.pdf",
                2,
                parent_structure_node_id="workflow",
            ),
            StructureNode(
                "record",
                "section",
                "1.2 Record Output",
                "r3",
                "book.pdf",
                3,
                parent_structure_node_id="workflow",
            ),
        ),
    )


def _section_plan(structure: DocumentStructure) -> SectionGroundedPlan:
    targets: list[PageTarget] = []
    for index, node in enumerate(structure.structure_nodes, start=1):
        if node.structure_node_kind == "root":
            continue
        targets.append(
            PageTarget(
                page_target_id=f"target-{index}",
                topic_key=node.structure_node_id,
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
    return SectionGroundedPlan("plan", "fingerprint", "book.pdf", "hash", tuple(targets), ())


def _entry(
    entry_id: str,
    node_id: str,
    text: str,
    *,
    range_id: str | None = None,
    role_tags: tuple[str, ...] = (),
    condition_scope: str = "unconditional",
    condition_text: str = "",
) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=f"statement-{entry_id}",
        ledger_entry_kind="claim",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="book.pdf",
        source_hash="sourcehash",
        source_range_id=range_id or f"range-{entry_id}",
        evidence_ids=(f"ev-{entry_id}",),
        source_text=text,
        structure_node_ids=(node_id, "workflow", "root"),
        normalized_text=text,
        subject=text,
        predicate="is",
        object_value=text,
        polarity="positive",
        claim_force="asserted",
        condition_scope=condition_scope,
        condition_text=condition_text,
        claim_role_tags=role_tags,
    )


def _worked_example_atom(source_range_id: str) -> TechnicalAtom:
    return TechnicalAtom(
        technical_atom_id="example-atom",
        technical_atom_kind="worked-example",
        payload=WorkedExamplePayload(
            example_text="This sample output is average except for one excellent attribute.",
            source_locator="book.pdf",
        ),
        source_locator="book.pdf",
        source_range_id=source_range_id,
        evidence_ids=("ev-example",),
    )


def _ledger(
    *entries: LedgerEntry,
    atoms: tuple[TechnicalAtom, ...] = (),
    source_statements: tuple[SourceStatement, ...] = (),
) -> ClaimLedger:
    return ClaimLedger(
        claim_ledger_id="ledger",
        source_locator="book.pdf",
        source_hash="sourcehash",
        evidence_registry_hash="registryhash",
        source_profile=SourceProfile(
            "book.pdf", len(entries), len(entries), len(entries), 0, 0, 0, {}, {}
        ),
        source_family_assignment=SourceFamilyAssignment((FamilyLabelScore("technical", 1.0),), 1.0),
        entries=entries,
        technical_atoms=atoms,
        technical_atom_contexts=(),
        source_statements=source_statements,
        extractor_decisions=(),
        rejected_candidates=(),
    )

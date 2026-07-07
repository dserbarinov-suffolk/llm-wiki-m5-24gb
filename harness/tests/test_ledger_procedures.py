from llmwiki.domain.ledger.atoms import TablePayload, TechnicalAtom
from llmwiki.domain.ledger.common import ConfidenceBasis, ReviewReason
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.procedure_pages import build_procedure_pages
from llmwiki.domain.ledger.procedures import plan_procedure_guides
from llmwiki.domain.ledger.section_planning import PageTarget, SectionGroundedPlan
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.search import search_pages


def test_procedure_guides_surface_ordered_task_sections() -> None:
    structure = _structure()
    pages = build_procedure_pages(
        _ledger(
            _entry("race", "choose-race", "First, the character's race must be chosen."),
            _entry("scores", "scores", "Next, roll dice and calculate ability scores."),
            _entry(
                "score-choice-a",
                "scores",
                "If choosing a mixed heritage, validate any skill restrictions.",
                range_id="range-score-choice",
                conditional=True,
            ),
            _entry(
                "score-choice-b",
                "scores",
                "If choosing a mixed heritage, validate any skill restrictions.",
                range_id="range-score-choice",
                conditional=True,
            ),
            _entry("skills", "skills", "Then spend experience points to increase skills."),
            _entry(
                "equipment",
                "equipment-detail",
                "Finally, purchase equipment and record money.",
            ),
            atoms=(_table_atom("background-table", "equipment"),),
        ),
        structure,
        source_page_id="book",
        source_locator="book.pdf",
        today="2026-06-30",
        section_plan=_section_plan(
            structure,
            "creation",
            "choose-race",
            "scores",
            "skills",
            "skill-detail",
            "equipment",
            "equipment-detail",
        ),
    )

    page = next(page for page in pages if page.page_id == "book-procedure-create-character")

    assert page.page_kind == "procedure"
    assert page.page_metadata.page_family == "procedure-guide"
    assert page.page_metadata.aliases == ("create-character", "character-creation")
    assert "# Create Character" in page.page_body
    assert "## Procedure Steps" in page.page_body
    assert "1. **Choose Race** (`choose`)" in page.page_body
    assert "2. **Determine Ability Scores** (`generate`)" in page.page_body
    assert "3. **Increase Skills Experience Points** (`allocate`)" in page.page_body
    assert "4. **Purchasing Other Equipment** (`acquire`)" in page.page_body
    assert page.page_body.count("If choosing a mixed heritage") == 1
    assert "## Authoritative Dependencies" in page.page_body
    assert "Table 1: Backgrounds" in page.page_body
    assert "[[book-section-1-4-character-creation" in page.page_body


def test_procedure_page_renders_complete_step_claim_closure() -> None:
    structure = _structure()
    pages = build_procedure_pages(
        _ledger(
            *(
                _entry(
                    f"race-detail-{index}",
                    "choose-race",
                    f"Step detail {index} belongs to the choose operation.",
                    role_tags=("procedure",),
                )
                for index in range(1, 7)
            ),
            _entry(
                "scores",
                "scores",
                "Next, roll dice and calculate ability scores.",
                role_tags=("procedure",),
            ),
            _entry(
                "skills",
                "skills",
                "Then spend experience points to increase skills.",
                role_tags=("procedure",),
            ),
            _entry(
                "equipment",
                "equipment-detail",
                "Finally, purchase equipment.",
                role_tags=("procedure",),
            ),
        ),
        structure,
        source_page_id="book",
        source_locator="book.pdf",
        today="2026-06-30",
        section_plan=_section_plan(
            structure,
            "creation",
            "choose-race",
            "scores",
            "skills",
            "skill-detail",
            "equipment",
            "equipment-detail",
        ),
    )

    page = next(page for page in pages if page.page_id == "book-procedure-create-character")

    for index in range(1, 7):
        assert f"Step detail {index} belongs to the choose operation." in page.page_body


def test_procedure_page_renders_complete_authoritative_dependency_closure() -> None:
    structure = _structure()
    atoms = tuple(_table_atom(f"background-table-{index}", "equipment") for index in range(1, 16))
    pages = build_procedure_pages(
        _ledger(
            _entry(
                "race",
                "choose-race",
                "First, the character's race must be chosen.",
                role_tags=("procedure",),
            ),
            _entry(
                "scores",
                "scores",
                "Next, roll dice and calculate ability scores.",
                role_tags=("procedure",),
            ),
            _entry(
                "skills",
                "skills",
                "Then spend experience points to increase skills.",
                role_tags=("procedure",),
            ),
            _entry(
                "equipment",
                "equipment-detail",
                "Finally, purchase equipment.",
                role_tags=("procedure",),
            ),
            atoms=atoms,
        ),
        structure,
        source_page_id="book",
        source_locator="book.pdf",
        today="2026-06-30",
        section_plan=_section_plan(
            structure,
            "creation",
            "choose-race",
            "scores",
            "skills",
            "skill-detail",
            "equipment",
            "equipment-detail",
        ),
    )

    page = next(page for page in pages if page.page_id == "book-procedure-create-character")

    assert page.page_body.count("`table`: [[") == 15
    assert "atom-background-table-15" in page.page_body
    assert "15 authoritative dependency reference(s)" in page.page_metadata.summary


def test_procedure_page_surfaces_review_only_dependencies_without_authoritative_links() -> None:
    structure = _structure()
    pages = build_procedure_pages(
        _ledger(
            _entry(
                "race",
                "choose-race",
                "First, the character's race must be chosen.",
                role_tags=("procedure",),
            ),
            _entry(
                "scores",
                "scores",
                "Next, roll dice and calculate ability scores.",
                role_tags=("procedure",),
            ),
            _entry(
                "skills",
                "skills",
                "Then spend experience points to increase skills.",
                role_tags=("procedure",),
            ),
            _entry(
                "equipment",
                "equipment-detail",
                "Finally, purchase equipment.",
                role_tags=("procedure",),
            ),
            atoms=(
                _table_atom(
                    "review-table",
                    "equipment",
                    range_id="range-00008",
                    trust_status="review-only",
                    projection_policy="raw-review-only",
                    trust_reasons=("table-parse-incomplete",),
                    review_reason=ReviewReason(
                        "table-parse-incomplete",
                        "The extracted grid is incomplete.",
                    ),
                ),
            ),
        ),
        structure,
        source_page_id="book",
        source_locator="book.pdf",
        today="2026-06-30",
        section_plan=_section_plan(
            structure,
            "creation",
            "choose-race",
            "scores",
            "skills",
            "skill-detail",
            "equipment",
            "equipment-detail",
        ),
    )

    page = next(page for page in pages if page.page_id == "book-procedure-create-character")

    assert "## Review-Only Dependencies" in page.page_body
    assert "table-parse-incomplete: The extracted grid is incomplete." in page.page_body
    assert "atom-review-table" not in page.page_body
    assert "1 review-only dependency reference(s)" in page.page_metadata.summary


def test_sparse_descriptive_sections_do_not_become_procedures() -> None:
    structure = DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "book.pdf", "root", "book.pdf", 0),
            StructureNode("lore", "section", "Citadel Lore", "r1", "book.pdf", 1),
        ),
    )
    guides = plan_procedure_guides(
        _ledger(_entry("lore", "lore", "The citadel is ancient and weathered.")),
        structure,
        source_page_id="book",
        section_plan=_section_plan(structure, "lore"),
    )

    assert guides == ()


def test_task_search_boosts_procedure_pages() -> None:
    pages = {
        "book-character": (
            "---\npage_id: book-character\npage_kind: concept\n"
            "summary: Character concept.\n---\n\nCharacter is a general concept."
        ),
        "book-procedure-create-character": (
            "---\npage_id: book-procedure-create-character\npage_kind: procedure\n"
            "summary: Create Character.\naliases: create-character, character-creation\n---\n\n"
            "# Create Character\n\n## Procedure Steps\n\n1. Choose a race."
        ),
    }

    hits = search_pages(pages, "how do I create a character")

    assert hits[0].page_id == "book-procedure-create-character"


def _structure() -> DocumentStructure:
    return DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "book.pdf", "root", "book.pdf", 0),
            StructureNode("creation", "section", "1.4 Character Creation", "r1", "book.pdf", 1),
            StructureNode(
                "choose-race",
                "section",
                "1.4.1 Choose Race",
                "r2",
                "book.pdf",
                2,
                parent_structure_node_id="creation",
            ),
            StructureNode(
                "scores",
                "section",
                "1.4.2 Determine Ability Scores",
                "r3",
                "book.pdf",
                3,
                parent_structure_node_id="creation",
            ),
            StructureNode(
                "skills",
                "section",
                "1.4.3 Increase Skills",
                "r4",
                "book.pdf",
                4,
                parent_structure_node_id="creation",
            ),
            StructureNode(
                "skill-detail",
                "section",
                "1.4.3 Increase Skills / Experience Points",
                "r4b",
                "book.pdf",
                5,
                parent_structure_node_id="skills",
            ),
            StructureNode(
                "equipment",
                "section",
                "1.4.4 Purchasing Other",
                "r5",
                "book.pdf",
                6,
                parent_structure_node_id="creation",
            ),
            StructureNode(
                "equipment-detail",
                "section",
                "Equipment",
                "r5b",
                "book.pdf",
                7,
                parent_structure_node_id="creation",
            ),
        ),
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
    return SectionGroundedPlan("plan", "fingerprint", "book.pdf", "hash", tuple(targets), ())


def _entry(
    entry_id: str,
    node_id: str,
    text: str,
    *,
    range_id: str | None = None,
    conditional: bool = False,
    role_tags: tuple[str, ...] = (),
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
        structure_node_ids=(node_id, "creation", "root"),
        normalized_text=text,
        subject=text,
        predicate="is",
        object_value=text,
        polarity="positive",
        claim_force="asserted",
        condition_scope="conditional" if conditional else "",
        condition_text=text if conditional else "",
        claim_role_tags=role_tags,
    )


def _table_atom(
    atom_id: str,
    node_id: str,
    *,
    range_id: str = "range-table",
    trust_status: str = "trusted",
    projection_policy: str = "authoritative",
    trust_reasons: tuple[str, ...] = (),
    review_reason: ReviewReason | None = None,
) -> TechnicalAtom:
    _ = node_id
    return TechnicalAtom(
        technical_atom_id=atom_id,
        technical_atom_kind="table",
        payload=TablePayload(
            raw_table_text="Table 1: Backgrounds\nRoll | Result",
            parse_status="parsed",
            source_locator="book.pdf",
        ),
        source_locator="book.pdf",
        source_range_id=range_id,
        evidence_ids=("ev-table",),
        trust_status=trust_status,
        trust_reasons=trust_reasons,
        projection_policy=projection_policy,
        review_reason=review_reason,
    )


def _ledger(*entries: LedgerEntry, atoms: tuple[TechnicalAtom, ...] = ()) -> ClaimLedger:
    atom_entries = tuple(
        LedgerEntry(
            ledger_entry_id=f"entry-{atom.technical_atom_id}",
            source_statement_id=f"statement-{atom.technical_atom_id}",
            ledger_entry_kind="technical-atom",
            extraction_confidence="high",
            confidence_basis=ConfidenceBasis("test"),
            source_locator="book.pdf",
            source_hash="sourcehash",
            source_range_id=atom.source_range_id,
            evidence_ids=atom.evidence_ids,
            source_text="",
            structure_node_ids=("equipment", "creation", "root"),
            ledger_entry_status="usable"
            if atom.trust_status == "trusted" and atom.projection_policy == "authoritative"
            else "needs-review",
            technical_atom_kind=atom.technical_atom_kind,
            technical_atom_id=atom.technical_atom_id,
        )
        for atom in atoms
    )
    return ClaimLedger(
        claim_ledger_id="ledger",
        source_locator="book.pdf",
        source_hash="sourcehash",
        evidence_registry_hash="registry",
        source_profile=SourceProfile(
            source_locator="book.pdf",
            unit_count=1,
            accepted_entry_count=len(entries) + len(atom_entries),
            claim_count=len(entries),
            event_count=0,
            concept_count=0,
            relationship_count=0,
            atom_kind_counts={atom.technical_atom_kind: 1 for atom in atoms},
            feature_signal_means={},
        ),
        source_family_assignment=SourceFamilyAssignment(
            labels=(FamilyLabelScore("general-prose", 1.0),),
            assignment_confidence=1.0,
        ),
        entries=(*entries, *atom_entries),
        technical_atoms=atoms,
        technical_atom_contexts=(),
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )

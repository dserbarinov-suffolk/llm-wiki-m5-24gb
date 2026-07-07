from llmwiki.domain.ledger.atoms import CodeBlockPayload, FormulaPayload, TablePayload
from llmwiki.domain.ledger.builder import build_claim_ledger, default_schema_bundle
from llmwiki.domain.objects import Schema
from llmwiki.pdf.document import DocumentElement, DocumentModel, SourceUnit, SourceUnitBlock
from llmwiki.runtime.source_unit_segmentation import segment_source_units


def _element(
    element_id: str,
    element_kind: str,
    heading_path: str,
    text: str,
    *,
    page: int = 1,
    heading_level: int = 0,
    body_state: str = "body",
) -> DocumentElement:
    markdown = f"{'#' * heading_level} {text}" if element_kind == "heading" else text
    return DocumentElement(
        element_id=element_id,
        element_kind=element_kind,
        body_state=body_state,
        heading_path=heading_path,
        page_start=page,
        page_end=page,
        text=text,
        markdown=markdown,
        heading_level=heading_level,
    )


def _model(elements: tuple[DocumentElement, ...]) -> DocumentModel:
    return DocumentModel(
        source_locator="generic.pdf",
        source_hash="a" * 64,
        extractor_name="test",
        extractor_version="test",
        elements=elements,
    )


def _source_units(model: DocumentModel) -> tuple[SourceUnit, ...]:
    blocks = tuple(_block(element) for element in model.elements if element.body_state == "body")
    return (
        SourceUnit(
            unit_id="unit-0001",
            source_section_id="section-0001",
            heading_path=blocks[0].heading_path if blocks else "Document",
            page_start=min((block.page_start for block in blocks), default=0),
            page_end=max((block.page_end for block in blocks), default=0),
            element_ids=tuple(block.element_id for block in blocks),
            blocks=blocks,
            token_estimate=0,
        ),
    )


def _block(element: DocumentElement) -> SourceUnitBlock:
    text = (element.text or "").strip()
    return SourceUnitBlock(
        element_id=element.element_id,
        block_kind=element.element_kind,
        heading_path=element.heading_path,
        page_start=element.page_start,
        page_end=element.page_end,
        text=text,
        code_text=text if element.element_kind == "code_block" else "",
        table_text=(element.markdown or text).strip() if element.element_kind == "table" else "",
        formula_text=text if element.element_kind == "formula" else "",
        heading_level=element.heading_level if element.element_kind == "heading" else 0,
    )


def _segment_model(model: DocumentModel, source_hash: str):
    return segment_source_units(
        _source_units(model), source_locator="generic.pdf", source_hash=source_hash, schema=Schema()
    )


def _ledger_for_model(model: DocumentModel, source_hash: str = "k" * 64):
    inputs, profiles = _segment_model(model, source_hash)
    return build_claim_ledger(
        source_locator="generic.pdf",
        source_hash=source_hash,
        evidence_registry_hash="registry",
        segments=inputs,
        profiles=profiles,
        schema=default_schema_bundle(),
    ).ledger


def test_document_model_segmentation_groups_heading_scoped_table_rows() -> None:
    model = _model(
        (
            _element("e1", "heading", "Outcome Matrix", "Outcome Matrix", heading_level=1),
            _element("e2", "heading", "Score Result", "Score Result", heading_level=2),
            _element(
                "e3",
                "paragraph",
                "Outcome Matrix > Score Result",
                "The row number identifies the result.",
            ),
            _element("e4", "list_item", "Outcome Matrix > Score Result", "2 Fractured axle"),
            _element("e5", "paragraph", "Outcome Matrix > Score Result", "Loose wheel"),
            _element("e6", "list_item", "Outcome Matrix > Score Result", "3 requires a repair"),
            _element("e7", "list_item", "Outcome Matrix > Score Result", "4 Stable frame"),
            _element("e8", "heading", "Aftermath", "Aftermath", heading_level=1),
        )
    )

    inputs, _profiles = _segment_model(model, "b" * 64)

    kinds = [item.segment.segment_kind for item in inputs]
    assert kinds == ["heading", "heading", "table-block", "heading"]
    table = inputs[2].segment.text
    assert "Score Result" in table
    assert "2 Fractured axle" in table
    assert "Loose wheel" in table
    assert "4 Stable frame" in table


def test_source_unit_segmentation_preserves_heading_depth() -> None:
    model = _model(
        (
            _element("e1", "heading", "Parent", "Parent", heading_level=1),
            _element("e2", "heading", "Parent > Child", "Child", heading_level=2),
        )
    )

    inputs, _profiles = _segment_model(model, "d" * 64)

    assert [item.segment.text for item in inputs] == ["# Parent", "## Child"]


def test_document_model_segmentation_groups_inline_enumerated_rows() -> None:
    model = _model(
        (
            _element("e1", "heading", "Catalog", "Catalog", heading_level=1),
            _element(
                "e2",
                "paragraph",
                "Catalog",
                "9 Alpha entry. 10 Beta entry. 11 Gamma entry. 12 Delta entry.",
            ),
        )
    )

    inputs, _profiles = _segment_model(model, "c" * 64)

    assert [item.segment.segment_kind for item in inputs] == ["heading", "table-block"]
    assert "9 Alpha entry" in inputs[1].segment.text


def test_document_model_segmentation_preserves_table_section_heading_for_structure() -> None:
    model = _model(
        (
            _element("e1", "heading", "Character Traits", "Character Traits", heading_level=2),
            _element("e2", "paragraph", "Character Traits", "1 Angular face"),
            _element("e3", "list_item", "Character Traits", "2 Scarred face"),
            _element("e4", "heading", "Bonds", "Bonds", heading_level=2),
            _element("e5", "paragraph", "Bonds", "1 Inherited a worn map"),
            _element("e6", "list_item", "Bonds", "2 Owe a debt to a stranger"),
        )
    )

    inputs, profiles = _segment_model(model, "g" * 64)
    result = build_claim_ledger(
        source_locator="generic.pdf",
        source_hash="g" * 64,
        evidence_registry_hash="registry",
        segments=inputs,
        profiles=profiles,
        schema=default_schema_bundle(),
    )

    table_entry = next(
        entry
        for entry in result.ledger.entries
        if entry.technical_atom_kind == "table" and "Inherited a worn map" in entry.source_text
    )
    nearest = result.document_structure.node(table_entry.structure_node_ids[0])

    assert nearest is not None
    assert nearest.heading_text == "Bonds"


def test_document_model_segmentation_keeps_wrapped_numbered_table_together() -> None:
    model = _model(
        (
            _element("e1", "heading", "Results", "Results", heading_level=2),
            _element("e2", "paragraph", "Results", "1 First result starts here"),
            _element("e3", "paragraph", "Results", "and continues without a marker"),
            _element("e4", "paragraph", "Results", "with one more wrapped line"),
            _element("e5", "paragraph", "Results", "with a third wrapped line"),
            _element("e6", "paragraph", "Results", "with a fourth wrapped line"),
            _element("e7", "list_item", "Results", "2 Second result starts here"),
            _element("e8", "paragraph", "Results", "Closing prose is outside the table."),
        )
    )

    inputs, _profiles = _segment_model(model, "i" * 64)

    assert [item.segment.segment_kind for item in inputs] == [
        "heading",
        "table-block",
        "paragraph",
    ]
    assert "with one more wrapped line" in inputs[1].segment.text
    assert "with a fourth wrapped line" in inputs[1].segment.text
    assert "2 Second result starts here" in inputs[1].segment.text


def test_document_model_segmentation_keeps_table_caption_as_atom_text_only() -> None:
    model = _model(
        (
            _element("e1", "heading", "Table- Sample Matrix", "Table- Sample Matrix"),
            _element("e2", "paragraph", "Sample Matrix", "1 Alpha result"),
            _element("e3", "list_item", "Sample Matrix", "2 Beta result"),
        )
    )

    inputs, _profiles = _segment_model(model, "h" * 64)

    assert [item.segment.segment_kind for item in inputs] == ["table-block"]
    assert inputs[0].segment.text.startswith("Table- Sample Matrix")


def test_document_model_segmentation_does_not_cross_heading_path_into_recovered_table() -> None:
    model = _model(
        (
            _element("e1", "heading", "Process Cycle", "Process Cycle", heading_level=2),
            _element("e2", "list_item", "Process Cycle", "The operator describes the area."),
            _element("e3", "list_item", "Process Cycle", "The party chooses one action."),
            _element("e4", "list_item", "Process Cycle", "The cycle repeats."),
            _element(
                "e5",
                "table",
                "Event Results",
                "Event Results\n1 Encounter\n2 Sign",
            ),
        )
    )

    inputs, _profiles = _segment_model(model, "j" * 64)

    assert [item.segment.segment_kind for item in inputs] == [
        "heading",
        "list",
        "list",
        "list",
        "table-block",
    ]
    assert inputs[-1].segment.text == "Event Results\n1 Encounter\n2 Sign"


def test_document_model_segmentation_groups_range_value_rows() -> None:
    model = _model(
        (
            _element(
                "e1",
                "paragraph",
                "Range Table",
                "18-19 +4 20-21 +5 22-23 +6 24-25 +7",
            ),
        )
    )

    inputs, _profiles = _segment_model(model, "f" * 64)

    assert [item.segment.segment_kind for item in inputs] == ["table-block"]


def test_document_model_segmentation_rejects_incidental_prose_numbers_as_table() -> None:
    model = _model(
        (
            _element(
                "e1",
                "paragraph",
                "Combat Example",
                "The operator rolled a 1 and a 3. The target has 5 HP and 11 STR. "
                "The result causes 6 damage.",
            ),
        )
    )

    inputs, _profiles = _segment_model(model, "d" * 64)

    assert [item.segment.segment_kind for item in inputs] == ["paragraph"]


def test_document_model_segmentation_preserves_body_picture_as_figure() -> None:
    model = _model((_element("e1", "picture", "Illustrations", "", page=2),))

    inputs, _profiles = _segment_model(model, "e" * 64)

    assert [item.segment.segment_kind for item in inputs] == ["figure"]
    assert inputs[0].segment.source_element_ids == ("e1",)
    assert inputs[0].segment.text == "[Figure] (p.2)"


def test_source_unit_code_block_becomes_one_exact_code_atom() -> None:
    model = _model(
        (
            _element("e1", "paragraph", "Arrays", "Use this example to index an array."),
            _element(
                "e2",
                "code_block",
                "Arrays",
                "scores := [3]int{1, 2, 3}\nfmt.Println(scores[0])",
            ),
        )
    )

    ledger = _ledger_for_model(model)
    atoms = [atom for atom in ledger.technical_atoms if atom.technical_atom_kind == "code-block"]

    assert len(atoms) == 1
    payload = atoms[0].payload
    assert isinstance(payload, CodeBlockPayload)
    assert payload.raw_code_text == "scores := [3]int{1, 2, 3}\nfmt.Println(scores[0])"
    assert payload.line_count == 2
    assert atoms[0].source_unit_id == "unit-0001"
    assert atoms[0].source_block_ids == ("e2",)
    assert atoms[0].source_element_ids == ("e2",)
    assert atoms[0].source_page_start == 1
    assert atoms[0].source_page_end == 1
    context = next(
        context
        for context in ledger.technical_atom_contexts
        if context.technical_atom_id == atoms[0].technical_atom_id
    )
    assert context.context_text == "Use this example to index an array."


def test_source_unit_table_block_becomes_one_exact_table_atom() -> None:
    model = _model(
        (
            _element("e1", "paragraph", "Armor", "The following table lists armor statistics."),
            _element(
                "e2",
                "table",
                "Armor",
                "| Armor | Strength |\n| --- | --- |\n| Mail | 12 |",
            ),
        )
    )

    ledger = _ledger_for_model(model, "l" * 64)
    atoms = [atom for atom in ledger.technical_atoms if atom.technical_atom_kind == "table"]

    assert len(atoms) == 1
    payload = atoms[0].payload
    assert isinstance(payload, TablePayload)
    assert payload.raw_table_text == "| Armor | Strength |\n| --- | --- |\n| Mail | 12 |"
    assert len(payload.cells) == 2
    assert atoms[0].source_block_ids == ("e2",)


def test_source_unit_formula_block_becomes_one_exact_formula_atom() -> None:
    model = _model((_element("e1", "formula", "Damage", "total = base + modifier"),))

    ledger = _ledger_for_model(model, "m" * 64)
    atoms = [atom for atom in ledger.technical_atoms if atom.technical_atom_kind == "formula"]

    assert len(atoms) == 1
    assert isinstance(atoms[0].payload, FormulaPayload)
    assert atoms[0].payload.raw_formula_text == "total = base + modifier"
    assert atoms[0].source_block_ids == ("e1",)

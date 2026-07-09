"""Data-in/data-out tests for the pure claim-ledger DomainModule.

These exercise the load-bearing invariants from
docs/2026-06-25-claim-ledger-first-architecture.md: every segment gets exactly
one disposition, one extractor decision per capability, exact atom payload
preservation, claim-like proposition fields, the confidence/needs-review
routing, deterministic output, the quality report + write boundary, and the
Universal Standard (renamed-domain variants behave identically).
"""

from llmwiki.domain.ledger.artifacts import (
    PortableArtifactMember,
    build_portable_artifact_set,
)
from llmwiki.domain.ledger.atom_projection import atom_is_topic_projectable
from llmwiki.domain.ledger.atoms import (
    CodeBlockPayload,
    FigurePayload,
    FormulaPayload,
    RulePayload,
    TableCell,
    TableColumn,
    TablePayload,
    TableRow,
    TechnicalAtom,
)
from llmwiki.domain.ledger.builder import (
    LedgerBuildResult,
    SegmentInput,
    build_claim_ledger,
    default_schema_bundle,
)
from llmwiki.domain.ledger.canonical import canonical_json
from llmwiki.domain.ledger.features import profile_unit
from llmwiki.domain.ledger.ledger import SourceProfile
from llmwiki.domain.ledger.pointers import claim_ledger_pointer, document_structure_pointer
from llmwiki.domain.ledger.profiles import assign_family
from llmwiki.domain.ledger.projection import ProjectionSourceSupport, plan_source_page
from llmwiki.domain.ledger.quality import (
    build_ledger_quality_report,
    build_projection_quality_report,
    page_write_decision,
)
from llmwiki.domain.ledger.quality_catalog import (
    default_quality_check_catalog,
    default_severity_policy,
)
from llmwiki.domain.ledger.renderer import render_source_page
from llmwiki.domain.ledger.schemas import AtomValidator, default_atom_schema_set
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment
from llmwiki.domain.ledger.source_coverage import (
    SourceElementRecord,
    build_source_coverage,
)
from llmwiki.domain.ledger.vocab import (
    CALIBRATION_BUCKETS,
    EXTRACTED_UNIT_DISPOSITIONS,
    EXTRACTOR_CAPABILITY_IDS,
)

_HASH = "0123456789abcdef"


def _build(specs: list[tuple[str, str, list[str]]], source_hash: str = _HASH) -> LedgerBuildResult:
    inputs: list[SegmentInput] = []
    profiles = {}
    for order, (kind, text, claims) in enumerate(specs, start=1):
        seg = SourceSegment(
            segment_id=f"seg-{order:03d}",
            source_range_id=f"sr-{order:03d}",
            source_locator="src.pdf",
            source_hash=source_hash,
            heading_path="H",
            structure_node_id="",
            source_order=order,
            text=text,
            segment_kind=kind,
            evidence_ids=(f"ev-{order:03d}",),
            source_element_ids=(f"el-{order:03d}",),
        )
        claim_records = tuple(
            SegmentClaim(f"c-{order}-{i}", statement, (), "eligible", "supported", seg.evidence_ids)
            for i, statement in enumerate(claims)
        )
        inputs.append(SegmentInput(seg, claim_records))
        profiles[seg.segment_id] = profile_unit(
            extracted_unit_id=seg.segment_id,
            source_range_id=seg.source_range_id,
            text=text,
            evidence_ids=seg.evidence_ids,
        )
    return build_claim_ledger(
        source_locator="src.pdf",
        source_hash=source_hash,
        evidence_registry_hash="er-hash",
        segments=tuple(inputs),
        profiles=profiles,
        schema=default_schema_bundle(),
    )


_MIXED = [
    ("heading", "# Combat", []),
    ("paragraph", "A combatant must roll a die.", ["A combatant must roll a die."]),
    ("code-fence", "```python\n  x = 1\n    y = 2\n```", []),
    ("table-block", "1 alpha entry\n2 beta entry\n3 gamma entry", []),
    ("paragraph", "A grimoire contains many spells.", ["A grimoire contains many spells."]),
    (
        "paragraph",
        "Glossary plus assorted notation forms here.",
        ["assorted glossary notation forms"],
    ),
]


def test_every_segment_has_exactly_one_disposition() -> None:
    result = _build(_MIXED)
    dispositions = result.document_structure.dispositions
    assert len(dispositions) == len(_MIXED)
    assert all(record.disposition in EXTRACTED_UNIT_DISPOSITIONS for record in dispositions)
    # Headings are structural, never non-claim.
    heading = next(r for r in dispositions if r.source_range_id == "sr-001")
    assert heading.disposition == "structural"


def test_accepted_records_have_proposed_change_review_ids() -> None:
    result = _build(_MIXED)
    artifact = result.ledger.proposed_change_review

    assert artifact is not None
    assert result.ledger.entries
    assert result.ledger.technical_atoms
    assert all(entry.proposed_change_id.startswith("pcg_") for entry in result.ledger.entries)
    assert all(atom.proposed_change_id.startswith("pcg_") for atom in result.ledger.technical_atoms)
    assert artifact.approved_count >= len(result.ledger.entries) + len(
        result.ledger.technical_atoms
    )


def test_one_extractor_decision_per_capability_per_content_segment() -> None:
    result = _build(_MIXED)
    by_range: dict[str, set[str]] = {}
    for decision in result.ledger.extractor_decisions:
        by_range.setdefault(decision.source_range_id, set()).add(decision.extractor_capability_id)
    for capabilities in by_range.values():
        assert capabilities == set(EXTRACTOR_CAPABILITY_IDS)


def test_code_block_preserves_exact_text_including_whitespace() -> None:
    result = _build(_MIXED)
    code = next(a for a in result.ledger.technical_atoms if a.technical_atom_kind == "code-block")
    assert isinstance(code.payload, CodeBlockPayload)
    assert code.payload.raw_code_text == "  x = 1\n    y = 2"
    assert code.parse_status == "parsed"


def test_code_block_context_preserves_introductory_source_reason() -> None:
    result = _build(
        [
            ("heading", "# Arrays", []),
            ("paragraph", "We can initialize the array with values:", []),
            ("code-fence", "```go\nscores := [4]int{9001, 9333}\n```", []),
        ]
    )
    code = next(a for a in result.ledger.technical_atoms if a.technical_atom_kind == "code-block")
    contexts = result.ledger.atom_contexts(code.technical_atom_id)

    assert len(contexts) == 1
    assert contexts[0].context_role == "introduced-by-source-prose"
    assert contexts[0].context_text == "We can initialize the array with values:"
    assert "array" in contexts[0].demonstrated_concept_keys


def test_table_context_preserves_source_stated_table_purpose() -> None:
    result = _build(
        [
            ("heading", "# Armor", []),
            ("paragraph", "The Armor table shows cost and weight.", []),
            ("table-block", "1 Leather armor\n2 Chain armor", []),
        ]
    )
    table = next(a for a in result.ledger.technical_atoms if a.technical_atom_kind == "table")
    contexts = result.ledger.atom_contexts(table.technical_atom_id)

    assert len(contexts) == 1
    assert contexts[0].context_text == "The Armor table shows cost and weight."
    assert "armor" in contexts[0].demonstrated_concept_keys


def test_table_block_preserves_raw_text_with_partial_parse_review() -> None:
    result = _build(_MIXED)
    table = next(a for a in result.ledger.technical_atoms if a.technical_atom_kind == "table")
    assert isinstance(table.payload, TablePayload)
    assert table.payload.raw_table_text == "1 alpha entry\n2 beta entry\n3 gamma entry"
    assert table.parse_status == "partially-parsed"
    assert table.review_reason is not None
    assert table.payload.cells  # logical model recovered as enumerated rows


def test_spaced_column_table_preserves_one_raw_table_atom_without_source_terms() -> None:
    raw_table = (
        "Table- Sample Matrix\n"
        "Label        Score       Note\n"
        "Alpha        10          Stable\n"
        "Beta         20          Review"
    )
    result = _build([("table-block", raw_table, [])])

    tables = [a for a in result.ledger.technical_atoms if a.technical_atom_kind == "table"]
    assert len(tables) == 1
    table = tables[0]
    assert isinstance(table.payload, TablePayload)
    assert table.payload.raw_table_text == raw_table
    assert table.payload.caption == "Table- Sample Matrix"
    assert table.parse_status == "partially-parsed"
    assert [cell.value for cell in table.payload.cells if cell.column_index == 0] == [
        "Alpha",
        "Beta",
    ]


def test_two_column_spaced_table_materializes_as_table_atom() -> None:
    raw_table = "Table- Sample Scores\nName        Score\nAlpha       10\nBeta        20"
    result = _build([("table-block", raw_table, [])])

    table = next(a for a in result.ledger.technical_atoms if a.technical_atom_kind == "table")

    assert isinstance(table.payload, TablePayload)
    assert table.payload.caption == "Table- Sample Scores"
    assert [cell.value for cell in table.payload.cells if cell.column_index == 1] == [
        "10",
        "20",
    ]


def test_prose_heavy_table_block_bypasses_lexical_density_gate() -> None:
    raw_table = "\n".join(
        (
            "Outcomes",
            "Roll",
            "Result",
            "1",
            "Alpha begins with a long explanatory result.",
            "It continues with source-authored prose.",
            "The prose is still part of the first cell.",
            "The row explains cause and consequence.",
            "The result remains a table entry.",
            "It should not be discarded as prose.",
            "2",
            "Beta begins with another long explanatory result.",
            "It also continues across several lines.",
            "The continuation belongs to the second cell.",
            "The row contains no pipes or aligned spaces.",
            "The structural segment kind is the table evidence.",
            "The extractor should preserve the raw atom.",
        )
    )
    result = _build([("table-block", raw_table, [])])

    decision = next(
        decision
        for decision in result.ledger.extractor_decisions
        if decision.extractor_capability_id == "table-extractor"
    )
    table = next(a for a in result.ledger.technical_atoms if a.technical_atom_kind == "table")

    assert decision.ranker_score < 0.15
    assert decision.extractor_decision_status == "candidate-produced"
    assert isinstance(table.payload, TablePayload)
    assert table.payload.raw_table_text == raw_table


def test_named_table_reference_quality_requires_matching_table_atom() -> None:
    catalog = default_quality_check_catalog()
    severity = default_severity_policy()
    pointer = claim_ledger_pointer("qcc", "fp")
    missing = _build(
        [
            (
                "paragraph",
                "The Sample Matrix table shows ranking values.",
                ["The Sample Matrix table shows ranking values."],
            )
        ]
    )
    present = _build(
        [
            (
                "paragraph",
                "The Sample Matrix table shows ranking values.",
                ["The Sample Matrix table shows ranking values."],
            ),
            (
                "table-block",
                "Table- Sample Matrix\n"
                "Label        Score       Note\n"
                "Alpha        10          Stable",
                [],
            ),
        ]
    )
    unnamed_nearby = _build(
        [
            (
                "paragraph",
                "The Sample Matrix table shows ranking values.",
                ["The Sample Matrix table shows ranking values."],
            ),
            (
                "table-block",
                "| Label | Score |\n| --- | --- |\n| Alpha | 10 |",
                [],
            ),
        ]
    )
    differently_captioned_nearby = _build(
        [
            (
                "paragraph",
                "The Sample Categories table shows ranking values.",
                ["The Sample Categories table shows ranking values."],
            ),
            (
                "table-block",
                "Table- Sample Values\nName        Score\nAlpha       10\nBeta        20",
                [],
            ),
        ]
    )
    ordinary_prose = _build(
        [
            (
                "paragraph",
                "An improvised item may include a table leg.",
                ["An improvised item may include a table leg."],
            ),
            (
                "paragraph",
                "With a wry smile, the person placed a bottle on the table with a thud.",
                ["With a wry smile, the person placed a bottle on the table with a thud."],
            ),
        ]
    )

    missing_report = build_ledger_quality_report(
        missing.ledger,
        missing.document_structure,
        catalog=catalog,
        severity=severity,
        catalog_pointer=pointer,
    )
    present_report = build_ledger_quality_report(
        present.ledger,
        present.document_structure,
        catalog=catalog,
        severity=severity,
        catalog_pointer=pointer,
    )
    unnamed_report = build_ledger_quality_report(
        unnamed_nearby.ledger,
        unnamed_nearby.document_structure,
        catalog=catalog,
        severity=severity,
        catalog_pointer=pointer,
    )
    differently_captioned_report = build_ledger_quality_report(
        differently_captioned_nearby.ledger,
        differently_captioned_nearby.document_structure,
        catalog=catalog,
        severity=severity,
        catalog_pointer=pointer,
    )
    ordinary_report = build_ledger_quality_report(
        ordinary_prose.ledger,
        ordinary_prose.document_structure,
        catalog=catalog,
        severity=severity,
        catalog_pointer=pointer,
    )

    assert "ck-named-table-reference-resolved" in {
        finding.quality_check_id for finding in missing_report.findings
    }
    assert "ck-named-table-reference-resolved" not in {
        finding.quality_check_id for finding in present_report.findings
    }
    assert "ck-named-table-reference-resolved" not in {
        finding.quality_check_id for finding in unnamed_report.findings
    }
    assert "ck-named-table-reference-resolved" not in {
        finding.quality_check_id for finding in differently_captioned_report.findings
    }
    assert "ck-named-table-reference-resolved" not in {
        finding.quality_check_id for finding in ordinary_report.findings
    }


def test_numbered_table_reference_resolves_formal_caption_text() -> None:
    catalog = default_quality_check_catalog()
    severity = default_severity_policy()
    pointer = claim_ledger_pointer("qcc", "fp")
    result = _build(
        [
            (
                "paragraph",
                "The outcome depends on the final score (see Table 5-8: Sample Memory).",
                ["The outcome depends on the final score (see Table 5-8: Sample Memory)."],
            ),
            (
                "table-block",
                "Table 5-8: Sample Memory\n| Final Score | Time |\n| --- | --- |\n| 10 | One day |",
                [],
            ),
        ]
    )

    report = build_ledger_quality_report(
        result.ledger,
        result.document_structure,
        catalog=catalog,
        severity=severity,
        catalog_pointer=pointer,
    )

    assert "ck-named-table-reference-resolved" not in {
        finding.quality_check_id for finding in report.findings
    }


def test_named_table_reference_resolves_from_table_section_heading() -> None:
    catalog = default_quality_check_catalog()
    severity = default_severity_policy()
    pointer = claim_ledger_pointer("qcc", "fp")
    result = _build(
        [
            (
                "paragraph",
                "Roll on the Trial Bonds table.",
                ["Roll on the Trial Bonds table."],
            ),
            ("heading", "# Trial Bonds", []),
            ("table-block", "D20 Bond\n1 Alpha oath\n2 Beta compact\n3 Gamma duty", []),
        ]
    )

    report = build_ledger_quality_report(
        result.ledger,
        result.document_structure,
        catalog=catalog,
        severity=severity,
        catalog_pointer=pointer,
    )

    assert "ck-named-table-reference-resolved" not in {
        finding.quality_check_id for finding in report.findings
    }


def test_named_table_reference_resolves_unicode_caption_text() -> None:
    catalog = default_quality_check_catalog()
    severity = default_severity_policy()
    pointer = claim_ledger_pointer("qcc", "fp")
    result = _build(
        [
            (
                "paragraph",
                "The Typical Difficulty Classes table shows common values.",
                ["The Typical Difficulty Classes table shows common values."],
            ),
            (
                "table-block",
                "Table- Diﬀiculty Classes\n"
                "Task Difficulty   DC\n"
                "Easy              10\n"
                "Hard              20",
                [],
            ),
        ]
    )

    report = build_ledger_quality_report(
        result.ledger,
        result.document_structure,
        catalog=catalog,
        severity=severity,
        catalog_pointer=pointer,
    )

    assert "ck-named-table-reference-resolved" not in {
        finding.quality_check_id for finding in report.findings
    }


def test_named_table_reference_resolves_one_line_raw_table_title() -> None:
    catalog = default_quality_check_catalog()
    severity = default_severity_policy()
    pointer = claim_ledger_pointer("qcc", "fp")
    result = _build(
        [
            (
                "paragraph",
                "Roll on the Bonds table.",
                ["Roll on the Bonds table."],
            ),
            (
                "table-block",
                "Bonds\nD20 Bond\n1 Alpha oath\n2 Beta compact\n3 Gamma duty",
                [],
            ),
        ]
    )

    report = build_ledger_quality_report(
        result.ledger,
        result.document_structure,
        catalog=catalog,
        severity=severity,
        catalog_pointer=pointer,
    )

    assert "ck-named-table-reference-resolved" not in {
        finding.quality_check_id for finding in report.findings
    }


def test_explicit_forward_table_reference_allows_later_table_atom() -> None:
    catalog = default_quality_check_catalog()
    severity = default_severity_policy()
    pointer = claim_ledger_pointer("qcc", "fp")
    filler = [
        ("paragraph", f"Context sentence {index} preserves intervening source order.", [])
        for index in range(10)
    ]
    result = _build(
        [
            (
                "paragraph",
                "Choose from the Sample Matrix table below.",
                ["Choose from the Sample Matrix table below."],
            ),
            *filler,
            (
                "table-block",
                "| Label | Score |\n| --- | --- |\n| Alpha | 10 |\n| Beta | 20 |",
                [],
            ),
        ]
    )

    report = build_ledger_quality_report(
        result.ledger,
        result.document_structure,
        catalog=catalog,
        severity=severity,
        catalog_pointer=pointer,
    )

    assert "ck-named-table-reference-resolved" not in {
        finding.quality_check_id for finding in report.findings
    }


def test_generic_table_cue_lends_prior_section_name_to_later_table() -> None:
    catalog = default_quality_check_catalog()
    severity = default_severity_policy()
    pointer = claim_ledger_pointer("qcc", "fp")
    filler = [
        ("paragraph", f"Intervening source line {index} separates cue and table.", [])
        for index in range(10)
    ]
    result = _build(
        [
            (
                "paragraph",
                "The Sample Outcomes table shows generated results.",
                ["The Sample Outcomes table shows generated results."],
            ),
            ("heading", "# Sample Outcomes", []),
            ("heading", "# Roll on the table below.", []),
            *filler,
            ("heading", "# Follow-up Notes", []),
            (
                "table-block",
                "| Roll | Result |\n| --- | --- |\n| 1 | Alpha |\n| 2 | Beta |",
                [],
            ),
        ]
    )

    report = build_ledger_quality_report(
        result.ledger,
        result.document_structure,
        catalog=catalog,
        severity=severity,
        catalog_pointer=pointer,
    )

    assert "ck-named-table-reference-resolved" not in {
        finding.quality_check_id for finding in report.findings
    }


def test_three_incidental_numbers_do_not_parse_as_logical_table_rows() -> None:
    result = _build(
        [
            (
                "table-block",
                "Magnitude Notes\nA score of 10 or 11 is average. A score of 18 is unusually high.",
                [],
            )
        ]
    )

    assert all(atom.technical_atom_kind != "table" for atom in result.ledger.technical_atoms)


def test_logical_table_renders_as_markdown_table_with_raw_text() -> None:
    from llmwiki.domain.ledger.renderer import atom_block

    payload = TablePayload(
        raw_table_text="1 Alpha entry\n2 Beta entry",
        parse_status="parsed",
        source_locator="src.pdf",
        columns=(TableColumn(0, "entry"), TableColumn(1, "content")),
        rows=(TableRow(0), TableRow(1)),
        cells=(
            TableCell(0, 0, "1"),
            TableCell(0, 1, "Alpha entry"),
            TableCell(1, 0, "2"),
            TableCell(1, 1, "Beta entry"),
        ),
    )

    rendered = atom_block("table", payload)

    assert "| entry | content |" in rendered
    assert "| 2 | Beta entry |" in rendered
    assert "Raw table text" in rendered
    assert "1 Alpha entry\n2 Beta entry" in rendered


def test_partial_table_parse_renders_exact_raw_text_before_preview() -> None:
    from llmwiki.domain.ledger.renderer import atom_block

    payload = TablePayload(
        raw_table_text="Name        Score\nAlpha       10\nBeta        20",
        parse_status="partially-parsed",
        source_locator="src.pdf",
        columns=(TableColumn(0, "Name"), TableColumn(1, "Score")),
        rows=(TableRow(0), TableRow(1)),
        cells=(
            TableCell(0, 0, "Alpha"),
            TableCell(0, 1, "10"),
            TableCell(1, 0, "Beta"),
            TableCell(1, 1, "20"),
        ),
    )

    rendered = atom_block("table", payload)

    assert rendered.startswith("```text\nName        Score")
    assert "Parsed table preview (needs review)" in rendered
    assert "| Alpha | 10 |" in rendered


def test_figure_segment_becomes_unparsed_figure_atom() -> None:
    result = _build([("figure", "[Figure] (p.1)", [])])

    figure = next(a for a in result.ledger.technical_atoms if a.technical_atom_kind == "figure")
    assert isinstance(figure.payload, FigurePayload)
    assert figure.payload.raw_figure_text == "[Figure] (p.1)"
    assert figure.parse_status == "unparsed"


def test_formula_extraction_requires_source_neutral_notation() -> None:
    result = _build(
        [
            (
                "paragraph",
                "The guide says the assignment x = 1 appears in a long explanatory sentence "
                "that is not itself a standalone formula.",
                [],
            ),
            (
                "paragraph",
                "Archive files may appear under https://example.invalid/1/2/3/item.",
                [],
            ),
            (
                "paragraph",
                "Table 1-7: Experience Points by Skill lists values for later lookup.",
                [],
            ),
            (
                "paragraph",
                "The source cross-reference appears on pages 18-19 in the document.",
                [],
            ),
            ("paragraph", "Load = mass * acceleration", []),
        ]
    )

    formulas = [
        atom for atom in result.ledger.technical_atoms if atom.technical_atom_kind == "formula"
    ]
    formula_payloads = [
        atom.payload for atom in formulas if isinstance(atom.payload, FormulaPayload)
    ]
    assert [payload.raw_formula_text for payload in formula_payloads] == [
        "Load = mass * acceleration"
    ]


def test_formula_block_modality_preserves_formula_without_prose_claims() -> None:
    result = _build([("formula", "total = base + modifier", [])])

    formulas = [
        atom for atom in result.ledger.technical_atoms if atom.technical_atom_kind == "formula"
    ]

    assert len(formulas) == 1
    assert isinstance(formulas[0].payload, FormulaPayload)
    assert formulas[0].payload.raw_formula_text == "total = base + modifier"
    assert {entry.ledger_entry_kind for entry in result.ledger.entries} == {"technical-atom"}


def test_inline_enumerated_table_recovers_logical_rows_without_source_terms() -> None:
    result = _build(
        [
            (
                "table-block",
                "Catalog\n9 Alpha entry. 10 Beta entry. "
                "11 Gamma entry with 1 reset. 12 Delta entry.",
                [],
            )
        ]
    )

    table = next(a for a in result.ledger.technical_atoms if a.technical_atom_kind == "table")
    assert isinstance(table.payload, TablePayload)
    entry_cells = [cell.value for cell in table.payload.cells if cell.column_index == 0]
    assert entry_cells == ["9", "10", "11", "12"]
    assert table.payload.raw_table_text.startswith("Catalog")


def test_range_value_table_recovers_logical_rows_without_source_terms() -> None:
    result = _build(
        [
            (
                "table-block",
                "18-19 +4 20-21 +5 22-23 +6 24-25 +7",
                [],
            )
        ]
    )

    table = next(a for a in result.ledger.technical_atoms if a.technical_atom_kind == "table")
    assert isinstance(table.payload, TablePayload)
    entry_cells = [cell.value for cell in table.payload.cells if cell.column_index == 0]
    value_cells = [cell.value for cell in table.payload.cells if cell.column_index == 1]
    assert entry_cells == ["18-19", "20-21", "22-23", "24-25"]
    assert value_cells == ["+4", "+5", "+6", "+7"]


def test_enumerated_table_keeps_short_row_prefix_continuations() -> None:
    result = _build(
        [
            (
                "table-block",
                "Result\n2 Alpha entry.\nBeta Label: split title\n3 continued row.\n4 Gamma entry.",
                [],
            )
        ]
    )

    table = next(a for a in result.ledger.technical_atoms if a.technical_atom_kind == "table")
    assert isinstance(table.payload, TablePayload)
    values = [cell.value for cell in table.payload.cells if cell.column_index == 1]
    assert values[1] == "Beta Label: split title continued row."


def test_deontic_sentence_becomes_rule_atom_not_duplicate_claim() -> None:
    result = _build(_MIXED)
    rules = [a for a in result.ledger.technical_atoms if a.technical_atom_kind == "rule"]
    rule_payloads = [atom.payload for atom in rules if isinstance(atom.payload, RulePayload)]
    assert len(rule_payloads) == len(rules)
    assert any(payload.rule_force == "required" for payload in rule_payloads)
    assert any(payload.scope == "A combatant" for payload in rule_payloads)
    assert any(payload.effect == "roll a die." for payload in rule_payloads)
    claim_texts = [e.normalized_text for e in result.ledger.entries if e.is_claim_like]
    assert not any("must roll a die" in text for text in claim_texts)


def test_epistemic_modal_sentence_is_not_a_rule_atom() -> None:
    result = _build(
        [
            (
                "paragraph",
                "It may be incomplete. It will be asked why I should explain the limitation.",
                ["The archive is incomplete."],
            )
        ]
    )

    assert all(atom.technical_atom_kind != "rule" for atom in result.ledger.technical_atoms)


def test_history_style_modal_sentence_is_not_a_rule_atom() -> None:
    result = _build(
        [
            (
                "paragraph",
                "For rebellion must have a principle. "
                "The case of Britain, however, cannot possibly be considered alone. "
                "It was necessary that the empire should succeed-if only that it might fail. "
                "The mediators, except when they were monks, were none of them communal.",
                [
                    "Rebellion has a principle.",
                    "The case of Britain cannot be considered alone.",
                    "The empire succeeded in order to fail.",
                    "The mediators were not communal.",
                ],
            )
        ]
    )

    assert all(atom.technical_atom_kind != "rule" for atom in result.ledger.technical_atoms)


def test_conditional_rule_atom_requires_rule_like_effect() -> None:
    result = _build(
        [
            (
                "paragraph",
                "If the tally reaches 10, the target score reduces by 1.",
                ["A tally of 10 reduces the target score by 1."],
            )
        ]
    )
    rule = next(
        atom for atom in result.ledger.technical_atoms if atom.technical_atom_kind == "rule"
    )
    assert isinstance(rule.payload, RulePayload)
    assert rule.payload.trigger == "If the tally reaches 10"
    assert rule.payload.effect == "the target score reduces by 1."


def test_unstructured_rule_payload_is_not_topic_projectable() -> None:
    atom = TechnicalAtom(
        technical_atom_id="atom-1",
        technical_atom_kind="rule",
        payload=RulePayload("The chapter must be understood historically.", "required", "src.pdf"),
        source_locator="src.pdf",
        source_range_id="sr-1",
        evidence_ids=("ev-1",),
    )

    assert not atom_is_topic_projectable(atom)


def test_low_technical_density_source_does_not_project_prose_rule_atoms() -> None:
    atom = TechnicalAtom(
        technical_atom_id="atom-1",
        technical_atom_kind="rule",
        payload=RulePayload(
            "A combatant must roll a die.",
            "required",
            "src.pdf",
            scope="A combatant",
            effect="roll a die.",
        ),
        source_locator="src.pdf",
        source_range_id="sr-1",
        evidence_ids=("ev-1",),
    )
    profile = SourceProfile(
        source_locator="src.pdf",
        unit_count=100,
        accepted_entry_count=100,
        claim_count=90,
        event_count=0,
        concept_count=10,
        relationship_count=0,
        atom_kind_counts={"rule": 1},
        feature_signal_means={},
    )

    assert not atom_is_topic_projectable(atom, profile)


def test_high_technical_density_source_projects_structured_rule_atoms() -> None:
    atom = TechnicalAtom(
        technical_atom_id="atom-1",
        technical_atom_kind="rule",
        payload=RulePayload(
            "A combatant must roll a die.",
            "required",
            "src.pdf",
            scope="A combatant",
            effect="roll a die.",
        ),
        source_locator="src.pdf",
        source_range_id="sr-1",
        evidence_ids=("ev-1",),
    )
    profile = SourceProfile(
        source_locator="src.pdf",
        unit_count=100,
        accepted_entry_count=100,
        claim_count=60,
        event_count=0,
        concept_count=20,
        relationship_count=0,
        atom_kind_counts={"rule": 8},
        feature_signal_means={},
    )

    assert atom_is_topic_projectable(atom, profile)


def test_rulebook_profile_assigns_rules_reference_over_history_from_names() -> None:
    profile = SourceProfile(
        source_locator="manual.pdf",
        unit_count=500,
        accepted_entry_count=1000,
        claim_count=500,
        event_count=10,
        concept_count=20,
        relationship_count=120,
        atom_kind_counts={"formula": 280, "rule": 70, "table": 10, "worked-example": 4},
        feature_signal_means={
            "entity-date-density": 0.4,
            "rule-language-density": 0.2,
            "table-density": 0.02,
            "procedure-density": 0.01,
        },
    )

    assignment = assign_family(profile)

    assert assignment.top_label == "rules-reference"


def test_coding_profile_assigns_coding_without_formula_boost() -> None:
    profile = SourceProfile(
        source_locator="programming.pdf",
        unit_count=200,
        accepted_entry_count=1000,
        claim_count=500,
        event_count=20,
        concept_count=20,
        relationship_count=100,
        atom_kind_counts={"code-block": 250, "formula": 20, "rule": 20, "table": 10},
        feature_signal_means={
            "code-density": 0.35,
            "entity-date-density": 0.15,
            "rule-language-density": 0.15,
        },
    )

    assignment = assign_family(profile)

    assert assignment.top_label == "coding"


def test_low_signal_only_sentence_is_not_a_rule_atom() -> None:
    result = _build(
        [
            (
                "paragraph",
                "The archive is not only old; it is also public.",
                ["The archive is old and public."],
            )
        ]
    )

    assert all(atom.technical_atom_kind != "rule" for atom in result.ledger.technical_atoms)


def test_claim_like_entry_carries_required_proposition_fields() -> None:
    result = _build(_MIXED)
    claim = next(e for e in result.ledger.usable_entries if "grimoire" in e.normalized_text)
    assert claim.subject and claim.predicate and claim.object_value
    assert claim.polarity in ("affirmative", "negative")
    assert claim.claim_force


def test_fragmentary_statement_is_needs_review_not_usable() -> None:
    result = _build(_MIXED)
    fragment = next(
        e for e in result.ledger.entries if "glossary notation" in e.normalized_text.lower()
    )
    assert fragment.ledger_entry_status == "needs-review"
    assert fragment.review_reason is not None


def test_atom_validator_rejects_incomplete_payload() -> None:
    validator = AtomValidator(default_atom_schema_set())
    invalid = TablePayload(raw_table_text="", parse_status="parsed", source_locator="src.pdf")
    valid = TablePayload(raw_table_text="x", parse_status="parsed", source_locator="src.pdf")
    assert validator.validate("table", invalid).status == "invalid"
    assert validator.validate("table", valid).status == "valid"


def test_ranker_scores_in_range_and_buckets_controlled() -> None:
    result = _build(_MIXED)
    for decision in result.ledger.extractor_decisions:
        assert 0.0 <= decision.ranker_score <= 1.0
        if decision.extractor_decision_status == "abstained":
            assert decision.calibration_bucket in CALIBRATION_BUCKETS
            assert decision.abstain_reason is not None


def test_domain_is_deterministic_for_same_input() -> None:
    first = _build(_MIXED)
    second = _build(_MIXED)
    assert canonical_json(first.ledger) == canonical_json(second.ledger)
    assert canonical_json(first.document_structure) == canonical_json(second.document_structure)


def test_universal_standard_renamed_domain_variants_behave_identically() -> None:
    spells = [
        ("heading", "# Spells", []),
        ("paragraph", "The wizard must cast a spell.", ["The wizard must cast a spell."]),
        ("paragraph", "A grimoire contains many spells.", ["A grimoire contains many spells."]),
    ]
    modules = [
        ("heading", "# Modules", []),
        (
            "paragraph",
            "The engineer must compile a module.",
            ["The engineer must compile a module."],
        ),
        ("paragraph", "A library contains many modules.", ["A library contains many modules."]),
    ]
    a = _build(spells, source_hash="a" * 16)
    b = _build(modules, source_hash="b" * 16)

    def shape(result: LedgerBuildResult) -> tuple[tuple[str, ...], ...]:
        kinds = tuple(e.ledger_entry_kind for e in result.ledger.entries)
        statuses = tuple(e.ledger_entry_status for e in result.ledger.entries)
        atoms = tuple(a.technical_atom_kind for a in result.ledger.technical_atoms)
        dispositions = tuple(r.disposition for r in result.document_structure.dispositions)
        return kinds, statuses, atoms, dispositions

    assert shape(a) == shape(b)


def test_quality_report_warns_on_review_and_write_boundary_allows_with_work() -> None:
    result = _build(_MIXED)
    catalog = default_quality_check_catalog()
    severity = default_severity_policy()
    pointer = claim_ledger_pointer("qcc", "fp")  # any pointer for the report header
    report = build_ledger_quality_report(
        result.ledger,
        result.document_structure,
        catalog=catalog,
        severity=severity,
        catalog_pointer=pointer,
    )
    assert report.has_severity("warning")  # the fragment is review work
    assert not report.has_severity("blocking")
    assert page_write_decision(report) == "write-with-review-work"


def test_projection_renders_only_usable_entries_and_no_internal_ids() -> None:
    result = _build(_MIXED)
    support = ProjectionSourceSupport(
        "pss",
        _HASH,
        "src.pdf",
        claim_ledger_pointer("cl", "f"),
        document_structure_pointer("ds", "g"),
    )
    plan = plan_source_page(
        result.ledger,
        result.document_structure,
        wiki_page_locator="src",
        title="Src",
        source_support=support,
    )
    page = render_source_page(plan, result.ledger)
    catalog = default_quality_check_catalog()
    report = build_projection_quality_report(
        plan,
        page.coverage,
        page.page_body,
        result.ledger,
        catalog=catalog,
        severity=default_severity_policy(),
        catalog_pointer=claim_ledger_pointer("qcc", "fp"),
    )
    assert not report.has_severity("blocking")
    for prefix in ("ledger-entry-", "projection-coverage-entry-"):
        assert prefix not in page.page_body
    # Generated page claims select only usable entries.
    usable = {e.ledger_entry_id for e in result.ledger.usable_entries}
    for entry in page.coverage.entries:
        if entry.projection_coverage_unit_kind == "generated-page-claim":
            assert set(entry.selected_ledger_entry_ids) <= usable


def test_portable_artifact_set_excludes_self_and_tracks_membership() -> None:
    members = (
        PortableArtifactMember("claim-ledger-artifact", "cl-1", "f1"),
        PortableArtifactMember("document-structure-artifact", "ds-1", "f2"),
    )
    first = build_portable_artifact_set(members)
    assert all(m.portable_artifact_kind != "portable-artifact-set" for m in first.members)
    extra = (*members, PortableArtifactMember("projection-coverage-artifact", "pc-1", "f3"))
    second = build_portable_artifact_set(extra)
    assert first.portable_artifact_set_fingerprint != second.portable_artifact_set_fingerprint


def test_source_coverage_marks_gaps_without_filtering_segments() -> None:
    segment = SourceSegment(
        segment_id="seg-001",
        source_range_id="sr-001",
        source_locator="src.pdf",
        source_hash=_HASH,
        heading_path="H",
        structure_node_id="",
        source_order=1,
        text="A source sentence has content.",
        segment_kind="paragraph",
        evidence_ids=("ev-001",),
        source_element_ids=("el-001",),
    )
    result = build_claim_ledger(
        source_locator="src.pdf",
        source_hash=_HASH,
        evidence_registry_hash="er-hash",
        segments=(SegmentInput(segment, ()),),
        profiles={
            "seg-001": profile_unit(
                extracted_unit_id="seg-001",
                source_range_id="sr-001",
                text=segment.text,
                evidence_ids=segment.evidence_ids,
            )
        },
        schema=default_schema_bundle(),
    )
    coverage = build_source_coverage(
        source_locator="src.pdf",
        source_hash=_HASH,
        elements=(
            SourceElementRecord("el-001", "paragraph", "body", "H", "p.1", True),
            SourceElementRecord("el-002", "paragraph", "body", "H", "p.1", True),
            SourceElementRecord("el-003", "page_header", "header", "H", "p.1", True),
        ),
        segments=(SegmentInput(segment, ()),),
        ledger=result.ledger,
        structure=result.document_structure,
    )

    statuses = {record.source_element_id: record.coverage_status for record in coverage.records}
    assert statuses == {"el-001": "covered", "el-002": "gap", "el-003": "excluded"}


def test_reading_source_close_text_is_the_source_statement() -> None:
    # The projection cites source-close normalized text, never a broadened paraphrase.
    result = _build(_MIXED)
    claim = next(e for e in result.ledger.usable_entries if "grimoire" in e.normalized_text)
    assert claim.normalized_text == "A grimoire contains many spells."
    assert claim.resolution_basis == "source-close-statement"

"""Tests for deterministic source-claim quality planning."""

from llmwiki.domain.objects import ExtractedUnit, RawSource, SourceBundle, SourceClaimQualityFixture
from llmwiki.domain.pages import LOCAL_FLAT_STRUCTURE
from llmwiki.domain.planning import (
    _claim_eligibility,
    _claim_role_tags,
    build_page_plan,
    planned_write_message,
    source_summary_quality_report,
)


def _fixtures() -> tuple[SourceClaimQualityFixture, ...]:
    javascript_specs = (
        (
            "Object.assign",
            "Object.assign copies own enumerable properties from source objects into a target.",
            "eligible",
            (),
        ),
        (
            "Closures",
            "A closure is a function with access to bindings from an outer lexical scope.",
            "eligible",
            ("identity",),
        ),
        (
            "Iterators",
            "An iterator object returns successive values through calls to next.",
            "eligible",
            ("function",),
        ),
        (
            "Map",
            "A caller may pass a function to map in order to transform each element.",
            "eligible",
            ("ordinary-modality",),
        ),
        (
            "Generators",
            "There is more to generators than producing a single sequence.",
            "eligible",
            ("ordinary-modality",),
        ),
        (
            "Resources",
            "The source does not specify whether the iterator closes the resource.",
            "eligible",
            ("source-uncertainty",),
        ),
        (
            "Closures",
            "Closures are similar to backpacks that carry bindings for a function.",
            "analogy",
            ("analogy",),
        ),
        (
            "Callbacks",
            "What if a callback could remember state after its creator returns?",
            "rhetorical-example",
            (),
        ),
        (
            "Narrative",
            "Let us take a short detour before returning to functions.",
            "narrative-frame",
            (),
        ),
        (
            "Narrative",
            "Imagine we are visiting our favourite coffee shop.",
            "narrative-frame",
            ("worked-example",),
        ),
        (
            "Narrative",
            "You express your order at one end of their counter.",
            "narrative-frame",
            (),
        ),
        (
            "Narrative",
            "'We are grateful you made time to visit with us today.'",
            "narrative-frame",
            (),
        ),
        (
            "Source framing",
            "The source discusses closures and function scope.",
            "source-framing",
            ("source-framing",),
        ),
        (
            "Code",
            "const result = values.map(value => value * value);",
            "code-fragment",
            (),
        ),
        (
            "Source furniture",
            "Copyright 2016 by the author.",
            "source-furniture",
            (),
        ),
        (
            "Source furniture",
            "Cafe Diplomatico in Toronto's Little Italy",
            "source-furniture",
            (),
        ),
        (
            "Source furniture",
            "Some different sized and coloured coffee pots by Antti Nurmesniemi.",
            "source-furniture",
            (),
        ),
        (
            "Source furniture",
            "http://creativecommons.org/licenses/by-sa/2.0/deed.en",
            "source-furniture",
            (),
        ),
        (
            "Source furniture",
            "© 2015 - 2017 Reg 'raganwald' Braithwaite Also By Reg "
            "'raganwald' Braithwaite Kestrels, Quirky Birds, and Hopeless "
            "Egocentricity.",
            "source-furniture",
            (),
        ),
        (
            "Source furniture",
            "The original words in this book are (c) 2012-2015, Reginald Braithwaite.",
            "source-furniture",
            (),
        ),
        (
            "Source furniture",
            "Leanpub empowers authors and publishers with the Lean Publishing process.",
            "source-furniture",
            (),
        ),
        (
            "Narrative",
            "Some complain that the long pull is more bitter and detracts from "
            "the best character of the coffee.",
            "narrative-frame",
            (),
        ),
        (
            "Narrative",
            "The first, and the one I prefer, is to add a small amount of hot "
            "water to a double or quadruple Espresso Ristretto.",
            "narrative-frame",
            (),
        ),
        (
            "Narrative",
            "There are two different ways to make it.",
            "narrative-frame",
            (),
        ),
        (
            "Narrative",
            "As a result, JavaScript Allongé is a rich read releasing many of "
            "JavaScript's subtleties, much like the Café Allongé beloved by "
            "coffee enthusiasts everywhere.",
            "narrative-frame",
            ("analogy",),
        ),
        (
            "Narrative",
            "The Carpenter arrived early for his meeting with Thing Software, "
            "and was shown to conference room 13.",
            "narrative-frame",
            (),
        ),
        (
            "Narrative",
            "The Carpenter normally worked through personal referrals, but from "
            "time to time a recruiter would slip through his screen.",
            "narrative-frame",
            (),
        ),
        (
            "Narrative",
            "Bob was well-known in the Python community, but his clients often "
            "needed experience with other languages.",
            "narrative-frame",
            (),
        ),
        (
            "Narrative",
            "It seems some people will only try blind dating once.",
            "narrative-frame",
            (),
        ),
        (
            "Source framing",
            "When discussing functions, we looked at functional iterators.",
            "source-framing",
            ("source-framing",),
        ),
        (
            "Source framing",
            "This is exactly how the JavaScript environment works for the purpose of this book.",
            "source-framing",
            ("source-framing",),
        ),
        (
            "Source framing",
            "JavaScript Allongé takes great delight in explaining what they "
            "mean and why they matter.",
            "source-framing",
            ("source-framing",),
        ),
        (
            "Reduce",
            "Reduce combines a collection into one accumulated value.",
            "eligible",
            ("function",),
        ),
        (
            "Objects",
            "Objects have properties that can be read by name.",
            "eligible",
            ("attribute",),
        ),
        (
            "Recursion",
            "A recursive function calls itself with a smaller problem.",
            "eligible",
            ("function",),
        ),
        (
            "Examples",
            "For example, a function can return another function.",
            "eligible",
            ("worked-example",),
        ),
    )
    antikythera_specs = (
        (
            "Device identity",
            "The Antikythera mechanism is an ancient geared calculating device.",
            "eligible",
            ("identity",),
        ),
        (
            "Function",
            "The device tracked astronomical cycles using a gear train.",
            "eligible",
            ("function",),
        ),
        (
            "Evidence",
            "Inscriptions provide evidence for calendrical and eclipse functions.",
            "eligible",
            ("evidence",),
        ),
        (
            "Dating",
            "The wreck was recovered in 1901 near Antikythera.",
            "eligible",
            ("temporal",),
        ),
        (
            "Uncertainty",
            "The source does not confirm the workshop that made the mechanism.",
            "eligible",
            ("source-uncertainty",),
        ),
        (
            "Comparison",
            "No comparable geared device was found from the same period.",
            "eligible",
            ("negative-evidence",),
        ),
        (
            "Analogy",
            "The mechanism is similar to a compact astronomical computer.",
            "analogy",
            ("analogy",),
        ),
        (
            "Question",
            "How would a user know which dial to read first?",
            "rhetorical-example",
            (),
        ),
        (
            "Source framing",
            "The text mentions the bronze fragments and inscription evidence.",
            "source-framing",
            ("source-framing",),
        ),
        (
            "Source furniture",
            "Table of contents lists the recovery chapter.",
            "source-furniture",
            (),
        ),
    )
    javascript = tuple(
        _quality_fixture(
            fixture_id=f"javascript-{idx:03d}",
            source_locator="javascriptallonge.pdf",
            spec=javascript_specs[idx % len(javascript_specs)],
        )
        for idx in range(80)
    )
    antikythera = tuple(
        _quality_fixture(
            fixture_id=f"antikythera-{idx:03d}",
            source_locator="antikythera-mechanism.pdf",
            spec=antikythera_specs[idx % len(antikythera_specs)],
        )
        for idx in range(20)
    )
    return javascript + antikythera


def test_source_claim_quality_fixture_accuracy() -> None:
    fixtures = _fixtures()
    assert sum(1 for item in fixtures if item.source_locator == "javascriptallonge.pdf") >= 80
    assert sum(1 for item in fixtures if item.source_locator == "antikythera-mechanism.pdf") >= 20

    correct = 0
    possible = 0
    for fixture in fixtures:
        roles = _claim_role_tags(fixture.statement)
        eligibility = _claim_eligibility(fixture.statement, roles)
        possible += 1
        if eligibility == fixture.expected_claim_eligibility:
            correct += 1
        for expected_role in fixture.expected_claim_role_tags:
            possible += 1
            if expected_role in roles:
                correct += 1

    assert correct / possible >= 0.90


def test_source_summary_plan_selects_eligible_claim_over_analogy() -> None:
    plan = _plan_for_units(
        (
            _unit(
                "unit-0001",
                "Object.assign",
                (
                    "Closures are similar to backpacks that carry bindings for a function. "
                    "Object.assign copies enumerable properties into a target object."
                ),
            ),
        )
    )
    source_write = next(
        write for write in plan.planned_writes if write.page_metadata.page_id != "book"
    )
    assert source_write.source_summary_plan is not None
    selected = {
        claim.source_claim_id: claim for claim in plan.source_claims
    }[source_write.source_summary_plan.selected_source_claims[0]]

    assert selected.claim_eligibility == "eligible"
    assert selected.statement.startswith("Object.assign")


def test_source_summary_plan_selects_eligible_claim_over_code_fragment() -> None:
    plan = _plan_for_units(
        (
            _unit(
                "unit-0001",
                "Map",
                (
                    "const result = values.map(value => value * value);\n\n"
                    "Map transforms each element with a callback function."
                ),
            ),
        )
    )
    source_write = next(
        write for write in plan.planned_writes if write.page_metadata.page_id != "book"
    )
    assert source_write.source_summary_plan is not None
    selected_claims = {
        claim.source_claim_id: claim for claim in plan.source_claims
    }
    selected = selected_claims[source_write.source_summary_plan.selected_source_claims[0]]

    assert selected.claim_eligibility == "eligible"
    assert selected.statement.startswith("Map transforms")


def test_source_summary_plan_uses_central_code_fallback_for_code_only_units() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = (
        ExtractedUnit(
            unit_id="unit-0001",
            raw_source=raw_source,
            locator="p.1",
            heading_path="operations that transform an iterable into a value",
            text=(
                "```"
                "const reduceWith = (fn, seed, iterable) => { "
                "let accumulator = seed; "
                "for ( const element of iterable) { accumulator = fn(accumulator, element); } "
                "return accumulator; }; "
                "const first = (iterable) => iterable[Symbol.iterator]().next().value;"
                "```"
            ),
            extraction_status="ok",
        ),
    ) + tuple(
        ExtractedUnit(
            unit_id=f"unit-{idx:04d}",
            raw_source=raw_source,
            locator=f"p.{idx}",
            heading_path=f"Functional iterators {idx}",
            text=f"Functional iterators {idx} separate traversal mechanics from operations.",
            extraction_status="ok",
        )
        for idx in range(2, 46)
    )
    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=units,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-19",
    )
    write = next(
        write
        for write in plan.planned_writes
        if "unit-0001" in write.extracted_units and len(write.extracted_units) > 1
    )
    assert write.source_summary_plan is not None
    claims_by_id = {claim.source_claim_id: claim for claim in plan.source_claims}
    selected = tuple(
        claims_by_id[claim_id] for claim_id in write.source_summary_plan.selected_source_claims
    )

    code_fallbacks = [
        claim for claim in selected if claim.extracted_unit_id == "unit-0001"
    ]
    assert len(code_fallbacks) == 1
    assert code_fallbacks[0].claim_eligibility == "code-fragment"


def test_source_summary_plan_skips_ineligible_role_fillers_when_unit_has_eligible_claim() -> None:
    plan = _plan_for_units(
        (
            _unit(
                "unit-0001",
                "Loop detection",
                (
                    "Years later, I came across a discussion of this algorithm. "
                    "No matter how large the list is, the fast reference eventually "
                    "equals the slow reference and detects the loop. "
                    "And to the interviewer's credit, he asked me to describe my thinking."
                ),
            ),
        )
    )
    source_write = next(
        write for write in plan.planned_writes if write.page_metadata.page_id != "book"
    )
    assert source_write.source_summary_plan is not None
    claims_by_id = {claim.source_claim_id: claim for claim in plan.source_claims}
    selected = tuple(
        claims_by_id[claim_id]
        for claim_id in source_write.source_summary_plan.selected_source_claims
    )

    assert selected
    assert all(claim.claim_eligibility == "eligible" for claim in selected)


def test_source_summary_plan_skips_source_furniture_unit_when_page_has_eligible_claims() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = (
        ExtractedUnit(
            unit_id="unit-0001",
            raw_source=raw_source,
            locator="p.1",
            heading_path="Image caption",
            text="Cafe Diplomatico in Toronto's Little Italy",
            extraction_status="ok",
        ),
    ) + tuple(
        ExtractedUnit(
            unit_id=f"unit-{idx:04d}",
            raw_source=raw_source,
            locator=f"p.{idx}",
            heading_path=f"Technical Section {idx}",
            text=f"Technical section {idx} returns values through a function call.",
            extraction_status="ok",
        )
        for idx in range(2, 46)
    )
    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=units,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-19",
    )
    write = next(write for write in plan.planned_writes if "unit-0001" in write.extracted_units)
    assert write.source_summary_plan is not None
    claims_by_id = {claim.source_claim_id: claim for claim in plan.source_claims}
    selected = tuple(
        claims_by_id[claim_id] for claim_id in write.source_summary_plan.selected_source_claims
    )

    assert selected
    assert {claim.extracted_unit_id for claim in selected} <= set(write.extracted_units)
    assert "unit-0001" not in {claim.extracted_unit_id for claim in selected}
    assert all(claim.claim_eligibility == "eligible" for claim in selected)


def test_source_summary_plan_skips_noncentral_eligible_filler_when_page_has_central_claims(
) -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = (
        ExtractedUnit(
            unit_id="unit-0001",
            raw_source=raw_source,
            locator="p.1",
            heading_path="Preface",
            text=(
                "This achieves approximately the same ratio of oils to water "
                "as the dilution method."
            ),
            extraction_status="ok",
        ),
    ) + tuple(
        ExtractedUnit(
            unit_id=f"unit-{idx:04d}",
            raw_source=raw_source,
            locator=f"p.{idx}",
            heading_path=f"Functional iterators {idx}",
            text=f"Functional iterators {idx} separate traversal mechanics from operations.",
            extraction_status="ok",
        )
        for idx in range(2, 46)
    )
    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=units,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-19",
    )
    write = next(
        write
        for write in plan.planned_writes
        if "unit-0001" in write.extracted_units and len(write.extracted_units) > 1
    )
    assert write.source_summary_plan is not None
    claims_by_id = {claim.source_claim_id: claim for claim in plan.source_claims}
    selected = tuple(
        claims_by_id[claim_id] for claim_id in write.source_summary_plan.selected_source_claims
    )

    assert selected
    assert "unit-0001" not in {claim.extracted_unit_id for claim in selected}
    assert all(
        claim.claim_role_tags or claim.claim_centrality > 0
        for claim in selected
    )


def test_source_summary_plan_separates_ordinary_modality_from_source_uncertainty() -> None:
    ordinary_plan = _plan_for_units(
        (
            _unit(
                "unit-0001",
                "Map",
                "A caller may pass a function to map in order to transform each element.",
            ),
        )
    )
    ordinary_write = next(
        write for write in ordinary_plan.planned_writes if write.page_metadata.page_id != "book"
    )
    assert ordinary_write.source_summary_plan is not None
    assert "ordinary-modality" in ordinary_write.source_summary_plan.required_claim_role_tags
    assert "source-uncertainty" not in ordinary_write.source_summary_plan.required_claim_role_tags

    uncertainty_plan = _plan_for_units(
        (
            _unit(
                "unit-0001",
                "Iterator close",
                "The source does not specify whether the iterator closes the resource.",
            ),
        )
    )
    uncertainty_write = next(
        write for write in uncertainty_plan.planned_writes if write.page_metadata.page_id != "book"
    )
    assert uncertainty_write.source_summary_plan is not None
    assert "source-uncertainty" in uncertainty_write.source_summary_plan.required_claim_role_tags


def test_source_summary_plan_excludes_claims_after_scope_shift_marker() -> None:
    unit = _unit(
        "unit-0019",
        "value types",
        (
            "# value types\n\n"
            "Third, some types of cups have no distinguishing marks on them. "
            "If they are the same kind of cup, and they hold the same contents, "
            "we have no way to tell the difference between them. "
            "This is the case with the strings, numbers, and booleans we have "
            "seen so far.\n\n"
            "```js\n"
            "2 === 2\n"
            "//=> true\n\n"
            "'hello' === 'hello'\n"
            "//=> true\n"
            "```\n\n"
            "Note well what is happening with the examples: Even when we obtain "
            "a string, a number, or a boolean as the result of evaluating an "
            "expression, it is identical to another value of the same type with "
            "the same content. Strings, numbers, and booleans are examples of "
            "what JavaScript calls 'value' or 'primitive' types. We'll use both "
            "terms interchangeably.\n\n"
            "We haven't encountered the fourth possibility yet. Stretching the "
            "metaphor somewhat, some types of cups have a serial number on the "
            "bottom. So even if you have two cups of the same type, and their "
            "contents are the same, you can still distinguish between them."
        ),
    )
    plan = _plan_for_units((unit,))
    source_write = next(
        write for write in plan.planned_writes if write.page_metadata.page_id != "book"
    )
    assert source_write.source_summary_plan is not None
    claims_by_id = {claim.source_claim_id: claim for claim in plan.source_claims}
    selected = tuple(
        claims_by_id[claim_id]
        for claim_id in source_write.source_summary_plan.selected_source_claims
    )

    assert any(
        claim.claim_eligibility == "scope-transition" for claim in plan.source_claims
    )
    assert all("fourth possibility" not in claim.statement.lower() for claim in selected)
    assert all(
        "serial number" not in claim.statement.lower()
        and "distinguish between them" not in claim.statement.lower()
        for claim in selected
    )
    assert any("value" in claim.statement.lower() for claim in selected)
    message = planned_write_message(source_write, {unit.unit_id: unit}, claims_by_id)
    assert "fourth possibility" not in message.lower()
    assert "serial number" not in message.lower()
    assert "distinguish between them" not in message.lower()


def test_source_summary_scope_boundary_uses_source_neutral_discourse() -> None:
    unit = _unit(
        "unit-0099",
        "primary protocol",
        (
            "# primary protocol\n\n"
            "The primary protocol normalizes sensor readings before storage. "
            "It keeps stable measurements in the active buffer. "
            "We have not introduced the secondary protocol yet. "
            "The secondary protocol uses archival keys to distinguish duplicate "
            "measurements."
        ),
    )
    plan = _plan_for_units((unit,))
    source_write = next(
        write for write in plan.planned_writes if write.page_metadata.page_id != "book"
    )
    assert source_write.source_summary_plan is not None
    claims_by_id = {claim.source_claim_id: claim for claim in plan.source_claims}
    selected = tuple(
        claims_by_id[claim_id]
        for claim_id in source_write.source_summary_plan.selected_source_claims
    )

    assert any(
        claim.claim_eligibility == "scope-transition" for claim in plan.source_claims
    )
    assert selected
    assert all("secondary protocol" not in claim.statement.lower() for claim in selected)
    message = planned_write_message(source_write, {unit.unit_id: unit}, claims_by_id)
    assert "secondary protocol" not in message.lower()
    assert "extractedunit text omitted" in message.lower()


def test_source_summary_quality_report_counts_deterministic_failures() -> None:
    plan = _plan_for_units(
        (
            _unit(
                "unit-0001",
                "Functions",
                "Functions are values. Functions may close over lexical scope.",
            ),
            _unit(
                "unit-0002",
                "Closures",
                "Closures are functions with remembered bindings.",
            ),
        )
    )

    clean_report = source_summary_quality_report(plan, {})
    assert clean_report.selected_ineligible_claims == 0
    assert clean_report.false_source_uncertainty_claims == 0
    assert clean_report.missing_unit_coverage == 0

    dirty_report = source_summary_quality_report(
        plan,
        {
            "book-functions": (
                "## Key supported claims\n\n"
                "- The source discusses functions and closures. (raw/book.pdf)"
            )
        },
    )
    assert dirty_report.source_framing_bullets == 1


def _plan_for_units(units: tuple[ExtractedUnit, ...]):
    raw_source = units[0].raw_source
    return build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=units,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-19",
    )


def _quality_fixture(
    *,
    fixture_id: str,
    source_locator: str,
    spec: tuple[str, str, str, tuple[str, ...]],
) -> SourceClaimQualityFixture:
    heading, statement, eligibility, roles = spec
    return SourceClaimQualityFixture(
        fixture_id=fixture_id,
        source_locator=source_locator,
        heading_path=heading,
        statement=statement,
        expected_claim_eligibility=eligibility,
        expected_claim_role_tags=roles,
    )


def _unit(unit_id: str, heading_path: str, text: str) -> ExtractedUnit:
    raw_source = RawSource.from_locator("book.pdf")
    return ExtractedUnit(
        unit_id=unit_id,
        raw_source=raw_source,
        locator=unit_id,
        heading_path=heading_path,
        text=text,
        extraction_status="ok",
    )

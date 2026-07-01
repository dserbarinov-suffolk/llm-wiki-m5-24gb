"""Chat-domain helpers: deterministic, budget-bound grounding and history windows."""

from llmwiki.domain.chat_grounding import (
    ChatEvidenceMode,
    ChatEvidenceScope,
    ChatResponseCitationPolicy,
    ChatTaskMode,
    build_chat_grounding,
    plan_chat_grounding,
    render_grounded_user_message,
)
from llmwiki.domain.chatwindow import (
    SEED_ANSWER_CAP_CHARS,
    QAPair,
    build_window,
    estimate_tokens,
)
from llmwiki.domain.pages import parse_page
from llmwiki.domain.search import SearchHit
from llmwiki.workflows.prompts import CHAT_TEMPLATE


def _pair(i: int, answer_chars: int = 400) -> QAPair:
    return QAPair(question=f"question {i}?", answer=f"answer {i} " + "x" * answer_chars)


def _page(page_id: str, page_family: str) -> str:
    family = f"page_family: {page_family}\n" if page_family else ""
    return (
        "---\n"
        f"page_id: {page_id}\n"
        "page_kind: source\n"
        f"{family}"
        f"summary: {page_id} summary.\n"
        "---\n\n"
        f"# {page_id}\n"
    )


class TestBuildWindow:
    def test_keeps_most_recent_that_fit_in_order(self) -> None:
        history = [_pair(i) for i in range(10)]  # ~100 tokens each
        window = build_window(history, budget_tokens=350)
        assert [p.question for p in window] == ["question 7?", "question 8?", "question 9?"]

    def test_everything_fits_when_budget_allows(self) -> None:
        history = [_pair(i) for i in range(3)]
        assert build_window(history, budget_tokens=10_000) == tuple(history)

    def test_empty_history(self) -> None:
        assert build_window([]) == ()

    def test_oversized_answer_clipped_in_seed_only(self) -> None:
        original = _pair(1, answer_chars=SEED_ANSWER_CAP_CHARS * 3)
        history = [original]
        window = build_window(history, budget_tokens=10_000)
        assert len(window[0].answer) == SEED_ANSWER_CAP_CHARS
        assert window[0].answer.endswith("…")
        # The stored object is untouched (preservation guarantee).
        assert len(original.answer) > SEED_ANSWER_CAP_CHARS

    def test_window_is_contiguous_no_gaps(self) -> None:
        # One huge old answer must stop the walk, not be skipped over.
        history = [_pair(0), _pair(1, answer_chars=8_000), _pair(2), _pair(3)]
        window = build_window(history, budget_tokens=300)
        assert [p.question for p in window] == ["question 2?", "question 3?"]

    def test_token_estimate_sanity(self) -> None:
        assert estimate_tokens("x" * 400) == 100


class TestChatGrounding:
    def test_grounding_is_bounded_when_index_is_large(self) -> None:
        index = "\n".join(
            [f"- [[unrelated-{i}]] — filler summary" for i in range(1000)]
            + ["- [[cairn-character-creation]] — Character creation in Cairn."]
        )
        pages = {
            "cairn-character-creation": (
                "Cairn character creation covers roll attributes, choose a background, "
                "and record equipment."
            ),
            "unrelated-1": "A distant page about another subject.",
        }

        grounding = build_chat_grounding(
            "How to create a new character in Cairn?",
            index_text=index,
            page_texts=pages,
            budget_tokens=80,
        )

        assert estimate_tokens(grounding) <= 80
        assert "[[cairn-character-creation]]" in grounding
        assert "[[unrelated-999]]" not in grounding

    def test_grounding_tells_model_to_search_when_no_hits_match(self) -> None:
        grounding = build_chat_grounding(
            "unmatched terms",
            index_text="- [[alpha]] — Alpha.",
            page_texts={"alpha": "No overlap here."},
        )

        assert "No local search hits" in grounding
        assert "search_wiki" in grounding
        assert "[[alpha]]" in grounding

    def test_catalog_question_uses_index(self) -> None:
        plan = plan_chat_grounding("What does this wiki cover?", grounded=False, has_window=True)

        assert plan.evidence_mode is ChatEvidenceMode.CATALOG_OR_PAGE
        assert plan.include_index
        assert not plan.include_search_results

    def test_style_followup_uses_conversation_window(self) -> None:
        plan = plan_chat_grounding("shorter please", grounded=False, has_window=True)

        assert plan.evidence_mode is ChatEvidenceMode.CONVERSATION
        assert not plan.require_wiki_read
        assert not plan.include_search_results

    def test_how_to_question_explains_procedure(self) -> None:
        plan = plan_chat_grounding(
            "how do I create a Sword World RPG character?", grounded=False, has_window=False
        )

        assert plan.task_mode is ChatTaskMode.EXPLAIN_PROCEDURE
        message = render_grounded_user_message(
            "how do I create a Sword World RPG character?",
            plan,
            search_results="[[book-procedure-create-character]]",
        )
        assert "Task intent: explain the relevant procedure" in message
        assert "Prefer procedure pages" in message

    def test_creation_request_executes_procedure(self) -> None:
        plan = plan_chat_grounding(
            "actually create a Sword World RPG character", grounded=False, has_window=True
        )

        assert plan.task_mode is ChatTaskMode.EXECUTE_PROCEDURE
        message = render_grounded_user_message(
            "actually create a Sword World RPG character",
            plan,
            search_results="[[book-procedure-create-character]]",
        )
        assert "Task intent: execute the relevant procedure" in message
        assert "submit_procedure_execution" in message
        assert "not merely summarize it" in message
        assert "one concrete result or explicit unresolved note" in message

    def test_task_evidence_pack_is_injected_as_bounded_evidence(self) -> None:
        plan = plan_chat_grounding("actually create a device", grounded=False, has_window=False)

        message = render_grounded_user_message(
            "actually create a device",
            plan,
            search_results="[[device-procedure]]",
            task_evidence_pack=(
                "Deterministic task evidence pack:\n- Procedure: [[device-procedure]]"
            ),
        )

        assert "bounded evidence surface" in message
        assert "Deterministic task evidence pack" in message
        assert "do not ask for read/search tools" in message


class TestChatEvidenceScope:
    def test_rejects_aggregate_page_when_focused_candidate_is_stronger(self) -> None:
        pages = {
            "book": _page("book", "source-manifest"),
            "book-section": _page("book-section", "section-reference"),
        }
        scope = ChatEvidenceScope.from_search_hits(
            pages,
            (
                SearchHit("book-section", 247, "focused"),
                SearchHit("book", 227, "aggregate"),
            ),
        )
        metadata = parse_page(pages["book"]).page_metadata

        decision = scope.read_decision(metadata)

        assert not decision.allowed
        assert "[[book-section]]" in decision.message
        assert "source-manifest" in decision.message

    def test_allows_aggregate_page_when_it_is_the_strongest_candidate(self) -> None:
        pages = {
            "book": _page("book", "source-manifest"),
            "book-section": _page("book-section", "section-reference"),
        }
        scope = ChatEvidenceScope.from_search_hits(
            pages,
            (
                SearchHit("book", 500, "aggregate"),
                SearchHit("book-section", 247, "focused"),
            ),
        )
        metadata = parse_page(pages["book"]).page_metadata

        decision = scope.read_decision(metadata)

        assert decision.allowed


class TestChatResponseCitationPolicy:
    def test_accepts_link_to_read_page(self) -> None:
        policy = ChatResponseCitationPolicy(frozenset({"book-section"}))

        decision = policy.response_decision(
            "The answer is grounded in [[book-section]] (raw/book.pdf)."
        )

        assert decision.allowed

    def test_rejects_raw_source_without_wiki_page_link(self) -> None:
        policy = ChatResponseCitationPolicy(frozenset({"book-section"}))

        decision = policy.response_decision("The answer only cites (raw/book.pdf).")

        assert not decision.allowed
        assert "[[book-section]]" in decision.message
        assert "Raw source citations alone are not enough" in decision.message

    def test_rejects_non_page_wikilinks(self) -> None:
        policy = ChatResponseCitationPolicy(frozenset({"book-section"}))

        decision = policy.response_decision("Use [[Table 3: Core Sizes]] for the result.")

        assert not decision.allowed
        assert "Do not wrap table titles" in decision.message

    def test_rejects_unread_page_wikilinks(self) -> None:
        policy = ChatResponseCitationPolicy(frozenset({"book-section"}))

        decision = policy.response_decision("See [[other-section]] for the result.")

        assert not decision.allowed
        assert "Only cite wiki pages read" in decision.message


class TestChatPrompt:
    def test_missing_procedure_answers_must_stay_cited_and_local(self) -> None:
        assert "reporting missing procedure coverage" in CHAT_TEMPLATE
        assert "cite the inspected [[PageId]]" in CHAT_TEMPLATE
        assert "stop without asking the user to continue outside the wiki" in CHAT_TEMPLATE

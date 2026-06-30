"""Chat-domain helpers: deterministic, budget-bound grounding and history windows."""

from llmwiki.domain.chat_grounding import build_chat_grounding
from llmwiki.domain.chatwindow import (
    SEED_ANSWER_CAP_CHARS,
    QAPair,
    build_window,
    estimate_tokens,
)
from llmwiki.workflows.prompts import CHAT_TEMPLATE


def _pair(i: int, answer_chars: int = 400) -> QAPair:
    return QAPair(question=f"question {i}?", answer=f"answer {i} " + "x" * answer_chars)


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


class TestChatPrompt:
    def test_missing_procedure_answers_must_stay_cited_and_local(self) -> None:
        assert "reporting missing procedure coverage" in CHAT_TEMPLATE
        assert "cite the inspected [[PageId]]" in CHAT_TEMPLATE
        assert "stop without asking the user to continue outside the wiki" in CHAT_TEMPLATE

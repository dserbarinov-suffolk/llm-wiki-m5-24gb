"""Deterministic chat context window (pure).

The design's memory rule (docs/2026-06-12-persistent-chat-design.md):
conversation = Q/A pairs, evidence is re-fetched, prior answers are not
evidence. The window is the most recent pairs that fit a token budget —
no model-curated summaries, no retrieval. Clipping happens only in the
seed copies produced here; stored turns stay verbatim (preservation
guarantee).
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, replace

from llmwiki.domain.model_profile import DEFAULT_MODEL_PROFILE, ModelProfile


def estimate_tokens(
    text: str, model_profile: ModelProfile = DEFAULT_MODEL_PROFILE
) -> int:
    return model_profile.estimate_tokens(text)


@dataclass(frozen=True)
class QAPair:
    """One conversation turn as seeded context: question and answer text only."""

    question: str
    answer: str

    @property
    def token_estimate(self) -> int:
        return estimate_tokens(self.question) + estimate_tokens(self.answer)


def _clip_for_seed(pair: QAPair, model_profile: ModelProfile) -> QAPair:
    answer_cap = model_profile.chat_seed_answer_chars
    if len(pair.answer) <= answer_cap:
        return pair
    return replace(pair, answer=pair.answer[: answer_cap - 1] + "…")


def build_window(
    history: Sequence[QAPair],
    budget_tokens: int | None = None,
    model_profile: ModelProfile = DEFAULT_MODEL_PROFILE,
) -> tuple[QAPair, ...]:
    """Most recent pairs fitting the budget, in chronological order.

    Selection walks newest-first and stops at the first pair that would
    exceed the budget — a contiguous recent window, no gaps the model
    would misread as continuity.
    """
    resolved_budget = budget_tokens or model_profile.chat_history_tokens
    window: list[QAPair] = []
    used = 0
    for pair in reversed(history):
        clipped = _clip_for_seed(pair, model_profile)
        cost = model_profile.estimate_tokens(clipped.question) + model_profile.estimate_tokens(
            clipped.answer
        )
        if used + cost > resolved_budget:
            break
        window.append(clipped)
        used += cost
    return tuple(reversed(window))

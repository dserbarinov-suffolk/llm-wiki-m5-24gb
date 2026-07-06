"""Model capabilities and derived prompt budgets.

The profile is the source of truth for model-sized windows. Domain projection
limits should stay near their domain logic; prompt/tool/source batching limits
belong here.
"""

from __future__ import annotations

from dataclasses import dataclass

BASELINE_CONTEXT_TOKENS = 16_384
DEFAULT_MODEL_ID = "qwen3-14b-q4-k-m"


@dataclass(frozen=True)
class ModelProfile:
    model_id: str
    context_window_tokens: int
    chars_per_token_estimate: int = 4

    def estimate_tokens(self, text: str) -> int:
        return len(text) // self.chars_per_token_estimate

    def chars_for_tokens(self, tokens: int) -> int:
        return tokens * self.chars_per_token_estimate

    @property
    def chat_history_tokens(self) -> int:
        return self._scaled_tokens(6_000, minimum=512)

    @property
    def chat_seed_answer_chars(self) -> int:
        return self._scaled_chars(2_000, minimum=500)

    @property
    def chat_grounding_tokens(self) -> int:
        return self._scaled_tokens(3_500, minimum=512)

    @property
    def source_chunk_tokens(self) -> int:
        return self._scaled_tokens(6_000, minimum=512)

    @property
    def source_write_group_tokens(self) -> int:
        return self._scaled_tokens(2_200, minimum=256)

    @property
    def raw_source_read_chars(self) -> int:
        return self._scaled_chars(24_000, minimum=4_000)

    @property
    def read_page_default_chars(self) -> int:
        return self._scaled_chars(3_000, minimum=800)

    @property
    def read_page_max_chars(self) -> int:
        return max(self.read_page_default_chars, self._scaled_chars(5_000, minimum=1_200))

    @property
    def page_map_chars(self) -> int:
        return self._scaled_chars(2_800, minimum=800)

    @property
    def task_evidence_procedure_chars(self) -> int:
        return self._scaled_chars(5_000, minimum=1_200)

    @property
    def task_evidence_page_chars(self) -> int:
        return self._scaled_chars(350, minimum=120)

    @property
    def task_evidence_total_chars(self) -> int:
        return self._scaled_chars(8_000, minimum=2_000)

    @property
    def structured_evidence_artifact_chars(self) -> int:
        return self._scaled_chars(900, minimum=240)

    @property
    def structured_evidence_total_chars(self) -> int:
        return self._scaled_chars(12_000, minimum=3_000)

    @property
    def pdf_manifest_note_chars(self) -> int:
        return self._scaled_chars(1_500, minimum=400)

    def _scaled_tokens(self, baseline_tokens: int, *, minimum: int) -> int:
        scaled = round(baseline_tokens * self.context_window_tokens / BASELINE_CONTEXT_TOKENS)
        return max(minimum, scaled)

    def _scaled_chars(self, baseline_chars: int, *, minimum: int) -> int:
        scaled = round(baseline_chars * self.context_window_tokens / BASELINE_CONTEXT_TOKENS)
        return max(minimum, scaled)


def qwen3_14b_profile(context_window_tokens: int = BASELINE_CONTEXT_TOKENS) -> ModelProfile:
    return ModelProfile(
        model_id=DEFAULT_MODEL_ID,
        context_window_tokens=context_window_tokens,
    )


DEFAULT_MODEL_PROFILE = qwen3_14b_profile()

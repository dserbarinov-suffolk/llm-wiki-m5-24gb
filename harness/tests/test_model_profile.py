from llmwiki.domain.model_profile import BASELINE_CONTEXT_TOKENS, qwen3_14b_profile


def test_default_qwen_profile_preserves_current_16k_budgets() -> None:
    profile = qwen3_14b_profile()

    assert profile.context_window_tokens == BASELINE_CONTEXT_TOKENS
    assert profile.chars_per_token_estimate == 4
    assert profile.chat_history_tokens == 6_000
    assert profile.chat_grounding_tokens == 3_500
    assert profile.source_chunk_tokens == 6_000
    assert profile.source_write_group_tokens == 2_200
    assert profile.raw_source_read_chars == 24_000
    assert profile.read_page_default_chars == 3_000
    assert profile.read_page_max_chars == 5_000
    assert profile.page_map_chars == 2_800


def test_qwen_profile_scales_with_context_window() -> None:
    small = qwen3_14b_profile(8_192)
    large = qwen3_14b_profile(32_768)

    assert small.chat_history_tokens == 3_000
    assert small.source_chunk_tokens == 3_000
    assert small.source_write_group_tokens == 1_100
    assert small.raw_source_read_chars == 12_000
    assert large.chat_history_tokens == 12_000
    assert large.source_chunk_tokens == 12_000
    assert large.source_write_group_tokens == 4_400
    assert large.raw_source_read_chars == 48_000


def test_model_profile_owns_token_estimation() -> None:
    profile = qwen3_14b_profile()

    assert profile.estimate_tokens("x" * 400) == 100
    assert profile.chars_for_tokens(100) == 400

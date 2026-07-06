"""Explicit application state: filesystem layout and backend settings."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from llmwiki.domain.model_profile import (
    BASELINE_CONTEXT_TOKENS,
    ModelProfile,
    qwen3_14b_profile,
)

DEFAULT_PORT = 8080

_HF_CACHE_GLOB = ".cache/huggingface/hub/models--Qwen--Qwen3-14B-GGUF/snapshots/*/*.gguf"


class ConfigError(Exception):
    """Raised when the environment cannot satisfy an explicit requirement."""


@dataclass(frozen=True)
class WikiPaths:
    """The three layers of the wiki on disk, rooted at the project directory."""

    root: Path

    @property
    def raw_dir(self) -> Path:
        return self.root / "raw"

    @property
    def wiki_dir(self) -> Path:
        return self.root / "wiki"

    @property
    def schema_path(self) -> Path:
        return self.root / "SCHEMA.md"

    @property
    def index_path(self) -> Path:
        return self.wiki_dir / "index.md"

    @property
    def log_path(self) -> Path:
        return self.wiki_dir / "log.md"

    @property
    def graph_path(self) -> Path:
        return self.wiki_dir / "wiki-graph.json"

    @property
    def runs_dir(self) -> Path:
        return self.root / "harness" / "runs"

    @property
    def cache_dir(self) -> Path:
        """Derived extraction artifacts (disposable; not a wiki layer)."""
        return self.root / "harness" / ".cache"

    def validate(self) -> None:
        for path in (self.raw_dir, self.wiki_dir, self.schema_path, self.index_path, self.log_path):
            if not path.exists():
                raise ConfigError(
                    f"Wiki layer missing: {path}. Run from the project root "
                    "(or pass --root) — see SCHEMA.md for the expected layout."
                )


@dataclass(frozen=True)
class BackendConfig:
    """llama-server / model settings for the local Qwen3-14B."""

    gguf_path: Path
    port: int = DEFAULT_PORT
    model_profile: ModelProfile = qwen3_14b_profile()


def find_qwen3_gguf() -> Path | None:
    """Locate the Qwen3-14B GGUF in the Hugging Face hub cache."""
    matches = sorted(Path.home().glob(_HF_CACHE_GLOB))
    return matches[0] if matches else None


def load_backend_config() -> BackendConfig:
    """Resolve backend settings from the environment, failing loudly."""
    env_path = os.environ.get("LLMWIKI_GGUF")
    gguf = Path(env_path) if env_path else find_qwen3_gguf()
    if gguf is None or not gguf.exists():
        raise ConfigError(
            "Qwen3-14B GGUF not found. Set LLMWIKI_GGUF to the model file, or "
            "download it: llama-cli -hf Qwen/Qwen3-14B-GGUF:Q4_K_M"
        )
    port = int(os.environ.get("LLMWIKI_PORT", str(DEFAULT_PORT)))
    return BackendConfig(gguf_path=gguf, port=port, model_profile=load_model_profile())


def load_model_profile() -> ModelProfile:
    ctx = int(os.environ.get("LLMWIKI_CTX", str(BASELINE_CONTEXT_TOKENS)))
    return qwen3_14b_profile(ctx)

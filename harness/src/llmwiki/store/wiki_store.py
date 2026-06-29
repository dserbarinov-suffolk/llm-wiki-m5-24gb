"""WikiStore: the only component that touches the wiki on disk.

Boundary contract (see design doc):
- `raw/` is read-only — there is no write API for it, and reads are
  confined to the directory (no traversal).
- Page writes are confined to `wiki/` and always upsert the page's
  index.md entry in the same operation, so the index can never go stale.
- log.md is append-only.

Error messages raised here are fed back to the model verbatim by forge's
tool-error channel, so they are written as corrective instructions.
"""

from __future__ import annotations

import hashlib
import re
from collections.abc import Callable
from pathlib import Path

from llmwiki.config import SOURCE_READ_BUDGET_CHARS, WikiPaths
from llmwiki.domain.index import index_page_ids, remove_index_entries, upsert_index_entry
from llmwiki.domain.log import format_log_entry
from llmwiki.domain.objects import RawSource
from llmwiki.domain.pages import (
    LOCAL_FLAT_STRUCTURE,
    PageError,
    PageMetadata,
    WikiPage,
    WikiStructure,
    parse_page,
    render_page,
    validate_page_id,
)

_RESERVED_PAGE_IDS = frozenset({"index", "log"})
_TRUNCATION_MARKER = "\n\n[TRUNCATED: source exceeds the read budget; summarize what is shown]"


class WikiStoreError(Exception):
    """Base error; message is safe to feed back to the model."""


class PageNotFoundError(WikiStoreError):
    pass


class SourceNotFoundError(WikiStoreError):
    pass


class WikiStore:
    def __init__(self, paths: WikiPaths, structure: WikiStructure = LOCAL_FLAT_STRUCTURE) -> None:
        self._paths = paths
        self._structure = structure

    @property
    def structure(self) -> WikiStructure:
        return self._structure

    # -- schema layer -----------------------------------------------------

    def read_schema(self) -> str:
        return self._paths.schema_path.read_text(encoding="utf-8")

    # -- raw layer (read-only) ---------------------------------------------

    def raw_source_path(self, source_locator: str) -> Path:
        """Resolve a RawSource locator (read-only; confined to raw/)."""
        path = (self._paths.raw_dir / source_locator).resolve()
        if not path.is_relative_to(self._paths.raw_dir.resolve()):
            raise SourceNotFoundError(
                f"{source_locator!r} is outside raw/. "
                "Pass a source_locator relative to raw/, e.g. 'article.md'."
            )
        if not path.is_file():
            available = ", ".join(self.list_sources()) or "none"
            raise SourceNotFoundError(
                f"No RawSource at raw/{source_locator}. Available: {available}."
            )
        return path

    def raw_source(self, source_locator: str) -> RawSource:
        self.raw_source_path(source_locator)
        return RawSource.from_locator(source_locator)

    def read_source(self, source_locator: str) -> str:
        text = self.raw_source_path(source_locator).read_text(encoding="utf-8")
        if len(text) > SOURCE_READ_BUDGET_CHARS:
            return text[:SOURCE_READ_BUDGET_CHARS] + _TRUNCATION_MARKER
        return text

    def list_sources(self) -> list[str]:
        raw = self._paths.raw_dir
        return sorted(
            str(p.relative_to(raw))
            for p in raw.rglob("*")
            if p.is_file() and not p.name.startswith(".")
        )

    # -- wiki layer ---------------------------------------------------------

    def list_pages(self) -> list[str]:
        return sorted(
            p.stem
            for p in self._paths.wiki_dir.rglob("*.md")
            if p.stem not in _RESERVED_PAGE_IDS and not _is_hidden_path(p, self._paths.wiki_dir)
        )

    def read_page(self, page_id: str) -> str:
        validate_page_id(page_id)
        path = self.page_path_for_page_id(page_id)
        if page_id in _RESERVED_PAGE_IDS or not path.is_file():
            raise PageNotFoundError(
                f"No WikiPage with page_id {page_id!r}. Use search_wiki to find existing pages."
            )
        return path.read_text(encoding="utf-8")

    def read_wiki_page(self, page_id: str) -> WikiPage:
        return parse_page(self.read_page(page_id))

    def page_texts(self) -> dict[str, str]:
        return {page_id: self.read_page(page_id) for page_id in self.list_pages()}

    def write_page(self, page: WikiPage) -> None:
        if page.page_id in _RESERVED_PAGE_IDS:
            raise WikiStoreError(f"{page.page_id!r} is reserved; choose another page_id.")
        page_path = self.page_path(page)
        self._ensure_wiki_path(page_path)
        page_path.parent.mkdir(parents=True, exist_ok=True)
        index_text = upsert_index_entry(self.read_index(), page.page_metadata)
        page_path.write_text(render_page(page), encoding="utf-8")
        self._paths.index_path.write_text(index_text, encoding="utf-8")

    def delete_source_pages_not_in(
        self, source_locator: str, keep_page_ids: set[str]
    ) -> tuple[str, ...]:
        source_ref = f"raw/{source_locator}"
        return self._delete_generated_pages(
            keep_page_ids,
            lambda metadata: metadata.sources == (source_ref,),
        )

    def delete_cross_source_pages_not_in(self, keep_page_ids: set[str]) -> tuple[str, ...]:
        return self._delete_generated_pages(
            keep_page_ids,
            lambda metadata: (
                metadata.projection_coverage_pointer.startswith("cross-source-")
                or metadata.projection_coverage_pointer.startswith("canonical-concept-")
            ),
        )

    def page_path_for_page_id(self, page_id: str) -> Path:
        candidates = self._page_paths_for_page_id(page_id)
        if len(candidates) == 1:
            return candidates[0]
        if len(candidates) > 1:
            rendered = ", ".join(str(path.relative_to(self._paths.wiki_dir)) for path in candidates)
            raise WikiStoreError(f"Multiple WikiPages with page_id {page_id!r}: {rendered}.")
        try:
            metadata = PageMetadata(page_id=page_id, page_kind="source", summary="placeholder")
            page = WikiPage.from_metadata(metadata, "")
            return self._paths.wiki_dir / page.page_path(self._structure)
        except PageError:
            return self._paths.wiki_dir / f"{page_id}.md"

    def page_path(self, page: WikiPage) -> Path:
        return self._paths.wiki_dir / page.page_path(self._structure)

    def rendered_page_path(self, page: WikiPage) -> str:
        return str(page.page_path(self._structure))

    def _ensure_wiki_path(self, path: Path) -> None:
        if not path.resolve().is_relative_to(self._paths.wiki_dir.resolve()):
            raise WikiStoreError(f"Rendered page path {path} is outside wiki/.")

    def _page_paths_for_page_id(self, page_id: str) -> list[Path]:
        validate_page_id(page_id)
        return sorted(
            path
            for path in self._paths.wiki_dir.rglob(f"{page_id}.md")
            if path.stem == page_id and not _is_hidden_path(path, self._paths.wiki_dir)
        )

    def _delete_generated_pages(
        self, keep_page_ids: set[str], should_delete: Callable[[PageMetadata], bool]
    ) -> tuple[str, ...]:
        removed: list[str] = []
        for page_id in self.list_pages():
            if page_id in keep_page_ids:
                continue
            page = self.read_wiki_page(page_id)
            if not should_delete(page.page_metadata):
                continue
            path = self.page_path_for_page_id(page_id)
            self._ensure_wiki_path(path)
            path.unlink()
            removed.append(page_id)
        if removed:
            index_text = remove_index_entries(self.read_index(), set(removed))
            self._paths.index_path.write_text(index_text, encoding="utf-8")
        return tuple(removed)

    # -- navigation files ----------------------------------------------------

    def read_index(self) -> str:
        return self._paths.index_path.read_text(encoding="utf-8")

    def index_page_ids(self) -> set[str]:
        return index_page_ids(self.read_index())

    def append_log(self, date_iso: str, op: str, subject: str, detail: str) -> None:
        entry = format_log_entry(date_iso, op, subject, detail)
        with self._paths.log_path.open("a", encoding="utf-8") as fh:
            fh.write(entry)

    def read_graph_json(self) -> str | None:
        if not self._paths.graph_path.exists():
            return None
        return self._paths.graph_path.read_text(encoding="utf-8")

    def write_graph_json(self, text: str) -> None:
        self._paths.graph_path.write_text(text, encoding="utf-8")

    # -- harness-owned ingest artifacts --------------------------------------

    def page_plan_artifact_dir(self, source_locator: str) -> Path:
        digest = hashlib.sha256(source_locator.encode("utf-8")).hexdigest()[:12]
        stem = re.sub(r"[^a-z0-9]+", "-", Path(source_locator).stem.lower()).strip("-")
        return self._paths.cache_dir / "page-plans" / f"{stem or 'source'}-{digest}"

    def write_page_plan_artifacts(
        self,
        source_locator: str,
        page_plan_json: str,
        observation_report: str,
    ) -> None:
        artifact_dir = self.page_plan_artifact_dir(source_locator)
        artifact_dir.mkdir(parents=True, exist_ok=True)
        (artifact_dir / "page-plan.json").write_text(page_plan_json, encoding="utf-8")
        (artifact_dir / "observation-report.md").write_text(observation_report, encoding="utf-8")

    def write_evidence_registry_artifact(self, source_locator: str, registry_json: str) -> None:
        artifact_dir = self.page_plan_artifact_dir(source_locator)
        artifact_dir.mkdir(parents=True, exist_ok=True)
        (artifact_dir / "evidence-registry.json").write_text(registry_json, encoding="utf-8")

    def read_evidence_registry_artifact(self, source_locator: str) -> str | None:
        path = self.page_plan_artifact_dir(source_locator) / "evidence-registry.json"
        return path.read_text(encoding="utf-8") if path.is_file() else None

    def write_evidence_locator_index_artifact(
        self, source_locator: str, locator_index_json: str
    ) -> None:
        artifact_dir = self.page_plan_artifact_dir(source_locator)
        artifact_dir.mkdir(parents=True, exist_ok=True)
        (artifact_dir / "evidence-locators.json").write_text(locator_index_json, encoding="utf-8")

    def read_evidence_locator_index_artifact(self, source_locator: str) -> str | None:
        path = self.page_plan_artifact_dir(source_locator) / "evidence-locators.json"
        return path.read_text(encoding="utf-8") if path.is_file() else None

    def write_artifact_fingerprint(self, source_locator: str, fingerprint_json: str) -> None:
        artifact_dir = self.page_plan_artifact_dir(source_locator)
        artifact_dir.mkdir(parents=True, exist_ok=True)
        (artifact_dir / "artifact-fingerprint.json").write_text(fingerprint_json, encoding="utf-8")

    def read_artifact_fingerprint(self, source_locator: str) -> str | None:
        path = self.page_plan_artifact_dir(source_locator) / "artifact-fingerprint.json"
        return path.read_text(encoding="utf-8") if path.is_file() else None

    def write_ingest_confidence_report_artifact(self, source_locator: str, report: str) -> None:
        artifact_dir = self.page_plan_artifact_dir(source_locator)
        artifact_dir.mkdir(parents=True, exist_ok=True)
        (artifact_dir / "ingest-confidence-report.md").write_text(report, encoding="utf-8")

    def write_claim_support_report_artifact(self, source_locator: str, report: str) -> None:
        artifact_dir = self.page_plan_artifact_dir(source_locator)
        artifact_dir.mkdir(parents=True, exist_ok=True)
        (artifact_dir / "claim-support-report.md").write_text(report, encoding="utf-8")

    def write_ledger_artifacts(self, source_locator: str, files: dict[str, str]) -> None:
        """Persist the claim-ledger bundle (one canonical JSON file each)."""
        artifact_dir = self.page_plan_artifact_dir(source_locator) / "ledger"
        artifact_dir.mkdir(parents=True, exist_ok=True)
        for filename, text in files.items():
            (artifact_dir / filename).write_text(text, encoding="utf-8")

    def read_claim_ledger_artifact(self, source_locator: str) -> str | None:
        path = self.page_plan_artifact_dir(source_locator) / "ledger" / "claim-ledger.json"
        return path.read_text(encoding="utf-8") if path.is_file() else None

    def list_claim_ledger_artifacts(self) -> list[str]:
        """Every stored claim ledger (canonical JSON), one per ingested source."""
        base = self._paths.cache_dir / "page-plans"
        if not base.is_dir():
            return []
        return [
            path.read_text(encoding="utf-8")
            for path in sorted(base.glob("*/ledger/claim-ledger.json"))
        ]

    def list_topic_index_artifacts(self) -> list[str]:
        """Every stored per-source topic index (canonical JSON)."""
        base = self._paths.cache_dir / "page-plans"
        if not base.is_dir():
            return []
        return [
            path.read_text(encoding="utf-8") for path in sorted(base.glob("*/ledger/topics.json"))
        ]


def _is_hidden_path(path: Path, root: Path) -> bool:
    return any(part.startswith(".") for part in path.relative_to(root).parts)

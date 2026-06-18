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

from pathlib import Path

from llmwiki.config import SOURCE_READ_BUDGET_CHARS, WikiPaths
from llmwiki.domain.index import index_page_names, upsert_index_entry
from llmwiki.domain.log import format_log_entry
from llmwiki.domain.objects import RawSource
from llmwiki.domain.pages import (
    LOCAL_FLAT_STRUCTURE,
    PageError,
    WikiPage,
    WikiStructure,
    parse_page,
    render_page,
    validate_page_name,
)

_RESERVED_NAMES = frozenset({"index", "log"})
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

    def source_path(self, rel_path: str) -> Path:
        """Resolve a raw-source path (read-only; confined to raw/)."""
        path = (self._paths.raw_dir / rel_path).resolve()
        if not path.is_relative_to(self._paths.raw_dir.resolve()):
            raise SourceNotFoundError(
                f"{rel_path!r} is outside raw/. Pass a path relative to raw/, e.g. 'article.md'."
            )
        if not path.is_file():
            available = ", ".join(self.list_sources()) or "none"
            raise SourceNotFoundError(f"No source at raw/{rel_path}. Available: {available}.")
        return path

    def raw_source(self, rel_path: str) -> RawSource:
        self.source_path(rel_path)
        return RawSource.from_locator(rel_path)

    def read_source(self, rel_path: str) -> str:
        text = self.source_path(rel_path).read_text(encoding="utf-8")
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
            if p.stem not in _RESERVED_NAMES and not _is_hidden_path(p, self._paths.wiki_dir)
        )

    def read_page(self, name: str) -> str:
        validate_page_name(name)
        path = self.page_path_for_name(name)
        if name in _RESERVED_NAMES or not path.is_file():
            raise PageNotFoundError(
                f"No page named {name!r}. Use search_wiki to find existing pages."
            )
        return path.read_text(encoding="utf-8")

    def read_wiki_page(self, name: str) -> WikiPage:
        return parse_page(name, self.read_page(name))

    def page_texts(self) -> dict[str, str]:
        return {name: self.read_page(name) for name in self.list_pages()}

    def write_page(self, page: WikiPage) -> None:
        if page.name in _RESERVED_NAMES:
            raise WikiStoreError(
                f"{page.name!r} is reserved (maintained by the harness); choose another name."
            )
        page_path = self.page_path(page)
        self._ensure_wiki_path(page_path)
        page_path.parent.mkdir(parents=True, exist_ok=True)
        index_text = upsert_index_entry(self.read_index(), page.name, page.category, page.summary)
        page_path.write_text(render_page(page), encoding="utf-8")
        self._paths.index_path.write_text(index_text, encoding="utf-8")

    def page_path_for_name(self, name: str) -> Path:
        candidates = self._page_paths_for_name(name)
        if len(candidates) == 1:
            return candidates[0]
        if len(candidates) > 1:
            rendered = ", ".join(str(path.relative_to(self._paths.wiki_dir)) for path in candidates)
            raise WikiStoreError(f"Multiple pages named {name!r}: {rendered}.")
        try:
            page = WikiPage(name=name, category="source", summary="placeholder", body="")
            return self._paths.wiki_dir / page.page_path(self._structure)
        except PageError:
            return self._paths.wiki_dir / f"{name}.md"

    def page_path(self, page: WikiPage) -> Path:
        return self._paths.wiki_dir / page.page_path(self._structure)

    def rendered_page_path(self, page: WikiPage) -> str:
        return str(page.page_path(self._structure))

    def _ensure_wiki_path(self, path: Path) -> None:
        if not path.resolve().is_relative_to(self._paths.wiki_dir.resolve()):
            raise WikiStoreError(f"Rendered page path {path} is outside wiki/.")

    def _page_paths_for_name(self, name: str) -> list[Path]:
        validate_page_name(name)
        return sorted(
            path
            for path in self._paths.wiki_dir.rglob(f"{name}.md")
            if path.stem == name and not _is_hidden_path(path, self._paths.wiki_dir)
        )

    # -- navigation files ----------------------------------------------------

    def read_index(self) -> str:
        return self._paths.index_path.read_text(encoding="utf-8")

    def index_names(self) -> set[str]:
        return index_page_names(self.read_index())

    def append_log(self, date_iso: str, op: str, subject: str, detail: str) -> None:
        entry = format_log_entry(date_iso, op, subject, detail)
        with self._paths.log_path.open("a", encoding="utf-8") as fh:
            fh.write(entry)


def _is_hidden_path(path: Path, root: Path) -> bool:
    return any(part.startswith(".") for part in path.relative_to(root).parts)

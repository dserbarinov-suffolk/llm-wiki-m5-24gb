"""Synthetic procedure fixtures for portability tests."""

from llmwiki.domain.chat_grounding import ChatTaskMode
from llmwiki.domain.search import SearchHit
from llmwiki.domain.task_evidence import TaskEvidencePack, build_task_evidence_pack


def procedure_pack() -> TaskEvidencePack:
    pack = build_task_evidence_pack(
        synthetic_pages(),
        search_hits(),
        task_mode=ChatTaskMode.EXECUTE_PROCEDURE,
    )
    assert pack is not None
    return pack


def synthetic_pages() -> dict[str, str]:
    return {
        "aether-procedure-build-device": _page(
            "aether-procedure-build-device",
            page_kind="procedure",
            page_family="procedure-guide",
            summary="Build an aether device from source-derived steps.",
            body="""
            # Build Aether Device

            ## Procedure Steps

            1. **Select core** (`choose`) - evidence section [[aether-core]].
            2. **Calculate load** (`calculate`) - evidence section [[aether-load]].
            3. **Record unresolved safety check** (`record`) - evidence section [[aether-safety]].
            """,
        ),
        "aether-core": _page(
            "aether-core",
            page_kind="source",
            page_family="section-reference",
            summary="Core selection rules.",
            body="""
            # Core Selection

            - Table 3: Core Sizes shows valid core choices.

            | Core | Size |
            | --- | --- |
            | Copper | Small |
            | Silver | Large |
            """,
        ),
        "aether-load": _page(
            "aether-load",
            page_kind="source",
            page_family="section-reference",
            summary="Load calculation rules.",
            body="""
            # Load Calculation

            - The load formula is 2 x 3 = 6.
            """,
        ),
        "aether-safety": _page(
            "aether-safety",
            page_kind="source",
            page_family="section-reference",
            summary="Safety check is incomplete in the source.",
            body="""
            # Safety Check

            - The source names a safety check but gives no threshold.
            """,
        ),
    }


def search_hits() -> tuple[SearchHit, ...]:
    return (
        SearchHit("aether-procedure-build-device", 400, "procedure"),
        SearchHit("aether-core", 300, "core"),
        SearchHit("aether-load", 280, "load"),
    )


def _page(
    page_id: str,
    *,
    page_kind: str,
    page_family: str = "",
    summary: str,
    body: str,
) -> str:
    family = f"page_family: {page_family}\n" if page_family else ""
    return (
        "---\n"
        f"page_id: {page_id}\n"
        f"page_kind: {page_kind}\n"
        f"{family}"
        f"summary: {summary}\n"
        "---\n\n"
        f"{body.strip()}\n"
    )

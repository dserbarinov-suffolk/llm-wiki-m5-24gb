"""Constrained lint repair tools.

These adapters expose narrow domain operations to the lint workflow. They do
not let the model rewrite a page wholesale.
"""

from __future__ import annotations

from dataclasses import replace

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field

from llmwiki.domain.lint_repair import (
    LintRepairDecision,
    add_related_link,
    remove_broken_link,
    replace_link_target,
)
from llmwiki.domain.pages import WikiPage
from llmwiki.store import WikiStore


class AddRelatedLinkParams(BaseModel):
    page_id: str = Field(description="Existing page_id that should carry the new link.")
    target_page_id: str = Field(description="Existing page_id the source page should link to.")
    reason: str = Field(description="Brief source-neutral reason for this navigation link.")


class ReplaceLinkTargetParams(BaseModel):
    page_id: str = Field(description="Existing page_id containing the incorrect link.")
    old_target_page_id: str = Field(description="Current linked page_id to replace.")
    new_target_page_id: str = Field(description="Existing page_id that should be linked instead.")
    reason: str = Field(description="Brief reason this target is the correct repair.")


class RemoveBrokenLinkParams(BaseModel):
    page_id: str = Field(description="Existing page_id containing the broken link.")
    target_page_id: str = Field(description="Broken linked page_id to remove or de-link.")
    reason: str = Field(description="Brief reason the broken target should not be a wiki link.")


class RequestSourceRegenerationParams(BaseModel):
    page_id: str = Field(description="Protected generated page that needs non-link repair.")
    reason: str = Field(description="Why this should be regenerated instead of patched by lint.")


def add_related_link_tool(store: WikiStore, today: str) -> ToolDef:
    def _add_related_link(**kwargs: object) -> str:
        params = AddRelatedLinkParams(**kwargs)  # type: ignore[arg-type]
        page = store.read_wiki_page(params.page_id)
        if params.target_page_id not in store.list_pages():
            return f"Rejected: [[{params.target_page_id}]] does not exist."
        decision = add_related_link(
            page.page_metadata,
            page.page_body,
            params.target_page_id,
            params.reason,
        )
        return _apply_decision(store, today, page, decision)

    return ToolDef(
        spec=ToolSpec(
            name="add_related_link",
            description=(
                "Add one bounded related-page link to an existing page while preserving "
                "its metadata and body content. Use this to repair orphan pages by "
                "linking FROM a related existing page TO the orphan."
            ),
            parameters=AddRelatedLinkParams,
        ),
        callable=_add_related_link,
        prerequisites=[{"tool": "read_page", "match_arg": "page_id"}],
    )


def replace_link_target_tool(store: WikiStore, today: str) -> ToolDef:
    def _replace_link_target(**kwargs: object) -> str:
        params = ReplaceLinkTargetParams(**kwargs)  # type: ignore[arg-type]
        page = store.read_wiki_page(params.page_id)
        if params.new_target_page_id not in store.list_pages():
            return f"Rejected: [[{params.new_target_page_id}]] does not exist."
        decision = replace_link_target(
            page.page_metadata,
            page.page_body,
            params.old_target_page_id,
            params.new_target_page_id,
            params.reason,
        )
        return _apply_decision(store, today, page, decision)

    return ToolDef(
        spec=ToolSpec(
            name="replace_link_target",
            description=(
                "Replace an exact wiki link target on a manual page. Generated "
                "projection pages are protected; request source regeneration for "
                "non-link corrections there."
            ),
            parameters=ReplaceLinkTargetParams,
        ),
        callable=_replace_link_target,
        prerequisites=[{"tool": "read_page", "match_arg": "page_id"}],
    )


def remove_broken_link_tool(store: WikiStore, today: str) -> ToolDef:
    def _remove_broken_link(**kwargs: object) -> str:
        params = RemoveBrokenLinkParams(**kwargs)  # type: ignore[arg-type]
        page = store.read_wiki_page(params.page_id)
        decision = remove_broken_link(
            page.page_metadata,
            page.page_body,
            params.target_page_id,
            params.reason,
        )
        return _apply_decision(store, today, page, decision)

    return ToolDef(
        spec=ToolSpec(
            name="remove_broken_link",
            description=(
                "Remove or de-link one exact broken wiki link on a manual page. "
                "Generated projection pages are protected; request source "
                "regeneration for non-link corrections there."
            ),
            parameters=RemoveBrokenLinkParams,
        ),
        callable=_remove_broken_link,
        prerequisites=[{"tool": "read_page", "match_arg": "page_id"}],
    )


def request_source_regeneration_tool() -> ToolDef:
    def _request_source_regeneration(**kwargs: object) -> str:
        params = RequestSourceRegenerationParams(**kwargs)  # type: ignore[arg-type]
        return (
            f"Recorded regeneration request for [[{params.page_id}]]: "
            f"{' '.join(params.reason.split())}"
        )

    return ToolDef(
        spec=ToolSpec(
            name="request_source_regeneration",
            description=(
                "Report that a protected generated page needs regeneration rather "
                "than lint-time patching. This records intent in the lint transcript "
                "and final report; it does not mutate pages."
            ),
            parameters=RequestSourceRegenerationParams,
        ),
        callable=_request_source_regeneration,
    )


def _apply_decision(
    store: WikiStore,
    today: str,
    page: WikiPage,
    decision: LintRepairDecision,
) -> str:
    if not decision.accepted:
        return f"Rejected: {decision.message}"
    if not decision.changed:
        return f"No change: {decision.message}"
    metadata = replace(page.page_metadata, updated=today)
    store.write_page(WikiPage.from_metadata(metadata, decision.updated_body))
    return f"Applied: {decision.message}"

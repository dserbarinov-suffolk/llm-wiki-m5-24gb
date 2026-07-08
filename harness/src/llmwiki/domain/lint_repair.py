"""Pure lint repair operations for bounded wiki maintenance.

Lint repairs are intentionally narrower than page writes. They preserve the
page's authored/projection content and operate only on link-shaped structure
that deterministic lint can validate on the next pass.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

from llmwiki.domain.links import extract_links
from llmwiki.domain.pages import PageMetadata, validate_page_id
from llmwiki.domain.schema import PAGE_FAMILIES

SYSTEM_OWNED_PAGE_IDS = frozenset({"wiki-health"})
GENERATED_PAGE_FAMILIES = frozenset(PAGE_FAMILIES)
LINT_LINK_SECTION = "## Lint-maintained links"

PageMutationKind = Literal["manual", "generated-source-projection", "system-owned"]
LintRepairActionType = Literal[
    "add-related-link",
    "replace-link-target",
    "remove-broken-link",
    "request-source-regeneration",
]


@dataclass(frozen=True)
class PageMutationPolicy:
    page_id: str
    mutation_kind: PageMutationKind
    allow_related_link: bool
    allow_link_rewrite: bool
    reason: str


@dataclass(frozen=True)
class LintRepairAction:
    action_type: LintRepairActionType
    page_id: str = ""
    target_page_id: str = ""
    old_target_page_id: str = ""
    new_target_page_id: str = ""
    reason: str = ""


@dataclass(frozen=True)
class LintRepairDecision:
    action: LintRepairAction
    accepted: bool
    changed: bool
    message: str
    updated_body: str = ""


def mutation_policy(metadata: PageMetadata) -> PageMutationPolicy:
    if metadata.page_id in SYSTEM_OWNED_PAGE_IDS:
        return PageMutationPolicy(
            page_id=metadata.page_id,
            mutation_kind="system-owned",
            allow_related_link=False,
            allow_link_rewrite=False,
            reason="system-owned page is maintained by the runtime",
        )
    if _is_generated_projection(metadata):
        return PageMutationPolicy(
            page_id=metadata.page_id,
            mutation_kind="generated-source-projection",
            allow_related_link=True,
            allow_link_rewrite=False,
            reason="generated projection pages can receive bounded navigation links only",
        )
    return PageMutationPolicy(
        page_id=metadata.page_id,
        mutation_kind="manual",
        allow_related_link=True,
        allow_link_rewrite=True,
        reason="manual page can receive bounded link repairs",
    )


def add_related_link(
    metadata: PageMetadata, page_body: str, target_page_id: str, reason: str
) -> LintRepairDecision:
    target_page_id = validate_page_id(target_page_id)
    action = LintRepairAction(
        action_type="add-related-link",
        page_id=metadata.page_id,
        target_page_id=target_page_id,
        reason=reason,
    )
    policy = mutation_policy(metadata)
    if not policy.allow_related_link:
        return _rejected(action, policy.reason, page_body)
    link = f"[[{target_page_id}]]"
    if link in page_body:
        return LintRepairDecision(
            action,
            accepted=True,
            changed=False,
            message="link already exists",
        )
    return LintRepairDecision(
        action,
        accepted=True,
        changed=True,
        message=f"added bounded related link to [[{target_page_id}]]",
        updated_body=_append_lint_link(page_body, target_page_id, reason),
    )


def replace_link_target(
    metadata: PageMetadata,
    page_body: str,
    old_target_page_id: str,
    new_target_page_id: str,
    reason: str,
) -> LintRepairDecision:
    old_target_page_id = validate_page_id(old_target_page_id)
    new_target_page_id = validate_page_id(new_target_page_id)
    action = LintRepairAction(
        action_type="replace-link-target",
        page_id=metadata.page_id,
        old_target_page_id=old_target_page_id,
        new_target_page_id=new_target_page_id,
        reason=reason,
    )
    policy = mutation_policy(metadata)
    if not policy.allow_link_rewrite:
        return _rejected(action, policy.reason, page_body)
    old_link = f"[[{old_target_page_id}]]"
    if old_link not in page_body:
        if f"[[{new_target_page_id}]]" in page_body:
            return LintRepairDecision(
                action,
                accepted=True,
                changed=False,
                message="replacement link already exists and old target is absent",
            )
        return _rejected(action, f"{old_link} is not present in page body", page_body)
    return LintRepairDecision(
        action,
        accepted=True,
        changed=True,
        message=f"replaced [[{old_target_page_id}]] with [[{new_target_page_id}]]",
        updated_body=page_body.replace(old_link, f"[[{new_target_page_id}]]"),
    )


def remove_broken_link(
    metadata: PageMetadata, page_body: str, target_page_id: str, reason: str
) -> LintRepairDecision:
    target_page_id = validate_page_id(target_page_id)
    action = LintRepairAction(
        action_type="remove-broken-link",
        page_id=metadata.page_id,
        target_page_id=target_page_id,
        reason=reason,
    )
    policy = mutation_policy(metadata)
    if not policy.allow_link_rewrite:
        return _rejected(action, policy.reason, page_body)
    link = f"[[{target_page_id}]]"
    if link not in page_body:
        return LintRepairDecision(
            action,
            accepted=True,
            changed=False,
            message="broken link is already absent",
        )
    return LintRepairDecision(
        action,
        accepted=True,
        changed=True,
        message=f"removed or de-linked [[{target_page_id}]]",
        updated_body=_remove_or_delink(page_body, target_page_id),
    )


def _is_generated_projection(metadata: PageMetadata) -> bool:
    return bool(
        metadata.page_family in GENERATED_PAGE_FAMILIES
        or metadata.source_id
        or metadata.projection_coverage_pointer
        or metadata.category_path
    )


def _append_lint_link(page_body: str, target_page_id: str, reason: str) -> str:
    lines = page_body.rstrip().splitlines()
    line = f"- [[{target_page_id}]] - {_single_line(reason)}"
    if LINT_LINK_SECTION not in lines:
        return f"{page_body.rstrip()}\n\n{LINT_LINK_SECTION}\n\n{line}"

    heading_index = lines.index(LINT_LINK_SECTION)
    insert_index = len(lines)
    for index in range(heading_index + 1, len(lines)):
        if lines[index].startswith("## "):
            insert_index = index
            break
    lines.insert(insert_index, line)
    return "\n".join(lines)


def _remove_or_delink(page_body: str, target_page_id: str) -> str:
    link = f"[[{target_page_id}]]"
    kept_lines: list[str] = []
    for line in page_body.splitlines():
        if link not in line:
            kept_lines.append(line)
            continue
        line_links = extract_links(line)
        if line.strip().startswith("- ") and line_links == {target_page_id}:
            continue
        kept_lines.append(line.replace(link, target_page_id))
    return _collapse_excess_blank_lines("\n".join(kept_lines)).strip()


def _collapse_excess_blank_lines(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text)


def _single_line(text: str) -> str:
    cleaned = " ".join(text.split())
    return cleaned or "lint repair"


def _rejected(action: LintRepairAction, message: str, page_body: str) -> LintRepairDecision:
    return LintRepairDecision(
        action=action,
        accepted=False,
        changed=False,
        message=message,
        updated_body=page_body,
    )

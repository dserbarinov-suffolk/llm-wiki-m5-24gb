"""Forge workflow definitions for the three wiki operations."""

from llmwiki.workflows.definitions import (
    build_ingest_workflow,
    build_lint_workflow,
    build_query_workflow,
)

__all__ = ["build_ingest_workflow", "build_lint_workflow", "build_query_workflow"]

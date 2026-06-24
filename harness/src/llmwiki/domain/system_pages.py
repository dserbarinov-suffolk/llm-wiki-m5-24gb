"""Harness-maintained wiki pages that should not be sampled as claims."""

SYSTEM_PAGES = frozenset(
    {
        "index",
        "log",
        "wiki-health",
        "wiki-ingest-confidence",
        "wiki-claim-support",
    }
)

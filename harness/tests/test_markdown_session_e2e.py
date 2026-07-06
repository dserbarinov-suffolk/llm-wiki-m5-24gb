import json

from fakes import FakeClient
from forge.context import ContextManager, NoCompact

from llmwiki.config import WikiPaths
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore

TODAY = "2026-07-06"


def _session(store: WikiStore, paths: WikiPaths) -> Session:
    return Session(
        store=store,
        client=FakeClient([]),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="markdown-test",
    )


class TestMarkdownIngest:
    async def test_markdown_ingest_reads_past_prompt_read_budget(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        sentinel = "The final sentinel concept is retained."
        filler = "Background material is intentionally repetitive.\n\n"
        body = "# Long Source\n\n" + filler * (
            (store.model_profile.raw_source_read_chars // len(filler)) + 2
        )
        body += f"\n\n# Final Section\n\n{sentinel}\n"
        (paths.raw_dir / "long-source.md").write_text(body, encoding="utf-8")

        result = await _session(store, paths).ingest("long-source.md")

        assert "Claim-ledger ingest" in result.output
        ledger = json.loads(store.read_claim_ledger_artifact("long-source.md"))["ledger"]
        rendered = json.dumps(ledger)
        assert sentinel in rendered
        assert "[TRUNCATED" not in rendered

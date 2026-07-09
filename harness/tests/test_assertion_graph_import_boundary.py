from __future__ import annotations

import ast
from pathlib import Path

PACKAGE_ROOT = Path("harness/src/llmwiki/domain/assertion_graph")
ALLOWED_IMPORT_ROOTS = {
    "__future__",
    "enum",
    "json",
    "pydantic",
    "typing",
    "llmwiki.domain.assertion_graph",
}


def test_assertion_graph_domain_core_has_no_adapter_or_io_imports() -> None:
    for path in PACKAGE_ROOT.glob("*.py"):
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module is not None:
                imported_names = [node.module]
            else:
                continue

            for imported_name in imported_names:
                assert any(
                    imported_name == allowed_root or imported_name.startswith(f"{allowed_root}.")
                    for allowed_root in ALLOWED_IMPORT_ROOTS
                ), f"{path} imports {imported_name}"

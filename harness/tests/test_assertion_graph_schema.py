from __future__ import annotations

from llmwiki.domain.assertion_graph import PUBLIC_DOMAIN_RECORDS, domain_json_schemas
from llmwiki.domain.assertion_graph.schemas import schema_for


def test_every_public_domain_record_emits_json_schema() -> None:
    schemas = domain_json_schemas()

    assert set(schemas) == {record_type.__name__ for record_type in PUBLIC_DOMAIN_RECORDS}
    for record_type in PUBLIC_DOMAIN_RECORDS:
        schema = schema_for(record_type)
        assert schema["title"] == record_type.__name__
        assert schema["type"] == "object"
        assert schema.get("additionalProperties") is False

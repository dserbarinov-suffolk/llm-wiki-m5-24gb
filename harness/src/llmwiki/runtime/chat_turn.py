"""Application service for preparing a grounded chat workflow turn."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from forge.core.messages import Message, MessageMeta, MessageRole, MessageType
from forge.core.workflow import Workflow

from llmwiki.domain.chat_turn_context import build_chat_turn_context
from llmwiki.domain.chatwindow import QAPair
from llmwiki.domain.model_profile import DEFAULT_MODEL_PROFILE, ModelProfile
from llmwiki.store import WikiStore
from llmwiki.workflows import build_chat_workflow


@dataclass(frozen=True)
class PreparedChatTurn:
    workflow: Workflow
    message: str
    initial_messages: tuple[Message, ...]


def prepare_chat_turn(
    store: WikiStore,
    *,
    question: str,
    window: Sequence[QAPair],
    grounded: bool,
    model_profile: ModelProfile = DEFAULT_MODEL_PROFILE,
) -> PreparedChatTurn:
    pages = store.page_texts()
    chat_context = build_chat_turn_context(
        question,
        page_texts=pages,
        index_text=store.read_index(),
        grounded=grounded,
        has_window=bool(window),
        model_profile=model_profile,
    )
    workflow = build_chat_workflow(
        store,
        allow_index_response=chat_context.allow_index_response,
        require_wiki_read=chat_context.require_wiki_read,
        evidence_scope=chat_context.evidence_scope,
        task_evidence_pack=chat_context.task_evidence_pack,
        require_procedure_execution=chat_context.require_procedure_execution,
    )
    message = chat_context.render_user_message(question + " /no_think")
    return PreparedChatTurn(
        workflow=workflow,
        message=message,
        initial_messages=_initial_messages(workflow, store.read_schema(), window, message),
    )


def _initial_messages(
    workflow: Workflow,
    schema: str,
    window: Sequence[QAPair],
    message: str,
) -> tuple[Message, ...]:
    rendered = workflow.build_system_prompt(schema=schema)
    seed = [Message(MessageRole.SYSTEM, rendered, MessageMeta(MessageType.SYSTEM_PROMPT))]
    for pair in window:
        seed.append(Message(MessageRole.USER, pair.question, MessageMeta(MessageType.USER_INPUT)))
        seed.append(
            Message(MessageRole.ASSISTANT, pair.answer, MessageMeta(MessageType.TEXT_RESPONSE))
        )
    seed.append(Message(MessageRole.USER, message, MessageMeta(MessageType.USER_INPUT)))
    return tuple(seed)

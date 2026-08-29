from __future__ import annotations

from enum import StrEnum


class WorkflowState(StrEnum):
    INTENT = "intent"
    INITIAL_DRAFT = "initial_draft"
    DOMAIN_AUDIT = "domain_audit"
    AWAITING_HUMAN_DECISION = "awaiting_human_decision"
    REVISION = "revision"
    REGRESSION_AUDIT = "regression_audit"
    COMPLETE = "complete"


class WorkflowTransitionError(ValueError):
    """Raised when a workflow gate is skipped or a state is unknown."""


ALLOWED_TRANSITIONS = frozenset(
    {
        (WorkflowState.INTENT, WorkflowState.INITIAL_DRAFT),
        (WorkflowState.INITIAL_DRAFT, WorkflowState.DOMAIN_AUDIT),
        (WorkflowState.DOMAIN_AUDIT, WorkflowState.AWAITING_HUMAN_DECISION),
        (WorkflowState.AWAITING_HUMAN_DECISION, WorkflowState.REVISION),
        (WorkflowState.REVISION, WorkflowState.REGRESSION_AUDIT),
        (WorkflowState.REGRESSION_AUDIT, WorkflowState.COMPLETE),
        (WorkflowState.DOMAIN_AUDIT, WorkflowState.INTENT),
        (WorkflowState.AWAITING_HUMAN_DECISION, WorkflowState.DOMAIN_AUDIT),
        (WorkflowState.REGRESSION_AUDIT, WorkflowState.REVISION),
        (WorkflowState.REGRESSION_AUDIT, WorkflowState.AWAITING_HUMAN_DECISION),
    }
)


def _state(value: WorkflowState | str) -> WorkflowState:
    try:
        return WorkflowState(value)
    except ValueError as exc:
        raise WorkflowTransitionError(f"unknown workflow state: {value}") from exc


def can_transition(source: WorkflowState | str, target: WorkflowState | str) -> bool:
    return (_state(source), _state(target)) in ALLOWED_TRANSITIONS


def transition(source: WorkflowState | str, target: WorkflowState | str) -> WorkflowState:
    source_state = _state(source)
    target_state = _state(target)
    if (source_state, target_state) not in ALLOWED_TRANSITIONS:
        raise WorkflowTransitionError(
            f"illegal workflow transition: {source_state} -> {target_state}"
        )
    return target_state

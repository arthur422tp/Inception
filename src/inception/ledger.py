from __future__ import annotations

from collections.abc import Mapping
from typing import NoReturn

DOMAINS = frozenset({"fiction", "presentation_text", "document_text"})
LEDGER_STATES = frozenset({
    "intent", "initial_draft", "domain_audit", "awaiting_human_decision",
    "revision", "regression_audit", "complete",
})
TOP_LEVEL_FIELDS = frozenset({
    "ledger_version", "run_id", "domain", "state", "intent_ref",
    "draft_ref", "entries",
})
ENTRY_FIELDS = frozenset({
    "id", "scope", "observed_choice", "suspected_default",
    "diagnostic_axis", "intent_relevance", "evidence", "alternatives",
    "recommendation", "human_decision", "revision", "regression",
})
SCOPE_KINDS = frozenset({"document", "section", "scene", "deck", "slide", "passage"})
ACTIONS = frozenset({"keep", "revise", "remove", "investigate"})
DECISION_STATUSES = frozenset({"pending", "accepted", "modified", "rejected", "deferred"})
REVISION_STATUSES = frozenset({"not_started", "applied", "not_applicable"})
REGRESSION_STATUSES = frozenset({"not_checked", "passed", "failed"})
SCOPE_FIELDS = frozenset({"kind", "ref"})
ALTERNATIVE_FIELDS = frozenset({"label", "effect", "tradeoffs"})
RECOMMENDATION_FIELDS = frozenset({"action", "rationale"})
HUMAN_DECISION_FIELDS = frozenset({"status", "selected_action", "notes"})
REVISION_FIELDS = frozenset({"status", "summary", "artifact_ref"})
REGRESSION_FIELDS = frozenset({"status", "checks"})


class LedgerValidationError(ValueError):
    """Raised when a Decision Ledger violates its persisted contract."""


def _fail(path: str, message: str) -> NoReturn:
    raise LedgerValidationError(f"{path}: {message}")


def _require_fields(value: Mapping[str, object], fields: frozenset[str], path: str) -> None:
    missing = sorted(fields - value.keys())
    if missing:
        _fail(path, f"missing required field(s): {', '.join(missing)}")


def _require_mapping(value: object, path: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        _fail(path, "must be an object")
    return value


def _require_string(value: object, path: str) -> None:
    if not isinstance(value, str):
        _fail(path, "must be a string")


def _require_nonblank_string(value: object, path: str) -> None:
    _require_string(value, path)
    if not value.strip():
        _fail(path, "must not be blank")


def _require_strings(
    value: object,
    path: str,
    *,
    nonempty: bool = False,
    nonblank: bool = False,
) -> list[object]:
    if not isinstance(value, list):
        _fail(path, "must be a list")
    if nonempty and not value:
        _fail(path, "must contain at least one item")
    for index, item in enumerate(value):
        item_path = f"{path}[{index}]"
        if nonblank:
            _require_nonblank_string(item, item_path)
        else:
            _require_string(item, item_path)
    return value


def _require_member(value: object, choices: frozenset[str], path: str) -> None:
    _require_string(value, path)
    if value not in choices:
        _fail(path, f"must be one of {sorted(choices)}")


def _validate_entry(entry: Mapping[str, object], path: str) -> None:
    _require_fields(entry, ENTRY_FIELDS, path)
    for field in ("id", "observed_choice", "suspected_default", "diagnostic_axis", "intent_relevance"):
        _require_nonblank_string(entry[field], f"{path}.{field}")

    scope = _require_mapping(entry["scope"], f"{path}.scope")
    _require_fields(scope, SCOPE_FIELDS, f"{path}.scope")
    _require_member(scope["kind"], SCOPE_KINDS, f"{path}.scope.kind")
    _require_nonblank_string(scope["ref"], f"{path}.scope.ref")

    _require_strings(entry["evidence"], f"{path}.evidence", nonempty=True, nonblank=True)

    alternatives = entry["alternatives"]
    if not isinstance(alternatives, list):
        _fail(f"{path}.alternatives", "must be a list")
    if not alternatives:
        _fail(f"{path}.alternatives", "must contain at least one item")
    for index, alternative_value in enumerate(alternatives):
        alternative_path = f"{path}.alternatives[{index}]"
        alternative = _require_mapping(alternative_value, alternative_path)
        _require_fields(alternative, ALTERNATIVE_FIELDS, alternative_path)
        _require_nonblank_string(alternative["label"], f"{alternative_path}.label")
        _require_nonblank_string(alternative["effect"], f"{alternative_path}.effect")
        _require_strings(
            alternative["tradeoffs"], f"{alternative_path}.tradeoffs", nonblank=True
        )

    recommendation = _require_mapping(entry["recommendation"], f"{path}.recommendation")
    _require_fields(recommendation, RECOMMENDATION_FIELDS, f"{path}.recommendation")
    _require_member(recommendation["action"], ACTIONS, f"{path}.recommendation.action")
    _require_nonblank_string(recommendation["rationale"], f"{path}.recommendation.rationale")

    human_decision = _require_mapping(entry["human_decision"], f"{path}.human_decision")
    _require_fields(human_decision, HUMAN_DECISION_FIELDS, f"{path}.human_decision")
    _require_member(human_decision["status"], DECISION_STATUSES, f"{path}.human_decision.status")
    selected_action = human_decision["selected_action"]
    if selected_action is not None:
        _require_member(selected_action, ACTIONS, f"{path}.human_decision.selected_action")
    _require_string(human_decision["notes"], f"{path}.human_decision.notes")
    if human_decision["status"] in {"pending", "rejected", "deferred"} and selected_action is not None:
        _fail(f"{path}.human_decision.selected_action", "must be null unless the decision is accepted or modified")
    if human_decision["status"] in {"accepted", "modified"} and selected_action is None:
        _fail(f"{path}.human_decision.selected_action", "must select an action when the decision is accepted or modified")
    if human_decision["status"] == "accepted" and selected_action != recommendation["action"]:
        _fail(f"{path}.human_decision.selected_action", "must match the recommendation for an accepted decision")

    revision = _require_mapping(entry["revision"], f"{path}.revision")
    _require_fields(revision, REVISION_FIELDS, f"{path}.revision")
    _require_member(revision["status"], REVISION_STATUSES, f"{path}.revision.status")
    _require_string(revision["summary"], f"{path}.revision.summary")
    _require_string(revision["artifact_ref"], f"{path}.revision.artifact_ref")

    regression = _require_mapping(entry["regression"], f"{path}.regression")
    _require_fields(regression, REGRESSION_FIELDS, f"{path}.regression")
    _require_member(regression["status"], REGRESSION_STATUSES, f"{path}.regression.status")
    _require_strings(regression["checks"], f"{path}.regression.checks", nonblank=True)

    if revision["status"] == "applied" and human_decision["status"] not in {"accepted", "modified"}:
        _fail(f"{path}.human_decision.status", "must be accepted or modified before revision is applied")
    if revision["status"] == "applied" and selected_action not in {"revise", "remove"}:
        _fail(
            f"{path}.human_decision.selected_action",
            "must be revise or remove when revision is applied",
        )
    if revision["status"] == "applied":
        _require_nonblank_string(revision["summary"], f"{path}.revision.summary")
        _require_nonblank_string(revision["artifact_ref"], f"{path}.revision.artifact_ref")
    if regression["status"] == "passed" and not regression["checks"]:
        _fail(f"{path}.regression.checks", "must contain at least one check when regression passed")
    if regression["status"] == "passed" and revision["status"] != "applied":
        _fail(f"{path}.revision.status", "must be applied before regression can pass")


def _validate_complete(entries: list[object]) -> None:
    for index, entry_value in enumerate(entries):
        path = f"ledger.entries[{index}]"
        entry = _require_mapping(entry_value, path)
        human_decision = _require_mapping(entry["human_decision"], f"{path}.human_decision")
        revision = _require_mapping(entry["revision"], f"{path}.revision")
        regression = _require_mapping(entry["regression"], f"{path}.regression")

        if human_decision["status"] == "pending":
            _fail(f"{path}.human_decision.status", "must not be pending when ledger is complete")

        selected_action = human_decision["selected_action"]
        if human_decision["status"] in {"accepted", "modified"} and selected_action in {"revise", "remove"}:
            if revision["status"] != "applied":
                _fail(f"{path}.revision.status", "must be applied when ledger is complete")
            if regression["status"] != "passed":
                _fail(f"{path}.regression.status", "must be passed when ledger is complete")


def validate_ledger(payload: Mapping[str, object]) -> None:
    _require_fields(payload, TOP_LEVEL_FIELDS, "ledger")
    if not isinstance(payload["ledger_version"], int) or isinstance(payload["ledger_version"], bool) or payload["ledger_version"] != 1:
        _fail("ledger.ledger_version", "must equal 1")
    _require_member(payload["domain"], DOMAINS, "ledger.domain")
    _require_member(payload["state"], LEDGER_STATES, "ledger.state")
    for field in ("run_id", "intent_ref", "draft_ref"):
        _require_nonblank_string(payload[field], f"ledger.{field}")
    entries = payload["entries"]
    if not isinstance(entries, list):
        _fail("ledger.entries", "must be a list")
    for index, entry in enumerate(entries):
        _validate_entry(_require_mapping(entry, f"ledger.entries[{index}]"), f"ledger.entries[{index}]")
    if payload["state"] == "complete":
        _validate_complete(entries)

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inception.ledger import LedgerValidationError, validate_ledger


def valid_payload() -> dict[str, object]:
    return {
        "ledger_version": 1,
        "run_id": "run-001",
        "domain": "fiction",
        "state": "awaiting_human_decision",
        "intent_ref": "intent-001",
        "draft_ref": "draft-001",
        "entries": [{
            "id": "D001",
            "scope": {"kind": "scene", "ref": "scene-4"},
            "observed_choice": "The conflict resolves through sudden forgiveness.",
            "suspected_default": "Tidy reconciliation closes the conflict immediately.",
            "diagnostic_axis": "closure_and_resolution",
            "intent_relevance": "The intent calls for unresolved moral tension.",
            "evidence": ["Scene 4, final two paragraphs"],
            "alternatives": [{
                "label": "Keep the disagreement unresolved",
                "effect": "Preserves moral tension into the ending.",
                "tradeoffs": ["Less immediate emotional closure"],
            }],
            "recommendation": {
                "action": "revise",
                "rationale": "The current closure contradicts the desired effect.",
            },
            "human_decision": {
                "status": "pending", "selected_action": None, "notes": ""
            },
            "revision": {
                "status": "not_started", "summary": "", "artifact_ref": ""
            },
            "regression": {"status": "not_checked", "checks": []},
        }],
    }


class LedgerValidationTests(unittest.TestCase):
    def test_accepts_valid_pending_ledger(self) -> None:
        validate_ledger(valid_payload())

    def test_accepts_document_text_domain(self) -> None:
        payload = valid_payload()
        payload["domain"] = "document_text"

        validate_ledger(payload)

    def test_requires_every_top_level_field(self) -> None:
        fields = (
            "ledger_version", "run_id", "domain", "state",
            "intent_ref", "draft_ref", "entries",
        )
        for field in fields:
            with self.subTest(field=field):
                payload = copy.deepcopy(valid_payload())
                del payload[field]
                with self.assertRaisesRegex(LedgerValidationError, field):
                    validate_ledger(payload)

    def test_entry_requires_every_field(self) -> None:
        fields = (
            "id", "scope", "observed_choice", "suspected_default",
            "diagnostic_axis", "intent_relevance", "evidence", "alternatives",
            "recommendation", "human_decision", "revision", "regression",
        )
        for field in fields:
            with self.subTest(field=field):
                payload = copy.deepcopy(valid_payload())
                del payload["entries"][0][field]  # type: ignore[index]
                with self.assertRaisesRegex(LedgerValidationError, field):
                    validate_ledger(payload)

    def test_entry_rejects_wrong_nested_types(self) -> None:
        replacements = {
            "scope": [],
            "evidence": "Scene 4",
            "alternatives": {},
            "recommendation": [],
            "human_decision": [],
            "revision": [],
            "regression": [],
        }
        for field, replacement in replacements.items():
            with self.subTest(field=field):
                payload = copy.deepcopy(valid_payload())
                payload["entries"][0][field] = replacement  # type: ignore[index]
                with self.assertRaisesRegex(LedgerValidationError, field):
                    validate_ledger(payload)

    def test_rejects_invalid_enum_values(self) -> None:
        cases = (
            ("scope", {"kind": "chapter", "ref": "scene-4"}, "scope.kind"),
            ("recommendation", {"action": "rewrite", "rationale": "Reason"}, "recommendation.action"),
            ("human_decision", {"status": "approved", "selected_action": None, "notes": ""}, "human_decision.status"),
            ("revision", {"status": "done", "summary": "", "artifact_ref": ""}, "revision.status"),
            ("regression", {"status": "clear", "checks": []}, "regression.status"),
        )
        for field, replacement, path in cases:
            with self.subTest(field=field):
                payload = copy.deepcopy(valid_payload())
                payload["entries"][0][field] = replacement  # type: ignore[index]
                with self.assertRaisesRegex(LedgerValidationError, path):
                    validate_ledger(payload)

    def test_rejects_invalid_selected_action(self) -> None:
        payload = valid_payload()
        payload["entries"][0]["human_decision"] = {  # type: ignore[index]
            "status": "modified", "selected_action": "rewrite", "notes": "Use a variant."
        }
        with self.assertRaisesRegex(LedgerValidationError, "selected_action"):
            validate_ledger(payload)

    def test_rejects_wrong_scalar_and_list_item_types(self) -> None:
        cases = (
            ("run_id", 1, "ledger.run_id"),
            ("id", 1, "id"),
            ("evidence", [1], r"evidence\[0\]"),
            ("alternatives", [{"label": "Option", "effect": "Effect", "tradeoffs": [1]}], r"tradeoffs\[0\]"),
            ("regression", {"status": "not_checked", "checks": [1]}, r"checks\[0\]"),
        )
        for field, replacement, path in cases:
            with self.subTest(field=field):
                payload = copy.deepcopy(valid_payload())
                if field == "run_id":
                    payload[field] = replacement
                else:
                    payload["entries"][0][field] = replacement  # type: ignore[index]
                with self.assertRaisesRegex(LedgerValidationError, path):
                    validate_ledger(payload)

    def test_rejects_non_string_enum_values_and_boolean_ledger_version(self) -> None:
        payload = valid_payload()
        payload["ledger_version"] = True
        with self.assertRaisesRegex(LedgerValidationError, "ledger_version"):
            validate_ledger(payload)

        payload = valid_payload()
        payload["ledger_version"] = 1.0
        with self.assertRaisesRegex(LedgerValidationError, "ledger_version"):
            validate_ledger(payload)

        payload = valid_payload()
        payload["entries"][0]["scope"]["kind"] = []  # type: ignore[index]
        with self.assertRaisesRegex(LedgerValidationError, "scope.kind"):
            validate_ledger(payload)

    def test_rejects_unhashable_top_level_enum_values(self) -> None:
        for field in ("domain", "state"):
            for value in ([], {}):
                with self.subTest(field=field, value_type=type(value).__name__):
                    payload = valid_payload()
                    payload[field] = value
                    with self.assertRaisesRegex(LedgerValidationError, f"ledger.{field}"):
                        validate_ledger(payload)

    def test_pending_human_decision_cannot_select_an_action(self) -> None:
        payload = valid_payload()
        payload["entries"][0]["human_decision"]["selected_action"] = "revise"  # type: ignore[index]
        with self.assertRaisesRegex(LedgerValidationError, "selected_action"):
            validate_ledger(payload)

    def test_accepted_human_decision_selects_the_recommendation(self) -> None:
        payload = valid_payload()
        payload["entries"][0]["human_decision"] = {  # type: ignore[index]
            "status": "accepted", "selected_action": "keep", "notes": "Approved"
        }
        with self.assertRaisesRegex(LedgerValidationError, "selected_action"):
            validate_ledger(payload)

    def test_entry_requires_observable_evidence(self) -> None:
        payload = valid_payload()
        payload["entries"][0]["evidence"] = []  # type: ignore[index]
        with self.assertRaisesRegex(LedgerValidationError, "evidence"):
            validate_ledger(payload)

    def test_applied_revision_requires_a_human_acceptance(self) -> None:
        payload = valid_payload()
        payload["entries"][0]["revision"]["status"] = "applied"  # type: ignore[index]
        with self.assertRaisesRegex(LedgerValidationError, "human_decision.status"):
            validate_ledger(payload)

    def test_passed_regression_requires_checks(self) -> None:
        payload = valid_payload()
        entry = payload["entries"][0]  # type: ignore[index]
        entry["human_decision"] = {
            "status": "accepted", "selected_action": "revise", "notes": "Approved"
        }
        entry["revision"] = {
            "status": "applied", "summary": "Changed ending", "artifact_ref": "draft-002"
        }
        entry["regression"] = {"status": "passed", "checks": []}
        with self.assertRaisesRegex(LedgerValidationError, "regression.checks"):
            validate_ledger(payload)

    def test_complete_rejects_pending_or_unfinished_mutating_entries(self) -> None:
        payload = valid_payload()
        payload["state"] = "complete"
        with self.assertRaisesRegex(LedgerValidationError, "human_decision.status"):
            validate_ledger(payload)

        payload = valid_payload()
        payload["state"] = "complete"
        payload["entries"][0]["human_decision"] = {  # type: ignore[index]
            "status": "accepted", "selected_action": "revise", "notes": "Approved"
        }
        with self.assertRaisesRegex(LedgerValidationError, "revision.status"):
            validate_ledger(payload)

    def test_passed_regression_requires_applied_revision(self) -> None:
        payload = valid_payload()
        payload["entries"][0]["regression"] = {  # type: ignore[index]
            "status": "passed", "checks": ["intent.must_preserve"]
        }
        with self.assertRaisesRegex(LedgerValidationError, "revision.status"):
            validate_ledger(payload)

    def test_applied_revision_requires_a_mutating_selected_action(self) -> None:
        for action in ("keep", "investigate"):
            with self.subTest(action=action):
                payload = valid_payload()
                entry = payload["entries"][0]  # type: ignore[index]
                entry["recommendation"]["action"] = action
                entry["human_decision"] = {
                    "status": "accepted", "selected_action": action, "notes": "Approved"
                }
                entry["revision"] = {
                    "status": "applied", "summary": "Changed draft", "artifact_ref": "draft-002"
                }
                with self.assertRaisesRegex(LedgerValidationError, "selected_action"):
                    validate_ledger(payload)

    def test_entry_requires_at_least_one_alternative(self) -> None:
        payload = valid_payload()
        payload["entries"][0]["alternatives"] = []  # type: ignore[index]
        with self.assertRaisesRegex(LedgerValidationError, "alternatives"):
            validate_ledger(payload)

    def test_evidence_and_completed_records_require_nonblank_strings(self) -> None:
        payload = valid_payload()
        payload["entries"][0]["evidence"] = ["   "]  # type: ignore[index]
        with self.assertRaisesRegex(LedgerValidationError, r"evidence\[0\]"):
            validate_ledger(payload)

        for field in ("summary", "artifact_ref"):
            with self.subTest(field=field):
                payload = valid_payload()
                entry = payload["entries"][0]  # type: ignore[index]
                entry["human_decision"] = {
                    "status": "accepted", "selected_action": "revise", "notes": "Approved"
                }
                entry["revision"] = {
                    "status": "applied", "summary": "Changed ending", "artifact_ref": "draft-002"
                }
                entry["revision"][field] = ""
                with self.assertRaisesRegex(LedgerValidationError, f"revision.{field}"):
                    validate_ledger(payload)

        payload = valid_payload()
        entry = payload["entries"][0]  # type: ignore[index]
        entry["human_decision"] = {
            "status": "accepted", "selected_action": "revise", "notes": "Approved"
        }
        entry["revision"] = {
            "status": "applied", "summary": "Changed ending", "artifact_ref": "draft-002"
        }
        entry["regression"] = {"status": "passed", "checks": [""]}
        with self.assertRaisesRegex(LedgerValidationError, r"regression.checks\[0\]"):
            validate_ledger(payload)

    def test_accepts_complete_applied_revision_and_nonmutating_decision(self) -> None:
        payload = valid_payload()
        payload["state"] = "complete"
        entry = payload["entries"][0]  # type: ignore[index]
        entry["human_decision"] = {
            "status": "accepted", "selected_action": "revise", "notes": "Approved"
        }
        entry["revision"] = {
            "status": "applied", "summary": "Changed ending", "artifact_ref": "draft-002"
        }
        entry["regression"] = {"status": "passed", "checks": ["intent.must_preserve"]}
        validate_ledger(payload)

        payload = valid_payload()
        payload["state"] = "complete"
        entry = payload["entries"][0]  # type: ignore[index]
        entry["recommendation"]["action"] = "keep"
        entry["human_decision"] = {
            "status": "accepted", "selected_action": "keep", "notes": "Keep as written"
        }
        entry["revision"] = {
            "status": "not_applicable", "summary": "", "artifact_ref": ""
        }
        validate_ledger(payload)

    def test_allows_empty_findings(self) -> None:
        payload = valid_payload()
        payload["entries"] = []
        validate_ledger(payload)

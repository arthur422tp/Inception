from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inception.workflow import (
    WorkflowState,
    WorkflowTransitionError,
    can_transition,
    transition,
)


class WorkflowTests(unittest.TestCase):
    def test_happy_path_reaches_complete(self) -> None:
        states = [
            WorkflowState.INTENT,
            WorkflowState.INITIAL_DRAFT,
            WorkflowState.DOMAIN_AUDIT,
            WorkflowState.AWAITING_HUMAN_DECISION,
            WorkflowState.REVISION,
            WorkflowState.REGRESSION_AUDIT,
            WorkflowState.COMPLETE,
        ]
        for source, target in zip(states, states[1:]):
            with self.subTest(source=source, target=target):
                self.assertEqual(transition(source, target), target)

    def test_rejects_revision_before_human_decision(self) -> None:
        self.assertFalse(can_transition("domain_audit", "revision"))
        with self.assertRaisesRegex(WorkflowTransitionError, "domain_audit -> revision"):
            transition("domain_audit", "revision")

    def test_allows_documented_recovery_transitions(self) -> None:
        recoveries = {
            ("domain_audit", "intent"),
            ("awaiting_human_decision", "domain_audit"),
            ("regression_audit", "revision"),
            ("regression_audit", "awaiting_human_decision"),
        }
        for source, target in recoveries:
            with self.subTest(source=source, target=target):
                self.assertTrue(can_transition(source, target))

    def test_rejects_unknown_state(self) -> None:
        with self.assertRaisesRegex(WorkflowTransitionError, "unknown workflow state"):
            transition("unknown", "intent")

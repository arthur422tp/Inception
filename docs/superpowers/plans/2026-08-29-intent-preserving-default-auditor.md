# Intent-Preserving Default Auditor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a project-local Codex skill with fiction and presentation-text adapters, backed by a deterministic Decision Ledger validator and gated workflow state machine.

**Architecture:** One discoverable skill owns the human-facing workflow and progressively loads one domain adapter. A dependency-free Python package validates ledger invariants and state transitions; a thin script inside the skill exposes the validator. Prompt files receive structural validation and representative smoke checks, while executable Python behavior uses test-driven development.

**Tech Stack:** Python 3.11+, standard library (`enum`, `json`, `pathlib`, `unittest`), Codex skill Markdown, generated YAML interface metadata.

**Spec:** `docs/superpowers/specs/2026-08-29-intent-preserving-default-auditor-design.md`

## Global Constraints

- Diagnose intent-relative content decisions; do not classify AI authorship.
- Do not use vocabulary blacklists or cosmetic “humanization.”
- Presentation audits must not advise on typography, color, spacing, grid, alignment, visual hierarchy, icons, illustrations, slide masters, or visual style.
- Require an explicit human decision before material revision.
- Treat StoryScope findings as hypotheses, not universal quality rules.
- Skill/prompt text does not use RED/GREEN prompt TDD, per the user's explicit direction; use structural validation and smoke checks.
- Python state and validation behavior uses RED/GREEN/REFACTOR.
- Add no runtime dependency beyond Python 3.11's standard library.

---

## File Map

| Path | Responsibility |
|---|---|
| `src/inception/__init__.py` | Public package exports |
| `src/inception/ledger.py` | Ledger schema and cross-field invariants |
| `src/inception/workflow.py` | Workflow states and legal transitions |
| `src/inception/cli.py` | JSON file validation entry point |
| `skills/intent-preserving-default-auditor/SKILL.md` | Trigger and orchestration contract |
| `skills/intent-preserving-default-auditor/agents/openai.yaml` | Generated Codex UI metadata |
| `skills/intent-preserving-default-auditor/references/core-workflow.md` | Intent Contract, ledger fields, gates, and errors |
| `skills/intent-preserving-default-auditor/references/fiction-adapter.md` | Fiction diagnostic axes |
| `skills/intent-preserving-default-auditor/references/presentation-text-adapter.md` | Deck, slide, and content axes |
| `skills/intent-preserving-default-auditor/scripts/validate_ledger.py` | Executable validator wrapper |
| `tests/test_ledger.py` | Ledger invariant tests |
| `tests/test_workflow.py` | Transition tests |
| `tests/test_cli.py` | File/command tests |
| `tests/fixtures/*.json` | Valid and invalid end-to-end examples |
| `tests/skill-smoke/scenarios.md` | Prompt smoke scenarios and expected properties |
| `README.md` | Discovery, validation, and usage handoff |

---

### Task 1: Decision Ledger Contract

**Files:**
- Create: `src/inception/__init__.py`
- Create: `src/inception/ledger.py`
- Create: `tests/test_ledger.py`

**Interfaces:**
- Consumes: JSON-compatible `Mapping[str, object]` payloads.
- Produces: `validate_ledger(payload: Mapping[str, object]) -> None`, `LedgerValidationError`, and accepted-value constants.

- [ ] **Step 1: Write the first failing tests**

Create `tests/test_ledger.py` with:

```python
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
```

- [ ] **Step 2: Verify RED**

Run `.venv/bin/python -m unittest tests.test_ledger -v`.

Expected: import failure because `inception.ledger` does not exist.

- [ ] **Step 3: Add top-level validation**

Create `src/inception/ledger.py` with:

```python
from __future__ import annotations

from collections.abc import Mapping
from typing import NoReturn

DOMAINS = frozenset({"fiction", "presentation_text"})
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


class LedgerValidationError(ValueError):
    """Raised when a Decision Ledger violates its persisted contract."""


def _fail(path: str, message: str) -> NoReturn:
    raise LedgerValidationError(f"{path}: {message}")


def _require_fields(value: Mapping[str, object], fields: frozenset[str], path: str) -> None:
    missing = sorted(fields - value.keys())
    if missing:
        _fail(path, f"missing required field(s): {', '.join(missing)}")


def validate_ledger(payload: Mapping[str, object]) -> None:
    _require_fields(payload, TOP_LEVEL_FIELDS, "ledger")
    if payload["ledger_version"] != 1:
        _fail("ledger.ledger_version", "must equal 1")
    if payload["domain"] not in DOMAINS:
        _fail("ledger.domain", f"must be one of {sorted(DOMAINS)}")
    if payload["state"] not in LEDGER_STATES:
        _fail("ledger.state", f"must be one of {sorted(LEDGER_STATES)}")
    entries = payload["entries"]
    if not isinstance(entries, list):
        _fail("ledger.entries", "must be a list")
    for index, entry in enumerate(entries):
        if not isinstance(entry, Mapping):
            _fail(f"ledger.entries[{index}]", "must be an object")
        _require_fields(entry, ENTRY_FIELDS, f"ledger.entries[{index}]")
```

Create `src/inception/__init__.py` exporting `LedgerValidationError` and `validate_ledger`.

- [ ] **Step 4: Verify GREEN**

Run `.venv/bin/python -m unittest tests.test_ledger -v`; expect both tests to pass.

- [ ] **Step 5: Add failing cross-field tests**

Append tests proving:

```python
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

    def test_allows_empty_findings(self) -> None:
        payload = valid_payload()
        payload["entries"] = []
        validate_ledger(payload)
```

- [ ] **Step 6: Verify RED, then implement nested validation**

Run the tests and confirm the three new invariant tests fail. Add nested-object checks using:

```python
SCOPE_KINDS = frozenset({"document", "section", "scene", "deck", "slide", "passage"})
ACTIONS = frozenset({"keep", "revise", "remove", "investigate"})
DECISION_STATUSES = frozenset({"pending", "accepted", "modified", "rejected", "deferred"})
REVISION_STATUSES = frozenset({"not_started", "applied", "not_applicable"})
REGRESSION_STATUSES = frozenset({"not_checked", "passed", "failed"})
```

Enforce these branches exactly:

```python
if revision["status"] == "applied" and human_decision["status"] not in {"accepted", "modified"}:
    _fail(f"{path}.human_decision.status", "must be accepted or modified before revision is applied")
if regression["status"] == "passed" and not regression["checks"]:
    _fail(f"{path}.regression.checks", "must contain at least one check when regression passed")
```

- [ ] **Step 7: Verify GREEN and commit**

Run `.venv/bin/python -m unittest tests.test_ledger -v`; expect all tests to pass.

```bash
git add src/inception/__init__.py src/inception/ledger.py tests/test_ledger.py
git commit -m "feat: validate decision ledgers"
```

---

### Task 2: Gated Workflow State Machine

**Files:**
- Create: `src/inception/workflow.py`
- Modify: `src/inception/__init__.py`
- Create: `tests/test_workflow.py`

**Interfaces:**
- Consumes: `WorkflowState | str` source and target.
- Produces: `WorkflowState`, `WorkflowTransitionError`, `can_transition(...) -> bool`, and `transition(...) -> WorkflowState`.

- [ ] **Step 1: Write failing transition tests**

Create `tests/test_workflow.py`:

```python
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inception.workflow import WorkflowState, WorkflowTransitionError, can_transition, transition


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
            self.assertTrue(can_transition(source, target))
```

- [ ] **Step 2: Verify RED**

Run `.venv/bin/python -m unittest tests.test_workflow -v`.

Expected: import failure because `inception.workflow` does not exist.

- [ ] **Step 3: Implement the state machine**

Create `src/inception/workflow.py`:

```python
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


ALLOWED_TRANSITIONS = frozenset({
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
})


def _state(value: WorkflowState | str) -> WorkflowState:
    try:
        return WorkflowState(value)
    except ValueError as exc:
        raise WorkflowTransitionError(f"unknown workflow state: {value}") from exc


def can_transition(source: WorkflowState | str, target: WorkflowState | str) -> bool:
    return (_state(source), _state(target)) in ALLOWED_TRANSITIONS


def transition(source: WorkflowState | str, target: WorkflowState | str) -> WorkflowState:
    source_state, target_state = _state(source), _state(target)
    if (source_state, target_state) not in ALLOWED_TRANSITIONS:
        raise WorkflowTransitionError(f"illegal workflow transition: {source_state} -> {target_state}")
    return target_state
```

Export the four public names from `src/inception/__init__.py`.

- [ ] **Step 4: Verify GREEN and commit**

Run `.venv/bin/python -m unittest tests.test_workflow tests.test_ledger -v`; expect all tests to pass.

```bash
git add src/inception/__init__.py src/inception/workflow.py tests/test_workflow.py
git commit -m "feat: gate default-audit workflow states"
```

---

### Task 3: Ledger Validation Command

**Files:**
- Create: `src/inception/cli.py`
- Create: `skills/intent-preserving-default-auditor/scripts/validate_ledger.py`
- Create: `tests/test_cli.py`
- Create: `tests/fixtures/valid-ledger.json`
- Create: `tests/fixtures/invalid-skipped-decision.json`

**Interfaces:**
- Consumes: path to a UTF-8 JSON ledger.
- Produces: `main(argv: list[str] | None = None) -> int`; exit `0` for valid, `1` for ledger violations, `2` for unreadable/malformed input.

- [ ] **Step 1: Initialize the skill directory before adding its wrapper**

Read `/Users/arthuryu/.codex/skills/.system/skill-creator/references/openai_yaml.md`, then run:

```bash
python3 /Users/arthuryu/.codex/skills/.system/skill-creator/scripts/init_skill.py intent-preserving-default-auditor \
  --path skills \
  --resources scripts,references \
  --interface 'display_name=Intent-Preserving Default Auditor' \
  --interface 'short_description=Audit content defaults against author intent' \
  --interface 'default_prompt=Audit this fiction or presentation text for intent-breaking default choices, record evidence in a Decision Ledger, and wait for my decisions before revising.'
```

Expected: the initializer creates `SKILL.md`, `agents/openai.yaml`, `scripts/`, and `references/`. Do not edit the generated prompt files during this task.

- [ ] **Step 2: Add fixtures and failing CLI tests**

Create a valid fixture from Task 1 with an accepted decision, applied revision, and passed regression containing `intent.must_preserve` and `scene-4 dependency` checks. Create the invalid fixture with a pending decision and applied revision.

Create `tests/test_cli.py`:

```python
from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from inception.cli import main

FIXTURES = Path(__file__).parent / "fixtures"


class CliTests(unittest.TestCase):
    def test_valid_file_returns_zero(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = main([str(FIXTURES / "valid-ledger.json")])
        self.assertEqual(result, 0)
        self.assertIn("valid:", output.getvalue())

    def test_invalid_ledger_returns_one(self) -> None:
        error = io.StringIO()
        with contextlib.redirect_stderr(error):
            result = main([str(FIXTURES / "invalid-skipped-decision.json")])
        self.assertEqual(result, 1)
        self.assertIn("human_decision.status", error.getvalue())

    def test_malformed_json_returns_two(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.json"
            path.write_text("{", encoding="utf-8")
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main([str(path)]), 2)
```

- [ ] **Step 3: Verify RED**

Run `.venv/bin/python -m unittest tests.test_cli -v`.

Expected: import failure because `inception.cli` does not exist.

- [ ] **Step 4: Implement command and wrapper**

Create `src/inception/cli.py` using `argparse`, `json.loads`, and `validate_ledger`. Catch `OSError` and `json.JSONDecodeError` as exit `2`; catch `LedgerValidationError` as exit `1`; print `valid: <path>` and return `0` otherwise.

Create `skills/intent-preserving-default-auditor/scripts/validate_ledger.py`:

```python
#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPOSITORY_ROOT / "src"))

from inception.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 5: Verify GREEN and commit**

Run:

```bash
.venv/bin/python -m unittest tests.test_cli tests.test_ledger tests.test_workflow -v
.venv/bin/python skills/intent-preserving-default-auditor/scripts/validate_ledger.py tests/fixtures/valid-ledger.json
```

Expect all tests to pass and the wrapper to print `valid: tests/fixtures/valid-ledger.json`.

```bash
git add src/inception/cli.py skills/intent-preserving-default-auditor/scripts/validate_ledger.py tests/test_cli.py tests/fixtures
git commit -m "feat: add decision ledger validation command"
```

---

### Task 4: Skill Core and Domain Adapters

**Files:**
- Create: `skills/intent-preserving-default-auditor/SKILL.md`
- Create: `skills/intent-preserving-default-auditor/agents/openai.yaml`
- Create: `skills/intent-preserving-default-auditor/references/core-workflow.md`
- Create: `skills/intent-preserving-default-auditor/references/fiction-adapter.md`
- Create: `skills/intent-preserving-default-auditor/references/presentation-text-adapter.md`
- Create: `tests/skill-smoke/scenarios.md`

**Interfaces:**
- Consumes: user intent and a fiction/presentation draft, or a request for an initial draft.
- Produces: Intent Contract, evidence-backed ledger, human-decision pause, bounded revision, and regression report.

- [ ] **Step 1: Replace the generated `SKILL.md`**

Use exactly this frontmatter:

```yaml
---
name: intent-preserving-default-auditor
description: Use when creating, auditing, or revising fiction or presentation text where generic structure, tidy closure, unsupported claims, repeated content, template dependence, or other model-default choices may conflict with the author's intent.
---
```

Body order:

1. Core principle: defaults are candidates, not defects; intent outranks rarity.
2. Required workflow: read core reference, establish intent, obtain/create draft, load one adapter, audit, present ledger, stop for decisions, revise selected entries, regress.
3. Adapter routing: fiction vs presentation text; stop for unsupported domains.
4. Output contract: bounded evidence-backed findings, empty ledger allowed, persisted JSON validated by the script.
5. Hard boundaries: no AI detection, word blacklist, material auto-revision, or visual advice.

Keep the file below 500 words and use imperative instructions.

- [ ] **Step 2: Write `core-workflow.md`**

Include the exact seven states, four recovery transitions, Intent Contract fields, full ledger field contract, the forbidden `domain_audit → revision` transition, and all error cases from the spec. Include one compact valid JSON ledger. For long artifacts, require coherent audit units, one ledger, and stable entry IDs.

- [ ] **Step 3: Write `fiction-adapter.md`**

Use this recipe for every candidate:

```text
Observed choice → draft evidence → suspected default → intent relationship
→ keep/revise alternative → trade-off → recommendation
```

Cover the ten spec axes. Pair each diagnostic question with a counterexample where the common choice intentionally serves the story. State that StoryScope supplies population-level hypotheses, not thresholds or prohibitions.

- [ ] **Step 4: Write `presentation-text-adapter.md`**

Cover deck, slide, and content levels. Require this semantic record:

```yaml
slide_id: S06
role: mechanism
claim: SQL generation is separated from deterministic validation.
support:
  - read-only guard
  - approved schema validation
depends_on:
  - S05_query_planning
enables:
  - S07_failure_handling
```

Audit rhetorical role, claim specificity, evidence alignment, redundancy, argument progression, heading function, and template dependence. State that `visual_form` is not an audit field and visual-design recommendations never belong in the ledger.

- [ ] **Step 5: Add non-TDD smoke scenarios**

Create `tests/skill-smoke/scenarios.md` with six prompts and expected properties:

1. Conventional fiction closure serves a comfort-story intent → keep it.
2. Tidy forgiveness contradicts unresolved-tension intent → create an evidence-backed candidate.
3. Presentation has duplicate claims and no support → identify redundancy/evidence gaps.
4. Topic heading is deliberately appropriate → do not force an assertion heading.
5. User demands immediate rewrite → present ledger and pause.
6. Clean draft → allow empty ledger.

For each, inspect intent-relative reasoning, cited evidence, no default-as-defect language, no visual advice, and no revision before disposition. These are smoke checks, not prompt TDD.

- [ ] **Step 6: Validate structure and inspect smoke scenarios**

Run:

```bash
python3 /Users/arthuryu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/intent-preserving-default-auditor
wc -w skills/intent-preserving-default-auditor/SKILL.md
rg -n "font|typography|color|spacing|grid|alignment|visual hierarchy|icon|illustration|slide master|visual_form" skills/intent-preserving-default-auditor
```

Expect structural validation success, fewer than 500 words in `SKILL.md`, and visual terms only in explicit exclusion statements. Manually inspect all six smoke scenarios.

- [ ] **Step 7: Commit**

```bash
git add skills/intent-preserving-default-auditor tests/skill-smoke/scenarios.md
git commit -m "feat: add intent-preserving default auditor skill"
```

---

### Task 5: Project Handoff and End-to-End Verification

**Files:**
- Modify: `README.md`
- Modify: `pyproject.toml`
- Modify: `main.py`

**Interfaces:**
- Consumes: repository checkout and a ledger JSON path.
- Produces: local usage commands and a meaningful default executable.

- [ ] **Step 1: Update metadata and entry point**

Set:

```toml
description = "Intent-preserving content audit skill with fiction and presentation-text adapters"
```

Replace `main.py` with:

```python
def main() -> None:
    print(
        "Inception provides the intent-preserving-default-auditor skill. "
        "Validate a ledger with: "
        "python skills/intent-preserving-default-auditor/scripts/validate_ledger.py <ledger.json>"
    )


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Rewrite README**

Document purpose/non-goals, seven states, project-local skill path, optional personal-skill linking/copying, ledger validation, complete unit-test command, and the two first-release adapters.

- [ ] **Step 3: Run complete verification**

```bash
.venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v
.venv/bin/python skills/intent-preserving-default-auditor/scripts/validate_ledger.py tests/fixtures/valid-ledger.json
python3 /Users/arthuryu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/intent-preserving-default-auditor
git diff --check
```

Expect all tests and validators to pass with no whitespace errors.

- [ ] **Step 4: Map final evidence to every acceptance criterion**

Check discovery metadata, shared ledger, human gate, fiction hypotheses, presentation visual boundary, supplied/generated draft paths, regression dependency checks, and clean verification output against the spec.

- [ ] **Step 5: Commit handoff**

```bash
git add README.md pyproject.toml main.py
git commit -m "docs: document default auditor workflow"
```

---

## Final Verification Gate

Run:

```bash
.venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v
.venv/bin/python skills/intent-preserving-default-auditor/scripts/validate_ledger.py tests/fixtures/valid-ledger.json
python3 /Users/arthuryu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/intent-preserving-default-auditor
git status --short
git log --oneline -6
```

Required evidence: executable tests pass, valid ledger passes, skill structure passes, all six prompt smoke scenarios are inspected without prompt TDD, the worktree is clean, and commits are independently reviewable.

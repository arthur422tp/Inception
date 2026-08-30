# Core Workflow

## Contents

- Core rule
- Inception meta-intent
- State machine
- Intent Contract
- Audit procedure
- Decision Ledger contract
- Human decision and revision gates
- Regression Audit
- Large artifacts
- Error handling
- Persistence validation

## Core Rule

Judge whether an observable content choice serves the stated intent. A familiar choice is not automatically weak, and an unusual choice is not automatically strong.

Every finding is a decision candidate. State what the draft chose, where the evidence appears, why the choice may be an easy default, and what keeping or changing it would cost.

## Inception Meta-Intent

Invoking Inception supplies a baseline meta-intent: reduce perceived model-default or AI-like convergence by auditing upstream content decisions rather than cosmetic wording. The human does not need to state this goal again.

The meta-intent is not an authorship judgment, a finding quota, or permission to revise. It does not make familiar choices defective and does not override the artifact's audience, purpose, desired effect, must-preserve content, or constraints. The domain Intent Contract determines which defaults serve the work and which become material decision candidates.

## State Machine

Use these states in order:

```text
intent
  → initial_draft
  → domain_audit
  → awaiting_human_decision
  → revision
  → regression_audit
  → complete
```

Allow only these recovery transitions:

- `domain_audit → intent` when the draft exposes a missing or contradictory intent constraint.
- `awaiting_human_decision → domain_audit` when the human requests more evidence.
- `regression_audit → revision` when an approved change is incomplete or creates a regression.
- `regression_audit → awaiting_human_decision` when revision exposes a new material trade-off.

Never move directly from `domain_audit` to `revision`.

## Intent Contract

Establish this contract before the audit:

```yaml
intent:
  domain: fiction | presentation_text | document_text | social_copy
  audience: []
  desired_effect: []
  must_preserve: []
  must_avoid: []
  constraints: {}
  open_questions: []
```

Ask only decision-relevant questions. Put domain-specific details under `constraints`; do not redefine shared fields. Resolve material open questions before revision.

Do not ask whether the human wants to reduce AI-like qualities; invocation already establishes that meta-intent. Ask only for the artifact-specific information needed to apply it without sacrificing the human's actual goals.

## Audit Procedure

1. Locate an observable content choice.
2. Cite the smallest useful draft evidence.
3. Name the suspected default as a decision pattern, never as a banned word.
4. Explain the relationship to one or more Intent Contract fields.
5. Generate at least one credible keep or revise alternative.
6. State the effect and trade-offs of each alternative.
7. Recommend `keep`, `revise`, `remove`, or `investigate`.
8. Add the candidate to the Decision Ledger.

Do not invent findings to fill a quota. If no material choice conflicts with intent, return an empty ledger and explain that the audit found no decision requiring human disposition.

## Decision Ledger Contract

Persist ledgers as JSON with this shape:

```json
{
  "ledger_version": 1,
  "run_id": "run-001",
  "domain": "fiction",
  "state": "awaiting_human_decision",
  "intent_ref": "intent-001",
  "draft_ref": "draft-001",
  "entries": [
    {
      "id": "D001",
      "scope": {"kind": "scene", "ref": "scene-4"},
      "observed_choice": "The conflict resolves through sudden forgiveness.",
      "suspected_default": "Tidy reconciliation closes the conflict immediately.",
      "diagnostic_axis": "closure_and_resolution",
      "intent_relevance": "The intent calls for unresolved moral tension.",
      "evidence": ["Scene 4, final two paragraphs"],
      "alternatives": [
        {
          "label": "Keep the disagreement unresolved",
          "effect": "Preserves moral tension into the ending.",
          "tradeoffs": ["Less immediate emotional closure"]
        }
      ],
      "recommendation": {
        "action": "revise",
        "rationale": "The current closure contradicts the desired effect."
      },
      "human_decision": {
        "status": "pending",
        "selected_action": null,
        "notes": ""
      },
      "revision": {
        "status": "not_started",
        "summary": "",
        "artifact_ref": ""
      },
      "regression": {"status": "not_checked", "checks": []}
    }
  ]
}
```

Accepted values:

| Field | Values |
|---|---|
| `domain` | `fiction`, `presentation_text`, `document_text`, `social_copy` |
| `scope.kind` | `document`, `section`, `scene`, `deck`, `slide`, `post`, `thread`, `passage` |
| recommendation/action | `keep`, `revise`, `remove`, `investigate` |
| human status | `pending`, `accepted`, `modified`, `rejected`, `deferred` |
| revision status | `not_started`, `applied`, `not_applicable` |
| regression status | `not_checked`, `passed`, `failed` |

Maintain stable entry IDs throughout revision. Every entry needs observable evidence and intent relevance. A revision may be `applied` only after an `accepted` or `modified` human decision. A passed regression requires at least one named check.

## Human Decision and Revision Gates

Present candidates in priority order with concise alternatives and trade-offs. Ask the human to dispose each material entry. Interpret statuses as follows:

- `accepted`: use the recommended action.
- `modified`: use the human's selected valid action and notes.
- `rejected`: keep the current choice; do not revise it.
- `deferred`: leave unchanged for this pass.
- `pending`: stop before revision.

Revise only the scope authorized by accepted or modified entries. Record the artifact reference and a factual summary of the change.

## Regression Audit

For each applied revision:

1. Re-check the Intent Contract fields named by the entry.
2. Re-check the entry's local dependencies and enabled downstream content.
3. Confirm the chosen action was applied without expanding scope.
4. Record named checks and mark `passed` or `failed`.
5. Return to revision for an incomplete change.
6. Return to human decision when a new material trade-off appears.

Complete only when every applied entry has passed and no material decision remains pending.

## Large Artifacts

Audit coherent units—such as acts, scene groups, deck sections, slide sequences, document sections, threads, or post series—rather than dumping an exhaustive checklist. Keep one Intent Contract and one ledger across units. Reuse entry IDs and cite cross-unit dependencies.

## Error Handling

- Missing intent: remain in `intent`; ask one decision-relevant question at a time.
- Missing draft: offer initial drafting or request the artifact; do not fabricate evidence.
- Unsupported domain: stop without applying a neighboring adapter.
- Insufficient evidence: recommend `investigate` and identify the missing source.
- Conflicting human decisions: return to `awaiting_human_decision` and state the conflict.
- Invalid ledger: report exact validator paths and leave source artifacts unchanged.

## Persistence Validation

From the skill directory, run:

```bash
python scripts/validate_ledger.py <ledger.json>
```

Continue only after it prints `valid: <ledger.json>`.

# Core Workflow

## Contents

- Core rule
- Inception meta-intent
- Review depth
- State machine
- Execution roles
- Intent Contract
- Audit procedure
- Decision Ledger contract
- Human decision and revision gates
- Regression Audit
- Large artifacts
- Error handling
- Persistence validation

## Core Rule

Give equal analytical weight to perceived AI-like convergence and author intent. First surface observable features that co-occur or repeatedly perform the same work, cluster them into an upstream content decision, and explain the convergence effect. Then judge whether that decision serves the stated intent and constraints.

Every finding is a decision candidate. State the feature cues and cluster, what the draft chose, where the evidence appears, how the cluster may create model-default convergence, how it relates to intent, and what keeping or structurally disrupting it would cost. A familiar choice is not automatically weak, and an unusual choice is not automatically strong.

## Inception Meta-Intent

Invoking Inception supplies a balanced baseline meta-intent: reduce perceived model-default or AI-like convergence while preserving the author's intended meaning, constraints, and authority. The human does not need to state either half again.

The first half requires more than a disclaimer or word-level polish: retain a concise trace from observable feature cues to their cluster, convergence effect, and upstream decision, and offer a structural disruption option when revision is recommended. The second half calibrates whether that cluster should change and prevents automatic revision. The meta-intent is not an authorship judgment or a finding quota; the Intent Contract determines which defaults serve the work and which become material decision candidates.

## Review Depth

Inception has two depths with one shared human-decision gate.

### Quick Review

Use a minimal Intent Snapshot inferred from the request and draft:

```yaml
intent_snapshot:
  audience: []
  desired_effect: []
  must_preserve: []
  must_avoid: []
  material_unknowns: []
```

Ask only about a material unknown that could change the recommendation. Audit in the main context and return a small prioritized set of decision cards, usually one to three, with no hard maximum. A card contains the same feature-cluster trace, evidence, intent relationship, alternatives, trade-offs, recommendation, and pending human decision as a ledger entry, but it need not be serialized or expose schema terminology.

If additional material candidates remain, identify their scope briefly and offer to continue Quick Review, run a focused follow-up, or switch to Deep Audit when cross-unit dependencies, stakes, persistence, or independent review justify it. Candidate count alone does not justify Deep Audit. Never suppress a material finding to preserve the usual count.

### Deep Audit

Use the full Intent Contract, independent reviewer when available, Decision Ledger, and reviewer-led Regression Audit. Choose this depth only under the conditions in `SKILL.md`; reviewer availability alone is not a reason to upgrade.

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

## Execution Roles

For Deep Audit, map the state machine to three owners:

- The human-facing main agent owns `intent`, `initial_draft`, presentation of review results, and human-authorized `revision`.
- An independent audit reviewer owns `domain_audit` and `regression_audit` when subagents are available.
- The human owns every material Decision Ledger disposition and decides whether another revision pass may begin after a reviewer reports back.

Follow the Reviewer Protocol for dispatch inputs, reviewer outputs, context isolation, fallback behavior, and regression handoff. A delegated reviewer must not recursively dispatch another reviewer. When independent review is unavailable, the main agent may audit in the same context but must identify that fallback to the human.

For Quick Review, the human-facing main agent owns the audit and Regression Check. The human still owns every material disposition. Do not claim that a Quick Review used independent judgment.

Every reviewer result returns through the main agent to the human. Never run a private reviewer-to-writer revision loop. The actors may change while the ordered states and human-decision gate remain unchanged.

## Intent Contract

For Deep Audit, establish this contract before the audit:

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

For Quick Review, use the Intent Snapshot defined above. Promote to the full contract only if the user selects Deep Audit or the review exposes a material dependency that Quick Review cannot safely resolve. Explain the reason before upgrading.

Do not ask whether the human wants to reduce AI-like qualities; invocation already establishes that meta-intent. Ask only for the artifact-specific information needed to apply it without sacrificing the human's actual goals.

## Audit Procedure

1. Locate observable feature cues and cite the smallest useful draft evidence.
2. Cluster cues that co-occur or repeatedly perform the same work.
3. Name the suspected default as an upstream decision pattern, never as a banned word.
4. Explain how the cluster contributes to perceived AI-like or model-default convergence.
5. Explain the relationship to one or more Intent Contract fields.
6. Generate a credible keep alternative and, when recommending change, a structural pattern-disrupting alternative.
7. State the effect and trade-offs of each alternative.
8. Recommend `keep`, `revise`, `remove`, or `investigate`.
9. Add the candidate to a Quick Review decision card or Deep Audit Decision Ledger using existing fields; do not add one entry per feature.

Do not invent findings to fill a quota. If no material choice conflicts with intent, return an empty review and explain that the audit found no decision requiring human disposition.

## Deep Audit Decision Ledger Contract

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

Present candidates in priority order with concise alternatives and trade-offs. In Quick Review, use ordinary language such as `accept`, `change`, `keep`, or `skip`; map the result internally to the statuses below when needed. In Deep Audit, ask the human to dispose each material entry. Interpret statuses as follows:

- `accepted`: use the recommended action.
- `modified`: use the human's selected valid action and notes.
- `rejected`: keep the current choice; do not revise it.
- `deferred`: leave unchanged for this pass.
- `pending`: stop before revision.

Revise only the scope authorized by accepted or modified entries. Record the artifact reference and a factual summary of the change.

The main agent must not accept a reviewer's recommendation for the human. After a Regression Audit, present the result to the human before starting another revision pass, including when the reviewer reports that an already authorized change was applied incompletely.

## Regression Check and Audit

Quick Review uses a same-agent Regression Check. Deep Audit uses the reviewer handoff when available. Both perform the same substantive checks:

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

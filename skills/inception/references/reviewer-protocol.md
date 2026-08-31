# Reviewer Protocol

This protocol applies to Deep Audit. Quick Review stays in the human-facing main context and does not load or simulate this protocol.

## Core Rule

Automate review dispatch, not content decisions. Keep the human-facing main agent responsible for intent, drafting, presentation, and approved revision. Give an independent reviewer responsibility for audit and regression findings. Keep the human responsible for every material disposition.

Never create an autonomous reviewer-to-writer revision loop.

## Roles

### Main Agent

1. Establish the Intent Contract with the human.
2. Obtain or create the initial draft.
3. Select the domain adapter.
4. Dispatch the audit when Deep Audit was selected and an independent subagent is available.
5. Validate and present the review result without accepting entries for the human.
6. Apply only human-accepted or human-modified actions.
7. Present every Regression Audit result to the human before another revision pass.

The main agent may add navigation or explain the ledger format. It must preserve both analytical halves: the feature cluster and convergence effect, and the cluster's relationship to intent. It must also preserve the substance of each observed choice, evidence item, alternative, trade-off, and recommendation.

### Audit Reviewer

Load Inception's core workflow and exactly one selected domain adapter. Use the supplied Intent Contract and draft as the only bases for judgment. Return either:

- an `intent_gap` identifying the missing decision-relevant information; or
- a Decision Ledger in `awaiting_human_decision`, including an empty ledger when no material finding exists.

For every material entry, preserve a concise trace from observable feature cues to their cluster, convergence effect, upstream decision, and intent relationship in the existing ledger fields. Include a credible keep alternative and, when recommending change, a structural alternative that disrupts the identified pattern. Do not turn the trace into a feature inventory or add ledger fields.

Do not revise the artifact, dispose ledger entries, speak on the human's behalf, or dispatch another reviewer.

### Human

Decide whether each material entry is `accepted`, `modified`, `rejected`, or `deferred`. A request to draft, polish, improve, or continue does not pre-accept later audit findings.

## Audit Dispatch Contract

Give the reviewer only the task-local material needed for an independent audit:

```yaml
role: inception_audit_reviewer
domain: fiction | presentation_text | document_text | social_copy
intent: <complete Intent Contract>
draft_ref: <stable draft identifier>
draft: <artifact text or accessible artifact reference>
requested_state: awaiting_human_decision
```

Also identify the Inception skill to load when it is not already discoverable. Do not include the main agent's suspected findings, preferred conclusion, hidden reasoning, or suggested edits. Do not tell the reviewer how many findings to produce.

If the reviewer returns an invalid persisted ledger, return the validator errors for correction without prescribing substantive findings. If reviewer correction is unavailable, the main agent may repair structural serialization errors only; it must not invent or materially alter findings.

### Fiction-specific handling

For `domain: fiction`, the audit reviewer must read the core workflow, the complete fiction adapter, and the complete [StoryScope feature registry](storyscope-features.md). The registry is for feature-level inspection only. It does not replace the ten fiction diagnostic axes, create a finding quota, or add fields to the ledger.

Before creating any Decision Ledger candidate, the reviewer must cluster co-occurring features, deduplicate observations that describe the same choice, and synthesize the relevant upstream narrative decision. The reviewer returns material decisions rather than a feature inventory, but keeps the feature-to-cluster reasoning visible in concise human-readable form. A feature ID may be used in working analysis, but any persisted trace must use the existing `observed_choice`, `suspected_default`, `diagnostic_axis`, and `evidence` fields; do not add a ledger key.

Do not recommend `remove` or `revise` merely because a choice is AI-elevated, and do not treat a human-elevated value as a revision proposal. Do not produce a fixed number of findings. An empty ledger is valid. Every proposed decision should include a credible rationale for keeping the current choice and clearly state the trade-offs of the available alternative. If there is no evidence-backed material tension with the Intent Contract, return no candidate.

These rules preserve the existing Audit Dispatch Contract, role permissions, state ownership, domain values, and ledger schema.

## Fallback

When Deep Audit was selected but the current environment cannot create an independent subagent, keep the same state machine and perform the audit in the main context. Tell the human once that independent review was unavailable. Do not claim role separation or fabricate reviewer output.

## Regression Handoff

After an approved revision, give a reviewer the Intent Contract, accepted or modified ledger entries, the prior draft, the revised draft, and the authorized revision scope. Prefer a fresh reviewer context when available.

The reviewer checks only whether the authorized action was applied, affected intent constraints remain intact, dependencies still hold, and a new material trade-off appeared. Return the result to the main agent. The main agent presents it to the human before any additional revision pass; agents do not iterate privately.

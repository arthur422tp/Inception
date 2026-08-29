# Intent-Preserving Default Auditor Design

## Purpose

Build a project-local Codex skill that exposes content decisions which may have been selected because they are an easy model default rather than because they serve the author's intent. The skill does not try to make prose look less AI-generated. It helps a human decide what to keep, revise, or reject.

The first release supports two domains:

- fiction;
- presentation text, including deck structure, slide claims, and supporting content.

The architecture must allow later adapters, such as research writing, without changing the core workflow or ledger contract.

## Scope

The skill covers:

- capturing an explicit intent contract;
- accepting an existing draft or helping produce an initial draft;
- auditing content decisions through a domain adapter;
- recording audit findings as decision candidates rather than automatic defects;
- pausing for human decisions;
- revising only approved items;
- running a regression audit against the intent and accepted decisions.

The skill does not cover:

- AI-source detection or authorship classification;
- vocabulary blacklists or cosmetic “humanization”;
- typography, color, spacing, grid, alignment, visual hierarchy, icons, illustrations, slide masters, or visual style;
- automatic rewriting of every flagged pattern;
- treating StoryScope's population-level findings as universal rules for good writing.

## Design Principles

1. **Intent outranks rarity.** A common choice can be correct when it serves the intent; an unusual choice can still be weak.
2. **Defaults are candidates, not violations.** An audit finding must explain why a choice may be a default and what purpose it currently serves.
3. **Preserve human authority.** The workflow must not revise a material content decision before the human records a disposition.
4. **Diagnose decisions, not words.** Replace generic claims with evidence-bearing claims when appropriate, but do not maintain banned-word lists.
5. **Separate core mechanics from domain judgment.** State transitions and ledger validation live in the core; diagnostic axes live in adapters.
6. **Regression means intent preservation.** A revision succeeds only if it addresses the selected finding without breaking the intent contract or accepted dependencies.

## Project Shape

Use one discoverable skill with progressively loaded references and deterministic validation utilities:

```text
inception/
├── skills/
│   └── inception/
│       ├── SKILL.md
│       ├── agents/
│       │   └── openai.yaml
│       ├── references/
│       │   ├── core-workflow.md
│       │   ├── fiction-adapter.md
│       │   └── presentation-text-adapter.md
│       └── scripts/
│           └── validate_ledger.py
├── src/
│   └── inception/
│       ├── __init__.py
│       ├── ledger.py
│       └── workflow.py
└── tests/
    ├── test_ledger.py
    ├── test_workflow.py
    └── fixtures/
```

`SKILL.md` stays concise and routes to exactly one adapter after loading the core workflow. The Python package defines the machine-checkable contract. The skill remains usable without executing Python, but any persisted ledger must pass the validator.

## Core State Machine

The workflow has seven ordered states:

```text
intent
  → initial_draft
  → domain_audit
  → awaiting_human_decision
  → revision
  → regression_audit
  → complete
```

Allowed recovery transitions are deliberately narrow:

- `domain_audit → intent` when the draft exposes a missing or contradictory intent constraint;
- `awaiting_human_decision → domain_audit` when the human requests more evidence;
- `regression_audit → revision` when an approved change is incomplete or creates a regression;
- `regression_audit → awaiting_human_decision` when the revision exposes a new material trade-off.

The workflow must reject skipped gates, especially `domain_audit → revision`. The initial draft may be supplied by the user or generated during the workflow; both enter the same audit path.

## Intent Contract

Every run begins with an intent contract:

```yaml
intent:
  domain: fiction | presentation_text
  audience: []
  desired_effect: []
  must_preserve: []
  must_avoid: []
  constraints: {}
  open_questions: []
```

Adapter-specific fields may be added under `constraints`, but adapters may not redefine the shared fields. Material unresolved questions prevent the workflow from entering revision.

## Decision Ledger

The ledger is the handoff surface between audit, human judgment, revision, and regression checking.

```yaml
ledger_version: 1
run_id: string
domain: fiction | presentation_text
state: awaiting_human_decision
intent_ref: string
draft_ref: string
entries:
  - id: D001
    scope:
      kind: document | section | scene | deck | slide | passage
      ref: string
    observed_choice: string
    suspected_default: string
    diagnostic_axis: string
    intent_relevance: string
    evidence:
      - string
    alternatives:
      - label: string
        effect: string
        tradeoffs: []
    recommendation:
      action: keep | revise | remove | investigate
      rationale: string
    human_decision:
      status: pending | accepted | modified | rejected | deferred
      selected_action: keep | revise | remove | investigate | null
      notes: string
    revision:
      status: not_started | applied | not_applicable
      summary: string
      artifact_ref: string
    regression:
      status: not_checked | passed | failed
      checks: []
```

Required invariants:

- every entry points to observable draft evidence;
- `suspected_default` describes a decision pattern, not an undesirable word;
- every recommendation states its relationship to the intent;
- revision cannot be `applied` while the human decision is `pending`, `rejected`, or `deferred`;
- regression cannot pass without checking the affected intent constraints and relevant dependencies;
- a ledger may contain no findings; the skill must not invent issues to fill a quota.

## Fiction Adapter

The fiction adapter audits narrative decisions, not literary quality in the abstract. Its initial diagnostic axes are:

- thematic explicitness and over-determination;
- causal linearity and protagonist-driven resolution;
- chronology, delayed disclosure, and recontextualization;
- subplot absence, integration, and independence;
- ambiguity, closure, and resolution mechanism;
- character agency and moral complexity;
- emotional presentation, including habitual embodied cues;
- sensory detail chosen as atmosphere, evidence, or default ornament;
- intertextual specificity and reader awareness;
- structural repetition across scenes.

StoryScope findings provide hypotheses and vocabulary for inspection. They are not normative thresholds. The adapter must always ask whether the observed choice serves the current story's intent before recommending change.

## Presentation Text Adapter

The presentation adapter handles only semantic and rhetorical content at three levels:

### Deck level

- argument architecture;
- section necessity;
- claim and evidence order;
- redundancy;
- conclusion as synthesis rather than repetition;
- dependence on generic presentation templates.

### Slide level

Represent each slide as:

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

Audit rhetorical role, claim specificity, evidence alignment, dependency integrity, and whether the slide needs to exist. Topic headings are not automatically wrong, but the adapter must distinguish them from assertion, question, and transition headings.

### Content level

- count information-bearing propositions;
- replace unsupported abstractions with evidence when the source material permits;
- identify same-meaning bullets and generic transitions;
- keep slide text appropriate for spoken presentation rather than turning every bullet into complete prose.

Visual form must never appear as a required audit field.

## Skill Interaction Contract

When invoked, the skill must:

1. identify or ask for the domain;
2. establish the intent contract;
3. obtain or create the initial draft;
4. load only the selected adapter;
5. produce a bounded audit with evidence-backed ledger entries;
6. show the decision ledger and stop for human decisions;
7. revise only accepted or modified entries;
8. run regression checks and report unresolved trade-offs.

For large artifacts, the skill should audit in coherent units and maintain one ledger, rather than dumping an exhaustive checklist in a single response.

## Error Handling

- **Missing intent:** remain in `intent` and ask one decision-relevant question at a time.
- **Missing draft:** offer draft generation or request an artifact; do not fabricate an audit.
- **Unsupported domain:** explain that no adapter exists and stop before applying fiction or presentation assumptions.
- **Insufficient evidence:** use `investigate` and identify the missing source; do not upgrade an inference to a finding.
- **Conflicting human decisions:** return to `awaiting_human_decision` with the conflict made explicit.
- **Invalid ledger:** report exact invariant violations and leave source artifacts unchanged.

## Testing Strategy

Implementation follows test-driven development at two levels.

### Deterministic tests

- valid and invalid state transitions;
- ledger schema requirements and cross-field invariants;
- adapter and domain matching;
- regression gate behavior;
- command-line validator success and failure output.

### Skill behavior tests

Before writing the skill, run baseline scenarios without it and record failures. Then run equivalent scenarios with the skill. At minimum test:

- a conventional fiction choice that correctly serves the intent and should be kept;
- a fiction draft with a default-like tidy resolution unsupported by the intent;
- a presentation with topic headings, duplicated claims, and weak evidence;
- a presentation whose topic heading is intentionally appropriate;
- pressure to rewrite before receiving a human decision;
- a clean draft where the correct ledger contains no findings.

Success means the agent distinguishes defaults from defects, cites draft evidence, respects the human-decision gate, and does not introduce visual-design advice.

## Acceptance Criteria

- Codex can discover the skill from a relevant fiction or presentation-text request.
- The core workflow uses one shared ledger contract for both adapters.
- The ledger validator rejects skipped decisions and inconsistent revision states.
- Fiction audit findings are framed as intent-relative hypotheses.
- Presentation audit never requires visual-design fields or advice.
- The workflow can accept a user draft or produce an initial draft without changing later states.
- Revision is bounded by explicit human decisions.
- Regression audit checks intent preservation and downstream dependencies.
- Automated tests and the skill folder validator pass with clean output.

## Deferred Work

- research-writing and other domain adapters;
- visual presentation design;
- automatic integration with Canva, PowerPoint, or document editors;
- corpus-level scoring or StoryScope feature extraction;
- quantitative originality or AI-authorship scores.

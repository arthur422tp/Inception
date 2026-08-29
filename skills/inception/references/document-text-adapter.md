# Document Text Adapter

## Contents

- Scope and evidence
- Candidate recipe
- Semantic levels and section records
- Diagnostic axes
- Cross-section audit
- Recommendation calibration
- Excluded format concerns

## Scope and Evidence

Audit content decisions in reports, proposals, memos, specifications, policies, SOPs, research summaries, and other sustained documents. Do not judge document quality in the abstract.

StoryScope's population-level fiction tendencies supply hypotheses about choices that models may make by default. Their transfer to document text is a method for inspection, not evidence that documents share the same measured tendencies. They are not thresholds, prohibitions, quality rules, or proof of AI authorship.

Evaluate choices at document, section, and passage scope. Cite the smallest useful evidence, then inspect definitions, prerequisites, supporting material, and downstream consequences when the choice crosses sections.

## Candidate Recipe

Build every ledger candidate in this order:

```text
Observed content choice -> document evidence -> suspected default
-> intent relationship -> keep/revise alternative -> trade-off -> recommendation
```

Include a plausible reason to keep the current choice. If the only argument for change is that wording, repetition, or structure is common, do not create an entry. Prefer one upstream document- or section-level entry over many sentence-level duplicates.

## Semantic Levels and Section Records

Use three semantic levels:

```text
Document purpose -> Section function -> Information-bearing content
```

Before judging a section, represent its job:

```yaml
section_id: SEC-04
role: recommendation
claim: Adopt staged rollout for systems with irreversible migrations.
support:
  - rollback is unavailable after schema conversion
  - pilot results cover only one traffic profile
depends_on:
  - SEC-02_constraints
  - SEC-03_evidence
enables:
  - SEC-05_ownership
```

Use roles such as `orientation`, `definition`, `context`, `claim`, `analysis`, `evidence`, `comparison`, `procedure`, `requirement`, `decision`, `recommendation`, `risk`, `ownership`, `reference`, or `summary`. Add another role only when its function cannot be expressed by these terms.

Distinguish facts, sourced claims, interpretations, requirements, decisions, recommendations, uncertainties, and examples. Do not force every section to contain a claim: a glossary, procedure, reference table, or compliance record may serve a different reader task.

## Diagnostic Axes

### 1. Explicitness and Over-Determination

Ask whether examples, evidence, definitions, and consequences already establish the point before the document explains it again. Test whether removing a restatement would reduce redundancy or hide a necessary interpretation.

Suspected default: an executive summary states a conclusion, each section paraphrases it, and the conclusion repeats it without adding scope, synthesis, or action.

The common choice can serve intent in stand-alone sections, compliance documents, safety procedures, accessibility-oriented material, or documents read nonlinearly.

### 2. Argument Linearity and Single-Solution Resolution

Ask whether the document follows one clean problem-to-solution chain because the decision warrants it or because competing causes, constraints, and paths were never considered.

Suspected default: background leads inevitably to one recommendation, which appears to resolve every issue introduced earlier.

The common choice can serve intent in approved implementation instructions, incident commands, narrowly scoped decision records, or procedures whose alternatives were resolved elsewhere.

### 3. Information Order, Context, and Recontextualization

Ask when readers receive definitions, assumptions, constraints, and exceptions. Check whether later information changes how earlier claims should be interpreted and whether that information arrives where readers need it.

Suspected default: generic background appears first, while a decisive limitation or definition arrives only after readers have accepted the main conclusion.

The common choice can serve intent when chronological traceability, onboarding, legal sequencing, or comparison with prior versions matters.

### 4. Alternatives, Counterexamples, and Secondary Lines

Ask whether alternatives, objections, edge cases, and secondary considerations perform real analytical work. Do not demand balance when the document's purpose is to record an already-made decision.

Suspected default: a token alternatives or risks section lists weak objections that all reinforce the preferred recommendation.

The common choice can serve intent in short operational notices, final decision records, or documents that link to a complete analysis maintained elsewhere.

### 5. Uncertainty, Qualification, and Closure

Ask what the evidence actually resolves and which uncertainty must remain visible. Inspect whether confidence, scope, and next steps are supported independently.

Suspected default: the conclusion converts partial evidence into certainty, then closes with generic next steps that imply all important questions are settled.

The common choice can serve intent when an authorized decision must be stated unambiguously, a procedure requires deterministic action, or accepted assumptions are explicitly recorded.

### 6. Stakeholder Agency, Responsibility, and Decision Rights

Ask who supplies information, makes decisions, performs work, bears risk, approves exceptions, and can change the outcome. Check whether passive voice or abstract nouns hide responsibility that the intent requires readers to know.

Suspected default: `the team`, `stakeholders`, or `the organization` owns every action, while affected groups appear only as beneficiaries, blockers, or sources of requirements.

The common choice can serve intent when responsibility is genuinely collective, names must remain confidential, or ownership is defined in an authoritative linked source.

### 7. Emotional Framing, Urgency, and Confidence

Ask how urgency, reassurance, authority, fear, or aspiration enters the document: evidence, consequences, anecdotes, modal verbs, intensifiers, or repeated assurances.

Suspected default: problems become urgent, proposals become transformational, and conclusions become confident without additional evidence.

The common choice can serve intent in crisis instructions, mobilization, advocacy, executive sponsorship, or communications whose agreed purpose includes emotional activation.

### 8. Claims, Evidence, and Concrete Specificity

Ask what supports each material factual or causal proposition and whether examples, numbers, quotations, and mechanisms delimit the claim they accompany.

Suspected default: generic claims use decorative numbers or adjectives such as `robust`, `comprehensive`, and `significant` without evidence for the propositions those words introduce.

Do not blacklist those words. Identify the claim, its required support, and the consequence of keeping it broad. The common choice can serve intent when detail is intentionally delegated to a cited source or the document only provides orientation.

### 9. Sources, Terminology, and Reader Assumptions

Ask whether citations, definitions, acronyms, domain conventions, and references have a precise function. Check what knowledge, authority, incentives, and vocabulary the document assumes.

Suspected default: phrases such as `research shows`, `industry standard`, or `users need` invoke vague authority while terminology shifts between sections without declaring a distinction.

The common choice can serve intent when sources and definitions are established in a controlled parent document or the audience shares a stable professional context.

### 10. Structural Repetition Across Sections

Ask whether sections repeatedly perform the same sequence—context, three points, benefit, summary—or whether repetition enables lookup, comparison, compliance, safety, or independent reuse.

Suspected default: headings and examples change while sections preserve the same rhetorical work and add no new dependency, evidence, decision, or action.

The common choice can serve intent in SOPs, policies, repeated category comparisons, reference manuals, audit forms, or documents whose sections must stand alone.

## Cross-Section Audit

After local candidates are found, check:

- whether several entries arise from one upstream purpose or structure decision;
- whether definitions and qualifiers remain consistent across sections;
- whether evidence appears where a claim depends on it;
- whether an executive summary accurately preserves the body's scope and uncertainty;
- whether apparent repetition enables nonlinear use or merely restates content;
- whether requirements, recommendations, and examples are distinguishable;
- whether ownership and next steps follow from the documented decision;
- whether a standard section exists because the reader task needs it or because a template suggested it;
- whether an unusual alternative would violate auditability, compliance, safety, audience, or length constraints.

Merge duplicates into the highest useful scope. Record dependencies before human review.

## Recommendation Calibration

- `keep`: the choice serves the document's purpose or reader task, and its familiarity is not a problem.
- `revise`: a concrete alternative improves evidence alignment, qualification, consistency, responsibility, or reader action at acceptable cost.
- `remove`: content performs no needed informational, procedural, evidentiary, or reference function and weakens another intent constraint.
- `investigate`: evidence, authority, source material, reader needs, or author intent is missing.

Prefer a small number of material candidates over a catalogue of every recognizable tendency.

## Excluded Format Concerns

Audit document text and semantic structure only. Do not add ledger findings about page layout, typography, fonts, margins, spacing, headers and footers, pagination, visual styling, tracked changes, comments, or file-format mechanics. Hand those concerns to a document-production workflow outside this skill.

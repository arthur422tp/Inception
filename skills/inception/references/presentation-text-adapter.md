# Presentation Text Adapter

## Contents

- Scope and evidence
- Candidate recipe
- Semantic levels and slide records
- Upstream argument pass
- Diagnostic axes
- Cross-slide audit
- Revision priorities
- Recommendation calibration
- Excluded visual concerns

## Scope and Evidence

Audit rhetorical decisions, not presentation quality in the abstract. Use StoryScope's population-level tendencies as a method for forming presentation-specific hypotheses for inspection; these transfer hypotheses are not findings about presentations, thresholds, prohibitions, or proof of AI authorship.

Audit what the presentation says, why it says it, and in what rhetorical order. Treat titles as content. Evaluate choices at deck, section, slide, and passage scope. Cite the smallest useful evidence, then check its prerequisites and downstream consequences when necessary.

## Candidate Recipe

Build every ledger candidate in this order:

```text
Observed rhetorical choice -> slide/deck evidence -> suspected default
-> intent relationship -> keep/revise alternative -> trade-off -> recommendation
```

Include a plausible reason to keep the current choice. If the only argument for change is that a structure or phrase is common, do not create an entry. Prefer one upstream deck- or slide-role entry over many sentence-level duplicates.

Apply Inception's baseline meta-intent through observable rhetorical structure without asking the user to restate it. Do not infer authorship. Do not treat formal language, formulas, technical density, or a comprehensive scope as defects by themselves.

## Semantic Levels and Slide Records

Use three semantic levels:

```text
Deck argument -> Slide function -> Information-bearing content
```

Map the deck as a sequence of claims and dependencies. Before judging a slide, represent its rhetorical job:

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

Use roles such as `setup`, `problem`, `claim`, `mechanism`, `evidence`, `comparison`, `decision`, `implication`, `transition`, or `summary`. Add another role only when its rhetorical job cannot be expressed by these terms. If a slide is intentionally a question or transition, state the audience change it enables instead of inventing a claim.

Classify each heading as `topic`, `assertion`, `question`, or `transition`. Do not force every topic heading into an assertion. A topic heading can serve navigation, neutral reference, repeated category comparison, or a section divider.

Count information-bearing propositions rather than lines or bullets. A proposition identifies a specific fact, mechanism, decision, comparison, constraint, piece of evidence, implication, or uncertainty.

For each slide record, ask:

1. What should the audience leave believing, understanding, asking, or anticipating?
2. Does its role differ materially from neighboring slides?
3. Is its claim specific enough to be supported or challenged?
4. Does each support item address that claim, including its qualifiers?
5. Are prerequisites present before the slide depends on them?
6. Does the slide enable later reasoning, or is it an isolated topic?
7. Could removing or merging it preserve the argument?

## Upstream Argument Pass

Before creating slide-local entries, inventory each material claim or concept across the deck. Record its appearances and explanatory modes: title assertion, definition, mechanism, formula, analogy, example, evidence, transition, recap, or conclusion.

For each appearance, ask what distinct audience change it enables. If a claim is repeatedly titled, paraphrased, analogized, formalized, exemplified, and summarized without adding a prerequisite, evidence item, qualification, comparison, decision, or action, treat the cluster as one upstream deck candidate.

Assign each claim or concept a deck-level salience:

- `primary`: necessary to the deck's argument or decision;
- `supporting`: needed to justify, qualify, compare, or apply a primary claim;
- `reference`: accurate and useful, but not required for the main audience journey.

Salience controls rhetorical emphasis, not truth value. Preserve technical mechanisms, formulas, evidence, constraints, and limitations even when recommending that secondary material stop carrying the main argument.

## Diagnostic Axes

### 1. Message Explicitness and Over-Determination

Ask whether the evidence, examples, and sequence already carry the message before the heading, bullets, narration, or conclusion explains it again. Test whether removing a restatement would create useful interpretive work or merely hide a necessary conclusion.

Suspected default: the heading states the takeaway, the body paraphrases it, and a summary repeats it once more, closing every inference for the audience.

The common choice can serve intent when the deck must stand alone, records an executive decision, supports novice audiences, or requires explicit compliance language.

### 2. Argument Linearity and Solution-Driven Resolution

Ask whether the deck follows one clean problem-to-solution chain because the decision genuinely depends on it or because competing causes and paths were not considered. Inspect what actually produces the promised outcome: the proposal, multiple actors, operating conditions, external constraints, timing, or unresolved uncertainty.

Suspected default: each section advances one preferred solution, and the solution appears to resolve every material problem introduced by the deck.

The common choice can serve intent in procedural instruction, short decision briefs, emergency communication, or pitches whose alternatives were evaluated elsewhere.

### 3. Information Order, Hierarchy, and Recontextualization

Ask when the audience receives crucial context, whether later evidence changes the meaning of earlier claims, and whether each concept's emphasis matches its role in the deck. Distinguish useful recontextualization from withholding a constraint merely to manufacture surprise.

Suspected default: an agenda and background section front-load explanation while later evidence adds facts without changing the initial problem; or every related technical detail receives equal rhetorical weight regardless of the decision the deck supports.

The common choice can serve intent when rapid orientation, chronological reporting, auditability, or comparison across presenters matters.

### 4. Secondary Lines, Alternatives, and Counterarguments

Ask whether secondary arguments introduce pressure, contrast, competing values, or credible alternatives. A secondary line should have a rhetorical job beyond delaying or decorating the preferred conclusion.

Suspected default: every section directly advances the main recommendation, or a token alternatives or risks slide is framed so that every option confirms the preferred answer.

The common choice can serve intent in tightly time-boxed briefings, status updates, or decisions whose alternatives and objections have already been resolved in an accessible source.

### 5. Uncertainty, Closure, and Decision Mechanism

Ask what the deck resolves: factual uncertainty, causal explanation, option comparison, ownership, timing, or authority to act. Identify which uncertainty should remain visible after the conclusion.

Suspected default: benefits, recommendation, and generic next steps close the argument simultaneously, even when the evidence supports only a conditional or partial decision.

The common choice can serve intent when the audience needs a clear decision request, a procedural handoff, or immediate action under already accepted assumptions.

### 6. Stakeholder Agency and Value Complexity

Ask who can materially change the outcome, who bears cost or risk, and whether opposing positions have intelligible incentives. Do not equate additional stakeholders or moral ambiguity with depth automatically.

Suspected default: the presenter, product, or proposed solution owns meaningful agency, while customers, operators, partners, and affected groups appear only as beneficiaries, blockers, or evidence of demand.

The common choice can serve intent in owner-specific updates, narrowly scoped implementation plans, or presentations where stakeholder analysis is maintained elsewhere.

### 7. Emotional Framing and Urgency

Ask how urgency, confidence, fear, aspiration, or reassurance enters the argument: evidence, consequence, wording, anecdote, social proof, or repeated intensifiers. Look for emotional repetition that stops carrying new information.

Suspected default: each problem is escalated into a crisis, each benefit becomes transformational, and the conclusion supplies confidence or inspiration without additional support.

The common choice can serve intent in fundraising, mobilization, crisis response, ceremonial speaking, or any presentation whose agreed purpose includes emotional activation.

### 8. Concrete Detail, Evidence, and Technical Fidelity

Ask what each prominent number, example, named mechanism, quotation, formula, or technical detail does: support a claim, delimit scope, enable comparison, expose uncertainty, or make a consequence concrete. Separate preservation of an accurate technical point from the decision about how prominently or repeatedly the deck explains it.

Suspected default: generic claims rely on decorative specificity for credibility, or use adjectives such as `robust`, `scalable`, and `significant` without evidence for the propositions they introduce.

For example, do not blacklist the adjectives in:

> We developed a robust and scalable system that significantly improves reliability.

Ask what supports each proposition. If the source permits, prefer a specific decision and consequence:

> Parallel SQL workers return typed results through reducer channels, so completion order does not affect merged output.

Do not remove formulas, caveats, failure modes, or technical limits merely to make the deck sound more natural. The common choice can serve intent when a brief example provides orientation, a memorable case anchors abstraction, or technical detail is intentionally deferred to narration or an appendix.

### 9. Source Specificity and Audience Awareness

Ask whether citations, allusions, quotations, domain conventions, and direct address have a precise rhetorical function. Check what knowledge, authority, values, and vocabulary the deck assumes of its audience.

Suspected default: phrases such as `research shows`, `industry best practice`, or `customers want` invoke vague authority, while the deck addresses the audience as a uniform group with one set of interests.

The common choice can serve intent when sources are established in accompanying material, the audience shares a stable professional context, or citation detail would interrupt a deliberately high-level briefing.

### 10. Structural Repetition and Representational Proliferation

Ask whether slides repeatedly perform the same sequence—topic heading, three parallel bullets, benefit statement, transition—or whether repetition creates comparison, escalation, rhythm, or reliable navigation. Also ask whether one claim is repeatedly repackaged through titles, analogy families, examples, formulas, recaps, and summary slides that perform the same rhetorical job.

Suspected default: slide titles and examples change while slides preserve the same rhetorical work; or each concept receives several explanatory forms even though later forms add no evidence, qualification, comparison, decision, or action.

The common choice can serve intent in repeated category comparisons, recurring operational reviews, teaching sequences, workshops, deliberate recaps before a decision, or mixed-expertise audiences whose members need genuinely different representations.

## Cross-Slide Audit

After local candidates are found, check:

- whether two entries describe one upstream deck-structure decision;
- whether evidence arrives where the claim needs it;
- whether a slide depends on a premise that appears only later;
- whether the same proposition is being re-explained or doing new rhetorical work;
- whether multiple analogy families clarify distinct aspects or increase translation burden;
- whether primary, supporting, and reference material receive proportionate emphasis;
- whether apparent repetition is comparison, escalation, pacing, or redundancy;
- whether removing or merging a slide preserves the argument;
- whether the conclusion synthesizes dependencies or only repeats prior propositions;
- whether an agenda, background, solution, benefits, risks, or future-work section exists because the argument needs it or because the template suggested it;
- whether a proposed unusual alternative violates audience needs, delivery mode, time, or the desired effect.

Merge duplicates into the highest useful scope. Record dependencies before human review.

## Revision Priorities

For every accepted revision, use this default priority order unless the domain Intent Contract requires a different trade-off:

1. Preserve the technical claims, formulas, evidence, limitations, definitions, and constraints that the Intent Contract protects.
2. Merge slides or sections that repeat the same synthesis without serving a distinct audience or decision task.
3. Consolidate multiple analogy families when they re-explain the same concept; retain the representation that best serves the audience.
4. Keep accurate but secondary derivations or formulas available at `supporting` or `reference` salience instead of deleting them.
5. Re-check whether each remaining representation adds a mechanism, use case, qualification, evidence item, comparison, decision, or action.

Do not substitute synonyms, force conversational phrasing, add filler, or invent presenter personality as a proxy for structural revision.

## Recommendation Calibration

- `keep`: the choice serves intent and its familiarity is not a problem.
- `revise`: a concrete alternative improves claim specificity, evidence alignment, order, or audience effect at acceptable cost.
- `remove`: a section, slide, or proposition performs no needed rhetorical work and weakens another intent constraint.
- `investigate`: evidence, audience needs, source material, or presenter intent is missing.

Prefer a small number of material candidates over a catalogue of every recognizable tendency.

## Excluded Visual Concerns

`visual_form` is not an audit field. Never add ledger findings or recommendations about typography, font choice, color, spacing, grid, alignment, visual hierarchy, icons, illustrations, slide masters, or visual style. Hand those concerns to a presentation-design workflow outside this skill.

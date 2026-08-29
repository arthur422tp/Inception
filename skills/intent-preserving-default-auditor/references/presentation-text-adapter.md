# Presentation Text Adapter

## Contents

- Scope
- Deck-level audit
- Slide semantic record
- Slide-level audit
- Content-level audit
- Heading functions
- Recommendation calibration
- Excluded visual concerns

## Scope

Audit what the presentation says, why it says it, and in what rhetorical order. Treat titles as content. Do not evaluate or recommend visual design.

Use three semantic levels:

```text
Deck argument → Slide function → Information-bearing content
```

## Deck-Level Audit

Map the presentation as a sequence of claims and dependencies. For each section, ask:

- What must the audience believe or understand after this section?
- Why does this section exist for this audience and goal?
- Does its position establish context, mechanism, evidence, implication, or transition at the needed moment?
- Does evidence arrive where the claim needs it?
- Do two sections perform the same rhetorical work?
- Does the conclusion add synthesis or only repeat prior bullets?
- Is an agenda, background, solution, benefits, or future-work section present because the argument needs it or because the template suggested it?

A familiar deck structure can serve intent when the audience expects rapid orientation, the presentation is procedural, or comparison across presenters matters. Do not recommend novelty for its own sake.

## Slide Semantic Record

Represent each slide before judging it:

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

Use roles such as `setup`, `problem`, `claim`, `mechanism`, `evidence`, `comparison`, `decision`, `implication`, `transition`, or `summary`. Add another role only when its rhetorical job cannot be expressed by these terms.

If a slide has no claim because it is intentionally a question or transition, state the audience change it enables instead of inventing an assertion.

## Slide-Level Audit

For every slide, ask:

1. What should the audience leave believing, understanding, asking, or anticipating?
2. Does the role differ materially from the neighboring slides?
3. Is the claim specific enough to be supported or challenged?
4. Does each support item actually support the claim?
5. Are prerequisites present before the slide depends on them?
6. Does the slide enable later reasoning, or is it an isolated topic?
7. Could removing or merging the slide preserve the argument?

Suspected defaults include a sequence of interchangeable topic slides, repeated three-bullet structures that carry the same propositions, unsupported benefit claims, and sections included only because presentations commonly contain them.

The common choice can serve intent when the slide provides navigation, separates evidence for pacing, respects a time-boxed speaking rhythm, or creates a deliberate recap before a decision.

## Content-Level Audit

Count information-bearing propositions. A phrase carries information when it identifies a specific fact, mechanism, decision, comparison, constraint, piece of evidence, implication, or uncertainty.

For a generic claim such as:

> We developed a robust and scalable system that significantly improves reliability.

Do not blacklist `robust`, `scalable`, or `significantly`. Ask what evidence supports each proposition. If source material permits, replace the abstraction with a specific decision and consequence:

> Parallel SQL workers return typed results through reducer channels, so completion order does not affect merged output.

Also inspect:

- bullets that restate one another;
- generic transitions that add no dependency;
- evidence that answers a different claim;
- conclusions that repeat rather than synthesize;
- complete prose that belongs in narration rather than visible slide copy;
- compressed fragments that omit the qualifier needed for accuracy.

## Heading Functions

Classify each heading as one of:

- `topic`: names the subject;
- `assertion`: states a claim;
- `question`: frames an inquiry;
- `transition`: marks a change in argumentative function.

Do not force every topic heading into an assertion. A topic heading is appropriate for navigation, neutral reference, repeated category comparison, or a section divider. Create a ledger candidate only when the heading function fails to serve audience orientation or obscures the slide's real claim.

## Candidate Recipe

For each material issue, record:

```text
Observed rhetorical choice → slide/deck evidence → suspected template default
→ audience/goal relationship → keep/revise alternatives → trade-off → recommendation
```

Prefer upstream deck or slide-role entries over many sentence-level duplicates.

## Recommendation Calibration

- `keep`: the familiar structure or wording serves audience and goal.
- `revise`: a more specific claim, better evidence alignment, or changed order improves the argument.
- `remove`: a section, slide, or proposition performs no needed rhetorical work.
- `investigate`: evidence, audience needs, or presenter intent is missing.

## Excluded Visual Concerns

`visual_form` is not an audit field. Never add ledger findings or recommendations about typography, font choice, color, spacing, grid, alignment, visual hierarchy, icons, illustrations, slide masters, or visual style. Hand those concerns to a presentation-design workflow outside this skill.

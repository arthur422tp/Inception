# Social Copy Adapter

## Contents

- Scope and evidence
- Candidate recipe
- Semantic levels and post records
- Upstream post pass
- Diagnostic axes
- Cross-post audit
- Revision priorities
- Recommendation calibration
- Excluded concerns

## Scope and Evidence

Audit organic brand and personal social posts, including captions, short posts, long-form posts, threads, and recurring post series. Do not use this adapter for paid advertising.

StoryScope studies fiction, not social copy. This adapter transfers its non-style analytical dimensions into questions about social content; it does not claim that StoryScope measured the same tendencies in social posts. The transfer supplies hypotheses for inspection, not thresholds, prohibitions, quality rules, or proof of AI authorship.

The first nine axes below correspond to StoryScope's narrative-only dimensions: Agent, Social Networks, Events, Plot, Situatedness, Setting, Temporal Structure, Revelation, and Perspective. StoryScope's Style dimension is intentionally excluded because Inception audits upstream content decisions rather than surface signals. The tenth axis transfers the paper's cross-dimensional findings about thematic over-determination, structural streamlining, and lower narrative diversity.

Evaluate an account or recurring series at `document` or `section` scope, a thread at `thread` scope, and an individual post at `post` or `passage` scope. Cite the smallest useful evidence, then inspect neighboring moves or posts when the choice depends on a larger pattern.

## Candidate Recipe

Build every ledger candidate in this order:

```text
Observed content choice -> post evidence -> StoryScope-derived hypothesis
-> intent relationship -> keep/revise alternative -> trade-off -> recommendation
```

Include a plausible reason to keep the current choice. If the only argument for change is that a hook, list, CTA, phrase, or post shape is common, do not create an entry. Prefer one upstream post- or series-level entry over several sentence-level duplicates.

Apply Inception's baseline meta-intent without asking the user to restate it. Do not infer authorship. Do not force slang, informality, errors, emotional disclosure, personal stories, or an invented brand personality as evidence of natural writing.

## Semantic Levels and Post Records

Use three semantic levels:

```text
Post purpose -> Rhetorical move -> Information-bearing content
```

Establish the social context under `intent.constraints`:

```yaml
post_type: personal | brand | community
platform: LinkedIn
relationship: peer | expert-to-practitioner | brand-to-customer | community-member
purpose: inform | share | reflect | discuss | announce | teach | invite
primary_point: A small migration exposed an assumption in our rollback plan.
desired_response: Compare similar operational assumptions with peers.
must_preserve:
  - the migration result
  - the actual limitation of the test
must_avoid:
  - presenting one incident as universal evidence
```

Represent each material move by its function, such as `hook`, `setup`, `event`, `claim`, `example`, `analogy`, `qualification`, `takeaway`, `recap`, or `call_to_action`. Add another function only when these terms cannot express what the move contributes.

Do not require every post to contain every move. A brief observation, announcement, question, or image caption may already fulfill its purpose without a hook, lesson, summary, or CTA.

## Upstream Post Pass

Before creating local entries, map every appearance of the primary point and supporting ideas across the post or thread. For each hook, setup, claim, example, analogy, takeaway, recap, and CTA, ask what new information or relationship it contributes.

Treat a move as information-bearing when it adds at least one of the following:

- an event, observation, or evidence item;
- context needed to interpret another move;
- a distinct viewpoint or affected party;
- a constraint, qualification, or uncertainty;
- an action or response that follows from the post's purpose.

If several moves repackage the same point without adding one of these functions, treat the cluster as one upstream candidate. Do not assume that brevity is better: repetition may support accessibility, emphasis, thread navigation, an announcement requirement, or a deliberate recurring format.

## Diagnostic Axes

### 1. Speaker and Actor Agency

**StoryScope source: Agent.** Transfer questions about character role, motivation, introduction, and agency into questions about who speaks, who acts, and whose experience supplies the post's material.

Ask whether the named people, brand, team, customers, or community members can materially affect what happens, or whether they exist mainly to validate the primary point. Distinguish observed action from traits or motives assigned by the speaker.

Suspected default: the author or brand owns all insight and agency, while other people appear only as beneficiaries, obstacles, or anonymous proof.

The common choice can serve intent in first-person reflection, owner-specific announcements, or posts whose evidence genuinely comes from one actor.

### 2. Audience Relationship Structure

**StoryScope source: Social Networks.** Transfer questions about relationship topology, group emphasis, and social trajectories into the relationship the post constructs with its audience.

Ask whether the post addresses peers, practitioners, customers, followers, or community members as participants with distinct knowledge and incentives. Check whether interaction is genuinely invited or merely staged to reinforce the speaker's authority.

Suspected default: the speaker teaches a uniform audience that has no credible knowledge, disagreement, or role beyond agreement and engagement.

The common choice can serve intent in direct instructions, service notices, or posts for a narrowly defined novice audience.

### 3. Event and Causal Continuity

**StoryScope source: Events.** Transfer questions about event selection, causal chains, escalation, and event diversity into the incidents and evidence used by the post.

Ask whether observations, actions, outcomes, and claims form a continuous chain because the source material supports it. Identify omitted conditions or external causes before recommending a more complex account.

Suspected default: one incident becomes a frictionless sequence from problem to insight to result, with every detail serving the same lesson.

The common choice can serve intent in concise incident summaries, chronological announcements, or posts reporting a well-established mechanism.

### 4. Rhetorical Arc and Resolution

**StoryScope source: Plot.** Transfer questions about plot integration, protagonist-driven resolution, thematic unity, and resolution mode into the post's rhetorical progression.

Ask what the hook, development, takeaway, and CTA actually resolve: uncertainty, interpretation, action, identity, or nothing at all. Check whether secondary ideas introduce useful contrast or are forced to confirm one central message.

Suspected default: every post moves from a clean problem through three supporting points to a personal or brand insight that resolves all introduced tension.

The common choice can serve intent in announcements, instructions, event recaps, or posts designed around one explicit decision.

### 5. Thematic Explicitness and Reader Address

**StoryScope source: Situatedness.** Transfer thematic explicitness, moralizing, narratorial commentary, intertextual engagement, and direct reader address into how the post states its meaning and positions the reader.

Ask whether the event, example, and claim already establish the point before a takeaway, brand declaration, or CTA explains it again. Inspect whether direct address creates a real relationship or supplies generic engagement language.

Suspected default: the hook announces the lesson, the body demonstrates it, the takeaway names it again, and the CTA asks the reader to repeat or endorse it.

The common choice can serve intent when the post communicates policy, safety, advocacy, education, or a brand position that must be explicit.

### 6. Context as Grounding or Psychological Mirror

**StoryScope source: Setting.** Transfer questions about physical grounding, sensory density, and setting as a psychological mirror into the context surrounding the post's event or claim.

Ask whether platform, place, occasion, objects, and sensory details locate the event or supply evidence. Distinguish functional context from atmosphere used mainly to intensify emotion or symbolize the takeaway.

Suspected default: weather, coffee, a late-night office, or a conference scene mirrors the speaker's emotional state without changing the reader's understanding of the event.

The common choice can serve intent in place-based reporting, event coverage, personal reflection, hospitality, travel, or work where atmosphere is part of the subject.

### 7. Temporal Arrangement

**StoryScope source: Temporal Structure.** Transfer narrative order, duration, frequency, retrospection, and chronological discontinuity into how the post arranges time.

Ask whether the post must proceed from background to event to lesson, or whether the purpose is better served by beginning with an observation, present consequence, later qualification, or retrospective comparison. Do not reward nonlinearity by itself.

Suspected default: every post narrates a complete chronological journey even when only one current observation matters.

The common choice can serve intent in progress reports, launches, incident timelines, transformations, or any post where sequence is evidence.

### 8. Information Revelation and Recontextualization

**StoryScope source: Revelation.** Transfer questions about disclosure timing, expectation, surprise, and reinterpretation into when the post reveals its primary point and supporting context.

Ask whether later information changes the meaning of an earlier statement or merely repeats it with more emphasis. Distinguish useful withholding from a curiosity gap that over-promises what the post later supplies.

Suspected default: the hook withholds a fully formed lesson, while the remaining post delays and then restates the same conclusion without recontextualizing it.

The common choice can serve intent when suspense, staged explanation, a thread reveal, or a sensitive announcement requires controlled disclosure.

### 9. Perspective and Authority Position

**StoryScope source: Perspective.** Transfer questions about focalization, narrator presence, distance, and speech balance into the post's knowledge position and authority.

Ask whose perspective governs the post and which statements come from direct experience, organizational knowledge, professional judgment, reported testimony, or inference. Check whether these positions are collapsed into one uniformly authoritative voice.

Suspected default: a personal observation, team result, and universal recommendation are presented with the same degree of certainty and ownership.

The common choice can serve intent when authority and evidence are established elsewhere, the account speaks in an official capacity, or brevity makes the source boundary obvious.

### 10. Cross-Dimensional Over-Determination and Convergence

**StoryScope source: cross-dimensional findings.** Transfer the paper's findings about thematic over-determination, structural streamlining, single-track construction, and lower narrative diversity into a whole-post profile. This is not a tenth narrative-only taxonomy dimension and must not be represented as one.

Ask whether several dimensions converge on the same highly resolved treatment: one authoritative speaker, one passive audience, one causal chain, one lesson, one emotional frame, and one generic response. Inspect whether hook, example, analogy, takeaway, recap, and CTA repeatedly package the same idea without adding information-bearing content.

Suspected default: the post is structurally comprehensive beyond its purpose, with every move closing the same interpretation and leaving no material distinction between explanation, summary, and invitation.

The common choice can serve intent in campaign statements, onboarding sequences, recurring educational formats, accessibility-oriented posts, or messages that must remain intelligible when excerpts circulate alone.

Do not convert this axis into a novelty score. StoryScope reports overlapping tendencies across dimensions and does not establish any single feature as a universal authorship or quality test.

## Cross-Post Audit

After local candidates are found, check:

- whether several entries arise from one upstream purpose or content-selection decision;
- whether the speaker, evidence source, and authority position remain consistent;
- whether a thread installment or series post adds a distinct function;
- whether the same primary point is repeatedly packaged as hook, lesson, recap, and CTA;
- whether multiple examples or analogy families contribute different evidence or viewpoints;
- whether platform conventions enable comprehension or merely fill a familiar template;
- whether a CTA follows from the desired response or exists by default;
- whether a short post without a takeaway or CTA already fulfills its intent;
- whether an unusual alternative would violate factual accuracy, brand stance, community expectations, accessibility, or platform constraints.

Merge duplicates into the highest useful scope. Record dependencies before human review.

## Revision Priorities

For every accepted revision, use this default priority order unless the social-copy Intent Contract requires a different trade-off:

1. Preserve facts, source boundaries, brand position, real personal experience, necessary limitations, and platform constraints.
2. Decide the primary task the post must perform and preserve the moves that directly serve it.
3. Merge hooks, takeaways, recaps, or CTAs that repeat the same interpretation without adding a distinct reader action.
4. Consolidate examples and analogy families when they perform the same explanatory job.
5. Keep hashtags, emoji, thread numbering, recurring formats, and CTA conventions when they serve navigation, accessibility, identity, or the desired response.
6. Re-check speaker authority, audience relationship, causal support, and the Intent Contract after revision.

Do not substitute synonyms, force conversational phrasing, add slang or mistakes, manufacture urgency, or invent lived experience as a proxy for structural revision.

## Recommendation Calibration

- `keep`: the choice serves the post's purpose or relationship, and its familiarity is not a problem.
- `revise`: a concrete alternative improves evidence alignment, selectivity, authority boundaries, or audience response at acceptable cost.
- `remove`: a move performs no needed informational, relational, or navigational function and weakens another intent constraint.
- `investigate`: evidence, brand authority, personal experience, platform context, or audience need is missing.

Prefer a small number of material candidates over a catalogue of social-writing conventions.

## Excluded Concerns

Do not use this adapter for paid ads, targeting, bidding, conversion optimization, ad-platform policy, visual design, image or video direction, scheduling, or algorithm speculation. Do not fabricate personal, employee, customer, or community stories. Hand these concerns to an appropriate advertising, design, research, or publishing workflow outside this skill.

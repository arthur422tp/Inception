# Fiction Adapter

## Contents

- Scope and evidence
- Candidate recipe
- StoryScope feature aggregation
- Diagnostic axes
- Cross-scene audit
- Revision priorities
- Recommendation calibration

## Scope and Evidence

Audit narrative decisions, not literary worth in the abstract. StoryScope findings describe population tendencies and supply hypotheses for inspection; they are not thresholds, prohibitions, or proof of AI authorship.

Before a fiction audit, read [storyscope-features.md](storyscope-features.md) completely. Use it as the feature registry and evidence layer alongside this adapter. The existing ten Diagnostic Axes remain the human-readable, intent-facing architecture; the 30 features are atomic inspection cues and do not replace those axes.

Evaluate choices at document, section, scene, and passage scope. Cite the smallest passage that demonstrates the choice, then check its earlier setup and later consequences when necessary.

## Candidate Recipe

Build every ledger candidate in this order:

```text
Observed choice → draft evidence → suspected default → intent relationship
→ keep/revise alternative → trade-off → recommendation
```

Include a plausible reason to keep the current choice. If the only argument for change is that a choice is common, do not create an entry.

Apply Inception's baseline meta-intent through observable narrative decisions without asking the user to restate it. Do not infer authorship. Do not treat genre conventions, linear chronology, closure, explicit emotion, or familiar imagery as defects by themselves.

## StoryScope Feature Aggregation

Inspect the registry features in this order:

```text
30 atomic features
  → co-occurring configuration or cluster
  → upstream narrative decision
  → relationship to Intent Contract
  → materiality check
  → Decision Ledger candidate
```

Do not turn every detected feature into a ledger entry or scan for 30 warnings. First cluster co-occurring features, deduplicate overlapping observations, and synthesize the upstream narrative decision they may express. When several features arise from one authorial choice, merge them into one candidate at the highest useful scope. When one feature appears in multiple places but performs the same narrative function, prefer one cross-scene or whole-story candidate. A single feature may stand alone only when it already creates a material conflict with the Intent Contract. If evidence is insufficient, intent relevance is absent, or the only reason to flag the choice is a population tendency, do not create an entry.

For example:

```text
thematic explicitness
+ narratorial thematic commentary
+ philosophical dialogue
+ unusually unified subplot functions
→ possible upstream decision:
  the story repeatedly closes interpretive space around one stated lesson
```

This cluster still requires an Intent Contract and a materiality check. For a fable, teaching story, children’s story, or deliberately blunt satire, the credible recommendation may be `keep`.

Treat familiar structure as a choice, not a defect. Linear chronology, explicit emotion, named references, ambiguity, subplots, direct reader address, and other registry values may all serve the work. Do not mechanically add nonlinear chronology, moral ambiguity, fourth-wall breaks, subplots, explicit references, or more locations to increase dispersion. Do not use synonym replacement, deliberate roughening, forced informality, or an invented personal voice as a substitute for changing a narrative decision.

## Diagnostic Axes

### 1. Thematic Explicitness and Over-Determination

Ask whether events, images, character choices, and dialogue already carry the theme before the narrator explains it. Test whether removing the explanation would create productive interpretive space or merely hide necessary context.

Suspected default: the draft closes every thematic inference with a lesson, philosophical summary, or dialogue that restates the same meaning.

The common choice can serve intent when the genre is fable, instruction, satire with deliberate bluntness, or a story designed for readers who need explicit framing.

### 2. Causal Linearity and Protagonist-Driven Resolution

Ask whether the event chain is linear because clarity matters or because no alternative causality was considered. Inspect what actually resolves the central pressure: protagonist choice, collective action, accident, institution, environment, time, or unresolved conflict.

Suspected default: each event causes the next cleanly and the protagonist's final decision resolves every major thread.

The common choice can serve intent in adventure, procedural, children's fiction, tragedy driven by a decisive flaw, or any story promising strong causal momentum.

### 3. Chronology, Disclosure, and Recontextualization

Ask when the reader receives crucial context and whether later information changes the meaning of earlier events. Distinguish genuine recontextualization from withholding a fact solely to manufacture a twist.

Suspected default: chronological narration front-loads explanatory backstory and revelations add facts without changing prior interpretation.

The common choice can serve intent when temporal clarity, suspense through anticipation, oral-story cadence, or an inexorable sequence is central.

### 4. Subplot Absence, Integration, and Independence

Ask whether secondary threads introduce pressure, contrast, resonance, or competing values. A subplot should have a job beyond delaying the main plot.

Suspected default: the story removes every thread not directly advancing the protagonist's goal, or makes every subplot mirror the same theme too neatly.

The common choice can serve intent in short forms, compressed thrillers, chamber pieces, monologues, or any work whose force depends on concentration.

### 5. Ambiguity, Closure, and Resolution Mechanism

Ask what is resolved—external problem, relationship, self-understanding, moral judgment, or reader uncertainty—and which uncertainty should remain active after the ending.

Suspected default: reconciliation, acceptance, revelation, or a final explanatory image closes conflict and interpretation simultaneously.

The common choice can serve intent in romance, restorative narratives, cathartic comedy, genre promises requiring solution, or stories meant to comfort.

### 6. Character Agency and Moral Complexity

Ask which characters can materially alter events, what each risks, and whether opposing positions have intelligible motives. Do not equate moral ambiguity with depth automatically.

Suspected default: one protagonist owns meaningful agency while supporting characters confirm the protagonist's growth; moral conflict collapses into a clear lesson.

The common choice can serve intent in myth, allegory, farce, heroic fantasy, or a tightly focalized account where asymmetrical agency is deliberate.

### 7. Emotional Presentation

Ask how emotion becomes knowable: action, bodily sensation, direct label, dialogue, omission, contradiction, rhythm, or another character's interpretation. Look for repetition that stops carrying new information.

Suspected default: each emotional beat arrives through tightening throats, pounding hearts, trembling hands, held breath, or environmental mirroring.

The common choice can serve intent when embodiment is thematically central, the viewpoint is highly somatic, panic changes action, or a repeated bodily cue accumulates meaning.

### 8. Sensory Detail and Atmosphere

Ask what each prominent sensory detail does: locate action, create evidence, trigger memory, shape attention, establish danger, or build atmosphere. Decorative density is a decision only when it affects reading.

Suspected default: smell, weather, light, and texture recur as generic mood intensifiers without changing perception or action.

The common choice can serve intent in lyric fiction, horror, place-centered stories, altered-state narration, or scenes where atmosphere is itself the dramatic pressure.

### 9. Intertextual Specificity and Reader Awareness

Ask whether allusions, genre expectations, direct address, and narrator-reader relations have a precise rhetorical function. Do not demand references merely to appear cultured.

Suspected default: the story uses vague mythic or literary echoes while maintaining a transparent narrator who never acknowledges how the reader is positioned.

The common choice can serve intent when immersion, timelessness, accessibility, or an effaced narrator is part of the contract.

### 10. Structural Repetition Across Scenes

Ask whether scenes repeatedly perform the same sequence—setup, conflict, explanation, emotional reaction, mini-resolution—or whether repetition creates escalation, ritual, contrast, or entrapment.

Suspected default: scene architecture changes names and settings while preserving the same rhetorical work and outcome.

The common choice can serve intent in ritual structures, comedy with variation, episodic forms, procedural narratives, or deliberate cycles whose differences matter.

## Cross-Scene Audit

After feature clustering and local candidates are found, check:

- whether feature observations have been clustered and deduplicated before candidate synthesis;
- whether multiple features are consequences of one upstream narrative decision;
- whether two entries describe one upstream structural decision;
- whether changing one scene would break setup or payoff elsewhere;
- whether apparent repetition is escalation or redundancy;
- whether a proposed unusual alternative violates genre, audience, length, or desired-effect constraints.

Merge duplicates into the highest useful scope. Record dependencies before human review, and return only material decisions rather than a feature inventory.

## Revision Priorities

For every accepted revision, use this default priority order unless the fiction Intent Contract requires a different trade-off:

1. Preserve genre promises, plot facts, established point of view, character relationships, setup and payoff, and the required emotional effect.
2. Address upstream choices such as over-explained themes, tidy closure that exceeds the intended resolution, single-track causality, or repeated scene functions before changing prose texture.
3. Consolidate bodily cues, sensory details, imagery, or metaphor families only when repeated instances perform the same narrative or emotional work.
4. Keep familiar structure when it serves the audience or genre; do not force ambiguity, subplots, moral complexity, nonlinear chronology, or unusual imagery merely to appear less model-default.
5. Re-check continuity, causality, character agency, setup, payoff, and the Intent Contract after revision.

Do not substitute synonyms, deliberately roughen prose, force informality, or invent autobiographical texture or personal voice as a proxy for narrative revision.

## Recommendation Calibration

- `keep`: the choice serves intent and its familiarity is not a problem.
- `revise`: a concrete alternative serves intent better at acceptable cost.
- `remove`: the choice contributes no necessary function and weakens another intent constraint.
- `investigate`: evidence, source material, or author preference is missing.

Prefer a small number of material candidates over a catalogue of every recognizable tendency.

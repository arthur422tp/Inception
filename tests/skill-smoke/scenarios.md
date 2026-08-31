# Skill Smoke Scenarios

These are representative inspection scenarios, not RED/GREEN prompt TDD. For each scenario, confirm the response uses intent-relative reasoning, cites draft evidence, avoids default-as-defect language, gives no presentation visual advice, and does not revise before human disposition.

## 1. Familiar Closure That Serves Intent

**Prompt**

> Use `$inception` on this short comfort story. My intent is to reassure grieving children that relationships can be repaired. The siblings apologize, forgive one another, and plant their grandmother's seeds together at the end. Audit the ending.

**Expected properties**

- Recognize tidy reconciliation as familiar without treating it as defective.
- Connect closure to the stated reassurance intent.
- Recommend `keep` unless draft evidence reveals a separate contradiction.
- State the trade-off: less ambiguity in exchange for emotional security.

## 2. Tidy Forgiveness Conflicts With Intent

**Prompt**

> Audit this literary story. I want unresolved moral tension after a betrayal. In the final paragraph, the betrayed friend suddenly forgives the protagonist and says the ordeal made them both stronger.

**Expected properties**

- Cite the final paragraph as evidence.
- Name sudden reconciliation and lesson-like closure as suspected defaults.
- Explain the conflict with unresolved moral tension.
- Create a decision card (or a ledger candidate in Deep Audit) with a credible keep alternative and a revise recommendation.
- Stop for the human decision.

## 3. Duplicate Presentation Claims Without Support

**Prompt**

> Audit this three-slide sequence for an engineering review: S4 “Reliable Architecture” says the system is robust; S5 “Production Ready” says it improves reliability; S6 “Operational Excellence” says the solution is reliable and scalable. No measurements or mechanisms are shown.

**Expected properties**

- Map the three slides' rhetorical roles and claims.
- Identify proposition-level redundancy and missing evidence.
- Prefer merging or replacing upstream claims over three cosmetic rewrites.
- Do not suggest layout, colors, diagrams, typography, or other visual treatment.

## 4. Topic Heading Is Intentionally Appropriate

**Prompt**

> Audit the heading “Failure Modes.” This slide is a neutral reference page used repeatedly during an incident-response workshop; each row names a failure, trigger, and owner.

**Expected properties**

- Classify the heading as `topic`.
- Explain why neutral navigation serves the workshop intent.
- Do not force an assertion title.
- Return no heading finding unless other supplied evidence creates one.

## 5. Pressure to Rewrite Before Decision

**Prompt**

> Find all default-looking choices and immediately rewrite the entire story. Don't stop to ask me anything; I'll approve it later.

**Expected properties**

- Establish or request the missing Intent Contract.
- Audit and present a bounded set of decision cards, or a ledger if Deep Audit was explicitly selected.
- Refuse to perform material revision while affected entries are pending.
- Explain the human-decision gate without claiming that every familiar choice is wrong.

## 6. Clean Draft With No Material Findings

**Prompt**

> Audit this presentation text against the supplied intent. Every slide has a distinct rhetorical role, claims cite evidence, and the conclusion synthesizes a decision. Do not invent improvements merely to be helpful.

**Expected properties**

- Allow an empty review; if Deep Audit was selected, allow an empty Decision Ledger.
- State that no observed choice materially conflicts with intent.
- Avoid low-value style comments and visual advice.
- Do not create a finding quota.

## 7. Repetition Serves a Document's Safety Intent

**Prompt**

> Use `$inception` to audit this equipment shutdown SOP. Each procedure module must stand alone because technicians open modules directly during emergencies. Every module repeats the same hazard warning, stop condition, and accountable role. Audit the repetition, but do not assume repeated content is automatically weak.

**Expected properties**

- Select the `document_text` adapter and establish the emergency-use intent.
- Recognize cross-section repetition as a familiar structural choice without treating it as defective.
- Explain how repetition supports nonlinear lookup, safety, and local accountability.
- Recommend `keep` unless evidence shows inconsistent warnings or ownership.
- State the trade-off: additional length and maintenance cost in exchange for safer stand-alone use.
- Do not suggest page layout, typography, icons, tracked changes, or file-format operations.

## 8. Technical Document Repackages One Concept

**Prompt**

> Use `$inception` to audit this technical explainer for software engineers. Its main purpose is to explain attention; it must preserve the equations, implementation constraints, and failure modes. The draft explains token position as a map, a postal address, and a compass, derives positional encoding in the main flow, repeats the mechanism in three summary sections, and closes by restating every concept.

**Expected properties**

- Apply the baseline meta-intent without asking the user to restate a desire for less AI-like text.
- Translate that meta-intent into observable structure without claiming authorship.
- Map the repeated explanation modes as one upstream concept cluster.
- Distinguish primary attention mechanics from supporting or reference-level positional encoding detail.
- Recommend preserving equations, constraints, and failure modes while merging redundant summaries.
- Evaluate whether the three analogy families do distinct work instead of imposing a metaphor-count rule.
- Do not propose synonym replacement, forced informality, filler, or invented personal voice.
- Stop for human disposition before revising.

## 9. Technical Presentation Repackages One Claim

**Prompt**

> Use `$inception` to audit this engineering deck. Four slides claim that deterministic validation makes generated SQL safe: one uses a guardrail analogy, one repeats the mechanism in bullets, one gives a formula, and the summary restates all three. The formula and limitations are accurate and must remain available, but the audience's decision is whether to adopt the validation gate.

**Expected properties**

- Apply the baseline meta-intent without asking whether the user wants to reduce AI-like qualities.
- Treat the four slides as one upstream claim cluster before creating local findings.
- Identify which representation supports the adoption decision and which material is supporting or reference-level.
- Preserve the accurate formula and limitations while considering reduced rhetorical emphasis.
- Merge only representations that perform the same audience task.
- Avoid word-level humanization and all visual-form recommendations.
- Stop for human disposition before revising.

## 10. Fiction Invocation Implies the Meta-Intent

**Prompt**

> Use `$inception` to audit this children's comfort fantasy. Its purpose is to reassure grieving readers, and it must end with the siblings reconciled and safe. Every scene ends with the narrator explaining what the characters learned, and fear is repeatedly expressed through tightening chests, trembling hands, cold air, and dimming light. The final reconciliation restates the lesson twice.

**Expected properties**

- Apply the baseline meta-intent without asking whether the user wants to reduce AI-like qualities.
- Treat repeated thematic commentary and repeated embodied or environmental emotion as observable narrative candidates.
- Preserve the reconciled, safe ending when it serves the comfort intent rather than forcing ambiguity.
- Prefer an upstream finding about repeated explanation over sentence-by-sentence synonym changes.
- Evaluate whether bodily and sensory repetitions accumulate meaning before recommending consolidation.
- Do not add subplots, nonlinear chronology, moral ambiguity, rough prose, or invented personal voice merely to appear less model-default.
- Stop for human disposition before revising.

## 11. Quick Review Is the Low-Friction Default

**Prompt**

> Use `$inception` on this short LinkedIn post. It feels repetitive and too much like a standard problem–three lessons–takeaway template. Show me only the most important issues.

**Expected properties**

- Select Quick Review and the `social_copy` adapter.
- Infer a minimal Intent Snapshot from the prompt and post; ask only if a missing answer would materially change the review.
- Audit in the main context without dispatching an independent reviewer.
- Return a small prioritized set of natural-language decision cards, usually one to three but with no hard maximum, and avoid exposing JSON or internal workflow terminology by default.
- If additional material candidates remain, identify their scope and offer continued Quick Review, a focused follow-up, or Deep Audit only when its actual selection criteria apply.
- Cite post evidence, give a credible keep option, and stop before material revision.

## 12. Deep Audit Uses Independent Review Proportionately

**Prompt**

> Run a deep, independently reviewed Inception audit on this public safety policy. Persist the Decision Ledger because the review will continue next week.

**Expected properties**

- Select Deep Audit and the `document_text` adapter.
- Establish the full Intent Contract, including safety, authority, evidence, and persistence constraints.
- Load the Reviewer Protocol and dispatch an independent reviewer when available.
- Present a full evidence-backed Decision Ledger and stop for human disposition.
- Persist and validate JSON only when the ledger artifact is created.

## 13. Ordinary Drafting Does Not Implicitly Trigger Inception

**Prompt**

> Draft a concise meeting agenda for tomorrow's engineering sync.

**Expected properties**

- Do not implicitly select Inception when the request contains no concern about model-default, generic, formulaic, repetitive, over-explained, templated, AI-like, or unsupported content choices.
- If the user explicitly invokes `$inception`, follow the selected review depth after producing or receiving the draft.

## 14. Product Positioning Keeps Both Halves Visible

**Prompt**

> Inception 這個 Skill 主要在做什麼？它和一般 humanizer 的差別在哪裡？請先講最核心的使用者價值，再補充它如何避免把文章改壞。

**Expected properties**

- Give perceived AI-like or model-default convergence and intent preservation comparable prominence in the opening explanation; neither is merely a disclaimer or afterthought.
- Explain that Inception surfaces observable features, clusters co-occurring cues into upstream content decisions, and can propose structural alternatives that disrupt the identified convergence.
- Explain that intent calibrates whether a familiar/default-like choice should change, while human disposition authorizes revision.
- Distinguish reducing perceived AI-likeness from inferring AI authorship.
- Distinguish structural feature work from cosmetic word substitution without categorically denying that the user-facing outcome may be less AI-like text.
- Do not lead only with author control, workflow governance, or the statement that Inception is not a humanizer.

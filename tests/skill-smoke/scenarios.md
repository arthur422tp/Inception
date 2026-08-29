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
- Create a ledger candidate with a credible keep alternative and a revise recommendation.
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
- Audit and present a bounded ledger.
- Refuse to perform material revision while affected entries are pending.
- Explain the human-decision gate without claiming that every familiar choice is wrong.

## 6. Clean Draft With No Material Findings

**Prompt**

> Audit this presentation text against the supplied intent. Every slide has a distinct rhetorical role, claims cite evidence, and the conclusion synthesizes a decision. Do not invent improvements merely to be helpful.

**Expected properties**

- Allow an empty Decision Ledger.
- State that no observed choice materially conflicts with intent.
- Avoid low-value style comments and visual advice.
- Do not create a finding quota.

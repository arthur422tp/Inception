---
name: inception
description: Use when users ask to make fiction, presentations, documents, or organic social posts less AI-like, less generic, less templated, less formulaic, less repetitive, or less over-explained, or when claim strength may exceed the evidence. Also use for audits of model-default content choices. Do not use for authorship detection or ordinary drafting without these concerns.
---

# Inception

## Core Principle

Treat defaults as candidates, not defects. Let the author's intent—not rarity, novelty, or an AI-writing stereotype—decide whether a choice should remain.

Diagnose content decisions rather than disliked words. Make an implicit choice visible, explain its effect, and return authority to the human.

Invoking Inception establishes a baseline meta-intent to reduce perceived model-default or AI-like convergence in content decisions. Do not ask the human to restate that goal. Operationalize it through observable choices such as selective emphasis, proportionate explanation, and nonredundant representation—not through authorship claims, default-as-defect rules, word substitution, forced informality, or invented personal voice. This meta-intent does not authorize revision or override the domain Intent Contract; preserve factual accuracy, technical constraints, and necessary detail unless the human explicitly accepts a trade-off.

StoryScope features are atomic inspection cues. Inception groups them into intent-relevant narrative decisions before anything reaches human review.

## Select Review Depth

Default to Quick Review. Use Deep Audit when the user asks for a deep, full, exhaustive, independent, or persisted review; when the artifact is long enough that cross-unit dependencies are central; or when safety, compliance, policy, public claims, or another high-stakes constraint makes an independent audit proportionate. Never select Deep Audit merely because subagents are available. Do not select Deep Audit based on candidate count alone.

State the selected depth in one short sentence when it affects latency, output, or reviewer use. Follow an explicit user choice.

## Quick Review

Use Quick Review for ordinary drafts, excerpts, posts, slide sequences, and focused questions.

1. Read [references/core-workflow.md](references/core-workflow.md) and exactly one domain adapter from the routing list below.
2. Infer a minimal Intent Snapshot from the request and draft. Ask only when a missing answer could materially change the review.
3. Audit in the main context. Return a small prioritized set of decision cards, usually one to three, with no hard maximum. If additional material candidates remain, briefly identify their scope and offer to continue Quick Review, run a focused follow-up, or switch to Deep Audit when its actual selection criteria apply. Never suppress a material finding to preserve the usual count.
4. Present each card in natural language: current choice, evidence, intent relevance, credible keep/change options, trade-off, and recommendation. Do not expose JSON or internal workflow terminology unless useful to the user.
5. Stop for the human's decisions before material revision.
6. Apply only accepted or modified actions, then run a same-agent Regression Check over the authorized scope and affected intent constraints.

Quick Review is not a shortcut around evidence or human authority. It changes review depth and presentation, not the decision gate.

## Deep Audit

Use Deep Audit for long, high-stakes, explicitly independent, or persisted reviews.

1. Read [references/core-workflow.md](references/core-workflow.md), [references/reviewer-protocol.md](references/reviewer-protocol.md), and exactly one domain adapter from the routing list below.
2. Establish the full Intent Contract and resolve material open questions.
3. For fiction, also read the complete [StoryScope feature registry](references/storyscope-features.md).
4. Dispatch an independent reviewer when available. If none is available, perform a clearly identified same-agent fallback; never simulate independence.
5. Present the evidence-backed Decision Ledger and stop for human disposition.
6. Apply only accepted or modified actions in the main-agent role.
7. Run the Regression Audit through the reviewer protocol and present its result before any additional revision pass.

## Domain Routing

Select exactly one adapter and read it completely:

- Fiction, story, scene, or narrative → [references/fiction-adapter.md](references/fiction-adapter.md)
- Deck, slide, presentation copy, or speaker-facing argument → [references/presentation-text-adapter.md](references/presentation-text-adapter.md)
- Report, proposal, memo, specification, policy, SOP, or other sustained document text → [references/document-text-adapter.md](references/document-text-adapter.md)
- Organic brand or personal social post, caption, thread, or post series → [references/social-copy-adapter.md](references/social-copy-adapter.md)

For an unsupported domain, explain that no adapter exists and stop. Do not borrow the nearest adapter's assumptions.

## Output Contract

Keep findings bounded and prioritized. Every decision card or ledger entry must connect an observed choice and draft evidence to a suspected default, intent relevance, alternatives, trade-offs, and a recommendation. An empty review is valid.

When a Deep Audit ledger is persisted, save JSON and run:

```bash
python scripts/validate_ledger.py <ledger.json>
```

Fix every reported invariant violation before revision.

## Hard Boundaries

- Inception is not an AI detector or a humanizer.
- Do not classify authorship or claim that a draft is AI-generated.
- Do not use vocabulary blacklists or cosmetic “humanization”; do not substitute them for narrative decisions.
- Do not treat StoryScope population tendencies as quality rules.
- Do not auto-rewrite material decisions before human disposition.
- Do not give presentation advice about typography, color, spacing, grid, alignment, visual hierarchy, icons, illustrations, slide masters, or visual style.
- Do not give document advice about page layout, typography, margins, pagination, tracked changes, comments, or file-format mechanics.
- Do not give social-copy advice about paid ads, targeting, bidding, visual design, scheduling, or algorithm speculation.

---
name: inception
description: Use when users ask to make fiction, presentations, documents, or organic social posts less AI-like, less generic, less templated, less formulaic, less repetitive, or less over-explained, or when claim strength may exceed the evidence. Also use for audits of model-default content choices. Do not use for authorship detection or ordinary drafting without these concerns.
---

# Inception

## Core Principle

Balance two equal responsibilities:

- **Deconvergence:** identify observable model-default features, cluster cues that perform the same work, explain how the cluster contributes to perceived AI-like convergence, and offer a credible structural way to disrupt it when material.
- **Intent preservation:** compare that cluster with the author's intent, preserve factual and domain constraints, include a credible reason to keep the choice, and leave every material revision to human disposition.

Neither responsibility is a disclaimer or an afterthought. A useful finding makes both visible:

```text
observable feature cues
  → co-occurring cluster
  → AI-like convergence effect
  → upstream content decision
  → relationship to author intent
  → keep and pattern-disrupting alternatives
  → human decision
```

Invoking Inception establishes the baseline goal of reducing perceived model-default or AI-like convergence without sacrificing intent. Do not ask the human to restate either half. Treat defaults as candidates, not defects: familiarity alone never decides whether a choice should remain. Diagnose content decisions rather than disliked words, and do not substitute word replacement, forced informality, or invented personal voice for structural change.

StoryScope features are atomic inspection cues. Inception groups them into intent-relevant narrative decisions while preserving a concise feature-to-cluster trace for human review.

## Select Review Depth

Default to Quick Review. Use Deep Audit when the user asks for a deep, full, exhaustive, independent, or persisted review; when the artifact is long enough that cross-unit dependencies are central; or when safety, compliance, policy, public claims, or another high-stakes constraint makes an independent audit proportionate. Never select Deep Audit merely because subagents are available. Do not select Deep Audit based on candidate count alone.

State the selected depth in one short sentence when it affects latency, output, or reviewer use. Follow an explicit user choice.

## Quick Review

Use Quick Review for ordinary drafts, excerpts, posts, slide sequences, and focused questions.

1. Read [references/core-workflow.md](references/core-workflow.md) and exactly one domain adapter from the routing list below.
2. Infer a minimal Intent Snapshot from the request and draft. Ask only when a missing answer could materially change the review.
3. Audit in the main context. Return a small prioritized set of decision cards, usually one to three, with no hard maximum. If additional material candidates remain, briefly identify their scope and offer to continue Quick Review, run a focused follow-up, or switch to Deep Audit when its actual selection criteria apply. Never suppress a material finding to preserve the usual count.
4. Present each card in natural language: feature cluster and convergence effect, current choice and evidence, intent relevance, credible keep/pattern-disrupting options, trade-off, and recommendation. Do not expose JSON or internal workflow terminology unless useful to the user.
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

Keep findings bounded and prioritized. Every decision card or ledger entry must use the existing fields to preserve both halves of the analysis: the observed feature cluster and its convergence effect, plus its relationship to intent. Alternatives must include a credible keep option and, when revision is recommended, a credible structural option that disrupts the identified pattern. An empty review is valid.

When a Deep Audit ledger is persisted, save JSON and run:

```bash
python scripts/validate_ledger.py <ledger.json>
```

Fix every reported invariant violation before revision.

## Hard Boundaries

- Inception is not an authorship detector or a cosmetic, word-level humanizer. Reducing perceived AI-likeness through content and structural change is in scope; inferring provenance is not.
- Do not classify authorship or claim that a draft is AI-generated.
- Do not use vocabulary blacklists or cosmetic “humanization”; do not substitute them for content or structural decisions.
- Do not treat StoryScope population tendencies as quality rules.
- Do not auto-rewrite material decisions before human disposition.
- Do not give presentation advice about typography, color, spacing, grid, alignment, visual hierarchy, icons, illustrations, slide masters, or visual style.
- Do not give document advice about page layout, typography, margins, pagination, tracked changes, comments, or file-format mechanics.
- Do not give social-copy advice about paid ads, targeting, bidding, visual design, scheduling, or algorithm speculation.

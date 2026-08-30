---
name: inception
description: Use when creating, auditing, or revising fiction, presentation text, document text, or organic brand and personal social posts where generic structure, tidy closure, unsupported claims, repeated content, template dependence, or other model-default choices may conflict with the author's intent.
---

# Inception

## Core Principle

Treat defaults as candidates, not defects. Let the author's intent—not rarity, novelty, or an AI-writing stereotype—decide whether a choice should remain.

Diagnose content decisions rather than disliked words. Make an implicit choice visible, explain its effect, and return authority to the human.

Invoking Inception establishes a baseline meta-intent to reduce perceived model-default or AI-like convergence in content decisions. Do not ask the human to restate that goal. Operationalize it through observable choices such as selective emphasis, proportionate explanation, and nonredundant representation—not through authorship claims, default-as-defect rules, word substitution, forced informality, or invented personal voice. This meta-intent does not authorize revision or override the domain Intent Contract; preserve factual accuracy, technical constraints, and necessary detail unless the human explicitly accepts a trade-off.

StoryScope features are atomic inspection cues. Inception groups them into intent-relevant narrative decisions before anything reaches the Decision Ledger.

## Required Workflow

1. Read [references/core-workflow.md](references/core-workflow.md) completely.
2. Read [references/reviewer-protocol.md](references/reviewer-protocol.md) completely.
3. Establish the Intent Contract before judging the draft.
4. Obtain the user's draft or help create an initial draft. Send both through the same later states.
5. Select exactly one adapter and read it completely:
   - Fiction, story, scene, or narrative → [references/fiction-adapter.md](references/fiction-adapter.md); also read the fiction adapter’s required [StoryScope feature registry](references/storyscope-features.md) completely.
   - Deck, slide, presentation copy, or speaker-facing argument → [references/presentation-text-adapter.md](references/presentation-text-adapter.md)
   - Report, proposal, memo, specification, policy, SOP, or other sustained document text → [references/document-text-adapter.md](references/document-text-adapter.md)
   - Organic brand or personal social post, caption, thread, or post series → [references/social-copy-adapter.md](references/social-copy-adapter.md)
6. If acting as the human-facing main agent, dispatch an independent audit reviewer when subagents are available. Otherwise perform a clearly identified same-agent fallback audit. Do not simulate an independent reviewer.
7. If explicitly dispatched as the audit reviewer, do not dispatch another reviewer. Audit observable choices against intent and return only the evidence-backed review result required by the reviewer protocol.
8. Present the ledger to the human and stop for decisions. Do not materially revise while any affected entry remains pending, rejected, or deferred.
9. Apply only accepted or modified actions in the main-agent role.
10. Run the Regression Audit through the reviewer protocol. Present its result to the human before any additional revision pass, and surface every new material trade-off for a human decision.

For an unsupported domain, explain that no adapter exists and stop. Do not borrow the nearest adapter's assumptions.

## Output Contract

Keep findings bounded and prioritized. Each entry must connect an observed choice and draft evidence to a suspected default, intent relevance, alternatives, trade-offs, and a recommendation. An empty ledger is valid.

When persisting a ledger, save JSON and run:

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

---
name: inception
description: Use when creating, auditing, or revising fiction, presentation text, or document text where generic structure, tidy closure, unsupported claims, repeated content, template dependence, or other model-default choices may conflict with the author's intent.
---

# Inception

## Core Principle

Treat defaults as candidates, not defects. Let the author's intent—not rarity, novelty, or an AI-writing stereotype—decide whether a choice should remain.

Diagnose content decisions rather than disliked words. Make an implicit choice visible, explain its effect, and return authority to the human.

## Required Workflow

1. Read [references/core-workflow.md](references/core-workflow.md) completely.
2. Establish the Intent Contract before judging the draft.
3. Obtain the user's draft or help create an initial draft. Send both through the same later states.
4. Select exactly one adapter and read it completely:
   - Fiction, story, scene, or narrative → [references/fiction-adapter.md](references/fiction-adapter.md)
   - Deck, slide, presentation copy, or speaker-facing argument → [references/presentation-text-adapter.md](references/presentation-text-adapter.md)
   - Report, proposal, memo, specification, policy, SOP, or other sustained document text → [references/document-text-adapter.md](references/document-text-adapter.md)
5. Audit observable choices against intent. Create only evidence-backed Decision Ledger entries.
6. Present the ledger and stop for human decisions. Do not materially revise while any affected entry remains pending, rejected, or deferred.
7. Apply only accepted or modified actions.
8. Run the Regression Audit against affected intent constraints and dependencies. Surface any new trade-off for a human decision.

For an unsupported domain, explain that no adapter exists and stop. Do not borrow the nearest adapter's assumptions.

## Output Contract

Keep findings bounded and prioritized. Each entry must connect an observed choice and draft evidence to a suspected default, intent relevance, alternatives, trade-offs, and a recommendation. An empty ledger is valid.

When persisting a ledger, save JSON and run:

```bash
python scripts/validate_ledger.py <ledger.json>
```

Fix every reported invariant violation before revision.

## Hard Boundaries

- Do not classify authorship or claim that a draft is AI-generated.
- Do not use vocabulary blacklists or cosmetic “humanization.”
- Do not treat StoryScope population tendencies as quality rules.
- Do not auto-rewrite material decisions before human disposition.
- Do not give presentation advice about typography, color, spacing, grid, alignment, visual hierarchy, icons, illustrations, slide masters, or visual style.
- Do not give document advice about page layout, typography, margins, pagination, tracked changes, comments, or file-format mechanics.

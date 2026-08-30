# Inception

[English](README.md) | [繁體中文](README.zh-TW.md)

> **A writing skill that reduces “AI-like” or model-default patterns while preserving the author's intent.**

Inception looks beyond word choice and tone. It asks a more upstream question: **what content choices did the draft make?**

It looks for decisions that may make writing feel overly polished, over-explained, predictable, repetitive, or more certain than the evidence supports.

It does not rewrite the whole draft as soon as it finds a possible issue.

Inception first tells you:

* what it noticed;
* why the choice may be worth examining;
* how it relates to your original intent;
* how you could change it;
* what the change might cost.

You decide which parts actually need to change.

The first release supports:

* fiction and narrative writing;
* presentation text, including deck argument, slide function, claims, and evidence;
* document text, including reports, proposals, memos, specifications, policies, SOPs, and research summaries;
* organic brand and personal social copy, including captions, posts, threads, and post series.

Inception works with **OpenAI Codex** and **Anthropic Claude Code**.

---

## What does Inception look for?

Many humanizers mainly operate on surface-level writing, such as:

* swapping words;
* changing sentence length;
* removing clichés;
* making the tone more conversational;
* making sentence patterns less regular.

These techniques can sometimes help.

But many features that make writing feel “AI-like” appear further upstream.

Inception looks beyond:

```text
How is this sentence written?
```

It also asks:

```text
Why was this choice made here?
Does this information need to be here?
Does this conclusion need to be this complete?
Does this point need to be made again?
Is the claim as certain as the evidence supports?
```

---

## Examples

### Fiction

Every conflict in a story is resolved through the protagonist's growth, understanding, and reconciliation, and the ending explicitly says what the protagonist “learned.”

Inception may point out:

* whether the ending is too neat;
* whether the theme is explained too completely;
* whether every conflict is being closed through the same resolution mechanism.

It does not decide that these patterns are wrong just because they are common in model outputs.

If the work is meant to be a fable, a healing story, or a story that needs clear closure, keeping them may be the right choice.

---

### Presentations

A presentation repeats the same conclusion across several slides and becomes increasingly certain, even though the evidence supports a more cautious claim.

Inception may point out:

* whether multiple slides are performing the same argument function;
* whether claim strength exceeds the evidence;
* whether the conclusion is stronger than the original intent.

---

### Documents

A proposal explains the same rationale again and again in the Executive Summary, Background, Recommendation, and Conclusion.

Inception does not just rewrite the four passages with different sentence patterns.

It first asks:

> Does this reason really need to be represented four times?

In other words, it checks the **representation decision**, not just the wording.

---

### Social copy

A post naturally falls into this familiar sequence:

```text
hook
→ problem
→ personal experience
→ three takeaways
→ positive takeaway
```

If the author's intent was a cooler, more observational voice without a clear conclusion, Inception may flag this familiar structure as a content choice worth reconsidering.

It does not force the writing to become conversational or deliberately messy just because it does not “sound human” enough.

---

## Why not use a regular humanizer?

Most humanizers mainly operate on:

```text
word choice
sentence structure
tone
register
```

Inception works further upstream:

```text
content selection
argument structure
narrative resolution
claim strength
repetition
emphasis
explanation
```

Inception is not trying to make every piece of writing unusual, strange, or unpredictable.

Familiar choices are not automatically bad.

Unusual choices are not automatically better.

The real question is:

> **Is this choice serving the author's intent, or is it simply the easiest default for a model to choose?**

For example:

* linear storytelling may be exactly what a children's story needs;
* a clear conclusion may be exactly what a policy document needs;
* repeating a key message in a presentation may be deliberate;
* a highly structured format may be exactly what an SOP needs.

Inception does not treat “common” as a synonym for “defective.”

It treats these patterns as **decision candidates worth examining**.

---

## How does it work?

From the user's perspective, the process is simple:

```text
Draft
  → Audit
  → You decide
  → Revision
  → Check
```

Inception first confirms:

> What is this piece of writing trying to achieve?

Only then does it examine the draft's content decisions.

If it finds important choices that may conflict with the intent, it returns them to you first.

You can:

* accept them;
* modify the recommendation;
* reject them;
* defer them.

Only decisions that you accept or modify can enter revision.

After the revision, Inception checks again:

* whether the approved change was applied correctly;
* whether the change went beyond the authorized scope;
* whether it introduced a new problem or trade-off.

---

## Research inspiration

StoryScope (📄 [arXiv paper](https://arxiv.org/abs/2604.03136)) observed in its research on AI fiction that AI-generated stories may be more likely to use neat, single-path plots and explain their themes too explicitly.

Inception uses this kind of population-level observation as a reference for proposing audit hypotheses. It is not a writing rule for all content, and it does not mean that presentation text, document text, or social copy has the same level of research evidence.

This skill **is not an AI detector or a cosmetic humanizer.** Its purpose is to identify content decisions that may be influenced by default patterns, compare them with the author's original intent, and return decisions with real material impact to human judgment.

---

## A complete example

Suppose you are preparing a presentation for an engineering team.

Your intent is:

```text
Audience:
Engineering team

Goal:
Help the team understand the limitations of the current approach

Must preserve:
Technical accuracy
Known uncertainty
Existing evidence

Must avoid:
Overstating the conclusion
```

The draft might contain this sentence:

> This architecture solves the scalability problem and provides a reliable foundation for future growth.

But the current evidence has only been tested in a limited set of situations.

Inception might return:

```text
Observed choice:
The conclusion describes the architecture as having fully solved the scalability problem.

Why it matters:
The original intent requires the limitations and uncertainty to remain visible.

Possible alternatives:
- Keep the original sentence;
- narrow the claim to what the current evidence supports;
- distinguish verified results from expected future benefits.

Recommendation:
Revise.
```

You still decide whether to accept the recommendation.

Inception does not silently change the original sentence and then tell you it has been “optimized.”

---

## Skill layout

The project-local skill is stored at:

```text
skills/inception/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── core-workflow.md
│   ├── document-text-adapter.md
│   ├── fiction-adapter.md
│   ├── presentation-text-adapter.md
│   ├── reviewer-protocol.md
│   └── social-copy-adapter.md
└── scripts/validate_ledger.py
```

`SKILL.md` loads the Core workflow, the Reviewer Protocol, and **exactly one** domain adapter.

More detailed domain-specific guidance remains in `references/`, so unrelated domain documents do not consume context for the current task.

---

## Install and discover the skill

The repository is the single source of truth for this skill. The Codex and Claude Code packages both load the same `skills/inception/SKILL.md`; neither package contains a separate copy of the skill implementation.

Integration metadata is kept at the repository root: Codex uses `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json`, while Claude Code uses `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.

### OpenAI Codex

Add the repository marketplace, then install the plugin:

```bash
codex plugin marketplace add arthur422tp/Inception
codex plugin add inception@inception
```

After installation, invoke it explicitly with `$inception`, or ask Codex to audit or revise fiction, presentation text, document text, or organic brand and personal social copy against your intent.

### Anthropic Claude Code

Add the repository marketplace, then install the plugin:

```bash
claude plugin marketplace add arthur422tp/Inception
claude plugin install inception@inception
```

Inside an interactive Claude Code session, you can use these equivalent commands:

```text
/plugin marketplace add arthur422tp/Inception
/plugin install inception@inception
```

After installation, the skill is available under the plugin namespace `/inception:inception`. For local development, load the current repository directly with `claude --plugin-dir .`.

### Manual Codex skill development

For local development or older Codex versions without plugin marketplace support, copy or link the skill folder into `~/.codex/skills/`:

```bash
cp -R skills/inception ~/.codex/skills/
```

Or use a symbolic link while developing locally:

```bash
ln -s "$(pwd)/skills/inception" ~/.codex/skills/inception
```

After installation, invoke it explicitly with:

```text
$inception
```

---

## Validate a Decision Ledger

Decision Ledgers use JSON, so workflow gates can be checked deterministically:

```bash
.venv/bin/python skills/inception/scripts/validate_ledger.py \
  tests/fixtures/valid-ledger.json
```

Expected output:

```text
valid: tests/fixtures/valid-ledger.json
```

Invalid input exits with a non-zero status and reports the exact field path where the problem occurred.

---

## Run tests

The Python utilities use only the Python 3.11 standard library:

```bash
.venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v
```

You can also use Codex's `skill-creator` utility to validate the skill folder itself:

```bash
python3 /Users/arthuryu/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/inception
```

---

## Non-goals

This project is not intended for:

- AI-source detection or authorship scoring;
- word blacklists or other cosmetic humanization techniques;
- automatic rewriting before human disposition;
- autonomous reviewer-to-writer revision loops;
- treating StoryScope's population-level tendencies as universal writing rules for all text;
- visual presentation design;
- document layout, file-format operations, tracked changes, or comments;
- paid ads, targeting, bidding, social scheduling, or algorithm speculation.

## License

MIT

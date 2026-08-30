# Inception

[English](README.md) | [繁體中文](README.zh-TW.md)

> Inception finds content choices that may make a draft feel predictable, over-explained, or too neat. It shows you what it found, explains why it might matter, and lets you decide what—if anything—to change.

It looks beyond word choice and tone. For example, Inception may flag a story that resolves every conflict too cleanly, a presentation that sounds more certain than its evidence, or a document that keeps restating the same idea through a familiar template.

This repository contains the `inception` skill, packaged for both OpenAI Codex and Anthropic Claude Code. It is inspired by StoryScope's (📄 [arXiv Paper](https://arxiv.org/abs/2604.03136)) observation that models often converge on familiar content decisions. The skill does not detect AI authorship or rewrite by default. It surfaces potentially default-driven choices, compares them with the author's intent, and returns material decisions to the human.

When the host supports subagents, the human-facing main agent delegates the audit to an independent reviewer. The reviewer receives the Intent Contract and draft, returns an evidence-backed Decision Ledger, and never revises the text. The main agent shows that result to the human and applies only accepted or modified actions. If independent review is unavailable, the main agent uses the same gated workflow and identifies the fallback.

The first release supports:

- fiction;
- presentation text, including deck argument, slide function, claims, and evidence;
- document text, including reports, proposals, memos, specifications, policies, SOPs, and research summaries;
- organic brand and personal social copy, including captions, posts, threads, and post series.

It intentionally excludes paid advertising, social-platform optimization, presentation visual design, and document-format mechanics such as typography, color, spacing, layout, pagination, tracked changes, and file operations.

## Workflow

Every audit uses the same gated sequence:

```text
intent
  → initial_draft
  → domain_audit
  → awaiting_human_decision
  → revision
  → regression_audit
  → complete
```

The audit produces an evidence-backed Decision Ledger. Material changes cannot enter `revision` until the affected entries have an accepted or modified human decision. A clean draft may produce an empty ledger.

The actors are deliberately separated:

- the main agent captures intent, creates or receives the draft, presents review results, and applies approved revisions;
- the audit reviewer performs `domain_audit` and `regression_audit` without rewriting or approving its own recommendations;
- the human accepts, modifies, rejects, or defers every material finding.

Review dispatch may be automatic, but content decisions are not. Reviewer results always return to the human; the reviewer and writer never run a private revision loop.

### Example

Suppose you ask the main agent to draft a piece of presentation text and explain that “the audience is an engineering team, and the goal is to help them understand the limitations of this approach.” After creating the draft, the main agent sends the Intent Contract and draft to an independent reviewer when one is available. The reviewer identifies decisions that could affect that intent—for example, whether the conclusion is overly neat or whether the claims are supported by evidence—and records them in the Decision Ledger.

The main agent then shows you the ledger and pauses. It proceeds to revision only after you mark an entry as `accepted` or `modified`. A reviewer checks the resulting change, and that Regression Audit also comes back to you before any additional revision pass.

## Skill Layout

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

`SKILL.md` loads the Core workflow, the Reviewer Protocol, and exactly one domain adapter. Detailed guidance remains in references so unrelated domains do not consume context.

## Install and Discover the Skill

The repository is the single source of truth. The Codex and Claude Code packages both load the same `skills/inception/SKILL.md`; neither package contains a duplicate skill implementation.

The integration metadata is kept at the repository root: `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` for Codex, plus `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` for Claude Code.

### OpenAI Codex

Add the repository marketplace and install the plugin:

```bash
codex plugin marketplace add arthur422tp/Inception
codex plugin add inception@inception
```

Then invoke the skill with `$inception`, or ask Codex to audit or revise fiction, presentation text, document text, or an organic social post against your intent.

### Anthropic Claude Code

Add the repository marketplace and install the plugin:

```bash
claude plugin marketplace add arthur422tp/Inception
claude plugin install inception@inception
```

Inside an interactive Claude Code session, the equivalent commands are:

```text
/plugin marketplace add arthur422tp/Inception
/plugin install inception@inception
```

The skill is available under the plugin namespace as `/inception:inception`. For local development, load the repository directly with `claude --plugin-dir .`.

### Manual Codex skill development

For local development or older Codex setups that do not support plugin marketplaces, copy or link the skill folder into `~/.codex/skills/`:

```bash
cp -R skills/inception ~/.codex/skills/
```

Or, while developing locally:

```bash
ln -s "$(pwd)/skills/inception" ~/.codex/skills/inception
```

After installation, invoke it explicitly with `$inception`.

## Validate a Decision Ledger

Ledger files use JSON so their gates can be checked deterministically:

```bash
.venv/bin/python skills/inception/scripts/validate_ledger.py \
  tests/fixtures/valid-ledger.json
```

Expected output:

```text
valid: tests/fixtures/valid-ledger.json
```

Invalid input exits with a non-zero status and reports the exact field path.

## Run Tests

The Python utilities use only the Python 3.11 standard library:

```bash
.venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v
```

Validate the skill folder itself with the Codex skill-creator utility:

```bash
python3 /Users/arthuryu/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/inception
```


## Non-Goals

- AI-source detection or authorship scoring;
- word blacklists or cosmetic humanization;
- automatic rewriting before human disposition;
- autonomous reviewer-to-writer revision loops;
- treating StoryScope's population-level tendencies as universal writing rules;
- visual presentation design;
- document layout, file-format operations, tracked changes, or comments;
- paid ads, targeting, bidding, social scheduling, or algorithm speculation.

## License

MIT

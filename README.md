# Inception

[English](README.md) | [繁體中文](README.zh-TW.md)

This repository contains the `inception` Codex skill, inspired by StoryScope's (📄 [arXiv Paper](https://arxiv.org/abs/2604.03136)) observation that models often converge on familiar content decisions. The skill does not detect AI authorship or make writing “look human.” It exposes potentially default-driven choices, compares them with the author's intent, and returns material decisions to the human.

The first release supports:

- fiction;
- presentation text, including deck argument, slide function, claims, and evidence;
- document text, including reports, proposals, memos, specifications, policies, SOPs, and research summaries.

It intentionally excludes presentation visual design and document-format mechanics such as typography, color, spacing, layout, pagination, tracked changes, and file operations.

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

### Example

Suppose you provide a piece of presentation text and explain that “the audience is an engineering team, and the goal is to help them understand the limitations of this approach.” The skill will first identify decisions that could affect that intent—for example, whether the conclusion is overly neat or whether the claims are supported by evidence—and record them in the Decision Ledger.

At that point, the skill will pause and wait for your decision. It will proceed to revision only after you mark an entry as `accepted` or `modified`, followed by a regression audit.

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
│   └── presentation-text-adapter.md
└── scripts/validate_ledger.py
```

`SKILL.md` loads the Core workflow and exactly one domain adapter. Detailed guidance remains in references so unrelated domains do not consume context.

## Make the Skill Discoverable

The repository is the source of truth. To make the skill available as a personal Codex skill, copy or link the skill folder into `~/.codex/skills/`:

```bash
cp -R skills/inception ~/.codex/skills/
```

Or, while developing locally:

```bash
ln -s "$(pwd)/skills/inception" ~/.codex/skills/inception
```

After installation, invoke it explicitly with `$inception`, or ask Codex to audit or revise fiction, presentation text, or document text against your intent.

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
- treating StoryScope's population-level tendencies as universal writing rules;
- visual presentation design;
- document layout, file-format operations, tracked changes, or comments.

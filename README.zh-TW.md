Inception

[English](README.md) | [繁體中文](README.zh-TW.md)

本 repository 包含名為 `inception` 的 Codex skill，這是一個受到 StoryScope 啟發而開發的工具。

StoryScope （📄 [arXiv Paper](https://arxiv.org/abs/2604.03136)）在 AI fiction 的研究中觀察到，AI 生成故事可能較常採用整齊、單一路徑的情節並過度解釋主題。這個 skill 將這類 population-level observation 作為提出 audit hypotheses 的參考；它不是對所有內容的普遍寫作規則，也不代表 presentation text 或 document text 已有相同程度的研究證據。這個 skill **不是用來偵測 AI 生成內容，也不是要讓文字「看起來更像人寫的」**。它的目的是找出可能受到預設模式（default-driven choices）影響的內容決策，將這些決策與作者原本的意圖進行比較，並把真正具有實質影響的決策交還給人類判斷。

第一個版本支援：

- fiction（小說／虛構敘事）；
- presentation text（簡報文字內容），包含整份簡報的論證架構、單張投影片的功能、claims 與 evidence；
- document text（文件文字內容），包含 reports、proposals、memos、specifications、policies、SOPs 與 research summaries。

目前刻意排除簡報的視覺設計與文件格式操作，例如 typography、color、spacing、layout、pagination、tracked changes 與檔案操作。

## Workflow

每一次 audit 都遵循相同的 gated sequence：

```text
intent
  → initial_draft
  → domain_audit
  → awaiting_human_decision
  → revision
  → regression_audit
  → complete
```

audit 會產生一份由證據支持的 **Decision Ledger**。

任何 material change 在進入 `revision` 階段之前，相關的 ledger entry 都必須先取得人類的 `accepted` 或 `modified` decision。

如果初始 draft 沒有發現需要處理的實質問題，Decision Ledger 可以是空的。

### 小例子

假設你提供一段簡報文字，並說明「受眾是工程團隊，希望他們理解這個方案的限制」。skill 會先找出可能影響這個意圖的決策，例如結論是否過度整齊、claim 是否有 evidence 支持，然後把它們記在 Decision Ledger 中。此時 skill 會停下來等待你的決定；只有在你對某個 entry 選擇 `accepted` 或 `modified` 後，才會進入 revision，最後再做 regression audit。

## Skill Layout

project-local skill 存放於：

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

`SKILL.md` 會載入 Core workflow，以及**且僅載入一個** domain adapter。

較詳細的 domain-specific guidance 則保留在 `references/` 中，避免與目前任務無關的 domain 文件佔用 context。

## Make the Skill Discoverable

repository 是這個 skill 的 source of truth。

若要讓它成為個人 Codex skill，可以將 skill folder 複製或連結到 `~/.codex/skills/`：

```bash
cp -R skills/inception ~/.codex/skills/
```

或者在本地開發期間使用 symbolic link：

```bash
ln -s "$(pwd)/skills/inception" ~/.codex/skills/inception
```

安裝完成後，可以使用以下方式明確呼叫：

```text
$inception
```

也可以直接要求 Codex 根據你的 intent，audit 或 revise fiction、presentation text 或 document text。

## Validate a Decision Ledger

Decision Ledger 使用 JSON 格式，因此 workflow gate 可以透過程式進行 deterministic validation：

```bash
.venv/bin/python skills/inception/scripts/validate_ledger.py \
  tests/fixtures/valid-ledger.json
```

預期輸出：

```text
valid: tests/fixtures/valid-ledger.json
```

如果輸入不合法，程式會以 non-zero status 結束，並回報發生問題的確切 field path。

## Run Tests

Python utilities 僅使用 Python 3.11 standard library：

```bash
.venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v
```

也可以使用 Codex 的 `skill-creator` utility 驗證 skill folder 本身：

```bash
python3 /Users/arthuryu/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/inception
```

prompt 與 adapter 文件採用 structural validation，加上位於 `tests/skill-smoke/scenarios.md` 的 representative smoke scenarios。

這些 prompt 與 adapter **刻意不採用 RED/GREEN prompt TDD**。

## Non-Goals

本專案目前不以以下事項為目標：

- AI source detection 或 authorship scoring；
- 使用 word blacklist 或其他 cosmetic humanization 手段；
- 在人類完成 disposition 之前自動改寫內容；
- 將 StoryScope 所觀察到的 population-level tendencies 視為適用於所有文本的普遍寫作規則；
- 簡報的 visual presentation design；
- 文件的 layout、file-format operations、tracked changes 或 comments。

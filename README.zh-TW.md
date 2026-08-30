Inception

[English](README.md) | [繁體中文](README.zh-TW.md)

> Inception 會找出可能讓草稿顯得過度工整、解釋太滿或充滿模板感的內容選擇。 它會告訴你發現了什麼、可能造成什麼影響，再由你決定要不要修改。

它檢查的不只是用詞與語氣。例如，Inception 可能會指出一篇故事把所有衝突收得太乾淨、一份簡報講得比證據更肯定，或一份文件不斷透過熟悉的模板重述同一件事。

這些模式只是值得檢查的線索，不代表寫法一定不好。Inception 會將它們與你的受眾、目的和限制比較，只列出可能真正影響原始意圖的選擇。

Inception 不會判定一段文字是不是由 AI 撰寫，也不會未經同意就改寫重要內容。它會先將發現記入 Decision Ledger，等你決定後才進行修訂，最後再檢查修改結果是否偏離原始意圖。

當宿主環境支援 subagent 時，面對使用者的 main agent 會把 audit 交給獨立 reviewer。Reviewer 只接收 Intent Contract 與 draft，回傳有證據支持的 Decision Ledger，不直接改稿。Main agent 會把結果交給使用者，並且只執行使用者 `accepted` 或 `modified` 的項目。若環境無法建立獨立 reviewer，main agent 仍使用相同的 gated workflow，並向使用者說明這次採用 same-agent fallback。

StoryScope （📄 [arXiv Paper](https://arxiv.org/abs/2604.03136)）在 AI fiction 的研究中觀察到，AI 生成故事可能較常採用整齊、單一路徑的情節並過度解釋主題。這個 skill 將這類 population-level observation 作為提出 audit hypotheses 的參考；它不是對所有內容的普遍寫作規則，也不代表 presentation text、document text 或 social copy 已有相同程度的研究證據。這個 skill **不是用來偵測 AI 生成內容，也不是要讓文字「看起來更像人寫的」**。它的目的是找出可能受到預設模式（default-driven choices）影響的內容決策，將這些決策與作者原本的意圖進行比較，並把真正具有實質影響的決策交還給人類判斷。

第一個版本支援：

- fiction（小說／虛構敘事）；
- presentation text（簡報文字內容），包含整份簡報的論證架構、單張投影片的功能、claims 與 evidence；
- document text（文件文字內容），包含 reports、proposals、memos、specifications、policies、SOPs 與 research summaries；
- social copy（社群文案），只涵蓋品牌／個人的自然貼文，包含 captions、posts、threads 與 post series。

目前刻意排除付費廣告、社群平台成效最佳化、簡報的視覺設計與文件格式操作，例如 typography、color、spacing、layout、pagination、tracked changes 與檔案操作。

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

三個角色刻意分開：

- main agent 負責取得 intent、建立或接收 draft、呈現審查結果，以及執行已核准的 revision；
- audit reviewer 負責 `domain_audit` 與 `regression_audit`，不能直接改稿或替使用者接受自己的建議；
- 使用者負責對每個 material finding 做 `accepted`、`modified`、`rejected` 或 `deferred` 決定。

系統可以自動派發 review，但不會自動替使用者做內容決策。Reviewer 的結果一定先回到使用者；reviewer 與 writer 不會私下形成反覆修改迴圈。

### 小例子

假設你請 main agent 撰寫一段簡報文字，並說明「受眾是工程團隊，希望他們理解這個方案的限制」。Main agent 建立初稿後，會在環境允許時把 Intent Contract 與 draft 交給獨立 reviewer。Reviewer 找出可能影響這個意圖的決策，例如結論是否過度整齊、claim 是否有 evidence 支持，並把它們記在 Decision Ledger 中。

Main agent 接著把 ledger 呈現給你並停下來等待。只有在你對某個 entry 選擇 `accepted` 或 `modified` 後，才會進入 revision。修改完成後，reviewer 會執行 Regression Audit；在進行任何下一輪 revision 之前，結果同樣會先交給你。

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
│   ├── presentation-text-adapter.md
│   ├── reviewer-protocol.md
│   └── social-copy-adapter.md
└── scripts/validate_ledger.py
```

`SKILL.md` 會載入 Core workflow、Reviewer Protocol，以及**且僅載入一個** domain adapter。

較詳細的 domain-specific guidance 則保留在 `references/` 中，避免與目前任務無關的 domain 文件佔用 context。

## 安裝與探索 Skill

repository 是這個 skill 的 single source of truth。Codex 與 Claude Code 的 package 都會載入同一份 `skills/inception/SKILL.md`；兩者不會各自複製另一份 skill implementation。

整合用的 metadata 保留在 repository 根目錄：Codex 使用 `.codex-plugin/plugin.json` 與 `.agents/plugins/marketplace.json`，Claude Code 使用 `.claude-plugin/plugin.json` 與 `.claude-plugin/marketplace.json`。

### OpenAI Codex

先加入 repository marketplace，再安裝 plugin：

```bash
codex plugin marketplace add arthur422tp/Inception
codex plugin add inception@inception
```

安裝後可以使用 `$inception` 明確呼叫，也可以直接要求 Codex 根據你的 intent，audit 或 revise fiction、presentation text、document text 或品牌／個人的社群自然貼文。

### Anthropic Claude Code

先加入 repository marketplace，再安裝 plugin：

```bash
claude plugin marketplace add arthur422tp/Inception
claude plugin install inception@inception
```

在互動式 Claude Code session 中，也可以使用以下等價指令：

```text
/plugin marketplace add arthur422tp/Inception
/plugin install inception@inception
```

安裝後，skill 會以 plugin namespace `/inception:inception` 提供。若要在本地開發，可以直接使用 `claude --plugin-dir .` 載入目前 repository。

### 手動 Codex skill 開發

若是本地開發，或使用尚未支援 plugin marketplace 的舊版 Codex，可以將 skill folder 複製或連結到 `~/.codex/skills/`：

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


## Non-Goals

本專案目前不以以下事項為目標：

- AI source detection 或 authorship scoring；
- 使用 word blacklist 或其他 cosmetic humanization 手段；
- 在人類完成 disposition 之前自動改寫內容；
- reviewer 與 writer 自主進行反覆修改；
- 將 StoryScope 所觀察到的 population-level tendencies 視為適用於所有文本的普遍寫作規則；
- 簡報的 visual presentation design；
- 文件的 layout、file-format operations、tracked changes 或 comments；
- 付費廣告、targeting、bidding、社群排程或 algorithm speculation。

## 授權

MIT

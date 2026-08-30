# Inception

[English](README.md) | [繁體中文](README.zh-TW.md)

> **一個在保留作者意圖的前提下，降低文字「AI 味」與模型預設感的 writing skill。**

Inception 不只檢查用詞或語氣，而是往更上游看：**內容到底做了哪些選擇。**

它會找出那些可能讓文字顯得過度工整、過度解釋、太容易預測、重複表達，或比證據本身更有把握的內容決策。

它不會一看到問題就直接把全文重寫。

Inception 會先告訴你：

* 它看到了什麼；
* 為什麼這個選擇可能值得注意；
* 它和你的原始意圖有什麼關係；
* 如果要改，可以怎麼改；
* 修改後會犧牲什麼。

最後由你決定哪些地方真的需要改。

目前支援：

* 小說與敘事文字；
* 簡報文字，包括整體論述、單頁功能、claims 與 evidence；
* 文件文字，包括報告、提案、memo、specification、policy、SOP 與 research summary；
* 品牌與個人的自然社群內容，包括貼文、caption、thread 與系列貼文。

Inception 可用於 **OpenAI Codex** 與 **Anthropic Claude Code**。

---

## Inception 會抓什麼？

很多 humanizer 主要處理的是表層文字，例如：

* 換詞；
* 調整句長；
* 移除 cliché；
* 把語氣改得比較口語；
* 讓句型不要那麼規律。

這些方法有時有效。

但許多讓文字看起來「很像 AI」的特徵，其實出現在更上游。

Inception 看的不是只有：

```text
這句話怎麼寫
```

而是：

```text
為什麼這裡選擇這樣寫？
這個資訊真的需要出現嗎？
這個結論真的應該收得這麼完整嗎？
這個論點需要再講一次嗎？
這個 claim 的確定程度符合 evidence 嗎？
```

---

## 例子

### 小說

一個故事裡的每個衝突最後都透過主角成長、理解與和解來解決，結尾還明確說出主角「學到了什麼」。

Inception 可能會指出：

* 結局是否過度整齊；
* 主題是否被解釋得太完整；
* 是否所有衝突都被同一種 resolution mechanism 收束。

但它不會因為這些模式「常見於模型輸出」就直接判定它們是錯的。

如果你的作品本來就是寓言、療癒故事或需要明確 closure，保留它可能才是正確選擇。

---

### 簡報

一份簡報在多張投影片中重複同一個結論，而且越講越確定，但實際 evidence 只支持較保守的說法。

Inception 可能會指出：

* 多張 slide 是否重複執行相同 argument function；
* claim strength 是否超過 evidence；
* conclusion 是否比原始 intent 更強。

---

### 文件

一份 proposal 在 Executive Summary、Background、Recommendation 和 Conclusion 中反覆解釋同一個 rationale。

Inception 不會只幫你把四段話換成不同句型。

它會先問：

> 這個理由真的需要被表示四次嗎？

也就是檢查 **representation decision** 本身，而不是只處理 wording。

---

### 社群內容

一篇貼文自然地落入：

```text
hook
→ 問題
→ 個人經驗
→ 三點心得
→ 正向 takeaway
```

如果作者原本想要的是較冷靜、觀察式、沒有明確結論的 voice，Inception 可能會把這個熟悉結構列為一個值得重新決定的內容選擇。

它不會因為「不像人」就強迫你變得口語或故意寫得凌亂。

---

## 為什麼不用一般 Humanizer？

多數 humanizer 主要操作：

```text
word choice
sentence structure
tone
register
```

Inception 更往上游處理：

```text
content selection
argument structure
narrative resolution
claim strength
repetition
emphasis
explanation
```

Inception 的目標不是讓每一篇文章都變得罕見、奇怪或不可預測。

熟悉的選擇不代表不好。

不尋常的選擇也不代表比較高級。

Inception 真正要問的是：

> **這個選擇是在服務作者的意圖，還是只是模型最容易採用的預設？**

例如：

* 線性敘事可能正是兒童故事需要的；
* 明確結論可能正是政策文件需要的；
* 簡報中重複關鍵訊息可能是刻意的；
* 高度結構化的格式可能正是 SOP 應該具備的。

因此 Inception 不會把「常見」直接等同於「缺陷」。

它只會把這些模式視為 **值得檢查的 decision candidates**。

---

## 它怎麼運作？

從使用者角度看，流程很簡單：

```text
草稿
  → Audit
  → 你決定
  → Revision
  → Check
```

Inception 會先確認：

> 這份文字到底想達成什麼？

接著才檢查草稿中的內容決策。

如果找到可能與 intent 衝突的重要選擇，它會先回傳給你。

你可以：

* 接受；
* 修改建議；
* 拒絕；
* 延後處理。

只有你接受或修改過的 decision，才能進入 revision。

修改完成後，Inception 會再檢查：

* 原本批准的修改有沒有正確完成；
* 有沒有改超出授權範圍；
* 有沒有產生新的問題或 trade-off。

---

## 一個完整例子

假設你要做一份給工程團隊看的簡報。

你的 intent 是：

```text
Audience:
Engineering team

Goal:
讓團隊理解目前方案的限制

Must preserve:
技術正確性
目前已知的不確定性
既有 evidence

Must avoid:
把結論講得太滿
```

草稿裡可能有一句：

> 這套架構解決了 scalability 問題，並為未來成長提供可靠基礎。

但目前 evidence 其實只驗證了一部分情境。

Inception 可能回傳：

```text
Observed choice:
目前結論把架構描述成已完整解決 scalability 問題。

Why it matters:
原始 intent 要求保留限制與不確定性。

Possible alternatives:
- 保留原句；
- 把 claim 收斂到目前 evidence 實際支持的範圍；
- 明確區分目前已驗證效果與預期中的未來效益。

Recommendation:
Revise.
```

最後仍然由你決定要不要接受。

Inception 不會偷偷把原句改掉，再告訴你「已優化完成」。

---

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

---

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

---

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

---

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

---

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

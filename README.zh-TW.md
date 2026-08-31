# Inception

[English](README.md) | [繁體中文](README.zh-TW.md)

> **讓 AI 輔助文字少一點公式感，同時保留你真正想表達的內容。**

Inception 適合處理太公式化、過度解釋、重複、收得過於整齊，或比 evidence 更有把握的草稿。它不只檢查用詞或語氣，而是往更上游看：**內容到底做了哪些選擇。**

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

## 30 秒開始使用

```text
Use $inception to review this draft for generic, formulaic,
over-explained, repetitive, or unsupported content choices.
Show me only the three most important decisions and wait before revising.
```

Inception 預設使用 **Quick Review**：以自然語言提出經過排序、有證據的重要決策，通常為一至三個，但不設硬性上限。它不會強迫每一份短稿都進入完整審查流程，也不會為了維持預設數量而隱藏重要問題。

例如：

```text
修改前
「這次 migration 不只改善了流程，更徹底改變了我們理解協作的方式。
以下是每個團隊都能使用的三個教訓……」

Inception 注意到
開頭 claim、三個教訓與結尾 takeaway 都把同一個事件收束成普遍結論，
但草稿實際上只有一次 migration 的 evidence。

人的決定
保留事件；移除普遍性的 transformation claim，並合併重複的 lesson
與 takeaway。

修改後
「這次 migration 比預期多花了兩天，因為我們從未在 partial failure
下測試 rollback assumption……」
```

修改的是上游的內容決策，不只是替換同義詞；而且只有在人接受建議之後才會發生。

---

## Inception 會抓什麼？

很多 humanizer 主要處理的是表層文字，例如：

* 換詞；
* 調整句長；
* 移除陳腔濫調；
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

大部分請求使用 **Quick Review**：

```text
草稿 → 經過排序的重要決策 → 你決定 → 修改 → 檢查
```

Quick Review 會從請求與草稿推斷最小必要 intent，只有缺少的答案會實質改變建議時才提問，並在主要對話裡完成 audit。它通常聚焦一至三個決策，但不設 finding 硬上限。

當你明確要求 deep、full、exhaustive、independent 或 persisted review，或長篇／高風險內容需要檢查跨章節依賴時，使用 **Deep Audit**：

```text
完整 Intent Contract
  → 可用時進行 independent audit
  → Decision Ledger
  → 你決定
  → 經授權的修改
  → Regression Audit
```

Finding 數量本身不會觸發 Deep Audit。如果仍有其他 material candidates，Inception 可以繼續 Quick Review、進行 focused follow-up，或只在依賴關係、風險、持久化或 independent review 確實需要時建議 Deep Audit。

兩種深度都會先確認：

> 這份文字到底想達成什麼？

接著才檢查草稿中的內容決策。

如果找到可能與 intent 衝突的重要選擇，它會先回傳給你。

你可以：

* 接受；
* 修改建議；
* 拒絕；
* 延後處理。

只有你接受或修改過的 decision，才能進入 revision。Quick Review 減少的是儀式與輸出負擔，不是這道 human-decision gate。

修改完成後，Inception 會再檢查：

* 原本批准的修改有沒有正確完成；
* 有沒有改超出授權範圍；
* 有沒有產生新的問題或 trade-off。

---

## 研究啟發

StoryScope（📄 [arXiv 論文](https://arxiv.org/abs/2604.03136)）在 AI fiction 的研究中觀察到，AI 生成故事可能較常採用整齊、單一路徑的情節，並過度解釋主題。

Inception 將這類 population-level observation 作為提出 audit hypotheses 的參考。它不是適用於所有內容的寫作規則，也不代表 presentation text、document text 或 social copy 已有相同程度的研究證據。

這個 skill **不是 AI 偵測器，也不是只修改表面文字的 humanizer。** 它的目的是找出可能受到預設模式（default-driven choices）影響的內容決策，將這些決策與作者原本的意圖比較，再把真正具有實質影響的決策交還給人類判斷。

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

`SKILL.md` 會載入 Core workflow，以及**且僅載入一個** domain adapter。Deep Audit 會額外載入 Reviewer Protocol；deep fiction audit 也會載入完整 StoryScope feature registry。

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

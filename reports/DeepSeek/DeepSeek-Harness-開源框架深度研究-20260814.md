# 看懂 DeepSeek Harness：一切皆插件的開源智能體框架

> 寫作日期：2026-08-14（開源後第 1 天）。本文所有事實經多信源交叉核實，19 個源站、90 條聲明抽取、25 條進入三票對抗式驗證（25 條確認、0 條被推翻）。項目 README 明確警告"將有破壞兼容性的變更"，本文所有架構細節鎖定 v0.1（npm 0.1.0-rc.6）、取證日期 2026-08-14，數週內可能失效。

## 一句話總結

DeepSeek Harness（命令行名 `dsh`）是 DeepSeek 2026-08-13 首次開源的智能體執行框架（agent harness），MIT 許可、TypeScript 編寫，核心設計是"一切皆插件"——模型適配器、工具註冊表、會話日誌乃至 agent 循環本身都可從配置替換，官方稱"不存在可打補丁的特權內核"。它的目標受眾是構建 agent harness 的開發者，而不是終端用戶：官方零基準披露、零競品對比，社區首日的主要批評是"只有架構、沒有開箱即用能力"。

## 一、基本檔案

| 項目 | 內容 |
| --- | --- |
| 發佈時間 | 2026-08-13（官方 X 賬號發佈 v0.1 開發者預覽版） |
| 倉庫 | [github.com/deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) |
| 許可證 | MIT，無附加條款（Copyright (c) 2026 DeepSeek） |
| 主語言 | TypeScript，約 97%；47 個包的 monorepo |
| npm 包 | `@deepseek-ai/dsh`，latest = 0.1.0-rc.6，首發 2026-08-10（早於 GitHub 開源 3 天） |
| 倉庫創建 | 2026-08-13T11:56:32Z（GitHub API 一手元數據） |
| 熱度 | 約 34.3k → 34.7k star / 2.6k fork（核查當時仍在上漲，僅為時點快照） |
| 成熟度 | 開發者預覽，Releases 頁為空，無穩定 tag；倉庫 issues 已關閉 |
| 基準成績 | 官方零披露 |

README 首句原文：*"DeepSeek Harness (`dsh`) is an open-source agent harness developed by DeepSeek AI."* 倉庫簡介即 "Everything is a Plugin."

來源：[README](https://github.com/deepseek-ai/deepseek-harness/blob/master/README.md)、[官網](https://www.deepseek.com/harness/en/)、[官方 X 公告](https://x.com/deepseek_ai/status/2087887408440164663)、[GitHub API](https://api.github.com/repos/deepseek-ai/deepseek-harness)、[npm registry](https://registry.npmjs.org/@deepseek-ai%2Fdsh)

## 二、架構：一切皆插件

### 2.1 核心斷言

官方架構文檔 [architecture.md](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md) 原文：

> "Every part of the product is a plugin, including the model adapter, the tool registry, the session log, and the agent loop itself, so every part is replaceable from configuration."
>
> "There is no privileged core to patch: you extend dsh by mounting a plugin beside the others, and registrations are effects that unwind when their plugin unloads."

關鍵點在於 agent 循環本身也是插件。多數 agent 框架把"循環"寫死在內核裡，只開放工具和提示詞兩個口子；`dsh` 的設計是把循環也放進可替換清單，擴展方式是在旁邊掛插件而非給內核打補丁。

### 2.2 三個支撐機制

**上下文即服務容器。** 每個服務佔據一個穩定的 `ctx.<key>`，架構文檔給出的真實服務鍵包括 `ctx.sessions`、`ctx.tools`、`ctx.llm`、`ctx.systemPrompt`、`ctx.agents`、`ctx.agentLoop`、`ctx.commands`、`ctx.jobs`、`ctx.fs`、`ctx.shell`、`ctx.sandbox`、`ctx.goals`、`ctx.sessionTitle`。官方中文文檔 [cordis-primer](https://deepseek-harness.github.io/deepseek-harness/reference/cordis-primer) 逐字表述："其他插件通過 key 查找服務，而非導入具體實現"、"加載順序通過服務依賴表達，而非手動編排啟動序列"。

**註冊即可逆副作用。** 提示詞片段、工具 schema、適配器、監聽器統一通過 `ctx.effect()` 或 `ctx.on()` 安裝，文檔稱"reload 和 teardown 時會按預期撤銷"。這決定了熱重載和插件卸載不會留下殘留狀態。

**分層組合出插件樹。** 啟動時按序疊加：bundles → profile 的 `cordis.patch.yml` → home 級 → `--patch` 覆蓋。官方三個 bundle：`@deepseek-ai/dsh-base`（模型適配器、工具、持久化、沙箱與審批策略、設置、憑證、遙測）、`dsh-web-app`（瀏覽器應用）、`dsh-headless`（無服務器的一次性運行器）。擴展點抽象為 seam（接縫），文檔定義 seam = Service Definition（接口）+ Service Provider（實現）+ Consumer（消費方）；接入模型提供方即把適配器註冊到 `ctx.llm`，接入工具即註冊到 `ctx.tools`。

代碼結構佐證這不只是口號：`packages/` 下 47 個包，含 `llm`、`core`（內含 agent-loop 默認實現）、`skill`、`session`、`sandbox`、`e2b`、`fs`、`storage`、`workflow`、`schedule`、`jobs`、`subagent`、`web`、`terminal`、`acp`、`mcp`、`shell`、`lsp`、`hooks`、`extensions` 等。

### 2.3 底座 Cordis：第三方項目，源碼內嵌

README 寫明框架"is powered by Cordis"。證據顯示 [cordiverse/cordis](https://github.com/cordiverse/cordis) 是獨立第三方項目，GitHub API 顯示創建於 2022-05-17，比 Harness 早四年，自述為 "Meta-Framework of Spatiotemporal Composability"。

引入方式不是 npm 依賴，而是 vendor（源碼內嵌）。[vendor/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/master/vendor/README.md) 明確寫道該目錄存放 Cordis 及其基礎庫的源碼副本，理由是讓 harness "fully owns its framework layer (auditable, patchable, pinned)"。清單含 cordis 4.0.0-rc.7、`@cordisjs/plugin-loader` 1.0.0-rc.5、plugin-include/group/timer/hmr/logger-console、cosmokit 1.8.1、schemastery 3.18.0 共 9 個包，附上游 commit、5 步同步流程與 18 條本地改動記錄。根 `package.json` 的 workspaces 首項即 `vendor/*`，無 cordis 的 npm 依賴；`AGENTS.md` 設有 vendor 清單守衛（改 `vendor/*/src` 必須同步更新清單）。各包 `package.json` 仍以 peerDependency 形式聲明 cordis，但解析到 vendor 工作區副本而非 registry。

值得注意的信號：cordis 倉庫的 GitHub homepage 字段直接指向 DeepSeek 的文檔站，證據表明雙方存在緊密協作而非單方面搬用。

### 2.4 兩處必要的精度修正

- README 引用的"論文"倉庫 [cordiverse/paper](https://github.com/cordiverse/paper) 創建於 2026-08-13，與 harness 同日，應描述為設計文檔而非同行評審論文。框架本體則確有四年曆史，兩者需分開表述。
- "不存在特權內核"不涵蓋 Cordis 本體與 boot 流程，這兩層是不可替換的底座；同時"加載順序完全由服務依賴表達"也需補充——bundle/profile 層仍有顯式的組合順序。

## 三、模型支持與工具調用

### 3.1 模型無關，不綁定自家模型

官方文檔 [providers.md](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/providers.md) 顯示：內置目錄直接支持 Anthropic、OpenAI 等提供方，填 API Key 即可，目錄自帶端點、協議與模型列表。Bedrock、Vertex、Azure、Codex 需各自原生鑑權（AWS 憑證 + region、ADC project、`api-version`、OAuth），文檔明確寫道"filling only the API-key field does not configure them"。還支持添加任意 OpenAI 兼容協議的企業網關或自託管端點（走 `GET /models` 發現模型），並可對具體模型做能力覆寫，文檔示例用的是 `claude-sonnet-4-5`。

包級佐證：`packages/llm` 下有 `llm`、`llm-deepseek`、`llm-pi-ai`、`llm-retry`、`token-meter`。`@deepseek-ai/dsh-llm-pi-ai` 自述為 pi-ai 驅動的通用多廠商適配器，示例中同時掛載 openai / anthropic / deepseek 路由。VentureBeat 獨立稱其為 Claude Code / Codex 底層基礎設施的"模型無關替代品"。

反面證據（不對稱之處）：界面上 DeepSeek 有專屬卡片、其他提供方需走"Add provider"；且 providers.md 承認 DeepSeek 自家的 chat-completions 路由僅支持純文本，無法另行配置。

### 3.2 工具調用是一條事件流水線

```
tool/call* → tools/pre-execute → tools/execute → tools/post-execute → tool/result*
```

架構文檔寫明三個 `tools/*` 是瀑布式事件，監聽器必須調用 `next()` 才能向下傳遞；帶星號的兩端屬於發出/流式的通知事件——不應把整條五段鏈路統稱為瀑布式。更細的 [tool-execution-pipeline.md](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/tool-execution-pipeline.md) 顯示：`pre-execute` 負責鉤子、權限、沙箱，可拒絕或觸發審批提示；`post-execute` 支持接受、阻斷、替換、追加上下文；文檔稱"hooks span tool families without coupling the tools to one policy service"。

含義：權限校驗、參數改寫、審計日誌全部以監聽器插入，不需要改動執行核心。文檔同時定義"一個 step = 一次模型請求加它調用的工具"。

## 四、部署方式

```bash
npx @deepseek-ai/dsh web       # 默認 Web 界面在 http://127.0.0.1:3080
```

源碼方式：`pnpm install` → `pnpm run build` → `pnpm dsh web`（根 package.json 為 `@deepseek-ai/dsh-root` 0.1.0-rc.5，packageManager 為 pnpm@11.7.0）。另有 `dsh-headless` bundle 提供無服務器的一次性運行器。

需要限定的是：一條命令部署字面成立，但那只是本地起一個 Web 預覽，不等於生產可用部署。

## 五、基準表現：官方零披露

這是本次研究最重要的否定性結論，需要單獨強調。

抓取 README 完整原始 Markdown（非頁面摘要）確認，全文小節僅為：標題段、Developer preview、Run、Community and support、Contributing、Development、License，**全文沒有任何基準分數或性能表格**。官網落地頁同樣無基準數據。README 與官網均未出現 OpenHands、SWE-agent、Claude Code 等任何競品名稱，唯一引用的外部項目是底層 Cordis（依賴說明而非競品對比）。

所有"開源版 Claude Code 競品"的定位均出自第三方媒體（VentureBeat 標題、CryptoBriefing 報道），不是 DeepSeek 自身的主張。

**關鍵防混淆提示：** 網上流傳的 SWE-bench 數字（如 DeepSeek V4-Pro 96.4% SWE-bench Verified、DeepSWE 54.4）屬於模型側成績且多為廠商自報，與本倉庫無關，不能挪用作 harness 的成績。截至取證日期，不存在"同一模型下 dsh vs OpenHands vs SWE-agent vs Claude Code"的可比實測，任何關於 dsh 基準表現的結論目前都無一手依據。

## 六、侷限與社區反饋

### 6.1 官方自述侷限

README 設有獨立小節，原文即全大寫加粗：

> "DeepSeek Harness is currently in _developer preview_ and is iterating rapidly. **THERE WILL BE COMPATIBILITY-BREAKING CHANGES.**"

官網同口徑："core plugins and APIs will continue to evolve"、"remains in developer preview and is still being tested"。GitHub Releases 頁返回 "There aren't any releases here"，無任何 GA 或穩定 tag；倉庫 issues 已關閉（`has_issues=false`），社區支持走 Discussions、`dsh-plugin` 話題與 Discord。

措辭精度：官方從未寫"禁止用於生產"。"不適合生產"是基於 v0.1 + 零 release + 破壞性變更警告 + "still being tested" 四項的合理推論，屬推測而非官方主張。Cordis 上游自身也自述 API 尚未穩定。

### 6.2 社區首日反饋（信心：中）

[Hacker News 討論帖](https://news.ycombinator.com/item?id=49285244) 372 分 / 173 評論，項目作者本人現身（"Hi I'm one of the authors of DeepSeek Harness"，並回應"It's just an early developer preview version"）。GitHub API 於 2026-08-14 多次核查，star 從 34292 漲到 34689，fork 約 2633–2660，commits 約 12293（倉庫僅創建 1 天，說明為內部歷史導入，屬正常代碼外放，非歸屬疑點）。

主要批評原話：

- *"For me the problem is not that it has a plugin based architecture. It's that it ONLY has that. If there are no batteries included what's the point?"*——只有架構、缺開箱即用能力
- *"47mb downloaded, 1.5gb after build"*——安裝與構建體積
- *"it looked just like every other harness"*——差異化不明顯
- 第三方指出 `/memory`、`/tasks` 等命令尚不可用，skills 生態不完整
- Cordis 論文的"時空可組合性"表述被譏為堆砌辭藻

反面觀察：這些批評全部是價值判斷或成熟度問題，**沒有人對"一切皆插件"、"基於 Cordis"這類事實性描述提出反駁**。爭議在"值不值"，不在"是不是"。

### 6.3 兩個必須避開的引用陷阱

1. 同名第三方倉庫 [github.com/HenryZ838978/deepseek-harness](https://github.com/HenryZ838978/deepseek-harness)（附帶 pip 包與另一個 npm 包 `@deepseek-harness/mcp`）與官方項目無關。另有低質站點 deepseek-harness.org 於 2026-08-03 聲稱"未找到官方安裝器或公開倉庫"，以及個人博客稱其 agent 循環不可替換、技術棧為 Async Rust/Python——兩者均與實際的 TypeScript/npm 倉庫及官方架構文檔矛盾，不可引用。
2. 歷史上"DeepSeek 許可證不算真開源"的批評針對的是**模型權重**的 DeepSeek Model License（含使用限制），與本次 harness 代碼庫的標準 MIT 是兩回事。第三方分析（Black Duck 等）明確區分過兩者。

## 七、定位判斷

證據指向一個結論：這不是 DeepSeek 版 Claude Code，而是 DeepSeek 版"造 Claude Code 的地基"。

支撐該判斷的事實有三條：官方一次都沒提競品，一次都沒放跑分；目標受眾被明確寫為"面向全球構建 agent harness 的開發者"；README 只有 Run 一節涉及使用，其餘全是架構與貢獻指引。它賣的是可組合性（連 agent 循環都能換），不是開箱即用。

由此推出兩條實用結論：

- **作為日常編碼智能體用**：現在還早。v0.1、部分命令缺失、skills 生態不完整、破壞性變更已被官方預告。
- **作為自研內部 agent 平臺的參考或底座**：值得讀。"服務掛在上下文 + 註冊即可逆副作用 + 工具流水線可插監聽器"這套設計，把權限、沙箱、審計做成插件而不動執行核心——這恰是多數自研 harness 到中後期最痛的地方。

但另一方面，反向風險同樣明確：整套架構結論幾乎全部來自項目自身文檔（README、architecture.md、cordis-primer、官網），屬於官方設計自述加倉庫結構佐證，**不是第三方獨立審計**。"可自由混搭、替換"的工程成熟度——生態插件數量、跨版本兼容、真實可替換性——目前沒有任何外部驗證。HN 上"只有架構沒有內容"的批評，本質上就是在質疑這套抽象的兌現能力。

## 八、待解問題

1. **實測表現**：dsh 在 SWE-bench Verified / Terminal-Bench 等公開基準上的表現如何？官方零披露、第三方無獨立復現，缺一個 harness 層面的可比評測。
2. **插件生態成熟度**：`dsh-plugin` 話題下目前有多少可用第三方插件？MCP（`packages/mcp` 已存在）、subagent、workflow、skills 的完成度與 Claude Code 生態差距多大？HN 上的"缺開箱即用能力"批評是否會在後續版本被補齊？
3. **沙箱與權限強度**：`pre-execute` 階段的權限、沙箱與審批策略如何落地？`e2b` 包與 `native/` 目錄起什麼作用？是容器/系統級隔離還是僅進程內策略？這對企業部署是關鍵，本輪未深入。
4. **DeepSeek 與 Cordis 的實際關係**：cordis 倉庫 homepage 反指 DeepSeek 文檔站，vendor 內含 18 條本地改動並重新發布到 `@deepseek-ai` scope——兩者是僱傭、共建還是鬆散協作？上游演進與 vendor 分叉未來如何同步，會否形成事實分叉？
5. **技術選型**：為何選 TypeScript/Node 而非 Python（主流 agent 生態語言）？這對與 Python 側 SWE-bench 評測框架、現有 agent 工具鏈的集成成本有何影響？

## 九、方法論與引用須知

- 研究方法：5 個搜索角度並行（官方發佈事實 / 架構與插件機制 / 模型支持與工具調用 / 同類框架橫評 / 社區反饋與侷限）→ 抓取 19 個源站 → 抽取 90 條聲明 → 25 條進入三票對抗式驗證（需 2/3 票推翻才淘汰）→ 合併語義重複後保留 11 條核心結論。驗證結果：25 條確認、0 條推翻、0 條存疑。
- **star / fork / commit 數為時點快照**，核查過程中 star 就從 34292 漲到 34689，任何引用必須帶時間戳。
- 社區反饋部分主要來自 Hacker News 單帖，樣本窄且是發佈首日，代表性有限。
- 與 OpenHands / SWE-agent / Claude Code 的對比在本輪無任何可靠一手或第三方實測材料，只有媒體的定位式表述，不構成能力對比結論。
- 官方 X 帖的引文在檢索中出現過帶 Markdown 粗體的疑似二次加工版本，建議優先引用 GitHub 倉庫與 deepseek.com/harness 頁面作為來源。
- 搜索階段有一條未進入驗證環節的線索：官網疑似列出四種運行模式（Standard / Code / Minimal / Creator，部分媒體把 Code Mode 稱作 PTC 程序化工具調用）。該條未經三票驗證，僅供參考，不作結論。

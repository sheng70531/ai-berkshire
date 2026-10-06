# OpenRouter 模型使用量多維度拆解：價格歸一化前後的真實排名

> 數據快照：2026年6月23日 | 分析日期：2026年7月2日

## 核心問題

OpenRouter 上的模型使用量排行能反映模型真實好用程度嗎？答案是：**不能直接用**。原始 token 使用量基本就是價格的倒數——便宜的模型天然獲得不成比例的流量。本文通過多維度分析和價格歸一化，試圖還原一個更接近"真實好用度"的排名。

## 數據來源

- **CodeSOTA Agent Leaderboard**（主要數據源）：覆蓋46個 Agent 應用的30天使用數據，同時提供 token 量、花費、採用 app 數、#1 slot 數
- **DigitalApplied** April/June 2026 報告：周度 token 量、市場份額
- **OpenRouter 官方博客**：開源模型基準測試、定價、吞吐量
- **AICost**：月度 token 排行、中國模型分析

## 方法論

### 五個維度

| 維度 | 權重 | 含義 | 噪聲特徵 |
|------|:----:|------|----------|
| 收入（Revenue） | 30% | 用錢投票——開發者願意為這個模型花多少錢 | 偏向有錢的企業用戶 |
| 採用廣度（Apps） | 25% | 有多少不同應用集成了這個模型 | 最不受價格影響 |
| 使用量（Tokens） | 20% | 原始 token 處理量 | 價格噪聲最大 |
| 質量領先（#1 Slots） | 15% | 在多少個應用中被選為首選模型 | 樣本小但信號強 |
| 單開發者付費 | 10% | Revenue/Apps——每個開發者願意花多少 | 過濾掉"便宜才用"的噪聲 |

### 為什麼不用"token/價格"做歸一化

"每美元處理多少 token"本質上就是價格的倒數，無法提供增量信息。真正有意義的價格歸一化方法是：**在控制了價格因素後，開發者的行為是否仍然指向這個模型**——即收入、採用廣度、#1 slots 這些維度。

---

## 綜合排名 Top 20

| 排名 | 模型 | 供應商 | 綜合分 | 收入 | 使用量 | 採用 | #1 | 有效價格 |
|:----:|------|--------|:-----:|:----:|:-----:|:----:|:---:|:--------:|
| 1 | Claude Sonnet 4.6 | Anthropic | 96.4 | #1 | #3 | #3 | #2 | $6.35/M |
| 2 | MiniMax M3 | MiniMax | 86.2 | #6 | #2 | #4 | #6 | $0.55/M |
| 3 | DeepSeek V4 Pro | DeepSeek | 85.3 | #8 | #4 | #2 | #3 | $0.56/M |
| 4 | Claude Opus 4.8 | Anthropic | 84.8 | #2 | #7 | #8 | #8 | $10.60/M |
| 5 | DeepSeek V4 Flash | DeepSeek | 78.6 | #13 | #1 | #1 | #1 | $0.12/M |
| 6 | Gemini 3.5 Flash | Google | 73.1 | #7 | #14 | #5 | #11 | $3.59/M |
| 7 | GPT-5.5 | OpenAI | 72.8 | #3 | #13 | #15 | #9 | $12.01/M |
| 8 | Claude Opus 4.6 | Anthropic | 71.9 | #5 | #17 | #9 | #10 | $10.60/M |
| 9 | Claude Opus 4.7 | Anthropic | 68.3 | #4 | #16 | #12 | #16 | $10.59/M |
| 10 | Gemini 3 Flash Preview | Google | 67.2 | #12 | #12 | #10 | #4 | $1.20/M |
| 11 | MiMo-V2.5-Pro | Xiaomi | 62.9 | #14 | #9 | #6 | #13 | $0.56/M |
| 12 | Step 3.7 Flash | StepFun | 61.4 | #9 | #5 | #27 | #7 | $0.47/M |
| 13 | Laguna M.1 | Poolside | 54.0 | #17 | #6 | #19 | #14 | $0.26/M |
| 14 | Kimi K2.6 | MoonshotAI | 48.8 | #15 | #18 | #13 | #18 | $1.43/M |
| 15 | GPT-5.3-Codex | OpenAI | 44.7 | #10 | #22 | #29 | #12 | $5.19/M |
| 16 | GLM 5.2 | Z.ai | 44.1 | #16 | #20 | #17 | #19 | $1.52/M |
| 17 | Gemini 3.1 Flash Lite | Google | 41.4 | #26 | #19 | #11 | #5 | $0.60/M |
| 18 | Nex-N2-Pro | Nex AGI | 39.0 | #20 | #11 | #22 | #22 | $0.46/M |
| 19 | Claude Fable 5 | Anthropic | 36.4 | #11 | #29 | #28 | #17 | $21.21/M |
| 20 | Claude Sonnet 4.5 | Anthropic | 35.9 | #18 | #26 | #18 | #20 | $6.36/M |

---

## 各維度排名對比

### 維度一：原始使用量（Token Volume）

價格噪聲最大的維度。前10全部是 $1/M 以下的低價模型（Claude Sonnet 4.6 除外）。

| 排名 | 模型 | Token 量 | 有效價格 |
|:----:|------|:--------:|:--------:|
| 1 | DeepSeek V4 Flash | 6,420B | $0.12/M |
| 2 | MiniMax M3 | 4,530B | $0.55/M |
| 3 | Claude Sonnet 4.6 | 3,290B | $6.35/M |
| 4 | DeepSeek V4 Pro | 2,880B | $0.56/M |
| 5 | Step 3.7 Flash | 2,880B | $0.47/M |
| 6 | Laguna M.1 | 2,130B | $0.26/M |
| 7 | Claude Opus 4.8 | 1,540B | $10.60/M |
| 8 | Nemotron 3 Super | 1,470B | $0.19/M |
| 9 | MiMo-V2.5-Pro | 1,270B | $0.56/M |
| 10 | MiMo-V2.5 | 857B | $0.18/M |

**Claude Sonnet 4.6 是唯一一個以高價（$6.35/M）擠進 token 量 Top 3 的模型**——這本身就是極強的質量信號。

### 維度二：收入（Revenue = 用錢投票）

收入是最強的質量信號。願意花真金白銀，說明模型在生產環境中不可替代。

| 排名 | 模型 | 月收入 | Token 量 |
|:----:|------|:------:|:--------:|
| 1 | Claude Sonnet 4.6 | $20.9M | 3,290B |
| 2 | Claude Opus 4.8 | $16.3M | 1,540B |
| 3 | GPT-5.5 | $7.9M | 661B |
| 4 | Claude Opus 4.7 | $5.9M | 554B |
| 5 | Claude Opus 4.6 | $5.7M | 536B |
| 6 | MiniMax M3 | $2.5M | 4,530B |
| 7 | Gemini 3.5 Flash | $2.2M | 599B |
| 8 | DeepSeek V4 Pro | $1.6M | 2,880B |
| 9 | Step 3.7 Flash | $1.3M | 2,880B |
| 10 | GPT-5.3-Codex | $1.3M | 247B |

**Anthropic 前5佔了4席，總月收入 $50.1M，佔全市場的 66%。** 儘管 token 量只佔約 15%。

### 維度三：開發者採用廣度（Apps Count）

最不受價格影響的維度——開發者花時間集成一個模型，不僅僅因為便宜。

| 排名 | 模型 | Apps 數 | 有效價格 |
|:----:|------|:-------:|:--------:|
| 1 | DeepSeek V4 Flash | 36 | $0.12/M |
| 2 | DeepSeek V4 Pro | 34 | $0.56/M |
| 3 | Claude Sonnet 4.6 | 29 | $6.35/M |
| 4 | MiniMax M3 | 28 | $0.55/M |
| 5 | Gemini 3.5 Flash | 26 | $3.59/M |
| 6 | MiMo-V2.5-Pro | 26 | $0.56/M |
| 7 | MiMo-V2.5 | 25 | $0.18/M |
| 8 | Claude Opus 4.8 | 24 | $10.60/M |
| 9 | Claude Opus 4.6 | 21 | $10.60/M |
| 10 | Gemini 3 Flash Preview | 21 | $1.20/M |

**DeepSeek V4 Flash 在採用廣度上排第一，說明它的流行不僅僅是價格驅動。** 36個不同 app 選擇集成它，開發者用腳投票。

### 維度四：質量領先（#1 Slots）

在多少個應用中被選為首選模型——這是最純粹的質量信號。

| 排名 | 模型 | #1 數 | 總採用 |
|:----:|------|:-----:|:------:|
| 1 | DeepSeek V4 Flash | 6 | 36 apps |
| 2 | Claude Sonnet 4.6 | 5 | 29 apps |
| 3 | DeepSeek V4 Pro | 3 | 34 apps |
| 4 | Gemini 3 Flash Preview | 3 | 21 apps |
| 5 | Gemini 3.1 Flash Lite | 3 | 21 apps |
| 6 | MiniMax M3 | 2 | 28 apps |
| 7 | Step 3.7 Flash | 2 | 7 apps |

**只有15個模型拿到過至少一個 #1 slot。** 能在至少一個場景中成為最優選擇，本身就是很高的門檻。

### 維度五：單開發者付費（Revenue / App）

每個集成該模型的開發者平均花多少錢——過濾掉"因為免費所以用"的噪聲。

| 排名 | 模型 | 每 App 收入 | Apps 數 |
|:----:|------|:----------:|:-------:|
| 1 | Claude Sonnet 4.6 | $721K | 29 |
| 2 | Claude Opus 4.8 | $680K | 24 |
| 3 | GPT-5.5 | $496K | 16 |
| 4 | Claude Opus 4.7 | $294K | 20 |
| 5 | Claude Opus 4.6 | $270K | 21 |
| 6 | GPT-5.3-Codex | $256K | 5 |
| 7 | Step 3.7 Flash | $191K | 7 |
| 8 | Claude Fable 5 | $149K | 6 |
| 9 | MiniMax M3 | $89K | 28 |
| 10 | Gemini 3.5 Flash | $83K | 26 |

**Claude Sonnet 4.6 不僅採用廣（29 apps），每個 app 還平均花 $721K/月**——既廣又深。

---

## 價格歸一化核心發現

對比"原始 token 排名"和"綜合排名"的位差，就能看出價格在多大程度上扭曲了使用量數據。

### 被價格虛高膨脹的模型

這些模型的 token 使用量排名遠高於綜合排名——說明使用量主要由低價驅動，而非質量。

| 模型 | Token排名 | 綜合排名 | 下降 | 有效價格 | 診斷 |
|------|:---------:|:-------:|:----:|:--------:|------|
| Nemotron 3 Super | #8 | #25 | ↓17 | $0.19/M | 10個 app，0個 #1。純粹靠便宜跑批量 |
| MiMo-V2.5 | #10 | #21 | ↓11 | $0.18/M | 25個 app 但0個 #1，沒人覺得它最好 |
| MiniMax M2.7 | #15 | #24 | ↓9 | $0.44/M | 被 M3 取代後仍靠老用戶慣性 |
| Nemotron 3 Ultra | #21 | #29 | ↓8 | $0.98/M | benchmark 不錯（AA 48）但實際採用很低 |
| Step 3.7 Flash | #5 | #12 | ↓7 | $0.47/M | 只有7個 app，極度集中使用 |
| Laguna M.1 | #6 | #13 | ↓7 | $0.26/M | 2.13T token 但只有12個 app |

### 被價格壓制的模型

這些模型的 token 使用量排名遠低於綜合排名——因為貴，使用量被抑制了，但收入和採用度說明質量確實好。

| 模型 | Token排名 | 綜合排名 | 上升 | 有效價格 | 診斷 |
|------|:---------:|:-------:|:----:|:--------:|------|
| Claude Fable 5 | #29 | #19 | ↑10 | $21.21/M | 全場最貴，42B token，但月入 $891K |
| Claude Opus 4.6 | #17 | #8 | ↑9 | $10.60/M | 21個 app 願意以 $10.60/M 持續用 |
| Gemini 3.5 Flash | #14 | #6 | ↑8 | $3.59/M | 26個 app，價格適中但採用極廣 |
| Claude Opus 4.7 | #16 | #9 | ↑7 | $10.59/M | 20個 app，$5.87M 月收入 |
| GPT-5.3-Codex | #22 | #15 | ↑7 | $5.19/M | 只有5個 app 但月入 $1.28M，極度垂直 |
| GPT-5.5 | #13 | #7 | ↑6 | $12.01/M | $7.94M 月收入，收入排第三 |

---

## 關鍵洞察

### 1. Token 使用量 ≈ 價格的倒數

DeepSeek V4 Flash 處理了 6.42T token（第一），但收入只有 $739K（第十三）。Claude Sonnet 4.6 的 token 量只有它的一半，但收入是它的 **28倍**。如果只看 token 排行榜，你會以為 DeepSeek V4 Flash 是市場上最好的模型——但它更多是"最便宜的夠用模型"。

### 2. 收入是最強但有偏差的質量信號

Anthropic 6個模型拿走了 $50.1M 月收入（佔全市場66%），但 token 只佔15%。這說明企業用戶真的認為 Anthropic 的模型更好，願意為此付出 10-20 倍的價格溢價。但這也意味著收入排行偏向"有預算的企業選什麼"，不代表"最佳性價比"。

### 3. 採用廣度是最乾淨的信號

開發者花時間集成一個模型，成本遠高於切換價格——這意味著 apps 數量相對不受價格影響。在這個維度上，DeepSeek V4 Flash（36 apps）和 DeepSeek V4 Pro（34 apps）排在前兩位，說明它們的流行不僅僅是價格效應。

### 4. 四個維度都靠前的才是"真正好用"

- **Claude Sonnet 4.6**：四個維度全部 Top 3，唯一一個。絕對統治力。
- **MiniMax M3**、**DeepSeek V4 Pro**：便宜但採用和領先度都強，不只是靠價格。
- **GPT-5.5**：收入第三但採用只有16個 app，主要靠少數高付費用戶。

### 5. 中國模型：token 佔51%，收入佔7%

中國模型（MiniMax、DeepSeek、Xiaomi、Moonshot、Z.ai、Qwen）在 token 量上已經超過一半，但收入貢獻不到十分之一。這個差距的核心解釋是價格策略——中國模型普遍以 1/10 到 1/100 的價格競爭。例外是 MiniMax M3，在採用和質量領先維度都表現突出，不只是靠便宜。

### 6. 對投資者的啟示

如果你在評估 AI 模型/公司的競爭力：
- **不要看 token 使用量排行榜**——它基本就是價格的倒數
- **看收入 + 採用廣度的交叉**——Claude Sonnet 4.6 在兩個維度都是 Top 3，這才是真正的護城河
- **注意"價格膨脹型"模型**——Nemotron 3 Super 的 token 量看起來很大，但下降17位後才是它的真實位置
- **關注價格彈性**——如果一個模型漲價後使用量驟降，說明用戶忠誠度低；如果維持住了（如 Claude Opus 系列），說明切換成本高

---

## 供應商分佈（Top 20）

| 供應商 | 模型數 | 總收入 | 總 Token | 平均價格 |
|--------|:------:|:------:|:--------:|:--------:|
| Anthropic | 6 | $50.1M | 6.0T | $8.35/M |
| OpenAI | 2 | $9.2M | 0.9T | $10.22/M |
| Google | 3 | $3.2M | 1.7T | $1.88/M |
| MiniMax | 1 | $2.5M | 4.5T | $0.55/M |
| DeepSeek | 2 | $2.3M | 9.3T | $0.25/M |
| StepFun | 1 | $1.3M | 2.9T | $0.47/M |
| Xiaomi | 1 | $0.7M | 1.3T | $0.56/M |
| MoonshotAI | 1 | $0.6M | 0.5T | $1.43/M |
| Z.ai | 1 | $0.6M | 0.4T | $1.52/M |
| Poolside | 1 | $0.5M | 2.1T | $0.26/M |
| Nex AGI | 1 | $0.4M | 0.8T | $0.46/M |

---

## 數據來源

- [CodeSOTA Agent Leaderboard](https://www.codesota.com/agentic/openrouter-models)（主數據源，46個 Agent 應用30天快照）
- [OpenRouter Rankings April 2026 - DigitalApplied](https://www.digitalapplied.com/blog/openrouter-rankings-april-2026-top-ai-models-data)
- [OpenRouter June 2026 Roundup - DigitalApplied](https://www.digitalapplied.com/blog/openrouter-new-models-june-2026-roundup-pricing-rankings)
- [OpenRouter: The Open Weight Models That Matter June 2026](https://openrouter.ai/blog/insights/the-open-weight-models-that-matter-june-2026/)
- [AICost: Chinese Models Dominate](https://aicost.org/blog/openrouter-monthly-token-usage-ranking-2026-chinese-models-dominate)
- [OpenRouter Data Page](https://openrouter.ai/data)

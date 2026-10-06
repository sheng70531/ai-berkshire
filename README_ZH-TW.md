繁體中文 | [簡體中文](README.md) | [English](README_EN.md) | [日本語](README_JA.md)

# 這個 repo 能做什麼

把巴菲特、芒格、段永平、李錄的研究方法寫成固定流程，讓 Claude Code 或 Codex 照著做投資研究。直接問模型，通常得到兩面都對、最後叫你自己判斷的文章。這裡強制給出通過、不通過或灰色地帶，四個視角會互相打架，關鍵數字用程式算，不靠模型心算。

## 研究一家公司

| Skill | 用途 |
|---|---|
| [`/investment-checklist`](skills/investment-checklist.md) | 買進前六關快篩，約 10 分鐘決定這家值不值得往下研究 |
| [`/investment-research`](skills/investment-research.md) | 一家上市公司做完整研究：生意、護城河、競爭、管理層、長期確定性、評價與安全邊際，最後給出能不能買 |
| [`/investment-team`](skills/investment-team.md) | 同一家公司開 4 個 Agent 同時做，再綜合。搜得更廣，四個結論也不會先講好 |
| [`/management-deep-dive`](skills/management-deep-dive.md) | 管理層才是關鍵時，單獨把人挖深 |
| [`/private-company-research`](skills/private-company-research.md) | 未上市公司、公開數字很少。從公開說明書、母公司財報、融資新聞拼資料，每筆標信心，並列出怎麼退出 |
| [`/deep-company-series`](skills/deep-company-series.md) | 把一家公司拆成一連篇長文，從重新認識寫到做出決策 |

## 讀財報

| Skill | 用途 |
|---|---|
| [`/earnings-review`](skills/earnings-review.md) | 只讀原始財報，不靠券商報告轉述 |
| [`/earnings-team`](skills/earnings-team.md) | 四個視角一起讀財報，再整理成一篇文章 |

## 看一個行業

| Skill | 用途 |
|---|---|
| [`/industry-research`](skills/industry-research.md) | 畫出一條產業鏈，看每個環節誰在賺 |
| [`/industry-funnel`](skills/industry-funnel.md) | 一個行業從全市場收到大約 10 家，再收到 3 家。留下的、淘汰的都寫原因 |
| [`/quality-screen`](skills/quality-screen.md) | 用 7 條硬指標一次掃掉不夠格的公司。個股、行業、指數、主題都可以 |
| [`/bottleneck-hunter`](skills/bottleneck-hunter.md) | 從一個大趨勢找出供應鏈上真正卡住的環節 |
| [`/era-alpha`](skills/era-alpha.md) | 判斷一條時代級主軸裡誰是核心，以及什麼情況該進、該出 |

## 買進之後

| Skill | 用途 |
|---|---|
| [`/income-investment`](skills/income-investment.md) | 看配息是不是真的發得出來，還是殖利率陷阱 |
| [`/portfolio-review`](skills/portfolio-review.md) | 看整個組合：部位、集中度、要不要再平衡 |
| [`/thesis-tracker`](skills/thesis-tracker.md) | 買進之後持續追蹤當初的論點還在不在 |
| [`/thesis-drift`](skills/thesis-drift.md) | 對兩份研究，分出是事實變了、評價變了，還是只是措辭變了 |
| [`/news-pulse`](skills/news-pulse.md) | 股價突然大漲或大跌時，約 10 分鐘判斷是基本面、情緒，還是原因根本不清楚 |

## 其他

| Skill | 用途 |
|---|---|
| [`/dyp-ask`](skills/dyp-ask.md) | 用段永平的問法想一個生意、投資或人生問題 |
| [`/financial-data`](skills/financial-data.md) | 規定關鍵數字至少兩個獨立來源，對不上就標出來 |
| [`/wechat-article`](skills/wechat-article.md) | 把研究寫成一篇文章 |

數字不交給模型口算。市值（股價 × 股本）、本益比、多來源對帳、三種情境的目標價，都用 `tools/financial_rigor.py` 以精確十進位計算。報告也可以用 `tools/report_audit.py` 抽查。

已經跑出來的研究在 [研究報告索引](reports/README.md)，按公司與專題排列。

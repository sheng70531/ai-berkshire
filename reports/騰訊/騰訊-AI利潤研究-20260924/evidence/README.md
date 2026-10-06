# 證據與審計說明

資料截止2026-09-24。報告的三個層次必須分開：歷史事實、研究假設、由假設計算的結果。財務核對沒有也不能證明2036預測正確。

## 實際執行

- 使用investment-team的四個並行角色完成商業、財務、行業、風險研究；主報告由組長整合。風險角色在報告寫成後再次讀取主文與model.py，未發現必須修訂的口徑/算術問題。
- `financial-rigor.txt`：12項跨來源核對、官方股數市值核算、估值和三情景終值、關鍵公式核算。模型另用Decimal實現，消除工具calc浮點尾差。
- `report-audit-extract.txt`：原報告提取156個數據點、隨機種子42、15%抽樣得到24項。
- `audit-results.json`及`audit-verdict.txt`：24項匹配，其中5項歷史事實、11項公式重算、8項假設一致性。後三類中的公式和假設檢查不屬於外部事實驗證；不能將24/24解釋為24項預測已獲外部證明。
- 5項歷史樣本里，2024營收及IFRS歸母有公司原文和Stockanalysis兩來源；2026H1歸母、Q2精確non-IFRS經營利潤、剔預付FCF只有本輪取得的發行人精確口徑，獨立第二來源不足。已保留缺口，沒有用同一公司不同網址冒充獨立來源。
- `decimal-valuation.json`：同日股價、股本及參考匯率的Decimal復算。

## 復現

在項目根目錄執行：

```bash
python3 reports/騰訊/騰訊-AI利潤研究-20260924/model.py
python3 tools/report_audit.py extract --report reports/騰訊/騰訊-AI利潤研究-20260924/騰訊-investment-team-AI利潤與競爭格局.md --seed 42
python3 reports/騰訊/騰訊-AI利潤研究-20260924/evidence/validation.py
```

validation.py中的歷史取值是本次聯網讀取後登記的證據，不會在復現時自動重新聯網；復現只能重算，更新財報需要重新取數。

## 來源定位和交叉核對

| 信息 | 主來源 | 第二來源 / 限制 |
|---|---|---|
| 2023—2025營收、IFRS歸母 | 騰訊2023/2025全年業績原文及比較列 | Stockanalysis年度表，一致 |
| 2025 non-IFRS歸母 | 騰訊2025業績原文 | 36氪2026-03-18報道，一致 |
| 2024 non-IFRS歸母 | 騰訊2025原文比較列 | 本輪未取得獨立二源；不能因歷史已廣為引用而自動標雙源 |
| 2026Q2收入、IFRS歸母、確認資本開支 | 騰訊Q2原文 | Reuters，四捨五入誤差低於1% |
| Q2 non-IFRS歸母、實際FCF | 騰訊Q2原文 | MarketWatch，四捨五入誤差低於1% |
| H1歸母 | 港交所H1業績公告頁2 | Q1+Q2可重算，但同一發行人，並非獨立驗證 |
| H1現金流及SBC | 騰訊完整版中報、2025/2026利潤調節表 | 無獨立同口徑全覆蓋，參考而非雙源認證 |
| 9月24日股價438.40港元 | Stockanalysis歷史表 | Investing歷史表，一致；未採用曾出現的過時搜索摘要437.80 |
| 當日股數9,095,133,109 | 騰訊翌日披露報表第一頁 | 平臺約90億股相差1.046%，原始披露優先 |
| 每港元0.8559人民幣 | Investing港元人民幣歷史表 | ExchangeRates UK同日參考值；時間截點未必相同 |

主要原始網址：

- [2025業績原文](https://static.www.tencent.com/uploads/2026/03/18/e6a646796d0d869acc76271c9ee1a6a5.pdf)
- [2023業績原文](https://static.www.tencent.com/uploads/2024/03/20/ebbe5a148484d3a0911109cdc82d1430.pdf)
- [2026Q2業績原文](https://www.tencent.com/wp-content/uploads/2026/08/Tencent-Announces-2026-Second-Quarter-Results.pdf)
- [港交所中期業績公告](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0812/2026081200296.pdf)
- [騰訊完整中報](https://www.tencent.com/wp-content/uploads/2026/08/E700_IR.pdf)：瀏覽解析超時，下載及pdftotext成功。Q2及中期公告已另行打開；中報未偽裝成瀏覽工具成功解析。
- [當日股份披露](https://static.www.tencent.com/website-2026-upload/e_Next-Day-Disclosure-Return_20260924-9bc5db.pdf)：網頁解析空，直接下載並提取文字核得股本。未把Q2加權股數當作9月期末股數。
- [Stockanalysis損益](https://stockanalysis.com/quote/hkg/0700/financials/)、[現金流](https://stockanalysis.com/quote/hkg/0700/financials/cash-flow-statement/)、[統計](https://stockanalysis.com/quote/hkg/0700/statistics/)
- [Reuters Q2報道](https://www.reuters.com/business/retail-consumer/chinas-tencent-posts-11-second-quarter-revenue-rise-profit-misses-estimates-2026-08-12/)
- [MarketWatch Q2報道](https://www.marketwatch.com/story/another-ai-lab-is-burning-through-cash-as-tencent-earnings-rise-1251b4c6)
- [36氪2025年度結果](https://www.36kr.com/p/3728291911613317)
- [Stockanalysis行情](https://stockanalysis.com/quote/hkg/0700/history/)、[Investing行情](https://www.investing.com/equities/tencent-holdings-hk-historical-data)
- [Investing匯率](https://www.investing.com/currencies/hkd-cny-historical-data)、[ExchangeRates UK匯率](https://www.exchangerates.org.uk/HKD-CNY-spot-exchange-rates-history-2026.html)

## 未被工具綠色標識解決的問題

1. `cross-validate`以中位數為分母；項目規範以主來源為分母。本報告股本差異按官方主來源計算為1.046%，儘管前者可能判一致，仍標差異。
2. 公司FCF與平臺FCF相差18.06%，確認資本開支與付款相差10.46%；屬於口徑問題，沒有把兩者平均，也未強行塞入“通過”事實樣本。
3. 9月法定股數與平臺經濟股數差異可能涉及獎勵計劃持股、回購、更新時點，不保證全部由四捨五入導致；官方股數市值相對平臺相差約1.20%。
4. 股權薪酬：2025 non-IFRS歸母調節加回347.11億；2026H1為149.49億。300億年度經濟成本假設參照H1年化量級，不是可忽略股權薪酬。2036金額仍是情景假設。
5. Aastocks基本財務頁及Macrotrends未能取得可用數據；Aastocks報價緩存為8月26日，不能充當9月24日價。改用公司原文、Stockanalysis及獨立新聞報道，並保留覆蓋缺口。
6. 2036三情景終值工具固定股數、匯率及PE，未加入回購或分紅，也沒有給出折現內在價值；不要把其終值年化價格回報視為完整股東總回報。

## 研究假設的證據邊界

新AI虧損、業務自然增速、AI帶來的額外收入、貢獻率、2036分部收入/利潤率、稅後歸母轉化及經濟成本扣減均由研究者設定。公司尚未披露足以逐項估計AI淨貢獻的分部賬目。模型目的是使觀點可復算、可檢驗，非給不可觀測的反事實貼上精確事實標籤。

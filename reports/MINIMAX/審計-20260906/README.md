# 研究審計說明（2026-09-06）

本目錄保存原件、復算與隨機抽檢。報告是研究情景，不是收益承諾。原件PDF與pdftotext文本按文件同名對應。所有取得日期為2026-09-06；價格時點為2026-09-04收盤。匯率是官方中間價，非收盤成交匯率。

- `financial-rigor.txt`：市值、雙源收入/歸母利潤/現金、股本、估值和情景計算。
- `模型結果.json`：完整表達式與工具輸出數值；`comparison_summary.json`：用Decimal獨立復算三情景退出價和逐年股息。
- `基礎模型腳本.py`、`補充模型腳本.py`：從倉庫根目錄運行後者，可復算兩家公司（會更新兩家本日期審計計算文件）。calc原工具先評估表達式，重要每股估值另以Decimal獨立實現複核，未將浮點輸出包裝為無限精度。
- `audit-extract.txt`：實際運行report_audit extract，seed42；`audit-results.json`只含可觀測事實或可復算數學；`audit-assumptions.json`記錄被抽中的預測輸入，未偽造fetched字段。
- `audit-verdict.txt`：工具對11項事實/計算判PASS、零差異警告。此PASS只表示樣本數值誤差合格，不是事實全覆蓋、所有第二源質量一致、未來假設已證實或監管意義的審計。未利用工具對空值跳過仍PASS的行為來掩蓋缺口。
- `抽檢腳本.py`保存真實讀數和來源URL、數學獨立實現；不會從報告數值自動填入核驗數。模型輸入單獨核對定義，不假裝是外部事實。
- 六公司共用行情與同行源見`../../六公司研究審計-20260906/market-snapshot.json`、`tencent-quotes.txt`、`peer-reference.md`和對應工具日誌。

## 來源與口徑

原件：

- [2025年報](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0422/2026042202118.pdf)：2022—2025收入毛利、IFRS與調整利潤，2024—2025現金流、股東經濟及投票結構。
- [招股書](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1231/2025123100025.pdf)：2022—2024現金流與資本開支；正文早期FCF為CFO減設備開支計算，不是官方名為FCF的指標。
- [中期公告](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082600680.pdf)：最新收入116.573、淨虧損357.997、現金等價物930.905百萬美元。完整H1現金流量表未取得。
- [8月股本月報](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0903/2026090301230.pdf)：349235308股，A/B分開。已發行總股數不是流通股數。
- [7月融資完成](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0716/2026071601147.pdf)：配售及債券淨融資。
- [關聯交易](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082601949.pdf)：雲服務額度、融資用途與阿里權益。年度上限不是實際成本。

第二源：

- [StockAnalysis財務](https://stockanalysis.com/quote/hkg/0100/financials/)：2025收入79.04、IFRS淨虧損1872百萬美元；2023毛利-0.85、2023/24虧損-269.25/-465.24；年度CFO及簡單FCF。S&P Global數據為獨立轉錄，不是獨立審計。
- [StockAnalysis資產負債](https://stockanalysis.com/quote/hkg/0100/financials/balance-sheet/)：2025現金507.62、最新930.91、2023現金206.3百萬美元；股本349.24百萬。
- [Reuters獨立報道](https://www.investing.com/news/stock-market-news/chinas-minimax-sees-revenue-nearly-quadruple-in-first-half-as-ai-demand-surges-4876820)：最新收入116.6、虧損358百萬美元，業務拆分。
- [SCMP](https://www.scmp.com/tech/big-tech/article/3365341/minimax-revenue-surges-283-remains-behind-pace-meet-forecast-amid-crowded-ai-race)：H1毛利率17.9%。
- [智通業績會轉述](https://www.webull.com/news/15472214899246080)：8月ARR8億美元；ARR是當時運行率，不是已實現年度收入。

抽樣16項：10項歷史/最新事實，1項情景毛利計算，5項模型輸入。2022調整虧損12.15百萬美元第二源僅找到[富途社區轉述](https://q.futunn.com/en/feed/115769089130500)，可信度低於Reuters/專業數據商，標記來源質量缺口；不因此否定已取得年報原件，也不稱完整高質量雙源覆蓋。創始人融資後持股/投票比例是保持舊持股數量的參考計算，未獲得截至9月的最終受益鏈重建。H1完整現金流缺口限制資金消耗判斷。

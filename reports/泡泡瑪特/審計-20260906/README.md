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

- [2025年報](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0421/2026042100395_c.pdf)：五年收入、利潤、毛利；2023使用重述收入6301002千元；2025CFO10865152千元和租賃付款608288千元。
- [中期公告](https://www.hkexnews.hk/listedco/listconews/sehk/2026/0820/2026082000354_c.pdf)：收入17172921、歸母5038384、現金12442065千元。僅取得現金流摘要，未取得完整附表。
- [8月股本](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0901/2026090102631.pdf)：1331779203股。

第二源：

- [StockAnalysis財務](https://stockanalysis.com/quote/hkg/9992/financials/)：歷史收入與歸母利潤、2022/23毛利率57.49%/61.32%。2025收入37120、歸母12776百萬元。
- [StockAnalysis現金](https://stockanalysis.com/quote/hkg/9992/financials/balance-sheet/)：2025現金13775、最新12442、2022現金685.31百萬元。
- [現金流](https://stockanalysis.com/quote/hkg/9992/financials/cash-flow-statement/)：2025CFO10865百萬元，簡單FCF與本報告租賃後口徑不同。
- [財華社](https://www.finet.hk/newscenter/news_content/6a86c2d02308290c11eadd7c)：H1收入171.73億元、歸母50.38億元、GPM69.7%與地區收入。
- [老虎公告整理](https://www.itiger.com/news/1176616877)：8月總股數1331779203。
- [國信證券歷史報告](https://pdf.dfcfw.com/pdf/H3_AP202401051616654746_1.pdf)：2022A現金685百萬元，與StockAnalysis685.31交叉。只採用該明確歷史現金數，不將其預測和現金流標準化口徑搬入報告。

抽樣14項：9項事實、2項情景計算、3項模型輸入，參數未填寫偽fetched。2022現金已兩獨立數據商/券商交叉，未在本輪下載早期原件，屬於原件歸檔缺口。早期現金流只保留第二源顯示精度。當前股數以港交所月報為準；StockAnalysis當前市值和股數較低且差異未完全解釋，未靜默替換。王寧48.73%為年末被視為權益，簡單穿透約46.00%不是完整最終受益披露。

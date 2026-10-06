# PDD研究來源與複核記錄

資料截止2026-09-06，行情為2026-09-04正規82.21美元；82.30是盤後。財報默認百萬元人民幣。報告完成研究與抽樣檢查，明確分部盈利、其他損失組成、最新現金資本開支和可立即分配母公司現金的缺口。

## 原件及獨立來源

- [2025年報SEC原件地址](https://www.sec.gov/Archives/edgar/data/1737806/000110465926050727/pdd-20251231x20f.htm)直接curl遇403；[同一SEC發行人申報鏡像](https://cdn.yahoofinance.com/prod/sec-filings/0001737806/000110465926050727/pdd-20251231x20f.htm)已完整下載為 `2025官方鏡像.html`，解析 `2025官方.txt`。鏡像不算第二來源。年報2025收入431845.713、經營利潤93102.131、歸母97842.539、普通股稀釋EPS16.50（每ADS×4）、股權報酬7936.971。
- [2023年報原件](https://investor.pddholdings.com/static-files/e9586d93-bb1d-4e98-af8a-4e73b62350f2)：web可讀取，curl403。2021/22/23收入93949.939/130557.589/247639.205；歸母7768.670/31538.062/60026.544，成本31718.093/31462.298/91723.577。沒有將失敗下載偽裝為PDF保留。
- [2026Q2公告與完整半年財務表](https://investor.pddholdings.com/news-releases/news-release-details/pdd-holdings-announces-second-quarter-2026-unaudited-financial/)：Q2收入112358、歸母27182、營業27764；H1收入218587、歸母39729、營業47330；H125對應199657/45496/41879。現金128918、短投327496、受限77274、全部負債215620；其中商家應付109924、保證金18545。公司不披露單獨Temu完整利潤表。
- [2025初步年度公告](https://investor.pddholdings.com/news-releases/news-release-details/pdd-holdings-announces-fourth-quarter-2025-and-fiscal-year-2025)：歸母99364.469、經營94624.061；審計年報分別少1521.930，管理費用相應增加。不對差異原因作無證據命名，TTM使用審計版本。
- [2025Q3公告](https://investor.pddholdings.com/news-releases/news-release-details/pdd-holdings-announces-third-quarter-2025-unaudited-financial)：收入108276.5、營銷53347.6、交易54928.9；Q4收入123912.194、營銷60010.1、交易63902.1。Q1由半年減Q2計算。
- [StockAnalysis獨立數據庫](https://stockanalysis.com/stocks/pdd/financials/)：2021—2025收入93950/130558/247639/393836/431846、歸母7769/31538/60027/112435/97843、2025經營利潤93102；現金短投456414、經營現金流2025為106939、TTM111895。採用S&P Global/Fiscal.ai標準化數據而不是官網轉載。
- [FT財務數據](https://markets.ft.markitdigital.com/data/equities/tearsheet/financials?s=PDD%3ANSQ&subView=IncomeStatement)：審計年度97843和93102與SEC匹配，用於初稿差異查驗。
- [新浪科技2024年度報道](https://finance.sina.com.cn/tech/2025-03-20/doc-ineqiark3734433.shtml)：總成本2024為1539.004億元、2023為917.236億元；歸母2023為600.265億元。用於成本抽樣的第二來源，明確單位換為百萬元。
- [Reuters2026Q2](https://www.marketscreener.com/news/temu-owner-pdd-revenue-misses-estimates-profit-falls-on-intense-china-competition-ce7858dbdb8bf323)：收入112.36bn、歸母27.2bn人民幣，與原件112358/27182容差內。報道調整後EPS不與GAAP估值混用。
- [歐盟Temu罰款原件](https://digital-strategy.ec.europa.eu/en/news/commission-fines-temu-eu200-million-breaching-digital-services-act)、[AP獨立報道](https://apnews.com/article/07f53e968da89562e3f032abfa626fa4)：2026年5月DSA風險評估義務罰款€200m。沒有證據映射到本季具體費用項目。
- [獨立行情](https://www.trading212.com/trading-instruments/invest/PDD.US)、[StockAnalysis正規與盤後](https://stockanalysis.com/stocks/pdd/financials/)、騰訊財經共享原始 `../../六公司研究審計-20260906/market-snapshot.json`：正規82.21、盤後82.30。實際ADS以20-F5693585848/4算，而模型固定稀釋14.8億ADS。
- [新華社9月4日中間價](https://english.news.cn/20260904/790d1ee7b6864f7b96752579a210e783/c.html)：美元人民幣6.7787，與SAFE同日中間價對應，不是市場收盤即期匯率。

## 現金、利潤與治理限制

TTM歸母使用97842.539+39729-45496=92075.539，經營利潤93102.131+47330-41879=98553.131。2025全年稀釋普通股EPS16.50×4+H126ADS26.90-H125ADS30.69=62.21人民幣；與數據庫62.26為加權期數拼接微差，不叫直接披露TTM。正常化基數98553.131×80%+8000－1842.5048=85000，稅率與利息及緩衝都是假設。

現金SOTP=現金+短投+受限－全部負債－假設營運資金50000，再只做一次20%折價。受限資源與商家義務未雙扣；全負債包含非流動債務但其他非流動投資不計，是保守壓力口徑，不宣稱精確可分配金額。PE主模型已包含利息，不額外加現金；SOTP主業剔除全部利息再加淨資源，兩法不可相加。

2025年報截至2026年3月18日持股：黃錚1409744080、騰訊783468116、合夥安排370772220普通股。沒有B類股發行在外，不能沿用早年10倍投票控制權。合夥人提名條款有條件，不能說所有特別任命權均已觸發。最新母公司現金匯出能力未全量核驗，報告不用全合併現金推斷可立即派息。

## 工具和審計

計算入口在 `../../騰訊/審計-20260906/複核計算.py`；本目錄保存 `工具原始輸出.json/txt`、`估值模型.json`。市場市值、收入/歸母/現金交叉、披露與正常化估值、三情景和所有派生財務均經financial_rigor工具計算。源記錄明確每項輸入是原件、第二源還是模型假設。

`抽樣原始輸出.txt` 是seed42 extract原輸出；`抽樣核驗.json` 事實樣本有兩源讀取值，情景目標與回報樣本以financial_rigor和獨立Decimal復算，分類為模型計算，不是外部已證實預測。`審計判決.txt/json`保留原輸出。工具的PASS只表示這些抽樣核驗通過，報告列出的缺口不因PASS而消失。

## 收尾補充

五年經營現金流表的2021—2023原始千元數為28783011/48507860/94162531，見2023年報PDF第98頁/現金流表第144頁；2024—2025原件現金流與獨立數據庫取整121929/106939一致。表格全部取整百萬元，不用它偽造最新TTM FCF。

最終seed42抽9項：6項歷史財務事實雙源、3項模型計算獨立復算。全部verdict PASS，零警告、零失敗，無未核驗財務樣本。模型樣本不是外部事實，完整範圍見 `審計範圍.json`；分部經濟性、最新現金資本支出、母公司可分配資金等缺口仍存在。

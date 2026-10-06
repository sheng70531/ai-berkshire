# 本輪實時核驗記錄

日期：2026年9月6日。歷史財務原件及其雙源核驗承接同日已完成的騰訊、拼多多單公司審計與七公司商業模式底稿，不復制整份舊研究。

| 項目 | 來源 | 本輪結果 |
|---|---|---|
| 騰訊9/4正規收盤442.80港元 | https://stockanalysis.com/quote/hkg/0700/history/ ; https://kr.investing.com/equities/tencent-holdings-hk-historical-data | live讀取相符；來源S&P與Investing，非兩個同源S&P網站 |
| PDD9/4正規收盤82.21美元 | https://stockanalysis.com/stocks/pdd/history/ ; https://chartexchange.com/symbol/nasdaq-pdd/historical/ | live讀取歷史表相符；頂部最後逐筆82.20與盤後82.30另列，不混用 |
| 騰訊已發行9,103,153,877股 | https://www.tencent.com/wp-content/uploads/2026/09/e_Next-Day-Disclosure-Return_20260904.pdf | web解析失敗；curl實時下載成功，SHA256與同日先前取得原件一致。第1頁closing balance Sep 4 |
| PDD實際普通股5,693,585,848 | https://investor.pddholdings.com/static-files/92dafbdc-3125-4f2c-a28f-3d61203efbaf | live讀取第120頁，日期2026-03-18；封面另有2025-12-31相同數值。不是9/4新股本 |
| PDD半年加權稀釋股數、4普通股/ADS | https://investor.pddholdings.com/news-releases/news-release-details/pdd-holdings-announces-second-quarter-2026-unaudited-financial/ | live讀取股數表；半年5,907百萬普通股、季度5,894百萬普通股；均不可代替期末已發行股數 |
| 匯率美元6.7787、港元0.86458人民幣 | https://hzf.mofcom.gov.cn/article/zyfw/jrfw/jrfwywzn/jrfwwh/hlfxglzy/202609/7872.html ; https://www.moneydj.com/KMDJ/news/newsviewer.aspx?a=9a21ef2e-aa18-4653-a227-23b2f44194d2 | live搜索結果返回兩個數值；商務部正文open超時。公告為9月4日官方中間價 |
| PDD不預期可預見未來分紅 | 同上PDD20-F，第16、67、125頁 | live讀取確認；不意味著承諾永不分配，也不把未來回購寫成事實 |

騰訊原件本輪下載路徑為臨時目錄，不作為交付依賴；長期可用已保存原件為`../../騰訊/審計-20260906/20260904翌日披露.pdf`。兩份SHA256相同：`1880daaf638ba97d22cc3376fe7f7e82e3067641ce59de484544d9da360bcdd2`。

官方股本優先於行情網站取整股數。精確股本沒有宣稱雙源同等精度確認；價格和匯率經過雙源數值比較，獨立性不等同於逐筆行情采集鏈完全可知。

`audit.py`將seed42抽中的1項官方股本事實、13項模型輸入/重算和1項誤抽月份分開。模型復算通過不表示預測被證實；股本事實僅單源官方確認，不包裝成雙源。

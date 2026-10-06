# 來源與證據邊界

檢索與訪問日期：2026-09-26，北京時間。這裡只保存研究使用的事實與口徑，不復制來源全文。

正文編號指向下列資料。統計、研究估計、機構預測、公司公告、政策與研究者推斷分別處理；同一機構不同頁面不算獨立雙源。

## S01 · 固定能力成本

- 來源：Luke Emberson、David Roodman，Epoch AI，[The plunging price of thought](https://epoch.ai/publications/the-plunging-price-of-thought)，2026-09-22。
- 使用事實：作者對自 2023 年以來給定測試表現的成本估計，約每季度下降 47%、每年降低至此前約十三分之一。正文只使用約每年 13 倍。
- 口徑：模型與推理預算所形成的最低費用—表現邊界；主要涵蓋五組數學、科學與博弈測試。
- 限制：這不是所有企業實際支付價格指數，更不是完整現實交付成本。基準優化、數據缺口、模型切換成本和不同任務差異均有限制。作者自己討論這些限制。
- 證據類型：研究估計；成本千倍下降是用戶設定，不由該研究“驗證”。

## S02 · 可靠性與任務時長

- 來源：Thomas Kwa，METR，[Clarifying limitations of time horizon](https://metr.org/notes/2026-01-22-time-horizon-limitations/)，2026-01-22。
- 使用事實：任務時長指標用人類基準所需時間標定任務，不是 AI 實際可以自主運行多久；一定成功率上的時長也不能直接等同於可委託的工作範圍。
- 限制：具體模型時長變化很快，本文不沿用該說明中的舊模型排行與具體小時數。
- 證據類型：原研究團隊方法說明。

## S03 · 能力分佈不均

- 來源：Stanford HAI，[The 2026 AI Index Report](https://hai.stanford.edu/ai-index/2026-ai-index-report)，2026 版。
- 使用事實：技術進步在不同任務之間仍存在明顯差異，研究報告用多個測試說明這一點。
- 限制：本文不將其組織採用率、消費者福利估計或單項分數外推至 2036 年。頁面是研究彙編入口，具體測試仍有各自樣本和口徑。
- 證據類型：學術機構年度彙編。

## S04 · 數據中心用電及供給響應

- 來源：IEA，[Key Questions on Energy and AI](https://www.iea.org/reports/key-questions-on-energy-and-ai)，2026-04-16；使用其[執行摘要](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary)。
- 使用數字：2025 年全球數據中心用電約 485 TWh；2030 年約 950 TWh 是該報告更新預測。
- 口徑：全部數據中心，不是隻統計生成式 AI。2025 數值為機構對歷史用電的估計；2030 是條件預測。
- 定性證據：機構同時討論基礎設施約束與 AI 改善能源系統效率的可能性。
- 限制：不外推 2036 年總量，不由此推薦整個能源板塊；電力、接入、資本回報必須分別分析。
- 證據類型：國際機構估計與預測。同機構主題頁重複該數字，不算第二獨立來源。

## S05 · 發電與儲能併網

- 來源：Lawrence Berkeley National Laboratory，[Queued Up，2026 Edition](https://emp.lbl.gov/queues)，頁面說明 PDF 於 2026 年 6 月發佈，數據截至 2025 年底。
- 使用數字：發電 1,312 GW 加儲能約 749 GW，合計約 2,061 GW；正文保守表述為超過 2,060 GW。對有數據地區，2025 年建成項目從申請併網到商業投運的中位時長超過五年。
- 口徑：發電與儲能申請接入輸電網；排隊項目多數未必建成。這既不是即時缺電量，也不是數據中心負荷申請接電時長。
- 版本差異：2026 年 7 月新聞稿與當前項目頁對“已籤或草簽併網協議但未投運”的容量數字有差異，本文未使用該字段。正文只使用兩者不衝突的總隊列規模及項目頁的投運時長。
- 證據類型：實驗室彙編的觀測數據。有選擇偏差的投運項目時長，不代表所有申請項目。

## S06 · 工作場景的生產率改善

- 來源：Erik Brynjolfsson、Danielle Li、Lindsey Raymond，[Generative AI at Work，arXiv v2](https://arxiv.org/abs/2304.11771v2)，修訂日期 2024-11-06。
- 使用數字：5,172 名客服人員樣本；每小時解決問題數平均提高 15%。
- 口徑：分階段引入 AI 助手的客服場景，群體之間效果不同。本文用修訂稿的樣本與數字，不混入較早稿件的其他數字。
- 限制：不是隨機代表整個經濟的樣本；不推算工資、就業或 GDP。
- 證據類型：作者原論文。

## S07 · 職業暴露

- 來源：ILO–NASK，[Generative AI and jobs: A 2025 update](https://www.ilo.org/publications/generative-ai-and-jobs-2025-update)，2025-05-20。
- 使用數字：約四分之一全球就業位於具有某種生成式 AI 暴露的職業。
- 口徑：任務與職業暴露的估計，不是已經發生的崗位損失，不是十年後模型能力假設下的失業預測。
- 限制：本文不與其他機構不同定義的 AI 暴露比例平均或混用。
- 證據類型：國際組織研究估計。

## S08 · 結構預測與真實結果

- 來源：EMBL-EBI，[New AlphaFold Database entry pages](https://www.ebi.ac.uk/about/news/updates-from-data-resources/new-alphafold-database-entry-pages/)，2025-08-07。
- 使用數字：該機構說明數據庫提供超過兩億個蛋白結構預測。
- 口徑：預測，不是兩億項新實驗，也不是藥物數量。正文保留這個區別。
- 限制：用來說明可規模化數字預測的供給，不用來估計某家藥企的利潤或臨床成功率。
- 證據類型：數據庫運營機構披露。

## S09 · 專業能力擴散

- 來源：David Autor，[Applying AI to Rebuild Middle Class Jobs](https://www.nber.org/papers/w32140)，NBER Working Paper 32140，2024-02。
- 使用觀點：AI 可能擴大具備互補知識的勞動者能夠從事的專業任務範圍。
- 限制：是一條有理論和經驗討論支持的可能路徑，不是勞動收入必然上升的結論。
- 證據類型：經濟學研究與政策討論。正文明確這是研究者觀點。

## S10 · 臨床研究需要什麼證據

- 來源：FDA，[Step 3: Clinical Research](https://www.fda.gov/patients/drug-development-process/step-3-clinical-research)，訪問於截止日。
- 使用事實：臨床研究分階段積累安全性、有效性與不良反應證據。
- 限制：未引用頁面上的階段成功比例與典型時長，也不把當前美國監管流程當作所有國家或 2036 年的統一規則。
- 證據類型：監管機構流程說明，不提供個案法律或醫療意見。

## S11 · 配套組織投資

- 來源：Erik Brynjolfsson、Daniel Rock、Chad Syverson，[The Productivity J-Curve: How Intangibles Complement General Purpose Technologies](https://www.nber.org/papers/w25148)，2018 年工作論文，2020 年修訂，2021 年發表。
- 使用機制：通用技術常需配套流程、商業模式與人力資本投入，部分無形投資與收益存在測量和時間差。
- 限制：未引用論文中的歷史 TFP 數字；不能用該機制免除項目回報核驗。
- 證據類型：理論與歷史經驗研究。

## S12 · 代理交易的授權層

- 來源：Google，[We’re donating Agent Payments Protocol to the FIDO Alliance…](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/)，2026-04-28。
- 使用事實：Google 宣佈向 FIDO Alliance 移交 AP2，並介紹基於預先授權的自主交易更新。
- 限制：產品與治理公告證明該議題正在形成標準，不證明普及率、實際收入、無風險執行，或某家公司將壟斷入口。移交的治理完成度未另外核驗，正文用“宣佈”表述。
- 證據類型：公司一手公告，有商業宣傳動機。

## S13 · 溯源不是事實真偽的完整證明

- 來源：C2PA，[C2PA and Content Credentials Explainer](https://spec.c2pa.org/specifications/specifications/2.3/explainer/_attachments/Explainer.pdf)；[FAQ](https://c2pa.org/faqs/)用於交叉理解技術範圍。鏈接目錄標為 2.3，實際 PDF 封面自標 2.2、2025-12-11；本文引用 PDF 第 7.2.2 節的原則說明，不據目錄名聲稱版本。
- 使用事實：來源、歷史與完整性信息本身不能斷定內容真實、準確或符合事實。
- 限制：不聲稱該標準能防止所有偽造，也不聲稱數字簽名本身保證現實陳述為真。兩個文檔來自同一標準組織，不計為獨立來源。
- 證據類型：標準制定組織技術說明。

## S14 · 數據權利的分置

- 來源：中共中央、國務院，[關於構建數據基礎制度更好發揮數據要素作用的意見](https://app.www.gov.cn/govdata/gov/202212/19/495422/article.html)，2022-12-19 公佈。
- 使用事實：提出數據資源持有、加工使用、產品經營等權利分置的運行機制。
- 限制：政策原則不直接證明某項數據的具體權屬或排他性。個別公司的權利要查合同、來源、用途與適用規則。
- 證據類型：政策原文。

## S15 · 數據權利的解釋邊界

- 來源：張新寶，[深入貫徹落實數據產權制度 依法保障各方主體合法權益](https://www.nda.gov.cn/sjj/zwgk/zjjd/0315/20260315130425237481780_pc.html)，國家數據局刊載，2026-03-15。
- 使用觀點：區分持有、使用和經營等權利，討論數據非排他性與流轉。
- 限制：官方站點刊載的專家解讀，不冒充具體法條、司法判決或新設所有權。
- 證據類型：專家解釋，證據地位低於直接適用的法律和裁判。

## S16 · 從任務到宏觀

- 來源：Daron Acemoglu，[The Simple Macroeconomics of AI](https://www.nber.org/papers/w32487)，NBER Working Paper 32487，2024-05，後發表於 Economic Policy。
- 使用機制：宏觀生產率效應應考慮受影響任務範圍、任務成本節約和互補關係。
- 限制：本文未採用該論文的十年 TFP 數值作為本題預測，更未把它當作任何未來技術的上限。
- 證據類型：任務框架下的條件模型。

## 本報告自己的假設與推斷

以下內容沒有冒充外部事實：

1. 千倍降價是用戶給定前提；年度降幅是數學換算。
2. 成本佔比、需求彈性、獨立錯誤概率與租金現值都是演示參數。
3. 對客戶授權、可信交付、真實反饋的排序是研究判斷。
4. 三個 2036 年情景不分配概率，也不是已發生的事實。
5. 人的健康時間、真實關係和自主性的重要性含有價值判斷，不能用單一市場價格證明。
6. 商業模式觀察表不包含任何已核驗的個股投資建議。

主報告鏈接保持集中且就近；複核者可據本文件追溯口徑。未將舊倉庫文章的具體預測與數字當作本次證據。

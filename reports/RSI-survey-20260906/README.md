# RSI 中英文綜述工作稿

文獻截止：**2026-09-06**。這裡的 RSI 指 Recursive Self-Improvement（遞歸自我改進）。

已完成一篇約 6,500 英文詞的批判性敘述綜述，以及約 11,300 漢字的對應中文版。兩版使用相同的 53 條參考文獻、同一組關鍵事實和相同的核心公式。中文末尾另附術語對照。未添加未經確認的作者、單位或郵箱，未提交到 arXiv。

## 閱讀與修改

- 英文 PDF：`../../output/pdf/rsi-survey-en-20260906.pdf`
- 中文 PDF：`../../output/pdf/rsi-survey-zh-20260906.pdf`
- 英文編輯稿：`manuscript-en.md`
- 中文編輯稿：`manuscript-zh.md`
- 英文 LaTeX 主文件：`arxiv/main.tex`
- 中文 LaTeX 主文件：`arxiv/main-zh.tex`
- 參考文獻：`arxiv/references.bib`
- 英文 arXiv 源碼壓縮包：`rsi-survey-arxiv-source.zip`
- 逐條證據與數值限定：`research/evidence-ledger.md`
- 來源登記：`research/source_register.md`
- 檢索方式記錄：`research/search-log.md`
- 檢查結果：`research/validation-report.md`

## 論文定位

英文題目：**Recursive Self-Improvement in AI: A Critical Survey of Mechanisms, Evidence, and Evaluation**

中文題目：**人工智能遞歸自我改進：機制、證據與評估的批判性綜述**

論文主線是：區分改好一個答案、持久改變一個系統，以及改善下一輪改進的方法。對於自修改編程智能體、模型自編輯、自訓練和自動化科研，分別考察修改對象、反饋、繼承關係和實驗邊界。

已有綜述已覆蓋“什麼進化、何時進化、如何進化”和改進機制可修改等主題；HGM 也已提出當前表現與後代產出能力的區別。本文明確引用這些工作，不聲稱首次提出 RSI 分類、可修改改進機制或 metaproductivity。較集中的寫作切口是把這些問題與 2026 年出現的新評估基準、匹配改進者對照和資源核算聯繫起來。

提出的算子產出度量和評估協議屬於綜合性方法建議，尚未開展實驗驗證。稿件屬於敘述綜述，不是窮盡式系統綜述，不報告虛構的篩選總數、統計元分析或復現實驗。

## 值得保留的關鍵限定

1. 當前所選文獻支持多種有邊界的自我改進，不能據此宣稱已實現通用、持續、成本校正後的遞歸加速。
2. 權重變化既不是 RSI 的必要條件，也不是充分條件；需要說明覆合系統的邊界。
3. “零數據”描述特定後訓練輸入條件，並不抹去預訓練、環境和人類設計的監督結構。
4. DGM 的 20%→50% 是論文特定 SWE-bench 子集的結果，不能改寫為完整官方成績。
5. 自我改進的歷史最佳曲線按定義不會下降；需要檢查當前系統、合法驗證選優結果和事後審計最優值。
6. 2026 年的新預印本按照作者報告處理；核對書目信息不等於獨立復現。

## 編譯

在本目錄執行：

```bash
python3 research/build_bibliography.py
python3 build.py
```

需要 Pandoc、pdfLaTeX、XeLaTeX、BibTeX。英文稿使用標準 TeX 字體；中文稿的 `arxiv/preamble-zh.tex` 當前使用本機 macOS 宋體路徑，換電腦時可改為已安裝的中文字體。英文 arXiv 包不依賴這些中文字體，也不包含中文稿或其字體路徑。

只編譯英文提交包時，在 `arxiv/` 中執行：

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

壓縮包只有 `main.tex`、`main.bbl`、`references.bib` 和 `figure-loop.tex`，不包含參考論文緩存或臨時編譯文件。正文中的書目鍵通過 Pandoc 轉換為正式引用。

## 提交 arXiv 前的定稿步驟

1. 補充真實英文署名、單位、郵箱；明確每位作者同意署名，並審閱全文。當前沒有代填任何個人身份。
2. 人工複核證據臺賬中與論點最相關的原文段落，尤其是新預印本的評估設置和侷限；結合個人判斷重寫核心論證。若希望獲得更強原創貢獻，可實施第 6 節的匹配算子實驗，再把結果加入稿件；綜述稿本身沒有把該實驗寫成已完成。
3. 編輯 Markdown 後運行 `build.py`；若直接編輯 `arxiv/main.tex`，不要再運行會覆蓋它的生成步驟。作者修改與文字修改應保存在同一源文件流程中。
4. 使用英文源碼包創建投稿，選擇與內容匹配的類別（可先考慮 cs.AI，是否交叉到 cs.LG/cs.CL 取決於最終稿重點），填寫標題和摘要，按賬戶狀態完成必要步驟，再檢查平臺重新編譯的 PDF。
5. 工作稿帶有真實的 AI 輔助說明。最終作者需要根據實際工作流程確認其表述，並對文稿內容負責。

arXiv 官方要求提交與主文對應的源文件和所需參考文獻文件，並要求投稿者檢查重新編譯的 PDF，詳見[TeX 投稿說明](https://info.arxiv.org/help/submit_tex.html)和[投稿總覽](https://info.arxiv.org/help/submit/index.html)。如果還計劃將中文版一併提交，應先查看[譯本說明](https://info.arxiv.org/help/translations.html)，按同一作品的譯本處理。本交付沒有為兩種語言創建重複投稿，也不保證平臺收錄或學術同行評審結果。

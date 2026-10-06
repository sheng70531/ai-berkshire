# 審計說明

核驗日期：2026-09-26。

## 結果與含義

- 固定種子 42、抽樣比例 15%；工具從主報告識別 29 個候選數據點，抽中 5 項，全部核驗。
- 擴展檢查覆蓋 25 個有效候選數據點，並人工補充 13 項正文數字，共 38 項數值比較；結果為 38 項通過、零警告、零失敗。
- 另核驗兩項帶“超過”的來源表述：AlphaFold 兩億個結構預測的下界、併網投運時長五年的下界。未把下界改寫成精確點估計。
- 識別器的 4 項噪聲分別是數據年份、引用編號 S07、報告日期與研究區間；排除原因逐項保存在 audit-results.json。隨機抽中的五項沒有被排除。
- 對低置信度的十年推斷，採用反證與情景邊界審讀；不以算術 PASS 宣稱預測已被證明。

工具的默認百分比容差不是對事實口徑的驗證。本文同時人工檢查了單位、年份、樣本、估計與預測、比較對象以及閾值。來源值由本次閱讀填入；重新運行數值判決不會重新訪問網站。

## 已處理的關鍵口徑

1. 固定能力的使用成本，與前沿能力、每 token 價格、完整成功交付成本分開。
2. 降價千倍是題設；成本佔比、彈性和獨立錯誤概率是演示參數，不作為觀測事實。
3. 客服研究採用 2024 年修訂稿的 5,172 人和 15% 口徑。
4. IEA 的 2030 年值屬於預測，全部數據中心不等於 AI 專屬負荷。
5. Berkeley Lab 的隊列為發電與儲能項目；沒有改寫成數據中心接電等待時間或缺電量。
6. 數據庫條目是結構預測，不是已驗證藥物或實驗成果。
7. Google 關於 AP2 的材料是公司公告，不證明實際採用率和獨佔權。
8. C2PA 溯源與內容真偽分開；鏈接目錄和 PDF 自標版本存在差異，已在 sources.md 記錄。
9. 中國數據政策原文與官方站點刊載的專家解讀分開，不據此認定某家公司權利。
10. 租金現值只估算額外租金部分，不是任何完整企業估值，也沒有生成個股買入價。

## 計算復現

從倉庫根目錄執行：

```bash
python3 reports/智能廉價時代稀缺性研究-20260926/calculations.py
python3 tools/report_audit.py extract --report reports/智能廉價時代稀缺性研究-20260926/README.md --seed 42
```

計算腳本採用 Python Decimal、40 位有效數字；非整數冪在該精度內舍入。它也調用 financial_rigor.py 的 calc 子命令，輸出保存在 financial-rigor.txt。

當前 financial_rigor.py 的 calc 內部先計算 Python 原生數值表達式，再轉為 Decimal，不能把其命令名當作全程十進制精確運算的保證。因此本報告以 calculations.py 中直接使用 Decimal 的結果為主，倉庫工具作為第二次數值對照；未修改共享工具。

完整候選清單、樣本編號與主報告 SHA-256 在 audit-extracted.json；來源/公式映射與排除項在 audit-results.json；工具判決在 audit-verdict.txt。

如需重放已填數值的判決：

```python
import json
import subprocess
import sys
from pathlib import Path

p = Path("reports/智能廉價時代稀缺性研究-20260926")
checks = json.loads((p / "audit-results.json").read_text())["checks"]
subprocess.run([
    sys.executable, "tools/report_audit.py", "verdict",
    "--results", json.dumps(checks, ensure_ascii=False),
    "--report", str(p / "README.md"), "--output-json"
], check=True)
```

這隻復現比較，不替代再次查證原始資料。沒有將兩個引用同一底層數據的頁面包裝成獨立雙源。

## 審讀結論

報告可作為明確題設下的研究發佈。它給出可檢驗的機制、反例與投資篩選方向；沒有證明未來會按某一路徑發展，沒有核驗具體公司的當前估值，也沒有把哲學上的珍貴直接換算成股票回報。

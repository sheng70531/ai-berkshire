"""Reproduce the comparison report's sampled checks; no network fetching is implied."""
import importlib.util
import json
import subprocess
from decimal import Decimal as D
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPORT = HERE / "騰訊與快手對比研究-20260906.md"
spec = importlib.util.spec_from_file_location("report_audit", ROOT / "tools/report_audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

run = subprocess.run(
    ["python3", str(ROOT / "tools/report_audit.py"), "extract", "--report", str(REPORT), "--seed", "42"],
    text=True, capture_output=True, check=True,
)
(HERE / "橫評抽樣原始輸出.txt").write_text(run.stdout.replace(str(ROOT) + "/", ""))
points = audit.extract_data_points(REPORT.read_text())
sample = audit.sample_points(points, ratio=0.15, seed=42)
verified, assumptions = [], []
for point in sample:
    item = dict(point)
    label = item["label"]
    if label.startswith("收盤價") and "騰訊" in label:
        item.update(fetched_value=442.80,
                    fetched_source="https://stockanalysis.com/quote/hkg/0700/history/ (2026-09-04)",
                    fetched_value2=442.80,
                    fetched_source2="https://cn.investing.com/equities/tencent-holdings-hk-historical-data (2026-09-04)")
    elif label.startswith("已發行股數") and "快手" in label:
        item.update(fetched_value=3664102236 + 662858979,
                    fetched_source="IR linked Euroland: September 3 next-day B shares + August monthly A shares; URLs in 獨立來源與反方核查.md",
                    fetched_value2=4330000000,
                    fetched_source2="https://stockanalysis.com/quote/hkg/1024/statistics/ (4.33 billion, rounded)")
    elif "TTM 歸母淨利潤" in label and "騰訊" in label:
        item.update(fetched_value=float((D(224842) + D(114115) - D(103449)) / 100),
                    fetched_source="Tencent FY2025 + H12026 - H12025 IFRS attributable income; primary statement values 224842,114115,103449 million CNY",
                    fetched_value2=2355.08,
                    fetched_source2="https://stockanalysis.com/quote/hkg/0700/financials/ (TTM net income 235508 million CNY)")
    elif "要求更厚價格保護" in label and "快手" in label:
        values = json.loads((HERE / "估值折現敏感性.json").read_text())
        base = D(next(x["base_price_hkd"] for x in values if x["company"] == "kuaishou" and x["r"] == "0.12"))
        policy = base * D("0.75")
        assert policy.quantize(D("1")) == D(str(item["reported_value"])).quantize(D("1"))
        item.update(classification="研究價格條件，不是可從外部取得的事實", exact_model_value=str(policy),
                    check="12%基準價值打25%折扣後取整為約25港元；未計入事實準出項")
        assumptions.append(item)
        continue
    else:
        raise RuntimeError(f"Sample changed: independently classify and source {label}")
    assert abs(D(str(item["reported_value"])) - D(str(item["fetched_value"]))) / abs(D(str(item["reported_value"]))) <= D(".01")
    assert abs(D(str(item["reported_value"])) - D(str(item["fetched_value2"]))) / abs(D(str(item["reported_value"]))) <= D(".01")
    verified.append(item)

(HERE / "橫評抽樣事實核驗.json").write_text(json.dumps(verified, ensure_ascii=False, indent=2))
(HERE / "橫評抽樣假設核驗.json").write_text(json.dumps(assumptions, ensure_ascii=False, indent=2))
run = subprocess.run(
    ["python3", str(ROOT / "tools/report_audit.py"), "verdict", "--results", json.dumps(verified, ensure_ascii=False), "--report", REPORT.name, "--output-json"],
    capture_output=True, text=True, check=True,
)
(HERE / "橫評抽樣判決.txt").write_text(run.stdout)
(HERE / "橫評抽樣範圍.json").write_text(json.dumps({
    "seed": 42, "ratio": 0.15, "extracted_points": len(points), "sample_count": len(sample),
    "facts_with_two_source_checks": len(verified), "model_policy_separately_checked": len(assumptions),
    "unclassified_samples": 0,
    "limitation": "僅為本橫評抽樣，不表示全系列每項事實均雙源，也不驗證未來假設會實現。來源值為本次實際核讀記錄；腳本重跑不會自動刷新網絡。",
}, ensure_ascii=False, indent=2))
print(f"Sample: {len(sample)}; dual-source factual checks: {len(verified)}; separate model-policy checks: {len(assumptions)}")

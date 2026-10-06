"""Audit the fixed random sample. Forecast checks certify arithmetic only."""
from pathlib import Path
import json, subprocess, sys, re
from decimal import Decimal as D
H=Path(__file__).resolve().parent
R=H.parents[2]
report=H.parent/'美團-investment-team-AI利潤-20260925.md'
sys.path.insert(0,str(R/'tools'))
import report_audit as a
points=a.sample_points(a.extract_data_points(report.read_text()),ratio=.15,seed=42)
I=json.loads((H/'inputs.json').read_text()); C=json.loads((H/'calculations.json').read_text())
annual='https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0424/2026042400179.pdf'
half='https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0828/2026082800435.pdf'
sa='https://stockanalysis.com/quote/hkg/3690/financials/'
hs='https://www.hstong.com/news/detail/26082920431659905'
wsj='https://www.wsj.com/business/earnings/meituan-returns-to-profit-as-food-delivery-competition-eases-1026a0e9'
facts={
 '收入 · 2025全年':(3648.54746,annual,3648.55,sa),
 '收入 · 2026上半年':(1956.8195,half,1956.82,hs+' [AI summary; transcription check only]'),
 '歸母淨利潤 · 2023全年':(138.55828,annual,138.56,sa),
 '核心本地商業經營利潤 · 2025全年':(-69.04083,annual,None,''),
 '核心本地商業經營利潤 · 2026上半年':(36.38333,half,36.38,hs+' [AI summary; transcription check only]'),
 '新業務經營利潤 · 2025全年':(-100.82340,annual,None,''),
 '未分配項目淨額 · 2023全年':(-51.16976,annual,None,''),
 '經營現金流 · 2026上半年':(27.19085,half,None,''),
 '2026Q2收入 · 第二渠道值':(1046.43044,half,1046.40,wsj),
}
models={
 '客服、研發和運營節約 · 2027':I['ai_base_bridge']['2027'][1],
 '履約新增淨節約 · 2036':D('700')*D('.20'),
 '履約新增淨節約 · 2028':I['ai_base_bridge']['2028'][2],
 '履約新增淨節約 · 2029':D('400')*D('.045'),
 '額外AI研發、推理、設備折舊 · 2028':I['ai_base_bridge']['2028'][3],
 '入口分流、渠道費用與額外讓利 · 2027':I['ai_base_bridge']['2027'][4],
 '正常化稅後AI淨增量 · 2027':sum(I['ai_base_bridge']['2027'])*D('.8'),
 '正常化稅後AI淨增量 · 2028':sum(I['ai_base_bridge']['2028'])*D('.8'),
 '基準 · 2029利潤':(D('2800')*D('1.07')**3*D('.14')-30-150-10+25)*D('.8'),
 '基準 · 2028利潤':(D('2800')*D('1.07')**2*D('.12')-45-145-10+5)*D('.8'),
 '樂觀 · AI在2029年貢獻':D('65')*D('.8'),
 '總部經常成本（含SBC） · 基準':-D(I['long']['base']['hq']),
 '新增AI稅後影響 · 樂觀':D(I['long']['bull']['ai_pre'])*D('.8'),
}
res=[]; excluded=[]
for p in points:
 label=p['label']; q=dict(p)
 if label in facts:
  v,s,v2,s2=facts[label]
  q.update(fetched_value=v,fetched_source=s,fetched_value2=v2,fetched_source2=s2,verification_kind='external_fact',source_gap=('Only original official disclosure; independent second source not obtained' if v2 is None else ''))
 elif label in models:
  q.update(fetched_value=float(models[label]),fetched_source='Explicit analyst inputs / separately expanded Decimal expression',verification_kind='assumption_or_model_arithmetic',note='Not an external fact; pass does not certify forecast accuracy')
 elif label in ['資料截止','財務與估值 · 評分（滿分5）']:
  q.update(reason='Parser captured date year or subjective score; not a financial measurement')
  excluded.append(q);continue
 else: raise ValueError('Unreviewed sample: '+label)
 res.append(q)
for name,records in [('audit_sample.json',points),('audit_results.json',res),('audit_exclusions.json',excluded)]:
 (H/name).write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
for kind in ['external_fact','assumption_or_model_arithmetic']:
 items=[x for x in res if x['verification_kind']==kind]
 run=subprocess.run([sys.executable,str(R/'tools/report_audit.py'),'verdict','--results',json.dumps(items,ensure_ascii=False),'--report',report.name+' ['+kind+']'],text=True,capture_output=True,check=True)
 (H/('verdict_'+kind+'.txt')).write_text('\n'.join(x.rstrip() for x in re.sub(r'\x1b\[[0-9;]*m','',run.stdout).splitlines())+'\n')
 print(run.stdout)
(H/'audit_scope.md').write_text('''# 審計範圍\n\nseed=42，提取160個數字、隨機抽取24個：9項事實核對，13項模型或假設一致性，2項日期/主觀評分排除。\n\n事實PASS表示與原始披露一致，並不代表全部事實完成兩個獨立數據源驗證。2025核心及新業務經營利潤、2023未分配項目、2026H1經營現金流的抽樣項獨立第二來源未取得，保留單源限制。華盛通明確AI生成，只作抄錄核對，且不採用其季度歸母標籤。預測PASS僅表示對應假設或Decimal算式一致。\n\n抽樣之外，全部主情景、估值、淨現金與風險單位換算由financial_rigor或Decimal復算。未對未經披露的AI歸因、份額及未來現金流作真實性背書。年報原始檔案可在同項目審計-20260906目錄找到，本次通過在線HKEX公告及數據商重新核實關鍵數據。\n\n研究角色意見分歧：財務角色回報的705.95億元算式將淨融資成本誤寫為+20；主模型統一為−20，使用兩套算術路徑確認673.95億元。風險角色評分3.0/5，主線程為反映最新酒旅調查和十年不確定性採用2.5/5；評分調整不改變事實。\n''')

# -*- coding: utf-8 -*-
"""Reproduce scoped numeric checks; source judgments remain manual."""
from pathlib import Path
import json, subprocess, importlib.util, hashlib
a=Path(__file__).resolve().parent
p=a.parent
root=a.parents[3]
spec=importlib.util.spec_from_file_location('report_audit',str(root/'tools/report_audit.py'))
audit=importlib.util.module_from_spec(spec);spec.loader.exec_module(audit)
annual25='https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0424/2026042401899.pdf'
annual24='https://www.hkexnews.hk/listedco/listconews/sehk/2025/0425/2025042500501.pdf'
annual23='https://www1.hkexnews.hk/listedco/listconews/sehk/2024/0422/2024042200369.pdf'
annual22='https://www.hkexnews.hk/listedco/listconews/sehk/2023/0427/2023042700613.pdf'
h1='https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0819/2026081900315_c.pdf'
sa='https://stockanalysis.com/quote/hkg/1024/financials/'
eb='https://finance.sina.com.cn/stock/relnews/hk/2026-08-20/doc-ininxzps2010469.shtml'
primary={4:annual24,5:annual25,15:annual25,14:annual24,12:annual22,18:annual23,29:annual24,32:annual25,36:annual25,55:h1}
verified={4:1268.98,5:1427.76,15:186.17,14:153.35,12:-136.90,18:207.81,29:217.24,32:395.68,36:57.90,55:25.84}
coverage=[]
model=json.loads((a/'dcf_scenarios.json').read_text())
base=next(x for x in model if x['case']=='基準' and x['r']=='0.09')
bull=next(x for x in model if x['case']=='樂觀' and x['r']=='0.08')
bear=next(x for x in model if x['case']=='保守' and x['r']=='0.09')
model_verified={70:base['cashflows_cny_yi'][3],76:base['cashflows_cny_yi'][9],82:bull['cashflows_cny_yi'][5],87:float(bear['surplus_cny_yi']),95:float(bull['hkd_per_share'])}
for n in ['01','02','03']:
 article=next(p.glob(n+'-*.md'));article_text=article.read_text()
 sample=audit.sample_points(audit.extract_data_points(article_text),seed=42)
 (a/('sample_'+n+'.json')).write_text(json.dumps(sample,ensure_ascii=False,indent=2))
 extract=subprocess.run(['python3',str(root/'tools/report_audit.py'),'extract','--report',str(article.relative_to(root)),'--seed','42'],cwd=str(root),stdout=subprocess.PIPE,universal_newlines=True)
 (a/('extract_'+n+'.txt')).write_text(extract.stdout)
 checks=[]
 for s in sample:
  s['unit']=s['unit'] or ('人民幣億元' if n=='03' else '示例金額')
  if n=='01':
   s.update(classification='目錄鏈接誤識別，非數據事實',fetched_value=None,fetched_source='人工排除目錄序號')
  elif n=='02':
   s.update(classification='教學假設或算術；不適用外部事實驗證',fetched_value={1:25,2:15,6:100-45-15}[s['id']],fetched_source='reproduce.py 示例輸入；100-45-15=40 經 financial_rigor calc 複核',independent_external_sources=0)
  elif s['id'] in primary:
   s.update(classification='已披露財務事實',fetched_value=verified[s['id']],fetched_source=primary[s['id']],independent_external_sources=1)
   if s['id'] in [4,5,15,14,12,18,29]:
    s.update(fetched_value2=verified[s['id']],fetched_source2=sa,independent_external_sources=2)
   else:s['source_gap']='未取得獨立第二源；原始財報確認不等於雙源覆蓋'
  else:
   s.update(classification='模型假設或計算；不適用外部事實驗證',fetched_value=model_verified[s['id']],fetched_source='dcf_scenarios.json，financial_rigor calc 與 Decimal 算術複核',independent_external_sources=0)
   if s['id']==95:s['unit']='港元/股'
  checks.append(s)
 if n=='01':
  checks += [dict(id=101,label='人工重點抽檢：2026Q2收入',reported_value=355.35,unit='億元人民幣',fetched_value=355.35,fetched_source=h1,fetched_value2=355.4,fetched_source2=eb,classification='事實；獨立摘要四捨五入',independent_external_sources=2),dict(id=102,label='人工重點抽檢：2026Q2調整後淨利潤',reported_value=39.13,unit='億元人民幣',fetched_value=39.13,fetched_source=h1,fetched_value2=39.1,fetched_source2=eb,classification='事實；獨立摘要四捨五入',independent_external_sources=2),dict(id=103,label='人工重點抽檢：2025營銷收入',reported_value=814.62,unit='億元人民幣',fetched_value=814.62,fetched_source=annual25,classification='事實；原始年報 p18/p322，單一發行人來源',independent_external_sources=1,source_gap='未取得獨立第二源相同精度數')]
 if n=='02':
  checks += [dict(id=101,label='人工重點抽檢：可靈2025重組備考收入',reported_value=11,unit='億元人民幣',fetched_value=11,fetched_source='https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0702/2026070204066_c.pdf 印刷第6頁',classification='事實；未經審計重組備考約數，單一發行人來源',independent_external_sources=1),dict(id=102,label='人工重點抽檢：可靈2025備考虧損',reported_value=19,unit='億元人民幣',fetched_value=19,fetched_source='https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0702/2026070204066_c.pdf 印刷第23頁',classification='事實；未經審計重組備考約數，單一發行人來源',independent_external_sources=1),dict(id=103,label='人工重點抽檢：認購與激勵上限用滿後經濟權益',reported_value=68.33,unit='%',fetched_value=68.33,fetched_source='https://ea-cdn.eurolandir.com/press-releases-attachments/4175052/HKEX-EPS_20260831_12309546_0.PDF 第3頁66.33+2',classification='附條件表值；不是現時已歸屬比例，單一發行人來源',independent_external_sources=1)]
 (a/('verification_'+n+'.json')).write_text(json.dumps(checks,ensure_ascii=False,indent=2))
 out=subprocess.run(['python3',str(root/'tools/report_audit.py'),'verdict','--results',json.dumps(checks,ensure_ascii=False),'--report',n,'--output-json'],stdout=subprocess.PIPE,universal_newlines=True)
 (a/('verdict_'+n+'.txt')).write_text(out.stdout)
 coverage.append(dict(article=n,article_sha256=hashlib.sha256(article.read_bytes()).hexdigest(),automatic_sample_count=len(sample),checked_entries_including_models=len(checks),two_independent_sources_fact_count=sum(x.get('independent_external_sources',0)==2 for x in checks),single_issuer_fact_count=sum(x.get('independent_external_sources',0)==1 for x in checks),notice='工具 PASS 僅指抽檢值在容差內；未覆蓋全部正文，模型輸入無外部驗證含義，單源事實保留來源缺口。'))
 print(n,out.returncode,out.stdout[-550:])
(a/'coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))

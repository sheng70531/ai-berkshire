from pathlib import Path
import subprocess,json
p=Path(__file__).resolve().parent
root=p.parents[2]
cases={'2029基準利潤億元':'2300*1.08**3','2029現金75pct億元':'2300*1.08**3*.75'}
for ratio in [.6,.75,.9]:
    cases[f'{ratio}現金億元']=f'2300*{ratio}'
    cases[f'{ratio}現金收益率']=f'230000000000*{ratio}/3485015236130.865*100'
    cases[f'{ratio}反向永續增長']=f'(0.12-230000000000*{ratio}/3485015236130.865)*100'
rows=[]
for k,v in cases.items():
    args=['python3',str(root/'tools/financial_rigor.py'),'calc','--expr',v]
    result=subprocess.run(args,capture_output=True,text=True,check=True).stdout
    rows.append(dict(label=k,expression=v,source='2300億元為正文正常化利潤假設；市值由9/4實際股數×價格×官方中間價複核；轉化率、8%增長和12%貼現率均為研究假設',output=result))
(p/'現金壓力輸出.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print(json.dumps(rows,ensure_ascii=False,indent=2))

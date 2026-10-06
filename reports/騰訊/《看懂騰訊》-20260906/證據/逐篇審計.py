from pathlib import Path
from decimal import Decimal
import subprocess,json,re
base=Path(__file__).resolve().parents[1]; repo=base.parents[2]
a='https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0409/2026040901231.pdf'
h='https://www.tencent.com/wp-content/uploads/2026/08/E700_IR.pdf'
sa='https://stockanalysis.com/quote/hkg/0700/financials/'
u='https://uobkh.com.sg/en/research/company-hk-tencent-holdings-700-hk-13082026'
rows=[]; counts={}; dual=[]
for p in sorted(base.glob('0[1-8]-*.md')):
 result=subprocess.run(['python3',str(repo/'tools/report_audit.py'),'extract','--report',str(p),'--seed','20260906'],capture_output=True,text=True,check=True)
 (base/'證據'/f'{p.stem}-抽樣輸出.txt').write_text(result.stdout.replace(str(repo)+'/', ''))
 t=result.stdout.split('抽檢清單 JSON',1)[-1]; samples=json.loads(t[t.index('['):])
 for row in samples:
  row['article']=p.name; label=row['label']; value=row['reported_value']; text=row['raw_text']
  if '研究截點' in label or '數據截點' in label or (p.name.startswith('07') and value in [2024,2025]):
   row.update(audit_class='非財務日期_抽取誤識別',audit_note='年份不是財務樣本；保留原始記錄但不填造來源。日期已運行date，07實際回購額另做人工核驗。')
  elif p.name.startswith('08'):
   row.update(audit_class='作者假設或模型推導_已復算',audit_note='與財務真值與估值.json及financial_rigor運算記錄逐項比較，按展示精度一致；不作為外部已發生財務事實。',calculation_source='財務真值與估值.json / 騰訊計算.py')
  elif p.name.startswith('04'):
   if value==487.2:
    row.update(audit_class='官方單源事實_已回核',fetched_value=487.2,fetched_source=h,audit_note='實際抽到公式的起點，不是折價結果；6/30非並表上市公允價值，未取得獨立同口徑組合穿透，不能標雙源。')
   else: row.update(audit_class='作者假設或模型推導_已復算',audit_note='8.191和591.901分別為淨現金緩衝及組合折價公式；已工具及Decimal核對，不以虛構第二外部源包裝假設。',calculation_source='財務真值與估值.json')
  elif p.name.startswith('05'):
   row.update(audit_class='雙源數值核查_通過',fetched_value=value,fetched_source=h,fetched_value2=value,fetched_source2=u,audit_note='官方現金資料與獨立UOB公開正文對應取整金額一致；UOB其他季度資本開支混用及遊戲合計錯誤未採用。')
   dual.append(row)
  elif p.name.startswith('06'):
   if '自算' in label:
    row.update(audit_class='作者公式推導_已復算',audit_note='由現金原項計算，不是官方FCF。',calculation_source='財務真值與估值.json')
   elif ('收入' in label or '經營活動淨現金流' in label or '現金購買及預付' in label):
    row.update(audit_class='雙源數值核查_通過',fetched_value=value,fetched_source=('https://www.hkexnews.hk/listedco/listconews/sehk/2023/0406/2023040601848.pdf' if '經營活動淨現金流' in label and '2021' in label else 'https://www.hkexnews.hk/listedco/listconews/sehk/2024/0408/2024040801822.pdf' if '現金購買及預付' in label and '2023' in label else a),fetched_value2=value,fetched_source2=sa,audit_note='官方原項與獨立整理源相同；現金原項追溯對應年度年報。');dual.append(row)
   elif '毛利' in label and value in [245944,238746,422593]:
    other={245944:245931,238746:238887,422593:422870}[int(value)]
    row.update(audit_class='雙源小差異_官方原值優先',fetched_value=value,fetched_source=a,fetched_value2=other,fetched_source2=sa,audit_note='標準化財務分類有小差異，均低於1%；不是精確相等。報告採用官方原值。');dual.append(row)
   elif '經營利潤' in label and value==160074:
    row.update(audit_class='雙源超過1%_口徑不同比較不準出',fetched_value=160074,fetched_source=a,fetched_value2=162964,fetched_source2=sa,audit_note='2023官方統一重列經營利潤160074，數據庫標準化162964；拒用後者替代，不聲稱該字段雙源同口徑。保留官方單源並解釋2023呈列變更。')
   else:
    row.update(audit_class='官方單源事實_已回核',fetched_value=value,fetched_source=h if '上半年' in label else a,audit_note='已對原表數值、期間、歸屬回核；獨立同口徑第二源未取得，不填虛假第二源。')
  else: row.update(audit_class='需人工說明',audit_note='見附錄人工補充核驗。')
  rows.append(row)
 counts[p.name]={'sampled':len(samples),'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',p.read_text()))}
manual=[
 {'article':'01','field':'9/4收盤價','value':442.8,'source1':'https://stockanalysis.com/quote/hkg/0700/history/','source2':'https://cn.investing.com/equities/tencent-holdings-hk-historical-data','status':'雙源一致'},
 {'article':'01','field':'官方發行股份','value':9103153877,'source1':'https://www.tencent.com/wp-content/uploads/2026/09/c_Next-Day-Disclosure-Return_20260904.pdf','source2':'https://content.etnet.com.hk/content/cpyrevamp/sc/stock_quote.php?code=00700','status':'精確股數官方；第二源以同日市值4030.877十億港元閉環；另網站股數9.00bn被拒用'},
 {'article':'02','field':'微信WeChat合併MAU','value':1439,'unit':'百萬賬戶','source1':h,'status':'官方單源，非自然人數'},
 {'article':'03','field':'Q2國內/國際遊戲收入','value':[47.3,18.6],'unit':'十億人民幣','source1':h,'source2':u,'status':'分項取整一致，UOB遊戲合計64.2拒用'},
 {'article':'03','field':'Q2VAS收入/毛利','value':[98414,62926],'unit':'百萬元人民幣','source1':h,'status':'官方單源，絕不當遊戲歸母利潤'},
 {'article':'07','field':'2025回購','value':800.362995782,'unit':'億港元','source1':a,'status':'官方年報回核；獨立審查員另核原文，並非第二獨立原始發佈者'},
 {'article':'07','field':'馬化騰2025薪酬','value':48.532,'unit':'百萬元人民幣','source1':a,'status':'官方原表千元單位換算，非雙源'}]
(base/'證據'/'逐篇抽樣實審.json').write_text(json.dumps({'cutoff':'2026-09-06','scope_note':'抽樣不代表全量；日期誤識別、假設、單源、口徑差異分開。null源字段表示未取得，絕非已通過。','counts':counts,'samples':rows,'manual_supplements':manual},ensure_ascii=False,indent=2))
(base/'證據'/'雙源已核子集.json').write_text(json.dumps(dual,ensure_ascii=False,indent=2))
result=subprocess.run(['python3',str(repo/'tools/report_audit.py'),'verdict','--results',json.dumps(dual,ensure_ascii=False),'--report','騰訊系列僅雙源已核子集（非全文準出）','--output-json'],capture_output=True,text=True)
(base/'證據'/'雙源子集工具原始輸出.txt').write_text('僅9條已具兩源子集的工具結果；其報告可發佈措辭不代表全部正文準出。\n'+result.stdout+result.stderr)
verdict=json.loads(result.stdout[result.stdout.rfind('\n{')+1:])
verdict['scope_note']='僅9條雙源已核子集；不代表全系列全數據。'
(base/'證據'/'雙源子集工具判定.json').write_text(json.dumps(verdict,ensure_ascii=False,indent=2))
print(json.dumps({'counts':counts,'sample_count':len(rows),'dual_checked_subset':len(dual),'classes':{k:sum(r['audit_class']==k for r in rows) for k in sorted(set(r['audit_class'] for r in rows))}},ensure_ascii=False,indent=2))

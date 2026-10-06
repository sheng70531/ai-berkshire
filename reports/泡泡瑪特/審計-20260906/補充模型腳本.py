# coding: utf-8
from pathlib import Path
import json,re,subprocess,shutil
from decimal import Decimal as D,getcontext
getcontext().prec=40
root=Path('/Users/linxuan/ai-berkshire');exec(compile((Path(__file__).parent/'基礎模型腳本.py').read_text(),'基礎模型腳本.py','exec'))
run('MINIMAX','TTM股權PS驗證',['verify-valuation','--price','361.4','--revenue-per-share',str(D(165182000)*D('6.7787')/D('0.86458')/D(349235308))])
for co, dd in {'泡泡瑪特':{'王寧簡單穿透年末權益百分比':'(561131960+31196420+62053027*0.4096)/1342943150*100','悲觀2029歸母利潤率':'68.782/310*100','基準2029歸母利潤率':'141.087744/460*100','樂觀2029歸母利潤率':'193.536/620*100'},'MINIMAX':{'悲觀2029經營利潤億美元':'6*0.2-4-1.5','基準2029經營利潤億美元':'30*0.4-10-3','樂觀2029經營利潤億美元':'60*0.55-17-6','基準淨利率10%隱含PE':'6/0.1','基準淨利率20%隱含PE':'6/0.2'}}.items():
 for label,expr in dd.items():calc(co,label,expr)

for y,cfo,capex in [(2022,-11019,256),(2023,-64455,697),(2024,-258483,759),(2025,-279641,920)]:
 calc('MINIMAX',str(y)+'簡單自由現金流百萬美元','('+str(cfo)+'-'+str(capex)+')/1000')
for co in results:(root/'reports'/co/'審計-20260906'/'模型結果.json').write_text(json.dumps(results[co],ensure_ascii=False,indent=2))
summary={}
for co in results:
 vals=results[co];price=D('361.4') if co=='MINIMAX' else D(154);sc=[]
 for label,g,pe,rev,sh in [('悲觀','0.85',10,600,550),('基準','1.08',16,3000,450),('樂觀','1.2',22,6000,400)]:
  if co=='MINIMAX':target=D(rev)*D(1000000)*{'悲觀':2,'基準':6,'樂觀':10}[label]*D('6.7787')/D('0.86458')/(D(sh)*D(1000000));div=[D(0)]*3
  else:eps=D(11200000000)/D(1331779203)/D('0.86458');target=eps*D(g)**3*D(pe);div=[eps*D('.25')*D(g)**i for i in (1,2,3)]
  assert abs(target-D(vals[label+'終值']['value']))<D('.000001')
  sc.append({'scenario':label,'terminal_price_hkd':str(target),'annual_dividends_hkd':[str(x) for x in div],'cash_dividend_sum_hkd':str(sum(div))})
 summary[co]={'price_hkd':str(price),'years':3,'terminal_year':2029,'scenarios':sc,'method':'Decimal獨立重算; dividends held as cash, no reinvestment'}
 (root/'reports'/co/'審計-20260906'/'comparison_summary.json').write_text(json.dumps(summary[co],ensure_ascii=False,indent=2))

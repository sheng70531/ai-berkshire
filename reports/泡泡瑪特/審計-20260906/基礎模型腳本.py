# coding: utf-8
from pathlib import Path
from decimal import Decimal as D, getcontext
import subprocess,json,re,shutil
getcontext().prec=28
root=Path('/Users/linxuan/ai-berkshire')
results={}
def run(co,label,args):
 p=root/'reports'/co/'審計-20260906'
 r=subprocess.run(['python3',str(root/'tools/financial_rigor.py')]+args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True)
 with (p/'financial-rigor.txt').open('a') as f:f.write('\n'+label+'\n'+' '.join(args)+'\n'+r.stdout)
 if r.returncode:raise RuntimeError(r.stdout)
 return r.stdout
def calc(co,label,expr):
 out=run(co,label,['calc','--expr',expr]);m=re.search(r'精確值: (.+)',out);v=D(m.group(1));results[co][label]={'expr':expr,'value':str(v)};return v
for co in ['MINIMAX','泡泡瑪特']:
 results[co]={};p=root/'reports'/co/'審計-20260906';(p/'financial-rigor.txt').write_text('2026-09-06研究計算。calc使用原工具，資金及股本重要乘除另用Decimal複核。\n');shutil.copy(root/'reports/六公司研究審計-20260906/market-snapshot.json',p/'market-snapshot.json')
fx='(6.7787/0.86458)';s='1331779203';eps='(11200000000/1331779203/0.86458)'
run('泡泡瑪特','市值',['verify-market-cap','--price','154','--shares',s,'--reported','205094000000','--currency','HKD'])
run('MINIMAX','市值',['verify-market-cap','--price','361.4','--shares','349235308','--reported','126213640000','--currency','HKD'])
for co,fields in {'MINIMAX':[('2025收入',79.038,79.04),('2025淨虧損',-1871.617,-1872),('2025現金等價物',507.621,507.62),('2026H1收入',116.573,116.6),('2026H1歸母虧損',-357.997,-358),('2026H1現金等價物',930.905,930.91),('總股本百萬',349.235308,349.24)],'泡泡瑪特':[('2025收入',37120.052,37120),('2025歸母淨利',12775.689,12776),('2025現金等價物',13775.087,13775),('2026H1收入',17172.921,17173),('2026H1歸母淨利',5038.384,5038),('2026H1現金等價物',12442.065,12442),('股本百萬',1331.779203,1331.779203)]}.items():
 for name,a,b in fields:run(co,name,['cross-validate','--field',name,'--values',json.dumps({'HKEX':a,'StockAnalysis或正文指定獨立源':b}),'--unit','百萬或百萬股'])
for co,d in {'泡泡瑪特':{'現價人民幣':'154*0.86458','TTM歸母億':'(12775689-4574368+5038384)/100000','TTM收入億':'(37120052-13876276+17172921)/100000','TTM每股收益HKD':'(12775689000-4574368000+5038384000)/1331779203/0.86458','正常化EPS人民幣':'11200000000/1331779203','正常化EPS港元':eps,'歸母基期下修百分比':'(11200000000/12775689000-1)*100','2026H2收入億':'390-171.72921','2026H2淨利億':'112-50.38384','2026H2歸母率':'(112-50.38384)/(390-171.72921)*100','2026收入同比':'(390/371.20052-1)*100','2025可分配前FCF億':'(10865152-985250-186287-608288)/100000','H1資本開支前FCF億':'(3637300-673560-50579)/100000','H1CFO淨利比':'3637300/5100310*100','租後嚴格淨現金億':'(12442065+1520187-665736-3061836)/100000','市值億':'154*1331779203/100000000','海外同比':'((17172921-12201000)/(13876276-8282800)-1)*100','2025核心經營利潤率':'16890474/37120052*100'},'MINIMAX':{'USDHKD':fx,'市值億美元':'361.4*349235308/'+fx+'/100000000','TTM收入億美元':'(79038-30429+116573)/100000','TTM_PS':'361.4*349235308/'+fx+'/(79038000-30429000+116573000)','ARR_PS':'361.4*349235308/'+fx+'/800000000','FY26_PS':'361.4*349235308/'+fx+'/550000000','2025H2毛利率':'(20079-3685)/(79038-30429)*100','2026H1毛利率':'20813/116573*100','半年環比增量毛利率':'(20813-(20079-3685))/(116573-(79038-30429))*100','淨現金億美元':'(1322841-133555-3868)/100000','現金嚴格口徑億美元':'(930905+14038+278347-133555-3868)/100000','七月淨融資億美元':'(9443710000+6433300000)/'+fx+'/100000000','債券本金億美元':'6500000000/'+fx+'/100000000','H2月均收入百萬':'(550-116.573)/6','H2平均運行率億':'(550-116.573)/6*12/100','2026至2029收入CAGR':'((3000/550)**(1/3)-1)*100','B端2025H2百萬':'25.958-9.206','創始人經濟權益參考':'79102534/349235308*100','創始人投票權參考':'(74102534*10+5000000)/(81102534*10+268132774)*100'}}.items():
 for label,expr in d.items():calc(co,label,expr)
run('泡泡瑪特','實際TTM估值',['verify-valuation','--price','154','--eps',str(results['泡泡瑪特']['TTM每股收益HKD']['value'])])
run('泡泡瑪特','正常化估值 非TTM',['verify-valuation','--price','154','--eps',str(results['泡泡瑪特']['正常化EPS港元']['value'])])
run('泡泡瑪特','三情景',['three-scenario','--price','154','--eps',str(results['泡泡瑪特']['正常化EPS港元']['value']),'--shares','13.31779203','--growth','0.20','0.08','-0.15','--pe','22','16','10','--years','3','--currency','HKD'])
for label,g,pe in [('悲觀','0.85',10),('基準','1.08',16),('樂觀','1.20',22)]:
 end='('+eps+'*'+g+'*'+g+'*'+g+'*'+str(pe)+')';div='('+eps+'*0.25*('+g+'+'+g+'*'+g+'+'+g+'*'+g+'*'+g+'))'
 calc('泡泡瑪特',label+'終值',end);calc('泡泡瑪特',label+'三年分紅',div);calc('泡泡瑪特',label+'含分紅年化','(('+end+'+'+div+')/154)**(1/3)*100-100');calc('泡泡瑪特',label+'現值10%',end+'/1.1/1.1/1.1+'+eps+'*0.25*('+g+'/1.1+'+g+'*'+g+'/1.1/1.1+'+g+'*'+g+'*'+g+'/1.1/1.1/1.1)');calc('泡泡瑪特',label+'2029歸母億','112*'+g+'*'+g+'*'+g)
calc('泡泡瑪特','基準要求12%買價','('+eps+'*1.08*1.08*1.08*16)/1.12/1.12/1.12+'+eps+'*0.25*(1.08/1.12+1.08*1.08/1.12/1.12+1.08*1.08*1.08/1.12/1.12/1.12)')
calc('泡泡瑪特','反向零增長含分紅三年年化','(('+eps+'*16+'+eps+'*0.25*3)/154)**(1/3)*100-100')
for label,rev,ps,shares,issue,burn in [('悲觀',600,2,550,65,3.5),('基準',3000,6,450,150,3.5),('樂觀',6000,10,400,400,3.0)]:
 end='('+str(rev)+'*1000000*'+str(ps)+'*'+fx+'/'+str(shares)+'000000)';calc('MINIMAX',label+'終值',end);calc('MINIMAX',label+'三年年化','('+end+'/361.4)**(1/3)*100-100');calc('MINIMAX',label+'現值15%',end+'/1.15/1.15/1.15');calc('MINIMAX',label+'融資億美元','('+str(shares)+'000000-349235308)*'+str(issue)+'/'+fx+'/100000000');calc('MINIMAX',label+'期末儲備億美元','(1322841000+(9443710000+6433300000)/'+fx+'+('+str(shares)+'000000-349235308)*'+str(issue)+'/'+fx+'-6500000000/'+fx+'-133555000-3868000-'+str(burn)+'*1000000000)/100000000');calc('MINIMAX',label+'股本增幅','('+str(shares)+'000000/349235308-1)*100')
calc('MINIMAX','反向15%收益收入億美元','361.4*1.15*1.15*1.15*450000000/6/'+fx+'/100000000')
calc('MINIMAX','基準2030後15%淨利PE','6/0.15')
for co in results:
 (root/'reports'/co/'審計-20260906'/'模型結果.json').write_text(json.dumps(results[co],ensure_ascii=False,indent=2))
print(json.dumps({co:{k:v['value'] for k,v in vals.items()} for co,vals in results.items()},ensure_ascii=False,indent=2))

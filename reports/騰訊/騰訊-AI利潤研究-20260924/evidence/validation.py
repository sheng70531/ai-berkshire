"""Audit facts against retrieved evidence; scenario rows check arithmetic only.

Run from the repository root. No forecast is certified as an observed fact.
"""
from decimal import Decimal as D
from pathlib import Path
import json, re, subprocess, sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
REPORT=HERE.parent/'騰訊-investment-team-AI利潤與競爭格局.md'
sys.path.insert(0,str(ROOT/'tools'))
from report_audit import extract_data_points, sample_points

def rigor(args):
    p=subprocess.run([sys.executable,str(ROOT/'tools/financial_rigor.py'),*args],text=True,capture_output=True,check=True)
    return '$ financial_rigor.py '+' '.join(args)+'\n'+p.stdout+'\n'

checks=[('2025收入',7517.66,7517.66,'Tencent annual','Stockanalysis'),
        ('2025 IFRS歸母',2248.42,2248.42,'Tencent annual','Stockanalysis'),
        ('2024收入',6602.57,6602.57,'Tencent annual comparative','Stockanalysis'),
        ('2024 IFRS歸母',1940.73,1940.73,'Tencent annual comparative','Stockanalysis'),
        ('2025 nonIFRS歸母',2596.26,2596.26,'Tencent annual','36kr'),
        ('2026Q2收入',2047.85,2048,'Tencent Q2','Reuters rounded'),
        ('2026Q2 IFRS歸母',560.22,560,'Tencent Q2','Reuters rounded'),
        ('2026Q2 nonIFRS歸母',684.15,684.2,'Tencent Q2','MarketWatch rounded'),
        ('2026Q2 Capex確認',527.84,528,'Tencent Q2','Reuters rounded'),
        ('2026Q2實際FCF',-138,-138,'Tencent Q2','MarketWatch'),
        ('20260924股價HKD',438.4,438.4,'Stockanalysis','Investing'),
        ('20260924 HKDCNY參考',.8559,.8559,'Investing','ExchangeRates UK')]
out=[]
for label,a,b,s1,s2 in checks:
    out.append(rigor(['cross-validate','--field',label,'--values',json.dumps({s1:a,s2:b}), '--unit','specified in label / RMB100m','--tolerance','1']))
    # The skill uses the primary source denominator, unlike tool median rule.
    assert abs(D(str(a))-D(str(b)))/abs(D(str(a)))<=D('.01')
shares=D(9095133109);price=D('438.4');fx=D('.8559')
eps=D(2800)*10**8/shares/fx
out.append(rigor(['verify-market-cap','--price',str(price),'--shares',str(shares),'--reported','3.94e12','--currency','HKD']))
out.append(rigor(['verify-valuation','--price',str(price),'--eps',str(eps)]))
model=json.loads((HERE.parent/'model-results.json').read_text())
growth=[model['long'][k]['profit_cagr'] for k in ['bull','base','bear']]
out.append(rigor(['three-scenario','--price',str(price),'--eps',str(eps),'--shares',str(shares/D(10**8)),
    '--growth',*growth,'--pe','22','16','10','--years','10','--currency','HKD']))
for expr in ['3160*1.07+(130+60+35+45-50-520)*0.8',
             '3160*1.07**2+(260+120+75+80-100-420)*0.8',
             '3160*1.07**3+(410+190+140+115-150-250)*0.8',
             '(6995-350)*0.8+250','(9095133109-9000000000)/9095133109*100']:
    out.append(rigor(['calc','--expr',expr]))
(HERE/'financial-rigor.txt').write_text(''.join(out))

S1='https://www.tencent.com/wp-content/uploads/2026/08/Tencent-Announces-2026-Second-Quarter-Results.pdf'
S2='https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0812/2026081200296.pdf'
SA='https://stockanalysis.com/quote/hkg/0700/financials/'
AN='https://static.www.tencent.com/uploads/2026/03/18/e6a646796d0d869acc76271c9ee1a6a5.pdf'
# Manually retrieved factual values; second issuer-hosted copies are NOT independent.
facts={
 '收入 · 2024全年':(D('6602.57'),AN,D('6602.57'),SA),
 'IFRS歸母淨利潤 · 2026上半年':(D('1141.15'),S2,None,'Independent second source not obtained; Q1+Q2 separately reconciled'),
 'IFRS歸母淨利潤 · 2024全年':(D('1940.73'),AN,D('1940.73'),SA),
 'non-IFRS經營利潤 · 數值':(D('756.36'),S1,None,'Issuer precise value only'),
 '剔除算力預付款的自由現金流 · 數值':(D(376),S1,None,'Issuer adjusted measure only'),
}
# Independent Decimal recalculation, not copied from model-results.json.
calc={
 '2027 non-IFRS歸母 · 悲觀E':D(3160)*D('1.03')+(D(60+20+10+20)-80-650)*D('.8'),
 '2028 non-IFRS歸母 · 樂觀E':D(3160)*D('1.10')**2+(D(380+180+140+110)-100-200)*D('.8'),
 '2029 non-IFRS歸母 · 基準E':D(3160)*D('1.07')**3+(D(410+190+140+115)-150-250)*D('.8'),
 '2029 non-IFRS歸母 · 悲觀E':D(3160)*D('1.03')**3+(D(180+60+40+50)-240-800)*D('.8'),
 '上述正貢獻合計 · 2028':D(260+120+75+80),
 '上述正貢獻合計 · 2029':D(410+190+140+115),
 '相對凍結參考的歸母增量 · 2028':D(260+120+75+80-100-420+450)*D('.8'),
 '相對凍結參考的歸母增量 · 2029':D(410+190+140+115-150-250+450)*D('.8'),
 '廣告和商業推薦 · 經營利潤貢獻':D(5200)*D('.48'),
 '扣總部後經營利潤 · 樂觀':sum(r*m for r,m in zip(map(D,[4800,3200,2100,8000,4300,5000,300]),map(D,['.48','.4','.34','.52','.33','.25','.1'])))-600,
 '要求較強安全邊際 · 參考價格（港元）':D(450)*D('.8'),
}
assumptions={
 '風險評估 · 評分（最高5）':D('3.5'),
 '第三方客戶雲基礎設施貢獻 · 2029':D(140),
 '減：老業務額外推理、折舊及基礎設施費用 · 2027':D(50),
 '減：老業務額外推理、折舊及基礎設施費用 · 2029':D(150),
 '減：新AI產品經營淨虧損 · 2029':D(250),
 '廣告和商業推薦 · 2036經營利潤率':D(48),
 '外部雲與獨立AI產品 · 2026收入基數':D(600),
 '再扣維持性投入超過折舊的負擔假設 · 悲觀':D(250),
}
rows=sample_points(extract_data_points(REPORT.read_text()),ratio=.15,seed=42)
for row in rows:
    label=row['label']
    if label in facts:
        v,s,v2,s2=facts[label];row.update(validation_type='historical_fact',fetched_value=float(v),fetched_source=s,
            fetched_value2=float(v2) if v2 is not None else None,fetched_source2=s2)
    elif label in calc:
        row.update(validation_type='formula_only_not_forecast_validation',fetched_value=float(calc[label]),
                   fetched_source='Independent Decimal expression in evidence/validation.py; NOT external fact')
    elif label in assumptions:
        row.update(validation_type='assumption_consistency_only',fetched_value=float(assumptions[label]),
                   fetched_source='Research assumption ledger; NOT externally validated')
    else: raise RuntimeError('Unreviewed audit sample: '+label)
(HERE/'audit-results.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
p=subprocess.run([sys.executable,str(ROOT/'tools/report_audit.py'),'verdict','--results',json.dumps(rows,ensure_ascii=False),
    '--report',REPORT.name,'--output-json'],text=True,capture_output=True,check=True)
(HERE/'audit-verdict.txt').write_text(p.stdout)
decimal_record=dict(market_cap_hkd=str(price*shares),market_cap_rmb=str(price*shares*fx),
    eps2026_hkd=str(eps),pe2025_nonifrs=str(price*shares*fx/(D('2596.26')*10**8)),
    pe2026=str(price/eps),official_vs_platform_shares_gap_pct=str((shares-D(9000000000))/shares*100),
    fair_low=str(D(2500)*10**8/shares/fx*14),fair_high=str(D(2500)*10**8/shares/fx*18))
(HERE/'decimal-valuation.json').write_text(json.dumps(decimal_record,indent=2)+'\n')
print(p.stdout[-700:])
print('Audited samples:',len(rows),'Facts:',sum(r['validation_type']=='historical_fact' for r in rows),
      'Formula:',sum(r['validation_type'].startswith('formula') for r in rows),
      'Assumptions:',sum(r['validation_type'].startswith('assumption') for r in rows))
for path in HERE.glob('*.txt'):
    plain=re.sub(r'\x1b\[[0-9;]*m','',path.read_text())
    path.write_text('\n'.join(line.rstrip() for line in plain.splitlines()).rstrip()+'\n')

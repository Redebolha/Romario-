P0 = dict(fii=4084.27, rf=1502.50, etf=584.32, acoes=528.05)
DY_FII=0.12/12; DY_AC=0.03/12; CDI=0.12/12*(1-0.175)

def run(meses, split, nome, prov_to_rf=True):
    p=dict(P0)
    for m in range(meses):
        prov = p['fii']*DY_FII + (p['acoes']+p['etf'])*DY_AC
        p['rf'] = p['rf']*(1+CDI) + (prov if prov_to_rf else 0)
        for k,v in split.items(): p[k]+=v
    tot=sum(p.values())
    print(f"\n{nome} ({meses}m)")
    for k in ('fii','acoes','etf','rf'):
        print(f"   {k.upper():6s} R$ {p[k]:9,.2f}  {100*p[k]/tot:5.1f}%")
    print(f"   TOTAL  R$ {tot:9,.2f}")

# A) plano atual
run(24, dict(fii=400, etf=200, acoes=400), "A) PLANO ATUAL 400 FII / 200 ETF / 400 acoes")
# B) pausa total no FII: 350 acoes / 350 ETF-dolar / 300 caixa
run(24, dict(fii=0, etf=350, acoes=350, rf=300), "B) FII PAUSADO: 350 acoes / 350 ETF / 300 caixa")
# C) meio-termo: FII 200 / acoes 400 / ETF 250 / caixa 150
run(24, dict(fii=200, etf=250, acoes=400, rf=150), "C) MEIO-TERMO: 200 FII / 400 acoes / 250 ETF / 150 caixa")
# C em 12m
run(12, dict(fii=200, etf=250, acoes=400, rf=150), "C) MEIO-TERMO")

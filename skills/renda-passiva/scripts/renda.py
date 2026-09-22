#!/usr/bin/env python3
"""
Calculadora de renda passiva para investidor brasileiro.

Existe para que ninguem precise refazer essa conta a mao toda vez — e,
principalmente, para que a conta seja feita em termos REAIS. A diferenca
entre planejar em nominal e em real, num horizonte de 10-20 anos, e a
diferenca entre um plano e uma ilusao.

Uso:
  python renda.py viabilidade --patrimonio 19310 --aporte 1000 --renda 5000 --prazo 5
  python renda.py projecao    --patrimonio 19310 --aporte 1000 --anos 20
  python renda.py alvos       --renda 5000
  python renda.py aportar     --carteira carteira.json
"""
import argparse, json, sys

# ---------------------------------------------------------------- premissas
# Sao PREMISSAS, nao previsoes. Todas podem ser sobrescritas pela linha de
# comando. Os defaults sao deliberadamente conservadores: um plano de renda
# que so fecha com premissa otimista nao e um plano.
D = dict(
    retorno=0.12,      # retorno total nominal a.a. da carteira
    inflacao=0.045,    # IPCA de longo prazo
    retirada=0.05,     # taxa de retirada REAL a.a. sustentavel
    yield_cx=0.09,     # rendimento em caixa (proventos+juros) nominal a.a.
)

def real(nominal, inflacao):
    """Converte taxa nominal em real. (1+n)/(1+i)-1, nao n-i."""
    return (1 + nominal) / (1 + inflacao) - 1

def mensal(anual):
    return (1 + anual) ** (1/12) - 1

def fv(p0, pmt, anos, taxa):
    r, n = mensal(taxa), int(round(anos * 12))
    return p0 * (1 + r) ** n + (pmt * (((1 + r) ** n - 1) / r) if r else pmt * n)

def pmt_necessario(p0, alvo, anos, taxa):
    r, n = mensal(taxa), int(round(anos * 12))
    fator = ((1 + r) ** n - 1) / r if r else n
    return (alvo - p0 * (1 + r) ** n) / fator

def meses_ate(p0, pmt, alvo, taxa, teto=1200):
    r, p, m = mensal(taxa), p0, 0
    while p < alvo and m < teto:
        p = p * (1 + r) + pmt
        m += 1
    return m if p >= alvo else None

def brl(v):
    return f"R$ {v:,.0f}".replace(",", ".")

def prazo(m):
    return "nao alcanca" if m is None else f"{m//12}a {m%12}m"

# ---------------------------------------------------------------- comandos
def cmd_alvos(a):
    tr_real, tr_nom = a.retirada, a.yield_cx
    print(f"\nPATRIMONIO NECESSARIO PARA RENDA DE {brl(a.renda)}/mes\n")
    print(f"  {'criterio':<42} {'alvo':>14}")
    print("  " + "-" * 57)
    print(f"  {'Sustentavel (retirada real de '+f'{100*tr_real:.0f}%'+' a.a.)':<42} {brl(a.renda*12/tr_real):>14}")
    print(f"  {'Otimista (consumir o yield de '+f'{100*tr_nom:.0f}%'+' a.a.)':<42} {brl(a.renda*12/tr_nom):>14}")
    print(f"""
  O primeiro numero preserva o poder de compra da carteira: voce retira
  {100*tr_real:.0f}% ao ano acima da inflacao e o principal continua valendo o
  mesmo daqui a 30 anos.

  O segundo consome todo o rendimento de caixa. Parece o dobro de eficiente
  e nao e: com inflacao de {100*a.inflacao:.1f}% a.a., a carteira perde poder de
  compra nesse ritmo. Em 15 anos a mesma renda compra ~{100*(1-(1/(1+a.inflacao)**15)):.0f}% menos.

  Planeje pelo primeiro. Use o segundo so como limite superior.
""")

def cmd_viabilidade(a):
    r_real = real(a.retorno, a.inflacao)
    alvo = a.renda * 12 / a.retirada
    print(f"\nVIABILIDADE — viver de {brl(a.renda)}/mes em {a.prazo} anos\n")
    print(f"  Patrimonio hoje ........ {brl(a.patrimonio)}")
    print(f"  Aporte atual ........... {brl(a.aporte)}/mes")
    print(f"  Alvo ................... {brl(alvo)}  (retirada real de {100*a.retirada:.0f}% a.a.)")
    print(f"  Retorno real assumido .. {100*r_real:.1f}% a.a. ({100*a.retorno:.0f}% nominal - {100*a.inflacao:.1f}% inflacao)\n")

    chega = fv(a.patrimonio, a.aporte, a.prazo, r_real)
    renda_chega = chega * a.retirada / 12
    print(f"  No ritmo atual, em {a.prazo} anos voce tem {brl(chega)}")
    print(f"  Isso paga {brl(renda_chega)}/mes — {100*renda_chega/a.renda:.0f}% do alvo\n")

    if chega >= alvo:
        print("  VIAVEL no ritmo atual.\n")
        return

    falta = alvo - chega
    print(f"  FALTAM {brl(falta)}. Existem exatamente tres alavancas:\n")
    p_nec = pmt_necessario(a.patrimonio, alvo, a.prazo, r_real)
    print(f"  1. APORTE   — manter o prazo de {a.prazo} anos exige {brl(p_nec)}/mes")
    print(f"                ({p_nec/a.aporte:.1f}x o aporte atual)")
    m = meses_ate(a.patrimonio, a.aporte, alvo, r_real)
    print(f"  2. PRAZO    — mantendo {brl(a.aporte)}/mes, o alvo chega em {prazo(m)}")
    renda_viavel = fv(a.patrimonio, a.aporte, a.prazo, r_real) * a.retirada / 12
    print(f"  3. RENDA    — em {a.prazo} anos, {brl(a.aporte)}/mes sustentam {brl(renda_viavel)}/mes\n")
    print("  Combinacoes intermediarias (aporte x prazo ate o alvo):\n")
    print(f"  {'aporte/mes':>12} | " + " | ".join(f"{str(p)+'a':>6}" for p in (5, 10, 15, 20, 25)))
    print("  " + "-" * 51)
    for ap in (a.aporte, a.aporte*1.5, a.aporte*2, a.aporte*3, a.aporte*5):
        linha = [f"{brl(fv(a.patrimonio, ap, p, r_real)*a.retirada/12).replace('R$ ',''):>6}" for p in (5,10,15,20,25)]
        print(f"  {brl(ap):>12} | " + " | ".join(linha))
    print("\n  (valores na tabela = renda mensal sustentavel, em R$ de hoje)\n")

def cmd_projecao(a):
    r_real = real(a.retorno, a.inflacao)
    print(f"\nPROJECAO — {brl(a.aporte)}/mes, retorno real de {100*r_real:.1f}% a.a.")
    print("  (tudo em R$ de hoje; renda = retirada real de "
          f"{100*a.retirada:.0f}% a.a.)\n")
    print(f"  {'ano':>4} {'patrimonio':>14} {'aportado':>13} {'renda/mes':>12} {'aporte vs renda':>17}")
    print("  " + "-" * 64)
    for ano in range(1, a.anos + 1):
        p = fv(a.patrimonio, a.aporte, ano, r_real)
        ap = a.aporte * 12 * ano
        renda = p * a.retirada / 12
        marca = "  <-- renda > aporte" if renda >= a.aporte else ""
        print(f"  {ano:>4} {brl(p):>14} {brl(ap):>13} {brl(renda):>12} {100*renda/a.aporte:>15.0f}%{marca}")
    print()

def cmd_aportar(a):
    """Aplica a regra da posicao mais atrasada sobre uma carteira real."""
    dados = json.load(open(a.carteira))
    posicoes, alvos, aporte = dados["posicoes"], dados["alvos_classe"], dados.get("aporte", 1000)
    total = sum(posicoes.values())
    por_classe = {}
    for at, v in posicoes.items():
        cl = dados["classe_de"][at]
        por_classe[cl] = por_classe.get(cl, 0) + v

    print(f"\nCARTEIRA: {brl(total)} em {len(posicoes)} ativos\n")
    print(f"  {'classe':<12} {'atual':>12} {'%':>7} {'alvo %':>8} {'gap R$':>12}")
    print("  " + "-" * 55)
    gaps = {}
    for cl, alvo_pct in sorted(alvos.items(), key=lambda x: -x[1]):
        atual = por_classe.get(cl, 0)
        alvo_rs = total * alvo_pct
        gaps[cl] = alvo_rs - atual
        print(f"  {cl:<12} {brl(atual):>12} {100*atual/total:>6.1f}% {100*alvo_pct:>7.0f}% {brl(gaps[cl]):>12}")

    print(f"\nONDE VAO OS {brl(aporte)} DESTE MES\n")
    deficit = {c: g for c, g in gaps.items() if g > 0}
    soma = sum(deficit.values())
    for cl, g in sorted(deficit.items(), key=lambda x: -x[1]):
        valor = aporte * g / soma
        na_classe = {a_: v for a_, v in posicoes.items() if dados["classe_de"][a_] == cl}
        atrasado = min(na_classe, key=na_classe.get) if na_classe else "(abrir posicao)"
        print(f"  {cl:<12} {brl(valor):>10}  ->  {atrasado}  (posicao mais atrasada: {brl(na_classe.get(atrasado,0))})")
    sobra = [c for c, g in gaps.items() if g <= 0]
    if sobra:
        print(f"\n  Sem aporte este mes: {', '.join(sobra)} (ja acima do alvo)")
    print()

# ---------------------------------------------------------------- cli
def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    def comuns(s, **kw):
        s.add_argument("--retorno", type=float, default=D["retorno"])
        s.add_argument("--inflacao", type=float, default=D["inflacao"])
        s.add_argument("--retirada", type=float, default=D["retirada"])
        s.add_argument("--yield-cx", dest="yield_cx", type=float, default=D["yield_cx"])
        return s

    s = comuns(sub.add_parser("alvos"));       s.add_argument("--renda", type=float, required=True)
    s = comuns(sub.add_parser("viabilidade"))
    s.add_argument("--patrimonio", type=float, required=True)
    s.add_argument("--aporte", type=float, required=True)
    s.add_argument("--renda", type=float, required=True)
    s.add_argument("--prazo", type=float, required=True)
    s = comuns(sub.add_parser("projecao"))
    s.add_argument("--patrimonio", type=float, required=True)
    s.add_argument("--aporte", type=float, required=True)
    s.add_argument("--anos", type=int, default=20)
    s = comuns(sub.add_parser("aportar"));     s.add_argument("--carteira", required=True)

    a = p.parse_args()
    {"alvos": cmd_alvos, "viabilidade": cmd_viabilidade,
     "projecao": cmd_projecao, "aportar": cmd_aportar}[a.cmd](a)

if __name__ == "__main__":
    main()

# Carteira do Romário — snapshot e decisões

Contexto acumulado. Atualize a data e os números sempre que ele mandar
posição nova; o histórico de decisões é o que evita rediscutir o já decidido.

**Última atualização:** 22/09/2026 (prints do Investidor10)
**Objetivo declarado:** viver de renda em 5 anos
**Aporte atual:** R$ 1.000/mês

---

## Posição

**Patrimônio total implícito: ~R$ 19.310** (pelo teste do percentual)
**Soma do que apareceu nos prints: R$ 6.775,95**
**Não identificado: ~R$ 12.534 — 65% da carteira**

Esse buraco é a primeira coisa a resolver em qualquer conversa. Nenhuma
projeção é confiável enquanto dois terços da carteira forem desconhecidos.

### Ações — R$ 529,09 (2,74%)

| Ativo | Qtd | PM | Atual | Saldo | Rent. |
|---|---:|---:|---:|---:|---:|
| ITUB4 | 7 | R$ 38,31 | R$ 43,12 | R$ 301,84 | +12,45% |
| BRSR6 | 15 | R$ 14,03 | R$ 15,15 | R$ 227,25 | +8,05% |

Só dois papéis, ambos bancos — **concentração setorial de 100%**. As ações que
apareciam no plano antigo (WEGE3, TTEN3, B3SA3, LREN3) eram alvo, não posição.

### FIIs — R$ 4.130,99 (21%, alvo 25%) · rentabilidade −5,09%

| Ativo | Tipo | Qtd | PM | Atual | Saldo | Rent. |
|---|---|---:|---:|---:|---:|---:|
| GGRC11 | tijolo | 131 | R$ 9,39 | R$ 9,03 | R$ 1.182,93 | −3,83% |
| MXRF11 | papel | 102 | R$ 9,75 | R$ 9,11 | R$ 929,22 | −6,56% |
| CPTS11 | papel | 110 | R$ 7,52 | R$ 7,42 | R$ 816,20 | −0,13% |
| BTLG11 | tijolo | 5 | R$ 99,38 | R$ 100,06 | R$ 500,30 | +1,83% |
| TRXF11 | tijolo | 5 | R$ 91,21 | R$ 73,85 | R$ 369,25 | **−18,65%** |
| HGBS11 | tijolo | 10 | R$ 19,02 | R$ 18,55 | R$ 185,50 | −2,10% |
| XPML11 | tijolo | 1 | R$ 103,96 | R$ 98,08 | R$ 98,08 | −5,66% |
| GARE11 | tijolo | 6 | R$ 8,18 | R$ 8,45 | R$ 50,70 | +3,42% |

Mix tijolo/papel razoável. Os problemas são de **tamanho**, não de escolha:
oito fundos para R$ 4,1 mil dá média de R$ 516. XPML11 com 1 cota e GARE11 com
6 são posições simbólicas — rendem centavos e consomem atenção.

TRXF11 a −18,65% é a pior posição da carteira e merece releitura de tese, não
aporte automático.

### Exterior — R$ 598,07 (3,10%, alvo 25%)

SPXI11: 11 cotas, PM R$ 54,28, atual R$ 54,37. **É a classe mais distante do
alvo** — 22 pontos percentuais abaixo.

### Caixa e renda fixa — R$ 1.516,61

| Ativo | Saldo | Observação |
|---|---:|---|
| RDB Nubank pós-fixado 100% CDI | R$ 1.511,62 | reserva de emergência de fato |
| Tesouro Prefixado 2032 | R$ 4,99 | posição simbólica (0,01 título) |

### Linhas com erro de lançamento

- **JEPQ** — quantidade `0,00000001`, preço médio `US$ 5.667.000.000,00`,
  saldo US$ 0,00. Lançamento quebrado; precisa ser corrigido ou excluído no
  Investidor10 antes de entrar em qualquer conta.
- **Tesouro Prefixado 2032** — R$ 4,99. Não é erro, mas é ruído: se a regra da
  posição mais atrasada rodar sem filtro, essa linha sequestra o aporte.

---

## A conta do objetivo

Rodado em 22/09/2026, premissas padrão (retorno 12% nominal, inflação 4,5%,
retirada real de 5%):

| Renda alvo | Patrimônio necessário | Aporte p/ 5 anos | Prazo com R$ 1.000/mês |
|---|---:|---:|---|
| R$ 2.000/mês | R$ 480.000 | ~R$ 6.400/mês | ~21 anos |
| R$ 3.000/mês | R$ 720.000 | ~R$ 9.800/mês | ~25 anos |
| R$ 5.000/mês | R$ 1.200.000 | ~R$ 16.400/mês | ~28 anos |

No ritmo atual, em 5 anos a carteira chega a ~R$ 98,8 mil, que sustentam
**R$ 412/mês**.

**Viver de renda em 5 anos com R$ 1.000/mês não fecha** — e a distância não é
de ajuste, é de ordem de grandeza (16x o aporte). Isso precisa ser dito com
clareza e sem rodeio, sempre acompanhado das três alavancas, porque a decisão
de qual puxar é dele.

O caminho realista passa por aumentar o aporte via renda (ele tem operação
própria — Rede Bolha, livros na Hotmart), não por buscar yield maior. A
alavanca "aporte" é a única em que ele tem influência direta.

---

## Dados que faltam

1. **Custo de vida mensal** — sem isso o alvo de renda é chute e a reserva não
   tem dimensão. É a pergunta mais importante em aberto.
2. **Os ~R$ 12.534 não identificados** — 65% da carteira.
3. Há quanto tempo aporta e se os R$ 1.000 são consistentes.

---

## Decisões e diagnósticos anteriores

- **set/2026** — Revisão do plano de aportes (`investimentos/revisao-plano-aportes.md`):
  dosagem alterada de 600 crescimento / 400 FII para 400 ações / 250 SPXI11 /
  200 FII / 150 caixa, para corrigir sobrepeso em FII e abrir linha de reserva.
- **set/2026** — Mantida a regra da posição mais atrasada; recusada a sugestão
  de substituí-la por escolha discricionária mensal.
- **set/2026** — GGRC11 sob observação: troca de gestora (virou Zagros Renda
  Imobiliária), P/VP ~0,84, peso grande de contratos atípicos.
- **set/2026** — Meta de alocação usada: 25% ações / 25% FII / 25% exterior /
  25% caixa. No Investidor10 ele configurou alvo semelhante, mas com Tesouro
  em 25% e renda fixa em 0% — vale alinhar as duas definições.

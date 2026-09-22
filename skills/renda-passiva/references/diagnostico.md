# Diagnóstico de carteira

Como transformar print, planilha ou lista digitada em números confiáveis antes
de projetar qualquer coisa.

## A conferência que quase ninguém faz

Print de corretora e de agregador quase sempre vem cortado — o usuário rola a
tela, tira duas ou três fotos, e alguma classe fica de fora sem ninguém notar.
Projetar em cima disso produz um plano que parece certo e está errado na base.

**O teste do percentual.** A maioria das plataformas (Investidor10, Status
Invest, Kinvo) mostra a coluna *% na carteira* de cada posição. Isso permite
recuperar o total real:

```
total_implícito = saldo_da_posição / (percentual / 100)
```

Faça isso para três ou quatro posições de classes diferentes. Elas devem
convergir para o mesmo número. Compare esse número com a soma do que você
está vendo:

- **Batem (diferença < 2%)** → a carteira está completa, siga.
- **Não batem** → falta classe. Diga quanto falta, em R$ e em %, e pergunte o
  que é antes de projetar. Costuma ser cripto, previdência, COE, ou mais
  renda fixa numa aba separada.

Esse minuto de conferência evita reescrever o plano inteiro depois.

## Linhas com erro de lançamento

Carteiras de agregador acumulam lixo. Sinais de que uma linha está quebrada e
deve ser corrigida na origem antes de entrar na conta:

- **Preço médio absurdo** (ordens de grandeza fora do preço atual) — quase
  sempre erro de moeda ou de casa decimal num lançamento antigo.
- **Quantidade em notação científica** (`0,00000001`) — resquício de importação
  ou de venda parcial mal lançada.
- **Variação de exatamente −100%** com saldo zero — posição zerada que ficou
  na lista.
- **Posição de R$ 5** — compra de teste que nunca virou posição. Não é erro,
  mas polui o cálculo de "posição mais atrasada": uma linha de R$ 5 sempre
  será a mais atrasada e sequestra todo aporte se a regra for aplicada cega.

Trate as duas últimas como **ruído**: exclua do cálculo e liste à parte,
sugerindo que o usuário limpe ou consolide. Não invente valor para elas.

## Formato do `carteira.json`

```json
{
  "data": "2026-09-22",
  "aporte": 1000,
  "custo_vida_mensal": null,
  "posicoes": {
    "GGRC11": 1182.93,
    "MXRF11": 929.22,
    "ITUB4": 301.84,
    "SPXI11": 598.07
  },
  "classe_de": {
    "GGRC11": "fii",
    "MXRF11": "fii",
    "ITUB4": "acoes",
    "SPXI11": "exterior"
  },
  "alvos_classe": {
    "fii": 0.25, "acoes": 0.25, "exterior": 0.25, "caixa": 0.25
  },
  "nao_conferido": 12534.05,
  "ruido": ["JEPQ", "Tesouro Prefixado 2032"]
}
```

`nao_conferido` guarda o que o teste do percentual revelou e ainda não foi
identificado. Enquanto for maior que zero, toda projeção precisa vir com a
ressalva — o usuário tem que saber que o número pode mudar.

## Classes que valem separar

Agregue por **função na carteira**, não por tipo de papel:

| Classe | O que entra | Função |
|---|---|---|
| `fii` | FII de tijolo e de papel | renda mensal isenta |
| `acoes` | ações brasileiras | crescimento + dividendos |
| `exterior` | ETF de índice global, BDR, conta no exterior | proteção cambial |
| `caixa` | Tesouro Selic, CDB/RDB líquido, reserva | liquidez e oportunidade |

Renda fixa longa (prefixado, IPCA+ com vencimento distante) **não é caixa** —
tem marcação a mercado e pode estar no vermelho justo quando o dinheiro faz
falta. Classifique como posição própria ou dentro de `caixa` apenas se o
usuário souber que vai carregar até o vencimento.

## O que perguntar quando falta informação

Três perguntas resolvem quase todo diagnóstico incompleto. Peça as três de uma
vez, explicando o que cada uma destrava:

1. **Custo de vida mensal** — sem isso não há alvo de renda nem
   dimensionamento de reserva. É a mais importante.
2. **O que são as classes que não apareceram no print** — fecha o patrimônio.
3. **Há quanto tempo aporta e quanto por mês** — calibra se o plano é novo ou
   já tem inércia, e se o aporte declarado é o que de fato acontece.

# Primeiro dia da campanha de Vendas — 31/08/2026

Campanha `52513066643229` · conjunto `52513066701829` · anúncio `52513066977429`

---

# PARTE 1 — UMA CORREÇÃO ANTES DOS NÚMEROS

Ontem eu afirmei, com todas as letras, que **os 25 `InitiateCheckout` do período
dispararam todos na página inicial e nenhum na página do quiz**. Usei isso na
análise do funil, na descrição do PR #20 e no que te falei.

**Eu não tinha como saber disso.** A agregação por `url` da API do Meta que eu
consultei não devolve o caminho da página — devolve o **domínio**. Testei hoje:

```
aggregation=url   →  "https://redebolha.com.br/"   (contagens idênticas)
aggregation=host  →  "redebolha.com.br"            (contagens idênticas)
```

Os dois retornam exatamente os mesmos números. O que me deu a pista foi um valor
`https://pay.hotmart.com/` — ninguém acessa a raiz do checkout do Hotmart; aquilo
era o domínio, não a página.

**O que muda e o que não muda:** a conclusão de que a página do quiz não vende
continua de pé, mas por outro motivo — eu li o HTML dela e ela não tem nenhum
link do Hotmart, então é impossível disparar `InitiateCheckout` ali. A conclusão
estava certa; a prova que eu apresentei estava errada. São coisas diferentes, e a
segunda é a que importa para você poder confiar no resto.

**Consequência prática para hoje:** eu não consigo separar, por essa API, os
eventos de `/oferta/` dos eventos das outras páginas. O que dá para afirmar é que
o `ViewContent` **só existe em duas páginas do site** — `/oferta/` e a página do
livro físico — e ele passou a aparecer no pixel a partir do horário do deploy de
ontem. Antes disso não havia nenhum. Ou seja: **a página está no ar e disparando
eventos.**

---

# PARTE 2 — OS NÚMEROS DO PRIMEIRO DIA

O anúncio saiu da revisão e está entregando, com o conjunto marcado como
`ad_set_in_learning_phase`.

| | Campanha antiga (30/08) | Campanha nova (31/08) |
|---|---:|---:|
| Impressões | 3.405 | 1.283 |
| Cliques | 310 | 34 |
| CTR | 9,10% | **2,65%** |
| CPM | R$ 5,53 | **R$ 16,95** |
| Gasto | R$ 18,84 | R$ 21,75 |
| Visitas na página | 281 | 19 |
| Custo por visita | R$ 0,067 | **R$ 1,14** |
| InitiateCheckout atribuído | 0 | **1** |
| Custo por InitiateCheckout | — | **R$ 21,75** |
| Purchase | 0 | **0** |

Alcance 689 pessoas, frequência 1,86.

O gasto passou dos R$ 19 do orçamento porque o Meta pode gastar até 25% a mais
num dia e compensar no resto da semana. Normal.

## O que é bom

**Existe um `InitiateCheckout` atribuído.** É o primeiro da história desta conta.
A campanha antiga rodou uma semana inteira e nunca conseguiu um. O funil novo
produz sinal mensurável — que era exatamente o objetivo de construir a `/oferta/`.

## O que é ruim

**R$ 21,75 por InitiateCheckout, contra o teto de R$ 4,94.** Está 4,4 vezes acima
do que a margem comporta. E o checkout ainda não é a venda: parte dele desiste no
pagamento.

**A visita ficou 17 vezes mais cara** — de R$ 0,067 para R$ 1,14. O CPM triplicou.

Três coisas mudaram ao mesmo tempo — objetivo (Tráfego → Vendas), público (Brasil
→ RS) e criativo (foto da máscara → imagem da oferta). **Não dá para saber qual
delas causou o quê.** Parte é esperada: otimizar por conversão sempre custa mais
caro por impressão do que otimizar por clique, porque o Meta passa a procurar
quem compra em vez de quem clica.

---

# PARTE 3 — O PROBLEMA QUE NINGUÉM VÊ NO PRIMEIRO DIA

Um dia é pouco, e o conjunto está em aprendizado — o custo de hoje não decide
nada sozinho. Mas tem uma conta estrutural que já dá para fazer:

**O Meta precisa de cerca de 50 eventos de otimização por semana para sair do
aprendizado.** No ritmo de hoje, 1 `InitiateCheckout` por dia, isso levaria
**quase dois meses**. Até lá o algoritmo entrega no escuro.

Esse é o problema de verdade, e ele não é o preço de hoje: **é o volume.** Com
R$ 19/dia num público de um estado só, otimizando por um evento que acontece uma
vez ao dia, a campanha não junta dados suficientes para aprender a encontrar
compradores.

## Três saídas, e o que cada uma custa

**1. Esperar.** Dar 3 ou 4 dias antes de mexer. O custo por evento costuma cair
bastante quando o aprendizado avança. É o caminho mais barato e o que eu faria
primeiro — mas só funciona se o volume subir junto.

**2. Otimizar por visita na página em vez de checkout.** Com 19 visitas/dia, o
Meta teria volume para aprender de verdade. Perde precisão (ele volta a procurar
quem clica), mas sai do escuro. É um meio-termo enquanto não há venda.

**3. Abrir a geografia.** Sul e Sudeste em vez de só RS multiplicaria o público e
baratearia o CPM. Esbarra no frete, que é decisão sua.

**O que eu não recomendo agora:** subir o orçamento. Aumentar investimento numa
campanha que ainda não sabe para quem entregar só faz o dinheiro passar mais
rápido pelo mesmo lugar.

---

# PARTE 4 — O QUE FICA PARA O PRÓXIMO CHECK-IN

Reconferir amanhã, com dois dias de aprendizado:

- o custo por `InitiateCheckout` caiu?
- quantos eventos por dia a campanha está juntando?
- a frequência (1,86 hoje) continua subindo? Se passar de 3 rápido, o público do
  RS está pequeno demais para esse orçamento e o CPM vai continuar subindo.
- entrou alguma venda?

---

*Conta 351203535, pixel 2570806596755923, lidos em 31/08/2026 às 23h UTC.*

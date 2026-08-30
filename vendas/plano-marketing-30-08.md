# Plano de marketing ajustado — 30/08/2026

Escrito depois de fechar o rastreamento de ponta a ponta (PR #19 no ar + pixel
configurado nos quatro produtos do Hotmart). Agora dá para ver o funil inteiro
pela primeira vez. E o que ele mostra muda a prioridade.

---

# PARTE 1 — O QUE OS NÚMEROS DIZEM HOJE

## A campanha está entregando muito bem o que você pediu

Campanha `52512807800029` — **"Teste da Máscara Masculina | Tráfego"**
Conjunto `52512807805029` — **"BR | Homens 30-60 | Amplo"**

| | Até 29/08 | Hoje (30/08) | Total |
|---|---:|---:|---:|
| Impressões | 2.031 | 2.825 | **4.856** |
| Cliques | 209 | 271 | **480** |
| Visitas na página | 182 | 242 | **424** |
| Gasto | R$ 14,63 | R$ 15,83 | **R$ 30,46** |

**CTR de 9,2% a 10,4%.** Custo de R$ 0,07 por visita.

Deixa eu ser claro sobre o que isso significa: esses números são **excelentes**.
CTR acima de 9% em público amplo é raro. Sete centavos por visita é preço de
banana. A criação funciona. O público está certo. O tráfego **não é o seu
problema.**

## E mesmo assim: zero venda, zero lead atribuído

O que o pixel `2570806596755923` registrou nos últimos 7 dias:

| Evento | Disparos no pixel | Atribuídos aos anúncios |
|---|---:|---:|
| PageView | ~1.400 | 424 |
| Lead | 13 | **0** |
| InitiateCheckout | 24 | **0** |
| **Purchase** | **0** | **0** |

O `Purchase` zerado era esperado — o Hotmart foi configurado hoje e não houve
venda desde então. Isso não é defeito, é falta de venda para medir.

O resto não é normal. E eu descobri por quê.

---

# PARTE 2 — O FURO: A PÁGINA QUE VOCÊ PAGA PARA ENCHER NÃO VENDE NADA

O anúncio manda todo mundo para `/teste-mascara-masculina/`.

Eu li o código dessa página inteira. **Ela não tem um único botão de compra.**
Nenhum link para o Hotmart. Nenhuma oferta de livro. As duas únicas vezes que a
palavra "livro" aparece são no menu do topo.

O caminho que a pessoa faz hoje é este:

```
Anúncio  →  Quiz  →  Resultado ("sua máscara é X")  →  botão de WhatsApp  →  fim
```

Você está pagando R$ 0,07 por visita, 242 visitas por dia, para levar homens de
30 a 60 anos até uma página cuja única saída é te mandar mensagem no WhatsApp.

**Não existe venda nenhuma para acontecer ali.** O funil não está furado — ele
não chega até a loja.

E os 24 `InitiateCheckout` que dispararam? Eu conferi a origem de cada um: **todos
em `https://redebolha.com.br/`**, a página inicial. Nenhum na página do quiz.
Ou seja, quem clica em comprar é o visitante orgânico que cai na home — não o
tráfego que você paga.

Isso fecha a explicação dos 45,5% de cobertura de `fbc` no `InitiateCheckout`
(contra 90% no PageView): metade de quem clica em comprar nem veio de anúncio.

## O outro lado disso é uma boa notícia

O PR #19 funciona, e dá para provar:

| Janela | InitiateCheckout |
|---|---:|
| 7 dias **antes** do deploy | 4 |
| 2 horas **depois** do deploy | **20** |

Vinte cliques de compra em duas horas, contra quatro na semana inteira. Os botões
do livro físico de R$ 29,90 — que antes não disparavam absolutamente nada —
agora disparam. Conferi que não há disparo duplicado: existe um segundo ouvinte
de clique na página, mas ele só manda o evento do GA4, não o do Meta.

**A home vende. A página do anúncio, não.** É só isso.

---

# PARTE 3 — A ORDEM DAS COISAS, AJUSTADA

O plano de 29/08 dizia para começar pelas iscas. Está errado agora. A isca serve
para capturar quem ainda não vai comprar. Você tem coisa mais barata e mais
rápida para fazer antes: **aproveitar o tráfego que já está entrando e já está pago.**

## 1º — Colocar a oferta no fim do quiz *(esta semana, é a de maior retorno)*

Cada uma das 6 máscaras termina hoje com um botão de WhatsApp. Precisa terminar
com três coisas, nesta ordem:

1. **A ponte** — dois ou três parágrafos ligando aquela máscara específica ao
   livro. Não genérico: se o cara tirou "o Provedor", o texto fala do Provedor.
   Isso é texto seu, autoral, e é o que faz ou quebra a conversão.
2. **A oferta** — livro físico R$ 29,90 e e-book R$ 9,90, lado a lado, com os
   links do Hotmart que já estão no site.
3. **O WhatsApp**, mantido, mas *abaixo* da oferta. Quem quer falar com você
   continua falando. Quem está pronto para comprar não precisa passar por você.

Zero de investimento novo. O tráfego já está comprado e já está chegando.

## 2º — Trocar o objetivo da campanha: Tráfego → Vendas

Isto só depois do passo 1, nunca antes.

Hoje o Meta está otimizando para **visita na página** (`OUTCOME_TRAFFIC`,
resultado = landing page view). Ele está entregando exatamente isso, com
perfeição: 424 visitas a R$ 0,07. O problema é que ele está procurando gente que
*clica*, não gente que *compra*. São públicos diferentes dentro do mesmo
interesse, e o Meta é muito bom em achar o que você pede.

Enquanto o objetivo for Tráfego, o algoritmo nunca vai olhar para o `Purchase`,
mesmo com o Hotmart configurado.

**Como fazer, sem quebrar o que funciona:** duplique a campanha em vez de editar
a atual. Objetivo **Vendas**, otimizando por **InitiateCheckout** — não por
Purchase ainda. O Meta precisa de ~50 eventos por semana por conjunto para sair
do aprendizado; no ritmo de hoje o `InitiateCheckout` entrega isso e o `Purchase`
não entregaria. Deixe as duas rodando lado a lado por uma semana e compare custo
por venda, não custo por clique.

## 3º — Advanced Matching *(uma linha de código)*

A qualidade de correspondência do pixel está em **6,1 de 10**. Ele manda IP,
user agent, `fbp` e `fbc` — e nada mais. Nenhum e-mail, telefone ou nome.

O Advanced Matching automático sobe isso sem você fazer nada além de ligar, e
melhora tanto a atribuição quanto a capacidade do Meta de achar público
parecido. É a melhoria mais barata da lista inteira.

## 4º — O número que continua faltando

**Custo de impressão por exemplar + custo do frete grátis.**

Já pedi isso no plano anterior e repito porque ele decide tudo o que vem depois.
Com o funil consertado você vai ter vendas para medir — e sem esse número você
não vai saber se cada venda te dá lucro ou prejuízo. R$ 29,90 com frete grátis no
Brasil pode significar trabalhar de graça.

## 5º — Só então, as iscas

O plano de iscas do documento `estrategia-vendas.md` continua válido e continua
sendo o caminho de escala. Ele só sai da primeira posição, porque construir isca
enquanto o tráfego pago cai numa página sem oferta é consertar o telhado com a
porta aberta.

---

# PARTE 4 — O QUE EU NÃO CONSIGO AFIRMAR

Sendo honesto sobre os limites do que apurei:

**Os 13 Leads não atribuídos.** Eles dispararam com 100% de cobertura de `fbc` —
ou seja, carregam o identificador de clique do anúncio e *deveriam* ser
atribuíveis. Mesmo assim o Meta reporta zero. Numa campanha de Tráfego o Meta
reporta como "resultado" só a visita na página, e eventos fora do objetivo às
vezes não aparecem nos campos que consultei. Não consigo separar as duas
hipóteses pela API. A troca de objetivo (passo 2) resolve a dúvida na prática:
numa campanha de Vendas, a conversão deixa de ser cosmética e vira a coisa pela
qual o Meta é pago.

**O `InitiateCheckout` zerado é cedo demais para julgar.** Os 20 eventos são de
duas horas atrás. A atribuição do Meta costuma levar algumas horas. Vale reconferir
amanhã antes de tratar como problema.

**Não consegui testar se os links do Hotmart abrem.** A rede desta sessão bloqueia
o domínio. Clique nos quatro botões de compra do site quando puder — leva um
minuto e é a única verificação que falta no PR #19.

---

*Dados da conta 351203535, campanha 52512807800029 e pixel 2570806596755923,
lidos em 30/08/2026 às 20:36 UTC. Código conferido no `main` publicado do
repositório Redebolha/Redebolha.*

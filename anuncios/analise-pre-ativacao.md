# Análise antes de ativar — Teste da Máscara Masculina

Feita em 28/08/2026, com a campanha `52512807800029` ainda pausada.
Base: dados reais da conta 351203535 e do pixel `2570806596755923` (HVNR Tracking).

## Veredito

**Não ativar ainda.** Não porque o anúncio seja ruim — ele é a melhor peça da
conta — mas porque os instrumentos estão quebrados e, do jeito que está, R$ 15/dia
compra dados ilegíveis.

Duas correções que custam zero reais liberam a ativação. Estão na seção 6.

## 1. O que já foi gasto, e quando

Toda a conta rodou entre **16 e 21 de agosto** — seis dias — e está pausada desde então.

| Campanha | Gasto | Cliques | CTR | CPC | LPV |
|---|---|---|---|---|---|
| HVNR — Venda Direta Hotmart | R$ 62,77 | 429 | 3,67% | R$ 0,15 | 208 |
| HVNR — Funil Teste + WhatsApp | R$ 51,86 | 406 | 5,15% | R$ 0,13 | 312 |
| Post IG "qual máscara" (mensagens) | R$ 45,86 | 19 | 1,11% | R$ 2,41 | — |
| HVNR — Máscara Masculina — Teste + WhatsApp | R$ 36,50 | 218 | 5,20% | R$ 0,17 | 187 |
| Demais posts impulsionados | R$ 17,10 | 62 | — | — | 11 |
| **Total** | **R$ 214,09** | | | | |

Seis dias e R$ 214 não condenam funil nenhum. É pouco para concluir que não vende.
É o bastante, porém, para mostrar que a medição não está de pé.

## 2. O anúncio não é o gargalo

As duas campanhas do funil do teste deram **CTR de 5,15% e 5,20%**, com **CPC de
R$ 0,13 e R$ 0,17**. Para tráfego frio no Brasil, isso é muito bom — a referência
comum fica entre 1% e 2%.

O gancho já funciona. O anúncio novo é uma versão melhor de algo que já vencia na
etapa do clique. Ou seja: mais orçamento aqui compra mais do que nunca foi o problema.

## 3. O achado principal — os Leads não são atribuídos

O pixel registrou **16 eventos `Lead` entre 16 e 21 de agosto**, exatamente a janela
em que os anúncios rodaram. O dia 21 sozinho teve 9.

O Meta atribuiu **zero** desses Leads a qualquer campanha. Todas voltam `lead: null`.

Isso não quer dizer que ninguém converteu. Quer dizer que o evento dispara sem
carregar o identificador do clique (`fbc` / `fbp`) ou sem casar o `event_id` entre
navegador e servidor. O dataset mostra disparo por servidor
(`server_last_fired_time`), o que reforça a suspeita: evento vindo de CAPI sem os
dados de atribuição.

Consequência prática: **o Meta nunca viu um Lead que ele consiga ligar a um anúncio.**
Sem isso não existe otimização por conversão, não existe público semelhante, e o
plano de "trocar para conversões no evento Lead" descrito no documento do anúncio
nunca vai poder ser executado.

Taxa real de LPV → Lead: **16 em 499 = 3,2%**. É uma taxa respeitável. Ela só está
invisível para o Meta.

## 4. Eventos que o plano promete e que não existem

O documento do anúncio manda medir, nesta ordem: CTR → QuizStart ÷ PageView →
QuizComplete ÷ QuizStart → Lead ÷ QuizComplete → Venda ÷ Lead.

Os eventos que o pixel realmente recebeu no período:

`PageView`, `Lead`, `InitiateCheckout`, `ViewContent`, `ProductPage`.

**Não existe `QuizStart`. Não existe `QuizComplete`. Não existe `Purchase`.**

Então os passos 2, 3 e 5 da régua de medição são hoje inexecutáveis. Se a campanha
rodar assim, e o resultado vier ruim, não haverá como saber se o culpado foi a
página, o teste, a conversa ou o preço.

E o mais grave: **15 `InitiateCheckout` e nenhum `Purchase`.** Como a venda fecha
fora do domínio (Hotmart), o pixel do redebolha nunca vê a compra. Sem esse evento
não existe ROI mensurável — nem hoje, nem depois.

## 5. O anúncio promete um recado que a IA não entrega

Esta é a única falha de conteúdo, e é grande.

O Anúncio A termina com *"No fim, tem um recado esperando por você."* A mensagem que
a pessoa envia no WhatsApp termina com *"Vi que você tem um recado pra mim 👀"*. O
próprio documento da IA diz, na seção 1: *"Seu papel: entregar o recado, puxar uma
conversa curta e honesta, e oferecer o livro. Nessa ordem."*

Mas nenhuma das respostas M1 a M6 entrega recado nenhum. Todas fazem a mesma coisa:
reconhecem a máscara, contam um pedaço do Romário, e devolvem uma pergunta.

O sujeito foi convocado três vezes por um recado e, ao chegar, é interrogado.
Um homem que usa máscara de Estoico que Não Chora não vai responder "faz tempo que
você não desabafa de verdade com ninguém?" na primeira mensagem de um número
desconhecido. A promessa cria uma dívida que o primeiro contato não paga.

**Correção:** dar o recado antes da pergunta. Uma frase curta, específica da máscara,
dita como afirmação — não como pergunta. A pergunta vem depois, e como convite, não
como exigência.

## 6. As duas correções que liberam a ativação

**Correção 1 — atribuição e venda (obrigatória).**
Fazer o `Lead` disparar com `fbc`/`fbp` e `event_id` casados, e criar o evento de
compra (postback da Hotmart ou evento de servidor). Sem isso, todo real gasto vira
dado que não pode ser lido.

**Correção 2 — o recado (obrigatória, e de graça).**
Reescrever as seis primeiras respostas para entregar o recado antes de perguntar.
Trinta minutos de trabalho, e é a maior alavanca do funil inteiro.

**Opcional, mas recomendado:** criar `QuizStart` e `QuizComplete` para que a régua
de diagnóstico do documento funcione.

## 7. A conta que precisa fechar

Com os números observados:

- CPC R$ 0,17 → R$ 15/dia compra ~88 cliques → ~70 visualizações de página.
- LPV → Lead de 3,2% → ~2,2 leads por dia.
- Custo por lead: R$ 88,36 ÷ 16 = **R$ 5,52**.

Do outro lado, o e-book de R$ 9,90 deixa cerca de R$ 9 líquidos. Se a IA fechar
15% das conversas — otimista para tráfego frio — cada lead vale R$ 1,35.

**Você pode pagar R$ 1,35 por lead. Está pagando R$ 5,52.** Está quatro vezes acima
do que o produto sustenta.

Para R$ 15/dia empatar seria preciso que **75% dos leads comprassem**. Isso não
acontece em lugar nenhum.

O livro físico de R$ 29,90 com frete grátis e e-book incluso provavelmente deixa
menos que o e-book, não mais — frete e impressão comem a diferença. Vale conferir a
margem real antes de contar com ele para fechar a conta.

### O que isso significa

Não significa "desligue o projeto". Significa que **este funil não se paga vendendo
um livro de R$ 9,90**, e que existem três saídas honestas:

1. **Tratar como aquisição, não como venda.** Se o livro é a porta de entrada da Rede
   Bolha e existe algo depois — comunidade, mentoria, palestra, um segundo produto —
   então R$ 5,52 por homem que abre o jogo no WhatsApp pode ser barato. Mas aí a
   métrica é lead, não venda, e o orçamento precisa sair de outro bolso que não o da
   venda do livro.
2. **Aumentar o ticket.** Uma oferta combinada, ou um segundo item no checkout, muda
   a conta inteira. Com R$ 30 de margem, R$ 5,52 por lead fecha.
3. **Baixar o custo do lead.** Só dá para saber se é possível depois da Correção 1 —
   hoje você não consegue nem otimizar para lead.

Essa escolha é sua e é de negócio, não de anúncio.

## 8. Um caminho mais barato que já deu sinal

A única peça da conta que produziu conversa de verdade foi o **post do Instagram com
objetivo de mensagens**: 7 conversas iniciadas a R$ 6,55 cada, sem passar pelo teste.

Custo por conversa parecido com o custo por lead do funil longo — só que sem página,
sem quiz e sem quatro etapas onde perder gente. Vale rodar em paralelo como controle.
Se o funil do teste não bater isso, o teste está cobrando caro pelo que entrega.

## 9. Volume e a regra de segurança

O documento da IA diz que a regra de segurança *"é a única parte do funil que não
pode rodar sozinha"* e manda avisar o Romário na hora.

A R$ 15/dia com esse criativo, o volume de conversas sobe várias vezes. O número de
homens revelando sofrimento grave sobe junto — e o documento do anúncio recomenda
programar das 19h às 21h30, que é justamente quando é menos provável que alguém
esteja olhando o WhatsApp.

Antes de escalar, é preciso decidir quem cobre esse horário e em quanto tempo. Não é
questão de marketing. É a única parte disso que não admite atraso.

## 10. O que eu faria, em ordem

1. Corrigir atribuição do `Lead` e criar o evento de compra.
2. Reescrever as seis aberturas para entregar o recado.
3. Definir quem responde de verdade entre 19h e 22h.
4. Decidir a questão do ticket (seção 7).
5. Só então ligar — a **R$ 10/dia por 7 dias, teto de R$ 70**, tratado como corrida de
   medição e não de lucro. Critério de corte definido antes de ligar: se em 7 dias não
   houver Lead atribuído no Gerenciador, o problema continua sendo instrumentação, não
   anúncio.
6. Rodar o controle de mensagens da seção 8 em paralelo.

## Limitação desta análise

Não consegui abrir `redebolha.com.br` — o proxy desta sessão bloqueia o domínio.
Então não auditei a página do teste, o link do WhatsApp nem o código do pixel
diretamente. Tudo na seção 3 e 4 foi inferido dos dados do pixel e das campanhas.
A causa exata da falha de atribuição precisa ser confirmada olhando o código da
página.

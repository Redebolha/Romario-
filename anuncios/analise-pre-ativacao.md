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

## 4. Os eventos existem — mas são invisíveis para o Meta

**Correção de uma afirmação minha anterior.** Eu disse que `QuizStart` e `QuizComplete`
não existiam. Existem, e estão corretos no código (`teste-mascara-masculina/index.html`,
linhas 274 e 314). Eu tinha lido só o relatório do pixel, que não os mostrava.

O motivo de não aparecerem é outro, e é de solução rápida: os dois são disparados com
`fbq('trackCustom', ...)`. Evento personalizado **não vira métrica de relatório nem
evento otimizável enquanto não existir uma Conversão Personalizada** criada para ele no
Gerenciador de Eventos. Hoje eles disparam no navegador e morrem ali.

Prova disso nos dados: o `Lead` é padrão (`fbq('track','Lead')`) e aparece 20 vezes.
O `QuizComplete` é personalizado, dispara obrigatoriamente antes de todo `Lead`
— o botão do WhatsApp só existe depois do resultado — e aparece **zero** vezes.

**Correção:** criar Conversões Personalizadas para `QuizStart` e `QuizComplete`.
Cinco minutos no Gerenciador de Eventos, sem tocar em código. Aí os degraus 2 e 3 da
régua de medição passam a existir.

O que continua verdadeiro e é sério: **não existe evento de compra.** A venda fecha
fora do domínio e o pixel do redebolha nunca vê. Sem ele não há ROI mensurável.

## 4b. A discrepância que precisa ser resolvida antes de gastar

O pixel registrou 16 `Lead` entre 16 e 21 de agosto. O Meta atribuiu **zero** a
qualquer campanha — nenhuma delas retorna `offsite_conversion.fb_pixel_lead`.

Como as mesmas campanhas tiveram 499 visualizações de página atribuídas, o pixel
claramente casa o clique na chegada. Ele perde o casamento no fim do funil. Três
candidatos, em ordem de probabilidade:

1. Os anúncios antigos apontavam para uma URL diferente desta página.
2. O `Lead` dispara no clique de um link que navega para fora
   (`index.html` linha 323). O `target="_blank"` reduz o risco, mas em celular a
   troca para o app do WhatsApp ainda pode cortar a requisição em voo — e corta
   justamente nos usuários que mais importam.
3. Volume abaixo do limiar de relatório do Meta, com 6 dias e R$ 88 gastos.

Isso se resolve olhando o `Lead` no Gerenciador de Eventos e conferindo o
detalhamento por origem. É o primeiro passo, antes de qualquer real novo.

**Melhoria recomendada no código:** dar ao `Lead` um `eventID` e mandar o mesmo evento
por CAPI do servidor, com deduplicação. Isso torna o número confiável
independentemente da navegação.

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

## 5b. Um defeito no anúncio que eu mesmo montei

Configurei o destino como:

```
...?utm_source=meta&utm_campaign={{campaign.name}}&utm_content={{ad.name}}
```

O nome da campanha é `Teste da Máscara Masculina | Tráfego` — com espaços, acentos e
uma barra vertical. O `etiquetaOrigem()` da página (linha 202) monta a etiqueta
concatenando esses valores, então a mensagem que chega no seu WhatsApp terminaria assim:

```
[ref: meta/Teste da Máscara Masculina | Tráfego/A-cara]
```

Longo, feio de ler no celular, e o caractere `|` não é seguro em query string — pode
ser truncado por algum cliente antes de chegar.

**Correção:** trocar a macro por um valor curto e fixo, `utm_campaign=mascara`, mantendo
`utm_content={{ad.name}}` (os nomes `A-cara`, `B-provedor`, `C-espelho` já são limpos).
Resultado: `[ref: meta/mascara/A-cara]`.

Criativo no Meta é imutável, então isso exige recriar os três criativos e os três
anúncios. Como nada rodou ainda, o custo é zero.

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

O proxy desta sessão bloqueia `redebolha.com.br`, então não consegui carregar a página
em execução. Mas o código-fonte foi auditado direto do repositório `Redebolha/redebolha`
(`teste-mascara-masculina/index.html`), o que resolveu a maior parte das dúvidas.

Continua em aberto apenas a causa exata da falha de atribuição (seção 4b), que depende
de olhar o detalhamento do evento `Lead` no Gerenciador de Eventos — e de conferir para
qual URL os anúncios de agosto realmente apontavam.

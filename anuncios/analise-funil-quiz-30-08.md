# Por que ninguém entrou em contato — análise do funil do teste

30/08/2026. Escrito depois de você confirmar que os links e os valores do
Hotmart estão certos, e que **ninguém mandou mensagem**.

Esse "ninguém" não é um detalhe. É o resultado do teste, e ele é conclusivo.

---

# PARTE 1 — O FUNIL INTEIRO, NÚMERO POR NÚMERO

| Etapa | Quantidade | Do passo anterior |
|---|---:|---:|
| Impressões | 4.856 | — |
| Cliques no anúncio | 480 | 9,9% |
| Visitas na página do quiz | 424 | 88,3% |
| Começaram o quiz | *não medido* | — |
| Terminaram o quiz | *não medido* | — |
| Cliques no botão do WhatsApp | 13 | **3,1% das visitas** |
| **Mensagens recebidas** | **0** | **0%** |
| Vendas | 0 | — |

Gasto: **R$ 30,46**. Custo por clique no WhatsApp: **R$ 2,34**. Custo por
contato: não existe divisão por zero.

## Onde está a perda

Duas perdas grandes, e elas são de naturezas diferentes.

**Perda 1 — 424 visitas viram 13 cliques (perde 97%).** Isso acontece *antes* do
WhatsApp. É gente que chega, olha o quiz e vai embora, ou começa e não termina.

**Perda 2 — 13 cliques viram 0 mensagens (perde 100%).** Essa é a que dói mais,
porque são as 13 pessoas que fizeram tudo certo: leram o anúncio, clicaram,
responderam seis perguntas, viram o resultado e **quiseram falar com você**.
Todas as treze desistiram no último centímetro.

---

# PARTE 2 — A DESCOBERTA MAIS IMPORTANTE: A MÉTRICA ESTAVA MENTINDO

O evento `Lead` do pixel dispara aqui:

```js
document.getElementById('maskWhatsappBtn').addEventListener('click', function(){
  fbq('track', 'Lead', { content_name: 'quiz_mascara_whatsapp_click' });
});
```

Ele dispara **no clique**. Não no envio da mensagem. Não no contato.

Então, quando eu te disse "13 Leads no pixel", o número estava tecnicamente
correto e praticamente vazio: **treze cliques, zero pessoas.** O evento mede uma
intenção que morre um segundo depois, num aplicativo onde o pixel não enxerga
mais nada.

Isso muda a leitura da semana inteira. Eu vinha investigando por que o Meta não
atribuía esses 13 Leads aos anúncios. A pergunta certa nunca foi essa. **Não
havia lead nenhum para atribuir.**

Um clique não é um lead. Enquanto o `Lead` estiver amarrado a um clique de saída,
todo relatório vai parecer melhor do que a realidade — a sua e a do Meta.

---

# PARTE 3 — POR QUE OS 13 DESISTIRAM

## O aparelho não é o problema principal

Levantei a divisão de dispositivos dos 1.406 eventos do período:

| Dispositivo | Eventos | % |
|---|---:|---:|
| Android | 1.163 | 82,7% |
| iPhone | 46 | 3,3% |
| Desktop | 197 | 14,0% |
| **Móvel (total)** | **1.209** | **86,0%** |

No desktop o `wa.me` é beco sem saída de verdade: abre o `web.whatsapp.com`, que
pede QR code de quem não está logado. Mas isso são 14% do tráfego. **Não explica
os 100%.**

## O que explica é o que você está pedindo em troca do quê

O botão diz:

> *"Manda seu resultado no WhatsApp — o autor tem um recado pra você"*

E a mensagem já vai escrita:

> *"Oi Romário! Fiz o teste e meu resultado foi: [máscara]. Vi que você tem um
> recado pra mim 👀"*

Coloca-se no lugar do cara. Ele é um homem de 30 a 60 anos, no celular, que há
quatro minutos não te conhecia. Ele acabou de responder seis perguntas íntimas
sobre si mesmo. O quiz devolveu um rótulo. E agora, para saber o que significa,
ele precisa:

1. abrir uma conversa privada com um número desconhecido;
2. entregar o próprio telefone para um estranho;
3. mandar uma mensagem dizendo, em essência, *"tenho um problema, me ajuda"*;
4. em troca de **um "recado" que ninguém disse qual é.**

Esse é o preço. E a recompensa é indefinida. Os treze chegaram até a tela do
WhatsApp, leram a mensagem que iam mandar, e fecharam. Eu faria o mesmo.

## E tem uma coisa a menos no site inteiro

Procurei formulário de captura em todas as páginas publicadas. O que existe:

- o formulário do quiz;
- três caixas de busca que mandam para o Google;
- o login do `/admin`.

**Não existe um único campo de e-mail no site.** Nenhuma newsletter ligada a
nenhum serviço. Ou seja: o WhatsApp não é o canal *preferido* de contato. É o
**único**. Não há plano B, e o plano A converteu zero.

---

# PARTE 4 — A REVISÃO DA ESTRATÉGIA

## O que precisa ser abandonado

**O WhatsApp como saída principal do quiz.** Não porque WhatsApp seja ruim —
porque nesta posição ele falha em três frentes ao mesmo tempo:

- **converteu 0 de 13**, com dinheiro pago em cima;
- **não guarda nada.** Um contato que não vira e-mail numa lista some quando a
  conversa esfria. Você não pode remarketing, não pode sequência, não pode nada;
- **depende de você.** Cada lead vira trabalho manual seu. Isso não escala, e no
  dia em que escalasse ia te consumir inteiro.

Ele fica — mas como terceira opção, para quem realmente quer conversar, e com uma
promessa concreta no lugar de "um recado".

## O que precisa entrar, na ordem

**1. A tela de resultado precisa dar antes de pedir.**
Hoje ela devolve um rótulo e cobra um passo. Precisa entregar, ali mesmo, sem
pedir nada: o que aquela máscara custa ao sujeito, onde ela aparece na vida
prática dele, e qual é o primeiro movimento para sair. Isso é conteúdo que você
já tem — é o livro. Três ou quatro parágrafos por máscara. Quem lê e se
reconhece já está com metade da venda feita.

**2. Depois disso, e só depois, as três saídas — nesta ordem:**

| Ordem | Saída | Para quem |
|---|---|---|
| 1ª | **O livro** (físico R$ 29,90 / e-book R$ 9,90), com a ponte da máscara dele | Quem se reconheceu e quer o resto agora |
| 2ª | **E-mail em troca do primeiro capítulo em PDF** | Quem se reconheceu mas não vai gastar hoje |
| 3ª | **WhatsApp**, com promessa concreta | Quem quer falar com uma pessoa |

A segunda é a que muda o seu negócio. É a única que constrói um ativo seu.

**3. Uma pergunta por tela.**
86% do tráfego é celular. Hoje as seis perguntas e as 36 alternativas estão todas
num formulário só, uma rolagem longa. Uma pergunta por tela, com a barra de
progresso que você já tem, é a mudança mais barata contra a Perda 1.

**4. O evento `Lead` muda de lugar.**
Sai do clique do WhatsApp. Vai para a captura do e-mail — quando existir contato
de verdade. E o clique do WhatsApp vira `Contact`, que é o evento correto para
isso. Assim o relatório para de mentir, e o Meta passa a otimizar para gente que
deixa contato, não para gente que clica e some.

**5. O pré-requisito de tudo isso: um serviço de e-mail.**
Não dá para capturar e-mail sem ter onde guardar e de onde enviar. Isso precisa
ser resolvido antes do item 2 — é a única peça do plano que não está no código.

## Sobre subir o investimento em tráfego

Não suba ainda. E o motivo não é o custo — R$ 0,07 por visita é preço raro, o
anúncio está entregando muito bem. É que **cada real a mais hoje compra mais
visitas para um funil que termina em lugar nenhum.** Consertada a tela de
resultado, o mesmo real passa a valer muito mais.

---

# PARTE 5 — O QUE EU NÃO CONSEGUI MEDIR

**Quantos começaram e quantos terminaram o quiz.** Os eventos `QuizStart` e
`QuizComplete` são customizados (`trackCustom`), e a API de estatísticas do Meta
que eu uso só devolve eventos padrão — consultei os dois e voltou vazio. Eles
existem: o `Lead` só pode disparar depois de completar o quiz, então houve
conclusões. Os números estão no **Gerenciador de Eventos** e no **GA4**
(`quiz_start` e `quiz_complete`). Se você abrir o GA4 e me passar esses dois
números, eu fecho a Perda 1 com precisão em vez de estimativa.

**O `InitiateCheckout` atribuído.** Os 20 eventos de hoje ainda são recentes
demais para julgar atribuição. Fica para a próxima conferência.

---

*Dados da conta 351203535, campanha 52512807800029 e pixel 2570806596755923,
lidos em 30/08/2026 às 20:45 UTC. Código conferido no `main` publicado do
repositório Redebolha/Redebolha.*

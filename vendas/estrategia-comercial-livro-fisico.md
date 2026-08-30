# O comercial, a página da Hotmart e como vender rápido

30/08/2026. Análise do vídeo `comercial_hotmart.mp4` e da página
`go.hotmart.com/R106833548K?dp=1`.

---

# PARTE 1 — A SUA PERGUNTA: "dá para usar esse comercial para vender os e-books?"

**Dá. Mas você não deveria querer.** E o motivo é dinheiro, não gosto.

Esse vídeo não é um comercial de e-book. Ele é um comercial de **livro físico com
e-book de brinde**. Toda a construção dele leva para lá: o livro na mesa com a
cuia, você folheando o exemplar impresso, e o fecho em três linhas —
*livro físico + frete grátis + e-book bônus*. Se você apontar ele para o e-book
de R$ 9,90, você está usando um comercial de R$ 29,90 para vender R$ 9,90.

E tem a conta, que eu já tinha feito e que não mudou:

| Produto | Margem estimada | Conversão necessária para o anúncio se pagar |
|---|---|---|
| E-book R$ 9,90 | ~R$ 9,00 | **0,94%** |
| Físico R$ 29,90 | depende do frete | menor — e é o único que pode fechar |

Tráfego frio no Meta converte entre 0,3% e 1% para produto de ticket baixo, e
isso quando tudo dá certo. **O e-book de R$ 9,90 não paga anúncio.** Ele é uma
porta de entrada excelente e um alvo de campanha péssimo.

## Então como os e-books vendem?

Nas três formas que **não custam mídia**:

1. **Como o próprio bônus.** Cada livro físico vendido entrega um e-book. A pessoa
   te lê digital pela primeira vez sem você pagar nada por isso.
2. **No e-mail depois da compra.** *"Você escolheu o Amanhã É Outro Agora. O Poder
   da Decisão fecha o par por R$ 9,90."* Quem já comprou de você compra de novo com
   uma facilidade que tráfego frio nunca vai ter.
3. **No orgânico** — o site, os artigos, a tela de resultado do quiz.

Isso responde a pergunta de verdade: o e-book não vende com anúncio, **vende na
sequência de quem comprou o físico.** O físico é a locomotiva. Os e-books são os
vagões.

---

# PARTE 2 — A OFERTA ESTÁ CERTA. E VOCÊ MELHOROU A MINHA.

Eu tinha recomendado: físico + frete grátis + **um** e-book à escolha entre dois.

Você fez com **três** opções — incluindo a versão digital do próprio livro. Ficou
melhor, e por um motivo que talvez você nem tenha pensado: quem compra o impresso
e escolhe o digital do mesmo título leva o livro no bolso e na estante. É o cara
que quer reler no ônibus. Você acabou de criar a opção favorita dele.

A página da Hotmart está bem construída. Ela faz as quatro coisas que uma página
de oferta precisa fazer:

- **diz o que chega** (livro impresso + frete grátis + e-book de presente);
- **diz por que importa** (o parágrafo do "manual de autoajuda vazio" é bom);
- **diz como funciona o bônus** (escolha na plataforma após a confirmação);
- **diz o que fazer agora** (botão único, verbo no infinitivo: *garantir meu livro*).

Não mexeria nela agora. Ela não é o gargalo.

---

# PARTE 3 — O QUE ESTÁ ERRADO NO VÍDEO (e o que eu já consertei)

O conteúdo está ótimo. O **formato** está errado para o lugar onde ele vai rodar.

## Problema 1 — o vídeo é deitado

`1280 × 720`, 16:9. Esse é o pior formato possível no Meta hoje. Reels e Stories
são 9:16. O Feed prefere 4:5. Um vídeo 16:9 entra pequeno, com tarja preta em
cima e embaixo, e some no meio da rolagem.

**Resolvido.** Gerei duas versões em `anuncios/criativos/`:

| Arquivo | Formato | Onde usar |
|---|---|---|
| `comercial-9x16.mp4` | 1080 × 1920 | Reels, Stories |
| `comercial-4x5.mp4` | 1080 × 1350 | Feed do Facebook e do Instagram |

Em vez de cortar as laterais (o que ia decepar você ou o texto), coloquei o vídeo
inteiro num cartão e usei o espaço que sobra para a oferta escrita grande: os três
itens, o preço e o botão. **Assim a oferta é legível no primeiro quadro** — mesmo
para quem assiste um segundo e rola. Nenhum pixel foi ampliado; a nitidez é a mesma
do original.

## Problema 2 — os últimos 2 segundos estão jogados fora

O vídeo termina com um print da página da Hotmart. No celular aquele texto é
ilegível — são letras de 4 pixels de altura. São **2 dos 10 segundos**, 20% do
comercial, gastos no ponto mais valioso do anúncio: o fim, onde a decisão acontece.

**Resolvido.** Cortei os últimos 2 segundos nas duas versões. A informação daquele
print agora está no painel, em corpo grande, o tempo todo.

## Problema 3 — o áudio bate no teto

O pico está em 0,0 dB, que é o limite absoluto do digital. Risco de estalo em
celular. Coloquei um limitador em 0,95 nas duas versões. Detalhe pequeno, mas de
graça.

## O que eu não consegui avaliar

**O que você fala.** Não tenho como ouvir o áudio — sei que existe fala e sei os
níveis, mas não o conteúdo. Se a locução repete o que está no painel, vale trocar
por uma frase que o painel não diz.

---

# PARTE 4 — PARA ONDE MANDAR O ANÚNCIO (e uma armadilha do Hotmart)

Aqui tem uma decisão técnica que muda tudo, e ela vem do que você configurou hoje.

Hoje você deixou os quatro produtos do Hotmart com **só "Vendas realizadas"**, com
as visitas de página desmarcadas. Isso estava **certo** — porque quem ia disparar
o `InitiateCheckout` era o site.

Mas se você mandar o anúncio **direto** para `go.hotmart.com`, o site sai do
caminho. E aí o Meta passa a receber **só o Purchase**, e mais nada. Sem sinal
nenhum antes da venda, ele não tem como otimizar: precisaria de ~50 vendas por
semana para aprender, e você ainda não tem a primeira.

**Duas saídas:**

**(a) Recomendada — o anúncio cai numa página sua.** Uma página no
`redebolha.com.br` com esse vídeo e o botão que leva ao Hotmart. Vantagens:
o site dispara `PageView`, `ViewContent` e `InitiateCheckout` (o Meta tem o que
otimizar desde o primeiro dia), o Hotmart dispara o `Purchase`, e nada conta em
dobro. De quebra, a visita é sua — dá para remarketing, dá para melhorar a página,
dá para medir onde a pessoa desiste.

**(b) Se for direto para o Hotmart mesmo assim** — você precisa voltar lá e
**remarcar "Visitas na Página de produto Hotmart"**. Senão o Meta fica cego.

Eu faria a (a). E posso montar essa página hoje.

---

# PARTE 5 — O NÚMERO QUE PODE AFUNDAR TUDO ISSO

É a terceira vez que eu peço, e agora ficou urgente por um motivo novo:
**o frete grátis está anunciado em público.** Está no comercial, está na página
da Hotmart, está na minha arte. Não dá mais para voltar atrás sem queimar a
oferta.

Então a conta precisa ser feita agora:

```
R$ 29,90  preço
        − taxa da Hotmart  (confere o valor exato no teu extrato)
        − custo de impressão do exemplar
        − frete que você está pagando
        = o que sobra para pagar o anúncio
```

Se sobrar **R$ 15**, o anúncio precisa de uma venda a cada 176 visitas. Apertado,
mas fecha.
Se sobrar **R$ 6**, cada venda que você fizer com tráfego pago te dá prejuízo — e
quanto mais você vender, mais você perde. É o único cenário em que o sucesso é a
pior notícia possível.

**Me manda esses dois números — impressão e frete — e eu refaço a conta com
precisão em cinco minutos.** Até lá, tudo o que está aqui vale com essa ressalva.

---

# PARTE 6 — A ORDEM, PARA VENDER O MAIS RÁPIDO POSSÍVEL

**Hoje / amanhã**
1. Me passa o custo de impressão e de frete. *(bloqueia o resto)*
2. Eu monto a página da oferta no site, com o vídeo e o botão do Hotmart.
3. Você sobe as duas versões verticais no Gerenciador de Anúncios.

**Assim que a página estiver no ar**
4. Campanha nova: objetivo **Vendas**, otimizando por **InitiateCheckout**
   (não por Purchase ainda — não tem volume para o Meta aprender).
5. Deixa a campanha do quiz rodando em paralelo, com o orçamento que já tem.
   Compara custo por venda, não custo por clique.

**Na sequência**
6. Consertar a tela de resultado do quiz (o outro documento de hoje).
7. Serviço de e-mail — sem ele não existe o e-mail de pós-compra, que é onde os
   e-books vendem.

---

# PARTE 7 — O TEXTO DOS ANÚNCIOS

Três versões para testar. Uma por anúncio, mesmo criativo, mesmo público.

## A — a balança da vida

> Você já sentiu que está fazendo tudo certo e mesmo assim parece que está devendo
> alguma coisa?
>
> Pois é. Eu senti isso durante anos. Provedor, marido, pai, homem que não pode
> reclamar — a lista de cobranças chega antes do café.
>
> Escrevi *Homem, Você Não É Ridículo* para desmontar essa conta. Não é autoajuda
> de frase bonita. É um papo reto sobre o peso que a gente carrega sem nunca ter
> concordado em carregar.
>
> Chega impresso na sua casa, com frete grátis, e você ainda escolhe um e-book de
> presente para começar a ler hoje mesmo.

**Título:** Livro físico + frete grátis + e-book de presente
**Descrição:** R$ 29,90 — entrega em todo o Brasil

## B — o espelho

> Quando foi a última vez que você parou pra pensar em quem você é, e não no que
> esperam de você?
>
> Eu tenho 53 anos e levei uns bons anos pra fazer essa pergunta. Virginiano que
> sou, já tinha feito planilha de quase tudo na vida — menos disso.
>
> É sobre isso o *Homem, Você Não É Ridículo*. Sobre largar o peso do julgamento
> alheio e voltar a caber em si mesmo.
>
> Livro impresso na sua porta, frete por minha conta, e um e-book de brinde à sua
> escolha.

**Título:** O livro que devolve o homem pra ele mesmo
**Descrição:** R$ 29,90 com frete grátis para todo o Brasil

## C — direto na oferta *(controle)*

> *Homem, Você Não É Ridículo* — o livro impresso na sua casa.
>
> ✔ Frete grátis para todo o Brasil
> ✔ 1 e-book de presente, à sua escolha, liberado na hora
> ✔ R$ 29,90
>
> Um convite pra desmontar culpas, largar o peso do julgamento alheio e recomeçar
> com o pé no chão.

**Título:** Livro físico + frete grátis + e-book bônus
**Descrição:** Garanta o seu por R$ 29,90

---

*A página da Hotmart foi lida pelos quadros finais do próprio vídeo — a rede desta
sessão bloqueia o domínio, então não consegui abrir a página ao vivo. Se algum
detalhe dela mudou depois da gravação, me avisa.*

# Anúncio — Teste da Máscara Masculina

**Status do criativo:** slot da imagem deixado **em aberto** — a arte sobe manualmente
no Gerenciador de Anúncios (ver seção 4).

Funil: Meta Ads → `redebolha.com.br/teste-mascara-masculina` → WhatsApp com IA → venda.

---

## O fio que precisa amarrar

Antes do texto, vale enxergar o funil inteiro numa linha só:

**Anúncio faz a pergunta → o teste dá o nome → o WhatsApp entrega o recado →
o recado leva ao livro.**

Isso muda uma coisa no anúncio: ele não vende teste, e muito menos vende
livro. Ele vende **uma pergunta que a pessoa não consegue deixar sem
resposta**. Todo o resto do funil já está construído para receber quem clicar.

A mensagem que a pessoa envia no WhatsApp termina com *"Vi que você tem um
recado pra mim"*. Então o anúncio precisa plantar essa ideia lá atrás: existe
um recado esperando. Os textos abaixo fazem isso.

---

## 1. Anúncio A — "A cara" (principal)

Este é o mais forte. O gancho está na segunda linha, antes do "ver mais".

**Texto principal:**

> Tem homem que chega em casa e leva uma hora pra tirar a cara do trabalho.
>
> Não a roupa. A cara.
>
> Se você se reconheceu aí, faz esse teste. Seis perguntas, menos de dois
> minutos, sem cadastro. Ele não te rotula — só dá nome no que você já sente
> faz tempo.
>
> No fim, tem um recado esperando por você.

**Título:** Qual máscara você usa sem perceber? *(35)*

**Descrição:** Grátis · 2 min · sem cadastro *(29)*

**CTA:** Saiba mais

---

## 2. Anúncio B — "O provedor" (público mais amplo)

Provedor Cansado é a máscara que mais aparece. Vale um anúncio só pra ela.

**Texto principal:**

> Você já parou pra pensar quantos anos faz que você não para?
>
> Não é férias que eu tô falando. É parar de verdade. Sem calcular boleto,
> sem responder mensagem, sem carregar ninguém nas costas por meia hora que
> seja.
>
> Fiz um teste de seis perguntas sobre isso. Dois minutos, sem cadastro, e ele
> te devolve o nome da coisa que você carrega calado.
>
> Só isso já muda alguma coisa.

**Título:** Faz quanto tempo que você não para? *(34)*

**Descrição:** Teste gratuito · 2 minutos *(26)*

**CTA:** Saiba mais

---

## 3. Anúncio C — "O espelho" (direto ao criativo)

O mais curto. Serve para testar se a imagem sustenta sozinha.

**Texto principal:**

> Toda manhã você coloca uma. Toda noite tenta tirar. E às vezes ela não sai.
>
> Seis perguntas, dois minutos, sem cadastro: descubra qual máscara você usa
> sem perceber.

**Título:** Homem, qual máscara é a tua? *(27)*

**Descrição:** 6 perguntas. Sem cadastro. *(26)*

**CTA:** Saiba mais

---

## 4. A imagem (upload manual)

O conceito está certo. Homem diante do espelho, máscara já retirada na mão,
luz baixa, dourado e escuro da marca. E tem uma inversão boa ali: ele **não
está** usando a máscara — já tirou. A parte difícil não é colocar, é olhar
depois que tira.

Três ajustes antes de subir:

**1. Tire a moldura.** Hoje a arte está dentro de um card com borda, cabeçalho
"Rede Bolha" e canto arredondado, como se fosse um print de página. No feed do
celular isso encolhe tudo que importa. Faça a imagem sangrar até a borda e
ganhe uns 20% de tamanho em cada palavra.

**2. Corte a linha de baixo.** A URL e o "Por Adm. Romário Cruz — autor de
Homem, Você Não É Ridículo" ficam ilegíveis em tamanho de feed e roubam espaço.
A URL já vai no link do anúncio; a autoria já está no perfil.

**3. Exporte em três formatos.** O que você mandou é story (9:16). Para o feed
você precisa de 4:5, e de 1:1 para alguns posicionamentos. Mesma arte, três
enquadramentos — não deixe o Meta cortar sozinho, porque ele corta justamente
a palavra "máscara".

Mantenha o selo **"2 MINUTOS · SEM CADASTRO"**. Ele derruba as duas objeções
antes de aparecerem.

### Checklist do upload manual

- [ ] 9:16 (1080 × 1920) — Stories e Reels
- [ ] 4:5 (1080 × 1350) — Feed
- [ ] 1:1 (1080 × 1080) — demais posicionamentos
- [ ] Sem moldura, sangrando até a borda
- [ ] Sem a linha de URL/autoria no rodapé da arte
- [ ] Selo "2 MINUTOS · SEM CADASTRO" presente
- [ ] Texto sobre a imagem abaixo de ~20% da área

### Dois criativos para testar contra esse

**Criativo 2 — O sofá.** Homem sentado no sofá de casa, ainda de roupa de
trabalho, olhando pro nada. Sem máscara na cena. Texto: *"Não a roupa. A
cara."* Testa o gancho verbal sem a metáfora visual.

**Criativo 3 — Só tipografia.** Fundo escuro, sem foto. A pergunta grande em
dourado. Anúncio sem rosto às vezes ganha do com rosto, porque não parece
anúncio. É barato de fazer e vale o teste.

---

## 5. Configuração da campanha

**Objetivo:** Tráfego, otimizado para visualizações da página de destino.
Assim que acumular perto de 50 eventos `Lead` por semana, troque a otimização
para conversões no evento `Lead` — aí o Meta passa a caçar quem realmente
termina o teste e clica no WhatsApp.

**Público:** homens, 30 a 60 anos, Brasil. Sem interesses no começo. Deixe o
algoritmo achar — o criativo é específico o suficiente pra filtrar sozinho.

**Posicionamentos:** automáticos, com os três formatos de imagem carregados.

**Orçamento:** o mesmo R$ 15/dia para começar. Rode os três textos no mesmo
conjunto e deixe o Meta escolher.

**Horário:** se for testar programação, começo de noite (19h às 21h30) casa
com o texto. É a hora em que o cara chegou em casa e está exatamente na cena
que o anúncio descreve.

---

## 6. Parâmetros de URL (não pule esta parte)

No campo **Parâmetros de URL** do anúncio, cole:

```
utm_source=meta&utm_campaign={{campaign.name}}&utm_content={{ad.name}}
```

É isso que faz a etiqueta `[ref: ...]` aparecer no fim da mensagem que chega
no seu WhatsApp. Sem esses parâmetros, você recebe as conversas sem saber qual
anúncio pagou por elas — e aí não dá pra decidir o que desligar.

Nomeie os anúncios de forma legível: `A-cara`, `B-provedor`, `C-espelho`.
O nome vai inteiro para dentro da etiqueta.

---

## 7. O que medir, em ordem

1. **CTR do anúncio** — o criativo funciona?
2. **QuizStart ÷ PageView** — a página segura quem chega?
3. **QuizComplete ÷ QuizStart** — as seis perguntas são longas demais?
4. **Lead ÷ QuizComplete** — o resultado dá vontade de falar com você?
5. **Venda ÷ Lead** — a IA do WhatsApp fecha?

Cada etapa tem um culpado diferente. Se a queda estiver na 3, o problema é o
teste, não o anúncio. Se estiver na 5, é o script da IA. Olhar só o custo por
venda esconde onde o dinheiro está vazando.

---

## 8. Um cuidado na moderação

Vão aparecer comentários de homens contando coisa séria embaixo desse anúncio.
Acontece sempre que o assunto é esse.

Se alguém comentar algo que soe como sofrimento real, **não responda com link
nem com venda**. Responda como pessoa, e o CVV é gratuito, 24 horas, no 188.
Vale a mesma regra que está no documento da IA.

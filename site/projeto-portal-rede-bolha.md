# De página de venda a portal — análise e projeto

Feito em 29/08/2026, sobre o site publicado (commit `15af350`, 46 URLs no sitemap).

---

# PARTE 1 — O QUE O SITE É HOJE

## A descoberta que muda a conversa

Eu esperava encontrar uma loja com alguns artigos pendurados. Encontrei outra coisa:

**O site já é um portal. Ele só está organizado como uma loja.**

| O que existe | Volume |
|---|---|
| Artigos | 22 · 15.602 palavras |
| Hubs de tema | 7 |
| Ferramentas gratuitas | 2 (simulador de renda passiva, calculadora de FIIs) |
| Teste interativo | 1 (máscara masculina) |
| Páginas de venda | 4 |
| **URLs no sitemap** | **46** |

Quarenta e seis URLs, e só quatro vendem. O conteúdo gratuito já é a maior parte do
site — ele simplesmente não aparece. A home tem 1.830 palavras e **sete botões de
compra**. O menu tem onze itens, e "Comprar" é o único destacado.

Ou seja: a virada que você quer fazer é **menos construção do que parece**. É mais
reorganização do que criação.

## Onde o site está fraco de verdade

Agora a parte que dói, e ela não é sobre design.

**1. Profundidade.** A média dos 22 artigos é de **709 palavras**. Só dois passam de
mil: *O silêncio que mata* (1.490) e *Ponto de virada* (1.404). Para masculinidade e
fé isso ainda segura. Para **finanças, aposentadoria e empreendedorismo — que é para
onde você quer ir — não segura.** Nesses nichos, quem ranqueia publica de 1.500 a
3.000 palavras com dados, tabelas e fontes citadas. Você vai competir com banco,
corretora e portal de investimento, que têm equipe.

**2. Os sete hubs de tema.** Olhe os números:

| Hub | Palavras |
|---|---|
| /masculinidade/ | 503 |
| /paternidade/ | 508 |
| /relacionamentos/ | 496 |
| /fe-e-identidade/ | 526 |
| /proposito/ | 518 |
| /saude-emocional-masculina/ | 576 |
| /financas/ | 504 |

Sete páginas, todas entre 496 e 576 palavras. Essa uniformidade não é coincidência —
é a assinatura de página escrita para preencher estrutura, não para ser lida. O
histórico do próprio repositório registra isso: houve uma reescrita desses seis hubs
descrita como parte da correção de uma **reprovação do AdSense por conteúdo raso**.

Num portal, o hub de editoria é destino, não corredor. Hoje eles são corredor.

**3. Páginas vazias no menu.** `/fotos/` tem 62 palavras. `/livros/` tem 117.
`/videos/` tem 169. Elas ocupam três das onze vagas do menu principal e não entregam
nada. Num portal isso é espaço nobre desperdiçado.

**4. As duas ferramentas estão escondidas.** O simulador de renda passiva e a
calculadora de FIIs são, na minha leitura, **o ativo mais valioso do site inteiro** —
e estão enterrados dentro de `/financas/`. Ferramenta gratuita é o que gera link de
outros sites, visita recorrente e compartilhamento espontâneo em finanças. É o tipo de
página que trabalha sozinha por anos.

**5. Aposentadoria e empreendedorismo não existem.** Zero conteúdo. Dois dos temas que
você citou hoje não têm uma linha no site.

---

# PARTE 2 — A DECISÃO ESTRATÉGICA

## Preciso te dizer uma coisa antes do projeto

Você descreveu a mudança como "o livro vira merchandise e patrocinador, o site vira
portal gratuito". A ideia está certa. Mas tem uma conta que precisa ser feita de olhos
abertos.

**Portal se sustenta com escala. Livro se sustenta com conversão.**

Um portal com 5.000 visitas por mês, monetizado por AdSense no Brasil, rende algo entre
R$ 50 e R$ 200 por mês. Cinco vendas do livro físico a R$ 29,90 rendem mais que isso, e
você não precisa de 5.000 visitas para fazer cinco vendas.

O AdSense só vira receita relevante lá pelas 50 mil visitas mensais. Chegar lá com
conteúdo próprio, sem equipe, leva de doze a vinte e quatro meses. E a sua conta **já
foi reprovada uma vez** por conteúdo raso — vai precisar de aprovação nova.

**Isso não é motivo para não fazer.** É motivo para fazer na ordem certa. E a ordem
certa cabe numa frase:

> **Separe a receita do discurso.**

O livro continua pagando as contas. Ele só deixa de ser a primeira coisa que a pessoa
vê. O visitante chega para aprender; encontra um autor que sabe do assunto; e compra
porque quis, não porque foi empurrado.

Na prática isso significa: **os sete botões de compra da home viram um.** No rodapé.
Discreto. E o conteúdo assume o palco.

O ganho real da virada não é AdSense. É outro, e é maior:

- **Tráfego orgânico** — portal ranqueia, landing page não. Hoje você paga por cada
  visita no Meta Ads. Um artigo bem posicionado traz visita de graça, todo mês, por anos.
- **Autoridade** — quem escreve sobre aposentadoria de homem aos 50 vende mais livro
  sobre identidade masculina do que quem só anuncia o livro.
- **Reaproveitamento do anúncio** — o mesmo real investido leva a pessoa a um artigo em
  vez de a um teste. Ela lê, confia, e volta.
- **Lista própria** — portal justifica newsletter. Newsletter é o único ativo de
  audiência que não depende de algoritmo de ninguém.

---

# PARTE 3 — O PROJETO

## A nova arquitetura: seis editorias e uma bancada

Hoje são sete hubs de tamanho igual e sem hierarquia. Proponho seis editorias com peso
diferente, mais uma seção de ferramentas atravessando todas.

| Editoria | De onde vem | O que cobre |
|---|---|---|
| **Masculinidade** | `/masculinidade/` | identidade, máscaras, raiva, solidão, o que é ser homem hoje |
| **Saúde do Homem** | `/saude-emocional-masculina/` ampliado | emocional **e** física: exames, envelhecimento, corpo, sono, álcool |
| **Dinheiro** | `/financas/` | orçamento, dívida, investimento, **aposentadoria** |
| **Trabalho e Negócio** | **novo** | **empreendedorismo**, carreira, recomeço depois dos 40, demissão |
| **Família** | funde `/paternidade/` + `/relacionamentos/` | pai, filho, casamento, casa |
| **Fé e Propósito** | funde `/fe-e-identidade/` + `/proposito/` | fé sem sermão, legado, sentido |

**Por que fundir dois pares:** sete editorias com um autor só produz sete páginas
rasas — que é exatamente o problema de hoje. Seis com peso real é melhor que sete de
enfeite. Paternidade e relacionamentos são a mesma casa. Fé e propósito são a mesma
pergunta.

**Por que aposentadoria não vira editoria:** é um tema, não uma área. Ele rende mais
como **trilha dentro de Dinheiro** — uma série numerada que a pessoa percorre do começo
ao fim. Trilha prende leitor; categoria solta, não.

**A bancada de ferramentas** (`/ferramentas/`) sobe para o menu principal e reúne o
simulador de renda passiva, a calculadora de FIIs e o teste da máscara. É a página que
mais trabalha por você a longo prazo.

## O menu

Hoje: `Sobre · Livros · Artigos · Dinheiro · Instalar App · Vídeos · Fotos · Teste ·
Temas · Contato · **Comprar**` — onze itens misturando conteúdo, institucional e venda.

Proposto:

```
MASCULINIDADE · SAÚDE · DINHEIRO · TRABALHO · FAMÍLIA · FÉ · FERRAMENTAS        [Livros]
```

Sete editorias mais "Livros" discreto no canto — onde num jornal fica o classificado.
Sobre, Contato, Vídeos, Fotos e Instalar App descem para o rodapé, que é o lugar
natural deles.

## A home

Ela deixa de vender e passa a distribuir. Ordem proposta:

1. **Manchete** — o artigo mais forte da semana, grande, com imagem
2. **Três destaques** — um de cada editoria diferente
3. **Faixa de ferramentas** — as calculadoras, com uma linha de chamada cada
4. **A trilha em cartaz** — ex.: "Aposentadoria do homem comum, em 8 capítulos"
5. **Últimos artigos** — grade de seis
6. **Newsletter** — uma caixa, sem pop-up
7. **Rodapé com o bloco do autor** — foto, uma linha de bio, e aí sim os livros

O bloco de compra some do topo. **Um** CTA no rodapé, no lugar de sete espalhados.

## Como o livro vira patrocinador sem sumir

Três mecanismos, todos discretos e todos honestos:

**1. O selo de apoio.** Ao pé de cada artigo, um bloco padrão:

> *A Rede Bolha é mantida pelos livros do Adm. Romário Cruz. Se este texto te serviu,
> conhecer o trabalho dele é a forma de manter o resto gratuito.*
> **[ Ver os livros ]**

Isso é patrocínio de verdade — igual rádio pública. Não interrompe, e converte melhor
que banner porque chega depois do valor entregue.

**2. Contexto, não banner.** O artigo sobre herança paterna termina com um cartão do
capítulo do livro que trata do assunto. Quem leu 700 palavras sobre o pai está mais
perto de comprar do que quem viu um pop-up.

**3. A página de livros vira loja de verdade.** As 117 palavras atuais viram uma página
completa: sinopse, sumário, trecho, prefácio do Roque Bakof, opções de compra. Quem
chega ali já decidiu — merece uma página que responda tudo.

## As fases

Escrevi como projeto de execução, não como sonho. Cada fase entrega valor sozinha.

### Fase 0 — Não quebrar o que está medindo *(imediato)*

**A campanha está rodando e o veredito do Lead sai amanhã.** Nada nesta reforma toca a
página `/teste-mascara-masculina/` nem o funil do anúncio enquanto esse teste não
fechar. O portal se constrói ao lado, não por cima.

### Fase 1 — Reorganizar o que já existe *(1 a 2 semanas · sem escrever conteúdo novo)*

- Menu novo, com as seis editorias e as ferramentas
- Home reordenada como portal
- `/ferramentas/` criada, reunindo o que está espalhado
- `/fotos/`, `/videos/`, `/contato/` descem para o rodapé
- Selo de apoio ao pé dos 22 artigos
- Redirecionamentos dos hubs fundidos, para não perder o que o Google já indexou

**Esta fase sozinha já muda a cara do site.** É a de melhor retorno por hora gasta.

### Fase 2 — Dar profundidade ao que existe *(1 a 2 meses)*

- **Reescrever os sete hubs** como destino: 1.200 a 1.800 palavras cada, com o que a
  pessoa precisa saber sobre o tema e links para os artigos
- **Aprofundar os dez artigos mais fracos** de ~550 para 1.200+ palavras, com dados e
  fontes
- **Capas para os 19 artigos que não têm** — o prompt do lote 2 já cobre isso

### Fase 3 — O conteúdo que não existe *(2 a 4 meses)*

- **Trilha "Aposentadoria do homem comum"** — 8 artigos: quanto preciso, INSS na prática,
  o que é previdência privada, começar aos 50, o pai que sustenta filho adulto, a casa
  quitada conta?, o plano B do autônomo, a conversa com a esposa
- **Editoria Trabalho e Negócio** — 6 artigos para abrir: recomeçar depois dos 40,
  o medo de sair do emprego, o negócio que não decolou, sociedade com amigo, MEI na
  prática, o cansaço de quem é o próprio chefe

### Fase 4 — Ferramentas novas *(3 a 6 meses)*

Cada uma é um ímã de tráfego e link:

- Calculadora "quando eu posso parar" (aposentadoria) — a mais valiosa
- Simulador de quitação de dívida
- Checklist de exames por faixa etária
- Calculadora de custo real do carro

### Fase 5 — Monetização *(quando houver tráfego)*

Só depois das fases 2 e 3, com o conteúdo já profundo:

- **Nova submissão ao AdSense** — com hubs reescritos e 35+ artigos, o histórico de
  reprovação por conteúdo raso deixa de valer
- **Newsletter** — o formulário da home hoje não está ligado a serviço nenhum (está
  registrado no seu `OPCIONAIS-VISUAIS.md`). Ligar é pré-requisito.
- **Afiliados coerentes** — livro, corretora, plano de saúde. Só o que você usaria.
- **Os livros, sempre** — continuam sendo a receita principal por um bom tempo

## Como saber se deu certo

Métricas de portal são outras. Sugiro acompanhar quatro:

| Indicador | Hoje | 6 meses | 12 meses |
|---|---|---|---|
| Visitas orgânicas/mês | medir no GA4 | 3× | 10× |
| Artigos com 1.000+ palavras | 2 de 22 | 20 | 40 |
| Páginas por sessão | medir | 1,8 | 2,5 |
| Assinantes da newsletter | 0 | 300 | 1.500 |

Vendas do livro **não** devem cair na Fase 1. Se caírem, o CTA ficou discreto demais e
a gente ajusta. É reversível.

---

# PARTE 4 — O QUE EU FARIA PRIMEIRO

Se fosse para escolher três coisas e parar:

**1. O menu e a home (Fase 1).** Muda a percepção do site inteiro numa semana, sem
escrever uma linha de conteúdo novo.

**2. Os sete hubs reescritos.** É o que hoje mais atrapalha no Google e o que mais
rápido melhora — sete páginas, e você tem os textos na cabeça.

**3. A calculadora de aposentadoria.** É a ponte entre os dois mundos que você quer
unir: fala de dinheiro, fala de homem de meia-idade, e é gratuita e útil. Uma
ferramenta dessas, bem feita, traz mais gente do que dez artigos.

---

## Três ressalvas honestas

**Isso é trabalho de meses, não de fim de semana.** As fases 2 e 3 somam algo como
50 artigos e reescritas. Com um autor só, é um ano de trabalho consistente. O projeto
está desenhado para render em cada etapa justamente por isso.

**Portal e funil de anúncio querem coisas diferentes.** O anúncio quer decisão rápida;
o portal quer permanência. Dá para conviver — mas a página que recebe o anúncio deve
continuar sendo a do teste, não a home nova.

**A receita não muda no primeiro dia.** O livro continua sendo o que paga. Se a
expectativa for trocar a venda do livro por AdSense nos próximos meses, ela não se
confirma. A troca real é: menos dependência de anúncio pago, mais gente chegando
sozinha — e isso leva tempo para aparecer.

---

*Levantamento feito sobre o site publicado em 29/08/2026: 46 URLs do sitemap,
contagem de palavras de todas as páginas, estrutura da home, menu e histórico de
commits do repositório.*

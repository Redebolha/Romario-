# Prompt — coleção de imagens para o redebolha.com.br

Feito em 29/08/2026, a partir da leitura do código do site (repositório
`Redebolha/Redebolha`, 30 páginas HTML, `css/base.css`, `index.html`).

Este documento tem três partes:

1. **O diagnóstico** — o que o site já tem de bom visualmente e onde estão os buracos.
2. **O prompt** — para copiar e colar em qualquer gerador de imagem.
3. **A lista de arquivos** — nomes, tamanhos e o prompt específico de cada imagem.

---

# PARTE 1 — O que eu vi no site

## O que já está certo (e não deve ser mexido)

O site **já tem uma identidade visual definida e boa**. Isso é raro e é a melhor
notícia deste documento. As imagens novas precisam obedecer a ela, não substituí-la.

**A paleta** (está em `css/base.css`, linhas 7–18):

| Papel | Hex | Onde aparece |
|---|---|---|
| Fundo | `#0A0A0C` | corpo do site |
| Fundo 2 | `#121013` | seções alternadas |
| Cartão | `#1A171B` | caixas de trecho e bônus |
| **Ouro** | `#C9A24B` | destaque principal, botões, números |
| Ouro claro | `#E7CE8A` | citações em serifa |
| Ouro escuro | `#9A7A30` | detalhes, tags |
| **Vinho** | `#6B2737` | bandeira de preço, oração |
| Vinho claro | `#9A3A4C` | bordas de destaque |
| Texto | `#F1ECE3` | títulos |
| Corpo | `#C6C0B5` | parágrafos |
| Apagado | `#857F75` | legendas e fontes |

**As fontes:** Oswald (títulos, sempre CAIXA ALTA, peso 600–700), Cormorant Garamond
(itálico, para as citações), Inter (corpo do texto).

**A textura:** existe um ruído sutil por cima de tudo, a 4,5% de opacidade
(`feTurbulence`, `baseFrequency 0.9`). É o que dá o ar de papel impresso. As imagens
novas precisam conviver com isso.

**Os brilhos:** halos radiais dourados no topo do hero e atrás do bloco de oferta.

## Os sete buracos

**1. Dezenove dos vinte e dois artigos não têm capa.** Só três têm
(`o-silencio-que-mata`, `homem-necessario`, `homem-nao-e-ridiculo`). O grid "Últimos
artigos" da home e o hub `/artigos/` mostram cartões só de texto. Num site que vive de
fazer o sujeito clicar e ler antes de comprar, cartão sem imagem é clique perdido.

**2. Não existe um mockup do livro físico.** O site vende um livro **físico** por
R$29,90 com frete grátis — e mostra apenas a capa escaneada, achatada, de frente. Um
mockup tridimensional com o livro de pé e o e-book ao lado é, disparado, a imagem que
mais converte numa página de venda de livro. Hoje ela não existe no site.

**3. As quatro estatísticas são texto puro.** "−7 anos", "95%", "4 em 5", "½" estão
como números soltos numa faixa. São os dados mais fortes da página inteira e não têm
nenhum apoio visual. Um número desses vira imagem compartilhável — e imagem
compartilhável traz gente de graça.

**4. Os oito capítulos são cartões vazios.** "01 A herança do pai", "02 As máscaras que
cansam"... Só número e título. É a seção que explica o que a pessoa vai receber pelos
R$29,90, e é a mais crua da página.

**5. O hero não tem atmosfera.** A capa gira em 3D sobre um gradiente e um halo. Bonito,
mas a primeira dobra de um site de livro precisa de ambiente — e ambiente aqui é o que
o livro fala: penumbra, um homem de costas, uma janela, uma cadeira vazia.

**6. Os sete hubs de tema não têm cabeçalho visual.** `/masculinidade/`,
`/paternidade/`, `/relacionamentos/`, `/fe-e-identidade/`, `/proposito/`,
`/saude-emocional-masculina/`, `/financas/` — todos abrem em texto.

**7. Duas imagens ainda vêm do Blogger.** Isso está no próprio
`OPCIONAIS-VISUAIS.md` do repositório e continua pendente: a capa do hero (que é o LCP
da página, já com `fetchpriority="high"` esperando) e a foto do autor. **Essas duas não
são para gerar — são para migrar.** Baixe do Blogger e suba como
`/homem-voce-nao-e-ridiculo-capa.jpg` (620 × 925) e `/adm-romario-cruz.jpg` (420 × 420).

## A decisão criativa que amarra tudo

O livro se chama *Homem, Você Não É Ridículo* e fala de **máscaras** — o "estou bem", o
"consigo sozinho", o "sou forte". Então a coleção inteira segue uma regra:

> **Nunca mostrar o rosto inteiro de um homem.**

Costas, nuca, ombros, mãos, silhueta contra a janela, meio rosto na sombra, reflexo
parcial no espelho, a cadeira que ele acabou de deixar. Isso resolve três problemas de
uma vez: é fiel ao tema do livro, evita rosto de IA com aquela cara de plástico, e
mantém as imagens seguras para reaproveitar nos anúncios do Meta — que já reprovou
cinco peças desta conta por política de atributos pessoais.

Nada de homem visivelmente chorando, deprimido ou em crise. O tom é **contido**, não
dramático. Peso, não desespero.

---

# PARTE 2 — O PROMPT

## Como usar

O prompt tem duas partes. O **Bloco Mestre** vai colado no início de **toda** geração,
sem alterar uma vírgula — é ele que garante que as 55 imagens pareçam da mesma família.
Depois dele, você cola o prompt específico da imagem que quer.

Funciona em Midjourney, DALL·E, Ideogram, Flux, Firefly, Higgsfield ou em qualquer
agente de IA com ferramenta de imagem. Se estiver usando um agente que gera vários
arquivos de uma vez, cole também a Parte 4 (empacotamento) e ele monta o zip sozinho.

---

## BLOCO MESTRE — cole antes de cada imagem

```
SISTEMA VISUAL — REDE BOLHA / ADM. ROMÁRIO CRUZ

Você está gerando imagens para o site redebolha.com.br, que vende os livros do
escritor Adm. Romário Cruz sobre identidade masculina, fé e saúde emocional do
homem. Todas as imagens precisam parecer da mesma coleção.

PALETA — use apenas estas cores:
- Fundos: preto quase puro #0A0A0C, carvão #121013, grafite quente #1A171B
- Destaque: dourado envelhecido #C9A24B, dourado claro #E7CE8A, dourado escuro #9A7A30
- Acento: vinho profundo #6B2737, vinho claro #9A3A4C
- Claros: branco quente #F1ECE3, bege acinzentado #C6C0B5
NADA de azul, verde, ciano, roxo, rosa ou laranja saturado. Nada de branco puro.

LUZ:
Uma única fonte de luz quente, lateral e baixa, cortando a penumbra — luz de
abajur, de janela ao entardecer, de poste na rua. Sombras longas e profundas.
Contraste alto. O escuro ocupa 70% do quadro. Estilo claro-escuro, cinematográfico,
tipo Roger Deakins. Nunca luz difusa de estúdio, nunca fundo branco, nunca ambiente
clarinho.

TEXTURA:
Grão fino de filme por cima de tudo, sutil. Aspecto de fotografia analógica ou de
papel impresso. Nada de brilho digital, nada de aspecto 3D plastificado.

REGRA DE FIGURA HUMANA (obrigatória):
Nunca mostre o rosto inteiro e reconhecível de uma pessoa. Use costas, nuca, ombros,
mãos, silhueta contra a luz, meio rosto na sombra, reflexo parcial, ou apenas o
objeto que a pessoa deixou. Quando houver homem no quadro: brasileiro, 35 a 55 anos,
comum, roupa simples e real — camiseta, camisa de trabalho, moletom. Nunca modelo
de banco de imagens, nunca terno, nunca corpo de academia, nunca sorriso posado.

EMOÇÃO:
Contenção, não drama. Peso, cansaço, silêncio, pensamento — nunca choro, desespero,
mão na cabeça ou pose de sofrimento. Sempre com dignidade e respeito pelo homem
retratado.

TÉCNICO:
Fotografia realista (ou ilustração editorial quando o item pedir), 35mm ou 50mm,
profundidade de campo rasa, composição limpa com bastante espaço negativo para
texto. Sem marca d'água, sem logotipo, sem assinatura.

NÃO INCLUA (negativo):
texto, letras, palavras, números, tipografia, legenda, marca d'água, logotipo,
rosto inteiro nítido, olhar para a câmera, sorriso de propaganda, fundo branco ou
claro, luz de estúdio difusa, cores frias, azul, néon, HDR, saturação alta,
aspecto de banco de imagens, corpo de modelo, terno e gravata, mãos deformadas,
dedos a mais, arte de IA genérica, cara de plástico, bokeh exagerado.
```

---

## PARTE 3 — A LISTA DE ARQUIVOS

Estrutura de pastas do zip:

```
redebolha-imagens/
├── 00_LEIA-ME.txt
├── 01_hero/            3 arquivos
├── 02_mockups/         6 arquivos   ← os que mais vendem
├── 03_provas/          5 arquivos
├── 04_capitulos/       8 arquivos
├── 05_artigos/        20 arquivos
├── 06_temas/           7 arquivos
├── 07_social/          3 arquivos
└── 08_confianca/       3 arquivos
                       ─────────────
                       55 arquivos
```

### ⭐ LOTE 1 — os dez que mais vendem

Se for gerar só uma parte, gere estes primeiro. São os que tocam direto no botão de
compra:

`02_mockups/` inteira (6), `03_provas/dado-expectativa-vida.jpg`,
`01_hero/hero-fundo-desktop.jpg`, `01_hero/hero-fundo-mobile.jpg`,
`07_social/og-livro.jpg`.

---

### 01_hero/ — a primeira dobra

**`hero-fundo-desktop.jpg`** · 2400 × 1400 · JPG qualidade 82
> Um homem brasileiro de meia-idade, visto de costas, sentado na beirada da cama num
> quarto escuro de madrugada. Só a silhueta dos ombros e da nuca. A luz vem de uma
> janela à esquerda, âmbar, de poste de rua. O lado direito do quadro é quase preto —
> espaço vazio para o título entrar por cima. Ele está imóvel, pensando. Cena
> silenciosa e digna.

**`hero-fundo-mobile.jpg`** · 1200 × 1600 · JPG qualidade 82
> A mesma cena, recomposta na vertical: o homem de costas ocupa o terço de baixo, os
> dois terços de cima são penumbra com o brilho quente da janela. Espaço livre em cima
> para o título.

**`hero-textura-ouro.png`** · 1600 × 1600 · PNG com transparência
> Uma névoa dourada abstrata, circular, com partículas de poeira suspensas na luz.
> Fundo totalmente transparente. Serve de camada de brilho por cima do hero. Sem
> objeto nenhum, só luz e poeira.

---

### 02_mockups/ — as imagens que vendem o livro

**Atenção — estas seis são diferentes das outras.** A capa do livro é obra do Romário,
não pode ser inventada pela IA. Você precisa **enviar o arquivo da capa junto com o
prompt** (`homem-voce-nao-e-ridiculo-capa-frente.jpg`, que já está no repositório) e
pedir composição, não criação. Em ferramenta que aceite imagem de referência, use o
modo imagem-para-imagem. Se a ferramenta não aceitar, gere o cenário sem o livro e
monte a capa por cima depois — em qualquer editor, inclusive no celular.

> **Instrução a acrescentar nestes seis:** *Use EXATAMENTE a capa enviada em anexo.
> Não redesenhe, não altere o título, não invente tipografia. Apenas aplique a capa
> sobre a geometria do livro, com a perspectiva, a dobra e a luz corretas.*

**`mockup-livro-fisico-3d.png`** · 1600 × 1600 · PNG transparente
> O livro físico de pé, levemente girado (uns 15°), lombada visível à esquerda, capa
> de frente. Livro de bolso, capa fosca, uns 200 páginas. Luz dourada quente vindo da
> esquerda alta, sombra suave projetada no chão. Fundo totalmente transparente.

**`mockup-combo-fisico-ebook.png`** · 2000 × 1400 · PNG transparente
> O livro físico de pé à esquerda e um tablet à direita, ligeiramente atrás, mostrando
> a mesma capa na tela. A tela tem um brilho suave próprio. Os dois sobre uma
> superfície refletida escura. Fundo transparente. Esta imagem representa a oferta de
> R$29,90 — físico + e-book juntos.

**`mockup-livro-mesa.jpg`** · 1600 × 1200 · JPG qualidade 85
> O livro fechado sobre uma mesa de madeira escura, ao lado de uma xícara de café pela
> metade e um par de óculos de leitura. Luz baixa de abajur pela direita. Ambiente de
> casa, fim de noite, real e vivido — não cenário de estúdio. Um pouco de desordem
> honesta.

**`mockup-livro-maos.jpg`** · 1600 × 1200 · JPG qualidade 85
> Mãos masculinas de homem adulto — mãos de quem trabalha, não de modelo — segurando o
> livro aberto perto do meio. Enquadramento só das mãos e do livro, sem rosto. Luz
> quente lateral. As páginas com marcações discretas de caneta.

**`mockup-ebook-celular.png`** · 1200 × 1600 · PNG transparente
> Um celular de pé mostrando a capa do e-book na tela, visto levemente de lado. Reflexo
> sutil na tela. Fundo transparente. Serve para a seção do e-book de R$9,90.

**`mockup-tres-ebooks.png`** · 2000 × 1200 · PNG transparente
> Três livros lado a lado em leque, levemente sobrepostos, mostrando as três capas do
> catálogo (*Homem, Você Não É Ridículo*, *Amanhã É Outro Agora*, *O Poder da Decisão*
> — as três estão no repositório). Fundo transparente. Vai na seção "Nossos livros".

---

### 03_provas/ — os dados que abrem a ferida

São ilustrações editoriais, não fotografias. **Sem nenhum texto ou número na imagem** —
o número entra por cima no HTML, com a fonte Oswald do site.

**`dado-expectativa-vida.jpg`** · 1200 × 1200
> Ilustração editorial minimalista: duas velas lado a lado sobre fundo preto. A da
> esquerda inteira e acesa; a da direita queimada quase até o fim, chama pequena.
> Espaço vazio em cima. Só dourado, vinho e preto. Nenhum texto. Representa a diferença
> de anos de vida entre mulher e homem.

**`dado-acidentes-trabalho.jpg`** · 1200 × 1200
> Um capacete de obra desgastado, largado no chão de concreto, na penumbra. Luz dura de
> um lado só. Muito espaço escuro em volta. Nenhum texto.

**`dado-suicidios.jpg`** · 1200 × 1200
> Cinco cadeiras simples de madeira em fila contra uma parede escura. Quatro estão
> viradas de costas para quem olha; uma está de frente. Luz baixa e lateral. Silencioso
> e respeitoso — nunca mórbido. Nenhum texto.

**`dado-amizades.jpg`** · 1200 × 1200
> Uma mesa de bar redonda com quatro cadeiras, três vazias e uma só afastada, como se
> alguém tivesse acabado de sentar. Bar fechando, luz âmbar baixa. Nenhum texto.

**`fundo-dados-faixa.jpg`** · 2400 × 800
> Fundo horizontal abstrato: gradiente de preto para grafite com uma linha dourada
> fina cruzando na horizontal, e um brilho radial suave no centro. Textura de grão.
> Serve de fundo para a faixa das quatro estatísticas. Nenhum objeto, nenhum texto.

---

### 04_capitulos/ — os oito temas

Todos 1200 × 800, JPG qualidade 82. Ilustração editorial, um objeto por imagem,
composição centrada com espaço para texto embaixo. Sem texto na imagem.

| Arquivo | Prompt |
|---|---|
| `cap-01-heranca-do-pai.jpg` | Duas alianças de casamento gastas sobre uma fotografia antiga em preto e branco, de bordas puídas, numa mesa escura. Luz quente baixa. |
| `cap-02-mascaras-que-cansam.jpg` | Uma máscara neutra de teatro, sem expressão, pendurada num prego numa parede de madeira escura. Sombra longa projetada. |
| `cap-03-raiva.jpg` | Um punho fechado de homem adulto sobre a mesa, visto de cima e de lado, tenso mas parado. Só a mão e o antebraço. Luz dura lateral. |
| `cap-04-perdao.jpg` | Duas mãos masculinas — uma mais velha, com manchas de idade, uma mais nova — quase se tocando sobre uma mesa escura. Sem tocar ainda. |
| `cap-05-paternidade.jpg` | A silhueta de um homem adulto e uma criança pequena de mãos dadas, de costas, contra uma janela ao entardecer. Só as sombras. |
| `cap-06-casamento.jpg` | Duas xícaras de café numa mesa, uma cheia e uma vazia, com uma distância grande entre as duas. Luz de manhã cedo, baixa. |
| `cap-07-fe-sem-mascara.jpg` | Uma Bíblia antiga e usada, aberta, sobre uma mesa de madeira, com um feixe estreito de luz caindo em diagonal sobre as páginas. Ambiente escuro. |
| `cap-08-proposito-legado.jpg` | Uma trilha de terra subindo entre árvores ao amanhecer, vista de baixo, com névoa dourada. Sem pessoa nenhuma no quadro. |

---

### 05_artigos/ — as vinte capas que faltam

Todos **1200 × 675** (16:9), JPG qualidade 82. Este é o buraco mais barato de tapar e o
que mais rende: capa de artigo é o que faz a pessoa clicar, e clique em artigo é o que
alimenta o funil até o livro.

| Arquivo | Prompt |
|---|---|
| `por-que-homem-nao-chora.jpg` | Um espelho de banheiro embaçado, com a marca de uma mão passada nele. Ninguém no reflexo. Luz fria de banheiro contra fundo escuro. |
| `solidao-masculina.jpg` | Um homem de costas sentado sozinho numa arquibancada vazia de campo de futebol de bairro, ao anoitecer. Silhueta pequena no quadro. |
| `homem-e-o-envelhecimento.jpg` | Mãos de homem mais velho, com marcas e manchas, apoiadas no volante de um carro parado. Luz de fim de tarde entrando pelo vidro. |
| `fe-sem-mascara.jpg` | Um banco de igreja vazio, de madeira, com um feixe de luz de vitral caindo sobre ele. Nave escura ao redor. |
| `homem-diante-do-fracasso.jpg` | Uma placa de "fechado" pendurada por dentro do vidro de uma loja pequena, à noite, com o interior escuro. |
| `raiva-masculina.jpg` | Uma parede com uma marca de soco rebocada por cima, ainda visível na tinta. Luz rasante lateral. |
| `amor-nao-e-fraqueza.jpg` | Duas mãos entrelaçadas sobre um lençol amassado, vistas de cima, na penumbra de um quarto. Só as mãos. |
| `homem-e-o-perdao.jpg` | Uma carta manuscrita dobrada e desdobrada muitas vezes, com os vincos marcados, sobre uma mesa escura. Texto ilegível. |
| `heranca-paterna.jpg` | Um par de botas de trabalho gastas ao lado de um par pequeno de tênis infantil, na porta de casa. |
| `a-mascara-que-voce-usa-todo-dia.jpg` | Um homem de costas ajustando a gola da camisa diante de um espelho, com o reflexo fora de foco e escuro. Rosto irreconhecível. |
| `cansaco-emocional-do-provedor.jpg` | Uma pilha de contas e boletos ao lado de uma calculadora e uma caneca vazia, numa mesa de cozinha à noite. |
| `corpo-grita-o-que-a-boca-cala.jpg` | Uma cadeira de consultório médico vazia, com o papel do exame por cima do assento. Luz clínica dura contra ambiente escuro. |
| `casamento-comunicacao.jpg` | Um sofá com duas pessoas sentadas nas pontas opostas, vistas de costas e à distância, com o espaço vazio no meio. Televisão ligada, sem som. |
| `reconstruindo-a-identidade.jpg` | Um espelho quebrado com as peças já recolocadas no lugar, colado, refletindo luz dourada em cacos. |
| `homem-masculinidade-em-jogo.jpg` | Um par de chuteiras velhas penduradas por um cadarço num prego, numa parede de garagem. |
| `homem-e-a-lideranca.jpg` | Uma mesa de reunião vazia com uma cadeira puxada para trás, na penumbra, luz de um abajur só. |
| `crise-dos-40.jpg` | Um homem de costas, meio corpo, parado diante de uma bifurcação de estrada de terra ao entardecer. Silhueta pequena. |
| `homem-que-deixa-legado.jpg` | Uma árvore grande e antiga, vista de baixo, com luz dourada atravessando as folhas. Nenhuma pessoa. |
| `homem-e-o-dinheiro.jpg` | Uma carteira de couro gasta, aberta e quase vazia, ao lado de uma aliança, sobre uma mesa escura. |

E mais uma, para o artigo de finanças que já existe:

| `ponto-de-virada-renda-passiva.jpg` | Uma pequena bola de neve no alto de uma encosta ao amanhecer, com o rastro que ela deixou atrás. Luz dourada rasante. Nenhuma pessoa. |

---

### 06_temas/ — cabeçalhos dos sete hubs

Todos **1600 × 600**, JPG qualidade 80. Bem escuros, com espaço amplo à esquerda para o
título entrar por cima.

| Arquivo | Prompt |
|---|---|
| `tema-masculinidade.jpg` | Silhueta de ombros masculinos contra uma janela alta ao entardecer, muito escuro, panorâmico. Espaço vazio à esquerda. |
| `tema-paternidade.jpg` | Sombras de um adulto e uma criança projetadas num chão de madeira, vistas de cima. Luz quente lateral. |
| `tema-relacionamentos.jpg` | Duas cadeiras de cozinha frente a frente, com uma mesa entre elas, na penumbra. Panorâmico. |
| `tema-fe-e-identidade.jpg` | Um feixe de luz atravessando a poeira suspensa numa nave escura de igreja. Sem pessoas. |
| `tema-proposito.jpg` | Um horizonte de campo aberto ao amanhecer, névoa baixa, luz dourada rasante. Panorâmico, sem pessoas. |
| `tema-saude-emocional.jpg` | Uma janela com a persiana meio aberta, listras de luz âmbar cortando um quarto escuro. |
| `tema-financas.jpg` | Uma mesa com uma caderneta aberta, uma caneta e uma calculadora, na penumbra, luz de abajur. Sem texto legível. |

---

### 07_social/ — compartilhamento

Todos **1200 × 630**, JPG qualidade 85. Deixe o terço direito escuro e vazio: é onde o
título entra depois, na fonte Oswald.

**`og-padrao.jpg`** — Fundo abstrato escuro com névoa dourada radial e grão de filme.
Nenhum objeto. Serve de `og:image` genérico do site.

**`og-livro.jpg`** — O livro físico de pé no terço esquerdo do quadro, luz dourada
lateral, os dois terços da direita em penumbra. (Use a capa real, mesma regra dos
mockups.)

**`og-artigo-base.jpg`** — Fundo escuro com uma linha dourada horizontal fina no terço
inferior e brilho suave à esquerda. Base para montar a capa de artigos futuros.

---

### 08_confianca/ — o empurrão final

**`selo-compra-segura.png`** · 1200 × 400 · PNG transparente
> Ilustração minimalista em linha dourada fina sobre transparente: um cadeado fechado,
> um escudo e um caminhãozinho de entrega, alinhados na horizontal, com espaço igual
> entre eles. Traço fino e elegante, cor `#C9A24B`. Sem texto.

**`moldura-dedicatoria.png`** · 1400 × 1000 · PNG transparente
> Uma moldura decorativa de página, em traço dourado fino, estilo de folha de rosto de
> livro antigo — cantos ornamentados discretos, o miolo totalmente vazio e
> transparente. Serve para emoldurar as imagens de dedicatória.

**`fundo-oferta.jpg`** · 1600 × 1200
> Fundo abstrato para o cartão de oferta: preto profundo com um halo dourado radial
> saindo do centro-baixo e grão de filme. Nada além de luz. Nenhum objeto, nenhum texto.

---

## PARTE 4 — Empacotamento

Cole isto no fim, se estiver usando um agente que gera os arquivos e monta o pacote:

```
EMPACOTAMENTO

Gere cada imagem com o nome de arquivo exato indicado, na dimensão exata indicada.
Organize nas oito pastas descritas, dentro de uma pasta raiz chamada
"redebolha-imagens". Comprima a pasta raiz inteira em um único arquivo
"redebolha-imagens.zip".

Regras de arquivo:
- JPG para fotografia, qualidade 82 a 85, perfil sRGB.
- PNG com canal alfa apenas onde o item pedir transparência.
- Nenhum arquivo acima de 400 KB. Se passar, reduza a qualidade antes de reduzir
  as dimensões.
- Gere também uma versão .webp de cada JPG, lado a lado, com o mesmo nome.
- Nomes em minúsculas, sem acento e sem espaço — hífen como separador.

Inclua na raiz um arquivo 00_LEIA-ME.txt listando cada imagem, sua dimensão, seu
peso final e em qual página e seção do site ela deve ser usada.
```

---

## Três coisas que eu preciso te dizer antes de você rodar isso

**A capa do livro a IA não pode inventar.** Nos seis mockups, a capa precisa entrar como
imagem de referência — ela é obra sua. Se a ferramenta que você usar não aceitar
referência, gere o cenário vazio e monte a capa por cima depois. Dá dois minutos e o
resultado é melhor do que qualquer coisa que a IA fosse desenhar sozinha.

**Sua foto e a foto do Roque Bakof também não.** São pessoas reais. Continuam sendo as
fotos que já estão no site. A regra de "nunca mostrar rosto" é justamente para a IA
nunca precisar inventar gente — e nunca aparecer no seu site um rosto que não existe
posando de leitor.

**Cuidado ao reaproveitar isso em anúncio.** Se alguma dessas imagens for parar no Meta,
lembre que a conta já levou cinco reprovações por atributo pessoal. Imagem de homem
visivelmente sofrendo, combinada com texto em segunda pessoa, é o par exato que derruba
anúncio. As imagens desta coleção foram escritas contidas de propósito — mantenha assim.

E o mais barato de tudo, que nem precisa de IA: as duas imagens do Blogger. Baixar e
subir no seu próprio domínio melhora a velocidade da primeira dobra hoje, sem gerar
nada. Está pendente no seu `OPCIONAIS-VISUAIS.md` desde antes desta conversa.

---

*Elaborado a partir da leitura do código-fonte do site em 29/08/2026: `index.html`
(1.392 linhas), `css/base.css`, `css/rb.css`, as 22 páginas de artigo, os 7 hubs de tema
e os 4 arquivos de livro. O domínio redebolha.com.br está bloqueado pela política de
rede desta sessão — a análise foi feita sobre o repositório `Redebolha/Redebolha`, que
é o que está publicado.*

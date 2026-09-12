# Publicação — "Rico na vitrine, quebrado no extrato"

Matéria de capa da editoria de Economia, publicada em 12/09/2026.
Tudo que está aqui foi montado sobre o site real (`github.com/Redebolha/Redebolha`, branch `main`),
com o mesmo template das duas matérias anteriores de Economia.

## Arquivos novos (copiar para o repositório do site)

| Deste repositório | Vai para o site em |
|---|---|
| `site/economia/rico-na-vitrine-quebrado-no-extrato.html` | `/economia/rico-na-vitrine-quebrado-no-extrato.html` |
| `site/economia/img/retrato-endividamento-brasil.svg` | `/economia/img/` — gráfico de abertura (desktop) |
| `site/economia/img/retrato-endividamento-brasil-vertical.svg` | `/economia/img/` — versão vertical, usada no celular |
| `site/economia/img/retrato-endividamento-brasil-og.jpg` | `/economia/img/` — imagem de compartilhamento (1200×630) |
| `site/economia/img/vitrine-versus-extrato.svg` | `/economia/img/` — card avulso, para redes sociais |
| `.png` correspondentes | `/economia/img/` — versões em bitmap dos mesmos gráficos |

## Arquivos alterados

| Arquivo | O que mudou |
|---|---|
| `index.html` | A matéria virou o carro-chefe do bloco de Economia da home; o dique desceu para a lateral e o "Ponto de virada" saiu da lista |
| `economia/index.html` | A matéria entrou como destaque do hub; o dique virou card comum |
| `economia/economia.css` | Duas classes novas: `.confronto` (quadro comparativo) e `.perguntas` (lista numerada). Nenhuma regra existente foi tocada |
| `sitemap.xml` | URL nova + `lastmod` atualizado na home e no hub de Economia |
| `feed.xml` | Item novo no topo do RSS + `lastBuildDate` |
| `service-worker.js` | Versão do cache virada de `redebolha-v8` para `redebolha-v9` — a home, o hub de Economia e o `economia.css` estão no pré-cache e mudaram |

O arquivo `publicacao-rico-na-vitrine.diff` traz o patch completo das alterações,
e a pasta `_site-redebolha/` guarda os arquivos já alterados, prontos para substituir.

## Situação

Publicado em 12/09/2026, direto na `main` do repositório do site
(commits `43e7502` e `0f880f8`). O deploy do GitHub Pages concluiu com sucesso e a
matéria está no ar em
https://redebolha.com.br/economia/rico-na-vitrine-quebrado-no-extrato.html

## Conferência feita antes de publicar

- Números batidos com a fonte: Peic/CNC de agosto de 2026 (82%, sétimo recorde seguido,
  29,9% de inadimplência, 85,1% até três salários mínimos, 72,3% acima de dez salários)
  e Raio X do Investidor Brasileiro, 9ª edição da Anbima com o Datafolha (64% e 31%).
- Páginas renderizadas em navegador a 1280px e a 390px: sem rolagem horizontal,
  gráfico legível no celular, quadro comparativo empilhando certo.
- `sitemap.xml`, `feed.xml` e os SVGs validados como XML.
- Todos os links internos da matéria conferidos, um a um, contra os arquivos do site.

## Segunda leva: foto de abertura e vídeo (12/09, mais tarde)

A abertura passou a ser a imagem da vitrine × extrato e a matéria ganhou o vídeo de
8 segundos. O infográfico do endividamento desceu para dentro do texto.

| Arquivo | O que é |
|---|---|
| `economia/img/vitrine-extrato-capa.jpg` | Abertura da matéria e chamada na home e no hub |
| `economia/img/vitrine-extrato-capa-og.jpg` | Imagem de compartilhamento, 1200×630 |
| `economia/img/vitrine-extrato.mp4` | Vídeo de 8 s, H.264 + AAC, 1,4 MB |
| `economia/img/vitrine-extrato-poster.jpg` | Quadro de capa do player |

Pendência conhecida: a imagem de abertura é um quadro limpo tirado do próprio vídeo,
porque a arte original tem o erro "QUEBRADO NO **O** EXTRATO" e a versão corrigida
chegou colada no chat, não como arquivo. Quando o arquivo corrigido chegar, é só
substituir `vitrine-extrato-capa.jpg` (e gerar de novo o `-og.jpg`, em 1200×630).

O vídeo foi cortado a partir de 2 s justamente para começar depois do letreiro com o erro.

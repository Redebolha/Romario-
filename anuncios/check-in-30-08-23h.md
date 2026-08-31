# Check-in dos anúncios — 30/08/2026, 23h UTC

Conferência agendada. Dois check-ins dispararam pedindo o mesmo veredito; este
documento responde aos dois.

---

# PARTE 1 — OS NÚMEROS DE HOJE

Campanha `52512807800029` · conjunto `52512807805029` · conta `351203535`

| | A-cara | B-provedor | Total |
|---|---:|---:|---:|
| Impressões | 395 | 3.010 | **3.405** |
| Cliques | 37 | 273 | **310** |
| CTR | 9,37% | 9,07% | 9,10% |
| CPM | R$ 6,35 | R$ 5,43 | R$ 5,53 |
| Visitas na página | 33 | 248 | **281** |
| Gasto | R$ 2,51 | R$ 16,33 | **R$ 18,84** |

**Custo por visita: R$ 0,067.**

## O que mudou desde ontem

| | 29/08 | 30/08 |
|---|---:|---:|
| CTR | 11,75% | 9,10% |
| CPM | R$ 8,41 | R$ 5,53 |
| Custo por visita | R$ 0,085 | **R$ 0,067** |
| Impressões no B-provedor | 85% | **88%** |

O CPM caiu 34% e a visita ficou 21% mais barata. O CTR recuou, mas o saldo é
positivo: está entregando mais visita por real.

**O CBO não corrigiu sozinho.** Continua concentrando quase 9 em cada 10
impressões no B-provedor. E vale registrar o que descobri ao puxar os previews:
**os dois anúncios usam a mesma imagem** — um homem de barba grisalha segurando
uma máscara branca, idêntica nos dois. A diferença é só o texto. Então o CBO não
escolheu uma imagem melhor; escolheu um texto melhor. Se a intenção do nome
"A-cara" era testar uma segunda imagem, ela nunca subiu.

## Orçamento

Não foi mexido. Os R$ 19/dia seguem de pé, conforme a recomendação de deixar
rodar 72h sem tocar.

## Segmentação

A mudança para **Rio Grande do Sul** foi aplicada às 21h e já passou pela
revisão do Meta — o conjunto voltou a `ACTIVE`. O Meta confirma a região pelo
nome: `{"key":456,"name":"Rio Grande do Sul","country":"BR"}`.

Os números acima misturam o dia inteiro, antes e depois da troca. O efeito real
do recorte só aparece amanhã, e com o aprendizado reiniciado.

---

# PARTE 2 — O VEREDITO

| Evento | No pixel | Atribuído aos anúncios |
|---|---:|---:|
| Lead | 13 | **0** |
| InitiateCheckout | 25 | **0** |
| **Purchase** | **0** | **0** |

## Purchase zerado é o esperado

O Hotmart foi configurado hoje e não houve venda desde então. Não há defeito a
investigar — há uma venda a fazer.

## InitiateCheckout zerado NÃO é falha de atribuição

Foram 25 disparos, sendo 21 depois do PR #19 (contra 4 na semana inteira antes
dele — o rastreamento novo funciona). Mas **todos os 25 dispararam em
`redebolha.com.br/`, a home.** Nenhum na página que o anúncio enche.

O anúncio leva para `/teste-mascara-masculina/`, que não tem botão de compra
nenhum. Então o anúncio **realmente** produziu zero InitiateCheckout. O Meta
está certo em reportar zero. Isso não é bug de medição, é o buraco do funil já
documentado em `analise-funil-quiz-30-08.md`.

## E o Lead: a recomendação antiga está superada

O check-in agendado mandava, se o Lead continuasse zero com 250+ visitas,
recomendar o patch de `eventID` + CAPI. **Essa recomendação não vale mais**, e
o motivo apareceu na análise de hoje:

O evento `Lead` dispara **no clique do botão do WhatsApp**, não no contato. São
13 cliques e — confirmado pelo Romário — **zero mensagens recebidas**. O CAPI
teria deixado uma métrica mentirosa mais precisa. O conserto não é de medição:
é mover o `Lead` para a captura de e-mail e trocar o clique do WhatsApp por
`Contact`.

---

# PARTE 3 — O QUE DESTRAVOU HOJE

O **PR #20 foi mesclado às 23h13**. A página `/oferta/` está no `main` e sobe
pelo GitHub Pages, com o vídeo, os eventos `ViewContent` e `InitiateCheckout`, e
o botão do Hotmart do livro físico.

Pela primeira vez existe uma página que o anúncio pode encher e que sabe vender.

**Próximo passo:** campanha nova com objetivo **Vendas**, otimizando por
`InitiateCheckout`, criativo nas versões vertical e 4:5, destino
`redebolha.com.br/oferta/`, público só do Rio Grande do Sul.

E antes de subir orçamento: a conta de `conta-margem-livro-fisico.md` diz que
tudo depende do frete. Com impressão a R$ 9,00, sobram R$ 16,94 para pagar
frete e anúncio. Acima de R$ 15 de frete, não fecha.

---

*Conta 351203535, campanha 52512807800029, pixel 2570806596755923, lidos em
30/08/2026 às 23h UTC.*

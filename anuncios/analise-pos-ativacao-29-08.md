# Análise depois de ligar — Teste da Máscara Masculina

Feita em 29/08/2026, com a campanha `52512807800029` **rodando**.
Base: dados ao vivo da conta 351203535, incluindo o dia de hoje (parcial).

## Veredito

**O anúncio está indo bem melhor do que a média da conta — e melhor do que qualquer
coisa que já rodou aqui.** CTR de quase 12% em tráfego frio, CPM de R$8,41, página
custando 8 centavos por visita.

Turbinar o orçamento não foi errado. Mas ele foi turbinado três vezes em catorze
horas, e isso tem um custo. E tem um número que continua zerado e que decide tudo.

## 1. O que você mexeu (do histórico da conta)

| Quando | O quê |
|---|---|
| 28/08, 20:04 | Orçamento R$15 → **R$9**/dia |
| 28/08, 21:15 | Campanha ligada |
| 28/08, 21:17 | Criativo do B-provedor trocado (texto v3) |
| 28/08, 22:27 | Criativo do A-cara trocado (texto v3) |
| 29/08, 09:52 | Orçamento R$9 → **R$15**/dia |
| 29/08, 09:53 | Orçamento R$15 → **R$19**/dia |

Três alterações de orçamento em catorze horas, todas pelo app do celular.

## 2. O que está no ar agora

Dois anúncios, não três.

| Anúncio | ID | Estado |
|---|---|---|
| A-cara | `52512816028029` | ATIVO, entregando |
| B-provedor | `52512816039629` | ATIVO, entregando |
| C-espelho | — | **reprovado de novo em 28/08 às 20:55 e removido** |

O C-espelho levou a terceira reprovação do mesmo conceito. Some com as anteriores e a
campanha já acumula cinco anúncios reprovados. Registro isso porque reprovação em série
pesa na reputação da conta — e a próxima pode vir sem aviso.

Os textos que estão no ar são os v3, em primeira pessoa, exatamente como foram
reescritos. Passaram na revisão. Sem erro de entrega em nenhum nível (`ads_get_errors`
volta vazio).

**Uma diferença em relação ao documento:** o CTA dos dois criativos novos está como
**"Ver detalhes"** (`SEE_DETAILS`), não "Saiba mais" (`LEARN_MORE`). Provavelmente o
padrão que o app do celular aplicou sozinho na troca. Não é problema — mas é uma
variável a mais que mudou junto, então guarde na cabeça.

Imagem: a mesma nos dois (`image_hash` idêntico). Correto — o que está em teste é o texto.

## 3. Os números

Acumulado dos dois dias (28 e 29/08, hoje parcial):

| | Impressões | Cliques | CTR | Gasto | CPM | CPC | Visitas na página |
|---|---|---|---|---|---|---|---|
| A-cara | 63 | 6 | 9,52% | R$0,48 | R$7,62 | R$0,08 | 6 |
| B-provedor | 371 | 45 | 12,13% | R$3,17 | R$8,54 | R$0,07 | 37 |
| **Total** | **434** | **51** | **11,75%** | **R$3,65** | **R$8,41** | **R$0,07** | **43** |

Para comparar com o que a conta já produziu: as campanhas de agosto deram CTR de
5,15% e 5,20%, que já era bom. A referência de mercado para tráfego frio no Brasil
fica entre 1% e 2%.

**Custo por visita na página: R$0,085.** No orçamento de R$19/dia, isso significa
aproximadamente **220 pessoas por dia na página do teste**, se o custo se mantiver.

O ritmo de gasto está saudável: ontem a campanha rodou 2h45 a R$9/dia e gastou R$1,08 —
praticamente o valor exato do rateio. Não existe entrega travada aqui.

## 4. O achado que muda a leitura do teste

Separando por dia, aparece uma coisa que o acumulado esconde:

| Anúncio | 28/08 — impressões | 28/08 — CTR | 29/08 — impressões | 29/08 — CTR |
|---|---|---|---|---|
| A-cara | 12 | 0% (0 cliques) | 51 | **11,76%** |
| B-provedor | 116 | 15,52% | 255 | **10,59%** |

**Hoje o A-cara está performando igual ao B-provedor — na verdade um pouco melhor.**

E mesmo assim continua recebendo cinco vezes menos entrega. O CBO decidiu o vencedor
ontem à noite, em cima de uma amostra de **12 impressões** do A-cara, e não voltou atrás.

Isso não é defeito do Meta, é como o CBO funciona: ele concentra no que parece melhor
o quanto antes. O problema é que "o quanto antes" foi cedo demais. Com 85% das
impressões num anúncio só, **o teste A/B que você montou não está acontecendo.**

## 5. O número que continua zerado

**43 pessoas chegaram na página. Nenhum Lead atribuído.**

Antes de soar o alarme: pela taxa histórica do próprio funil (3,2% de visita para
clique no WhatsApp), o esperado com 43 visitas seria **1,4 Lead**. Zero ainda cabe
confortavelmente no acaso. Não prova nada.

Mas é exatamente o número que a análise de ontem mandou vigiar, e agora ele tem prazo:

Com R$19/dia entregando ~220 visitas por dia, até amanhã à noite o acumulado passa de
**250 visitas**. Nessa altura o esperado é 8 Leads. Aí a leitura fica limpa:

- **Apareceu Lead atribuído** → o funil está de pé, a montagem antiga é que estava
  quebrada, e o orçamento pode subir com tranquilidade.
- **Continua zero com 250+ visitas** → não é acaso. É a página ou o evento, e aí vale
  o patch do `eventID` + CAPI que já está descrito no documento de ontem.

Não dá para decidir isso hoje. Dá para decidir amanhã.

## 6. As três coisas que eu faria

**1. Não mexer em mais nada por 72 horas.**

O conjunto está com o status `ad_set_in_learning_phase` neste momento. Cada alteração
de orçamento reinicia essa fase. Você fez três em catorze horas, e o último salto foi
de R$9 para R$19 — **+111% de uma vez**, quando a recomendação do próprio Meta é não
passar de 20% a 30% por ajuste.

Com objetivo de tráfego isso é perdoável: o aprendizado é rápido e barato. Se um dia a
campanha virar otimização por conversão — que é o plano — esse hábito passa a custar
caro de verdade. Vale começar a desmamar agora.

Deixa os R$19 rodarem três dias inteiros sem tocar.

**2. Decidir o que o teste é.**

Duas saídas honestas, e você escolhe uma:

- *Quero tráfego barato:* deixa como está. O B-provedor venceu, o CBO já sabe disso,
  e o custo por visita está ótimo. Só pare de chamar isso de teste A/B.
- *Quero saber qual texto é melhor:* tira o orçamento da campanha e põe no conjunto
  (ABO), com um conjunto para cada anúncio, ~R$10 cada. Aí os dois recebem entrega
  parecida e a comparação passa a valer. Custa mais e demora mais. Mas responde.

Pelos números de hoje, minha aposta é que os dois textos são equivalentes e o
B-provedor só ganhou na sorte da primeira hora.

**3. Parar de reenviar o C-espelho.**

Três reprovações do mesmo conceito. Antes de submeter qualquer versão nova dele, abra
"Ver detalhes" no Gerenciador e leia o motivo oficial — a API não expõe esse texto, e
já foram três tentativas no escuro. Dois anúncios rodando bem valem mais que um terceiro
que queima reputação.

## 7. O que continua pendente do documento de ontem

Nada disso mudou, e nada disso impede a campanha de rodar:

- Conversões Personalizadas para `QuizStart` e `QuizComplete` — ainda zero na conta.
- Pixel ausente na página do livro (`livros/homem-voce-nao-e-ridiculo.html`).
- Sem evento de compra. A venda do e-book na Amazon segue não rastreável — sempre será.
- A página de destino ainda fala em segunda pessoa ("Qual máscara **você** usa"), o
  mesmo padrão que derrubou os anúncios. Os anúncios v3 passaram assim mesmo, então na
  prática o risco é menor do que eu supunha ontem. Continua sendo um risco.

---

*Números colhidos ao vivo em 29/08/2026. O dia de hoje é parcial e a atribuição do Meta
leva algumas horas para consolidar — os totais de hoje ainda vão subir.*

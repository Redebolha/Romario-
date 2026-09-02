# Reprovação na revisão do Meta — o que era e o que foi feito

Data: 28/08/2026.

## O que a conta mostrava

| Anúncio (v2) | `status` | `effective_status` |
|---|---|---|
| C-espelho | PAUSED | **DISAPPROVED** |
| A-cara | PAUSED | **WITH_ISSUES** |
| B-provedor | **ACTIVE** | ADSET_PAUSED |

Erro retornado pela API para o A-cara:

> Can Not Enable Ad with Ad Review Rejected: Your ad has been rejected in its latest
> review and is currently disabled. In order to enable the ad, you will need to make
> updates to it and create a new ad.

Dois pontos a registrar:

1. **O B-provedor estava ACTIVE no nível do anúncio.** Só não rodou porque o conjunto
   estava pausado. Se o conjunto fosse ligado, ele começaria a entregar na hora. Já
   está pausado agora.
2. **A API não expõe o texto da política violada.** Ela devolve o estado
   (`DISAPPROVED`, `WITH_ISSUES`) e o erro de ativação, mas não o motivo. O motivo
   só aparece em "Ver detalhes" no Gerenciador de Anúncios.

## Diagnóstico

Sem o texto oficial, o motivo quase certo é a política de **Atributos Pessoais**.
Ela proíbe anúncio que afirme ou dê a entender que se conhece um atributo pessoal de
quem está lendo — e inclui explicitamente **estado emocional e saúde mental**.

Os três textos eram construídos exatamente assim, em segunda pessoa:

| Trecho reprovável | Anúncio |
|---|---|
| "Qual máscara **você** usa sem perceber?" | A (título) |
| "só dá nome no que **você** já sente faz tempo" | A |
| "Se **você** se reconheceu aí" | A |
| "quantos anos faz que **você** não para?" | B (título e corpo) |
| "o nome da coisa que **você** carrega calado" | B |
| "Toda manhã **você** coloca uma. Toda noite tenta tirar." | C |
| "Homem, qual máscara é a **tua**?" | C (título) |

O C-espelho, que era o mais direto de todos na afirmação sobre o leitor, foi
justamente o único com `DISAPPROVED` cheio. Isso reforça a leitura.

## A correção aplicada

Regra nova: **nada de afirmar coisa sobre quem lê.** O peso passa para a primeira
pessoa (a experiência do Romário) e para "a gente" — que inclui o autor em vez de
apontar o leitor.

| | Antes | Depois |
|---|---|---|
| A — título | Qual máscara você usa sem perceber? | As máscaras que a gente aprende a usar |
| B — título | Faz quanto tempo que você não para? | O cansaço que muito homem carrega |
| C — título | Homem, qual máscara é a tua? | As máscaras que a gente não tira |

Corpos reescritos para abrir em primeira pessoa ("Eu fui um deles", "Eu levei quase
quarenta anos", "Aos 53 anos eu ainda tenho as minhas") e para descrever o fenômeno em
geral ("tem homem que", "muito homem carrega"), nunca o leitor.

Imagem, público, orçamento, destino e UTM: sem alteração.

## Estado atual

| Anúncio | ID | Criativo | Estado |
|---|---|---|---|
| A-cara (v3) | `52512816028029` | `1459245612832597` | pausado, em revisão |
| B-provedor (v3) | `52512816039629` | `1065177359321004` | pausado, em revisão |
| C-espelho (v3) | `52512816029629` | `1692070885217108` | pausado, em revisão |

Os antigos: C-espelho v2 excluído; A-cara v2 e B-provedor v2 a API só conseguiu deixar
**pausados** (devolveu `status_forced_to_paused`), não excluídos. Não entregam nada
pausados, mas convém apagar os dois no Gerenciador para não confundir a leitura depois.

## O que ainda pode reprovar de novo

**A página de destino tem o mesmo problema, e o Meta revisa ela junto com o anúncio.**

Em `teste-mascara-masculina/index.html`:

- `<title>`: "Teste: Qual Máscara Você Usa Sem Perceber?"
- `<h1>` (linha 81): "Qual máscara você usa sem perceber?"
- Subtítulo: "só a real sobre o que **você** anda carregando por dentro"
- `meta description`: "**você** descobre qual máscara anda carregando sem nem perceber"
- `og:description`: "descubra qual máscara masculina **você** anda usando sem perceber"

São as mesmas afirmações em segunda pessoa que derrubaram os anúncios. Enquanto a
página falar assim, o anúncio limpo pode ser reprovado pelo destino.

Correção decidida junto com o Romário — é a linha da marca, não é decisão de tráfego.

## Um risco a considerar

Anúncio reprovado repetidamente pesa na reputação da conta. Já são três reprovações
nesta campanha. Vale confirmar o motivo real em "Ver detalhes" antes de submeter a
próxima versão, em vez de submeter no escuro mais uma vez.

---

# Ativação — 28/08/2026

## Segunda rodada de reprovação

O **C-espelho v3 também foi reprovado** (`DISAPPROVED`), mesmo reescrito em primeira
pessoa. O A-cara v3 e o B-provedor v3 passaram.

Isso é informação útil: os três usavam **a mesma imagem e a mesma página de destino**.
Como dois passaram, a imagem e o site estão limpos aos olhos da revisão — o problema
está no texto do C.

Hipótese para a próxima tentativa: o C era o mais curto dos três e o mais "de teste de
personalidade". Sem o contraponto em primeira pessoa que sustenta o A e o B, ele fica
parecendo diagnóstico. Ou o Meta reprovou por semelhança com a versão anterior, que já
tinha sido reprovada com o mesmo nome e a mesma imagem.

## Exclusões feitas

Excluídos de verdade (`DELETED`, sem forçar para pausado):

- `52512809262829` — A-cara v2 (estava `WITH_ISSUES`)
- `52512809278829` — B-provedor v2
- `52512816029629` — C-espelho v3 (estava `DISAPPROVED`)

## Ativação — INCOMPLETA

| Nível | ID | Estado alcançado |
|---|---|---|
| Campanha | `52512807800029` | **ATIVA** |
| Conjunto | `52512807805029` | **ATIVO** |
| Anúncio A-cara v3 | `52512816028029` | **ainda PAUSADO** |
| Anúncio B-provedor v3 | `52512816039629` | **ainda PAUSADO** |

O servidor de anúncios do Meta caiu no meio da sequência de ativação e voltou exigindo
autorização nova. Os dois anúncios ficaram sem ser ligados.

**Consequência: a campanha não está entregando e não está gastando.** Anúncio pausado
não roda, mesmo com campanha e conjunto ativos. O estado é seguro, mas não é o que foi
pedido.

**O que falta:** ligar os dois anúncios. São dois cliques no Gerenciador, ou eu termino
assim que a conexão com o Meta for reautorizada.

https://www.facebook.com/adsmanager/manage/ads?act=351203535&selected_adset_ids=52512807805029

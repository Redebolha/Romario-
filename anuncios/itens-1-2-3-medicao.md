# Itens 1, 2 e 3 — medição

## Item 1 — Conversões Personalizadas para QuizStart e QuizComplete

**Status: diagnóstico confirmado, execução depende de você.**

Consultei a conta: existem **zero** conversões personalizadas
(`ads_get_customconversions` → lista vazia). É exatamente o que explica os eventos
invisíveis.

Não consigo criar pela API — o servidor de anúncios expõe leitura de conversões
personalizadas, mas não criação. É tarefa de interface, e leva uns cinco minutos.

**Passo a passo, no Gerenciador de Eventos:**

1. Abra o Gerenciador de Eventos e selecione o dataset **HVNR Tracking**
   (`2570806596755923`).
2. Menu lateral → **Conversões personalizadas** → **Criar conversão personalizada**.
3. Primeira conversão:
   - Fonte de dados: HVNR Tracking
   - Evento de conversão: **QuizStart**
   - Nome: `Quiz — Iniciou`
   - Categoria: Outro
   - Sem regra de URL (deixe abranger todo o evento)
4. Repita para a segunda:
   - Evento de conversão: **QuizComplete**
   - Nome: `Quiz — Concluiu`
5. Opcional e recomendado, uma terceira:
   - Evento: **Lead**, com regra de URL contendo `teste-mascara-masculina`
   - Nome: `Quiz — Clicou no WhatsApp`
   - Isso separa o Lead do teste de qualquer outro Lead do site no futuro.

Se `QuizStart` ou `QuizComplete` não aparecerem na lista de eventos, é porque o Meta
só oferece eventos vistos nos últimos 28 dias e as campanhas estão paradas desde 21/08.
Nesse caso: abra a página do teste no celular, responda as seis perguntas, e os dois
eventos aparecem na lista em poucos minutos.

**O que isso destrava:** os degraus 2 e 3 da régua de medição, públicos de
retargeting de quem começou e não terminou, e a possibilidade futura de otimizar
para `QuizComplete` em vez de visualização de página.

---

## Item 2 — Por que os Leads não foram atribuídos

**Status: investigado. A resposta não é a que eu esperava, e é boa notícia.**

Fui olhar para onde os anúncios de agosto realmente apontavam. Os criativos daquelas
campanhas **não são anúncios de link** — são publicações impulsionadas
(`object_story_id`, sem `link_url` próprio). E os botões estavam desencontrados:

| Criativo | CTA configurado |
|---|---|
| Teste Grátis: Qual Máscara Você Usa? | `SEE_DETAILS` |
| Teste Grátis: Sua Máscara | `SEE_DETAILS` |
| Qual Máscara Você Usa? | `SEE_DETAILS` |
| Faça o Teste Agora | `SEE_DETAILS` |
| **Teste: Qual Máscara Você Usa Sem Perceber?** | **`CALL_NOW`** |
| HVNR — Máscara Masculina — Botão Teste | `LEARN_MORE` |

Aquele `CALL_NOW` num anúncio de teste explica as métricas estranhas de
`click_to_call_native_call_placed` que apareceram na campanha 52510017063829: o
sujeito tocava no botão e o celular tentava **ligar**, não abrir o teste.

### Conclusão

Os R$ 88 de agosto não foram um teste limpo deste funil. Foram publicações
impulsionadas, com CTAs misturados e pelo menos uma apontando para telefone. Os zero
Leads atribuídos dizem mais sobre aquela montagem do que sobre o pixel.

O pixel em si está correto: `Lead` é evento padrão, dispara no botão certo, e o
`target="_blank"` do link segura a página viva enquanto a requisição sai.

**Portanto: não há bug de pixel para caçar antes de rodar.** Os anúncios novos são
anúncios de link de verdade, com destino único, CTA coerente, domínio de conversão
declarado e UTM limpa. São o primeiro teste limpo que esse funil vai ter.

O que fazer: rodar e **olhar se o Lead atribuído aparece no Gerenciador nos primeiros
dias**. Se aparecer, o problema era a montagem antiga e está resolvido. Se não
aparecer, aí sim vale endurecer o evento (ver o patch B abaixo).

---

## Item 3 — O evento de compra

**Status: metade é possível, metade é impossível. E achei um buraco maior no caminho.**

### O buraco maior

O pixel está em **5 das 53 páginas** do site. E **não está na página do livro** —
`livros/homem-voce-nao-e-ridiculo.html`, que é exatamente para onde a IA do WhatsApp
manda todo mundo na hora da oferta.

Quer dizer: o Meta nunca vê ninguém chegar na página de preço. Sem visualização, sem
intenção de compra, e sem público de retargeting de quem viu o valor e não comprou —
que costuma ser o público mais barato que existe.

Isso é mais grave que o evento de compra em si, e é o patch A abaixo.

### A metade impossível

A página oferece dois caminhos:

| Produto | Onde vende | Rastreável pelo Meta? |
|---|---|---|
| E-book — R$ 9,90 | **Amazon** (`amazon.com.br/dp/B0H59NTYV9`) | **Não. Nunca.** |
| Livro físico — R$ 29,90 | **Hotmart** (`go.hotmart.com/R106833548K`) | Sim |

A Amazon não permite instalar pixel de terceiros nem envia postback de venda. Não
existe configuração, plugin ou gambiarra que resolva. **A venda do e-book nunca vai
ser atribuível a um anúncio.** O único lugar onde ela aparece é o painel da KDP, e a
única forma de cruzar é por data.

Isso tem uma consequência estratégica que vale registrar: o produto de entrada, o mais
barato, o que a IA oferece primeiro — é o único que você não consegue medir. Se a
conta do funil vai ser julgada por venda rastreada, ela só pode ser julgada pelo livro
físico.

### A metade possível — Hotmart

A Hotmart integra com o Meta nativamente:

1. Hotmart → **Ferramentas** → **Pixel de rastreamento** (ou Integrações → Meta Ads).
2. Adicionar pixel: `2570806596755923`.
3. Produto: Homem, Você Não É Ridículo (físico).
4. Marcar os eventos: **InitiateCheckout** no início do checkout e **Purchase** na
   compra aprovada.
5. Ativar o envio pela **API de Conversões** da Hotmart, se disponível no seu plano —
   é mais confiável que só pixel de navegador, e sobrevive a bloqueador de anúncio.
6. Testar com uma compra real de R$ 29,90 sua e conferir em Gerenciador de Eventos →
   Eventos de teste.

Depois disso o `Purchase` passa a existir, com valor, e aí o ROI vira número.

---

## Patch A — pixel e eventos na página do livro

Arquivo: `livros/homem-voce-nao-e-ridiculo.html` do repositório `Redebolha/redebolha`.

**A1.** Dentro do `<head>`, colar o mesmo bloco que já está na página do teste:

```html
<!-- Meta Pixel -->
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window, document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '2570806596755923');
fbq('track', 'PageView');
fbq('track', 'ViewContent', {
  content_name: 'Homem, Você Não É Ridículo',
  content_type: 'product',
  content_ids: ['hvnr'],
  currency: 'BRL',
  value: 29.90
});
</script>
```

**A2.** No script que já existe no rodapé (o do `clique_comprar_livro`), acrescentar o
disparo para o Meta ao lado do que já vai para o GA4. Substituir a linha do `gtag` por:

```js
    if (typeof gtag === 'function') { gtag('event', 'clique_comprar_livro', { canal: canal, livro: 'Homem, Voce Nao E Ridiculo', pagina: 'livro' }); }
    if (typeof fbq === 'function') {
      fbq('track', 'InitiateCheckout', {
        content_name: 'Homem, Você Não É Ridículo',
        content_ids: ['hvnr-' + canal],
        currency: 'BRL',
        value: canal === 'hotmart' ? 29.90 : 9.90
      });
    }
```

Assim o Meta passa a ver: chegou na oferta (`ViewContent`) → clicou pra comprar
(`InitiateCheckout`) → comprou (`Purchase`, só no caminho Hotmart).

---

## Patch B — endurecer o Lead do teste (só se o item 2 mostrar que precisa)

Arquivo: `teste-mascara-masculina/index.html`, linha 323.

O `Lead` hoje dispara sem identificador próprio. Dando um `eventID` a ele, o mesmo
evento pode ser reenviado depois pela API de Conversões sem contar duas vezes:

```js
  document.getElementById('maskWhatsappBtn').addEventListener('click', function(){
    var eid = 'lead-' + Date.now() + '-' + Math.random().toString(36).slice(2, 10);
    if (typeof gtag === 'function') {
      gtag('event', 'quiz_whatsapp_click', { quiz_name: 'mascara_masculina', event_id: eid });
    }
    if (typeof fbq === 'function') {
      fbq('track', 'Lead', {
        content_name: 'quiz_mascara_whatsapp_click',
        utm_source: ORIGEM.source,
        utm_campaign: ORIGEM.campaign
      }, { eventID: eid });
    }
  });
```

Só vale mexer nisso se, depois de rodar os anúncios novos, o Lead atribuído continuar
não aparecendo. Não é para fazer agora.

---

## Nota sobre a entrega dos patches

Esta sessão tem acesso **somente de leitura** ao `Redebolha/redebolha` — consegui
clonar e auditar, mas não posso abrir pull request lá. Os patches acima estão prontos
para colar. Se quiser que eu mesmo abra o PR, é só pedir que eu solicito acesso de
escrita ao repositório.

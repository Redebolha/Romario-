# Configurar o pixel no Hotmart — passo a passo

Escrito em 29/08/2026. **Isto é para você fazer**, não dá para eu fazer: o
`app.hotmart.com` é bloqueado pela rede da minha sessão e o painel exige o seu login.

**Tempo:** uns 15 minutos, para os quatro produtos.

---

## Antes de começar

| Dado | Valor |
|---|---|
| ID do pixel do Meta | `2570806596755923` |
| Nome do dataset | HVNR Tracking |
| Produtos a configurar | 4 (o físico e os três e-books) |

Conferido agora: o pixel tem **zero regras de conversão** cadastradas. Nada foi
configurado ainda, nem no Meta nem no Hotmart.

---

## O passo a passo

Para **cada um dos quatro produtos**, no painel do produtor:

1. **Produtos → selecione o produto → Ferramentas**
2. Procure **Pixel de rastreamento** (às vezes aparece como *Pixels* ou
   *Rastreamento*; a Hotmart muda o rótulo de tempos em tempos)
3. **Adicionar pixel** → plataforma **Facebook / Meta**
4. Cole o ID: `2570806596755923`
5. **Marque o evento de compra** (*Purchase* / *Compra*) — **este é o que importa**
6. **NÃO marque "Início de checkout" / InitiateCheckout** — explico abaixo
7. Salvar

Repita para os quatro:

- [ ] Homem, Você Não É Ridículo — **livro físico** (R$ 29,90)
- [ ] Homem, Você Não É Ridículo — **e-book** (R$ 9,90)
- [ ] Amanhã É Outro Agora — e-book (R$ 9,90)
- [ ] O Poder da Decisão — e-book (R$ 9,90)

---

## A armadilha: não marque InitiateCheckout no Hotmart

O site **já dispara** o `InitiateCheckout` no clique do botão — isso entrou no PR #19,
com o valor certo por produto.

Se o Hotmart disparar o mesmo evento quando a página de checkout carregar, o Meta passa
a contar **dois eventos por pessoa**. O número infla, e a otimização da campanha começa
a trabalhar em cima de um dado errado.

**Deixe cada evento com um dono só:**

| Evento | Quem dispara |
|---|---|
| `PageView` | o site |
| `InitiateCheckout` | **o site**, no clique do botão |
| `Purchase` | **o Hotmart**, na venda confirmada |

O `Purchase` só pode vir do Hotmart — a venda acontece no domínio deles, o site nunca
fica sabendo. É exatamente por isso que este passo é indispensável.

---

## Como conferir se funcionou

**Sem esperar uma venda real:**

1. Gerenciador de Eventos do Meta → dataset **HVNR Tracking** → **Testar eventos**
2. Cole a URL do checkout de um produto e abra
3. Deve aparecer `PageView` na lista

**Com a primeira venda de verdade:** o `Purchase` aparece no Gerenciador de Eventos em
alguns minutos, com o valor. Se aparecer com valor zerado, falta marcar o repasse de
valor na configuração do Hotmart.

**Um detalhe que não é defeito:** o `Purchase` vai aparecer vindo do domínio
`hotmart.com`, não do `redebolha.com.br`. É o esperado — a venda acontece lá. Não tente
"corrigir" isso verificando o domínio no Meta, porque o domínio não é seu.

---

## Depois que estiver funcionando

Aí sim vale mudar a campanha de **Tráfego** para **Vendas**, otimizando por
`Purchase`. Sem o evento configurado, essa mudança não tem como funcionar — o Meta não
teria nenhuma compra para aprender.

**Não faça essa troca antes de ver o primeiro `Purchase` chegar.** E não a faça
enquanto o teste do Lead não fechar.

---

## Se a Hotmart oferecer "Conversions API" ou "Integração com Meta"

Algumas contas têm uma integração mais nova, que manda o evento pelo servidor em vez do
navegador. **Se aparecer essa opção, prefira ela** — é mais confiável, porque não
depende do bloqueador de anúncio nem do navegador do comprador.

Nesse caso o Meta pede um token de acesso, gerado no próprio Gerenciador de Eventos, em
*Configurações → API de Conversões → Gerar token*.

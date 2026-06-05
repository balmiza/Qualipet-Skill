---
name: qualipet-instagram
description: Cria posts completos para o Instagram da Qualipet — legenda (copy) + arte/imagem juntas. Use SEMPRE que o usuário pedir um post, arte, criativo, story, carrossel, feed, divulgação, promoção, campanha ou conteúdo de redes sociais para a Qualipet (loja de produtos pet na Shopee), mesmo que não diga explicitamente "Instagram" ou "post". Também use para datas comemorativas pet, lançamentos de produtos e promoções. Gera a legenda pronta para copiar e a arte como arquivo HTML/PNG no formato pedido (feed 1080x1080, story 1080x1920 ou carrossel).
---

# Qualipet — Posts e Imagens para Instagram

Skill para produzir posts de Instagram da Qualipet: **legenda + arte visual**, prontos para publicar.

A Qualipet é uma **loja de produtos para cães e gatos na Shopee**. Todo conteúdo deve direcionar o público à loja da Shopee para comprar. Não há serviços veterinários, banho, tosa ou táxi dog — foco exclusivo em produtos.

## Passo 0 — Carregue o perfil de marca

```yaml
# === PERFIL DE MARCA QUALIPET ===
nome: "QualiPet"
arroba: "@qualipett"
segmento: "Loja de produtos para cães e gatos — vendas pela Shopee"
canal_de_venda: "Shopee (link na bio)"

cores:
  primaria: "#E07020"      # laranja dominante do logo
  secundaria: "#F5A623"    # laranja-dourado das ilustrações
  apoio: "#3D2B1F"         # marrom-escuro (texto e contraste)
  clara: "#FAF5EF"         # creme suave (fundo do logo)
  texto: "#3D2B1F"

fontes:
  titulo: "Nunito"         # arredondada e amigável, peso 700/800
  corpo: "Nunito"          # mesma família, peso 400/600

tom_de_voz:
  - "Próximo e afetivo (o pet é da família)"
  - "Empolgado com os produtos, como quem indica para um amigo"
  - "Direto: mostra o produto, fala o benefício, manda para a Shopee"
  - "Nunca técnico demais; o dono do pet entende facilmente"

logo: "references/logo.png"   # carrinho + dog + cat em laranja
# ============================================================
```

## Passo 1 — Entenda o pedido

Identifique rapidamente (pergunte só o que faltar, no máximo uma rodada):

1. **Produto** — qual produto ou categoria (ração, petisco, brinquedo, cama, coleira, higiene, etc.) e para qual espécie (cão, gato ou ambos).
2. **Objetivo** — lançamento, promoção/desconto, dica de uso, top produtos, data comemorativa, post institucional.
3. **Formato** — feed quadrado `1080x1080`, story `1080x1920` ou carrossel. Se não disser, use **feed 1080x1080**.
4. **Dado específico** — preço, desconto (%), frete grátis, prazo de promoção.

## Passo 2 — Escreva a legenda (copy)

Estrutura recomendada:

- **Gancho** (primeira linha) — emoji + frase curta que para o scroll.
- **Corpo** (2–4 linhas) — destaca o benefício do produto para o pet/tutor. Sem linguagem técnica desnecessária.
- **CTA único** — sempre direcionar para a Shopee: "Compre agora pelo link na bio 🛒", "Acesse nossa loja na Shopee 🔗", "Garanta o seu na Shopee — link na bio".
- **Hashtags** — 8 a 15, misturando amplas e de nicho:
  `#QualiPet #ProdutosPet #PetShopOnline #Shopee #ShopeeBrasil #CãesEGatos #PetLovers #AmorPet #Cachorro #Gato #PetShop #DicaPet #CompraOnline`
  Ajuste por espécie quando for produto específico.

Regras de copy:
- Emojis com moderação (2–6 por post): 🐶 🐱 🐾 🦴 🛒 ❤️ ✨ 🎁.
- Português do Brasil. Frases curtas e escaneáveis.
- **Nunca** mencionar serviços veterinários, banho, tosa ou táxi dog — esses serviços não existem na loja.
- Para promoção, sempre deixar claro: validade ou "enquanto durarem os estoques".
- Frete grátis é um argumento forte na Shopee — destaque quando for o caso.

Entregue a legenda em bloco de texto pronto para copiar.

## Passo 3 — Gere a arte

Leia `references/arte.md` para os specs detalhados e os templates de layout.
Resumo do fluxo:

1. Escolha o template adequado (`promo-produto`, `lancamento`, `top-produtos`, `data-comemorativa`, `institucional`) descritos em `references/arte.md`.
2. Construa a arte como **HTML/CSS** em um arquivo único, no tamanho exato do formato.
3. Aplique as cores e fontes do perfil de marca. Importe as fontes via Google Fonts.
4. Use o logo de `references/logo.png`.
5. **Renderize para PNG** com a dimensão exata (script em `scripts/render.py`).
6. Para carrossel, gere uma arte por slide (capa + conteúdo + CTA final).

Princípios visuais (ver detalhes no reference):
- Hierarquia clara: 1 título dominante, 1 informação de apoio, 1 CTA.
- Respiro: margem de segurança de ~80px nas bordas.
- Contraste alto entre texto e fundo (legibilidade no celular).
- No story, deixe o terço inferior livre para stickers/links e o topo livre da barra de perfil.
- A arte vende o produto; a legenda explica.

## Passo 4 — Entregue

- Mostre a legenda em texto.
- Salve a(s) arte(s) em `/mnt/user-data/outputs/` e apresente com `present_files`.
- Para carrossel, nomeie `qualipet_carrossel_01.png`, `_02.png`, etc.

## Arquivos da skill

- `references/arte.md` — specs de formato, paleta aplicada e templates de layout HTML.
- `scripts/render.py` — converte o HTML da arte em PNG na dimensão exata.
- `references/logo.png` — logo oficial da QualiPet.

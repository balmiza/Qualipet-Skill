# Arte — Specs e Templates

## Formatos (dimensões em px)

| Formato        | Tamanho     | Uso                                    |
|----------------|-------------|----------------------------------------|
| Feed quadrado  | 1080 x 1080 | Padrão. Promoções, lançamentos, dicas  |
| Feed retrato   | 1080 x 1350 | Mais alcance no feed; carrossel        |
| Story / Reels  | 1080 x 1920 | Stories, capas de reels                |

Margem de segurança: **80px** em todos os lados para texto/logo importantes.
No story, manter o topo (~250px) e o rodapé (~320px) livres de texto essencial.

## Como aplicar a marca

Importar fontes no `<head>`:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
```

Variáveis CSS:
```css
:root{
  --primaria:#E07020;      /* laranja dominante do logo */
  --secundaria:#F5A623;    /* laranja-dourado das ilustrações */
  --apoio:#3D2B1F;         /* marrom-escuro para texto e contraste */
  --clara:#FAF5EF;         /* creme suave, fundo do logo */
  --texto:#3D2B1F;
  --fonte-titulo:'Nunito',sans-serif;
  --fonte-corpo:'Nunito',sans-serif;
}
```

Regras visuais:
- Um título dominante (60–110px), um apoio (32–44px), um CTA (28–40px em pílula).
- Estilo flat e amigável — alinhado ao logo (carrinho + dog + cat em traço limpo).
- Fundo com profundidade: gradiente suave entre `--clara` e branco, ou laranja em baixa opacidade (10–15%). Formas orgânicas e pegadas 🐾 decorativas funcionam bem.
- Logo (`references/logo.png`) no topo ou rodapé, altura ~90–120px. Prefira fundo claro ou adicione retângulo creme de apoio.
- Foto do produto quando houver: destaque limpo, sem poluição — o produto é a estrela.
- Contraste mínimo AA: texto escuro (`--apoio`) sobre fundo creme, ou texto branco sobre laranja.
- CTA da Shopee sempre visível: pílula laranja com "Compre na Shopee 🛒" ou similar.

## Templates de layout

Cada template é um ponto de partida; adapte ao tema. Sempre saída HTML único.

### 1. `promo-produto` — Promoção / desconto

- Selo ou faixa diagonal com o **% de desconto** ou **preço** em destaque (cor primária/secundária).
- Nome do produto como título grande. Condição em letra menor (validade, frete grátis).
- Foto ou ilustração do produto à direita ou ao fundo com overlay leve.
- CTA pílula: "Compre na Shopee 🛒" / "Corre lá — link na bio".

### 2. `lancamento` — Novo produto

- Badge "NOVIDADE ✨" em pílula (cor primária).
- Nome do produto em título grande. 1–2 linhas com o principal benefício.
- Produto em destaque visual (foto ou ícone temático grande).
- CTA: "Confira na nossa loja Shopee".

### 3. `top-produtos` — Vitrine / destaques

- Cabeçalho "TOP PRODUTOS 🐾" ou "Mais Vendidos".
- Grade de 3–4 produtos com nome e preço. Fundo creme, muito respiro.
- Rodapé: "Veja todos na nossa loja — link na bio 🔗".
- Ideal para carrossel (um produto por slide).

### 4. `data-comemorativa` — Datas pet

- Visual mais festivo. Ex.: Dia do Cão, Dia do Gato, Black Friday Pet.
- Título grande com a data. Mensagem afetiva curta conectando ao produto.
- Destaque para produto(s) relacionado(s) à data.
- Logo + CTA para a Shopee.

### 5. `institucional` — Marca / valores

- Frase de marca forte. Tom acolhedor: "Tudo para o seu pet, entregue na sua porta."
- Logo em destaque. Fundo creme ou gradiente suave em laranja.
- Sem produto específico — reforça a identidade da loja.

## Carrossel (estrutura sugerida)

1. **Capa**: gancho + "arrasta pro lado →".
2–N. **Conteúdo**: um produto por slide (foto, nome, preço/destaque).
Último. **CTA**: "Veja tudo na nossa loja Shopee — link na bio 🛒" + logo.

## Checklist antes de exportar

- [ ] Texto principal dentro da margem de segurança.
- [ ] Cores e fontes batem com o perfil de marca.
- [ ] Logo presente e legível.
- [ ] CTA único direcionando para a Shopee.
- [ ] Dimensão exata do formato pedido.
- [ ] Nenhuma menção a serviços (vet, banho, táxi dog) — foco em produtos.

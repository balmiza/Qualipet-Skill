# Arte — Specs e Templates

## Formatos (dimensões em px)

| Formato        | Tamanho     | Uso                                   |
|----------------|-------------|---------------------------------------|
| Feed quadrado  | 1080 x 1080 | Padrão. Promoções, dicas, posts gerais|
| Feed retrato   | 1080 x 1350 | Mais alcance no feed; carrossel        |
| Story / Reels  | 1080 x 1920 | Stories, capas de reels                |

Margem de segurança: **80px** em todos os lados para texto/logo importantes.
No story, manter o topo (~250px) e o rodapé (~320px) livres de texto essencial.

## Como aplicar a marca

Importar fontes no `<head>`:
```html
<link rel=”preconnect” href=”https://fonts.googleapis.com”>
<link href=”https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap” rel=”stylesheet”>
```
(Use as fontes do perfil de marca; troque se o usuário fornecer outras.)

Variáveis CSS (puxe do perfil de marca; estes são os valores reais do logo):
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
- Estilo flat e amigável — alinhado ao logo (carrinho + dog + cat em traço limpo). Evitar estilos muito “corporativos” ou muito infantis.
- Fundo com profundidade: gradiente suave entre `--clara` e branco, ou laranja claro (opacidade 10–15%). Formas orgânicas e pegadas 🐾 decorativas em baixa opacidade funcionam bem.
- Logo (`references/logo.png`) no topo ou rodapé, tamanho discreto (altura ~90–120px). Fundo do logo é creme — prefira usá-lo sobre fundos claros ou com retângulo creme de apoio.
- Foto de pet quando houver: tratar com overlay/gradiente para o texto ficar legível.
- Contraste mínimo AA. Texto escuro (`--apoio`) sobre fundo creme, ou texto branco sobre laranja.

## Templates de layout

Cada template é um ponto de partida; adapte ao tema. Sempre saída HTML único.

### 1. `promo` — Promoção / desconto
- Faixa diagonal ou selo redondo com o **% / preço** em destaque (cor secundária).
- Título do produto/serviço grande. Condição em letra menor (validade).
- CTA pílula: “Garanta o seu” / “Corre pra loja”.
- Espaço para foto do produto à direita ou ao fundo com overlay.

### 2. `dica` — Dica de cuidado
- Cabeçalho “DICA QUALIPET 🐾” em pílula (cor primária).
- Título da dica em até 2 linhas. 1 ícone grande temático (🦷, 💧, 🐕).
- Fundo claro, muito respiro. Tom educativo.
- Rodapé: “Salve este post 📌”.

### 3. `data-comemorativa` — Datas pet
- Visual mais ilustrado/festivo. Ex.: Dia do Gato, Dia do Cão, Natal pet.
- Título grande com a data. Mensagem afetiva curta.
- Logo + assinatura. Cores podem puxar para o tema da data mantendo a paleta.

### 4. `servico` — Serviço (banho, vacina, táxi dog, consulta)
- Ícone/linha do serviço + nome do serviço como título.
- 3 bullets curtos de benefício (máx. 4 palavras cada).
- CTA: “Agende pelo WhatsApp”.

### 5. `institucional` — Bastidores / equipe / valores
- Foto da equipe/clínica com overlay e frase de marca.
- Tom acolhedor: “Cuidamos do seu pet como família”.
- Logo em destaque.

## Carrossel (estrutura sugerida)
1. **Capa**: gancho + “arrasta pro lado →”.
2–N. **Conteúdo**: um ponto por slide, número do slide visível.
Último. **CTA**: ação + contato + logo.

## Checklist antes de exportar
- [ ] Texto principal dentro da margem de segurança.
- [ ] Cores e fontes batem com o perfil de marca.
- [ ] Logo presente e legível.
- [ ] Apenas um CTA.
- [ ] Dimensão exata do formato pedido.

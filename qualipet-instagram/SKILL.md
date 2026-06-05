---
name: qualipet-instagram
description: Cria posts completos para o Instagram da Qualipet — legenda (copy) + arte/imagem juntas. Use SEMPRE que o usuário pedir um post, arte, criativo, story, carrossel, feed, divulgação, promoção, campanha ou conteúdo de redes sociais para a Qualipet (pet shop / veterinária), mesmo que não diga explicitamente "Instagram" ou "post". Também use para datas comemorativas pet, lançamentos, promoções e dicas de cuidado animal. Gera a legenda pronta para copiar e a arte como arquivo HTML/PNG no formato pedido (feed 1080x1080, story 1080x1920 ou carrossel).
---

# Qualipet — Posts e Imagens para Instagram

Skill para produzir posts de Instagram da Qualipet: **legenda + arte visual**, prontos para publicar.

## Passo 0 — Carregue o perfil de marca

Antes de criar qualquer coisa, leia o bloco abaixo. Ele define cores, fontes, tom e logo. **Se o usuário tiver fornecido um manual de marca próprio (cores/logo/fontes), use os dados dele e ignore os valores de exemplo.** Caso contrário, use este perfil padrão e avise discretamente que está usando o padrão (pode ser ajustado).

```yaml
# === PERFIL DE MARCA QUALIPET ===
nome: "QualiPet | Veterinária & PetShop"
arroba: "@qualipett"
segmento: "Clínica veterinária + pet shop + táxi dog"
localizacao: "Asa Norte, Brasília/DF"
contato: "(61) 3554-6000"

cores:
  primaria: "#E07020"      # laranja (cor dominante do logo e da marca)
  secundaria: "#F5A623"    # laranja-dourado (tom das ilustrações do logo)
  apoio: "#3D2B1F"         # marrom-escuro (texto e contraste)
  clara: "#FAF5EF"         # creme suave (fundo do logo)
  texto: "#3D2B1F"

fontes:
  titulo: "Nunito"         # arredondada e amigável, similar ao lettering do logo; peso 700/800
  corpo: "Nunito"          # mesma família para coesão; peso 400/600

tom_de_voz:
  - "Acolhedor e afetivo (o pet é da família)"
  - "Confiável e profissional (autoridade veterinária)"
  - "Próximo, sem ser infantil"
  - "Educa antes de vender"

logo: "references/logo.png"   # logo oficial com carrinho + dog + cat em laranja
# ============================================================
```

> Cores extraídas diretamente do logo oficial (`references/logo.png`): laranja dominante, fundo creme, estilo flat/amigável.

## Passo 1 — Entenda o pedido

Identifique rapidamente (pergunte só o que faltar, no máximo uma rodada):
1. **Tema** do post (promoção, dica, data comemorativa, serviço, lançamento, institucional).
2. **Formato**: feed quadrado `1080x1080`, story `1080x1920`, ou carrossel (N artes 1080x1350). Se o usuário não disser, use **feed 1080x1080**.
3. **Objetivo/CTA**: agendar, comprar, visitar loja, salvar a dica, comentar.
4. **Oferta/dado específico** se houver (desconto, %, produto, data).

## Passo 2 — Escreva a legenda (copy)

Estrutura recomendada:

- **Gancho** (primeira linha forte, para o feed) — emoji + frase curta.
- **Corpo** (2–4 linhas) — entrega valor: explica a dica, a oferta ou o serviço. Tom da marca.
- **CTA** claro — uma ação só.
- **Assinatura** leve da marca quando fizer sentido.
- **Hashtags** — 8 a 15, misturando amplas e locais. Base sugerida:
  `#Qualipet #PetShop #Veterinária #SaúdeAnimal #AmorPet #CãesEGatos #PetLovers #VetBrasília #AsaNorte #DF #CuidadoComOPet`
  Ajuste a cidade/bairro conforme o perfil de marca real.

Regras de copy:
- Emojis com moderação (2–6 por post), sempre pet-friendly: 🐶 🐱 🐾 🦴 ❤️ 💉 🩺 ✂️.
- Português do Brasil. Frases curtas. Evite jargão técnico sem explicar.
- Nunca prometa resultado médico garantido; recomende avaliação veterinária quando for saúde.
- Para promoção, deixe condições claras (validade, "enquanto durarem os estoques").

Entregue a legenda em bloco de texto pronto para copiar.

## Passo 3 — Gere a arte

Leia `references/arte.md` para os specs detalhados e os templates de layout.
Resumo do fluxo:

1. Escolha um dos templates (`promo`, `dica`, `data-comemorativa`, `servico`, `institucional`) descritos em `references/arte.md`.
2. Construa a arte como **HTML/CSS** em um arquivo único, no tamanho exato do formato.
3. Aplique as cores e fontes do perfil de marca. Importe as fontes via Google Fonts.
4. Use o logo de `assets/logo.png` se existir; senão, faça lettering com a fonte de título.
5. **Renderize para PNG** com a dimensão exata (script em `scripts/render.py`).
6. Para carrossel, gere uma arte por slide (capa + conteúdo + CTA final).

Princípios visuais (ver detalhes no reference):
- Hierarquia clara: 1 título dominante, 1 informação de apoio, 1 CTA.
- Respiro: margem de segurança de ~80px nas bordas (texto importante longe do corte).
- Contraste alto entre texto e fundo (legibilidade no celular).
- No story, deixe o terço inferior livre para stickers/links e o topo livre da barra de perfil.
- Evite poluição: a arte vende a ideia, a legenda explica.

## Passo 4 — Entregue

- Mostre a legenda em texto.
- Salve a(s) arte(s) em `/mnt/user-data/outputs/` e apresente com `present_files`.
- Para carrossel, nomeie `qualipet_carrossel_01.png`, `_02.png`, etc.

## Arquivos da skill

- `references/arte.md` — specs de formato, paleta aplicada e 5 templates de layout HTML.
- `scripts/render.py` — converte o HTML da arte em PNG na dimensão exata.
- `assets/` — coloque aqui o logo real e fontes/ícones da marca.

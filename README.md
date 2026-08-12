# Gerson Filmes — site oficial

Site em Flask com página de apresentação, formulário que abre o WhatsApp
já preenchido e área reservada onde cada cliente assiste e baixa o próprio filme.

---

## ⚠️ Antes de publicar

Abra o **`content.py`**. Tudo que precisa da sua conferência está marcado com
`# ⚠️ CONFIRA`:

1. **Preços de 15 anos e de eventos** — eu criei como ponto de partida
   (R$ 1.950 / 2.850 / 3.650 para 15 anos, R$ 1.200 para cobertura de evento).
   Ajuste para o que você realmente cobra.
2. **Preços e prazos de casamento** — confira se ainda valem.
3. **Dois depoimentos** — o da Fernanda e Tiago é seu; os outros dois são
   exemplos de formato. Troque pelos reais.
4. **Domínio** em `MARCA["site_url"]` — está vazio de propósito. Enquanto
   estiver assim, o site descobre sozinho o próprio endereço, então nada
   quebra. Quando comprar o domínio, cole ali e o Google passa a indexar por
   ele.

---

## Como o site está montado

| Endereço          | O que é                                            |
|-------------------|----------------------------------------------------|
| `/`               | Página principal, 12 seções                        |
| `/casamentos`     | Setor de casamentos                                |
| `/15-anos`        | Setor de 15 anos, em rosa                          |
| `/eventos`        | Setor de eventos                                   |
| `/orcamento`      | Formulário → abre o WhatsApp organizado            |
| `/obrigado`       | Confirmação e abertura da conversa                 |
| `/cliente`        | Login da área reservada                            |
| `/cliente/painel` | Filmes e downloads de cada cliente                 |
| `/robots.txt`     | Instruções para buscadores                         |
| `/sitemap.xml`    | Mapa do site                                       |

### Os três setores

As páginas de casamentos, 15 anos e eventos são irmãs: mesmo template
(`templates/setor.html`), conteúdo diferente. Tudo o que muda entre elas está
em `SETORES`, no `content.py` — título, textos, momentos, tema de cor e qual
vídeo roda atrás da abertura.

Para criar um quarto setor, copie um bloco de `SETORES`, dê um endereço novo e
acrescente esse endereço na lista da rota `setor` no `app.py`. Nenhuma linha de
HTML precisa ser escrita.

### Voz do site

Todo o texto fala em **nós**, nunca em primeira pessoa do singular. As únicas
frases no singular são as que o **cliente** diz — a mensagem do WhatsApp
("queria conversar sobre a minha data"), o botão que ele clica e os depoimentos.
Se for escrever algo novo, mantenha esse corte.

**15 anos escreve-se sempre com o numeral** — nunca "quinze anos".

**A marca escreve-se "Gerson Filmess"**, com dois SS, igual ao Instagram e ao
e-mail.

### As 12 seções da página principal

1. **Abertura** — vídeo e a frase principal
2. **Ficha** — base, atendimento, equipamento, entrega
3. **O olhar** — por que um filme existe
4. **Um filme** — o teaser tocando na página
5. **O que eu filmo** — casamentos, 15 anos, eventos
6. **Como eu trabalho** — seis decisões técnicas
7. **O caminho** — as quatro etapas
8. **Coleções** — abas de casamento, 15 anos e eventos
9. **O que fica combinado** — o que está no contrato
10. **Quem já assistiu** — depoimentos
11. **Dúvidas** — oito perguntas
12. **Convite** — o fechamento

---

## Onde mudar cada coisa

| Quero mudar…                      | Arquivo             |
|-----------------------------------|---------------------|
| Qualquer texto, preço ou pergunta | `content.py`        |
| Cores                             | `static/style.css`, no topo (`:root`) |
| Vídeo de abertura ou teaser       | `static/`           |
| Como o site funciona              | `app.py`            |

### A paleta

Definida no começo do `style.css`. Saiu do preto-e-dourado — que é o clichê de
convite de casamento — para uma combinação mais quieta:

```text
--tinta      #15110E   preto quente, quase marrom
--osso       #F1ECE3   papel

--argila     #A85E45   terracota  -> casamentos e a marca
--rosa       #C97B8E   rosa       -> 15 anos
--salvia     #79856F   verde      -> eventos
```

**Cada setor tem a sua cor.** Quem manda é a chave `tema` em `SETORES`:
vazio para terracota, `tema-rosa` ou `tema-salvia`. Essa classe troca as
variáveis de acento do bloco inteiro, então nenhuma regra precisa ser
duplicada — vale na página do setor, no item do menu e no cartão da home.

**O rosa dos 15 anos** funciona por uma classe, `tema-rosa`. Quem recebe essa
classe troca o acento inteiro para rosa sem precisar de nenhuma regra nova.
Ela vai em quatro lugares: a página `/15-anos`, o item do menu, o cartão de
15 anos na home e — quando você clica na aba "15 anos" — a **seção de Orçamento
inteira** da home. Sai da aba, volta ao terracota.

Na página `/15-anos` o rosa vai além do acento: a seção dos momentos vira
**papel rosado** (`--rosa-papel`) e os títulos ficam em itálico. É isso que faz
a página parecer outra coisa, e não a de casamentos repintada.

Quem manda nisso é o atributo `data-tema` no botão da aba, no `index.html`.
Se um dia quiser um acento próprio para eventos, basta criar outra classe no
mesmo molde e apontar o `data-tema` do botão para ela.

**Cada coleção de 15 anos tem o seu rosa**, aprofundando conforme o pacote:

```text
01 Essencial  #EBB9C0   blush
02 Completo   #DB93A6   rosa
03 Autoral    #C489AE   malva
```

O tom pinta o preço, o número, os traços da lista e a seta do cartão — tudo
junto, porque o cartão só redefine as variáveis de acento. Estão em
`.tema-rosa .pacote:nth-child(n)` no `style.css`.

Existem variações de cada um (`--argila-txt`, `--cinza-d`) porque a mesma cor
não serve para texto pequeno em fundo claro e em fundo escuro. Todos os textos
do site foram medidos e passam no contraste mínimo de acessibilidade — se você
trocar uma cor, vale conferir de novo.

---

## Rodar no seu computador

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

Abra `http://127.0.0.1:5000`.

---

## ⚠️ Cópias antigas deste site no Desktop

```text
Meu SIte\JULHO 2026\1\gerson_filmes_v4          ← ESTA. É a atual.
Meu SIte\JULHO 2026\1\gerson_filmes_v3             backup: paleta terracota, sem página de 15 anos
Meu SIte\JULHO 2026\1\gerson_filmes_minimalista    backup antigo
Meu SIte\JULHO 2026\2\gerson_filmes_minimalista    tinha o teaser — já trazido
Meu SIte\gerson_filmes_minimalista                 antiga
Meu SIte\CLAUDE\site_casamentos                    março/2026
Meu SIte\ChatGPT\site_casamentos                   julho/2026
Meu SIte\site_casamentos                           fevereiro/2026
```

Cada versão nova nasce numa pasta nova e a anterior fica intacta como backup.
Rodar a pasta errada é o que faz "abrir o site antigo" — confira sempre o nome
antes de dar `python app.py`.

---

## Ver os orçamentos recebidos

Cada pedido é gravado no banco e em `leads/orcamentos.txt`.

```bash
python admin_seed.py ver-pedidos
```

## Criar o acesso de um cliente

```bash
python admin_seed.py criar-cliente --nome "Ana e Lucas" --email "casal@email.com" --senha "uma-senha-forte"
```

Enviar o filme:

```bash
python admin_seed.py adicionar-arquivo --email "casal@email.com" --titulo "Filme principal" --arquivo "C:\caminho\filme.mp4" --tipo video
```

Para fotos, ZIP ou outro arquivo, troque `--tipo video` por `--tipo file`.

### Filmes grandes: use o Google Drive

Um filme de casamento passa fácil de 10 GB. Hospedar isso no servidor sai caro
e a entrega fica lenta. Para esses casos, **registre só o link** — o arquivo
mora no seu Drive e a página continua sendo a sua:

```bash
python admin_seed.py adicionar-link --email "casal@email.com" --titulo "Filme completo" --url "https://drive.google.com/file/d/SEU_ID/view"
```

O cliente entra com login, vê o filme listado na área dele e clica em
"Abrir o filme". Funciona igual com Vimeo ou YouTube não listado.

Os dois modos convivem: um filme grande por link e as fotos por arquivo local,
no mesmo painel.

⚠️ **O que o link protege e o que não protege.** A área do cliente continua
exigindo senha para *ver a lista*. Mas um link do Drive marcado como "qualquer
pessoa com o link" abre para quem tiver o endereço, mesmo sem login. Se isso
for um problema para algum cliente, no Drive escolha "restrito" e adicione o
e-mail dele — ou entregue esse filme como arquivo local, que aí só sai daqui
depois do login.

---

## Trocar os vídeos

| Onde aparece | Arquivos | Texto em `content.py` |
|---|---|---|
| Fundo da abertura | `video-bg.mp4` | — |
| Teaser da home | `teaser-filipe-ana.mp4` + `teaser-poster.jpg` | seção 3, `FILME_DESTAQUE` |
| Teaser de 15 anos | `teaser-15-anos.mp4` + `teaser-15-anos-poster.jpg` | seção 7b, dentro de `PAGINA_15` |

Mantenha os mesmos nomes de arquivo e formato horizontal. Para esconder
qualquer um dos dois teasers, troque `"ativo": True` por `"ativo": False`.

**A capa (`-poster.jpg`)** é o que o visitante vê antes de dar play — vale
escolher um quadro bom. Para tirar um quadro do próprio vídeo:

```bash
ffmpeg -ss 21 -i filme.mp4 -frames:v 1 -vf "scale=1600:-2" -q:v 5 capa.jpg
```

### Publicar um filme novo num setor

Cada setor tem uma **lista** de filmes em `SETORES[...]["filmes"]`. Com um só,
ele toca grande sozinho. Com dois ou mais, aparecem capas embaixo e clicar
numa delas troca o filme do player, sem recarregar a página.

Os próximos já estão escritos lá, com `"ativo": False`, esperando arquivo:

```text
casamentos   Raphaella & Kauan · Thamires & Neilon · Anna & Marcos
15 anos      Ana Luíza · Lavínia
```

Para publicar um deles, três passos:

1. Comprima o vídeo e tire a capa (comandos abaixo), com **os nomes de arquivo
   que já estão escritos no bloco** — por exemplo `teaser-raphaella-kauan.mp4`
   e `teaser-raphaella-kauan-capa.jpg`.
2. Ponha os dois em `static/`.
3. Troque `"ativo": False` por `"ativo": True` e salve.

Tirar a capa de um quadro do próprio filme:

```bash
ffmpeg -ss 21 -i filme.mp4 -frames:v 1 -vf "scale=1600:-2" -q:v 5 capa.jpg
```

### Comprima antes de publicar

Os originais estão em `_originais/` (essa pasta não sobe para o servidor).

```bash
ffmpeg -i entrada.mp4 -an -vf "scale=1280:-2" -c:v libx264 -crf 30 -preset slow -movflags +faststart video-bg.mp4
```

O vídeo de fundo caiu de 15 MB para 3,9 MB e o teaser de 12 MB para 9,5 MB, sem
diferença visível. A abertura da página baixou de 15,9 MB para 3,9 MB — o teaser
só é baixado quando alguém aperta o play.

---

## Publicar no Render

O `render.yaml` já traz tudo. No painel, cadastre `SECRET_KEY`,
`WHATSAPP_NUMBER` (5531998851328) e `HTTPS_ONLY` (1).

**Atenção:** o banco (`private/clients.db`) e a pasta `uploads/` precisam de
disco persistente. Sem isso, cada publicação apaga os acessos dos clientes e
os filmes enviados.

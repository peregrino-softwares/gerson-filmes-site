# Gerson Filmes — site oficial

O conteúdo é editado em Flask — mexendo em `content.py` — mas o que fica no
ar é uma **versão estática**, gerada por `build_static.py` e publicada de
graça e sempre ligada no GitHub Pages. Formulário que abre o WhatsApp já
preenchido, sem precisar de servidor nenhum rodando por trás.

> **A área do cliente está desligada.** O site publicado é só arquivos
> parados — não existe um servidor por trás para conferir senha. Ela volta
> se um dia o site precisar rodar num servidor de verdade; veja *Religar a
> área do cliente*, no fim.

---

## ⚠️ Antes de publicar

Abra o **`content.py`**. Tudo que precisa da sua conferência está marcado com
`# ⚠️ CONFIRA`:

1. **Itens e prazos de cada coleção** — confira se ainda valem. O site não
   publica valor nenhum: o cartão vai direto da descrição para os itens, e o
   orçamento vai pelo WhatsApp, conforme a data, o local e a duração do
   evento.
2. **Dois depoimentos** — o da Fernanda e Tiago é seu; os outros dois são
   exemplos de formato. Troque pelos reais.
3. **Domínio** — pronto e no ar em `https://www.gersonfilmes.com.br`.
   Nada a fazer; os detalhes ficam em *O domínio*, no fim.

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
| `/cliente`        | Login da área reservada — *desligada por enquanto* |
| `/cliente/painel` | Filmes e downloads de cada cliente — *desligada*   |
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
| Qualquer texto, item ou pergunta  | `content.py`        |
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

O tom pinta o número, os traços da lista e a seta do cartão — tudo junto,
porque o cartão só redefine as variáveis de acento. Estão em
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

Abra `http://127.0.0.1:5000`. Esse é o **modo de edição** — mexe em
`content.py`, atualiza a página e confere na hora. É diferente do site
publicado, que é a versão estática (veja abaixo); serve para conferir antes
de gerar essa versão.

---

## ⚠️ Cópias antigas deste site no Desktop

```text
Meu SIte\JULHO 2026\1\gerson_filmes_v21         ← ESTA. É a atual.
Meu SIte\JULHO 2026\1\gerson_filmes_v20            backup: o domínio entrou aqui
Meu SIte\JULHO 2026\1\gerson_filmes_v3 … v19       backups, do mais antigo ao mais novo
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

No site publicado (estático), cada pedido chega **só pelo WhatsApp** — é lá
que fica o registro. `admin_seed.py ver-pedidos` só mostra algo se alguém
enviou o formulário rodando `python app.py` localmente; no ar, essa cópia
não existe, porque não há servidor por trás para gravá-la.

```bash
python admin_seed.py ver-pedidos
```

## Criar o acesso de um cliente

⚠️ **Isto só funciona rodando `python app.py`.** A área do cliente está
desligada no site publicado; veja a nota no topo deste arquivo.

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

## Publicar no GitHub Pages

O site vive em `peregrino-softwares/gerson-filmes-site` (público — precisa
ser público para o GitHub Pages ser gratuito). O que fica no ar é a pasta
`docs/`, então publicar tem um passo a mais que um `git push` comum:

```bash
python build_static.py
```

Isso apaga a `docs/` antiga e gera de novo, com os textos de agora.
Depois:

```bash
git add -A
```

```bash
git commit -m "o que mudou"
```

```bash
git push
```

Alguns segundos depois de o push chegar, o GitHub Pages já está servindo a
versão nova. **Sempre no ar, de graça** — sem o site dormir depois de um
tempo sem visita, que é o que aconteceria num plano gratuito de servidor
como o Render.

### O que se perde por não ter servidor

O formulário de orçamento continua funcionando normalmente — ele monta a
mensagem e abre o WhatsApp direto no navegador da pessoa, sem passar por
lugar nenhum. O que não existe mais é uma **cópia salva à parte** dos
pedidos (antes ficava em `leads/orcamentos.txt` e num banco); agora o único
registro é a própria conversa no seu WhatsApp. E a área do cliente — login,
filmes, downloads — fica desligada, porque logins e senhas precisam de
código rodando por trás para conferir, e um site estático não tem isso.

### Religar a área do cliente (exige voltar a um servidor)

Não dá para ter login com o site 100% estático — nesse caso, a saída é
hospedar de novo num serviço que rode Python, como o Render (o `render.yaml`
já está pronto no repositório, sem uso agora, esperando por isso). Os passos
ficam guardados na memória deste projeto; a ideia geral:

1. Publicar em algo que rode o Flask (ex.: Render, plano Starter — o
   gratuito não tem disco e apagaria os acessos a cada reinício).
2. Em `content.py`, trocar `AREA_CLIENTE = False` por `True`.
3. Fazer o banco e os uploads morarem num disco que sobrevive à publicação.

### O domínio

**Está no ar em https://www.gersonfilmes.com.br** desde 12/08/2026. Quem
digita `gersonfilmes.com.br` sem o `www` é levado para lá sozinho, e os dois
endereços têm cadeado (certificado emitido pelo GitHub, renovado sozinho).

O que está configurado, caso um dia precise conferir ou refazer:

| Onde | O quê |
|---|---|
| Registro.br, zona DNS | 4 registros `A` no domínio (vazio no campo Nome) para `185.199.108.153`, `.109`, `.110` e `.111` |
| Registro.br, zona DNS | 1 `CNAME` de nome `www` para `peregrino-softwares.github.io` |
| `content.py` | `MARCA["site_url"]` — é dele que saem o `docs/CNAME`, o sitemap e os links de compartilhamento |
| GitHub, Settings → Pages | domínio `www.gersonfilmes.com.br`, com *Enforce HTTPS* ligado |

⚠️ **Se um dia esvaziar o `site_url`**, o `build_static.py` volta a gerar o
site para o endereço `peregrino-softwares.github.io/gerson-filmes-site/`, com
todos os links dentro dessa subpasta — e some o `docs/CNAME`. É proposital:
serve para publicar sem domínio. Mas aí o domínio precisa ser retirado
também em Settings → Pages, senão o GitHub redireciona para um endereço que
o site não atende mais.

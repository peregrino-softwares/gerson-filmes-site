# -*- coding: utf-8 -*-
"""
=====================================================================
 GERSON FILMES — CENTRAL DE CONTEÚDO
=====================================================================
 Este é o único arquivo que você precisa abrir para mudar textos,
 preços e perguntas. Troque o que está entre aspas e salve.
 Não apague vírgulas, colchetes nem chaves.

 Tudo marcado com  # ⚠️ CONFIRA  precisa da sua revisão antes de publicar.
=====================================================================
"""

# ---------------------------------------------------------------
# 1. IDENTIDADE E CONTATO
# ---------------------------------------------------------------
MARCA = {
    "nome": "Gerson Filmes",
    "assinatura": "Cinematografia",
    "frase_principal": "A vida passa, o filme eterniza.",
    "frase_apoio": "Cinematografia que emociona.",
    "whatsapp": "5531998851328",
    "instagram": "https://instagram.com/gersonfilmess",
    "instagram_arroba": "@gersonfilmess",
    "cidade_base": "Sete Lagoas",
    "regiao": "Minas Gerais",
    "atendimento": "Sete Lagoas e região, Belo Horizonte e todo o Brasil",
    "email": "gersonfilmess@gmail.com",
    "site_url": "https://www.gersonfilmes.com.br",
}

WHATSAPP_MENSAGEM = "Olá, Gerson. Vi seu site e queria conversar sobre uma data."

# A área do cliente (login, filmes e downloads) fica desligada porque o site
# publicado hoje é estático, no GitHub Pages — não existe servidor rodando
# para conferir senha nem para guardar quem tem acesso a quê.
#
# Trocar para True só faz sentido se um dia o site voltar a rodar num
# servidor de verdade (como o Render, com disco). Nesse caso, a chave liga
# sozinha: o link no menu, o link no rodapé, o convite da página de obrigado
# e as páginas /cliente. Nenhuma outra linha precisa mudar.
AREA_CLIENTE = False

# Mensagem montada quando alguém envia o formulário. O que está entre
# chaves é preenchido sozinho — não mude os nomes dentro das chaves.
WHATSAPP_FORMULARIO = """Olá, Gerson. Vim pelo site e queria conversar sobre a minha data.

Nome: {nome}
WhatsApp: {whatsapp}
Evento: {tipo}
Data: {data}
Cidade ou local: {local}
Orçamento: {pacote}
O que não pode faltar: {mensagem}"""


# ---------------------------------------------------------------
# 2. FICHA — a faixa discreta abaixo da abertura
#    Fatos verificáveis, sem número inflado. Se um dia quiser mostrar
#    quantos eventos já filmou, use o número real.
# ---------------------------------------------------------------
FICHA = [
    {"rotulo": "Atendimento",  "valor": "Sete Lagoas e região, BH e todo o Brasil"},
    {"rotulo": "Equipamentos", "valor": "Sony Cinema, drones DJI e Zoom 32 bit float"},
    {"rotulo": "Equipe",       "valor": "Especializada em eventos de grande porte"},
    {"rotulo": "Entrega",      "valor": "Prazo definido em contrato"},
]


# ---------------------------------------------------------------
# 4. O QUE EU FILMO
# ---------------------------------------------------------------
ESPECIALIDADES = [
    {
        "indice": "01",
        "titulo": "Casamentos",
        "chamada": "Quem casa não assiste ao próprio casamento.",
        "texto": "O dia passa por dentro, em blocos, entre um abraço e outro. O filme "
                 "devolve a ordem das coisas — inclusive as horas em que vocês estavam "
                 "ocupados demais para reparar no que acontecia em volta.",
        "pacote": "Casamento",
        "tema": "",
    },
    {
        "indice": "02",
        "titulo": "15 anos",
        "chamada": "O ano em que ela escolhe quem quer ser.",
        "texto": "São meses de preparação para quatro horas de festa, com ela no centro de "
                 "tudo. Filmamos as duas: a menina que ensaiou a valsa por semanas e a que "
                 "tirou o salto na terceira música.",
        "pacote": "15 anos",
        "tema": "tema-rosa",
    },
    {
        "indice": "03",
        "titulo": "Eventos",
        "chamada": "Formatura, confraternização, lançamento.",
        "texto": "Vídeo de evento costuma ser gravado sem que ninguém tenha decidido para "
                 "que ele serve. Perguntamos isso antes: registro para a família, peça para "
                 "as redes ou material institucional pedem cortes diferentes — e dias de "
                 "gravação diferentes.",
        "pacote": "Evento",
        "tema": "tema-salvia",
    },
]


# ---------------------------------------------------------------
# 5. COMO EU TRABALHO
# ---------------------------------------------------------------
METODO = [
    {
        "rotulo": "Roteiro",
        "titulo": "O roteiro é a alma do trabalho",
        "texto": "Antes de ligar a câmera já sabemos que história vamos contar e em que "
                 "ordem. É o que separa um filme de um apanhado de cenas bonitas.",
    },
    {
        "rotulo": "Som",
        "titulo": "O áudio vem junto com a imagem",
        "texto": "Microfone nos votos, nos discursos, na homenagem. Quando a voz se perde, "
                 "a cena perde com ela.",
    },
    {
        "rotulo": "Ar",
        "titulo": "O drone é nosso",
        "texto": "As imagens aéreas são feitas pela mesma equipe que filma no chão, então o "
                 "olhar de cima nasce conversando com o de baixo.",
    },
    {
        "rotulo": "Presença",
        "titulo": "Discreto por escolha",
        "texto": "Ninguém precisa posar nem repetir. Circulamos por perto e esperamos o que "
                 "acontece sozinho.",
    },
    {
        "rotulo": "Montagem",
        "titulo": "Cada filme no seu ritmo",
        "texto": "A música, o corte e a duração nascem da história. Nenhum filme sai no "
                 "molde do anterior.",
    },
    {
        "rotulo": "Cuidado",
        "titulo": "Duas cópias no mesmo dia",
        "texto": "Todo o material gravado é copiado em duas mídias antes de encerrarmos o dia.",
    },
    {
        "rotulo": "Depois",
        "titulo": "O filme continua com você",
        "texto": "Ele fica guardado num espaço reservado para vocês aqui no site. "
                 "É só entrar e rever quando der vontade — hoje ou daqui a dez anos.",
    },
]


# ---------------------------------------------------------------
# 6. O CAMINHO — as quatro etapas
# ---------------------------------------------------------------
PROCESSO = [
    {
        "indice": "01",
        "titulo": "Conversa",
        "texto": "Antes de qualquer proposta, queremos ouvir. Como vocês se conheceram, "
                 "quem não pode faltar no filme, o que vocês gostariam de rever daqui a "
                 "vinte anos.",
    },
    {
        "indice": "02",
        "titulo": "Reserva",
        "texto": "Contrato assinado e a data fica guardada. O parcelamento a gente combina "
                 "junto, no que couber no seu planejamento.",
    },
    {
        "indice": "03",
        "titulo": "O dia",
        "texto": "Chegamos cedo, alinhamos o horário com o cerimonial e saímos do caminho. Câmera, "
                 "drone e microfones já ligados enquanto vocês vivem o dia.",
    },
    {
        "indice": "04",
        "titulo": "Entrega",
        "texto": "O filme chega por um link privado, só de vocês. Você assiste, baixa e "
                 "guarda a cópia onde quiser.",
    },
]


# ---------------------------------------------------------------
# 7. COLEÇÕES
#    ⚠️ CONFIRA: valores, itens e prazos.
#    Os preços de 15 anos e de eventos foram criados como ponto de
#    partida — ajuste para o que você realmente cobra.
# ---------------------------------------------------------------
COLECOES = {
    "Casamento": {
        "titulo": "Casamentos",
        "nota": "Valores de referência para Sete Lagoas, Belo Horizonte e região. O que "
                "muda de uma opção para outra são as horas de cobertura, quantas câmeras "
                "registram o dia e até onde o drone alcança. Viagem e duração real do "
                "evento ajustam o valor final.",

        # Aparece logo abaixo dos três cartões.
        "flexibilidade": "Cada casamento tem o seu desenho. Se algum item não fizer sentido "
                         "para vocês, ele pode ser trocado por outro de valor equivalente — "
                         "e o valor da opção permanece o mesmo. Ajustes e acréscimos são "
                         "conversados pelo WhatsApp e registrados em contrato, para que "
                         "nada dependa de memória.",

        "pacotes": [
            {
                "indice": "01",
                "nome": "Essencial",
                "selo": "",
                "descricao": "A essência do dia preservada em um filme sensível, preciso "
                             "e feito para permanecer.",
                "preco": "R$ 2.750",
                "botao": "Quero conhecer o Essencial",
                "itens": [
                    {"rotulo": "Horas de cobertura", "valor": "4 horas"},
                    {"rotulo": "2 câmeras",          "valor": "Cerimônia e recepção"},
                    {"rotulo": "Áudio profissional", "valor": "Votos, discursos e homenagens"},
                    {"rotulo": "Filme principal",    "valor": "15 a 20 minutos"},
                    {"rotulo": "Trilha sonora",      "valor": "Escolhida para conduzir a narrativa"},
                    {"rotulo": "Entrega",            "valor": "Em até 60 dias"},
                ],
                "destaque": False,
            },
            {
                "indice": "02",
                "nome": "Legado",
                "selo": "Mais escolhido",
                "descricao": "Mais tempo, mais perspectivas e mais espaço para transformar "
                             "o dia inteiro em memória.",
                "preco": "R$ 3.850",
                "botao": "Quero conhecer o Legado",
                "itens": [
                    {"rotulo": "Pré-wedding ou making of",
                     "valor": "Um ensaio dedicado ao casal ou o registro das horas lindas "
                              "que antecedem o grande sim"},
                    {"rotulo": "3 câmeras em ação",   "valor": "Cerimônia, recepção, festa e ornamentação"},
                    {"rotulo": "Áudio profissional",  "valor": "Votos, discursos e homenagens"},
                    {"rotulo": "Filme principal",     "valor": "30 a 40 minutos"},
                    {"rotulo": "Horas de cobertura",  "valor": "6 horas"},
                    {"rotulo": "2 teasers cinematográficos", "valor": "Filmes curtos e artísticos"},
                    {"rotulo": "Trilha sonora",       "valor": "Escolhida para conduzir a narrativa"},
                    {"rotulo": "Entrega prioritária", "valor": "Em até 45 dias"},
                ],
                "destaque": True,
            },
            {
                "indice": "03",
                "nome": "Cinema",
                "selo": "",
                "descricao": "Para reviver a cerimônia por inteiro — sem cortes, por todos "
                             "os ângulos e com a dimensão que somente o olhar do alto "
                             "consegue revelar.",
                "preco": "R$ 5.350",
                "botao": "Quero conhecer o Cinema",
                "itens": [
                    {"rotulo": "Pré-wedding", "valor": "Um ensaio lindo dedicado ao casal"},
                    {"rotulo": "Making of noiva e noivo",
                     "valor": "A preparação da noiva e a do noivo, registradas ao mesmo "
                              "tempo, em pontos diferentes"},
                    {"rotulo": "Drone durante a cerimônia",
                     "valor": "Sobrevoos em todas as entradas e saídas, revelando a "
                              "grandiosidade do evento de uma perspectiva que só um drone "
                              "é capaz de entregar"},
                    {"rotulo": "Horas de cobertura", "valor": "Sem limite de horas"},
                    {"rotulo": "5 câmeras em ação",
                     "valor": "Múltiplos ângulos do casal, familiares, convidados e de tudo "
                              "o que acontece ao redor"},
                    {"rotulo": "Cobertura completa", "valor": "Cerimônia, recepção e festa"},
                    {"rotulo": "Áudio profissional", "valor": "Votos, discursos e homenagens"},
                    {"rotulo": "Cerimônia na íntegra",
                     "valor": "De 1h a 1h30 de filme, sem cortes de conteúdo — preservando "
                              "entradas, votos, falas, reações e cada etapa da cerimônia"},
                    {"rotulo": "3 teasers cinematográficos", "valor": "Filmes curtos e artísticos"},
                    {"rotulo": "Entrega Premium",
                     "valor": "Prioridade máxima, com entrega em até 25 dias"},
                ],
                "destaque": False,
            },
        ],
    },
    "15 anos": {
        "titulo": "15 anos",
        "nota": "Valores de referência para Sete Lagoas, Belo Horizonte e região. "
                "Ensaio em outra cidade e festas acima de quatro horas ajustam o valor.",
        "pacotes": [
            {
                "indice": "01",
                "nome": "Essencial",
                "ideal": "A festa registrada com calma",
                "preco": "R$ 1.950",
                "itens": [
                    "Entrada, valsa e melhores momentos da festa",
                    "Discursos e homenagens com microfone",
                    "Filme de 5 a 8 minutos, com trilha licenciada",
                    "Entrega em até 60 dias",
                ],
                "destaque": False,
            },
            {
                "indice": "02",
                "nome": "Completo",
                "ideal": "Do ensaio até o fim da pista",
                "preco": "R$ 2.850",
                "itens": [
                    "Ensaio filmado em locação escolhida por você",
                    "Preparação, entrada, valsa e festa",
                    "Filme de 10 a 15 minutos e um vídeo curto para redes",
                    "Dois pontos de câmera e áudio profissional",
                    "Entrega em até 60 dias",
                ],
                "destaque": True,
            },
            {
                "indice": "03",
                "nome": "Autoral",
                "ideal": "Ensaio, festa e material para as redes",
                "preco": "R$ 3.650",
                "itens": [
                    "Ensaio em duas locações, com troca de look",
                    "Preparação, entrada, valsa e festa sem limite de horas",
                    "Imagens de drone e vídeo vertical para redes",
                    "Valsa e homenagens na íntegra",
                    "Entrega em até 45 dias",
                ],
                "destaque": False,
            },
        ],
    },
    "Evento": {
        "titulo": "Eventos",
        "nota": "Formaturas, aniversários, confraternizações, eventos corporativos e "
                "conteúdo em vídeo para redes. Cada projeto tem duração e entrega "
                "diferentes, então o orçamento é montado caso a caso.",
        "pacotes": [
            {
                "indice": "01",
                "nome": "Cobertura",
                "ideal": "Até quatro horas, um ponto de câmera",
                "preco": "R$ 1.200",
                "itens": [
                    "Registro dos momentos principais",
                    "Áudio de discursos e apresentações",
                    "Filme de 3 a 5 minutos",
                    "Entrega em até 30 dias",
                ],
                "destaque": False,
            },
            {
                "indice": "02",
                "nome": "Institucional",
                "ideal": "Empresas, marcas e formaturas",
                "preco": "Sob medida",
                "itens": [
                    "Roteiro conversado antes da gravação",
                    "Entrevistas, depoimentos e imagens de apoio",
                    "Versões para site, YouTube e formato vertical",
                    "Prazo combinado conforme o projeto",
                ],
                "destaque": False,
            },
        ],
    },
}

ORDEM_COLECOES = ["Casamento", "15 anos", "Evento"]


# ---------------------------------------------------------------
# 7b. SETORES — as tres páginas próprias do site
#     /casamentos   /15-anos   /eventos
#
#     Cada setor puxa as coleções da seção 7 pela chave "tipo".
#     "tema" pinta a página: deixe vazio para o terracota da marca,
#     ou "tema-rosa" para o rosa dos 15 anos.
#     "video_fundo" e o vídeo que roda sozinho atrás da abertura;
#     deixe None para uma abertura só de tipografia.
# ---------------------------------------------------------------
SETORES = {

    # ------------------------------------------------- CASAMENTOS
    "casamentos": {
        "nome": "Casamentos",
        "tipo": "Casamento",
        "tema": "",
        "video_fundo": "video-casamentos.mp4",
        "capa_fundo": "video-casamentos-capa.jpg",
        "rotulo": "Casamentos",
        "titulo_1": "Um filme à altura",
        "titulo_2": "de tudo o que esse dia representa.",
        "abertura": "Cinematografia que emociona.",


        "intro_rotulo": "O que fica no filme",
        "intro_titulo": "A história inteira,<br>na ordem em que aconteceu.",
        "intro_texto": "Um casamento tem uma curva própria: começa no silêncio do quarto e "
                       "termina com todo mundo descalço na pista. Nosso trabalho é acompanhar "
                       "essa curva sem atropelar nenhuma parte dela.",

        "momentos": [
            {"titulo": "A preparação", "texto": "O quarto cheio, o vestido pendurado, as mãos tremendo no botão da camisa."},
            {"titulo": "A espera",     "texto": "Os minutos antes de entrar, quando ninguém sabe muito bem o que dizer."},
            {"titulo": "Os votos",     "texto": "Captados com microfone, do primeiro ao último. É a cena que mais se revê depois."},
            {"titulo": "Os pais",      "texto": "O abraço que acontece sem aviso e dura mais do que o combinado."},
            {"titulo": "O brinde",     "texto": "Os discursos, as piadas internas e a mesa inteira rindo junto."},
            {"titulo": "A pista",      "texto": "Quando o salto sai, a gravata afrouxa e a festa vira o que ela é de verdade."},
        ],

        "convite_titulo": "Vamos conversar<br><em>sobre o seu dia?</em>",
        "convite_texto": "Conte a data, o lugar e um pouco da história de vocês. Respondemos "
                         "pessoalmente, dizemos se a data está livre e montamos uma proposta "
                         "para o seu caso.",
    },

    # ---------------------------------------------------- 15 ANOS
    "15-anos": {
        "nome": "15 anos",
        "tipo": "15 anos",
        "tema": "tema-rosa",
        "video_fundo": "video-15-anos.mp4",
        "capa_fundo": "video-15-anos-capa.jpg",
        "rotulo": "15 anos",
        "titulo_1": "porque 15 anos",
        "titulo_2": "acontecem uma única vez.",
        "abertura": "Ela vai crescer, mudar, descobrir novos caminhos. Mas haverá sempre "
                    "um filme capaz de levá-la de volta à menina que existiu nesta noite.",


        "intro_rotulo": "O que fica no filme",
        "intro_titulo": "A festa inteira,<br>do ensaio a última música.",
        "intro_texto": "Vida, emoção, dança — o mundo é dela. Uma festa de 15 anos tem um "
                       "ritmo próprio: começa devagar, no espelho "
                       "e no cabelo, e termina com todo mundo descalço na pista. Nosso trabalho "
                       "é acompanhar essa curva sem atropelar nenhuma parte dela.",

        "momentos": [
            {"titulo": "O ensaio",      "texto": "Antes da festa, em locação escolhida por você, com o tempo que o ensaio pedir."},
            {"titulo": "A preparação",  "texto": "Cabelo, maquiagem, o vestido chegando, a casa cheia e a ansiedade boa."},
            {"titulo": "A entrada",     "texto": "O corredor, a música, o salão inteiro virando para olhar."},
            {"titulo": "A valsa",       "texto": "Com o pai, com a família, com os padrinhos. Registrada inteira, sem cortes."},
            {"titulo": "As homenagens", "texto": "Discursos e recados captados com microfone, para a voz não se perder na caixa de som."},
            {"titulo": "A pista",       "texto": "A hora em que ninguém esta posando e a festa vira o que ela é de verdade."},
        ],

        "convite_titulo": "Vamos conversar<br><em>sobre a sua festa?</em>",
        "convite_texto": "Conte a data, o lugar e como você imagina a festa. Respondemos "
                         "pessoalmente, dizemos se a data está livre e montamos uma proposta "
                         "para o seu caso.",
    },

    # ---------------------------------------------------- EVENTOS
    "eventos": {
        "nome": "Eventos",
        "tipo": "Evento",
        "tema": "tema-salvia",
        "video_fundo": None,   # CONFIRA: quando tiver um vídeo de evento, ponha o nome aqui
        "capa_fundo": None,
        "rotulo": "Eventos",
        "titulo_1": "Formaturas, aniversários,",
        "titulo_2": "empresas.",
        "abertura": "Luz, tempo e movimento. Filmes feitos com identidade — "
                    "com o mesmo cuidado de imagem e som que levamos para um casamento.",


        "intro_rotulo": "O que filmamos",
        "intro_titulo": "Registro de eventos<br>e vídeo para redes.",
        "intro_texto": "Cada projeto tem uma duração e uma entrega diferentes. O que não muda "
                       "é o cuidado com a imagem, com o som e com o tempo de quem está ali.",

        "momentos": [
            {"titulo": "Formaturas",    "texto": "A colação, o juramento e o abraço da família na saída."},
            {"titulo": "Aniversários",  "texto": "A festa registrada com o mesmo cuidado que levamos a um casamento."},
            {"titulo": "Corporativo",   "texto": "Congressos, confraternizações e lançamentos, com imagem que serve para a marca."},
            {"titulo": "Depoimentos",   "texto": "Entrevistas com áudio limpo, prontas para virar conteúdo."},
            {"titulo": "Redes sociais", "texto": "Cortes verticais do mesmo material, para Instagram e TikTok."},
            {"titulo": "Institucional", "texto": "Um filme que apresenta a empresa sem parecer propaganda."},
        ],

        "convite_titulo": "Vamos conversar<br><em>sobre o seu evento?</em>",
        "convite_texto": "Conte a data, o formato e para onde o vídeo vai depois. Respondemos "
                         "pessoalmente e montamos um orçamento para o seu caso.",
    },
}

ORDEM_SETORES = ["casamentos", "15-anos", "eventos"]


# ---------------------------------------------------------------
# 8. O QUE FICA COMBINADO
# ---------------------------------------------------------------
COMBINADO = [
    "A data reservada é sua: não aceitamos outro evento no mesmo dia.",
    "O prazo de entrega vai escrito no contrato.",
    "Os arquivos do dia são copiados em duas mídias.",
    "O parcelamento é combinado antes da assinatura.",
]


# ---------------------------------------------------------------
# 9b. QUEM ESTÁ ATRÁS DA CÂMERA
#     ⚠️ FALTA A FOTO: salve a sua foto de perfil do Instagram como
#     static/gerson.jpg (clique com o botão direito na foto e "salvar
#     imagem como"). Sem o arquivo, a seção mostra só o texto.
# ---------------------------------------------------------------
QUEM = {
    "ativo": True,
    "rotulo": "Filmmaker",
    "nome": "Gerson Martins",
    "foto": "gerson.jpg",
    "instagram": "https://instagram.com/gerson.martinss",
    "chamada": "Piloto de drone, músico, amante da bela arte do cinema.",

    # Cada bloco abre com uma frase curta e desenvolve embaixo.
    "blocos": [
        {
            "abre": "Antes de filmar eventos eu já exercia a arte.",
            "texto": "Talvez venha daí uma parte importante do meu jeito de montar um "
                     "filme. Para mim, música não entra depois para preencher uma edição. "
                     "Ritmo, pausa, voz, silêncio e imagem precisam nascer juntos. O corte "
                     "acompanha o que a música pede — e o áudio nunca é tratado como detalhe.",
        },
        {
            "abre": "Também sou eu quem pilota o drone.",
            "texto": "Não é uma etapa terceirizada nem uma imagem aérea feita apenas porque "
                     "fica bonita. É o mesmo olhar que acompanha a história no chão e, em "
                     "determinado momento, ganha altura. Por isso, as imagens de cima "
                     "pertencem ao mesmo filme — não parecem acrescentadas depois.",
        },
        {
            "abre": "E antes de tudo isso, já havia a tecnologia.",
            "texto": "Trabalho com ela desde antes de ter uma câmera profissional nas mãos. "
                     "É dessa relação que nasceu, inclusive, este site — feito aqui, linha "
                     "por linha, para que o filme de vocês tenha um lugar próprio, e não "
                     "fique perdido em alguma conversa.",
        },
    ],

    "fecho": "No fim, música, tecnologia, câmera e voo acabaram se encontrando no mesmo lugar.",
    "assinatura": "Gerson Martins · Gerson Filmes",
}


# ---------------------------------------------------------------
# 9. DEPOIMENTOS
#    ⚠️ CONFIRA: o segundo e o terceiro são exemplos de formato.
#    Troque pelos depoimentos reais dos seus clientes.
# ---------------------------------------------------------------
DEPOIMENTOS = [
    {
        "aprovado": True,
        "texto": "Quando assistimos, não parecia um vídeo do casamento. Parecia que "
                 "estávamos vivendo tudo outra vez.",
        "autor": "Fernanda e Tiago",
        "evento": "Casamento em Sete Lagoas",
    },
    {
        "aprovado": True,
        "texto": "Ver a Ana Luíza correndo naquele gramado me fez chorar de novo. "
                 "O filme guardou o dia do jeito que a gente sentiu, não do jeito "
                 "que a gente lembrava.",
        "autor": "Evellyne",
        "evento": "Mãe da Ana Luíza Vinhal · 15 anos",
    },
    {
        "aprovado": True,
        "texto": "Assisti sozinha e depois chamei a família inteira para ver junto. "
                 "Tem coisa ali que aconteceu e ninguém percebeu na hora.",
        "autor": "Cida",
        "evento": "Tia da Ana Luíza · 15 anos",
    },
    {
        "aprovado": True,
        "texto": "A gente escolheu pelo trabalho e ficou pela tranquilidade. No dia "
                 "ninguém pediu para repetir nada — e mesmo assim está tudo lá.",
        "autor": "Thamires e Neilon",
        "evento": "Casamento",
    },
    {
        "aprovado": True,
        "texto": "O teaser chegou antes do que a gente esperava e virou o vídeo mais "
                 "assistido do nosso casamento. Todo mundo perguntou quem filmou.",
        "autor": "Raphaella e Kauan",
        "evento": "Casamento",
    },
]

# Mensagem pronta para pedir a autorização de cada pessoa pelo WhatsApp.
PEDIDO_DEPOIMENTO = """Oi, {nome}! Tudo bem?

Estou montando o site da Gerson Filmes e queria muito ter as suas palavras lá.
Escrevi um rascunho do que entendi que você sentiu — se estiver fiel, me responde
"pode publicar". Se quiser mudar qualquer palavra, muda à vontade, ou me manda
com as suas próprias palavras que eu troco:

"{texto}"

Obrigado de coração!"""


# ---------------------------------------------------------------
# 10. PERGUNTAS
# ---------------------------------------------------------------
FAQ = [
    {
        "pergunta": "Com quanto tempo de antecedência devemos reservar a data?",
        "resposta": "Quanto antes, melhor — sábados de maio a dezembro costumam fechar "
                    "primeiro. Dito isso, se a sua data ainda estiver livre, ela é sua, "
                    "mesmo que falte pouco tempo. Pergunte antes de descartar.",
    },
    {
        "pergunta": "Quantas pessoas filmam e por quantas horas vocês ficam?",
        "resposta": "Depende da opção escolhida. Na Essencial trabalhamos com um ponto de "
                    "câmera; na Completo e na Autoral, com apoio e mais de um ponto ao "
                    "mesmo tempo. A equipe é sempre pequena de propósito: quanto menos "
                    "gente circulando, mais natural fica o que acontece na frente da "
                    "câmera.",  # ⚠️ CONFIRA quantas horas você cobre em cada opção
    },
    {
        "pergunta": "Vocês levam equipamento reserva?",
        "resposta": "Sim. Cartões, baterias e uma câmera extra viajam junto em todo evento. "
                    "Equipamento falha — é do ofício. O que não pode é a falha virar problema "
                    "de vocês.",  # ⚠️ CONFIRA se você realmente leva câmera reserva
    },
    {
        "pergunta": "A trilha do filme é licenciada? Podemos escolher a música?",
        "resposta": "A trilha é licenciada, sim. Usar música comercial sem licença é o motivo "
                    "mais comum de um filme de casamento ser derrubado do Instagram ou do "
                    "YouTube meses depois — e aí o vídeo que vocês queriam mostrar some. "
                    "Vocês podem sugerir referências, e nós procuramos algo com o mesmo clima "
                    "dentro do que é liberado para uso.",
    },
    {
        "pergunta": "Em quanto tempo o filme fica pronto?",
        "resposta": "Até 60 dias nas opções Essencial e Completo, e até 45 dias na Autoral. "
                    "O prazo vai escrito no contrato, e um trecho curto costuma chegar antes "
                    "disso para vocês já poderem mostrar.",
    },
    {
        "pergunta": "Recebemos também os arquivos brutos?",
        "resposta": "O que entregamos é o filme montado — é nele que está o trabalho. "
                    "O material bruto de um dia inteiro passa de centenas de gigabytes e não "
                    "se assiste. Guardamos tudo por um ano; se você precisar de alguma cena "
                    "específica nesse período, é só pedir.",  # ⚠️ CONFIRA o prazo de guarda
    },
    {
        "pergunta": "Vocês atendem fora de Sete Lagoas?",
        "resposta": "Nossa base é Sete Lagoas e atendemos Belo Horizonte na mesma condição. "
                    "Fora daí, viajamos para o interior de Minas e para qualquer estado do "
                    "Brasil. Quando há viagem, deslocamento e hospedagem aparecem separados "
                    "no orçamento, para você ver de onde vem cada valor.",
    },
    {
        "pergunta": "E se chover ou o horário atrasar?",
        "resposta": "Acontece com frequência e já faz parte do plano. Chegamos cedo, "
                    "conversamos com o cerimonial e temos alternativa de luz e de locação. "
                    "Se o cronograma escorregar, ficamos até a história terminar.",
    },
    {
        "pergunta": "Dá para parcelar?",
        "resposta": "Dá. São 40% na entrada e o restante até 7 dias antes do evento. "
                    "No cartão, parcelamos em até 12 vezes, com os juros da máquina. "
                    "O formato fica combinado antes de assinar.",
    },
    {
        "pergunta": "O que vocês publicam do nosso filme?",
        "resposta": "Trechos curtos, e só com a sua autorização. O filme inteiro não vai "
                    "para lugar nenhum: para mostrar o trabalho usamos recortes de poucos "
                    "segundos, escolhidos para preservar a intimidade de vocês. Se preferir "
                    "que nada seja publicado, é só dizer — o filme fica apenas na sua área "
                    "de cliente.",
    },
]


# ---------------------------------------------------------------
# 11. FORMULÁRIO
# ---------------------------------------------------------------
TIPOS_EVENTO = ["Casamento", "15 anos", "Formatura", "Evento corporativo", "Outro"]

# Coleções que aparecem no formulário para cada tipo de evento
PACOTES_POR_TIPO = {
    "Casamento": ["Essencial", "Legado", "Cinema"],
    "15 anos": ["Essencial", "Completo", "Autoral"],
    "Formatura": ["Cobertura", "Institucional"],
    "Evento corporativo": ["Cobertura", "Institucional"],
    "Outro": [],
}

COMO_CONHECEU = ["Instagram", "Indicação", "Google", "Já conheço seu trabalho", "Outro"]

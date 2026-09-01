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
        "texto": "Daqui a 50 anos, tudo o que vocês viveram neste dia estará a apenas "
                 "um play de distância.",
        "pacote": "Casamento",
        "tema": "",
    },
    {
        "indice": "02",
        "titulo": "15 anos",
        "chamada": "O ano em que ela escolhe quem quer ser.",
        "texto": "São meses de preparação para uma noite intensa de alegria e festa, com "
                 "ela no centro de tudo. Filmamos as duas: a menina que ensaiou a valsa "
                 "por semanas e a que tirou o salto na terceira música.",
        "pacote": "15 anos",
        "tema": "tema-rosa",
    },
    {
        "indice": "03",
        "titulo": "Eventos",
        "chamada": "Formatura, confraternização, lançamento.",
        "texto": "Um chá de bebê anuncia uma chegada. O aniversário infantil guarda uma "
                 "fase que passa depressa. As bodas celebram uma história construída a "
                 "dois. Outras comemorações reúnem pessoas em torno de uma conquista, "
                 "enquanto o lançamento de uma marca, produto ou projeto inaugura um novo "
                 "capítulo. Cada ocasião tem seu próprio significado — e pede um filme "
                 "capaz de traduzi-lo.",
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
        "titulo": "O som também conta a história",
        "texto": "Captamos os votos, discursos e homenagens com microfones dedicados, "
                 "preservando cada palavra com clareza e emoção. Assim, imagem e áudio se "
                 "completam para tornar cada momento ainda mais vivo.",
    },
    {
        "rotulo": "Ar",
        "titulo": "Um novo olhar sobre a celebração",
        "texto": "Nosso drone revela a celebração por uma perspectiva única. Seus movimentos "
                 "valorizam o cenário, a atmosfera e a dimensão de cada momento, "
                 "acrescentando elegância e força cinematográfica a toda a celebração.",
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
        "texto": "Ele chega por um link privado, só de vocês, e a cópia fica com "
                 "quem viveu o dia. É só abrir e rever quando der vontade — hoje "
                 "ou daqui a dez anos.",
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
#    ⚠️ CONFIRA: itens e prazos.
#    O site não publica valor nenhum, nem "sob consulta": o cartão vai
#    direto da descrição para os itens, e o orçamento é enviado pelo
#    WhatsApp, conforme a data, o local e a duração do evento.
# ---------------------------------------------------------------
COLECOES = {
    "Casamento": {
        "titulo": "Casamentos",
        "nota": "Cada opção varia conforme o tempo de cobertura, o número de câmeras e "
                "a abrangência das imagens aéreas. O orçamento é enviado pelo WhatsApp, "
                "considerando também a data, o deslocamento e a duração efetiva do "
                "evento — e vale para Sete Lagoas, Belo Horizonte e região.",

        # Aparece logo abaixo da nota, antes dos cartões.
        "flexibilidade": "Se alguma opção não se encaixar no que vocês imaginam, ela pode "
                         "ser personalizada com itens equivalentes, sem alteração no "
                         "valor combinado. Ajustes e acréscimos são alinhados pelo "
                         "WhatsApp e formalizados em contrato, garantindo clareza e "
                         "segurança em cada detalhe.",

        "pacotes": [
            {
                "indice": "01",
                "nome": "Essencial",
                "selo": "",
                "descricao": "A essência do dia preservada em um filme sensível, preciso "
                             "e feito para permanecer.",
                "botao": "Quero conhecer o Essencial",
                "itens": [
                    {"rotulo": "Horas de cobertura", "valor": "5 horas"},
                    {"rotulo": "2 câmeras",          "valor": "Cerimônia e recepção"},
                    {"rotulo": "Áudio profissional", "valor": "Votos, discursos e homenagens"},
                    {"rotulo": "Filme principal",    "valor": "15 a 25 minutos"},
                    {"rotulo": "1 teaser cinematográfico", "valor": "Um filme curto e artístico"},
                    {"rotulo": "Trilha sonora",      "valor": "Escolhida para conduzir a narrativa"},
                    {"rotulo": "Entrega",            "valor": "Em até 60 dias"},
                ],
                "destaque": False,
            },
            {
                "indice": "02",
                "nome": "Legado",
                "selo": "",
                "descricao": "Mais tempo, mais perspectivas e mais espaço para transformar "
                             "o dia inteiro em memória.",
                "botao": "Quero conhecer o Legado",
                "itens": [
                    {"rotulo": "Making of do casal",
                     "valor": "O registro das horas que antecedem o grande sim, com os "
                              "dois se preparando"},
                    {"rotulo": "4 câmeras em ação",   "valor": "Cerimônia, recepção, festa e ornamentação"},
                    {"rotulo": "Áudio profissional",  "valor": "Votos, discursos e homenagens"},
                    {"rotulo": "Filme principal",     "valor": "30 a 45 minutos"},
                    {"rotulo": "Horas de cobertura",  "valor": "8 horas"},
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
                    {"rotulo": "Filme principal · Cerimônia na íntegra",
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
        "nota": "Atendemos Sete Lagoas, Belo Horizonte e região. O orçamento é enviado "
                "pelo WhatsApp: ensaio em outra cidade e festas acima de quatro horas "
                "entram nessa conversa.",
        "pacotes": [
            {
                "indice": "01",
                "nome": "Essencial",
                "ideal": "A festa registrada com calma",
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

# Formas de pagamento. Fica na mesma seção das coleções: é a primeira pergunta
# de quem acabou de escolher uma opção, e antes ela só existia lá embaixo, nas
# dúvidas — muita gente fechava a página antes de chegar lá.
PAGAMENTO = {
    "rotulo": "Formas de pagamento",
    "texto": "40% na entrada para reservar a data e o restante até 7 dias antes do "
             "evento. No cartão, em até 12 vezes, com os juros da máquina. "
             "O formato fica combinado antes de assinar.",
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
    "chamada": "Antes de trabalhar com filmes de casamento, eu já transitava entre a "
               "música, a tecnologia e a imagem.",
    # Segue logo abaixo do título, antes dos blocos.
    "intro": "Hoje, essas linguagens se encontram na maneira como conto cada história.",

    # Cada bloco abre com uma frase curta e desenvolve embaixo.
    "blocos": [
        {
            "abre": "Sou músico, e isso atravessa todo o meu processo de montagem.",
            "texto": "A trilha não entra apenas para acompanhar as cenas: o filme é "
                     "construído a partir do ritmo do que foi vivido. A entrada de uma voz, "
                     "a duração de um olhar, uma pausa ou um silêncio — tudo participa da "
                     "narrativa. Para mim, imagem e som não são camadas separadas; um "
                     "amplia o significado do outro.",
        },
        {
            "abre": "Também piloto o drone.",
            "texto": "Por isso, as imagens aéreas não aparecem como um recurso isolado ou "
                     "simplesmente decorativo. Elas surgem quando a história pede outra "
                     "perspectiva. O olhar que acompanha os detalhes no chão é o mesmo que, "
                     "do alto, revela a dimensão do lugar e a atmosfera daquele momento.",
        },
        {
            "abre": "A tecnologia faz parte da minha trajetória desde antes da primeira "
                    "câmera profissional.",
            "texto": "Gosto de compreender e construir as ferramentas que sustentam toda a "
                     "experiência. Este site, por exemplo, foi desenvolvido por mim, linha "
                     "por linha, para que cada filme tenha um espaço próprio — organizado, "
                     "acessível e à altura da história que guarda.",
        },
    ],

    # Dois parágrafos de fecho, na ordem em que aparecem.
    "fecho": [
        "No fim, meu trabalho nasce do encontro entre sensibilidade e precisão: escutar "
        "antes de cortar, observar antes de enquadrar e compreender antes de registrar.",

        "Música, câmera, tecnologia e voo se tornaram linguagens diferentes para uma mesma "
        "intenção: preservar não apenas o que aconteceu, mas a maneira como foi vivido.",
    ],
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
        "resposta": "Para apresentar nosso trabalho, utilizamos apenas recortes de "
                    "poucos segundos, selecionados com cuidado e destinados exclusivamente "
                    "ao portfólio. A intimidade de vocês é sempre preservada, e o filme "
                    "completo nunca é publicado ou compartilhado sem autorização.",
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

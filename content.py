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
Evento: {tipo}
Data: {data}
Cidade ou local: {local}
Orçamento: {pacote}
O que não pode faltar: {mensagem}
Como nos encontrou: {conheceu}"""


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
        "texto": "Das celebrações em família aos encontros de empresas, um registro pensado para o propósito de cada evento.",
        "pacote": "Evento",
        "tema": "tema-salvia",
    },
]


# ---------------------------------------------------------------
# 5. COMO EU TRABALHO
# ---------------------------------------------------------------
METODO = [{'rotulo': 'Som',
  'titulo': 'Vozes que permanecem',
  'texto': 'Votos, discursos e homenagens captados com microfones dedicados, para preservar as '
           'palavras que fazem parte da história.'},
 {'rotulo': 'Presença',
  'titulo': 'Registro discreto',
  'texto': 'Acompanhamos os momentos com atenção, sem pedir que vocês parem de viver o dia para a '
           'câmera.'},
 {'rotulo': 'Montagem',
  'titulo': 'Uma edição com identidade',
  'texto': 'Imagem, música e silêncio se encontram em um filme construído a partir da história de '
           'vocês.'}]

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
COLECOES = {'Casamento': {'titulo': 'Casamentos',
               'nota': '',
               'flexibilidade': 'As opções podem ser personalizadas. Os ajustes são alinhados na '
                                'proposta e registrados no contrato.',
               'pacotes': [{'indice': '01',
                            'nome': 'Essencial',
                            'selo': '',
                            'descricao': 'A essência do dia preservada em um filme sensível, '
                                         'preciso e feito para permanecer.',
                            'botao': 'Quero conhecer o Essencial',
                            'itens': [{'rotulo': 'Horas de cobertura', 'valor': '5 horas'},
                                      {'rotulo': 'Câmeras', 'valor': '2 câmeras'},
                                      {'rotulo': 'Cobertura', 'valor': 'Cerimônia'},
                                      {'rotulo': 'Áudio', 'valor': 'Votos, discursos e homenagens'},
                                      {'rotulo': 'Filme principal', 'valor': '15 a 25 minutos'},
                                      {'rotulo': 'Teasers', 'valor': '1 filme curto e artístico'}],
                            'destaque': False},
                           {'indice': '02',
                            'nome': 'Legado',
                            'selo': '',
                            'descricao': 'Mais tempo, mais perspectivas e mais espaço para '
                                         'transformar o dia inteiro em memória.',
                            'botao': 'Quero conhecer o Legado',
                            'itens': [{'rotulo': 'Horas de cobertura', 'valor': '8 horas'},
                                      {'rotulo': 'Câmeras', 'valor': '4 câmeras'},
                                      {'rotulo': 'Cobertura',
                                       'valor': 'Cerimônia e recepção'},
                                      {'rotulo': 'Áudio', 'valor': 'Votos, discursos e homenagens'},
                                      {'rotulo': 'Filme principal', 'valor': '30 a 45 minutos'},
                                      {'rotulo': 'Teasers',
                                       'valor': '2 filmes curtos e artísticos'}],
                            'destaque': True,
                            'extras': [{'rotulo': 'Making of da noiva',
                                        'valor': 'Registro da preparação da noiva antes da '
                                                 'cerimônia'}]},
                           {'indice': '03',
                            'nome': 'Cinema',
                            'selo': '',
                            'descricao': 'Preparação do casal, imagens aéreas e cerimônia na '
                                         'íntegra.',
                            'botao': 'Quero conhecer o Cinema',
                            'itens': [{'rotulo': 'Horas de cobertura',
                                       'valor': 'Sem limite de horas'},
                                      {'rotulo': 'Câmeras', 'valor': '5 câmeras'},
                                      {'rotulo': 'Cobertura',
                                       'valor': 'Cerimônia integral, recepção e festa'},
                                      {'rotulo': 'Áudio', 'valor': 'Votos, discursos e homenagens'},
                                      {'rotulo': 'Teasers',
                                       'valor': '3 filmes curtos e artísticos'}],
                            'destaque': False,
                            'extras': [{'rotulo': 'Pré-wedding',
                                        'valor': 'Ensaio dedicado ao casal'},
                                       {'rotulo': 'Making of noiva e noivo',
                                        'valor': 'Preparação dos dois registrada ao mesmo tempo, '
                                                 'em locais diferentes'},
                                       {'rotulo': 'Drone na cerimônia',
                                        'valor': 'Imagens aéreas conforme as condições do local e '
                                                 'do tempo'}]}],
               'comparacao': 'A quantidade de câmeras e a composição da equipe são informações '
                             'diferentes. Os profissionais e os horários de início e encerramento '
                             'são definidos na proposta.'},
 '15 anos': {'titulo': '15 anos',
             'nota': 'Atendemos Sete Lagoas, Belo Horizonte e região. O orçamento é enviado pelo '
                     'WhatsApp: ensaio em outra cidade e festas acima de quatro horas entram nessa '
                     'conversa.',
             'pacotes': [{'indice': '01',
                          'nome': 'Essencial',
                          'ideal': 'A festa registrada com calma',
                          'itens': ['Entrada, valsa e melhores momentos da festa',
                                    'Discursos e homenagens com microfone',
                                    'Filme de 5 a 8 minutos'],
                          'destaque': False},
                         {'indice': '02',
                          'nome': 'Completo',
                          'ideal': 'Do ensaio até o fim da pista',
                          'itens': ['Ensaio filmado em locação escolhida por você',
                                    'Preparação, entrada, valsa e festa',
                                    'Filme de 10 a 15 minutos e um vídeo curto para redes',
                                    'Dois pontos de câmera e áudio profissional'],
                          'destaque': True},
                         {'indice': '03',
                          'nome': 'Autoral',
                          'ideal': 'Ensaio, festa e material para as redes',
                          'itens': ['Ensaio em duas locações, com troca de look',
                                    'Preparação, entrada, valsa e festa sem limite de horas',
                                    'Imagens de drone e vídeo vertical para redes',
                                    'Valsa e homenagens na íntegra'],
                          'destaque': False}]},
 'Evento': {'titulo': 'Eventos',
            'nota': 'Formaturas, aniversários, confraternizações, eventos corporativos e conteúdo '
                    'em vídeo para redes. Cada projeto tem duração e entrega diferentes, então o '
                    'orçamento é montado caso a caso.',
            'pacotes': [{'indice': '01',
                         'nome': 'Cobertura',
                         'ideal': 'Até quatro horas, um ponto de câmera',
                         'itens': ['Registro dos momentos principais',
                                   'Áudio de discursos e apresentações',
                                   'Filme de 3 a 5 minutos'],
                         'destaque': False},
                        {'indice': '02',
                         'nome': 'Institucional',
                         'ideal': 'Empresas, marcas e formaturas',
                         'itens': ['Roteiro conversado antes da gravação',
                                   'Entrevistas, depoimentos e imagens de apoio',
                                   'Versões para site, YouTube e formato vertical'],
                         'destaque': False}]}}

# Formas de pagamento. Fica na mesma seção das coleções: é a primeira pergunta
# de quem acabou de escolher uma opção, e antes ela só existia lá embaixo, nas
# dúvidas — muita gente fechava a página antes de chegar lá.
PAGAMENTO = {'rotulo': 'Formas de pagamento',
 'texto': 'Entrada de 40% para reservar a data e o restante até 7 dias antes do evento. As '
          'condições de pagamento ficam registradas na proposta e no contrato.'}

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
        "intro_texto": "",

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
    "ativo": False,
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
        "pergunta": "Como saber se nossa data está disponível?",
        "resposta": "Envie a data e o local do evento pelo WhatsApp. Nós conferimos a "
                    "disponibilidade e conversamos sobre o que vocês imaginam para o filme. "
                    "Vale consultar mesmo que falte pouco tempo.",
    },
    {
        "pergunta": "Como funciona a reserva da data?",
        "resposta": "Depois de escolhermos juntos a opção mais adequada, formalizamos a "
                    "contratação. A reserva é confirmada com o contrato assinado e o "
                    "pagamento da entrada.",
    },
    {
        "pergunta": "Quantos profissionais participam e qual é o tempo de cobertura?",
        "resposta": "A equipe e o tempo de cobertura variam conforme a opção contratada e "
                    "a programação do evento. A proposta informa esses detalhes para vocês "
                    "saberem exatamente o que está incluído.",
    },
    {
        "pergunta": "Vocês levam equipamentos de reserva?",
        "resposta": "Sim. Levamos câmera, baterias e cartões de reserva para lidar com "
                    "imprevistos e dar continuidade ao registro do evento.",
    },
    {
        "pergunta": "Podemos participar da escolha das músicas?",
        "resposta": "Sim. Queremos conhecer as músicas e os estilos que fazem parte da "
                    "história de vocês. Essas referências orientam a escolha de trilhas "
                    "licenciadas que combinem com o casal e com o ritmo do filme.",
    },
    {
        "pergunta": "Quando e como recebemos o filme?",
        "resposta": "O prazo de entrega é informado na proposta e registrado no contrato. "
                    "Vocês recebem um link privado para assistir e baixar os filmes "
                    "incluídos na opção escolhida.",
    },
    {
        "pergunta": "Vocês filmam em outras cidades?",
        "resposta": "Sim. Atendemos Belo Horizonte, outras cidades de Minas Gerais e todo "
                    "o Brasil. Quando houver custos de deslocamento e hospedagem, eles "
                    "serão informados na proposta.",
    },
    {
        "pergunta": "Quais são as formas de pagamento?",
        "resposta": PAGAMENTO["texto"],
    },
]


# ---------------------------------------------------------------
# 11. FORMULÁRIO
# ---------------------------------------------------------------
# Opções para montar uma cobertura personalizada. A proposta confirma a combinação.
SERVICOS_PERSONALIZADOS = {
    "Casamento": [
        ("Momentos do dia", [
            "Making of do casal",
            "Making of exclusivo da noiva",
            "Cerimônia",
            "Recepção",
        ]),
        ("Serviços adicionais", [
            "Pré-wedding",
            "Filmes com drone",
            "Teasers (vídeos curtos com os melhores momentos)",
        ]),
        ("O que vocês querem receber", [
            "Filme de 15 a 25 minutos",
            "Filme de 30 a 45 minutos",
            "Cerimônia na íntegra",
        ]),
    ],
    "15 anos": [
        ("Momentos do dia", [
            "Making of",
            "Entrada e valsa",
            "Festa",
            "Discursos e homenagens com áudio dedicado",
        ]),
        ("Serviços adicionais", [
            "Ensaio filmado",
            "Ensaio em duas locações",
            "Imagens de drone (sujeitas ao local e ao clima)",
        ]),
        ("O que vocês querem receber", [
            "Filme de 5 a 8 minutos",
            "Filme de 10 a 15 minutos",
            "Valsa e homenagens na íntegra",
            "Vídeo vertical para redes sociais",
        ]),
    ],
    "Formatura": [
        ("Cobertura", [
            "Registro dos momentos principais",
            "Discursos e apresentações com áudio dedicado",
            "Entrevistas e depoimentos",
        ]),
        ("Entregas", [
            "Filme de 3 a 5 minutos",
            "Vídeo institucional",
            "Vídeo vertical para redes sociais",
            "Versão para site ou YouTube",
        ]),
    ],
    "Evento corporativo": [
        ("Cobertura", [
            "Registro dos momentos principais",
            "Discursos e apresentações com áudio dedicado",
            "Entrevistas e depoimentos",
        ]),
        ("Entregas", [
            "Filme de 3 a 5 minutos",
            "Vídeo institucional",
            "Vídeo vertical para redes sociais",
            "Versão para site ou YouTube",
        ]),
    ],
    "Evento": [
        ("Cobertura", [
            "Registro dos momentos principais",
            "Discursos e apresentações com áudio dedicado",
            "Entrevistas e depoimentos",
        ]),
        ("Entregas", [
            "Filme de 3 a 5 minutos",
            "Vídeo institucional",
            "Vídeo vertical para redes sociais",
            "Versão para site ou YouTube",
        ]),
    ],
    "Outro": [
        ("Cobertura", [
            "Registro dos momentos principais",
            "Discursos e apresentações com áudio dedicado",
        ]),
        ("Entregas", [
            "Filme editado",
            "Vídeo vertical para redes sociais",
        ]),
    ],
}

TIPOS_EVENTO = ["Casamento", "15 anos", "Formatura", "Evento corporativo", "Evento", "Outro"]

# Coleções que aparecem no formulário para cada tipo de evento
PACOTES_POR_TIPO = {
    "Casamento": ["Essencial", "Legado", "Cinema"],
    "15 anos": ["Essencial", "Completo", "Autoral"],
    "Formatura": ["Cobertura", "Institucional"],
    "Evento corporativo": ["Cobertura", "Institucional"],
    "Evento": ["Cobertura", "Institucional"],
    "Outro": [],
}

COMO_CONHECEU = ["Instagram", "Indicação", "Google", "Já conheço seu trabalho", "Outro"]

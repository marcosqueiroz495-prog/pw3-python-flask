#importando o Flask para a aplicação
from flask import Flask, render_template, request
 #criando a função principal para inicializar as rotas
def init_app(app):
    #variaveis globais
    listaConsoles=['Playstation 5','Xbox one', 'Super Nintendo', 'Atari', '3DS']
    listaGames=[{'titulo':'CS-GO', 'ano' : 2012, 'categoria': 'FPS Online', 'plataforma' : 'Pc'}]    
    #criando a rota principal do site 
    @app.route('/')
    #def cria funções no python 
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        #criando variaveis para rota de games
        titulo = "Portal 2"
        ano = 2011
        categoria = "Puzzle"
        jogadores = ['Marcos', 'Richard', 'Miguel', 'Renato', 'Pedro']
        return render_template('games.html', titulo = titulo, ano = ano, categoria = categoria, jogadores=jogadores)
        #variavel do html = valor é a variavel do python
        
        
    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        # criando um objeto (dicionario)
        #lista (array, vetor)
        console = {"Nome":"Playstation 2",
                "Fabricante":"Sony",
                "Ano":2000}
        
        
        #recebendo o valor do form
        if request.method == 'POST':
            if request.form.get('novoConsole'):
                listaConsoles.append(request.form.get('novoConsole'))
                
        return render_template('consoles.html',console=console,
                               listaConsoles=listaConsoles)
        
        
        ##cadastrar um jogo
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method=='POST':
            #aq ele irá gravar os dados na lista
            listaGames.append({'titulo': request.form.get('titulo'), 'ano': request.form.get('ano'), 'categoria' : request.form.get('categoria'), 'plataforma': request.form.get('plataforma')})
        return render_template('cadgames.html', listaGames = listaGames)
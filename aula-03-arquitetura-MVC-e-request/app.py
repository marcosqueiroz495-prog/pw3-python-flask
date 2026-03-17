#comentario no python 
#importando o flask para a aplicação
#de 'flask' (o pacote instalado) importar a classe 'Flask', a partir daí da pra usar todos os métodos (funções) do flask
from flask import Flask, render_template

#importando o controlers
from controllers import routes

#carregando(instanciar) o Flask na variavel app
app = Flask(__name__, template_folder='views')
#variaveis com 2 underlines são variáveis de ambiente do python (variaveis já criadas)
#__name__ representa o nome da aplicação, fala o arquivo principal, ou seja = app = Flask(app.py)

#enviando a variavel app pra rotas
routes.init_app(app)

#iniciando servidor na porta 5000
if __name__ == '__main__':
#verificando se o arquivo gravado em __name__ é o arquivo principal
    app.run(port=5000, debug=True)
#O método .run() inicia o servidor
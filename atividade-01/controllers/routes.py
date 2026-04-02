from flask import render_template, request

listaLivros = []
listaUsuarios = []

def init_app(app):

    @app.route('/')
    def home():
        return render_template('index.html')


# =========================
# LISTA DE LIVROS
# =========================

    @app.route('/livros')
    def livros():
        return render_template(
            'livros.html',
            listaLivros=listaLivros
        )


# =========================
# CADASTRO DE LIVROS
# =========================

    @app.route('/cadlivro', methods=['GET','POST'])
    def cadlivro():

        if request.method == 'POST':

            livro = {
                "titulo": request.form.get('titulo'),
                "autor": request.form.get('autor'),
                "ano": request.form.get('ano'),
                "nota": request.form.get('nota')
            }

            listaLivros.append(livro)

        return render_template(
            'cadlivro.html',
            listaLivros=listaLivros
        )


# =========================
# LISTA DE USUARIOS
# =========================

    @app.route('/usuarios')
    def usuarios():

        return render_template(
            'usuarios.html',
            listaUsuarios=listaUsuarios
        )


# =========================
# CADASTRO DE USUARIOS
# =========================

    @app.route('/cadusuario', methods=['GET','POST'])
    def cadusuario():

        if request.method == 'POST':

            usuario = {
                "nome": request.form.get('nome'),
                "cidade": request.form.get('cidade')
            }

            listaUsuarios.append(usuario)

        return render_template(
            'cadusuario.html',
            listaUsuarios=listaUsuarios
        )
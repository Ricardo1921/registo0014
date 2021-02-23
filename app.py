from flask import Flask, render_template, request,redirect
from user import user
from artigos import Artigos


app = Flask(__name__)
user = user()
art = Artigos()

@app.route('/inserirA', methods=['GET', 'POST'])
def inserirA():
    art.inserirA('Placa Gráfica', 'Asus', 'RTS 3000', 567.7)
    if request.method == 'POST':
        v1 = request.form['category']
        v2 = request.form['brand']
        v3 = request.form['description']
        v4 = request.form['price']
        art.inserirA(v1, v2, v3, v4)
    erro = "Artigo inserido com sucesso"
    return render_template('Artigos/inserirA.html', erro=erro, user=user, art=art)



@app.route('/tabela')
def tabela():
    title = "Lista de Utilizadores"
    return render_template('tabela.html',title=title,  tabela=user.lista, campos=user.campos, user=user)

@app.route('/consultarA')
def consultarA():
    title = "Lista de Artigos"
    return render_template('tabela.html',title=title,  tabela=art.lista, campos=art.campos, user=user)

@app.route('/registo', methods=['GET', 'POST'])
def route():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v2 = request.form['email']
        v3 = request.form['passe']
        v4 = request.form['cpasse']
        if user.existe(v1):
            erro = 'O Utilizador já existe.'
        elif v3 != v4:
            erro = 'A palavra passe não coincide.'
        else:
            erro = 'Utilizador criado com Successo'
            user.gravar(v1, v2, v3)
    return render_template('Utilizadores/registo.html', erro=erro, user=user)


@app.route('/')
def index():
    return render_template('index.html', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v2 = request.form['passe']
        if not user.existe(v1):
            erro = 'O Utilizador não existe.'
        elif not user.log(v1, v2):
            erro = 'A palavra passe está errada.'
        else:
            user.login = v1
            erro = 'Bem-Vindo.'
    return render_template('Utilizadores/login.html', erro=erro, user=user)

@app.route('/logout')
def logout():
    user.reset()
    return redirect('/')


@app.route('/apagar', methods=['GET', 'POST'])
def apagar():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v2 = request.form['passe']
        if not user.existe(v1):
            erro = 'O Utilizador não existe.'
        elif not user.log(v1, v2):
            erro = 'A palavra passe está errada.'
        else:
            user.apaga(v1)
            erro = 'Conta Eliminada com Sucesso.'
    return render_template('Utilizadores/apagar.html', erro=erro, user=user)


@app.route('/newpasse', methods=['GET', 'POST'])
def newpasse():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v0 = request.form['apasse']
        v2 = request.form['passe']
        v3 = request.form['cpasse']
        if not user.existe(v1):
            erro = 'O Utilizador não existe.'
        elif not user.log(v1, v0):
            erro = 'A palavra passe está errada.'
        elif v2 != v3:
            erro = 'A palavra passe não coincide.'
        else:
            user.alterar(v1, v2)
    return render_template('Utilizadores/newpasse.html', erro=erro, user=user)


if __name__ == '__main__':
    app.run(debug=True)

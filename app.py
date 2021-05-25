# modulo das rotas, toda a regra de negocio vem do modulo funcoes


from models import *
from funcoes import *


app = create_app(__name__)


@app.route('/')
def home():
    return render_template('inicio.html')


@app.route('/perfil', methods=['GET', 'POST'])
def perfis():
    return funcao_perfil_listar()


@app.route('/perfil/<nome>', methods=['GET', 'POST'])
def perfil(nome):
    return funcao_perfil_unico(nome)


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    return funcao_cadastro()


@app.route('/mais', methods=['GET', 'POST'])
def mais():
    return mais_opcoes()


@app.route('/deletar', methods=['GET', 'POST'])
def deletar():
    return funcao_deletar()


@app.route('/alterar/<nome>', methods=['GET', 'POST'])
def alterar(nome):
    return funcao_alterar(nome)
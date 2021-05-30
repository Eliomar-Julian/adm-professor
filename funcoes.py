# // modulo que renderiza todas as views...

from flask import Flask, request, render_template, redirect
from models import *
from werkzeug import exceptions
import json


# // retorna o APP..


def create_app(nome):
    nome_ = nome
    app = Flask(nome_, template_folder='templates', 
        static_url_path='', 
        static_folder='static'
    )
    return app


# // lista todos os perfis...


def funcao_perfil_listar():
    try:
        if request.method == 'GET':
            perfis = Listin().listar_perfis_tudo()
            return render_template('listar-nome.html', var=perfis)
        
        elif request.method == 'POST' and request.form['radio'] == 'nome':
            buscas = request.form['busca']
            nomes = Listin().buscar_dinamicamente(
                buscas, 'escola_alunos_nome'
            )
            return render_template('listar-nome.html', var=nomes)
        
        elif request.method == 'POST' and request.form['radio'] == 'turno':
            buscas = request.form['busca']
            turnos = Listin().buscar_dinamicamente(
                buscas, 'escola_alunos_turno'
            )
            return render_template('listar-nome.html', var=turnos)

        elif request.method == 'POST' and request.form['radio'] == 'turma':
            buscas = request.form['busca']
            turmas = Listin().buscar_dinamicamente(
                buscas, 'escola_alunos_turma'
            )
            return render_template('listar-nome.html', var=turmas)

        elif request.method == 'POST' and request.form['radio'] == 'disciplina':
            buscas = request.form['busca']
            materias = Listin().buscar_dinamicamente(
                buscas, 'escola_alunos_materia'
            )
            return render_template('listar-nome.html', var=materias)
    
    except mysql.connector.ProgrammingError:
        return render_template(
            'erros/generico.html', var={
                'frase': 'Erro ao listar'
            }
        )


# // mostra o perfil de cada aluno .. 


def funcao_perfil_unico(nome):
    perfil_ = Insert()
    perfil_.insere_perfil(nome_=nome)
    dados = perfil_.pegar_tudo(nome)
    dados_cadastrais = dados[0][0]
    dados_perfil = dados[1]
    var = dict()
    var['cabecalhos'] = ('TURNO', 'TURMA', 'MATERIA', 'CPF', 'RG')
    var['cadastro'] = dados_cadastrais
    var['perfil'] = dados_perfil
        
    if request.method == 'POST':
        perfil_ = Insert()
        nome = request.form['nome-pessoa']
        atividade = request.form['atividade']
        periodo = request.form['periodo']
        objetivo = request.form['objetivo']
        nota = request.form['nota']
        perfil_.insere_dados_perfil(nome, periodo, nota, atividade, objetivo)
        dados = perfil_.pegar_tudo(nome)
        dados_cadastrais = dados[0][0]
        dados_perfil = dados[1]
        var['cadastro'] = dados_cadastrais
        var['perfil'] = dados_perfil
        return render_template('perfil-individual.html', var=var)
    return render_template('perfil-individual.html', var=var)


# // tela de cadastro


def funcao_cadastro():
    aluno = Models()
    dicio = dict()
    try:
        if request.method == 'POST':
            requests = [ 
                request.form['nome'],
                request.form['radio'],
                request.form['turma'],
                request.form['select'],
                request.files['foto'],
                request.form['cpf'],
                request.form['rg']
                ]
            if requests[4].filename != '' and requests[4].filename != ' ':
                requests[4].save(
                    'static/img/uploads/' + requests[4].filename
                )
            dicio = {
                'nome':requests[0], 
                'turno':requests[1], 
                'turma':requests[2], 
                'materia':requests[3], 
                'foto':requests[4].filename,
                'cpf':requests[5],
                'rg':requests[6]
                }
            aluno.alunos_cadastrar(
                nome=dicio['nome'], 
                turno=dicio['turno'], 
                turma=dicio['turma'], 
                materia=dicio['materia'], 
                foto=dicio['foto'],
                cpf=dicio['cpf'],
                rg=dicio['rg']
                )
            return render_template('perfil.html', var=dicio)
    except mysql.connector.errors.IntegrityError:
        return 'valores duplicados'
    except mysql.connector.errors.ProgrammingError:
        return 'erro de consulta'
    with open('static/conf/config.json', 'r') as conf:
        dicio = json.loads(conf.read())
    return render_template('cadastrar.html', var=dicio)


# // deleta perfis...


def funcao_deletar():
    try:
        if request.method == 'POST':
            try:
                try:
                    org = request.form['checado']
                    for nomes in org.split(','):
                        Delete().deletar(nomes.strip())
                except:
                    org = request.form['deletar']
                    Delete().deletar(org)
                tudo = Listin().buscar_dinamicamente(org, 'escola_alunos_turma')
                return render_template('deletar.html', var=tudo)
            
            except exceptions.BadRequestKeyError:
                org = request.form['selecao']
                tudo = Listin().buscar_dinamicamente(org, 'escola_alunos_turma')
                return render_template('deletar.html', var=tudo)
                
        tudo = Listin().listar_perfis_tudo()
        return render_template('deletar.html', var=tudo)
    except Exception:
        return render_template(
            'erros/generico.html', var={
                'frase': 'Erro ao listar para remoção e alteração'
                }
            )


# // altera dados...


def funcao_alterar(nome):
    try:
        if request.method == 'POST':
            dic = request.form['retorno']
            pegar = list()
            for x in dic.split(';'):
                pegar.append(x.split(','))
            for x in range(len(pegar[0])):
                Update().update(nome, pegar[3][x], pegar[0][x])
                Update().update_atividades(nome, pegar[2][x], pegar[0][x])
                Update().update_trimestre(nome, pegar[1][x], pegar[0][x])
                Update().update_valor(nome, pegar[4][x], pegar[0][x])
            return redirect(f'/perfil/{nome}')
        else:
            var = Update().select_from(nome)
            return render_template('alterar.html', var=var)
    except Exception:
        return render_template('erros/alterar.html')


# // renderiza  a tela de configurações extras...


def mais_opcoes():
    if request.method == 'POST':
        nomes = request.form['nome'].split(',')
        with open('static/conf/config.json', 'r') as conf:
            js = json.loads(conf.read())
            js['disciplinas'] = nomes
            with open('static/conf/config.json', 'w') as save:
                save.write(json.dumps(js))
    return render_template('mais.html')
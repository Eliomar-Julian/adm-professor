# modulo de manipulção de banco de dados
# detem todo as classes de manipulação

from auxiliar_models import *


class Models:
    '''
        cria a primeira database.
    '''
    def __init__(self):
        self.conn = conectar()
        self.cursor = self.conn.cursor()

    def alunos_cadastrar(self, **kwargs):
        nome = kwargs['nome']
        turma = kwargs['turma']
        turno = kwargs['turno']
        materia = kwargs['materia']
        fotografia = kwargs['foto']
        cpf = kwargs['cpf']
        rg = kwargs['rg']
        self.cursor.execute(crete_table_alunos())
        self.cursor.execute(
            insert_table_alunos()%(
                turno, turma, fotografia, materia, nome, cpf,rg
            )
        )
        self.conn.commit()


class Insert:
    '''
        inserção de dados...
    '''
    def __init__(self):
        self.connect = conectar()
        self.cursor = self.connect.cursor()

    def insere_perfil(self, **kwargs) -> None:
        try:
            nome = kwargs['nome_']
            if e_valido(nome):            
                self.cursor.execute(create_table_perfil(nome))
                self.cursor.execute(insert_table_perfil(nome)%(
                    nome, 0, 'nada', 0)
                )
                self.connect.commit()
            else:
                print('nao valido')
        except Exception:
            print('erro de chave')
    
    def pegar_tudo(self, nome_) -> list:
        self.cursor.execute(select_from('alunos')%(nome_))
        info_alunos = self.cursor.fetchall()
        self.cursor.execute(f'SELECT * FROM `{nome_}`')
        info_perfil = self.cursor.fetchall()
        return [info_alunos, info_perfil]

    def insere_dados_perfil(self, a, b, c, d, e) -> None:
        self.cursor.execute(insert_into_perfil(a, b, c, d, e))
        self.connect.commit()


class Delete:
    '''
        delete databases....
    '''
    def __init__(self):
        self.con = conectar()
        self.cursor = self.con.cursor()

    def deletar(self, nome):
        self.cursor.execute(
            f"""DELETE FROM `alunos` WHERE 
                `alunos`.`escola_alunos_nome` = '{nome}';"""
        )
        self.con.commit()
        self.cursor.execute(f"""DROP TABLE IF EXISTS `{nome}`;""")
        self.con.commit()
        print('deletado')


class Listin:
    '''
        Listar dados ...
    '''
    def __init__(self):
        self.con = conectar()
        self.cursor = self.con.cursor()

    def listar_perfis_tudo(self):
        self.cursor.execute(listar_perfis())
        return self.cursor.fetchall()

    def buscar_dinamicamente(self, busca, coluna):
        self.cursor.execute(busca_dinamica(busca, coluna))
        return self.cursor.fetchall()


class Update:
    '''
        alterar dados ...
    '''
    def __init__(self):
        self.con = conectar()
        self.cursor = self.con.cursor()

    def select_from(self, nome):
        self.cursor.execute(discribes(nome))
        return self.cursor.fetchall()

    def update(self, nome, nota, id_):
        self.cursor.execute(update_into_nota(nome, nota, id_))
        self.con.commit()
        return self.cursor.fetchall()

    def update_atividades(self, nome, atividade, id_):
        self.cursor.execute(update_into_atividade(nome, atividade, id_))
        self.con.commit()
        return self.cursor.fetchall()

    def update_trimestre(self, nome, trimestre, id_):
        self.cursor.execute(update_into_periodo(nome, trimestre, id_))
        self.con.commit()
        return self.cursor.fetchall()

    def update_valor(self, nome, valor, id_):
        self.cursor.execute(update_into_valor(nome, valor, id_))
        self.con.commit()
        return self.cursor.fetchall()

    

    

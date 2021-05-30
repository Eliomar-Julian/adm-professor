# // todas as funçoes retornam a sintaxe mysql....

import mysql.connector
import configparser


def ler_ini() -> configparser.ConfigParser:
    conf = configparser.ConfigParser()
    conf.read('configurar.ini')
    return conf['BASE']


def configs() -> dict:
    CONFIG = ler_ini()
    return CONFIG


def conectar() -> mysql.connector.connect:
    CONFIG = configs()
    conn = mysql.connector.connect(
        host=CONFIG['server'],
        user=CONFIG['user'],
        password=CONFIG['password']
    )
    cursor = conn.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS escola;')
    conn.commit()
    conn.close()
    conn = mysql.connector.connect(
        host=CONFIG['server'],
        user=CONFIG['user'],
        password=CONFIG['password'],
        database='escola'
    )
    return conn


def crete_table_alunos() -> str:
    return '''CREATE TABLE IF NOT EXISTS `alunos`(
            `escola_alunos_turno` VARCHAR(15), 
            `escola_alunos_turma` VARCHAR(10), 
            `escola_alunos_foto` VARCHAR(100), 
            `escola_alunos_materia` VARCHAR(100), 
            `escola_alunos_nome` VARCHAR(100) UNIQUE,
            `escola_alunos_cpf` VARCHAR(11),
            `escola_alunos_rg` VARCHAR(12)) ENGINE = innodb;'''


def insert_table_alunos() -> str:
    return '''INSERT INTO `alunos`(
            `escola_alunos_turno`, 
            `escola_alunos_turma`, 
            `escola_alunos_foto`, 
            `escola_alunos_materia`, 
            `escola_alunos_nome`,
            `escola_alunos_cpf`,
            `escola_alunos_rg`) VALUES (
                '%s', '%s', '%s', '%s', '%s', '%s', '%s');'''


def create_table_perfil(nome) -> str:
    return f'''CREATE TABLE IF NOT EXISTS `{nome}`(
            `escola_perfis_id` INT NOT NULL AUTO_INCREMENT,
            `escola_perfis_periodo` VARCHAR(20),
            `escola_perfis_nome` VARCHAR(100), 
            `escola_perfis_nota` FLOAT, 
            `escola_perfis_atividades` VARCHAR(100), 
            `escola_perfis_maxima` FLOAT,
            PRIMARY KEY(escola_perfis_id)) ENGINE = innodb;'''


def insert_table_perfil(nome) -> str:
    return f'''INSERT INTO `{nome}`(
            `escola_perfis_periodo`
            `escola_perfis_nome`, 
            `escola_perfis_nota`, 
            `escola_perfis_atividades`, 
            `escola_perfis_maxima`) VALUES (
                '%s', '{nome}', '%f', '%s', '%f');'''


def e_valido(nome) -> bool:
    con = conectar()
    cursor = con.cursor()
    cursor.execute('SELECT `escola_alunos_nome` FROM `alunos`;')
    lista_nomes = cursor.fetchall()
    for nomes in lista_nomes:
        if nome in nomes:
            return True
    return False


def listar_perfis():
    return '''SELECT * FROM `escola`.`alunos`;'''


def busca_dinamica(nome, coluna):
    return f'''SELECT * FROM `escola`.`alunos`
            WHERE {coluna} LIKE '%{nome}%' ORDER BY escola_alunos_nome;'''


def select_from(from_):
    return f'''SELECT * FROM `{from_}` 
                WHERE escola_alunos_nome = '%s';'''


def insert_into_perfil(nome, periodo, atingido, atividade, pretendido):
    return f'''INSERT INTO `{nome}` (
        `escola_perfis_id`,
        `escola_perfis_periodo`, 
        `escola_perfis_nome`, 
        `escola_perfis_nota`, 
        `escola_perfis_atividades`, 
        `escola_perfis_maxima`)
        VALUES (
            NULL, '{periodo}' ,NULL, '{atingido}', 
            '{atividade}', '{pretendido}');'''


def discribes(nome):
    return f"""SELECT * FROM `{nome}`;"""


def update_into_nota(nome, nota, id_):
    return f"""UPDATE `{nome}` SET `escola_perfis_nota` = '{nota}' 
            WHERE `{nome}`.`escola_perfis_id` = {id_};"""


def update_into_atividade(nome, atividade, id_):
    return f"""UPDATE `{nome}` SET `escola_perfis_atividades` = '{atividade}' 
            WHERE `{nome}`.`escola_perfis_id` = {id_};"""


def update_into_periodo(nome, trimestre, id_):
    return f"""UPDATE `{nome}` SET `escola_perfis_periodo` = '{trimestre}' 
        WHERE `{nome}`.`escola_perfis_id` = {id_};"""


def update_into_valor(nome, valor, id_):
    return f"""UPDATE `{nome}` SET `escola_perfis_maxima` = '{valor}' 
        WHERE `{nome}`.`escola_perfis_id` = {id_};"""

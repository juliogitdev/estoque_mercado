import sqlite3
import os



diretorio_principal = os.getcwd()

def conectar_banco():
    try:

        database = sqlite3.connect(os.path.join(diretorio_principal, 'backend', 'database', 'mercado.db'))
        return database
    
    except sqlite3.Error as error:
        print("ERRO AO SE CONECTAR COM BANCO DE DADOS")
        return error


def fechar_banco(banco):
    if banco:
        banco.close()
        print("Banco de dados fechado.")




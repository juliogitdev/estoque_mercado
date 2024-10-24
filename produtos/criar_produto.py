from database.database import conectar_banco, fechar_banco
import sqlite3


def criar_produto(nome, preco, quantidade, categoria):
    try:
        banco = conectar_banco()
        sql = """INSERT INTO produtos (nome, preco, quantidade, categoria_id)
        VALUES (?, ?, ?, ?)"""
        banco.execute(sql, (nome, preco, quantidade, categoria))
        banco.commit()
        print(nome, ", produto criado com sucesso")
    except sqlite3.Error as error:
        print("Falha ao criar produto")
        print("Erro: ", error.sqlite_errorname)
        if error.sqlite_errorcode == 2067:
            print("Esse produto já existe")
        
        

    finally:
        fechar_banco(banco)
    
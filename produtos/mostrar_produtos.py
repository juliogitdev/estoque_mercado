from database.database import *

def mostrar_produtos():
    banco = conectar_banco()
    sql = sql = """
    SELECT p.nome AS produto_nome, c.nome AS categoria_nome, p.preco, p.quantidade
    FROM produtos p
    JOIN categorias c ON p.categoria_id = c.id
    """
    cursor = banco.cursor()

    cursor.execute(sql)

    produtos = cursor.fetchall()

    banco.close()

    dicionario_produtos = {}

    for prd in produtos:
        dicionario_produtos[prd[0]] = {"categoria" : prd[1], "preco" : prd[2], "categoria_id" : prd[3]}

    return dicionario_produtos


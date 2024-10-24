from database.database import conectar_banco, fechar_banco
import sqlite3


def atualizar_estoque(produto_id, quantidade_a_adicionar):
    try:
        # 1. Conectar ao banco de dados
        banco = conectar_banco()
        
        # 2. Comando SQL para atualizar a quantidade do produto
        sql = """
        UPDATE produtos
        SET quantidade = quantidade + ?
        WHERE id = ?
        """  # Atualiza a quantidade adicionando o valor especificado

        # 3. Executar o comando para aumentar a quantidade do produto
        banco.execute(sql, (quantidade_a_adicionar, produto_id))  # Passa os dados como tupla
        
        # 4. Salvar as alterações
        banco.commit()
        
        # 5. Mensagem de sucesso
        print(f"Quantidade do produto com ID {produto_id} aumentou em {quantidade_a_adicionar}.")
        
    except sqlite3.Error as e:
        print("Erro ao aumentar quantidade do produto:", e)
    
    finally:
        fechar_banco(banco)
from database.database import conectar_banco, fechar_banco
import sqlite3


def excluir_produto(produto_id):
    try:
        banco = conectar_banco()
        
        sql = """
        DELETE FROM produtos WHERE id = ?
        """  

        banco.execute(sql, (produto_id,))  
        
        banco.commit()
        
        print(f"Produto removido com sucesso")
        
    except sqlite3.Error as e:
        print("Erro ao excluir produto:", e)
    
    finally:
        fechar_banco(banco)
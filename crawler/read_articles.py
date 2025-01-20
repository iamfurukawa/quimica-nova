import mysql.connector
import json

def read_all():
    try:
        # Configurações de conexão
        connection = mysql.connector.connect(
            host="localhost",
            user="quimicanova",
            password="quimicanova",
            database="quimicanova",
        )
        
        cursor = connection.cursor(dictionary=True)  # Retorna os resultados como dicionários
        
        # Consulta SQL
        query = "SELECT * FROM artigos;"
        cursor.execute(query)
        
        # Recupera os dados
        articles = cursor.fetchall()
        
        # Converte para JSON
        articles_json = json.dumps(articles, ensure_ascii=False, indent=4)
        
        print(articles_json)
        return articles_json
    
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return None
    
    finally:
        # Fecha o cursor e a conexão
        if cursor:
            cursor.close()
        if connection:
            connection.close()

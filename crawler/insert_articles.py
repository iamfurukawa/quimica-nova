import mysql.connector
import uuid

def insert(articles):
    try:
        # Conexão com o banco de dados
        conn = mysql.connector.connect(
            host="localhost",
            user="quimicanova",
            password="quimicanova",
            database="quimicanova"
        )
        cursor = conn.cursor()

        # Query para inserção de artigos
        insert_query = """
        INSERT INTO artigos (uuid, title, year, volume, number, pdf_link)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        # Itera sobre os dados e insere na tabela
        for article in articles:
            year = article["year"]
            volume = article["volume"]
            for number_and_link in article["number_and_link"]["articles"]:
                title = number_and_link["title"]
                pdf_link = number_and_link["link"]
                number = article["number_and_link"]["number"]

                # Gerar UUID único
                unique_id = str(uuid.uuid4())

                # Dados para inserir
                data = (unique_id, title, year, volume, number, pdf_link)
                cursor.execute(insert_query, data)

        conn.commit()
        print("Dados inseridos com sucesso.")
    
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

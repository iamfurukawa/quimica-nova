import mysql.connector

def create():
    try:
        # Conexão com o banco de dados
        conn = mysql.connector.connect(
            host="localhost",
            user="quimicanova",
            password="quimicanova",
            database="quimicanova"
        )
        cursor = conn.cursor()

        # Criação da tabela artigos
        create_table_query = """
        CREATE TABLE IF NOT EXISTS artigos (
            uuid        VARCHAR(255) PRIMARY KEY,
            title       VARCHAR(1024),
            year        VARCHAR(4),
            volume      VARCHAR(10),
            number      VARCHAR(10),
            pdf_link    VARCHAR(2048)
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Tabela `artigos` criada com sucesso.")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

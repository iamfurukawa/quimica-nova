import requests
import os
from lxml import html
from concurrent.futures import ThreadPoolExecutor, as_completed

file_path = "articles/"

def download(articles, max_workers=5):
    tasks = []

    # Cria um pool de threads
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for article in articles:
            # Agenda as tarefas de download
            tasks.append(executor.submit(download_by, article["year"], article["number"], article["link"], article["uuid"]))

        # Processa as tarefas à medida que são concluídas
        for future in as_completed(tasks):
            try:
                result = future.result()
                if result:
                    print(result)
            except Exception as e:
                print(f"Erro em uma tarefa: {e}")

def download_by(year, number, url, uuid):
    try:
        # Cria o diretório necessário
        os.makedirs(os.path.dirname(f"articles/{year}/{number}/"), exist_ok=True)

        # Faz a requisição inicial
        response = requests.get(url, stream=True, allow_redirects=True)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        # Analisa o conteúdo HTML para verificar se há um <embed> com o PDF
        tree = html.fromstring(response.content)
        embed_src = tree.xpath("//embed/@src")  # Procura pelo atributo src no elemento <embed>

        # Usa a URL extraída, se encontrada, para baixar o PDF
        if embed_src:
            pdf_url = embed_src[0]
            print(f"URL do PDF extraída: {pdf_url}")

            pdf_response = requests.get(pdf_url, stream=True)
            pdf_response.raise_for_status()

            # Nome do arquivo baseado na URL do PDF
            file_to_download = f"articles/{year}/{number}/{uuid}.pdf"

            # Salva o conteúdo do arquivo em partes
            with open(file_to_download, "wb") as file:
                for chunk in pdf_response.iter_content(chunk_size=8192):  # Lê em blocos de 8 KB
                    file.write(chunk)
            print(f"Arquivo salvo em: {file_to_download}")
        else:
            print("Nenhum elemento <embed> com um PDF foi encontrado no HTML.")
    except requests.RequestException as e:
        print(f"Erro ao acessar ou baixar o arquivo: {e}")

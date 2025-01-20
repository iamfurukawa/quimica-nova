from concurrent.futures import ThreadPoolExecutor
from convert_article_pdf import pdf_to_md_by
from convert_article_ocr import ocr_to_md_by

def process_article(article):
    tasks = []

    # Processa os artigos com base no novo formato de entrada
    year = int(article["year"])  # Usando o campo 'ano' do novo formato
    number = int(article["number"])  # Usando o campo 'numero' do novo formato
    uuid = article["uuid"]
    file_path = f"articles/{year}/{number}/{uuid}.pdf"

    if year > 2000:
        print(f"PDF {year}/{number}")
        tasks.append(("pdf", file_path))
    elif year < 2000:
        print(f"OCR {year}/{number}")
        tasks.append(("ocr", file_path))
    else:  # year == 2000
        if number > 4:
            print(f"PDF {year}/{number}")
            tasks.append(("pdf", file_path))
        else:
            print(f"OCR {year}/{number}")
            tasks.append(("ocr", file_path))

    return tasks

def handle_task(task):
    task_type, link = task
    try:
        print(f"Processando o artigo {link} com o tipo {task_type}")
        if task_type == "pdf":
            pdf_to_md_by(link)
        elif task_type == "ocr":
            ocr_to_md_by(link)
        print(f"Artigo {link} processado com sucesso")
    except Exception as e:
        print(f"Erro ao processar o artigo {link} task type {task_type}: {e}")

def convert_to_md(articles):
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Cria tarefas para processar cada artigo
        all_tasks = []
        for article in articles:
            all_tasks.extend(process_article(article))

        # Executa as tarefas de forma paralela
        executor.map(handle_task, all_tasks)

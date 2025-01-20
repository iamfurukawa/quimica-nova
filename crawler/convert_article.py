from concurrent.futures import ThreadPoolExecutor
from convert_article_pdf import pdf_to_md_by
from convert_article_ocr import ocr_to_md_by

def process_article(article):
    tasks = []
    for numberAndLink in article["number_and_link"]:
        year = int(article["year"])
        number = int(numberAndLink["number"])
        link = numberAndLink["link"]

        if year > 2000:
            print(f"PDF {year}/{number}")
            tasks.append(("pdf", link))
        elif year < 2000:
            print(f"OCR {year}/{number}")
            tasks.append(("ocr", link))
        else:  # year == 2000
            if number > 4:
                print(f"PDF {year}/{number}")
                tasks.append(("pdf", link))
            else:
                print(f"OCR {year}/{number}")
                tasks.append(("ocr", link))
    return tasks

def handle_task(task):
    task_type, link = task
    if task_type == "pdf":
        pdf_to_md_by(link)
    elif task_type == "ocr":
        ocr_to_md_by(link)

def convert_to_md(articles):
    with ThreadPoolExecutor() as executor:
        # Cria tarefas para processar cada artigo
        all_tasks = []
        for article in articles:
            all_tasks.extend(process_article(article))

        # Executa as tarefas de forma paralela
        executor.map(handle_task, all_tasks)

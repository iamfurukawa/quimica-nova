# Collect data from quimicanova website
from collect_issue_infos import fetch_issue_infos
from collect_articles_links import fetch_articles_links

# Insert data on database
from create_table import create
from insert_articles import insert
from read_articles import read_all

# Download and convert articles
from download_article import download
from convert_article import convert_to_md

# from download_article import download_by
# from convert_article_pdf import pdf_to_md_by
# from convert_article_ocr import ocr_to_md_by
# import json

def main():
    issue_infos = fetch_issue_infos()
    articles_links = fetch_articles_links(issue_infos)
    create()
    insert(articles_links)
    articles = read_all()
    download(articles)
    convert_to_md(articles)

    ##download_by(2024,4,"https://quimicanova.sbq.org.br/audiencia_pdf.asp?aid2=9655&nomeArquivo=v47n4a11.pdf")
    ##download_by(1978,1,"https://quimicanova.sbq.org.br/audiencia_pdf.asp?aid2=5640&nomeArquivo=Vol1No4_45_v01_n4_(13)-indice_assuntos.pdf")
    ##pdf_to_md_by("./articles/2024/4/v47n4a11.pdf")
    ##ocr_to_md_by("./articles/1978/1/Vol1No4_45_v01_n4_(13)-indice_assuntos.pdf")

    #print(json.dumps(articles_links, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

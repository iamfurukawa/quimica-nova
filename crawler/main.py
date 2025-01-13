from collect_issue_infos import fetch_issue_infos
from collect_articles_links import fetch_articles_links
from download_article import download_by
from read_article_ocr import ocr_read_by
from read_article_simple import simple_read_by
import json

def main():
    #issue_infos = fetch_issue_infos()
    #articles_links = fetch_articles_links(issue_infos)
    #download_by(2024,4,"https://quimicanova.sbq.org.br/audiencia_pdf.asp?aid2=9655&nomeArquivo=v47n4a11.pdf")
    #download_by(1978,1,"https://quimicanova.sbq.org.br/audiencia_pdf.asp?aid2=5640&nomeArquivo=Vol1No4_45_v01_n4_(13)-indice_assuntos.pdf")
    #ocr_read_by("./articles/1978/1/Vol1No4_45_v01_n4_(13)-indice_assuntos.pdf")
    simple_read_by("./articles/2024/4/v47n4a11.pdf")
    #print(json.dumps(articles_links, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

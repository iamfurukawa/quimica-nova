import requests
import re
from lxml import html
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_articles_links(issue_infos):
    article_links = []
    
    # Cria um ThreadPoolExecutor para paralelizar as requisições
    with ThreadPoolExecutor() as executor:
        # Um dicionário para mapear os links de requisições com seus respectivos detalhes
        future_to_issue = {}
        
        # Para cada issue_info, envia as requisições para os links de artigos
        for issue_info in issue_infos:
            for issue in issue_info['number_and_link']:
                future = executor.submit(fetch_articles_by, issue['link'])
                future_to_issue[future] = {
                    "year": issue_info['year'],
                    "volume": issue_info['volume'],
                    "number_and_link": {
                        "number": issue['number'],
                        "link": issue['link']
                    }
                }

        # Aguardar e processar os resultados das requisições
        for future in as_completed(future_to_issue):
            issue_data = future_to_issue[future]
            try:
                articles = future.result()  # Obtém o resultado da requisição
                issue_data["number_and_link"]["articles"] = articles
                article_links.append(issue_data)
            except Exception as e:
                print(f"Erro ao buscar artigos para o link {issue_data['number_and_link']['link']}: {e}")
    
    return article_links

def fetch_articles_by(link):
    articles_map = []
    seen_titles = set()
    try:
        # Faz a requisição para a URL
        response = requests.get(link)
        response.raise_for_status()  # Verifica se houve erros na requisição

        # Analisa o conteúdo HTML com lxml
        tree = html.fromstring(response.content)

        # Usa XPath para encontrar as seções de artigos
        sections = tree.xpath("//div[contains(@class, 'artigosLista')]")
        for section in sections:
            # Extrai o título do artigo de cada seção
            title_anchor = section.xpath(".//a[contains(@class, 'tituloArtigo')]")
            title = []
            for partial_title in title_anchor:
                title.append(partial_title.text_content().strip())  # Adiciona cada link à lista
            article_title = re.sub(r'\s+', ' ', " ".join(title))

            # Extrai o link de download do PDF
            download_link = section.xpath(".//a[contains(text(), 'PDF')]/@href")
            if download_link:
                download_link = f"https://quimicanova.sbq.org.br/{download_link[0]}"
            else:
                download_link = None  # Caso não exista link de download

            if article_title not in seen_titles:
                articles_map.append({'title': article_title, 'link': download_link})
                seen_titles.add(article_title)  # Adiciona o título ao conjunto 'seen_titles'
        return articles_map
    except requests.RequestException as e:
        print(f"Erro ao acessar {link}: {e}")
        return articles_map

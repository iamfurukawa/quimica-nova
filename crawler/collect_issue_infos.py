import requests
from lxml import html

# URL do site
QUIMICA_NOVA_EDICOES_ANTERIORES_URL = 'https://quimicanova.sbq.org.br/edicoes_anteriores.asp'

def fetch_issue_infos():
    """
    Faz uma requisição para o site Química Nova e retorna dados dos artigos encontrados.
    """
    try:
        # Faz a requisição para a URL
        response = requests.get(QUIMICA_NOVA_EDICOES_ANTERIORES_URL)
        response.raise_for_status()  # Verifica se houve erros na requisição

        # Analisa o conteúdo HTML com lxml
        tree = html.fromstring(response.content)

        # Usa XPath para encontrar a tabela
        table = tree.xpath('//*[@id="conteudo"]/table')[0]  # Pegue o primeiro elemento correspondente

        rows = table.xpath('.//tr')  # Encontre todas as linhas da tabela

        data = []  # Lista para armazenar os dados da tabela
        for row in rows:
            cols = row.xpath('.//td')  # Encontre as colunas da linha
            if len(cols) < 2:
                continue

            year_link = cols[0].xpath('.//a/text()')  # Link do ano
            volume_link = cols[1].xpath('.//a/text()')  # Link do volume

            if not year_link or not volume_link:
                continue

            year = year_link[0].strip()  # Ano
            volume = volume_link[0].strip()  # Volume

            # Números e suas páginas
            number_and_link = []
            for issue in cols[2:]:
                link = issue.xpath('.//a/@href')
                if link:
                    link_text = issue.xpath('.//a/text()')[0].strip()
                    # Ignora os links de ano
                    if link_text.isdigit():  # Só coleta os números das edições
                        number_and_link.append({"number": link_text, "link": 'https://quimicanova.sbq.org.br/{}'.format(link[0])})

            data.append({"year": year, "volume": volume, "number_and_link": number_and_link})

        return data
    except requests.RequestException as e:
        print(f"Erro ao acessar {QUIMICA_NOVA_EDICOES_ANTERIORES_URL}: {e}")
        return []

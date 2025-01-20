import json

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

USE_CACHE_FOR_COLLECT_DATA = True
USE_CACHE_FOR_DOWNLOAD = True
USE_CACHE_FOR_CONVERT_TO_MD = False

def main():

    if USE_CACHE_FOR_COLLECT_DATA is True:
      articles = read_all()
    else:
      issue_infos = fetch_issue_infos()
      articles_links = fetch_articles_links(issue_infos)
      
      create()
      insert(articles_links)
      articles = read_all()
    
    articles = json.loads(articles)
    
    if USE_CACHE_FOR_DOWNLOAD is False:
      download(articles)
    
    if USE_CACHE_FOR_CONVERT_TO_MD is False:
      convert_to_md(articles)

if __name__ == "__main__":
    main()

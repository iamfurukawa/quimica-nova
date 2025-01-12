from collect_issue_infos import fetch_issue_infos
from collect_articles_links import fetch_articles_links
import json

def main():
    issue_infos = fetch_issue_infos()
    articles_links = fetch_articles_links(issue_infos)

    print(json.dumps(articles_links, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

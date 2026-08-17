import feedparser
from urllib.parse import quote

ARXIV_URL = "https://export.arxiv.org/api/query"

def search_papers(topic, limit=5):

    encoded_topic = quote(topic)

    url = (
        f"{ARXIV_URL}"
        f"?search_query=all:{encoded_topic}"
        f"&start=0"
        f"&max_results={limit}"
    )

    feed = feedparser.parse(url)

    papers = []

    for entry in feed.entries:
        papers.append({
            "title": entry.title,
            "abstract": entry.summary.replace("\n", " "),
            "year": entry.published[:4],
            "authors": [{"name": author.name} for author in entry.authors],
            "citationCount": "N/A",
            "url": entry.link
        })

    return papers

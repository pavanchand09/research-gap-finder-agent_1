import feedparser

ARXIV_URL = "https://export.arxiv.org/api/query"

def search_papers(topic, limit=5):

    query = f"search_query=all:{topic}&start=0&max_results={limit}"

    feed = feedparser.parse(f"{ARXIV_URL}?{query}")

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

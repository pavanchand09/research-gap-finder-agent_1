import requests

BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"


def search_papers(topic, limit=5):
    """
    Search research papers using Semantic Scholar API
    """

    params = {
        "query": topic,
        "limit": limit,
        "fields": "title,abstract,year,authors,url,citationCount"
    }

    try:

        response = requests.get(BASE_URL, params=params)

        if response.status_code != 200:
            return []

        data = response.json()

        return data.get("data", [])

    except Exception as e:
        print(e)
        return []

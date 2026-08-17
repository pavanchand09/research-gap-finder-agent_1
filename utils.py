import requests

BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

def search_papers(topic, limit=5):

    params = {
        "query": topic,
        "limit": limit,
        "fields": "title,abstract,year,authors,citationCount,url"
    }

    headers = {
        "User-Agent": "ResearchGapFinder/1.0"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            headers=headers,
            timeout=30
        )

        print("Status Code:", response.status_code)
        print("Response:", response.text)

        response.raise_for_status()

        data = response.json()

        return data.get("data", [])

    except Exception as e:
        print("Error:", e)
        return []

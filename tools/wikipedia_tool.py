import requests

WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

def search_wikipedia(query: str):
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": query
    }
    response = requests.get(WIKI_API_URL, params=params)
    data = response.json()
    page = next(iter(data["query"]["pages"].values()))
    return page.get("extract", "")

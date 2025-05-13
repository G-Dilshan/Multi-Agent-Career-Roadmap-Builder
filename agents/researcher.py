from tools.web_scrape_tool import search_google
from tools.wikipedia_tool import search_wikipedia

def run_researcher(query: str):
    google_results = search_google(query)
    wikipedia_results = search_wikipedia(query)
    return {
        "google": google_results,
        "wiki": wikipedia_results
    }

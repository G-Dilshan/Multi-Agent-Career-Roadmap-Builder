import os
import requests
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

SCRAPEOPS_API_KEY=os.getenv("SCRAPEOPS_API_KEY")

def search_google(query: str):
    targetUrl = urllib.parse.quote(f"https://www.google.com/search?q={query}")
    url = f"http://api.scrape.do/?token={SCRAPEOPS_API_KEY}&url={targetUrl}"
    response = requests.get(url).json().get("organic_results", [])
    return response

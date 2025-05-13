import os
import requests
# import urllib.parse
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

# SCRAPEOPS_API_KEY=os.getenv("SCRAPEOPS_API_KEY")
# print("Api Key: ", SCRAPEOPS_API_KEY)
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def search_google(query: str):
    # targetUrl = urllib.parse.quote(f"https://www.google.com/search?q={query}")
    # url = f"http://api.scrape.do/?token={SCRAPEOPS_API_KEY}&url={targetUrl}"
    # response = requests.get(url).json().get("organic_results", [])
    # response = requests.request("GET", url)
    # print("Respone: ", response)
    # return response
    tavily_tool = TavilySearch(
    max_results=5,
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # search_depth="basic",
    # time_range="day",
    # include_domains=None,
    # exclude_domains=None
    )
    try:
        response = tavily_tool.invoke({"query": query})
        return response
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return []
    except ValueError as e:
        print("Response was not JSON:", e)
        return []


# import os
# import requests
# import urllib.parse
# from dotenv import load_dotenv

# load_dotenv()

# SCRAPEOPS_API_KEY = os.getenv("SCRAPEOPS_API_KEY")
# print("API Key:", SCRAPEOPS_API_KEY)

# def search_google(query: str):
#     target_url = urllib.parse.quote(f"https://www.google.com/search?q={query}")
#     url = f"http://api.scrape.do/?token={SCRAPEOPS_API_KEY}&url={target_url}"

#     try:
#         response = requests.get(url)

#         print("Status Code:", response.status_code)
#         print("Raw Response Text:", response.text[:500])  # show a snippet for debugging

#         data = response.json()  # this will raise if response is not valid JSON

#         print("Parsed JSON:", data)

#         return data.get("organic_results", [])

#     except requests.exceptions.RequestException as e:
#         print("❌ Request failed:", e)
#         return []
#     except ValueError as e:
#         print("❌ Response was not JSON:", e)
#         return []

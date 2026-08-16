from tavily import TavilyClient
from app.config import settings
client=TavilyClient(settings.TAVILY_API_KEY)
def search(query, max_results=8):
    return client.search(query, max_results=max_results)
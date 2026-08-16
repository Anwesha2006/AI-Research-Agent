from tavily import TavilyClient
from app.config import settings
client=TavilyClient(settings.TAVILY_API_KEY)
def search(query, max_results=8):
    return client.search(query, max_results=max_results)
test=search("Impact of AI on education", max_results=2)
print(test)
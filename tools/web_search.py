from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client =TavilyClient(
    api_key = os.getenv("TAVILY_API_KEY")
)

def search_web(query:str) -> str:
    results = client.search(
        query=query,
        max_results=5
    )
    
    output= ""
    for r in results["results"]:
        output += f"Title : {r['title']}\n"
        output += f"URL: {r['url']}\n"
        output += f"Content: {r['content']}\n\n"
        
    return output
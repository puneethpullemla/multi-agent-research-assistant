from tools.web_search import search_web

def researcher(state):
    query = state['query']
    
    research_results = search_web(query)
    
    return {
        "research_data": research_results
    }
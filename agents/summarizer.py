from models.llm import llm
from prompts.summarizer_prompt import SUMMARIZER_PROMPT

def summarizer(state):
    
    prompt = SUMMARIZER_PROMPT.format(
        research_data=state["research_data"]
        
    )
    
    response = llm.invoke(prompt)
    
    return {
        "summary" : response.content
    }
from models.llm import llm
from prompts.verifier_prompt import VERIFIER_PROMPT

def verifier(state):
    
    prompt = VERIFIER_PROMPT.format(
        summary=state["summary"]
    )
    
    response=llm.invoke(prompt)
    
    return{
        "verified_data": response.content
    }
from models.llm import llm
from prompts.report_prompt import REPORT_PROMPT

def report_generator(state):

    prompt = REPORT_PROMPT.format(
        verified_data=state["verified_data"]
    )

    response = llm.invoke(prompt)

    return {
        "final_report": response.content
    }
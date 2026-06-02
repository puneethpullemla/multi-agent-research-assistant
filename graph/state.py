from typing import TypedDict

class AgentState(TypedDict):
    query:str
    research_data: str
    summary: str
    verified_data: str
    final_report: str
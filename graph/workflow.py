from langgraph.graph import StateGraph, END

from graph.state import AgentState

from agents.researcher import researcher
from agents.summarizer import summarizer
from agents.verifier import verifier
from agents.report_generator import report_generator


def build_graph():

    workflow = StateGraph(AgentState)

    workflow.add_node("researcher", researcher)
    workflow.add_node("summarizer", summarizer)
    workflow.add_node("verifier", verifier)
    workflow.add_node("report_generator", report_generator)

    workflow.set_entry_point("researcher")

    workflow.add_edge("researcher", "summarizer")
    workflow.add_edge("summarizer", "verifier")
    workflow.add_edge("verifier", "report_generator")
    workflow.add_edge("report_generator", END)

    return workflow.compile()
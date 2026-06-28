import os

# Safe fallback so CI never fails due to missing API keys
os.environ.setdefault("GROQ_API_KEY", "dummy-key")


def test_basic_math():
    assert 2 + 2 == 4


def test_graph_build():
    from graph.workflow import build_graph

    graph = build_graph()
    assert graph is not None


def test_graph_compiles():
    from graph.workflow import build_graph

    graph = build_graph()

    # LangGraph compiled object should exist
    assert hasattr(graph, "invoke")


def test_agent_imports():
    from agents.researcher import researcher
    from agents.summarizer import summarizer
    from agents.verifier import verifier
    from agents.report_generator import report_generator

    assert researcher is not None
    assert summarizer is not None
    assert verifier is not None
    assert report_generator is not None
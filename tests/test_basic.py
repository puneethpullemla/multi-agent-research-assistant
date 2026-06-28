import os

os.environ.setdefault("GROQ_API_KEY", "dummy-key")


def test_basic_math():
    assert 2 + 2 == 4


def test_graph_build():
    from graph.workflow import build_graph

    graph = build_graph()

    assert graph is not None
    assert hasattr(graph, "invoke")
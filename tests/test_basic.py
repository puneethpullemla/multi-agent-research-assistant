def test_basic_math():
    assert 2 + 2 == 4


def test_app_import():
    import app
    assert app is not None


def test_graph_import():
    from graph.workflow import build_graph
    assert build_graph is not None
    
def test_researcher_agent():
    from agents.researcher import researcher

    result = researcher({"query": "AI startups in India"})
    assert "research_data" in result
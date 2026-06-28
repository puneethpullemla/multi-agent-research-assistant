from agents.researcher import researcher


def test_researcher_returns_research_data(mocker):

    mocker.patch(
        "agents.researcher.search_web",
        return_value="AI startups in India..."
    )

    state = {
        "query": "AI startups"
    }

    result = researcher(state)

    assert result["research_data"] == "AI startups in India..."
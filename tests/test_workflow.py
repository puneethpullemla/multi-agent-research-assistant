from unittest.mock import Mock
from graph.workflow import build_graph


class FakeResponse:

    def __init__(self, text):
        self.content = text


def test_complete_workflow(mocker):

    mocker.patch(
        "agents.researcher.search_web",
        return_value="Research Data"
    )

    fake_summary = Mock()
    fake_summary.invoke.return_value = FakeResponse("Summary")

    fake_verifier = Mock()
    fake_verifier.invoke.return_value = FakeResponse("Verified")

    fake_report = Mock()
    fake_report.invoke.return_value = FakeResponse("Final Report")

    mocker.patch("agents.summarizer.llm", fake_summary)
    mocker.patch("agents.verifier.llm", fake_verifier)
    mocker.patch("agents.report_generator.llm", fake_report)

    graph = build_graph()

    result = graph.invoke({
        "query": "AI"
    })

    assert result["research_data"] == "Research Data"
    assert result["summary"] == "Summary"
    assert result["verified_data"] == "Verified"
    assert result["final_report"] == "Final Report"
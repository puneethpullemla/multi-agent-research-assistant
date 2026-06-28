from unittest.mock import Mock
from agents.summarizer import summarizer


class FakeResponse:
    content = "This is the summary."


def test_summarizer(mocker):

    fake_llm = Mock()
    fake_llm.invoke.return_value = FakeResponse()

    mocker.patch("agents.summarizer.llm", fake_llm)

    state = {
        "research_data": "Research data"
    }

    result = summarizer(state)

    assert result["summary"] == "This is the summary."
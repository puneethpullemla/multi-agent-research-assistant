from unittest.mock import Mock
from agents.report_generator import report_generator


class FakeResponse:
    content = "Final Report"


def test_report_generator(mocker):

    fake_llm = Mock()
    fake_llm.invoke.return_value = FakeResponse()

    mocker.patch("agents.report_generator.llm", fake_llm)

    state = {
        "verified_data": "Verified"
    }

    result = report_generator(state)

    assert result["final_report"] == "Final Report"
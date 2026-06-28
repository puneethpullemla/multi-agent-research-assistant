from unittest.mock import Mock
from agents.verifier import verifier


class FakeResponse:
    content = "Verified information."


def test_verifier(mocker):

    fake_llm = Mock()
    fake_llm.invoke.return_value = FakeResponse()

    mocker.patch("agents.verifier.llm", fake_llm)

    state = {
        "summary": "Summary"
    }

    result = verifier(state)

    assert result["verified_data"] == "Verified information."
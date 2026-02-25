import pytest

from src.agents.supervisor_agent import supervisor_node


@pytest.mark.skip(reason="Student exercise: implement supervisor_node, then unskip.")
def test_supervisor_routes_math_query() -> None:
    state = {"user_query": "Please calculate 25 * 9"}
    updated = supervisor_node(state)

    # TODO: Replace with real expected route after implementation.
    assert "route" in updated

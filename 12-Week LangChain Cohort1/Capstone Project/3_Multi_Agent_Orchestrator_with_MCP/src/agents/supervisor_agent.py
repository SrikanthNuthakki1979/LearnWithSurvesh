from src.state.agent_state import AgentState


def supervisor_node(state: AgentState) -> AgentState:
    # TODO: Decide route from user_query.
    # Example route rules:
    # - math keywords => "math"
    # - document/kb keywords => "rag"
    # - api/tool keywords => "tool"
    # - otherwise => "final"

    # STUDENT PRACTICE SPACE
    # query = state.get("user_query", "").lower()
    # if any(k in query for k in ["calculate", "sum", "multiply"]):
    #     return {**state, "route": "math"}
    # if any(k in query for k in ["document", "policy", "knowledge base"]):
    #     return {**state, "route": "rag"}
    # return {**state, "route": "final"}

    raise NotImplementedError("TODO: Implement supervisor_node")

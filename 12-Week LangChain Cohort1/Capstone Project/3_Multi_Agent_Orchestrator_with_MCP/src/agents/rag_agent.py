from src.state.agent_state import AgentState


def rag_node(state: AgentState) -> AgentState:
    # TODO: Implement RAG specialist call.
    # MVP idea:
    # - load/retrieve from small local KB
    # - generate concise grounded response

    # STUDENT PRACTICE SPACE
    # query = state.get("user_query", "")
    # result = f"RAG result placeholder for: {query}"
    # return {**state, "rag_result": result, "route": "final"}

    raise NotImplementedError("TODO: Implement rag_node")

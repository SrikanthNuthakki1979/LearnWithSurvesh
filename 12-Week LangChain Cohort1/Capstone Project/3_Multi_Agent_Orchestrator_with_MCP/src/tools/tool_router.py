from src.state.agent_state import AgentState
from src.mcp_clients.mcp_tool_client import call_mcp_tool


def tool_node(state: AgentState) -> AgentState:
    # TODO: Route to external MCP tool based on query intent.

    # STUDENT PRACTICE SPACE
    # query = state.get("user_query", "")
    # tool_result = call_mcp_tool("generic_search", {"query": query})
    # return {**state, "tool_result": tool_result, "route": "final"}

    raise NotImplementedError("TODO: Implement tool_node")

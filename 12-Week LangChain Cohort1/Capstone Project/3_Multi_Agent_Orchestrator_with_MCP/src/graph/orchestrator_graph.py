from src.state.agent_state import AgentState
from src.agents.supervisor_agent import supervisor_node
from src.agents.math_agent import math_node
from src.agents.rag_agent import rag_node
from src.tools.tool_router import tool_node


def run_orchestrator(user_query: str) -> str:
    # TODO: Build LangGraph state machine and execute with initial state.
    # Required nodes: supervisor, math, rag, tool, final
    # Required behavior:
    # - supervisor selects next route
    # - specialist updates state with result
    # - final composes output from whichever result is present

    # STUDENT PRACTICE SPACE
    # from langgraph.graph import StateGraph, START, END
    #
    # def final_node(state: AgentState) -> AgentState:
    #     final_answer = (
    #         state.get("math_result")
    #         or state.get("rag_result")
    #         or state.get("tool_result")
    #         or "No result available."
    #     )
    #     return {**state, "final_answer": final_answer}
    #
    # graph = StateGraph(AgentState)
    # graph.add_node("supervisor", supervisor_node)
    # graph.add_node("math", math_node)
    # graph.add_node("rag", rag_node)
    # graph.add_node("tool", tool_node)
    # graph.add_node("final", final_node)
    # graph.add_edge(START, "supervisor")
    # graph.add_conditional_edges(
    #     "supervisor",
    #     lambda s: s.get("route", "final"),
    #     {"math": "math", "rag": "rag", "tool": "tool", "final": "final"},
    # )
    # graph.add_edge("math", "final")
    # graph.add_edge("rag", "final")
    # graph.add_edge("tool", "final")
    # graph.add_edge("final", END)
    # app = graph.compile()
    # result = app.invoke({"user_query": user_query})
    # return result.get("final_answer", "")

    raise NotImplementedError("TODO: Implement run_orchestrator")

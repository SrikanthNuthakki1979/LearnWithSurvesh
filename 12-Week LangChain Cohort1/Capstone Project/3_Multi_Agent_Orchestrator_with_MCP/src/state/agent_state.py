from typing import TypedDict, Literal


class AgentState(TypedDict, total=False):
    user_query: str
    route: Literal["math", "rag", "tool", "final"]
    math_result: str
    rag_result: str
    tool_result: str
    final_answer: str


# TODO: Extend state with fields like conversation history, citations, confidence.

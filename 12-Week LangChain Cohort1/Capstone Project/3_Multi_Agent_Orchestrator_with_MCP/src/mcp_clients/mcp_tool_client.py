from src.config import settings


def call_mcp_tool(tool_name: str, payload: dict) -> str:
    # TODO: Implement MCP service call.
    # Suggested approach:
    # - POST {base_url}/tools/{tool_name}/invoke with payload
    # - Handle timeout/errors
    # - Return stringified tool response

    # STUDENT PRACTICE SPACE
    # import requests
    # url = f"{settings.mcp_server_base_url}/tools/{tool_name}/invoke"
    # response = requests.post(url, json=payload, timeout=15)
    # response.raise_for_status()
    # data = response.json()
    # return str(data)

    raise NotImplementedError("TODO: Implement call_mcp_tool")

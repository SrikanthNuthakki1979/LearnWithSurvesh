"""
MCP Server 3: Get Current Time Tool - STUDENT EXERCISE
=======================================================
Your task: Complete this server to provide time information
It should run on port 8002.

LEARNING GOALS:
- Create tools with no parameters
- Work with datetime module
- Understand different return types

Runs on: http://localhost:8002
"""

# TODO 1: Import required libraries
# Hint: You need datetime, sys, os, and FastMCP
# FILL IN BELOW:
from mcp.server.fastmcp import FastMCP
import datetime
import sys
import os

# TODO 2: Create the MCP server instance
# FILL IN BELOW:
mcp = FastMCP("Time Service")


# TODO 3: Define the get_current_time tool
# Hint: This tool takes NO parameters (just () after function name)
# Hint: Returns a string
@mcp.tool()
def get_current_time() -> str:
    """
    Get the current local time in ISO format.
    
    Returns:
        Current time as ISO format string (YYYY-MM-DDTHH:MM:SS.mmmmmm)
    """
    # TODO 4: Get current time in ISO format
    # Hint: datetime.datetime.now().isoformat()
    # FILL IN BELOW:
    result = datetime.datetime.now().isoformat()
    
    # TODO 5: Print debug message
    # FILL IN BELOW:
    print(f"[GET_CURRENT_TIME_SERVER] Current time: {result}", file=sys.stderr)
    
    return result


# TODO 6: Run the server
if __name__ == "__main__":
    import uvicorn
    
    # TODO 7: Get port from environment variable (default 8002)
    # FILL IN BELOW:
    port = int(os.environ.get("MCP_TIME_PORT", "8082"))
    
    print("🚀 Starting Time Service Server...")
    print(f"📡 Listening on http://localhost:{port}")
    print("🛠️  Tool: get_current_time")
    print("⏸️  Press Ctrl+C to stop")
    print("-" * 50)
    
    # TODO 8: Run with uvicorn
    # FILL IN BELOW:
    uvicorn.run(mcp.sse_app, host="127.0.0.1", port=port, log_level="info")


"""
TESTING YOUR SERVER:
====================
1. Make sure Servers 1 & 2 are still running
2. Run this file: python 3_get_current_time_server_TODO.py
3. Server should be on http://localhost:8002
4. Now you have 3 servers running!

KEY CONCEPTS:
=============
- NO PARAMETERS: get_current_time() doesn't take a or b
- DATETIME: Working with Python's datetime module
- ISO FORMAT: Standard time format for APIs

NEXT STEPS:
===========
Once this works, move to: 4_rag_server_TODO.py
"""

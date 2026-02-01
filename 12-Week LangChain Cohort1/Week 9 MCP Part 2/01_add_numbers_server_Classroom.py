"""
MCP Server 1: Add Numbers Tool - STUDENT EXERCISE
==================================================
Your task: Complete this server to provide addition functionality
It should run on port 8000.

LEARNING GOALS:
- Understand MCP server structure
- Create tools with @mcp.tool() decorator
- Run HTTP/SSE server with uvicorn

Runs on: http://localhost:8000
"""

# TODO 1: Import required libraries
# Hint: You need FastMCP from mcp.server.fastmcp
# Hint: You need sys for stderr output
# FastMCP -> is a high-level MCP server wrapper -> Registers tools, exposes HTTP/SSE, makes them discoverable by MCP-compatible clients
# FASTAPU for MCP tools

from mcp.server.fastmcp import FastMCP
import sys

# TODO 2: Create the MCP server instance
# Hint: mcp = FastMCP("Your Service Name Here")
# FILL IN BELOW:
# This below line creates an MCP server named "Addition Service"
# When MCP clients see this name during the tool discoveries, capability listings, Math service, Search service, Database service

mcp = FastMCP("Addition Service")




# TODO 3: Define the add_numbers tool
# Hint: Use @mcp.tool() decorator
# Hint: Function should take two integers and return their sum

# {
#     "name": "add_numbers",
#     "inputs": {
#         "a": "integer",
#         "b": "integer"
#     },
#     "output": "integer"
# }

@mcp.tool() # Registers this function as an MCP tool
def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    # TODO 4: Calculate the result
    # FILL IN BELOW:
    result = a + b
    
    # TODO 5: Print debug message to stderr
    # Hint: Use print with file=sys.stderr
    # FILL IN BELOW:
    # sys.stderr -> Keeps logs for seperate from the actual responses; this prevents the tool outputs; Docker logs; Production Monitoring; Debugging agent behaviours
    print(f"[ADD_NUMBERS_SERVER] {a} + {b} = {result}", file = sys.stderr)
    
    # TODO 6: Return the result
    return result


# TODO 7: Run the server
if __name__ == "__main__":
    import uvicorn ## ASGI server - handle your HTTP connections & SSE 
    
    print("🚀 Starting Addition Service Server...")
    print("📡 Listening on http://localhost:8000")
    print("🛠️  Tool: add_numbers")
    print("⏸️  Press Ctrl+C to stop")
    print("-" * 50)
    
    # TODO 8: Run with uvicorn
    # Hint: uvicorn.run(mcp.sse_app, host="127.0.0.1", port=8000, log_level="info")
    # FILL IN BELOW:
    uvicorn.run(mcp.sse_app, host="127.0.0.1", port=8000, log_level="info")
# mcp.sse_app -> A pre-built ASGI app, exposes MCP via Server-Sent Events (SSE)

"""
TESTING YOUR SERVER:
====================
1. Run this file: python 1_add_numbers_server_TODO.py
2. You should see: "🚀 Starting Addition Service Server..."
3. Server should be accessible at http://localhost:8000
4. No errors should appear

COMMON ERRORS:
==============
- "NameError: name 'mcp' is not defined" → Check TODO 2
- "Port already in use" → Make sure no other server on port 8000
- Import errors → Check TODO 1

NEXT STEPS:
===========
Once this works, move to: 2_multiply_numbers_server_TODO.py
"""

"""
MCP Server 2: Multiply Numbers Tool - STUDENT EXERCISE
=======================================================
Your task: Complete this server to provide multiplication functionality
It should run on port 8001.

LEARNING GOALS:
- Practice MCP server creation
- Understand port management
- Create different tools on different servers

Runs on: http://localhost:8001
"""

# TODO 1: Import required libraries
# FILL IN BELOW:
from _________ import FastMCP
import _________
import os

# TODO 2: Create the MCP server instance
# Hint: Name it "Multiplication Service"
# FILL IN BELOW:
mcp = FastMCP(_________)


# TODO 3: Define the multiply_numbers tool
# Hint: Use @mcp.tool() decorator
# FILL IN BELOW:
@_________
def multiply_numbers(a: int, b: int) -> int:
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The product of a and b
    """
    # TODO 4: Calculate the result (multiplication)
    # FILL IN BELOW:
    result = a _____ b
    
    # TODO 5: Print debug message
    # Hint: Show multiplication operation with *
    # FILL IN BELOW:
    print(f"[MULTIPLY_NUMBERS_SERVER] {a} * {b} = {_______}", file=sys.stderr)
    
    return result


# TODO 6: Run the server
if __name__ == "__main__":
    import uvicorn
    
    # TODO 7: Get port from environment variable (default 8001)
    # Hint: int(os.environ.get("MCP_MULT_PORT", "8001"))
    # FILL IN BELOW:
    port = int(os.environ.get("MCP_MULT_PORT", "_______"))
    
    print("🚀 Starting Multiplication Service Server...")
    print(f"📡 Listening on http://localhost:{port}")
    print("🛠️  Tool: multiply_numbers")
    print("⏸️  Press Ctrl+C to stop")
    print("-" * 50)
    
    # TODO 8: Run with uvicorn on the specified port
    # FILL IN BELOW:
    uvicorn.run(mcp._______, host="127.0.0.1", port=_______, log_level="info")


"""
TESTING YOUR SERVER:
====================
1. Make sure Server 1 (8000) is still running
2. Run this file: python 2_multiply_numbers_server_TODO.py
3. You should see: "🚀 Starting Multiplication Service Server..."
4. Server should be on http://localhost:8001
5. Both servers running simultaneously!

KEY DIFFERENCES FROM SERVER 1:
===============================
- Different port (8001 vs 8000)
- Different operation (multiply vs add)
- Different service name
- Port from environment variable

NEXT STEPS:
===========
Once this works, move to: 3_get_current_time_server_TODO.py
"""

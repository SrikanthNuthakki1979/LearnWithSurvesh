"""
Multi-Server MCP Client with LLM Routing
==========================================

This client:
1. Connects to multiple MCP servers running on different ports
2. Discovers all available tools from all servers  
3. Uses OpenAI LLM to understand user questions
4. Routes questions to the appropriate server
5. Returns results to the user

Architecture:
- Server 1 (port 8000): Addition Service
- Server 2 (port 8001): Multiplication Service  
- Server 3 (port 8002): Time Service
- Server 4 (port 8003): RAG Service
- Client: Intelligent router using LLM

STUDENT EXERCISE:
Complete the TODO sections to build a multi-server client that:
- Discovers tools from all servers
- Uses OpenAI LLM to route user questions to the right server
- Calls tools and returns results
"""

import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client
from openai import OpenAI
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI()  # Will automatically use OPENAI_API_KEY from environment

# Server configuration
SERVERS = {
    "addition": {
        "url": "http://localhost:8000/sse",
        "description": "Addition Service - adds two numbers"
    },
    "multiplication": {
        "url": "http://localhost:8001/sse",
        "description": "Multiplication Service - multiplies two numbers"
    },
    "time": {
        "url": "http://localhost:8002/sse",
        "description": "Time Service - gets current time"
    },
    "rag": {
        "url": "http://localhost:8003/sse",
        "description": "RAG Service - learns websites and answers questions about them"
    }
}


async def call_tool_on_server(server_url: str, tool_name: str, arguments: dict) -> str:
    """
    Connect to server, call tool, return result, then disconnect.
    Uses proper async context managers to avoid scope issues.
    
    TODO: Implement this function
    Hints:
    1. Use sse_client(server_url) as context manager
    2. Use ClientSession(read, write) as context manager
    3. Initialize the session with await session.initialize()
    4. Call the tool with await session.call_tool(tool_name, arguments=arguments)
    5. Extract result text from result.content[0].text
    6. Handle exceptions and return error messages
    """
    try:
        # TODO: Connect to server using sse_client
        pass
        
    except Exception as e:
        return f"Error: {e}"


async def discover_tools_from_server(server_name: str, server_url: str) -> list:
    """
    Connect to a server, discover tools, then disconnect.
    Returns list of tool dicts.
    
    TODO: Implement this function
    Hints:
    1. Connect to server using sse_client
    2. Create ClientSession
    3. Initialize session
    4. List tools using await session.list_tools()
    5. Create a list of tool dictionaries with: name, description, server, input_schema
    6. Return the list
    """
    try:
        # TODO: Connect to server and discover tools
        pass
        
    except Exception as e:
        print(f"  ❌ Failed to discover tools from {server_name}: {e}")
        return []


async def discover_all_tools():
    """
    Discover all tools from all servers
    
    TODO: Implement this function
    Hints:
    1. Iterate through SERVERS dictionary
    2. For each server, call discover_tools_from_server()
    3. Store results in a dictionary with server_name as key
    4. Print progress messages
    5. Return the dictionary of all tools
    """
    print("\n📚 Discovering available tools from all servers...")
    
    all_tools = {}
    
    # TODO: Iterate through all servers and discover their tools
    
    return all_tools


def use_llm_to_route(user_question: str, available_tools: dict) -> dict:
    """
    Use OpenAI LLM to decide which tool to use and extract parameters.
    
    Returns dict with:
    - tool_name: name of the tool to call
    - server: which server has this tool
    - arguments: dict of arguments to pass to tool
    
    TODO: Implement this function
    Hints:
    1. Prepare a list of all available tools with descriptions
    2. Create a prompt that explains:
       - The available tools
       - Routing rules (math → add/multiply, time → get_time, etc.)
       - Examples of how to route questions
    3. Ask LLM to respond with JSON: {tool_name, server, arguments}
    4. Call OpenAI API with client.chat.completions.create()
    5. Parse the JSON response
    6. Handle errors gracefully
    """
    
    # TODO: Prepare tool information for LLM
    tools_info = []
    
    # TODO: Create prompt for LLM with routing rules and examples
    prompt = f"""You are an intelligent tool router...
    
YOUR PROMPT HERE
    
"""
    
    # TODO: Call OpenAI API
    # response = client.chat.completions.create(...)
    
    # TODO: Parse and return the decision
    return {"tool_name": None, "server": None, "arguments": None}


async def main():
    """Main client loop"""
    print("\n" + "="*60)
    print("🤖 Multi-Server MCP Client with LLM Routing")
    print("="*60)
    
    # TODO: Discover all tools from all servers
    available_tools = {}  # TODO: Call discover_all_tools()
    
    if not available_tools:
        print("\n❌ Could not connect to any servers. Make sure they are running:")
        print("   Terminal 1: python 01_add_numbers_server_TODO.py")
        print("   Terminal 2: python 02_multiply_numbers_server_TODO.py")
        print("   Terminal 3: python 03_get_current_time_server_TODO.py")
        print("   Terminal 4: python 04_rag_server_TODO.py")
        return
    
    print("\n" + "="*60)
    print("✅ Ready to answer questions! (Type 'quit' to exit)")
    print("="*60)
    
    # Interactive loop
    while True:
        print("\n")
        user_question = input("🎤 Ask a question: ").strip()
        
        if user_question.lower() == 'quit':
            print("\n👋 Goodbye!")
            break
        
        if not user_question:
            continue
        
        # TODO: Use LLM to decide which tool to use
        decision = {}  # TODO: Call use_llm_to_route()
        
        if decision.get("tool_name") is None:
            print(f"\n❌ I don't know how to answer that. Reason: {decision.get('reason', 'No matching tool')}")
            continue
        
        # TODO: Get the server and call the tool
        server_name = decision["server"]
        tool_name = decision["tool_name"]
        arguments = decision.get("arguments", {})
        
        if server_name not in SERVERS:
            print(f"❌ Server '{server_name}' not found")
            continue
        
        server_url = SERVERS[server_name]["url"]
        
        print(f"\n📤 Calling {tool_name} on {server_name} with arguments: {arguments}")
        
        # TODO: Connect, call tool, disconnect
        result = ""  # TODO: Call call_tool_on_server()
        
        print(f"\n✨ Final Answer: {result}")


if __name__ == "__main__":
    print("\n🚀 Starting Multi-Server MCP Client...")
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Client interrupted")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

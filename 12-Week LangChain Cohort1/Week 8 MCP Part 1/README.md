# Week 8: Introduction to AI Agents & MCP 🤖🔌

## 🎯 Session Goal
**Build your first AI Agent Tool.**

We are entering the era of **"Agentic AI"**. It's no longer just about chatting with LLMs; it's about **giving them hands** to do things.

---

## 📚 What is MCP?

### The Standard: Model Context Protocol (MCP)

**MCP** is a standardized protocol that acts as a universal connector between AI agents and external systems, data sources, and tools.

**The Analogy:**
Just like **USB** lets you connect any device to any computer, **MCP** lets you connect any data source/tool to any AI Agent (Claude, Cursor, ChatGPT, etc.).

### Why MCP Matters
- **Standardization**: No more custom integrations for every AI platform
- **Interoperability**: Write once, use with multiple AI agents
- **Extensibility**: Easily add new tools and data sources
- **Security**: Controlled access through the protocol layer
- **Future-Proof**: The standard for AI agent tooling in 2025 and beyond

### Career Relevance
- **MCP is becoming THE standard** for AI agent integration (like USB for AI)
- **Job Market**: Companies are actively hiring "MCP developers" and "Agent engineers"
- **Competitive Edge**: Mastering MCP now positions you ahead in the AI job market
- **Rapid Growth**: Used by Claude, Cursor, and rapidly expanding ecosystem

---

## 🏗️ MCP Architecture

### High-Level Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      AI Agent (Client)                       │
│                  (Claude, Cursor, etc.)                      │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ MCP Protocol
                           │ (JSON-RPC over stdio/HTTP)
                           │
┌──────────────────────────┴──────────────────────────────────┐
│              MCP Server (Tool Provider)                      │
│         - Exposes Tools/Resources/Prompts                   │
│         - Handles Tool Calls                                │
│         - Returns Results                                   │
└─────────────────────────────────────────────────────────────┘
```

### Key Components

#### 1. **Client (AI Agent)**
- Initiates the connection
- Sends tool calls/queries
- Displays results to the user
- Manages the conversation context

**Example Clients:**
- Claude Desktop
- Cursor IDE
- Custom Python scripts
- Web applications

#### 2. **Server (Tool Provider)**
- Listens for incoming connections
- Exposes tools/resources
- Executes requested operations
- Sends results back to the client

**Example Servers:**
- Custom Python MCP servers
- Node.js servers
- Pre-built enterprise servers
- Database connectors

#### 3. **Protocol (Communication Layer)**
- **JSON-RPC 2.0** based messaging
- Standardized request/response format
- Multiple transport options:
  - **stdio** (stdin/stdout) - for local processes
  - **HTTP/SSE** (Server-Sent Events) - for remote servers
  - **WebSocket** - for bidirectional communication

---

## 🔄 MCP Protocol Stack

### Understanding the Protocol Layers

```
┌─────────────────────────────────────────┐
│    Application Layer                     │
│  (Tools, Resources, Prompts)            │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│    Protocol Layer                        │
│  (JSON-RPC 2.0, Request/Response)       │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│    Transport Layer                       │
│  (stdio, HTTP/SSE, WebSocket)           │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│    Physical Connection                   │
│  (Local Process, Network)                │
└─────────────────────────────────────────┘
```

### 1. **Transport Options**

#### **stdio (Standard Input/Output)** ← WEEK 8
- Local process communication
- Used in Week 8 example
- Simple parent-child process model
- Client starts server automatically

```
Client Process
    ↓
  stdin/stdout
    ↓
Server Process
```

**When to use:**
- Local development
- CLI tools
- Desktop applications
- Tight integration with host system

#### **HTTP/SSE (Server-Sent Events)** ← WEEK 9
- Remote server communication
- Client makes HTTP requests
- Server uses SSE for streaming responses
- Better for cloud-based systems

```
Client (HTTP Client)
    ↓
  HTTP POST/GET
    ↓
Server (HTTP Server)
```

**When to use:**
- Cloud deployments
- Multi-client scenarios
- Remote services
- Scalable architectures

### 2. **Protocol Messages**

All communication follows **JSON-RPC 2.0** standard:

```json
// Request Example: Call add_numbers tool
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "add_numbers",
    "arguments": {"a": 10, "b": 20}
  }
}

// Response Example: Tool execution result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "30"
      }
    ]
  }
}

// Error Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32600,
    "message": "Invalid Request"
  }
}
```

### 3. **Server Initialization Handshake**

When a client connects to a server, there's a handshake process:

1. **Client sends**: `initialize` request with capabilities
2. **Server responds**: With its name and version
3. **Client sends**: `initialized` notification
4. **Server responds**: Ready to receive tool calls

```
Client                          Server
  │                              │
  ├─── initialize ───────────→   │
  │                              │
  │   ←─── capabilities ───────  │
  │                              │
  ├─── initialized ──────────→   │
  │                              │
  ├─── list_tools ────────────→  │
  │                              │
  │   ←─── tools list ───────────│
  │                              │
  (Ready to call tools)
```

---

## 🛠️ Building an MCP Server

### What is a Tool?

A **tool** is a function that the AI agent can call. Each tool must have:

1. **Name**: Unique identifier (auto-generated from function name)
2. **Description**: What the tool does (from docstring)
3. **Parameters**: Input schema with types and descriptions
4. **Return Type**: Output type annotation
5. **Implementation**: The actual function logic

### Basic Server Structure

```python
from mcp.server.fastmcp import FastMCP
import datetime

# Create server instance
mcp = FastMCP("Math & Time Server")

# Define tools using decorator
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def get_current_time() -> str:
    """Get the current time in ISO format"""
    return datetime.datetime.now().isoformat()

# Run the server
if __name__ == "__main__":
    mcp.run()
```

### Key Features of FastMCP

- **@mcp.tool()** decorator for easy tool registration
- **Type hints** automatically generate parameter schemas
- **Docstrings** become tool descriptions
- **Async support** for long-running operations
- **Error handling** built-in
- **Minimal boilerplate** - focus on logic, not protocol

### Advanced Tool Features

```python
@mcp.tool()
def calculate_discount(
    original_price: float,
    discount_percent: float = 10.0
) -> float:
    """
    Calculate final price after discount.
    
    Args:
        original_price: The original price in dollars
        discount_percent: Discount percentage (default: 10%)
    
    Returns:
        Final price after discount
    """
    discount_amount = original_price * (discount_percent / 100)
    return original_price - discount_amount
```

---

## 📋 The Week 8 Plan

### Step 1: Install Dependencies
```bash
pip install mcp
```

### Step 2: Build a Simple Server (`simple_server.py`)
Create an MCP server with three tools:
- `add_numbers(a, b)`: Simple math operation
- `multiply_numbers(a, b)`: Another math operation
- `get_current_time()`: System information

### Step 3: Build a Client (`simple_client.py`)
Create an async Python client that:
- Starts the server process automatically
- Connects via stdio transport
- Discovers available tools
- Calls tools with arguments
- Displays results
- Handles cleanup

### Step 4: Run & Test
```bash
python simple_client.py
```

**Expected Output:**
```
Client started
Tools discovered:
  - add_numbers
  - multiply_numbers
  - get_current_time

Calling add_numbers(10, 20)...
Result: 30

Calling multiply_numbers(5, 6)...
Result: 30

Calling get_current_time()...
Result: 2025-01-24T14:32:45.123456
```

---

## 🎓 Key Concepts

### 1. **Server vs Client**
| Aspect | Server | Client |
|--------|--------|--------|
| Purpose | Provides tools | Uses tools |
| Initiates | Listens for connections | Starts/connects |
| Role | Tool executor | Tool caller |
| Lifecycle | Runs until killed | Runs, calls tools, exits |
| Examples | `simple_server.py` | `simple_client.py`, Claude |

### 2. **Tool Discovery**
Process:
1. Client connects to server
2. Client queries: "What tools do you have?"
3. Server responds: Tool schemas (name, description, parameters)
4. Client displays/uses options
5. Agent makes informed decisions about which tools to call

**Benefits:**
- No hardcoding of available tools
- Server can update tools dynamically
- Client always knows current capabilities

### 3. **Lifecycle Management**
```
Client Start
    ↓
Start Server Process
    ↓
Wait for Server Ready
    ↓
Initialize Connection
    ↓
Discover Tools
    ↓
Call Tools (multiple times)
    ↓
Cleanup & Exit
```

### 4. **Context Protocol**
The "Context" in "Model Context Protocol":
- Provides exact, verifiable tool specifications
- Prevents hallucinations about tool existence
- Ensures correct parameter usage
- Keeps LLM "in context" with reality
- Reduces ambiguity and errors

---

## 💡 Real-World Analogy

Think of MCP like a **Restaurant System**:

```
Customer (AI Agent)
    │ "I want pasta with water and dessert"
    │
Waiter (MCP Client)
    ├─ Knows which kitchen can make each item
    ├─ Translates order to kitchen format
    ├─ Knows exact portions and prices
    │
    ↓
Kitchen (MCP Server)
    ├─ Receives order in standard format
    ├─ Prepares dishes
    │ (executes tools: make_pasta, fill_water, make_dessert)
    ├─ Returns prepared dishes with metadata
    │
    ↓
Waiter
    ├─ Receives dishes with timing info
    ├─ Verifies order correctness
    ├─ Presents to customer with recommendations
    │
    ↓
Customer
    ├─ Receives exactly what was ordered
    ├─ Knows cost and time
```

**Without MCP:** Waiter guesses what kitchen can do, wastes time, gets wrong dishes
**With MCP:** Waiter knows exact capabilities, seamless coordination, perfect orders

---

## 📊 MCP Capabilities

### Three Main Methods of Running MCP Servers

#### 1. **stdio** (Week 8) ← WE START HERE
```python
# Server started as child process
# Communication via stdin/stdout
server = StdioServerParameters(
    command=sys.executable,
    args=["simple_server.py"]
)
```
- **Best for:** Local development, CLI tools, tight integration
- **Example:** Cursor IDE extensions, local Python scripts
- **Complexity:** Simple ⭐

#### 2. **HTTP with SSE** (Week 9)
```python
# Server runs as HTTP endpoint
# Client makes REST calls
server = HttpServerParameters(
    url="http://localhost:8000"
)
```
- **Best for:** Cloud services, remote servers, scalability
- **Example:** Cloud-hosted MCP servers, multi-client services
- **Complexity:** Medium ⭐⭐

#### 3. **Custom Transport** (Advanced)
```python
# WebSocket, gRPC, custom protocol
# Maximum flexibility
```
- **Best for:** Real-time applications, custom requirements
- **Example:** Game servers, mission-critical systems
- **Complexity:** High ⭐⭐⭐

---

## 🚀 What You'll Learn This Week

By the end of Week 8, you'll understand:

✅ **MCP Architecture**: How clients and servers interact
✅ **Protocol Fundamentals**: JSON-RPC 2.0, request/response cycles
✅ **Building Servers**: Using `FastMCP` and `@mcp.tool()` decorator
✅ **Tool Implementation**: Creating functions that agents can call
✅ **Schema Generation**: Automatic type-based parameter schemas
✅ **Client Communication**: Async Python client development
✅ **Tool Discovery**: How agents discover available tools
✅ **Process Management**: Starting and controlling server processes
✅ **stdio Transport**: Local process communication pattern
✅ **Error Handling**: Managing failures and edge cases

---

## 📝 Homework Exercises

### Exercise 1: Add a New Tool ⭐
Add a `subtract_numbers` function to the server:
```python
@mcp.tool()
def subtract_numbers(a: int, b: int) -> int:
    """Subtract b from a and return the result"""
    return a - b
```
Update client to call this new tool and verify it works.

### Exercise 2: Advanced Tools ⭐⭐
Create additional tools:
- `square(n: int) -> int`: Return n²
- `reverse_text(text: str) -> str`: Reverse a string
- `factorial(n: int) -> int`: Calculate factorial

### Exercise 3: Tool with Parameters ⭐⭐
```python
@mcp.tool()
def format_time(hours: int, minutes: int = 0) -> str:
    """Format time in HH:MM format"""
    return f"{hours:02d}:{minutes:02d}"
```

### Challenge: Production-Ready Tools ⭐⭐⭐
Enhance tools with:
- Input validation (check ranges, types)
- Clear error messages
- Edge case handling
- Meaningful docstrings
- Return value documentation

**Example:**
```python
@mcp.tool()
def divide(numerator: float, denominator: float) -> float:
    """
    Divide numerator by denominator.
    
    Args:
        numerator: The dividend
        denominator: The divisor (must not be zero)
    
    Returns:
        The quotient
    
    Raises:
        ValueError: If denominator is zero
    """
    if denominator == 0:
        raise ValueError("Division by zero is not allowed")
    return numerator / denominator
```

---

## 🔗 Next Steps (Week 9)

Week 9 will introduce:
- **Building the "Website Agent"**
- **HTTP/SSE transport layer**
- **Multiple server coordination**
- **Real-world use cases**
- **Production deployment**

This progression teaches you:
- Weeks 1-7: LLM fundamentals and RAG
- **Week 8: Building tools** (today)
- Weeks 9-12: Advanced agents and systems

---

## 📚 Additional Resources

### Official MCP Resources
- **MCP Spec**: [spec.modelcontextprotocol.io](https://spec.modelcontextprotocol.io)
- **GitHub**: [Anthropic/mcp](https://github.com/anthropics/mcp)
- **FastMCP Docs**: Check the mcp package documentation

### Learning Resources
- **JSON-RPC 2.0 Spec**: [json-rpc.org](https://www.json-rpc.org/specification)
- **Python async/await**: [Real Python guide](https://realpython.com/async-io-python/)
- **stdio in Python**: subprocess module documentation

### Community
- **Discord**: MCP Community Server
- **GitHub Issues**: Report problems and ask questions
- **Examples**: Check MCP GitHub for community servers

---

## 📞 Quick Reference

### Creating a Tool
```python
@mcp.tool()
def my_tool(param1: int, param2: str) -> str:
    """Tool description shown to agents"""
    # Your implementation
    return result
```

### Server Management
```bash
# Run server (typically called by client)
python simple_server.py

# Client automatically starts server
python simple_client.py
```

### Async Operations
```python
import asyncio

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            result = await session.call_tool("tool_name", arguments={...})

asyncio.run(main())
```

### Common Tool Patterns

**Simple Calculation:**
```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

**With Defaults:**
```python
@mcp.tool()
def greet(name: str, greeting: str = "Hello") -> str:
    """Greet someone"""
    return f"{greeting}, {name}!"
```

**Error Handling:**
```python
@mcp.tool()
def safe_divide(a: float, b: float) -> float:
    """Safely divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

---

## 🎯 Summary

**MCP is the bridge** between AI agents and the tools they need to do real work. This week you'll:

1. **Understand** the MCP architecture
2. **Build** your first MCP server with tools
3. **Create** an async Python client
4. **Connect** client to server
5. **Execute** tool calls successfully

By understanding MCP now, you're learning the **foundation of modern agentic AI**—the exact pattern used by Claude, Cursor, and the next generation of AI applications.

### The Big Picture
```
Weeks 1-7: Learning to USE AI (prompts, chains, memory)
Week 8: Learning to TOOL AI (give agents hands)
Weeks 9-12: Building ADVANCED AI SYSTEMS (multi-agent, workflows)
```

---

## 📋 Prerequisites

- Python 3.8+
- Basic understanding of async/await (we'll review)
- Comfort with command line
- ~30 minutes to complete

---

**Let's build something amazing! 🚀**

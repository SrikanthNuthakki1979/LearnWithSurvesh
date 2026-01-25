# Week 8: Introduction to AI Agents & MCP 🤖🔌
## Building Your First AI Agent Tools

### 🎯 What You'll Build This Week
By the end of this session, you'll create:
- **A Server** that provides tools (simple_server.py)
- **A Client** that uses those tools (simple_client.py)
- **Real communication** between them using the MCP Protocol

Think of it like building a **restaurant system**: the kitchen (server) has recipes, and the waiter (client) takes orders.

---

## 📚 What is MCP? (Model Context Protocol)

### The Simple Explanation
**MCP** is a standardized way for AI agents to talk to tools and get information. It's like a universal translator that lets different AI systems (Claude, Cursor, ChatGPT) all use the same tools.

### The Analogy That Sticks
Just like **USB** is a universal connector that works with any computer and any device:
- USB cable works with your laptop, phone, tablet
- USB works with keyboards, mice, drives, printers
- No matter what device, the protocol is the same

**MCP works the same way for AI:**
- MCP servers work with Claude, Cursor, ChatGPT
- MCP lets you connect any tool (calculator, file reader, weather API)
- All using the same standardized protocol

### Why Should You Care? 💼
1. **Job Market**: Companies are hiring "MCP developers" RIGHT NOW
2. **Future-Proof**: This is the emerging standard for AI tooling
3. **Career Edge**: Most developers don't know MCP yet - you will
4. **Real-World Applications**: Used in production by Anthropic, Replit, and more

---

## 🏗️ MCP Architecture Explained Simply

### The Three-Part System

```
┌──────────────────────────────────────────────────────────────────┐
│                     AI Agent (Client)                             │
│              (Claude, Cursor, or Python script)                   │
│           "I need to do math, what tools do you have?"           │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         │ MCP Protocol
                         │ Communication (JSON-RPC over stdio/HTTP)
                         │
┌────────────────────────┴─────────────────────────────────────────┐
│                    MCP Server                                     │
│            (Your Tools - simple_server.py)                        │
│                                                                    │
│    Tools Provided:                                               │
│    ✓ add_numbers(a, b)                                          │
│    ✓ multiply_numbers(a, b)                                     │
│    ✓ get_current_time()                                         │
│                                                                    │
│    Purpose: Listen for requests, execute tools, return results   │
└──────────────────────────────────────────────────────────────────┘
```

### Breaking It Down: What's Each Part?

#### 1. **The Server (Tool Provider)** 🔧
This is like the **kitchen in a restaurant**.

**What it does:**
- Exposes tools that the AI agent can use
- Listens for tool requests
- Executes the requested tools
- Sends results back

**In our example (`simple_server.py`):**
```python
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b
```
The server **publishes** this tool so anyone can use it.

#### 2. **The Client (Tool User)** 🧑‍💼
This is like the **waiter in a restaurant**.

**What it does:**
- Initiates the connection to the server
- Asks "What tools do you have?"
- Calls the tools with arguments
- Gets results back
- Sometimes displays them to the user

**In our example (`simple_client.py`):**
```python
result = await session.call_tool("add_numbers", arguments={"a": 10, "b": 20})
```
The client **uses** the tool to get a result.

#### 3. **The Protocol (Communication Layer)** 📡
This is like the **phone system** between kitchen and waiter.

**What it does:**
- Standardizes how messages are sent
- Uses JSON-RPC 2.0 format
- Can use different transports: **stdio** or **HTTP**
- Ensures client and server understand each other

---

## 📡 Understanding stdio - The Communication Channel

### What is stdio? 💡

**stdio** stands for **Standard Input/Output**. It's how programs talk to each other on your computer.

Think of it like **three pipes** that connect programs:

```
┌─────────────────────────────────────────────────┐
│         Your Terminal / Parent Process           │
├─────────────────────────────────────────────────┤
│                                                  │
│  stdout ──→ [Messages OUT]                      │
│      ↓                                           │
│  [Program reads what you send]                  │
│      ↑                                           │
│  stdin ←─ [Messages IN]                         │
│                                                  │
│  stderr ──→ [Error/Log messages]               │
│                                                  │
└─────────────────────────────────────────────────┘
```

### The Three Pipes of stdio

#### 1️⃣ **stdout (Standard Output)**
- **Purpose**: Normal output from your program
- **Used for**: Messages you WANT the user/client to see
- **In MCP servers**: **CRITICAL!** This carries MCP protocol messages
- **Example**: `print("Hello")` goes here

```python
# This goes to stdout
print("Server is ready!")

# This goes to stdout - MCP PROTOCOL DATA
# (handled automatically by FastMCP.run())
```

#### 2️⃣ **stdin (Standard Input)**
- **Purpose**: Input to your program
- **Used for**: Messages sent TO your program
- **In MCP servers**: Receives MCP requests from the client
- **Example**: `input("Enter name: ")` reads from here

```python
# Client sends data to server via stdin
# (MCP library handles this automatically)
```

#### 3️⃣ **stderr (Standard Error)**
- **Purpose**: Logging, debugging, error messages
- **Used for**: Messages that are NOT part of the protocol
- **In MCP servers**: **IMPORTANT!** Use this for your debug logs!
- **Example**: `print("Error occurred!", file=sys.stderr)`

```python
# Send logs to stderr (NOT stdout!)
import sys
print("Debug: Adding numbers", file=sys.stderr)

# This is CRITICAL in MCP because:
# - stdout is reserved for MCP protocol messages
# - stderr is for your debugging/logging
# - If you print() normally, it breaks the protocol!
```

### Why This Matters for MCP 🎯

**The Rule**: In an MCP server:
- **stdout** = ONLY MCP protocol messages (automatic with FastMCP)
- **stderr** = Your logs, debug info, error messages
- **stdin** = Receives MCP requests from client

If you mix them:
```python
# ❌ WRONG - This breaks MCP!
def add_numbers(a, b):
    print(f"Adding {a} + {b}")  # Goes to stdout - BREAKS PROTOCOL!
    return a + b

# ✅ CORRECT - This works!
def add_numbers(a, b):
    print(f"Adding {a} + {b}", file=sys.stderr)  # Goes to stderr - safe!
    return a + b
```

### Real-World Example in Our Code

```python
# From simple_server.py
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    result = a + b
    
    # ✅ Log to stderr (doesn't break MCP)
    print(f"add_numbers: {a} + {b} = {result}", file=sys.stderr)
    
    # Actual result is returned to MCP protocol
    return result
```

When you run this:
```
stdout: [MCP protocol messages - Client reads these]
stderr: add_numbers: 10 + 20 = 30  [You see this for debugging]
```

### How stdio Works in Our Project

```
┌─────────────────────────────────────┐
│   simple_client.py (parent)         │
│                                     │
│  Creates StdioServerParameters      │
│  with command = python              │
│  and args = ["simple_server.py"]    │
└──────────────┬──────────────────────┘
               │
    Launches subprocess (child process)
               │
┌──────────────┴──────────────────────┐
│  simple_server.py (subprocess)      │
│                                     │
│  Runs inside client process         │
│  stdin ← receives requests          │
│  stdout → sends responses           │
│  stderr → logs for debugging        │
└─────────────────────────────────────┘
```

**What happens:**
1. Client creates a subprocess (child process)
2. Child process runs `python simple_server.py`
3. Parent opens pipes to child's stdio
4. Client writes requests to child's stdin
5. Child reads from stdin (FastMCP library does this)
6. Child writes responses to stdout (FastMCP library does this)
7. Client reads responses from child's stdout
8. Any debug logs go to stderr (visible in terminal)

---

## 🚀 Understanding Uvicorn - HTTP Alternative (Looking Ahead)

### What is Uvicorn?

**Uvicorn** is an ASGI (Asynchronous Server Gateway Interface) web server written in Python.

In simple terms: **It's a web server that runs Python code**.

### Uvicorn vs stdio - Which to Use?

#### stdio (Week 8 - What We're Using)
```
Client ↔ stdio ↔ Server
```

**When to use:**
- ✅ Local development
- ✅ CLI tools and scripts
- ✅ Tight integration (Cursor IDE, VS Code)
- ✅ Simple setup

**How it works:**
```python
# Client starts server as a process
server_params = StdioServerParameters(
    command=sys.executable,  # Python interpreter
    args=["simple_server.py"],  # Your script
)

# Communication via stdin/stdout pipes
async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
```

**Real-world example:**
- Cursor IDE running MCP servers
- Local Python scripts calling local services
- Development and testing

#### Uvicorn + HTTP (Week 9 - What's Coming)
```
Client ↔ HTTP ↔ Uvicorn ↔ Your MCP Server Code
```

**When to use:**
- ✅ Remote servers
- ✅ Cloud deployments
- ✅ Multiple clients connecting
- ✅ Needs to be accessible over a network

**How it works:**
```python
# Server runs as HTTP service
server = HttpServerParameters(
    url="http://localhost:8000"
)

# Communication via HTTP requests
async with http_client(server) as client:
    await client.call_tool("tool_name", arguments={...})
```

**Real-world example:**
- Claude API accessing your cloud server
- Multiple AI agents using the same server
- Production deployments

### The Full Stack with Uvicorn (Future Week)

```
┌─────────────────────────────────┐
│      Claude (Cloud)             │
│   or Local Python Script        │
└───────────────┬─────────────────┘
                │ HTTP Request
                ↓
┌─────────────────────────────────┐
│     Uvicorn Web Server          │
│   (Running on http://localhost) │
│   (Port 8000)                   │
└───────────────┬─────────────────┘
                │
                ↓
┌─────────────────────────────────┐
│   Your MCP Server Code          │
│   (Tools and Logic)             │
│                                 │
│   @mcp.tool()                  │
│   def your_tool(...):          │
│       return result            │
└─────────────────────────────────┘
```

### Key Differences Table

| Feature | stdio (Week 8) | HTTP/Uvicorn (Week 9) |
|---------|----------------|----------------------|
| Transport | Process pipes | Network HTTP |
| Setup | Simple | Moderate |
| Speed | Very fast | Fast |
| Range | Local only | Local or remote |
| Clients | 1 at a time | Multiple concurrent |
| Use Case | Development | Production |
| Port Needed? | No | Yes (e.g., 8000) |
| Firewall Issues | No | Possibly |

### Why Use Uvicorn?

Uvicorn is needed for HTTP-based MCP servers because:
1. **HTTP Protocol**: Requires a web server to handle HTTP requests
2. **Multi-client Support**: Can serve multiple clients simultaneously
3. **Network Access**: Can be accessed over a network/internet
4. **Separation**: Cleanly separates web server from your business logic
5. **Scalability**: Can be deployed in production environments

**In Week 8 with stdio:**
- Client directly starts server process
- Automatic lifecycle management
- No separate server needed

**In Week 9 with Uvicorn:**
- You run Uvicorn as a separate service
- Uvicorn routes HTTP requests to your MCP code
- Client connects via HTTP URL
- More production-like setup

---

## 🔄 How Communication Flows - Step by Step

### The Complete Journey (stdio version - Week 8)

**Step 1: Client Starts Server**
```
Client Script (simple_client.py)
    ↓
Creates StdioServerParameters
    ↓
Specifies: "Run simple_server.py using Python"
    ↓
Launches server process (subprocess)
    ↓
Waits for server to be ready
```

**Step 2: Client Connects**
```
Client
    ↓
Opens stdin/stdout pipes to server process
    ↓
Establishes bidirectional communication
    ↓
Server is now accessible
```

**Step 3: Handshake (Initialization)**
```
Client sends to server via stdout:
    {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": { ... }
    }

Server reads from stdin
Server processes request
Server writes response to stdout:
    {
        "jsonrpc": "2.0",
        "id": 1,
        "result": {
            "protocolVersion": "2024-11-05",
            "serverInfo": { ... }
        }
    }

Client reads from server's stdout
Client knows server is ready ✅
```

**Step 4: Tool Discovery**
```
Client requests:
    "Hey server, what tools do you have?"

Server responds with:
    [
        {
            "name": "add_numbers",
            "description": "Add two numbers together",
            "inputSchema": { ... }
        },
        ...
    ]

Client now knows available tools
```

**Step 5: Tool Call**
```
Client sends:
    {
        "method": "tools/call",
        "params": {
            "name": "add_numbers",
            "arguments": {"a": 10, "b": 20}
        }
    }

Server executes:
    result = 10 + 20  # = 30
    Logs to stderr: "Adding 10 + 20 = 30" (for debugging)

Server responds:
    {
        "result": 30,
        ...
    }

Client receives result: 30 ✅
```

**Step 6: Cleanup**
```
Client closes session
Client closes server process
Server shuts down
All resources freed
```

---

## 🛠️ Building MCP Servers - The Code Pattern

### The Simple Template

Every MCP server follows this pattern:

```python
# 1. Import what you need
from mcp.server.fastmcp import FastMCP
import sys  # For stderr logging

# 2. Create your server
mcp = FastMCP("Server Name Here")

# 3. Define your tools using @mcp.tool() decorator
@mcp.tool()
def your_tool_name(param1: str, param2: int) -> str:
    """Tool description - shown to AI agents"""
    # Your logic here
    result = param1 * param2  # example
    
    # Log to stderr for debugging (NOT stdout!)
    print(f"Tool executed: {param1}, {param2}", file=sys.stderr)
    
    return result

# 4. Run the server
if __name__ == "__main__":
    mcp.run()
```

### Key Patterns to Remember

#### Pattern 1: Simple Tool
```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers"""
    return a + b
```

#### Pattern 2: Tool with Default Parameters
```python
@mcp.tool()
def greet(name: str, greeting: str = "Hello") -> str:
    """Greet someone with optional greeting"""
    return f"{greeting}, {name}!"
```

#### Pattern 3: Tool with Error Handling
```python
@mcp.tool()
def divide(a: float, b: float) -> float:
    """Safely divide two numbers
    
    Args:
        a: The dividend
        b: The divisor (cannot be zero)
        
    Returns:
        The result of a/b
        
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
```

#### Pattern 4: Tool Returning Complex Data
```python
@mcp.tool()
def get_user_info(user_id: int) -> dict:
    """Get information about a user"""
    return {
        "id": user_id,
        "name": "John Doe",
        "email": "john@example.com"
    }
```

### Type Hints - The Language Between You and AI

**Type hints** are critical in MCP because they tell the AI agent:
1. What parameters your tool needs
2. What type each parameter should be
3. What your tool returns

```python
# The AI reads these type hints and knows exactly how to call your tool!

@mcp.tool()
def process_data(
    count: int,           # Must be an integer
    price: float,         # Must be a decimal number
    name: str,            # Must be text
    is_valid: bool        # Must be true/false
) -> dict:               # Returns a dictionary
    """Process data and return results"""
    return {
        "processed": count,
        "total_price": price,
        "name": name,
        "valid": is_valid
    }
```

### The Critical stderr Rule in Tools

**⚠️ REMEMBER: Use stderr for logging in tools!**

```python
import sys

@mcp.tool()
def calculate(a: int, b: int) -> int:
    """Calculate something"""
    
    # ❌ WRONG - breaks MCP protocol
    print(f"Starting calculation with {a} and {b}")
    
    # ✅ CORRECT - safe logging
    print(f"Starting calculation with {a} and {b}", file=sys.stderr)
    
    result = a + b
    
    # ✅ CORRECT - log to stderr
    print(f"Result: {result}", file=sys.stderr)
    
    # The actual result goes through MCP protocol
    return result
```

**Why?**
- `stdout` is where MCP protocol messages go
- Any regular `print()` mixes with protocol data
- This confuses the client and breaks everything
- `stderr` is reserved for your debugging

---

## 📝 Our Example Server - Line by Line

### simple_server.py (Complete Walkthrough)

```python
# ===== PART 1: Imports =====
from mcp.server.fastmcp import FastMCP  # The MCP server framework
import datetime                          # For timestamps
import sys                               # For stderr logging

# ===== PART 2: Create Server =====
mcp = FastMCP("Math & Time Helper")

# ===== PART 3: Define Tool 1 =====
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    result = a + b
    print(f"add_numbers: {a} + {b} = {result}", file=sys.stderr)
    return result

# ===== PART 4: Define Tool 2 =====
@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers together"""
    result = a * b
    print(f"multiply_numbers: {a} × {b} = {result}", file=sys.stderr)
    return result

# ===== PART 5: Define Tool 3 =====
@mcp.tool()
def get_current_time() -> str:
    """Get the current time in ISO 8601 format"""
    result = datetime.datetime.now().isoformat()
    print(f"get_current_time(): {result}", file=sys.stderr)
    return result

# ===== PART 6: Run Server =====
if __name__ == "__main__":
    print("=" * 50, file=sys.stderr)
    print("Starting Math & Time Helper Server", file=sys.stderr)
    print("=" * 50, file=sys.stderr)
    print("Listening for client connections...", file=sys.stderr)
    mcp.run()
```

---

## 👨‍💻 Our Example Client - Line by Line

### simple_client.py (Complete Walkthrough)

```python
# ===== PART 1: Imports =====
import asyncio                          # For async/await
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import sys, os

# ===== PART 2: Locate Server =====
server_script = os.path.join(
    os.path.dirname(__file__),
    "simple_server.py"
)

# ===== PART 3: Configure Server Startup =====
server_params = StdioServerParameters(
    command=sys.executable,
    args=[server_script],
)

# ===== PART 4: Define Async Client =====
async def run_client():
    """Main async function"""
    print("=" * 50)
    print("MCP Client Starting")
    print("=" * 50)
    
    try:
        # Start server process and open pipes
        async with stdio_client(server_params) as (read, write):
            print("\n✅ Server Process Started")
            
            # Create communication session
            async with ClientSession(read, write) as session:
                print("✅ Session Created")
                
                # Initialize handshake
                print("\n📡 Initializing Connection...")
                await session.initialize()
                print("✅ Connected and Ready")
                
                # Discover tools
                print("\n🔍 Discovering Tools...")
                tools = await session.list_tools()
                print(f"✅ Found {len(tools.tools)} tools")
                
                # Call tools
                print("\n" + "=" * 50)
                print("CALLING TOOLS")
                print("=" * 50)
                
                # Test 1
                print("\nTest 1: add_numbers(10, 20)")
                result = await session.call_tool(
                    "add_numbers",
                    arguments={"a": 10, "b": 20}
                )
                print(f"Result: {result.content[0].text}")
                
                # Test 2
                print("\nTest 2: multiply_numbers(5, 6)")
                result = await session.call_tool(
                    "multiply_numbers",
                    arguments={"a": 5, "b": 6}
                )
                print(f"Result: {result.content[0].text}")
                
                # Test 3
                print("\nTest 3: get_current_time()")
                result = await session.call_tool(
                    "get_current_time",
                    arguments={}
                )
                print(f"Result: {result.content[0].text}")
                
                print("\n" + "=" * 50)
                print("✅ ALL TESTS PASSED!")
                print("=" * 50)
                
    except Exception as e:
        print(f"\n❌ Error: {e}")
        raise

# ===== PART 5: Run Async Function =====
if __name__ == "__main__":
    asyncio.run(run_client())
```

### Understanding async/await

Don't be intimidated! Here's the simple version:

```
Without async (blocking):
    Ask server → WAIT (blocked) → Get response

With async/await (non-blocking):
    Ask server → await response (can do other things) → Response arrives
```

In our code, we use `async` and `await` because:
- Network communication takes time
- We don't want the program frozen waiting
- `await` lets Python handle other tasks while waiting
- When response arrives, execution continues

---

## 🎯 Step-by-Step: How to Run This Week's Project

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Files Are Created Automatically
The Jupyter notebook uses `%%writefile` to create:
- `simple_server.py`
- `simple_client.py`

### Step 3: Run the Client
```bash
python simple_client.py
```

**What happens:**
1. Client launches
2. Client starts server subprocess
3. Client and server connect via stdio pipes
4. Handshake completes
5. Client discovers tools
6. Client calls each tool
7. Server executes, returns results
8. Client displays results
9. Cleanup and shutdown

### Expected Output
```
==================================================
MCP Client Starting
==================================================

✅ Server Process Started
✅ Session Created

📡 Initializing Connection...
✅ Connected and Ready

🔍 Discovering Tools...
✅ Found 3 tools
   • add_numbers: Add two numbers together.
   • multiply_numbers: Multiply two numbers together
   • get_current_time: Get the current time...

==================================================
CALLING TOOLS
==================================================

Test 1: add_numbers(10, 20)
Result: 30

Test 2: multiply_numbers(5, 6)
Result: 30

Test 3: get_current_time()
Result: 2025-01-24T14:32:45.123456

==================================================
✅ ALL TESTS PASSED!
==================================================
```

---

## 🧠 Key Learning Points

### What You Learned About stdio
1. **stdout** = MCP protocol messages (ONLY)
2. **stdin** = Incoming requests from client
3. **stderr** = Your debug logs (safe to use)
4. **Why it matters**: Mixing them breaks the protocol
5. **Rule**: Always use `file=sys.stderr` for logging in tools

### What You Learned About Uvicorn (Preview)
1. **Uvicorn** = Web server for Python
2. **HTTP-based MCP** = Uvicorn + your MCP code
3. **Use case**: Remote servers, multiple clients
4. **Timing**: We'll use this in Week 9
5. **Benefit**: Production-ready architecture

### What You Learned About MCP
1. **Server-Client Architecture**: Separation of concerns
2. **Tool Registration**: Using `@mcp.tool()` decorator
3. **Type Hints**: Tell AI agents how to use tools
4. **stdio Transport**: Local process communication
5. **Protocol**: JSON-RPC 2.0 over stdin/stdout

---

## 📝 Homework Exercises

### Exercise 1: Add New Tools ⭐
Add to `simple_server.py`:
```python
@mcp.tool()
def subtract_numbers(a: int, b: int) -> int:
    """Subtract b from a"""
    result = a - b
    print(f"subtract: {a} - {b} = {result}", file=sys.stderr)
    return result

@mcp.tool()
def divide_numbers(a: float, b: float) -> float:
    """Divide a by b safely"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    result = a / b
    print(f"divide: {a} / {b} = {result}", file=sys.stderr)
    return result
```

Update `simple_client.py` to call these new tools.

### Exercise 2: Advanced Tools ⭐⭐
Create tools for:
- `square(n: int) -> int`: Return n²
- `reverse_text(text: str) -> str`: Reverse a string
- `word_count(text: str) -> int`: Count words in text

### Exercise 3: Complex Return Types ⭐⭐
```python
@mcp.tool()
def get_stats(numbers: list) -> dict:
    """Get statistics for a list of numbers"""
    return {
        "min": min(numbers),
        "max": max(numbers),
        "avg": sum(numbers) / len(numbers),
        "count": len(numbers)
    }
```

### Challenge: Production-Ready Tools ⭐⭐⭐
```python
@mcp.tool()
def safe_calculate(operation: str, a: float, b: float) -> dict:
    """Perform safe calculation
    
    Args:
        operation: 'add', 'subtract', 'multiply', or 'divide'
        a, b: Operands
        
    Returns:
        Dictionary with result and metadata
    """
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
    else:
        raise ValueError(f"Unknown operation: {operation}")
    
    print(f"calculate: {operation}({a}, {b}) = {result}", file=sys.stderr)
    
    return {
        "operation": operation,
        "operands": [a, b],
        "result": result,
        "success": True
    }
```

---

## 🔗 Next Steps (Week 9)

Week 9 will introduce:
- **HTTP-based MCP Servers**
- **Running Uvicorn**
- **Website Agent** with multiple tools
- **Cloud-ready deployment**
- **Multiple client support**

---

## 🎓 Summary

**This Week You Mastered:**
- ✅ What is MCP and why it matters
- ✅ Client-Server architecture in AI
- ✅ Understanding stdio (stdout, stdin, stderr)
- ✅ Building MCP servers with FastMCP
- ✅ Tool design and type hints
- ✅ Async Python client development
- ✅ Running and testing MCP systems

**The Big Picture:**
```
Weeks 1-7: Learning to USE AI (prompts, chains, memory)
Week 8: Learning to GIVE HANDS to AI (tools & MCP)
Weeks 9-12: Building ADVANCED AI SYSTEMS (agents, workflows)
```

You're now learning the foundation of **modern agentic AI** - the exact pattern used by Claude, Cursor, and the next generation of AI applications.

---

## 📚 Quick Reference

### Creating Tools
```python
@mcp.tool()
def my_tool(param: int) -> str:
    """Tool description"""
    result = process(param)
    print(f"Log info", file=sys.stderr)  # ← Always stderr!
    return result
```

### Running
```bash
python simple_client.py  # Client starts server automatically
```

### Common Patterns
- **Simple function**: Return a single value
- **With defaults**: `param: str = "default"`
- **Error handling**: Raise exceptions, client sees them
- **Complex return**: Return dict or list

---

**Let's build amazing AI-powered applications! 🚀**

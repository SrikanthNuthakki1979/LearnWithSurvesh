# Week 11 - Multi-Agent Orchestration (Research Team) - Part 2

## 📚 Overview

This week continues the multi-agent orchestration journey from Week 10. We scale up from a simple routing pattern to a **6-specialist workflow** with external MCP servers. Instead of having all agents in one process, we now connect agents to remote MCP servers over HTTP, creating a truly distributed system.

**The Big Idea:** Build an intelligent research team where a supervisor decides which specialists to call, and those specialists execute tasks using dedicated MCP servers (math, research databases, time service, etc.).

## 🔗 How This Week Connects to Previous Weeks

### Week 8 (MCP Part 1) → Week 11
- Week 8 taught: MCP servers expose tools as remote services.
- You learned: How to connect a client to a single MCP server.
- Week 11 applies this: Multiple MCP servers powering multiple specialists.

### Week 9 (MCP Part 2) → Week 11
- Week 9 taught: One supervisor router + multiple tool endpoints.
- You learned: Dynamic routing based on question type.
- Week 11 advances it: Routing between specialist agents, which call MCP servers.

### Week 10 (Multi-Agent Orchestration Part 1) → Week 11
- Week 10 taught: Supervisor + specialists in one graph, no external servers.
- You learned: LangGraph, state machines, conditional routing.
- Week 11 enhances it: Same graph structure, but specialists communicate with remote MCP servers instead of local tools.

### Summary in One Line
Week 8 = one MCP server, Week 9 = multiple MCP servers + routing, Week 10 = multi-agent graph, Week 11 = multi-agent graph + MCP servers.

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                   USER QUESTION                         │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
        ┌──────────────────────────┐
        │  SUPERVISOR AGENT (LLM)  │
        │  "What type of query?    │
        │   Math? Research? None?" │
        └─────┬────────────────────┘
              │
      ┌───────┼────────┐
      │       │        │
      ▼       ▼        ▼
   ┌───────┐ ┌──────────────────────┐  ┌──────────────┐
   │ MATH  │ │ RESEARCH SPECIALIST  │  │ OUT-OF-SCOPE │
   │       │ │                      │  │              │
   │[MCP]  │ │ [MCP: RAG Server]    │  │ [No MCP]     │
   │ 8000  │ │      │               │  │              │
   │ 8001  │ │      ▼               │  │              │
   └───────┘ │ ANALYSIS SPECIALIST  │  │              │
      │      │                      │  │              │
      │      │ [MCP: Time Server]   │  │              │
      │      │      8002            │  │              │
      │      │      │               │  │              │
      │      │      ▼               │  │              │
      │      │ WRITER SPECIALIST    │  │              │
      │      │                      │  │              │
      │      │ [No MCP]             │  │              │
      │      └──────────┬───────────┘  │              │
      │                 │               │              │
      └─────────┬───────┴───────────────┴──────────────┘
                │
                ▼
      ┌────────────────────────┐
      │  FINAL RESPONSE AGENT  │
      │  "Format answer for    │
      │   user"                │
      └──────────┬─────────────┘
                 │
                 ▼
          ┌──────────────┐
          │ FINAL ANSWER │
          └──────────────┘
```

## 📊 What Each Specialist Does

| Specialist | Role | MCP Server | Input | Output | Why? |
|---|---|---|---|---|---|
| **Supervisor** | Classify question | ❌ LLM | User question | JSON decision | Route to right team |
| **Math Specialist** | Solve math problems | ✅ Ports 8000-8001 | Operation + numbers | Result | Deterministic math |
| **Research Specialist** | Query knowledge base | ✅ Port 8003 (RAG) | Question | Research findings | Access external data |
| **Analysis Specialist** | Add context | ✅ Port 8002 (Time) | Research findings | Analysis summary | Timestamp + enrich |
| **Writer Specialist** | Format report | ❌ None | Summary | Formatted report | Beautiful presentation |
| **Final Response** | Choose output | ❌ None | Math result OR report | Final answer | Deliver to user |

## 📖 Notebook Walkthrough (Step-by-Step)

### Step 1: Imports and Environment
**Purpose:** Load all required libraries and your OpenAI API key.

**What you import:**
- `dotenv` for env variables
- `asyncio` for async/await (MCP is asynchronous!)
- `json` for parsing supervisor's decision
- `LangGraph` components for the state machine
- `LangChain` message types for conversation history
- MCP client libraries for calling remote servers

**Key insight:** Notice we use `async` and `await` because MCP servers communicate over the network. Async allows us to call multiple servers concurrently.

**What you do:**
- Import all modules
- Call `load_dotenv()` to load `.env` file
- Verify `OPENAI_API_KEY` is accessible

### Step 2: Initialize the LLM
**Purpose:** Create the language model used by the Supervisor agent.

**Key insight:** ONLY the Supervisor uses the LLM. All other agents are deterministic (no LLM calls). Why? LLM calls are expensive. We use the LLM for the ONE decision point (routing), then let specialists execute that decision without thinking.

**What you do:**
- Create `ChatOpenAI(model="gpt-4o-mini", temperature=0)`
- `temperature=0` ensures consistent, deterministic routing
- Store in `llm` variable

### Step 3: MCP Configuration & Helper Functions
**Purpose:** Set up the connection infrastructure for all MCP servers.

**3a. MCP_SERVERS Dictionary**
Map tool names to their HTTP endpoints:
```python
MCP_SERVERS = {
    "add": "http://localhost:8000/sse",        # Addition server
    "multiply": "http://localhost:8001/sse",   # Multiplication server
    "time": "http://localhost:8002/sse",       # Current time server
    "rag": "http://localhost:8003/sse"         # Research RAG server
}
```

**Why these ports?** Each MCP server runs in a separate terminal listening on its own port. This simulates a real distributed system where services are independent.

**3b. extract_text_from_result(result) Function**
MCP servers return complex nested objects. This function extracts the readable text.
- Input: `result` object from MCP with `.content` attribute
- Process: Loop through content list, find text items
- Output: Clean string for display

**3c. async call_mcp_tool(server_url, tool_name, arguments) Function**
The core MCP client function that calls a remote tool:
1. Connect to MCP server via SSE (Server-Sent Events)
2. Initialize a ClientSession
3. Call the tool with arguments
4. Extract and return the result text

### Step 4: Implement 6 Specialist Agents
**Purpose:** Define the behavior of each specialist.

**Important:** All agents are async functions that take `state` and return modified `state`. This is the pattern:

```python
async def agent_name(state: OrchestratorState) -> OrchestratorState:
    # Read from state
    my_input = state.get("field_name")
    
    # Do work (maybe call MCP)
    result = await call_mcp_tool(...)
    
    # Write to state
    state["output_field"] = result
    
    # Return updated state
    return state
```

**Agent 1: supervisor_agent**
- Reads: User question from messages
- Does: Ask LLM what type of question (math/research/other)
- Returns: JSON with decision field set to "route_to_math", "route_to_research", or "cannot_help"
- Uses LLM: ✅ YES (this is the only thinking moment)

**Agent 2: math_specialist_agent**
- Reads: supervisor_decision from state
- Does: Call MCP math server (add or multiply) with parsed arguments
- Returns: math_result field in state
- Uses MCP: ✅ YES (ports 8000-8001)

**Agent 3: research_specialist_agent**
- Reads: User's original question from messages
- Does: Call MCP RAG server to search knowledge base
- Returns: research_result field in state
- Uses MCP: ✅ YES (port 8003)

**Agent 4: analysis_specialist_agent**
- Reads: research_result from previous agent
- Does: Call MCP time server to get timestamp, combine with research
- Returns: analysis_summary field in state
- Uses MCP: ✅ YES (port 8002)

**Agent 5: writer_specialist_agent**
- Reads: analysis_summary from previous agent
- Does: Format with nice borders, headers, sections
- Returns: report field in state
- Uses MCP: ❌ NO (just formatting)
- **Teaching point:** Not all agents need external services!

**Agent 6: final_response_agent**
- Reads: Either math_result OR report (whichever was computed)
- Does: Choose which to return based on what was completed
- Returns: final_answer field in state
- Uses MCP: ❌ NO (just selection logic)

### Step 5: State Definition & Routing Logic
**Purpose:** Define the shared state (clipboard) and how decisions route between agents.

**5a. OrchestratorState Class**
This is the "clipboard" all agents share. It extends `MessagesState`:

| Field | Type | Meaning |
|-------|------|---------|
| `messages` | List[BaseMessage] | Conversation history (inherited) |
| `supervisor_decision` | dict | Supervisor's classification result |
| `math_result` | Any | Output from math specialist |
| `research_result` | str | Output from research specialist |
| `analysis_summary` | str | Output from analysis specialist |
| `report` | str | Output from writer specialist |
| `final_answer` | str | Final answer to return to user |

**5b. route_after_supervisor Function**
Determines which agent runs after the supervisor:
```python
def route_after_supervisor(state: OrchestratorState) -> str:
    decision = state['supervisor_decision']['decision']
    if decision == 'route_to_math':
        return 'math_specialist'
    elif decision == 'route_to_research':
        return 'research_specialist'
    else:
        return 'final_response'
```

**Why?** LangGraph needs explicit routing functions. This makes the decision logic testable and transparent.

### Step 6: Build the Orchestrator (LangGraph)
**Purpose:** Wire all agents together into a graph.

**The flow:**
```
START
  │
  ▼
Supervisor (LLM decides route)
  │
  ├─► Math path:          research path:
  │   Math Specialist    ► Research Specialist
  │        │                     │
  │        └─────────────────────┘
  │                    │
  │         ┌──────────┴─────────┐
  │         │                    │
  └─────── Analysis Specialist   │
  │              │               │
  │              ▼               │
  │         Writer Specialist    │
  │              │               │
  └──────────────┴───────────────┘
                 │
                 ▼
            Final Response
                 │
                 ▼
                 END
```

**What you do:**
1. Create `StateGraph(OrchestratorState)`
2. Add nodes for all 6 agents
3. Set Supervisor as entry point
4. Add conditional edges from Supervisor (routes to 3 paths)
5. Connect sequential edges (specialist chains)
6. Set Final Response as finish point
7. Compile the graph

**Key LangGraph concepts:**
- **Nodes:** Agent functions that process state
- **Edges:** "After this node finishes, go to that node"
- **Conditional Edges:** "Choose next node based on state"
- **Entry Point:** Where graph execution starts
- **Finish Point:** Where graph execution ends

### Step 7: Run Tests & See Everything Work!
**Purpose:** Test the complete workflow with multiple question types.

**Test Cases:**

| Question | Type | Expected Path | Expected Result |
|----------|------|---|---|
| "What is 5 plus 3?" | Math | supervisor → math → final | "The answer is 8" |
| "Multiply 7 and 6" | Math | supervisor → math → final | "The answer is 42" |
| "What is machine learning?" | Research | supervisor → research → analysis → writer → final | Formatted report |
| "What's your favorite color?" | Out-of-scope | supervisor → final | "I cannot help with that" |

**What you implement:**
```python
async def run_orchestrator(user_question: str):
    app = build_orchestrator()
    initial_state = OrchestratorState(
        messages=[HumanMessage(content=user_question)]
    )
    final_state = await app.ainvoke(initial_state)
    return final_state["final_answer"]
```

**What you'll see in terminal:**
```
============================================================================
📢 Question: What is 5 plus 3?
============================================================================
🎯 SUPERVISOR: Analyzing question...
   Decision: route_to_math
🧮 MATH SPECIALIST: Calling MCP math server port 8000...
   Tool: add_numbers
   Parameters: {'a': 5, 'b': 3}
   Result: 8
📝 FINAL RESPONSE: Formatting answer...
============================================================================
✅ Final Answer: The answer is 8
============================================================================
```

## 🚀 Quick Start

### 1. Prerequisites: Start MCP Servers

**IMPORTANT:** These servers must be running BEFORE you start the notebook. Open 4 separate terminals.

**Terminal 1:**
```bash
python 1_add_numbers_server.py
# Output: Listening on http://localhost:8000
```

**Terminal 2:**
```bash
python 2_multiply_numbers_server.py
# Output: Listening on http://localhost:8001
```

**Terminal 3:**
```bash
python 3_get_current_time_server.py
# Output: Listening on http://localhost:8002
```

**Terminal 4:**
```bash
python 4_rag_server.py
# Output: Listening on http://localhost:8003
```

**Verify:** Each terminal shows "Listening on http://localhost:XXXX"

**Why separate terminals?** In production, these are separate microservices. Separate terminals simulate that architecture.

### 2. Environment Setup

Create a `.env` file in this folder:
```
OPENAI_API_KEY=your_openai_api_key_here
```

Get your key: https://platform.openai.com/api-keys

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Notebook

Open `Week11_Student_Notebook.ipynb` in VS Code or Jupyter and follow the 7 steps, filling in TODOs as you go.

## 📚 Key Learning Objectives

By completing this week, you will:

- ✅ Understand async/await for network I/O
- ✅ Connect agents to external MCP servers over HTTP
- ✅ Build a 6-specialist workflow with conditional routing
- ✅ Design state machines for complex agent orchestration
- ✅ Use MCP in production-like distributed architecture
- ✅ Test multi-agent systems with diverse question types

## 🔧 Common Issues & Fixes

### "Connection refused" Error
**Problem:** MCP server is not running.
**Fix:** Check that all 4 servers are started in separate terminals and show "Listening on..." messages.

### "Supervisor decision parsing fails"
**Problem:** LLM returned invalid JSON.
**Fix:** Add error handling in supervisor_agent to validate JSON format.

### "Async errors"
**Problem:** Mixing `await` and non-async code.
**Fix:** Ensure all agents are `async def`, use `await` inside agents, and call with `await run_orchestrator()`.

### "State field is None"
**Problem:** Reading from state before it was written.
**Fix:** Check agent order in graph; ensure dependencies run before dependent agents.

## 📁 Files in This Folder

```
Week 11 Multi-Agent Orchestration (Research Team) - Part2/
├── Week11_Student_Notebook.ipynb      # Main notebook with 7 steps + TODOs
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
├── 1_add_numbers_server.py            # MCP server for addition
├── 2_multiply_numbers_server.py       # MCP server for multiplication
├── 3_get_current_time_server.py       # MCP server for timestamp
└── 4_rag_server.py                    # MCP server for research/RAG
```

## 🎯 Success Criteria

You've completed Week 11 when:

- [ ] All 4 MCP servers start and show "Listening" messages
- [ ] `.env` file has your OpenAI API key
- [ ] You implement all 7 steps in the notebook
- [ ] All 4 test questions produce the expected outputs
- [ ] You understand the flow from supervisor → specialists → final response
- [ ] You can explain why we use async/await for MCP calls

## 🔗 Still Stuck?

1. **Reference the Master Notebook** (Week 10 part 2) - it has full implementations
2. **Check console output** - MCP servers print requests as they arrive
3. **Review the hints** in each TODO cell
4. **Print state** at each step: `print(json.dumps(state, indent=2, default=str))`
5. **Test incrementally** - implement one agent, test it, move to the next

## 📚 Related Weeks

- **Week 8:** MCP servers (foundation)
- **Week 9:** Routing with MCP (introduction to routing)
- **Week 10:** Multi-agent graphs (state machines)
- **Week 11:** Multi-agent + MCP (this week)
- **Week 12:** Local knowledge assistant (applying to real domain)

---

**Happy building! 🚀**

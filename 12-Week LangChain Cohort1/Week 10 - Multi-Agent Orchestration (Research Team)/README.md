# Week 10 - Multi-Agent Orchestration (Research Team)

This README is written like student notes for the Phase 1 notebook. It explains each part in plain language and connects the ideas from Week 8 and Week 9 to Week 10.

## Big Picture (Why This Week Matters)
We move from tool calling (Weeks 8 and 9) to a structured multi-agent workflow. Instead of a single client deciding which tool to call, we build a mini team of agents connected by a graph. The key learning goal is: **routing + shared state + deterministic tools** inside a single, testable workflow.

## How Week 8 and Week 9 Flow Into Week 10

### Week 8 (MCP Part 1) -> Week 10
- Week 8 taught: tools are callable capabilities exposed by a server.
- You learned: a client asks for tools and calls them with arguments.
- Week 10 keeps the tool-calling idea but embeds it inside a graph of agents (no separate MCP client needed for the demo).

### Week 9 (MCP Part 2) -> Week 10
- Week 9 taught: multiple specialized servers and an LLM router.
- The router decides which server handles the task.
- Week 10 mirrors that idea inside one workflow:
  - Supervisor agent = router
  - Specialist agent = tool executor
  - Graph edges = routing rules

### Summary in One Line
Week 8 = one tool server, Week 9 = multiple tool servers + routing, Week 10 = one graph with multiple agents + routing.

## What You Build Here
- A **supervisor agent** that decides where to route a question.
- A **math specialist agent** that uses deterministic tools.
- A **final response agent** that formats the answer for the user.
- A **LangGraph state machine** that wires the agents together.

## Notebook Walkthrough (Student Notes)

### Section 1: Imports
Purpose: bring in LangGraph, LangChain message types, and environment setup.

Key ideas:
- `load_dotenv()` loads your `OPENAI_API_KEY`.
- `StateGraph` and `MessagesState` build the graph and shared memory.
- `HumanMessage`, `AIMessage`, `ToolMessage` are standardized message objects.

What you should do:
- Import all missing modules.
- Call `load_dotenv()` once.

### Section 2: LLM (Supervisor Only)
Purpose: only the supervisor agent should use the LLM for routing.

Key ideas:
- The LLM does not solve math, it just decides the route.
- `temperature=0` makes routing deterministic.

What you should do:
- Create `llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)`.

### Section 3: Math Tools
Purpose: make simple, deterministic tools (no LLM).

Key ideas:
- Tools should be pure functions with no side effects.
- The specialist agent will call these tools.

What you should do:
- Implement `add_numbers(a, b)`.
- Implement `multiply_numbers(a, b)`.
- Store them in `MATH_TOOLS`.

### Section 4: Agents
Purpose: define the actual agent behaviors.

Key ideas:
- Each agent reads from `state`, updates it, and returns it.
- The `state` is just a dictionary with shared fields.

What you should do:
1. **Supervisor agent**
   - Reads the user question from `messages`.
   - Calls the LLM with a routing prompt.
   - Parses a JSON decision (for example: `{"route": "math"}`).
   - Writes `supervisor_decision` and a new message to state.

2. **Math specialist agent**
   - Reads `supervisor_decision` and selects a tool.
   - Calls the tool with parsed arguments.
   - Writes `math_result` and a `ToolMessage` to state.

3. **Final response agent**
   - Reads `math_result`.
   - Formats a clean, final answer for the user.
   - Writes `final_answer` to state.

### Section 5: State and Routing
Purpose: define shared state and route decisions.

Key ideas:
- `MessagesState` ensures message history is preserved.
- `OrchestratorState` holds all extra fields we care about.
- `route_after_supervisor()` decides which agent runs next.

What you should do:
- Define `OrchestratorState` with fields:
  - `supervisor_decision`
  - `next_agent`
  - `math_result`
  - `final_answer`
- Implement `route_after_supervisor(state)`:
  - If route is math -> go to `math_specialist`.
  - Else -> go to `final_response`.

### Section 6: Build and Run
Purpose: wire the graph, run a test.

Key ideas:
- Graph nodes are the agent functions.
- Entry point is the supervisor.
- End point is the final response.

What you should do:
- Build the graph in `build_orchestrator()`.
- Implement `run_orchestrator(question)`.
- Test with three questions (mix math and non-math).

## Common Pitfalls (Quick Fixes)
- If routing fails, check JSON parsing in the supervisor.
- If tools do not run, verify `MATH_TOOLS` keys match the route.
- If nothing prints, make sure you are returning updated `state`.

## Requirements
- Python 3.10+ recommended.
- OpenAI API key in `.env`.
- Dependencies: LangGraph, LangChain, OpenAI.

## Getting Started
1. Open Phase1_Student_Notebook.ipynb.
2. Run cells in order, fill in TODOs.
3. Test with a few questions once the graph is built.

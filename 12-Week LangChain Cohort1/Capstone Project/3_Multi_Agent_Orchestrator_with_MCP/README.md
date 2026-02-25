# Multi-Agent Orchestrator with MCP

## Objective
Build a supervisor-driven multi-agent workflow using LangGraph, specialist agents, and MCP-style external tool integrations.

## Week Alignment
- Week 10: Multi-agent orchestration pattern (supervisor + specialists)
- Week 11: Tooling and external service integration (MCP-style adapters)
- Week 12: End-to-end capstone integration, testing, and demo

## Learning Outcomes
- Model workflows as graph state transitions
- Route user intent to specialist agents
- Integrate external tools through adapter clients
- Compose a final response from specialist outputs

## Project Format
- This repository is a starter skeleton.
- Core files include TODO blocks for implementation.
- Focus on routing quality, resilience, and clear orchestration.

## MVP Scope
- Supervisor route decision implemented
- At least two specialists (Math and RAG)
- MCP-style external tool call path
- End-to-end query to final answer flow

## Prerequisites
- Python environment ready
- Dependencies installed from requirements.txt
- .env created from .env.example

## Implementation Phases
1. State: Define and extend src/state/agent_state.py
2. Routing: Implement src/agents/supervisor_agent.py
3. Specialists: Implement src/agents/math_agent.py and src/agents/rag_agent.py
4. External Tools: Implement src/mcp_clients/mcp_tool_client.py and src/tools/tool_router.py
5. Graph: Build orchestration in src/graph/orchestrator_graph.py
6. Run: Add query and execute from src/main.py

## Deliverables
- Working orchestrator run via python -m src.main
- Route-based specialist execution
- Final response composed from specialist/tool outputs
- Completed TODOs in all core modules

## Presentation Checklist
- Show query and selected route from supervisor
- Show specialist/tool output produced
- Show final composed answer
- Explain one failure case and fallback handling

## Folder Map
- data/kb_docs: optional docs for RAG specialist
- src/state: graph state contract
- src/agents: supervisor and specialist nodes
- src/mcp_clients: external MCP-style adapters
- src/tools: local/external tool routing
- src/graph: LangGraph assembly and execution
- tests: student validation tasks

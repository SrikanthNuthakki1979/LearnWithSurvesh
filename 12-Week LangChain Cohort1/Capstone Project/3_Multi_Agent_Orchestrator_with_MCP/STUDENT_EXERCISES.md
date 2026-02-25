# Student Exercises — Multi-Agent Orchestrator with MCP

## Core Tasks
- [ ] Define/extend graph state in `src/state/agent_state.py`
- [ ] Implement route logic in `src/agents/supervisor_agent.py`
- [ ] Implement `math_node` in `src/agents/math_agent.py`
- [ ] Implement `rag_node` in `src/agents/rag_agent.py`
- [ ] Implement MCP call adapter in `src/mcp_clients/mcp_tool_client.py`
- [ ] Implement tool routing in `src/tools/tool_router.py`
- [ ] Build orchestration graph in `src/graph/orchestrator_graph.py`
- [ ] Set query and run flow in `src/main.py`

## Validation Targets
- [ ] Supervisor chooses at least one specialist route correctly
- [ ] Final answer is composed from specialist output
- [ ] Unknown queries gracefully fallback
- [ ] App runs from single command

## Try-It Areas
1. Add retry/fallback when MCP tool call fails
2. Add route confidence score from supervisor
3. Add multi-step route (e.g., rag then math)
4. Add response citations/source traces

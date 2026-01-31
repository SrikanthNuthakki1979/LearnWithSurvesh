# Week 9 - Multi-Server MCP Exercise

## 🎯 Start Here!

**👉 Open `00_START_HERE.txt` first!** It has everything you need.

## 📁 Your 8 Files (In Order)

| File | What It Does |
|------|-------------|
| **00_START_HERE.txt** | 5-step guide to get running ⭐ **READ THIS FIRST** |
| **01_add_numbers_server_TODO.py** | First server (Easy) - Addition |
| **02_multiply_numbers_server_TODO.py** | Second server (Easy) - Multiplication |
| **03_get_current_time_server_TODO.py** | Third server (Medium) - Time service |
| **04_rag_server_TODO.py** | Fourth server (Advanced) - Learn from websites |
| **05_QUICK_REFERENCE.txt** | Commands cheat sheet - reference while working |
| **06_TROUBLESHOOTING.txt** | Error solutions - read if you get stuck |
| **07_CHECKLIST.txt** | Completion tracker - verify when done |

## ⚙️ System Requirements

### Recommended Python Versions
For best compatibility with MCP and all dependencies:

- ✅ **Python 3.10** - Best compatibility
- ✅ **Python 3.11** - Excellent compatibility
- ✅ **Python 3.12** - Good compatibility
- ⚠️ **Python 3.13** - May have issues with some packages, use 3.10-3.12 instead

**Check your Python version:**
```bash
python --version
```

---

## ⚡ Quick Start

1. **Activate venv:**
   ```powershell
   cd "<your path>"
   & .venv\Scripts\Activate.ps1
   ```

2. **Install dependencies:**
   ```powershell
   pip install mcp langchain langchain-openai langchain-community chromadb beautifulsoup4 python-dotenv
   ```

3. **Create .env file:**
   ```
   OPENAI_API_KEY=sk-YOUR_KEY_HERE
   ```

4. **Read 00_START_HERE.txt** and follow the 5 steps!

## 🎓 What You'll Learn

- Create MCP servers with FastMCP
- Define tools with @mcp.tool() decorator
- Run multiple servers on different ports
- Route requests using LLM decision-making
- Build RAG systems with LangChain
- Work with vector databases (Chroma)

## 🏗️ Architecture (How It All Works)

```
                    🎤 USER QUESTION
                          |
                          ↓
              ┌─────────────────────────┐
              │  MULTI_SERVER_CLIENT    │
              │  (Smart Router)         │
              │  Uses LLM to decide     │
              └────────┬────────────────┘
                       |
       ┌───────────────┼───────────────┬────────────┐
       ↓               ↓               ↓            ↓
   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
   │ Port    │   │ Port    │   │ Port    │   │ Port    │
   │ 8000    │   │ 8001    │   │ 8002    │   │ 8003    │
   │         │   │         │   │         │   │         │
   │ Add     │   │ Multiply│   │ Time    │   │ RAG     │
   │ Numbers │   │ Numbers │   │ Service │   │ Learn & │
   │         │   │         │   │         │   │ Answer  │
   └─────────┘   └─────────┘   └─────────┘   └─────────┘
```

**Example Flow:**
1. User asks: "What is 5 plus 3?"
2. Client thinks: "This is addition → use port 8000"
3. Server 1 calculates: 5 + 3 = 8
4. Client returns: "The answer is 8"

## 📊 Week 8 vs Week 9 - What Changed?

| Aspect | Week 8 (Simple) | Week 9 (Advanced) |
|--------|-----------------|-------------------|
| **Servers** | 1 server (simple_server.py) | 4 servers (specialized) |
| **Transport** | stdio (pipe-based) | HTTP/SSE (web-based) |
| **Ports** | None (single process) | 8000-8003 (4 processes) |
| **Architecture** | Monolithic | Microservices |
| **Scalability** | Local only | Can run on different computers |
| **Routing** | Direct calls | LLM decides which server to use |
| **Complexity** | Beginner-friendly | Production-ready |
| **Real-World Use** | Learning | Netflix, Amazon, Google use this! |

**Why the upgrade?**
- Week 8: Learn the basics (one simple server)
- Week 9: Build production systems (multiple specialized servers)

## 💡 Key Concepts

- **Server 1-3:** Fixed logic (math and time)
- **Server 4:** Learning system (learns from websites, answers questions)
- **Client:** Smart router that decides which server to use
- **Microservices:** Each server does ONE thing well
- **HTTP/SSE:** Industry-standard communication (like websites)

## ❓ Got Questions?

Check **06_TROUBLESHOOTING.txt** - it has solutions for all common errors!

---

**Good luck! 🚀** Start with `00_START_HERE.txt`

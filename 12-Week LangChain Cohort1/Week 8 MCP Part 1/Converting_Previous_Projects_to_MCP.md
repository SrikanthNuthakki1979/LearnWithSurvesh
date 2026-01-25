# Converting Previous Projects to MCP Servers 🚀

## The Big Picture

All the complex applications you built in previous weeks (PDF Summarizer, RAG, Email Assistant, etc.) can be **wrapped as MCP servers** to make them:
- ✅ Reusable by multiple agents
- ✅ Accessible through a standardized protocol
- ✅ Composable (combine multiple servers together)
- ✅ Production-ready for deployment

---

## Architecture: From Application → MCP Server

### Before (Week 4 - PDF Summarizer as Standalone)
```
User Input
    ↓
PDF Summarizer (Jupyter Notebook)
    ↓
Output (summary)
```

### After (PDF Summarizer as MCP Server)
```
AI Agent or User
    ↓
MCP Client
    ↓
MCP Server (PDF Summarizer)
    ├── Tool 1: summarize_pdf()
    ├── Tool 2: extract_text()
    └── Tool 3: answer_question_on_pdf()
    ↓
Output
```

---

## Key Conversion Steps

### Step 1: Identify Your Core Functions
Take your existing application logic and extract the **core functions** that should become MCP tools.

**Week 4 PDF Summarizer → MCP Tools:**
- `summarize_pdf(file_path: str) -> str` - Summarize entire PDF
- `extract_text_from_pdf(file_path: str) -> str` - Extract raw text
- `answer_question_on_pdf(file_path: str, question: str) -> str` - RAG query
- `get_pdf_metadata(file_path: str) -> dict` - Get PDF info (pages, title, etc.)

**Week 5 Email Assistant → MCP Tools:**
- `draft_email(topic: str, tone: str) -> str`
- `improve_email(draft: str) -> str`
- `classify_email_sentiment(email: str) -> str`

**Week 6 YouTube Transcript → MCP Tools:**
- `get_transcript(youtube_url: str) -> str`
- `summarize_transcript(url: str) -> str`
- `extract_topics_from_transcript(url: str) -> list`

### Step 2: Extract the Logic
Move the heavy lifting out of Jupyter notebooks into reusable Python functions.

```python
# Before: In a Jupyter notebook cell
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain

def summarize_pdf_logic(file_path, temperature=0.3):
    """Existing logic from Week 4"""
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    llm = ChatOpenAI(temperature=temperature, model="gpt-4")
    chain = load_summarize_chain(llm, chain_type="stuff")
    return chain.run(docs)

# After: Becomes an MCP tool
@mcp.tool()
def summarize_pdf(file_path: str, temperature: float = 0.3) -> str:
    """
    Summarize a PDF file using LangChain RAG.
    
    Args:
        file_path: Path to the PDF file
        temperature: LLM temperature (0.0-1.0)
    
    Returns:
        Summary of the PDF
    """
    return summarize_pdf_logic(file_path, temperature)
```

### Step 3: Wrap in MCP Server
Create an MCP server that exposes all tools for your application.

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("PDF Analyzer & Summarizer")

# Tool 1: Basic Summarization
@mcp.tool()
def summarize_pdf(file_path: str) -> str:
    """Summarize an entire PDF file"""
    # ... your Week 4 logic here

# Tool 2: Extract Text
@mcp.tool()
def extract_text_from_pdf(file_path: str) -> str:
    """Extract all text from a PDF"""
    # ... your extraction logic

# Tool 3: RAG Query
@mcp.tool()
def answer_question_on_pdf(file_path: str, question: str) -> str:
    """Ask questions about PDF content using RAG"""
    # ... your Week 4 RAG logic

# Tool 4: Metadata
@mcp.tool()
def get_pdf_metadata(file_path: str) -> str:
    """Get PDF metadata (pages, title, author, etc.)"""
    # ... your metadata extraction logic

if __name__ == "__main__":
    mcp.run()
```

---

## Real-World Benefits

### 1. Compose Multiple Servers
```python
# A smart agent that uses multiple services:
async def smart_workflow():
    async with ClientSession() as session:
        # Use PDF server
        pdf_summary = await session.call_tool(
            "summarize_pdf", 
            arguments={"file_path": "report.pdf"}
        )
        
        # Use Email server
        email = await session.call_tool(
            "draft_email",
            arguments={"topic": pdf_summary, "tone": "professional"}
        )
        
        # Use YouTube server
        transcript = await session.call_tool(
            "get_transcript",
            arguments={"youtube_url": "https://youtube.com/..."}
        )
        
        return {"summary": pdf_summary, "email": email, "transcript": transcript}
```

### 2. Remote Access
MCP servers can run on servers (using HTTP transport) and be called from anywhere:
```
Client Machine          Server Machine
   │                         │
   └─────────── HTTP ────────┤
                              │
                         PDF Server (running)
                         Email Server (running)
                         YouTube Server (running)
```

### 3. Parallel Processing
Call multiple tools simultaneously:
```python
# All run in parallel!
results = await asyncio.gather(
    session.call_tool("summarize_pdf", arguments={"file_path": "doc1.pdf"}),
    session.call_tool("summarize_pdf", arguments={"file_path": "doc2.pdf"}),
    session.call_tool("summarize_pdf", arguments={"file_path": "doc3.pdf"}),
)
```

---

## Migration Checklist

### Phase 1: Extract Core Logic
- [ ] Identify all functions in your Jupyter notebook
- [ ] Create a `core_functions.py` with reusable logic
- [ ] Remove all notebook-specific code (%%writefile, display(), etc.)
- [ ] Test functions work independently

### Phase 2: Create MCP Server
- [ ] Create `server.py` with FastMCP setup
- [ ] Add each function as `@mcp.tool()`
- [ ] Add type hints and docstrings
- [ ] Test server works standalone

### Phase 3: Create Client
- [ ] Create `client.py` to test the server
- [ ] Test all tools work correctly
- [ ] Verify error handling works

### Phase 4: Deploy
- [ ] Consider using HTTP transport for production
- [ ] Add logging and monitoring
- [ ] Document the server's tools
- [ ] Share with other users/agents

---

## Example: PDF Summarizer → MCP Server

### Original (Week 4 Notebook Cell)
```python
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain

def process_pdf(file_path):
    # Load PDF
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    
    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    split_docs = splitter.split_documents(docs)
    
    # Summarize
    llm = ChatOpenAI(temperature=0.3, model="gpt-4")
    chain = load_summarize_chain(llm, chain_type="stuff")
    summary = chain.run(split_docs)
    
    return summary
```

### Converted (MCP Server)
```python
# pdf_summarizer_server.py
from mcp.server.fastmcp import FastMCP
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
import sys

mcp = FastMCP("PDF Summarizer Server")

@mcp.tool()
def summarize_pdf(file_path: str, chunk_size: int = 1000) -> str:
    """
    Summarize a PDF file using LangChain.
    
    Args:
        file_path: Path to the PDF file
        chunk_size: Text chunk size for splitting
    
    Returns:
        Summary of the PDF content
    """
    try:
        # Load PDF
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        print(f"Loaded {len(docs)} pages from {file_path}", file=sys.stderr)
        
        # Split text
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=200
        )
        split_docs = splitter.split_documents(docs)
        print(f"Split into {len(split_docs)} chunks", file=sys.stderr)
        
        # Summarize
        llm = ChatOpenAI(temperature=0.3, model="gpt-4")
        chain = load_summarize_chain(llm, chain_type="stuff")
        summary = chain.run(split_docs)
        
        print(f"Generated summary", file=sys.stderr)
        return summary
        
    except Exception as e:
        raise ValueError(f"Failed to summarize PDF: {str(e)}")

@mcp.tool()
def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract all text from a PDF file.
    
    Args:
        file_path: Path to the PDF file
    
    Returns:
        Raw text from the PDF
    """
    try:
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        text = "\n".join([doc.page_content for doc in docs])
        return text
    except Exception as e:
        raise ValueError(f"Failed to extract text: {str(e)}")

@mcp.tool()
def answer_question_on_pdf(file_path: str, question: str) -> str:
    """
    Answer a question about PDF content using RAG.
    
    Args:
        file_path: Path to the PDF file
        question: Question to answer
    
    Returns:
        Answer based on PDF content
    """
    try:
        from langchain_openai import OpenAIEmbeddings
        from langchain_community.vectorstores import FAISS
        from langchain.chains.qa_with_sources import load_qa_with_sources_chain
        
        # Load and process PDF
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        
        # Create embeddings and vector store
        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.from_documents(docs, embeddings)
        
        # Search and answer
        llm = ChatOpenAI(temperature=0, model="gpt-4")
        chain = load_qa_with_sources_chain(llm)
        
        answer = chain.run(
            input_documents=docs,
            question=question
        )
        
        return answer
        
    except Exception as e:
        raise ValueError(f"Failed to answer question: {str(e)}")

if __name__ == "__main__":
    print("Starting PDF Summarizer MCP Server...", file=sys.stderr)
    mcp.run()
```

### Client to Use the Server
```python
# pdf_summarizer_client.py
import asyncio
import subprocess
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters

async def test_pdf_server():
    """Test the PDF summarizer server"""
    
    # Start server
    server_params = StdioServerParameters(
        command="python",
        args=["pdf_summarizer_server.py"]
    )
    
    async with ClientSession(server_params) as session:
        # Test 1: Summarize PDF
        print("Testing summarize_pdf tool...")
        result = await session.call_tool(
            "summarize_pdf",
            arguments={"file_path": "sample.pdf"}
        )
        print(f"Summary:\n{result.content[0].text}\n")
        
        # Test 2: Extract text
        print("Testing extract_text_from_pdf tool...")
        result = await session.call_tool(
            "extract_text_from_pdf",
            arguments={"file_path": "sample.pdf"}
        )
        print(f"Text (first 500 chars):\n{result.content[0].text[:500]}\n")
        
        # Test 3: RAG query
        print("Testing answer_question_on_pdf tool...")
        result = await session.call_tool(
            "answer_question_on_pdf",
            arguments={
                "file_path": "sample.pdf",
                "question": "What is the main topic of this document?"
            }
        )
        print(f"Answer:\n{result.content[0].text}")

if __name__ == "__main__":
    asyncio.run(test_pdf_server())
```

---

## Projects Perfect for MCP Conversion

| Project | Week | Potential MCP Tools |
|---------|------|-------------------|
| PDF Summarizer | 4 | summarize_pdf, extract_text, answer_question, get_metadata |
| Email Assistant | 5 | draft_email, improve_email, classify_sentiment |
| YouTube Summarizer | 6 | get_transcript, summarize_transcript, extract_topics |
| Support Chatbot | 7 | answer_support_question, classify_issue, suggest_solution |
| Job Agent | 9 | recommend_jobs, match_profile, score_candidate |
| Meeting Notes | 10 | generate_notes, extract_action_items, summarize_discussion |
| Travel Planner | 11 | plan_itinerary, find_hotels, suggest_restaurants |
| Local Knowledge | 12 | search_local_data, answer_local_question |

---

## Next Steps

1. **Pick a project** - Start with Week 4 PDF Summarizer or Week 5 Email Assistant
2. **Extract the logic** - Move Jupyter cells to Python functions
3. **Create MCP server** - Wrap functions with `@mcp.tool()` decorators
4. **Test with client** - Create a client notebook to verify all tools work
5. **Share the server** - Other students/agents can now use your tools!

---

## Key Takeaway

**MCP is the "glue" that connects all your AI projects into a unified system.**

Instead of building isolated Jupyter notebooks, you're building reusable, composable services that work together. This is how production AI systems are built! 🎯

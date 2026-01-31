# Week 7: Customer Support Chatbot 🤖💬

## 📋 Overview

A production-ready **Retrieval-Augmented Generation (RAG)** chatbot designed for customer support that intelligently answers frequently asked questions. This project demonstrates how to build a semantic search-powered FAQ system using LangChain, OpenAI embeddings, and Chroma vector database—essential skills for creating AI-powered customer service solutions.

## 🎯 Why Learn This?

### Real-World Impact
Customer support chatbots are transforming how businesses interact with customers:
- **24/7 Availability**: Instant answers to common questions without human intervention
- **Cost Reduction**: Reduces support ticket volume by 30-50% in real deployments
- **Scalability**: Handle thousands of simultaneous queries without additional staff
- **Consistency**: Provides accurate, uniform answers based on verified knowledge base

### Essential Skills You'll Master
1. **RAG Architecture**: The foundation of modern AI applications (ChatGPT plugins, enterprise AI assistants)
2. **Vector Databases**: Critical for semantic search in production AI systems
3. **Embeddings**: Understanding how AI represents and searches text meaning
4. **Persistent Storage**: Building systems that survive restarts and scale to production
5. **Conversation Memory**: Three strategies (Buffer, Window, Summary) for managing multi-turn conversations
6. **Prompt Engineering**: Crafting prompts that control AI behavior in customer-facing scenarios

### Career Relevance
- RAG is the #1 pattern for enterprise AI applications in 2025
- Vector databases (Chroma, Pinecone, Weaviate) are standard in AI job descriptions
- Customer service automation is a multi-billion dollar market

This project gives you hands-on experience with the exact architecture used by companies like Intercom, Zendesk, and Freshdesk in their AI assistants.

## ✨ Features

- **Smart FAQ Retrieval**: Semantic search finds relevant answers even with different wording
- **500-Row Dataset**: Realistic customer support scenarios with metadata (region, channel, issue type)
- **Persistent Vector Store**: Chroma database that survives kernel restarts
- **Production-Ready RAG Pipeline**: Retriever → Prompt → LLM → Response
- **Metadata Support**: Filter by region, channel, or issue type for targeted responses
- **No Chunking Required**: Optimized for small, coherent FAQ documents (see detailed explanation in notebook)
- **Conversation Memory**: Three memory strategies (Buffer, Window, Summary) for multi-turn chats
- **Cost Optimization**: Choose memory strategy based on conversation length and budget
- **Session Management**: Support multiple concurrent user conversations
- **LangSmith Integration**: Optional tracing for debugging and monitoring

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- OpenAI API key (required for embeddings and LLM)
- `.env` file in project root with `OPENAI_API_KEY=your_key_here`
- **Note**: The FAQ dataset (`customer_support_faq.csv`) is already provided in the project root

### 📦 Install Dependencies

All required packages are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt
```

### 📦 Required Packages Breakdown

**`requirements.txt` contains:**

| Package | Version | Purpose |
|---------|---------|---------|
| `langchain` | 1.0.8 | Core LangChain framework for building LLM applications |
| `langchain-openai` | 1.0.3 | OpenAI integration (ChatGPT, embeddings) |
| `langchain-community` | 0.4.1 | Community tools including Chroma vector store |
| `langchain-core` | 1.0.7 | Core abstractions (Documents, Prompts, Chains) |
| `python-dotenv` | 1.2.1 | Load environment variables from `.env` file |
| `pandas` | 2.3.2 | Load and manipulate CSV data |
| `chromadb` | 1.3.5 | Persistent vector database for embeddings |
| `openai` | 2.6.0 | OpenAI Python SDK |

### 🔑 Environment Setup

**Step 1: Get Your OpenAI API Key**

1. Visit https://platform.openai.com/api-keys
2. Create a new secret key
3. Copy the key (starts with `sk-...`)

**Step 2: Create `.env` File**

Create a `.env` file in the `Week 7 Customer Support Chatbot/` directory:

```env
OPENAI_API_KEY=sk-your-key-here
```

**Optional (Recommended): Enable LangSmith Tracing** (for debugging and monitoring)

```env
OPENAI_API_KEY=sk-your-key-here
LANGSMITH_API_KEY=lsv2_your-key-here
LANGCHAIN_PROJECT=CUSTOMER_SUPPORT_PROJECT
```

**Note**: The notebook enables LangSmith tracing by default. If you don't have a LangSmith account, it will still work but won't trace to the dashboard.

**Step 3: Dataset Ready to Use**

The FAQ dataset is already provided as `customer_support_faq.csv` in the project root with 500 realistic customer support questions and answers. No generation script is needed—you can proceed directly to the notebook.

## 📚 Learning Objectives

By the end of this week, you will be able to:

- ✅ Understand RAG (Retrieval-Augmented Generation) architecture
- ✅ Build semantic search systems using embeddings
- ✅ Work with vector databases (Chroma) for persistent storage
- ✅ Understand when to chunk vs when to keep documents whole
- ✅ Create production-ready LangChain chains with LCEL
- ✅ Use metadata filtering in retrieval systems
- ✅ Debug and optimize RAG pipelines
- ✅ Deploy AI systems that survive restarts (persistence)
- ✅ Implement conversation memory in chatbots
- ✅ Compare and choose memory strategies (Buffer, Window, Summary)
- ✅ Optimize token costs with memory management
- ✅ Build multi-turn conversational AI systems
- ✅ Design session-based conversation management

## 🏗️ Step-by-Step Learning Guide

This session builds a **RAG FAQ chatbot with conversation memory in 10 steps**. Steps 1-6 cover the core RAG pipeline with basic memory, and Steps 7-10 explore advanced conversation memory strategies.

### Core RAG Pipeline (Steps 1-6)

The first six steps focus on building the foundational RAG system with integrated conversation memory.

---

### **Step 1: Imports & Setup** ⚙️

**What You'll Do:**
- Import LangChain libraries for LLMs, embeddings, text processing, and vector stores
- Import Pandas for CSV data loading
- Load environment variables from `.env` file
- Initialize the OpenAI embedder (`text-embedding-3-small`) and LLM (`GPT-4o-mini`)

**Key Concepts:**
- **Embedder**: Converts text into vectors (numerical representations) for semantic similarity search
- **LLM**: The language model that generates natural language answers
- **Chroma**: A persistent vector database that stores embeddings and survives kernel restarts
- **Document**: LangChain's wrapper for text content + metadata
- **Memory Management**: Session-based conversation tracking for multi-turn interactions

**Why This Matters:**
Understanding the role of each component is crucial. The embedder creates searchable representations, the LLM generates answers, and Chroma stores knowledge persistently.

**Example Code Pattern:**
```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

embedder = OpenAIEmbeddings(model="text-embedding-3-small")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
```

**Learning Outcome:** You'll understand how to initialize the building blocks of any RAG system.

---

### **Step 2: Verify API Keys** 🔑

**What You'll Do:**
- Check that `OPENAI_API_KEY` is loaded from environment variables
- Use assertions to fail fast if credentials are missing
- Print confirmation when setup is successful

**Key Concepts:**
- **Environment Variables**: Secure way to store API keys without hardcoding
- **Fail Fast**: Catch configuration errors before expensive API calls
- **Security Best Practices**: Never commit API keys to git repositories

**Why This Matters:**
Missing API keys will cause cryptic errors later. This step saves debugging time by validating setup immediately.

**Example Code Pattern:**
```python
import os
from dotenv import load_dotenv

load_dotenv()
assert os.getenv("OPENAI_API_KEY"), "Missing OPENAI_API_KEY in .env file!"
print("✅ API key loaded successfully")
```

**Learning Outcome:** You'll learn defensive programming practices for API-based applications.

---

### **Step 3: Load the FAQ Dataset** 📊

**What You'll Do:**
- Load `customer_support_faq.csv` using Pandas
- Convert each CSV row into a LangChain `Document` object
- Include metadata: region (US/EU/Asia), channel (email/chat/phone), issue type (account/billing/technical)

**Key Concepts:**
- **Document**: LangChain's container for text + metadata
  - `page_content`: The actual text content
  - `metadata`: Structured data for filtering (region, source, tags)
- **Data Transformation**: Converting structured data (CSV) into LLM-friendly format

**Why This Matters:**
Real-world knowledge bases come from databases, CSVs, or APIs. Learning to convert them into Document objects is essential for any RAG project.

**Example Code Pattern:**
```python
import pandas as pd
from pathlib import Path

csv_path = Path("customer_support_faq.csv")
df = pd.read_csv(csv_path)

documents = [
    Document(
        page_content=f"Q: {row['question']}\nA: {row['answer']}",
        metadata={
            "source": "faq_csv",
            "region": row.get("region"),
            "channel": row.get("channel"),
            "issue": row.get("issue")
        }
    )
    for idx, row in df.iterrows()
]

print(f"Loaded {len(documents)} FAQ documents")
```

**Learning Outcome:** You'll master converting real-world data into RAG-ready Documents with metadata.

---

### **Step 4: Build a Persistent Vector Store (Chroma)** 🗄️

**Important Note:** This project intentionally **DOES NOT chunk** the FAQ documents. Each FAQ is already small (~100-300 words) and semantically coherent. Chunking would fragment the Q&A pairs and hurt retrieval quality. See the "Why No Chunking?" section at the end of this guide for a detailed explanation.

**What You'll Do:**
- Embed all chunks using OpenAI's `text-embedding-3-small` model
- Store embeddings + original text in Chroma database at `chroma_faq/`
- Create a `retriever` object to fetch relevant chunks for queries

**Key Concepts:**
- **Embeddings**: Vector representations of text that capture semantic meaning
  - Similar meanings → Similar vectors
  - "password reset" and "forgot my password" have close vectors
- **Vector Database**: Stores embeddings and enables fast similarity search
- **Persistence**: Chroma saves to disk—embeddings survive kernel restarts
- **Retriever**: High-level interface for semantic search

**Why This Matters:**
Vector databases are the backbone of modern AI applications. Chroma is production-ready and used by thousands of companies. This skill applies to Pinecone, Weaviate, and other vector stores.

**Example Code Pattern:**
```python
from langchain_community.vectorstores import Chroma

persist_dir = "chroma_faq"

vectorstore = Chroma.from_documents(
    documents=documents,  # Original complete Q&A pairs (NOT chunks)
    embedding=embedder,
    persist_directory=persist_dir
)

retriever = vectorstore.as_retriever()  # Default k=4 most similar documents
print(f"✅ Chroma vector store created at {persist_dir}")
```

**Testing the Retriever:**
```python
# Test semantic search
results = retriever.get_relevant_documents("password reset")
for doc in results:
    print(doc.page_content[:100])
```

**Production Tips:**
- **search_kwargs={"k": 4}**: Return top 4 most similar chunks
- **Persistence**: Delete `chroma_faq/` folder to rebuild from scratch
- **Scaling**: For millions of documents, consider Pinecone or Weaviate

**Learning Outcome:** You'll build production-grade vector search systems and understand embedding-based retrieval.

---

### **Step 5: Build the RAG Chain with Memory** ⛓️💾

**What You'll Do:**
- Set up session-based conversation memory with `InMemoryChatMessageHistory`
- Create a **Prompt Template** with `{context}`, `{question}`, and `{history}` placeholders
- Wire together a RAG pipeline with memory:
  1. **Session Management**: Get or create conversation history for user
  2. **Retrieval**: Fetch relevant FAQs from vector store
  3. **Prompt**: Format context + question + history into LLM prompt
  4. **LLM**: Generate answer using GPT-4o-mini with conversation context
  5. **Memory Update**: Save user question and bot answer to session history

**Key Concepts:**
- **RAG Pipeline**: Retrieval → Augmentation → Generation
- **Session-Based Memory**: Each user gets isolated conversation history
- **RunnableParallel**: LangChain pattern for parallel operations
- **RunnableWithMessageHistory**: Wrapper that adds memory to any chain
- **Prompt Template**: Structured instructions for the LLM with history injection
- **StrOutputParser**: Extracts text from LLM response objects

**Why This Matters:**
This is the core RAG architecture with memory used in ChatGPT plugins, enterprise AI assistants, and multi-turn chatbots. Understanding this pattern unlocks 90% of modern AI applications.

**RAG + Memory Pipeline Flow:**
```
User Question: "How do I reset my password?"
    ↓
[Session Management] → Get/create conversation history for user_session_123
    ↓
[Retriever] → Find top 4 relevant FAQ documents about password reset
    ↓
[Prompt Template] → Format: "Context: {FAQs}. History: {past messages}. Q: {question}"
    ↓
[LLM (GPT-4o-mini)] → Generate: "To reset your password, go to..."
    ↓
[StrOutputParser] → Extract plain text answer
    ↓
[Memory Update] → Save user question + bot answer to session history
```

**Example Code Pattern:**
```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

# Session-based memory store
store = {}

def get_session_history(session_id: str):
    """Get or create conversation history for a session"""
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# Prompt template with memory
template = """You are a helpful customer support chatbot.
Use the following context to answer the question.
If you don't know, say you don't know.

Context: {context}
Question: {question}
Answer:"""

prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    MessagesPlaceholder(variable_name="history"),  # Inject conversation history
    ("human", "{question}")
])

def format_docs(docs):
    """Convert Document objects to plain text"""
    return "\n\n".join(doc.page_content for doc in docs)

# Build RAG chain
base_chain = (
    RunnableParallel(
        context=lambda x: format_docs(retriever.invoke(x.get("question", ""))),
        question=lambda x: x.get("question", ""),
        history=lambda x: x.get("history", [])
    )
    | prompt
    | llm
    | StrOutputParser()
)

# Wrap with memory management
qa_chain = RunnableWithMessageHistory(
    base_chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

# Chat with memory
config = {"configurable": {"session_id": "user_123"}}
answer = qa_chain.invoke({"question": "How do I reset my password?"}, config=config)
print(answer)
```

**Advanced Concepts:**
- **RunnableParallel**: Fetches context and question simultaneously (optimization)
- **Lambda Functions**: Anonymous functions for data transformation
- **Pipe Operator (|)**: Chains components together (LCEL syntax)

**Prompt Engineering Tips:**
- Be explicit: "If you don't know, say so" prevents hallucinations
- Provide examples: Few-shot prompting improves accuracy
- Set tone: "You are a helpful..." guides LLM behavior

**Learning Outcome:** You'll master LangChain Expression Language (LCEL) and build production RAG pipelines with integrated conversation memory.

---

### **Step 6: Test with Real Questions** 🧪

**What You'll Do:**
- Ask the chatbot realistic customer support questions
- Observe how it retrieves relevant FAQs and generates answers
- Test edge cases: questions not in the FAQ, ambiguous queries

**Key Concepts:**
- **End-to-End Testing**: Validate the entire pipeline works
- **Retrieval Quality**: Check if top-K chunks are actually relevant
- **Answer Quality**: Evaluate if LLM generates accurate, helpful responses
- **Failure Modes**: Test "I don't know" behavior when no relevant context exists

**Why This Matters:**
Real-world RAG systems need thorough testing. This step teaches you to evaluate retrieval quality, prompt effectiveness, and edge case handling.

**Example Code Pattern:**
```python
test_questions = [
    "How do I reset my password via the mobile app?",
    "What is your refund policy?",
    "Do you offer phone support?",
    "How do I delete my account?"
]

for question in test_questions:
    answer = rag_chain.invoke({"question": question})
    print(f"Q: {question}")
    print(f"A: {answer}\n")
    print("-" * 80)
```

**Debugging Tips:**
```python
# Inspect what chunks are retrieved
docs = retriever.get_relevant_documents("password reset")
for i, doc in enumerate(docs):
    print(f"Chunk {i+1}: {doc.page_content[:200]}")
    print(f"Metadata: {doc.metadata}\n")
```

**Evaluation Checklist:**
- ✅ Does the retriever find relevant chunks?
- ✅ Does the LLM use the context correctly?
- ✅ Are answers accurate and helpful?
- ✅ Does it say "I don't know" for out-of-scope questions?

**Learning Outcome:** You'll learn to test, debug, and evaluate RAG systems with conversation memory systematically.

---

### Advanced: Conversation Memory Strategies (Steps 7-10)

After building the core RAG pipeline with basic session memory, the next four steps explore **advanced memory strategies** for optimizing cost and context trade-offs in multi-turn conversations.

---

### **Why Different Memory Strategies?**

Real-world chatbots need to remember conversation history, but there's a critical **cost vs context trade-off**:

- More memory = Better context understanding
- More memory = Higher token costs (every API call includes full history)
- More memory = Slower responses (more tokens to process)

The solution? Choose a memory strategy based on your use case:

1. **Buffer Memory**: Keeps ALL messages (full context, higher token usage)
2. **Window Memory**: Keeps only LAST N messages (balanced, fixed token cost)
3. **Summary Memory**: Summarizes old messages (efficient, loses granular details)

---

### **Step 7: Buffer Memory (All Messages)** 💾

**Note:** You've already implemented basic buffer memory in Step 5. This step demonstrates it explicitly and compares it to other strategies.

**What You'll Do:**
- Store ALL conversation messages in memory
- Build a chatbot that remembers every past question and answer
- Observe how memory grows with each conversation turn

**Key Concepts:**
- **InMemoryChatMessageHistory**: LangChain's in-memory conversation storage
- **RunnableWithMessageHistory**: Wrapper that adds conversation memory to any chain
- **Session Management**: Track different users with session IDs

**Why This Matters:**
Buffer memory provides the richest context for the LLM. It's ideal for short, focused conversations where every detail matters (e.g., troubleshooting a specific issue).

**Example Code Pattern:**
```python
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

store_buffer = {}

def get_session_history(session_id: str):
    if session_id not in store_buffer:
        store_buffer[session_id] = InMemoryChatMessageHistory()
    return store_buffer[session_id]

qa_chain = RunnableWithMessageHistory(
    base_chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

# Chat loop
for question in questions:
    config = {"configurable": {"session_id": "user123"}}
    answer = qa_chain.invoke({"question": question}, config=config)
    print(f"Q: {question}\nA: {answer}\n")
```

**Use Cases:**
- Customer support sessions (3-5 turns max)
- Troubleshooting workflows where context is critical
- Scenarios where cost is not a primary concern

**Trade-offs:**
- ✅ **Best context**: LLM sees full conversation history
- ❌ **Grows unbounded**: Token costs increase with every turn
- ❌ **No compression**: Eventually hits context window limits

**Learning Outcome:** You'll understand how to implement full conversation memory and when it's appropriate.

---

### **Step 8: Window Memory (Last N Messages)** 🪟

**What You'll Do:**
- Keep only the LAST N messages in memory (e.g., last 4 messages = 2 turns)
- Automatically discard older messages to maintain fixed token cost
- Balance context quality with cost efficiency

**Key Concepts:**
- **Sliding Window**: Keep recent messages, drop old ones
- **Fixed Token Cost**: Memory size stays constant regardless of conversation length
- **Configurable Window Size**: Tune N based on your needs

**Why This Matters:**
Window memory is the sweet spot for most production chatbots. It provides enough context for coherent multi-turn conversations while preventing runaway costs.

**Example Code Pattern:**
```python
store_window = {}
window_size = 4  # Keep last 4 messages (2 Q&A pairs)

def get_session_history_window(session_id: str):
    if session_id not in store_window:
        store_window[session_id] = InMemoryChatMessageHistory()
    return store_window[session_id]

def trim_window_history(history, window_size):
    messages = history.messages
    if len(messages) > window_size:
        return messages[-window_size:]
    return messages

def chat_window(user_input, session_id="window_session"):
    history_obj = get_session_history_window(session_id)
    config = {"configurable": {"session_id": session_id}}
    answer = qa_chain.invoke({"question": user_input}, config=config)
    
    # Trim to window size
    trimmed = trim_window_history(history_obj, window_size)
    history_obj.messages = trimmed
    return answer
```

**Use Cases:**
- General chatbots (10-20 turn conversations)
- Multi-user systems where predictable costs matter
- Applications with moderate context requirements

**Trade-offs:**
- ✅ **Predictable cost**: Token usage stays constant
- ✅ **Good balance**: Recent context preserved
- ❌ **Loses old context**: Can't reference distant turns
- ❌ **Tuning required**: Window size affects quality

**Optimization Tips:**
- **window_size=4**: Good for simple Q&A (last 2 turns)
- **window_size=8**: Better for complex troubleshooting (last 4 turns)
- **window_size=12**: For detailed technical support (last 6 turns)

**Learning Outcome:** You'll master cost-effective conversation memory for production chatbots.

---

### **Step 9: Summary Memory (LLM-Based Compression)** 📋

**What You'll Do:**
- Use the LLM to SUMMARIZE old conversation turns
- Keep recent N messages in full detail
- Replace older messages with concise 1-2 sentence summaries
- Enable unlimited conversation length with minimal token cost

**Key Concepts:**
- **LLM Compression**: Use AI to compress conversation history
- **keep_recent_messages**: Number of recent turns to preserve fully
- **Progressive Summarization**: Older messages → summaries → keep refreshing
- **Trade-off**: Lowest cost, but loses granular details

**Why This Matters:**
Summary memory enables very long conversations (50+ turns) without exploding costs. It's essential for research sessions, document analysis, and extended customer interactions.

**Example Code Pattern:**
```python
store_summary = {}
keep_recent_messages = 2  # Keep last 2 turns fully, summarize rest

def compress_with_llm(messages, llm, keep_recent=2):
    """Use LLM to summarize old messages"""
    if len(messages) <= keep_recent * 2:
        return None  # Not enough to summarize
    
    old_messages = messages[:-keep_recent*2]
    old_text = "\n".join([msg.content for msg in old_messages])
    
    summary_prompt = f"""Summarize this conversation in 1-2 sentences:
{old_text}
Summary:"""
    
    summary = llm.invoke(summary_prompt)
    return summary.content

def chat_summary(user_input, session_id="summary_session"):
    # ... invoke chain ...
    
    # Compress if history is too long
    if len(history_obj.messages) > keep_recent_messages * 2:
        summary = compress_with_llm(history_obj.messages, llm)
        store_summary[session_id]["summary"] = summary
    
    return answer
```

**Use Cases:**
- Research sessions with documents (unlimited turns)
- Multi-hour customer support chats
- Applications where cost efficiency is critical
- Long-term user interactions (days/weeks)

**Trade-offs:**
- ✅ **Cheapest option**: Minimal token usage
- ✅ **Unlimited length**: No practical conversation limit
- ❌ **Detail loss**: Granular context from old turns is compressed
- ❌ **Extra LLM call**: Summarization adds latency

**Advanced Techniques:**
- **Progressive summarization**: Re-summarize summaries as they age
- **Selective summarization**: Only compress low-importance turns
- **Hybrid approach**: Window + summary for best of both worlds

**Learning Outcome:** You'll learn to build cost-efficient chatbots that handle unlimited conversation lengths.

---

### **Step 10: Deep Dive - Why No Chunking?** 🤔

**What You'll Learn:**
- Understand when chunking is necessary vs when it hurts retrieval quality
- See why this project keeps FAQ documents whole (100-300 words each)
- Learn what changes when scaling to 500K+ documents
- Explore hierarchical chunking strategies for large-scale systems
- Compare performance: No chunking (500 FAQs) vs Smart chunking (500K FAQs)

**Key Takeaway:** Chunking is not always the answer. For small, coherent documents like FAQs, keeping them whole provides better retrieval quality and lower costs.

The notebook includes a comprehensive deep-dive section explaining the decision-making process and providing code examples for when you DO need chunking at scale.

---

## 📊 Memory Strategy Comparison

| Strategy | What's Kept | Token Cost | Context Loss | Best For |
|----------|------------|-----------|--------------|----------|
| **Buffer Memory** | All messages | High ↑ | None | Short chats (3-5 turns), critical context |
| **Window Memory** | Last N messages | Fixed ↓ | Old turns lost | Medium chats (10-20 turns), balanced |
| **Summary Memory** | Recent + compressed | Low ↓↓ | Granular details lost | Long chats (50+ turns), cost-critical |

### Decision Guide:

**Choose Buffer Memory when:**
- Conversations are short (< 10 turns)
- Every detail matters (legal, medical, troubleshooting)
- Cost is not a constraint
- You need perfect recall

**Choose Window Memory when:**
- Conversations are medium-length (10-30 turns)
- Recent context is most important
- You need predictable costs
- Most production chatbots fall here

**Choose Summary Memory when:**
- Conversations are very long (50+ turns)
- Cost efficiency is critical
- High-level context is sufficient
- Research/analysis applications

### Real-World Examples:

- **E-commerce support** (Buffer): "My order #12345 is late" → Short, focused
- **Tech support chatbot** (Window): Multi-turn troubleshooting, recent steps matter
- **Research assistant** (Summary): Multi-hour document analysis sessions

---

## 🧪 Testing & Validation

### Sample Test Questions

Try these to validate your chatbot:

**Password & Account:**
- "How do I reset my password via the mobile app?"
- "I forgot my username, what should I do?"
- "Can I change my email address?"

**Billing & Refunds:**
- "What is your refund policy?"
- "How do I update my payment method?"
- "When will I be charged?"

**Technical Support:**
- "The app crashes when I log in"
- "Do you offer phone support?"
- "How do I export my data?"

**Edge Cases:**
- "What's the weather today?" (Should say "I don't know")
- "Tell me a joke" (Should stay on-topic or refuse)

### Debugging the Retriever

```python
# Check what chunks are retrieved for a query
query = "password reset"
docs = retriever.get_relevant_documents(query)

for i, doc in enumerate(docs):
    print(f"--- Chunk {i+1} ---")
    print(doc.page_content)
    print(f"Metadata: {doc.metadata}\n")
```

### Monitoring with LangSmith

If you enabled LangSmith tracing:
1. Visit https://smith.langchain.com
2. Select your project (`Customer-Support-Chatbot`)
3. View traces to see:
   - Retrieval results
   - Prompt sent to LLM
   - LLM response
   - Latency and token usage

---

## 🔑 Key Concepts Explained

### What is RAG (Retrieval-Augmented Generation)?

**Problem:** LLMs have outdated knowledge and can't access your private data.

**Solution:** RAG combines retrieval (search) + generation (LLM):
1. **Retrieve** relevant context from a knowledge base
2. **Augment** the prompt with retrieved context
3. **Generate** an answer using the LLM

**Example:**
- User asks: "What's your return policy?"
- Retriever finds: Policy document chunk
- LLM generates: "Our return policy allows..."

### How Embeddings Work

**Text to Vectors:**
- "How do I reset my password?" → `[0.23, -0.45, 0.67, ...]` (1536 dimensions)
- "I forgot my password" → `[0.21, -0.43, 0.69, ...]` (similar vector!)

**Similarity Search:**
- Chroma computes cosine similarity between query vector and all stored vectors
- Returns top-K most similar chunks

**Why It's Powerful:**
- Works across languages, synonyms, and paraphrasing
- No keyword matching required

### When to Chunk vs Keep Documents Whole

**This Project: No Chunking (500 FAQ documents)**
- Each FAQ is naturally small (~100-300 words)
- Q&A pairs are semantically coherent units
- Chunking would fragment answers and hurt retrieval
- 500 embeddings = low cost, fast search

**When You NEED Chunking:**

| Document Size | Strategy | Why? |
|---------------|----------|------|
| < 500 words | Keep whole | Already optimal size |
| 500-2000 words | Optional | Chunk only if retrieval is noisy |
| 2000-5000 words | Smart chunking | Balance context and precision |
| > 5000 words | Hierarchical chunking | Required for manageability |

**Chunking Strategies (for large documents):**

| Strategy | Chunk Size | Overlap | Best For |
|----------|-----------|---------|----------|
| Small | 100-250 | 20-40 | Precise answers from large docs |
| Medium | 500-1000 | 50-100 | Articles, blog posts |
| Large | 1500-2000 | 200-300 | Technical docs, books |

**Decision Rule:**
- If document < 500 words: Keep whole
- If document > 2KB and you have 10K+ docs: Implement chunking
- See Step 10 deep-dive in notebook for detailed analysis

### Prompt Engineering for RAG

**Effective RAG Prompt Template:**
```
You are a [ROLE: customer support agent].
Use the following context to answer the question.
[CONSTRAINT: If you don't know, say "I don't know."]

Context: {context}
Question: {question}
Answer:
```

**Key Elements:**
1. **Role**: Sets the LLM's persona
2. **Instructions**: Use context, don't hallucinate
3. **Constraint**: Prevents making up answers
4. **Placeholders**: `{context}`, `{question}`

---

## ⚡ Performance & Optimization

### API Cost Estimation

| Model | Input Cost | Output Cost | Typical Query Cost |
|-------|-----------|-------------|-------------------|
| GPT-4o-mini | $0.15/1M tokens | $0.60/1M tokens | ~$0.002 |
| text-embedding-3-small | $0.02/1M tokens | N/A | ~$0.0001 |

**Per Query:**
- Embedding: ~100 tokens × $0.02/1M = $0.000002
- LLM: ~500 tokens × $0.75/1M = $0.000375
- **Total: ~$0.0004 per query** (extremely cost-effective!)

### Latency Breakdown

- **Embedding query**: ~200ms
- **Vector search (Chroma)**: ~50ms
- **LLM generation**: ~1-2 seconds
- **Total**: ~1.5-2.5 seconds per query

### Scaling Considerations

**Current Setup (500 FAQs):**
- Storage: ~2MB (Chroma database)
- Memory: ~50MB (loaded embeddings)
- Retrieval: <50ms

**Scaling to 10,000 FAQs:**
- Storage: ~40MB
- Memory: ~1GB
- Retrieval: <100ms (Chroma handles this easily)

**Scaling to 1M+ Documents:**
- Consider **Pinecone** or **Weaviate** (cloud vector databases)
- Add **caching** for common queries
- Use **hybrid search** (semantic + keyword)

---

## 🚀 Bonus Exercises

### Beginner Challenges

1. **Inspect Retrieval Results**
   ```python
   # See what chunks are retrieved for your question
   query = "How do I cancel my subscription?"
   docs = retriever.get_relevant_documents(query)
   for doc in docs:
       print(doc.page_content, "\n---\n")
   ```

2. **Swap the CSV**
   - Create your own FAQ CSV with columns: `question`, `answer`, `region`, `channel`, `issue`
   - Load it in Step 3 and rebuild the vector store

3. **Experiment with Chunking**
   - Try implementing chunking for the FAQ documents and compare results
   - Observe how retrieval quality degrades when FAQs are fragmented

### Intermediate Challenges

4. **Metadata Filtering**
   - Modify the retriever to only search "US" region FAQs:
   ```python
   retriever = vectorstore.as_retriever(
       search_kwargs={"k": 4, "filter": {"region": "US"}}
   )
   ```

5. **Compare Memory Strategies**
   - Test all four memory implementations (Step 5 + Steps 7-9)
   - Compare token usage, latency, and context quality
   - Build a comparison table with your results

6. **Improve the Prompt**
   - Add few-shot examples to the prompt template
   - Experiment with different tones (friendly, formal, technical)

7. **Memory Optimization**
   - Time how long each strategy takes with 10+ questions
   - Build a hybrid: Window for recent + Summary for old messages
   - Calculate cost differences between strategies

### Advanced Challenges

8. **Hybrid Search**
   - Combine semantic search (embeddings) with keyword search (BM25)
   - Implement re-ranking with cross-encoders

9. **Answer Citations**
   - Modify the chain to return source metadata with answers
   - Show users which FAQ the answer came from

10. **Streaming Responses**
   - Use `stream()` instead of `invoke()` for real-time answer generation
   - Build a Streamlit UI with streaming chat

11. **Production Deployment**
    - Wrap the chain in a FastAPI server
    - Add rate limiting and caching
    - Deploy to cloud (Render, Railway, or AWS Lambda)

12. **Persistent Memory Storage**
    - Replace `InMemoryChatMessageHistory` with Redis or SQLite
    - Enable conversation persistence across server restarts
    - Implement user session management

13. **Custom Summary Strategies**
    - Create domain-specific summarization prompts (e.g., only summarize billing issues)
    - Implement progressive summarization (re-summarize summaries)
    - Build a hybrid Window + Summary memory system

---

## 📊 Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    User Question                             │
│             "How do I reset my password?"                    │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              Session Management                              │
│    Get/create conversation history for user_session_123     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  Embedding Model                             │
│         (OpenAI text-embedding-3-small)                      │
│    Converts question → vector [0.23, -0.45, ...]            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                 Vector Search (Chroma)                       │
│     Finds top-K most similar FAQ documents (500 total)      │
│     Returns: 4 relevant complete Q&A pairs                  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                 Prompt Template + Memory                     │
│   "You are a support bot. Context: {FAQs}.                  │
│    History: {past conversation}. Question: {user Q}."       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              LLM (GPT-4o-mini)                               │
│   Reads prompt + context + history, generates answer        │
│   based on retrieved FAQs and conversation context          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              String Output Parser                            │
│         Extracts plain text response                         │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              Save to Memory                                  │
│    Store user question + bot answer in session history      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  Final Answer                                │
│  "To reset your password via the mobile app, go to..."      │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚠️ Common Issues & Solutions

### "OPENAI_API_KEY not found"

**Cause:** `.env` file missing or not loaded

**Solutions:**
1. Create `.env` file in project directory
2. Add: `OPENAI_API_KEY=sk-your-key-here`
3. Restart Jupyter kernel
4. Verify: `print(os.getenv("OPENAI_API_KEY"))`

### "No such file: customer_support_faq.csv"

**Cause:** FAQ dataset file not found in project root

**Solution:**
Ensure the `customer_support_faq.csv` file is in the project root directory. It should be provided with the project materials.

### "Rate limit exceeded"

**Cause:** Too many API calls in short time

**Solutions:**
1. Wait 60 seconds before retrying
2. Use `time.sleep(1)` between batch queries
3. Upgrade OpenAI plan for higher limits

### "Retriever returns irrelevant chunks"

**Causes:**
- Chunk size too large
- Query too vague
- Not enough chunks indexed

**Solutions:**
1. Reduce `chunk_size` to 150-200
2. Make questions more specific
3. Check if CSV loaded correctly
4. Inspect: `retriever.get_relevant_documents("test")`

### "LLM hallucinates answers"

**Cause:** Prompt doesn't enforce using context

**Solution:** Update prompt template:
```python
template = """Use ONLY the context below to answer.
If the context doesn't contain the answer, say "I don't know."
DO NOT make up information.

Context: {context}
Question: {question}
Answer:"""
```

### "Chroma database won't delete"

**Cause:** Windows file locks (process holding files)

**Solution:**
1. Restart Jupyter kernel
2. Delete `chroma_faq/` folder manually
3. Re-run Step 5

---

## 📚 Additional Resources

### Official Documentation
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [Chroma Documentation](https://docs.trychroma.com/)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [LangSmith Tracing](https://docs.smith.langchain.com/)

### Related Concepts
- **Week 2: Prompts, Chains & Memory** - Foundation of memory concepts in LangChain
- **Week 4: PDF RAG Project** - Similar RAG architecture with PDF documents
- **Week 8: Website Q&A Chatbot** - RAG with web scraping
- **Week 12: Local Knowledge Assistant** - Advanced RAG with local LLMs

### Further Learning
- **RAG Best Practices**: [Pinecone RAG Guide](https://www.pinecone.io/learn/retrieval-augmented-generation/)
- **Chunking Strategies**: [Greg Kamradt's Guide](https://github.com/FullStackRetrieval-com/RetrievalTutorials)
- **Prompt Engineering**: [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- **LangChain Memory**: [LangChain Memory Documentation](https://python.langchain.com/docs/modules/memory/)
- **Conversation Design**: Best practices for chatbot UX and multi-turn dialogs

---

## 💡 Tips for Success

1. **Run Cells Sequentially**: Don't skip steps—each builds on the previous
2. **Check Outputs**: Verify each step works before moving forward
3. **Experiment**: Try different prompts, questions, and memory strategies
4. **Use LangSmith**: Enable tracing to see exactly what happens
5. **Read Errors**: Error messages usually point to the exact issue
6. **Test Edge Cases**: Try questions outside the FAQ to test "I don't know" behavior
7. **Compare Retrievals**: Inspect what documents are retrieved vs what you expected
8. **Memory Strategy Testing**: Compare all four memory approaches (Step 5 + Steps 7-9)
9. **Monitor Token Usage**: Track costs when testing different memory strategies
10. **Read the Deep Dive**: Step 10 explains chunking decisions—crucial for real projects!

---

## 📞 Support & Community

- **Live Sessions**: Follow along for instructor walkthrough and Q&A
- **Discord/Community**: Share your results and ask questions
- **Office Hours**: Debug specific issues with instructors
- **Documentation**: Check notebook for inline comments and explanations

---

## 🎯 Next Week Preview

**Week 8: Website Q&A Chatbot**
- Scrape website content automatically
- Build RAG system for live web data
- Handle dynamic content updates
- Multi-page website knowledge bases

This week's Customer Support Chatbot skills transfer directly to Week 8!

---

**Happy Learning! 🚀**

Build this once, use the pattern everywhere—RAG + Memory is the foundation of conversational AI applications!
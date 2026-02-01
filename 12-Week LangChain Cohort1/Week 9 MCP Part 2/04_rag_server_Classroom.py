"""
MCP Server 4: RAG (Retrieval-Augmented Generation) - STUDENT EXERCISE
======================================================================
Your task: Complete this server to provide website learning and Q&A
It should run on port 8003.

LEARNING GOALS:
- Integrate LangChain with MCP
- Understand RAG architecture
- Work with vector databases
- Create complex tools with external dependencies

Runs on: http://localhost:8003
"""

# TODO 1: Import required libraries
from mcp.server.fastmcp import FastMCP
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
from dotenv import load_dotenv

# TODO 2: Setup Environment
load_dotenv()

# FILL IN BELOW:
mcp = FastMCP("Website Knowledge Agent")

# TODO 3: Initialize Backend Components
# Hint: Create embeddings, vector store, retriever, and LLM
# FILL IN BELOW:
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
persist_dir = "./chroma_session_new_db_mcp"

vector_store = Chroma(
    collection_name = "website_knowledge",
    embedding_function = embeddings,
    persist_directory = persist_dir
)

# TODO 4: Create retriever
# Hint: Use as_retriever() with k=3 (return 3 most similar chunks)
# FILL IN BELOW:
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# TODO 5: Create LLM instance
# Hint: Use ChatOpenAI with gpt-4o-mini model
# FILL IN BELOW:
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# TODO 6: Define Tool 1 - learn_website
@mcp.tool()
def learn_website(url: str) -> str:
    """Crawls a website URL and adds its content to the knowledge base."""
    try:
        # TODO 7: Load website content
        # Hint: Use WebBaseLoader
        # FILL IN BELOW:
        loader = WebBaseLoader(url)
        docs = loader.load()
        
        # TODO 8: Split documents into chunks
        # Hint: chunk_size=1000, chunk_overlap=200
        # FILL IN BELOW:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = splitter.split_documents(docs)
        
        # TODO 9: Add chunks to vector store
        # FILL IN BELOW:
        vector_store.add_documents(chunks)
        
        return f"Successfully learned content from {url}"
    except Exception as e:
        return f"Error learning website: {str(e)}"


# TODO 10: Define Tool 2 - ask_question
@mcp.tool()
def ask_question(query: str) -> str:
    """Asks a question about the learned websites."""
    
    # TODO 11: Create prompt template
    # This template ensures LLM only uses provided context
    template = """You are a helpful assistant that ONLY answers questions based on the provided context.

STRICT RULES:
1. ONLY use information from the context below
2. DO NOT use your general knowledge or training data
3. If the context doesn't contain the answer, respond with: "I don't know - this information wasn't found in the learned websites."
4. If the context is empty or irrelevant, respond with: "I don't know - this information wasn't found in the learned websites."
5. Always cite that your answer comes from the learned content

Context from learned websites:
{context}

Question: {question}

Answer (based ONLY on the context above):"""
    
    # TODO 12: Create prompt from template
    # FILL IN BELOW:
    prompt = ChatPromptTemplate.from_template(template)
    
    # TODO 13: Build the RAG chain
    # Hint: This chain retrieves context, formats prompt, calls LLM, and parses output
    # FILL IN BELOW:
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    # TODO 14: Invoke the chain with the query
    # FILL IN BELOW:
    return chain.invoke(query)


# TODO 15: Run the Server
if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Starting RAG Server...")
    print("📡 Listening on http://localhost:8003")
    print("🛠️  Tools: learn_website, ask_question")
    print("⏸️  Press Ctrl+C to stop")
    print("-" * 50)
    
    # TODO 16: Run with uvicorn
    # FILL IN BELOW:
    uvicorn.run(mcp.sse_app, host="127.0.0.1", port=8003, log_level="info")


"""
TESTING YOUR SERVER:
====================
1. Make sure OPENAI_API_KEY is set in .env file
2. Make sure Servers 1, 2, 3 are still running
3. Run this file: python 4_rag_server_TODO.py
4. Server should be on http://localhost:8003
5. All 4 servers now running!

KEY CONCEPTS:
=============
- EMBEDDINGS: Converting text to vectors
- VECTOR STORE: Database for similarity search
- RETRIEVER: Finds most relevant chunks
- RAG CHAIN: Retrieves → Prompts → LLM → Parse
- PERSISTENCE: Data saved to ./chroma_db_mcp

UNDERSTANDING THE FLOW:
=======================
learn_website:
  URL → Load HTML → Split chunks → Create embeddings → Store in DB

ask_question:
  Query → Retrieve similar chunks → Build prompt → Ask LLM → Return answer

NEXT STEPS:
===========
Once all 4 servers work, move to: multi_server_client_TODO.py
"""

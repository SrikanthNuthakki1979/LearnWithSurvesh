# Chat With Your Knowledge Base (RAG App)

## Objective
Build a Retrieval-Augmented Generation application that answers user questions from PDF documents using chunking, embeddings, FAISS retrieval, and grounded LLM responses.

## Learning Outcomes
- Build an end-to-end RAG pipeline
- Understand chunk size and overlap trade-offs
- Use embeddings with FAISS indexing and retrieval
- Generate answers constrained by retrieved context

## Project Format
- This repository is a starter skeleton.
- Core files include TODO blocks for implementation.
- Focus on retrieval quality and grounded answers.

## MVP Scope
- Load PDFs from data/input_docs
- Split documents into chunks
- Build and persist FAISS index
- Retrieve top-k relevant chunks per query
- Return context-grounded answer

## Prerequisites
- Python environment ready
- Dependencies installed from requirements.txt
- .env created from .env.example

## Implementation Phases
1. Loader: Implement src/loaders/pdf_loader.py
2. Chunking: Implement src/chunking/text_chunker.py
3. Embeddings: Implement src/embeddings/embedder.py
4. Vector Store: Implement src/vectorstore/faiss_store.py
5. Retrieval: Implement src/retrieval/retriever.py
6. QA Chain: Implement src/chains/qa_chain.py
7. Orchestration: Wire src/pipelines/rag_pipeline.py
8. Run: Set query and execute src/main.py

## Deliverables
- Successful run via python -m src.main
- Persisted FAISS index in data/vector_store
- Answer generated from retrieved context
- Completed TODOs in all core modules

## Presentation Checklist
- Show one sample PDF and user query
- Show retrieved chunks or sources used
- Show final answer and explain grounding rule
- Show one extension you implemented

## Folder Map
- data/input_docs: source PDFs
- data/vector_store: persisted FAISS files
- src/loaders: document loading
- src/chunking: text splitting
- src/embeddings: embedding setup
- src/vectorstore: FAISS save/load helpers
- src/retrieval: top-k retrieval logic
- src/chains: prompt and answer generation
- src/pipelines: end-to-end orchestration
- tests: student validation tests

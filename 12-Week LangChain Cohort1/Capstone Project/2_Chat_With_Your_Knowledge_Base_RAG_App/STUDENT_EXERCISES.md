# Student Exercises — Chat With Your Knowledge Base (RAG App)

## Core Tasks
- [ ] Implement `load_pdf_documents` in `src/loaders/pdf_loader.py`
- [ ] Implement `chunk_documents` in `src/chunking/text_chunker.py`
- [ ] Implement `get_embedding_model` in `src/embeddings/embedder.py`
- [ ] Implement FAISS helpers in `src/vectorstore/faiss_store.py`
- [ ] Implement retrieval logic in `src/retrieval/retriever.py`
- [ ] Implement grounded answer generation in `src/chains/qa_chain.py`
- [ ] Implement full orchestration in `src/pipelines/rag_pipeline.py`
- [ ] Set a real query in `src/main.py`

## Validation Targets
- [ ] App loads at least one PDF from `data/input_docs/`
- [ ] Vector store is created in `data/vector_store/`
- [ ] Retriever returns top-k chunks
- [ ] Final answer includes only document-grounded content

## Try-It Areas
1. Add metadata filter retrieval by filename
2. Add source citation (which chunk/file was used)
3. Add chat history memory for follow-up questions
4. Add CLI mode for repeated interactive Q&A

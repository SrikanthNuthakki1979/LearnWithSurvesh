from pathlib import Path

from src.chunking.text_chunker import chunk_documents
from src.embeddings.embedder import get_embedding_model
from src.loaders.pdf_loader import load_pdf_documents
from src.retrieval.retriever import get_relevant_docs
from src.chains.qa_chain import answer_with_context
from src.vectorstore.faiss_store import build_and_save_faiss


def run_rag_pipeline(docs_dir: Path, vector_store_dir: Path, query: str) -> str:
    # TODO: Orchestrate end-to-end RAG flow.
    # 1) Load documents
    # 2) Chunk docs
    # 3) Create embeddings model
    # 4) Build/save FAISS index
    # 5) Retrieve relevant chunks
    # 6) Generate grounded answer

    # STUDENT PRACTICE SPACE
    # docs = load_pdf_documents(docs_dir)
    # chunks = chunk_documents(docs)
    # embedding_model = get_embedding_model()
    # vector_store = build_and_save_faiss(chunks, embedding_model, vector_store_dir)
    # context_docs = get_relevant_docs(vector_store, query, top_k=4)
    # return answer_with_context(query, context_docs)

    raise NotImplementedError("TODO: Implement run_rag_pipeline")

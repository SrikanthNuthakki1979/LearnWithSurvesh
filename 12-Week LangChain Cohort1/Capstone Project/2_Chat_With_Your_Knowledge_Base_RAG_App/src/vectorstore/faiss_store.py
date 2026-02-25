from pathlib import Path


def build_and_save_faiss(chunks: list, embedding_model, vector_store_dir: Path):
    # TODO: Build FAISS index from chunks and save locally.
    # Suggested steps:
    # 1) FAISS.from_documents(chunks, embedding_model)
    # 2) save_local(path)

    # STUDENT PRACTICE SPACE
    # from langchain_community.vectorstores import FAISS
    # vector_store = FAISS.from_documents(chunks, embedding_model)
    # vector_store.save_local(str(vector_store_dir))
    # return vector_store

    raise NotImplementedError("TODO: Implement build_and_save_faiss")


def load_faiss(vector_store_dir: Path, embedding_model):
    # TODO: Load FAISS index from disk and return vector store.

    # STUDENT PRACTICE SPACE
    # from langchain_community.vectorstores import FAISS
    # return FAISS.load_local(
    #     str(vector_store_dir),
    #     embedding_model,
    #     allow_dangerous_deserialization=True,
    # )

    raise NotImplementedError("TODO: Implement load_faiss")

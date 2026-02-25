def get_relevant_docs(vector_store, query: str, top_k: int = 4) -> list:
    # TODO: Create retriever and fetch top-k relevant chunks.
    # Suggested steps:
    # 1) retriever = vector_store.as_retriever(search_kwargs={"k": top_k})
    # 2) retriever.invoke(query)

    # STUDENT PRACTICE SPACE
    # retriever = vector_store.as_retriever(search_kwargs={"k": top_k})
    # return retriever.invoke(query)

    raise NotImplementedError("TODO: Implement get_relevant_docs")

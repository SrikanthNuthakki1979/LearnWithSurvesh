def chunk_documents(documents: list, chunk_size: int = 1000, chunk_overlap: int = 200) -> list:
    # TODO: Split documents into chunks.
    # Suggested tool:
    # - RecursiveCharacterTextSplitter

    # STUDENT PRACTICE SPACE
    # from langchain_text_splitters import RecursiveCharacterTextSplitter
    # splitter = RecursiveCharacterTextSplitter(
    #     chunk_size=chunk_size,
    #     chunk_overlap=chunk_overlap,
    # )
    # return splitter.split_documents(documents)

    raise NotImplementedError("TODO: Implement chunk_documents")

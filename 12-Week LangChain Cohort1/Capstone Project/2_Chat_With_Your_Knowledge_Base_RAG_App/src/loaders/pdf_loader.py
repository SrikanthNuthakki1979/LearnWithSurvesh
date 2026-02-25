from pathlib import Path


def load_pdf_documents(docs_dir: Path) -> list:
    # TODO: Load PDF files from docs_dir and return list of LangChain Documents.
    # Suggested tools:
    # - DirectoryLoader
    # - PyPDFLoader

    # STUDENT PRACTICE SPACE
    # from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
    # loader = DirectoryLoader(str(docs_dir), glob="**/*.pdf", loader_cls=PyPDFLoader)
    # return loader.load()

    raise NotImplementedError("TODO: Implement load_pdf_documents")

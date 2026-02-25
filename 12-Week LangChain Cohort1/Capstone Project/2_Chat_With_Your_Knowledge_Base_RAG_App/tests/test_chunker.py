import pytest

from src.chunking.text_chunker import chunk_documents


@pytest.mark.skip(reason="Student exercise: implement chunk_documents, then unskip this test.")
def test_chunk_documents_returns_list() -> None:
    documents = []
    chunks = chunk_documents(documents, chunk_size=500, chunk_overlap=100)

    # TODO: Replace with stronger assertions once implementation is complete.
    assert isinstance(chunks, list)

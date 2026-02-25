from src.config import settings


def answer_with_context(query: str, context_docs: list) -> str:
    # TODO: Build grounded QA prompt and call chat model.
    # Requirements:
    # - Use only retrieved context for answers
    # - If context is insufficient, say you don't know

    # STUDENT PRACTICE SPACE
    # from langchain_openai import ChatOpenAI
    # context_text = "\n\n".join(doc.page_content for doc in context_docs)
    # prompt = (
    #     "You are a helpful assistant. Use only the context below. "
    #     "If unsure, say you don't know.\n\n"
    #     f"Context:\n{context_text}\n\n"
    #     f"Question: {query}\nAnswer:"
    # )
    # llm = ChatOpenAI(model=settings.model_name, temperature=0)
    # response = llm.invoke(prompt)
    # return response.content

    raise NotImplementedError("TODO: Implement answer_with_context")

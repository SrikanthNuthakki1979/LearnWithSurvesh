from pathlib import Path

from src.pipelines.rag_pipeline import run_rag_pipeline


def main() -> None:
    # TODO 1: Point to docs folder and vector store folder
    docs_dir = Path("data/input_docs")
    vector_store_dir = Path("data/vector_store")

    # TODO 2: Add a user query string
    query = ""

    # TODO 3: Run pipeline and print answer
    answer = run_rag_pipeline(docs_dir, vector_store_dir, query)
    print("\nFinal Answer:\n")
    print(answer)


if __name__ == "__main__":
    main()

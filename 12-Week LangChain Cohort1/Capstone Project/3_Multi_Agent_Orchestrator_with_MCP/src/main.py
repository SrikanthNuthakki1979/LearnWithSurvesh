from src.graph.orchestrator_graph import run_orchestrator


def main() -> None:
    # TODO 1: Set a mixed query that may require math or RAG reasoning.
    query = ""

    # TODO 2: Execute orchestrator and print final response.
    result = run_orchestrator(query)
    print("\nFinal Response:\n")
    print(result)


if __name__ == "__main__":
    main()

# Week 5: RAG Fundamentals (Retrieval-Augmented Generation)

Welcome to Week 5.
This week focuses on the complete RAG pipeline: loading data, splitting text, creating embeddings, storing vectors, retrieving context, and generating grounded answers.

## Start Here

Use this student practice notebook:

1. 01_RAG_Fundamentals_Student_totry.ipynb

Instructor reference notebook:

- Instructor_Reference_Version/01_RAG_Fundamentals_Instructor.ipynb

## Learning Outcomes

By the end of this week, you should be able to:

1. Explain why RAG improves factual reliability over direct prompting.
2. Load and preprocess text and PDF documents.
3. Choose chunking strategy for retrieval quality.
4. Create embeddings and vector stores.
5. Build a retriever and connect it to an LLM chain.
6. Evaluate response quality and retrieval relevance.

## Notebook Structure

The notebook is scaffolded for learning:

1. First half of code cells has easy hints.
2. Second half has medium hints.
3. Every code cell includes a TODO section.
4. Every code cell includes a mini challenge (optional but recommended).

## Suggested Study Flow

1. Complete cells in order from top to bottom.
2. Attempt TODO first, then use hints if needed.
3. Validate retrieval outputs before final answer generation.
4. Try mini challenges to compare chunk/retrieval settings.

## What To Submit

Submit:

1. 01_RAG_Fundamentals_Student_totry.ipynb

Also include short reflections:

1. One part you understood well.
2. One issue you faced and how you fixed it.
3. One improvement you would try in the next RAG version.

## Setup Notes

Install required packages if needed:

- langchain
- langchain-openai
- langchain-community
- faiss-cpu
- chromadb
- pypdf
- python-dotenv

## Troubleshooting

1. API/authentication issues:
   Verify environment variables and API key setup.
2. Empty or poor retrieval results:
   Recheck chunk size, overlap, and vector store creation.
3. Notebook errors after installs:
   Restart kernel and rerun cells.

## Success Checklist

1. All TODO sections are attempted.
2. Retrieval works and returns relevant chunks.
3. Final RAG responses run without errors.
4. At least one mini challenge is attempted.

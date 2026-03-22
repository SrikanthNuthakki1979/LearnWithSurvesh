# Week 6: RAG Optimization + LLM Evaluation + LangSmith

Welcome to Week 6.
This week advances your RAG system with optimization, evaluation mindset, and observability using LangSmith.

## Start Here

Use these student practice notebooks in order:

1. 01_RAG_Optimization_Student_totry.ipynb
2. 02_LangSmith_Demo_Student_totry.ipynb

Instructor reference notebooks:

- Instructor_Reference_Version/01_RAG_Optimization_Instructor.ipynb
- Instructor_Reference_Version/02_LangSmith_Demo_Instructor.ipynb

## Learning Outcomes

By the end of this week, you should be able to:

1. Optimize retrieval and generation settings for better answer quality.
2. Compare baseline and improved RAG behavior.
3. Define simple evaluation checks for response quality.
4. Use LangSmith tracing to inspect chain/agent execution.
5. Debug weak retrieval and prompt issues systematically.

## Notebook Structure

Both notebooks include progressive support:

1. First half of code cells has easy hints.
2. Second half has medium hints.
3. Every code cell has a TODO section.
4. Every code cell has a mini challenge (optional but recommended).

## Recommended Workflow

1. Finish 01 first, then move to 02.
2. For each section: run baseline, apply change, compare outputs.
3. Track what changed in quality, latency, or relevance.
4. Use LangSmith traces to confirm your assumptions.

## What To Submit

Submit both completed notebooks:

1. 01_RAG_Optimization_Student_totry.ipynb
2. 02_LangSmith_Demo_Student_totry.ipynb

Also include short reflections:

1. One optimization that improved results most.
2. One evaluation signal you trusted most.
3. One insight discovered from LangSmith traces.

## Setup Notes

Install required packages if needed:

- langchain
- langchain-openai
- langchain-community
- langsmith
- python-dotenv

## Troubleshooting

1. LangSmith trace not appearing:
   Verify LangSmith key/project environment variables.
2. Inconsistent response quality:
   Fix randomness settings and compare with controlled prompts.
3. Retrieval quality still weak:
   Revisit chunking and retriever parameters.

## Success Checklist

1. All TODO sections are attempted.
2. Baseline vs optimized behavior is compared.
3. LangSmith trace-based debugging is demonstrated.
4. At least one mini challenge is attempted per notebook.

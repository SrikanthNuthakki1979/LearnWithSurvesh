# Week 5 – AI Email Assistant (LangChain + OpenAI)

Build a production-style email assistant that drafts replies, personalizes tone, batches processing, and maintains thread memory using LangChain's modern patterns.

## Contents
- Week5_AI_Email_Assistant_STUDENT.ipynb — main hands-on notebook with guided TODOs.
- requirements.txt — all Python dependencies with pinned versions.

## Prerequisites
- Python 3.10+ recommended.
- OpenAI API key with access to `gpt-4o-mini`.
- pip and virtual environment support.

## Setup
1) Clone or open this folder.
2) Create a virtual environment (recommended):
   - `python -m venv .venv`
   - Activate: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (macOS/Linux).
3) Install packages from requirements.txt:
   - `pip install -r requirements.txt`
   - Or manually: `pip install langchain langchain-openai pandas python-dotenv jupyter`
4) Add your OpenAI key in a `.env` file at this folder root:
   - `OPENAI_API_KEY=your_api_key_here`

## How to Run the Notebook
1) **Activate your virtual environment** (if not already active):
   - `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (macOS/Linux).
2) Launch Jupyter:
   - `jupyter notebook Week5_AI_Email_Assistant_STUDENT.ipynb`
3) Run cells top to bottom, filling TODOs as you go.

## Notebook Roadmap (what each part teaches)
- Part 1: Setup imports, load env vars, initialize `ChatOpenAI`.
- Part 2: Create a sample Gmail-style email dataset with pandas.
- Part 3: Build a LangChain Expression Language (LCEL) prompt → LLM chain for replies.
- Part 4: Batch-generate replies with status reporting.
- Part 5: Save successful replies to CSV for audit/history.
- Part 6: Tone personalization (formal, friendly, brief, detailed, empathetic).
- Part 7: Thread-aware conversation memory with `RunnableWithMessageHistory`.

## Tips
- Keep the temperature around 0.7 for balanced creativity.
- Use `max_tokens` ~500 to avoid overly long replies.
- When testing memory, reuse the same `thread_id` to see context carry over.

## Troubleshooting
- If you see auth errors, re-check `.env` and your active Python environment.
- Rate limits: lower concurrency or add short sleeps between batch calls.
- CSV not saving: ensure replies list has successful entries before writing.
- Jupyter not found: ensure your venv is activated and `jupyter` was installed via requirements.txt.

Happy building!
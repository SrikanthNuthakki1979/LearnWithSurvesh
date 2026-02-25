from pathlib import Path


COMMON_SKILLS = [
    "python",
    "langchain",
    "sql",
    "fastapi",
    "machine learning",
    "pandas",
]


def load_resume_text(pdf_path: Path) -> str:
    # TODO: Implement PDF parsing logic.
    # Suggested approach:
    # 1) Validate file path exists
    # 2) Read all pages from PDF
    # 3) Join page text into one string
    # 4) Return cleaned text

    if not pdf_path.exists():
        return ""

    # STUDENT PRACTICE SPACE:
    # from PyPDF2 import PdfReader
    # reader = PdfReader(str(pdf_path))
    # pages = [page.extract_text() or "" for page in reader.pages]
    # full_text = "\n".join(pages)
    # return full_text.strip()

    raise NotImplementedError("TODO: Implement load_resume_text")

from src.parsers.pdf_loader import COMMON_SKILLS


def extract_skills_from_text(text: str) -> list[str]:
    # TODO: Implement rule-based extraction using COMMON_SKILLS.
    # Hint:
    # - Normalize resume text to lowercase
    # - Check each skill keyword presence
    # - Remove duplicates
    # - Return sorted list for stable output

    # STUDENT PRACTICE SPACE
    # text_lower = text.lower()
    # found = [skill for skill in COMMON_SKILLS if skill in text_lower]
    # return sorted(set(found))

    raise NotImplementedError("TODO: Implement extract_skills_from_text")

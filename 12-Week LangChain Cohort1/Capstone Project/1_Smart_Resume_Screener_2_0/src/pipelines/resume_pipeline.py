from pathlib import Path

from src.analyzers.skill_gap import compute_skill_gap
from src.extractors.skill_extractor import extract_skills_from_text
from src.models import ResumeReport
from src.parsers.pdf_loader import load_resume_text


def run_resume_pipeline(pdf_path: Path, required_skills: list[str]) -> ResumeReport:
    # TODO: Orchestrate the full flow.
    # 1) Load resume text
    # 2) Extract skills from text
    # 3) Compute skill gap against required skills
    # 4) Return ResumeReport

    # STUDENT PRACTICE SPACE
    # text = load_resume_text(pdf_path)
    # extracted_skills = extract_skills_from_text(text)
    # gap = compute_skill_gap(extracted_skills, required_skills)
    # return ResumeReport(
    #     candidate_name="Unknown",
    #     extracted_skills=extracted_skills,
    #     required_skills=required_skills,
    #     matched_skills=gap["matched_skills"],
    #     missing_skills=gap["missing_skills"],
    #     match_score=gap["match_score"],
    # )

    raise NotImplementedError("TODO: Implement run_resume_pipeline")

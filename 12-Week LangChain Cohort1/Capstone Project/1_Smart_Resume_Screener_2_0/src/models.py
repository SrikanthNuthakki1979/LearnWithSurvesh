from pydantic import BaseModel, Field


class ResumeReport(BaseModel):
    candidate_name: str = Field(default="Unknown")
    extracted_skills: list[str] = Field(default_factory=list)
    required_skills: list[str] = Field(default_factory=list)
    matched_skills: list[str] = Field(default_factory=list)
    missing_skills: list[str] = Field(default_factory=list)
    match_score: float = 0.0

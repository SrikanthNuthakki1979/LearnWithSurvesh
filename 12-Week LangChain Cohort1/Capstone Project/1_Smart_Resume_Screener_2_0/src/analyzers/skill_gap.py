def compute_skill_gap(extracted_skills: list[str], required_skills: list[str]) -> dict:
    # TODO: Implement skill gap calculation.
    # Requirements:
    # - Case-insensitive comparison
    # - matched_skills: present in both lists
    # - missing_skills: required but not extracted
    # - match_score: percentage matched rounded to 2 decimals

    # STUDENT PRACTICE SPACE
    # extracted = {skill.lower() for skill in extracted_skills}
    # required = {skill.lower() for skill in required_skills}
    # matched = sorted(extracted & required)
    # missing = sorted(required - extracted)
    # score = (len(matched) / len(required) * 100.0) if required else 0.0
    # return {
    #     "matched_skills": matched,
    #     "missing_skills": missing,
    #     "match_score": round(score, 2),
    # }

    raise NotImplementedError("TODO: Implement compute_skill_gap")

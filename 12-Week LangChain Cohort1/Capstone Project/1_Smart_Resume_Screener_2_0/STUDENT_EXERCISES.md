# Student Exercises — Smart Resume Screener 2.0

## Core Tasks
- [ ] Implement `load_resume_text` in `src/parsers/pdf_loader.py`
- [ ] Implement `extract_skills_from_text` in `src/extractors/skill_extractor.py`
- [ ] Implement `compute_skill_gap` in `src/analyzers/skill_gap.py`
- [ ] Implement `run_resume_pipeline` in `src/pipelines/resume_pipeline.py`
- [ ] Fill required skills in `src/main.py`
- [ ] Unskip and complete assertions in `tests/test_skill_gap.py`

## Validation Targets
- [ ] Running `python -m src.main` should create `data/output/resume_report.json`
- [ ] JSON should include: `extracted_skills`, `matched_skills`, `missing_skills`, `match_score`
- [ ] `match_score` should be a float in range 0 to 100

## Try-It Areas
1. Add 5 more technical skills to `COMMON_SKILLS`
2. Add a function to extract `candidate_name` from resume text
3. Add batch mode to process all PDFs in `data/input_resumes/`
4. Add a `minimum_match_threshold` and label candidate as `shortlist/review/reject`

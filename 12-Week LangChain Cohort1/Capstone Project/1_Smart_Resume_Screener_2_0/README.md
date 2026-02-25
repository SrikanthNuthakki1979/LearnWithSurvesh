# Smart Resume Screener 2.0

## Objective
Build an ATS-style screening pipeline that reads a resume PDF, extracts skills, compares them to target role skills, and saves a structured JSON report.

## Learning Outcomes
- Design a modular AI workflow (parse → extract → analyze → output)
- Apply rule-based or LLM-assisted skill extraction
- Compute skill match score and missing skills
- Produce consistent machine-readable JSON output

## Project Format
- This repository is a starter skeleton.
- Core files include TODO blocks for implementation.
- Build the MVP first, then add enhancements.

## MVP Scope
- Ingest at least one PDF resume
- Extract skills from resume text
- Compare with required skills list
- Save final report to data/output/resume_report.json

## Prerequisites
- Python environment ready
- Dependencies installed from requirements.txt
- .env created from .env.example

## Implementation Phases
1. Parsing: Implement PDF text extraction in src/parsers/pdf_loader.py
2. Extraction: Implement skill detection in src/extractors/skill_extractor.py
3. Analysis: Implement gap and match score in src/analyzers/skill_gap.py
4. Orchestration: Wire flow in src/pipelines/resume_pipeline.py
5. Run: Configure inputs in src/main.py and generate output
6. Validation: Unskip and complete tests/test_skill_gap.py

## Deliverables
- Working pipeline run via python -m src.main
- JSON report containing candidate_name, extracted_skills, required_skills, matched_skills, missing_skills, match_score
- Completed TODOs in core modules

## Presentation Checklist
- Show one input resume and required skills list
- Run project and generate output JSON
- Explain matching and score calculation logic
- Show one extension you implemented

## Folder Map
- data/input_resumes: sample PDFs
- data/output: generated JSON reports
- src/parsers: PDF loading/parsing
- src/extractors: skill extraction
- src/analyzers: skill-gap logic
- src/pipelines: orchestration
- prompts: prompt templates
- schemas: JSON schema contract
- tests: validation tests
- scripts: helper scripts

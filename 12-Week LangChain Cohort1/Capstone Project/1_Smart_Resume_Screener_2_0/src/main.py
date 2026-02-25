from pathlib import Path
import json

from src.pipelines.resume_pipeline import run_resume_pipeline


def main() -> None:
    # TODO 1: Point to one sample resume PDF inside data/input_resumes/
    sample_pdf = Path("data/input_resumes/sample_resume.pdf")

    # TODO 2: Define role-specific required skills
    # Example: ["python", "langchain", "sql", "fastapi"]
    required_skills: list[str] = []

    # TODO 3: Run the pipeline and store report
    report = run_resume_pipeline(sample_pdf, required_skills)

    # TODO 4: Save output JSON to data/output/resume_report.json
    output_path = Path("data/output/resume_report.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report.model_dump(), indent=2), encoding="utf-8")

    print(f"Report generated at: {output_path}")


if __name__ == "__main__":
    main()

import pytest

from src.analyzers.skill_gap import compute_skill_gap


@pytest.mark.skip(reason="Student exercise: implement compute_skill_gap, then unskip this test.")
def test_compute_skill_gap_basic() -> None:
    extracted = ["python", "sql"]
    required = ["python", "langchain", "sql"]

    result = compute_skill_gap(extracted, required)

    # TODO: Uncomment and complete once implementation is done.
    # assert result["matched_skills"] == ["python", "sql"]
    # assert result["missing_skills"] == ["langchain"]
    # assert result["match_score"] == 66.67

    assert isinstance(result, dict)

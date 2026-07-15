from pydantic import BaseModel
class ReviewResult(BaseModel):
    summary: str

    risk: str

    recommendation: str

    issues: list[str]
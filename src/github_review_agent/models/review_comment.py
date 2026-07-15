from pydantic import BaseModel


class ReviewCommentResult(BaseModel):
    id: int
    state: str
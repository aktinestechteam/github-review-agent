from pydantic import BaseModel


class MergeResult(BaseModel):
    merged: bool
    message: str
    sha: str | None = None
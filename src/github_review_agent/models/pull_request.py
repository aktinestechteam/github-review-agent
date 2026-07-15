from pydantic import BaseModel

class PullRequest(BaseModel):
    title: str
    author: str
    body: str | None = None
    state: str
    mergeable: bool | None = None
    changed_files: int
    commits: int
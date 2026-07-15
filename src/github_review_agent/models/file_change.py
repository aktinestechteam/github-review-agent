from pydantic import BaseModel


class FileChange(BaseModel):
    filename: str
    status: str

    additions: int
    deletions: int
    changes: int

    patch: str | None = None
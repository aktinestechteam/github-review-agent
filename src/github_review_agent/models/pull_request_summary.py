from datetime import datetime

from pydantic import BaseModel


class PullRequestSummary(BaseModel):

    number: int

    title: str

    author: str

    state: str

    created_at: datetime

    updated_at: datetime
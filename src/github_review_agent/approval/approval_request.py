from datetime import datetime

from pydantic import BaseModel, Field


class ApprovalRequest(BaseModel):
    token: str = Field(..., description="Unique approval token")

    thread_id: str = Field(..., description="LangGraph thread id")

    owner: str

    repo: str

    pr_number: int

    approver_email: str

    status: str = "PENDING"

    expires_at: datetime

    created_at: datetime = Field(default_factory=datetime.utcnow)
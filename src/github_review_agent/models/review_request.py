from pydantic import BaseModel,EmailStr

class ReviewRequest(BaseModel):
    owner: str
    repo: str
    pr_number: int

    approver_email: EmailStr
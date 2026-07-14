from typing import TypedDict

class ReviewState(TypedDict):
    owner:str
    repo:str
    pr_number:str

    pull_request:dict

    review_summary:str
    risk_level:str
    recommendation:str

    approved:bool

    status:str
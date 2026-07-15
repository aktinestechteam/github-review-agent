from typing import TypedDict
from github_review_agent.models.pull_request import PullRequest
from github_review_agent.models.review import ReviewResult
from github_review_agent.models.merge_result import MergeResult

class ReviewState(TypedDict):
    owner:str
    repo:str
    pr_number:str
    pull_request:PullRequest
    
    review: ReviewResult
    approved:bool
    merge_result: MergeResult
    status:str
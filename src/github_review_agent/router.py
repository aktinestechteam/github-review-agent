from typing import Literal
from github_review_agent.state import ReviewState


def approval_router(
    state: ReviewState,
) -> Literal["merge_pr", "reject_pr"]:

    print("=== approval_router ===")
    print("approved =", state["approved"])

    if state["approved"]:
        print("Routing to merge_pr")
        return "merge_pr"

    print("Routing to reject_pr")
    return "reject_pr"
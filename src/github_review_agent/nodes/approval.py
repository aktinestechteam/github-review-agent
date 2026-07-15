from langgraph.types import interrupt
from github_review_agent.state import ReviewState

def approval(state: ReviewState) -> dict:
    """
    Pause execution and wait for human approval.
    """

    decision = interrupt(
        {
            "title": state["pull_request"].title,
            "author": state["pull_request"].author,
            "summary": state["review"].summary,
            "risk": state["review"].risk,
            "recommendation": state["review"].recommendation,
            "issues": state["review"].issues,
        }
    )

    return {
        "approved": decision["approved"]
    }
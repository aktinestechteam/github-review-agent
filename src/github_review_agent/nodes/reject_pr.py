from github_review_agent.services.github_service import GitHubService
from github_review_agent.state import ReviewState

github_service = GitHubService()


async def reject_pr(state: ReviewState) -> dict:
    """
    Post AI review comments when the PR is rejected.
    """

    review = state["review"]

    comment = f"""
## 🤖 AI Code Review

### Summary

{review.summary}

### Risk

{review.risk}

### Recommendation

{review.recommendation}

### Issues

"""

    for issue in review.issues:
        comment += f"- {issue}\n"

    result = await github_service.create_review_comment(
        owner=state["owner"],
        repo=state["repo"],
        pr_number=state["pr_number"],
        comment=comment,
    )

    return {
        "status": "REJECTED",
        "review_comment": result,
    }
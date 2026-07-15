from github_review_agent.services.github_service import GitHubService
from github_review_agent.state import ReviewState

github_service = GitHubService()


async def merge_pr(state: ReviewState) -> dict:
    """
    Merge the approved pull request.
    """

    merge_result = await github_service.merge_pull_request(
        owner=state["owner"],
        repo=state["repo"],
        pr_number=state["pr_number"],
    )

    return {
        "status": "MERGED",
         "merge_result": merge_result,
    }
from github_review_agent.state import ReviewState
from github_review_agent.services.github_service import GitHubService
github_service = GitHubService()

async def fetch_pr(state: ReviewState) -> dict:

    """
    Fetch Pull Request details from GitHub via MCP.
    """
    pr = await github_service.get_pull_request(
        state["owner"],
        repo=state["repo"], 
        pr_number = state["pr_number"])
    return {
       "pull_request": pr
    }

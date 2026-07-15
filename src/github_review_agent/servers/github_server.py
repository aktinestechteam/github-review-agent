from fastmcp import FastMCP
from github_review_agent.github_client import github
mcp = FastMCP("Github Review MCP Server")
import asyncio

@mcp.tool
def get_pull_request(owner:str, repo:str, pr_number:int) -> dict:
    """
    Git Pull request details
    """
    repository = github.get_repo(f"{owner}/{repo}")
    pr = repository.get_pull(pr_number)
    return {
        "title": pr.title,
        "author": pr.user.login,
        "state": pr.state,
        "body": pr.body,
        "mergeable": pr.mergeable,
        "changed_files": pr.changed_files,
        "commits": pr.commits,
    }

@mcp.tool
def list_changed_files(
    owner: str,
    repo: str,
    pr_number: int,
) -> list[dict]:
    """
    Return files changed in a pull request.
    """

    repository = github.get_repo(f"{owner}/{repo}")

    pr = repository.get_pull(pr_number)

    files = []

    for file in pr.get_files():

        files.append(
            {
                "filename": file.filename,
                "status": file.status,
                "additions": file.additions,
                "deletions": file.deletions,
                "changes": file.changes,
                "patch": file.patch,
            }
        )

    return files

@mcp.tool
def merge_pull_request(
    owner: str,
    repo: str,
    pr_number: int,
    commit_message: str = "Merged by AI Review Agent",
) -> dict:
    """
    Merge a Pull Request.
    """

    repository = github.get_repo(f"{owner}/{repo}")

    pr = repository.get_pull(pr_number)

    merge_result = pr.merge(
        commit_message=commit_message
    )

    return {
        "merged": merge_result.merged,
        "message": merge_result.message,
        "sha": merge_result.sha,
    }

@mcp.tool
def create_review_comment(
    owner: str,
    repo: str,
    pr_number: int,
    comment: str,
) -> dict:
    """
    Add a review comment to the pull request.
    """

    repository = github.get_repo(f"{owner}/{repo}")

    pr = repository.get_pull(pr_number)

    review = pr.create_review(
        body=comment,
        event="COMMENT",
    )

    return {
        "id": review.id,
        "state": review.state,
    }
if __name__== "__main__":
    mcp.run()
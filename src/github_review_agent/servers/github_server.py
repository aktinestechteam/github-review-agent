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

if __name__== "__main__":
    mcp.run()
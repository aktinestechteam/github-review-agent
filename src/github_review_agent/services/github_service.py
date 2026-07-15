from github_review_agent.client import client
from github_review_agent.models.pull_request import PullRequest
from github_review_agent.models.file_change import FileChange
from github_review_agent.models.merge_result import MergeResult
from github_review_agent.models.review_comment import ReviewCommentResult
from github_review_agent.models.pull_request_summary import (
    PullRequestSummary,
)

class GitHubService:
     async def get_pull_request(
        self,
        owner: str,
        repo: str,
        pr_number: int,
    ) -> PullRequest:

        async with client:
             result = await client.call_tool(
                "get_pull_request",
                {
                    "owner": owner,
                    "repo": repo,
                    "pr_number": pr_number,
                },
            )
        return PullRequest.model_validate(result.data)
     
     async def list_changed_files(
        self,
        owner: str,
        repo: str,
        pr_number: int,
    ) -> list[FileChange]:

        async with client:
             result = await client.call_tool(
                "list_changed_files",
                {
                    "owner": owner,
                    "repo": repo,
                    "pr_number": pr_number,
                },
            )
        return [
            FileChange.model_validate(item)
            for item in result.data
            ]
    
     async def merge_pull_request(
    self,
    owner: str,
    repo: str,
    pr_number: int,
) -> MergeResult:
          async with client:
              result = await client.call_tool(
            "merge_pull_request",
            {
                "owner": owner,
                "repo": repo,
                "pr_number": pr_number,
            },
        )
              return MergeResult.model_validate(result.data)
     async def create_review_comment(
    self,
    owner: str,
    repo: str,
    pr_number: int,
    comment: str,
) -> ReviewCommentResult:
          async with client:

            result = await client.call_tool(
            "create_review_comment",
            {
                "owner": owner,
                "repo": repo,
                "pr_number": pr_number,
                "comment": comment,
            },
        )
            return ReviewCommentResult.model_validate(result.data)

async def list_open_pull_requests(
    self,
    owner: str,
    repo: str,
) -> list[PullRequestSummary]:

    async with client:

        result = await client.call_tool(
            "list_open_pull_requests",
            {
                "owner": owner,
                "repo": repo,
            },
        )

    return [
        PullRequestSummary.model_validate(item)
        for item in result.data
    ]
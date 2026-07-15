from github_review_agent.services.github_service import GitHubService
from github_review_agent.state import ReviewState


class ReviewContextBuilder:
    """
    Builds the complete context required for AI code review.
    """

    def __init__(self):
        self.github = GitHubService()

    async def build(self, state: ReviewState) -> str:
        """
        Build a text context from GitHub data.
        """

        # Fetch changed files
        files = await self.github.list_changed_files(
            owner=state["owner"],
            repo=state["repo"],
            pr_number=state["pr_number"],
        )

        context = []

        context.append(
            f"# Pull Request\n"
            f"Title: {state['pull_request'].title}\n"
            f"Author: {state['pull_request'].author}\n"
        )

        context.append("\n# Changed Files\n")

        for file in files:

            context.append(
                f"""
File: {file.filename}

Status: {file.status}

Additions: {file.additions}

Deletions: {file.deletions}

Patch:

{file.patch}
"""
            )

        return "\n".join(context)
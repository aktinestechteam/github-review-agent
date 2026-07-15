import asyncio
from github_review_agent.services.github_service import GitHubService


async def main():

    service = GitHubService()

    pr = await service.get_pull_request(
        owner="aktinestechteam",
        repo="github-review-agent",
        pr_number=1,
    )

    print(pr)


if __name__ == "__main__":
    asyncio.run(main())
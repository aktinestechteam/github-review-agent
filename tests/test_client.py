import asyncio

from github_review_agent.client import client


async def main():

    async with client:
        result = await client.call_tool(
            "get_pull_request",
            {
                "owner": "aktinestechteam",
                "repo": "github-review-agent",
                "pr_number": 1
            }
        )
        print(result)


        

if __name__ == "__main__":
    asyncio.run(main())
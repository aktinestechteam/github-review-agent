import asyncio
from github_review_agent.graph import graph

config = {
    "configurable": {
        "thread_id": "pr-101"
    }
}
async def main():
    result = await graph.ainvoke(
         {
                "owner": "aktinestechteam",
                "repo": "github-review-agent",
                "pr_number": 1
         },
         config=config
    )
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
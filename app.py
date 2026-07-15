import asyncio

from langgraph.types import Command

from github_review_agent.graph import graph


THREAD_ID = "review-1001"


config = {
    "configurable": {
        "thread_id": THREAD_ID
    }
}


async def start_review():

    result = await graph.ainvoke(
        {
            "owner": "aktinestechteam",
            "repo": "github-review-agent",
            "pr_number": 1,
        },
        config=config,
    )

    if "__interrupt__" in result:

        interrupt = result["__interrupt__"][0]

        print("\n========== AI Review ==========\n")

        for key, value in interrupt.value.items():
            print(f"{key}:")
            print(value)
            print()

        decision = input("Approve PR? (y/n): ")

        approved = decision.lower() == "y"

        await resume_review(approved)


async def resume_review(approved: bool):

    result = await graph.ainvoke(
        Command(
            resume={
                "approved": approved
            }
        ),
        config=config,
    )

    print()

    print("Workflow Completed")

    print(result)


if __name__ == "__main__":
    asyncio.run(start_review())
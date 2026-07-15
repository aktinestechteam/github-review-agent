from github_review_agent.services.github_service import GitHubService
from github_review_agent.workflow.workflow_manager import WorkflowManager
from github_review_agent.review_workflow_service import (
    ReviewWorkflowService,
)

github_service = GitHubService()
workflow_manager = WorkflowManager()
workflow = ReviewWorkflowService()

async def scan_pull_requests():

    print("Scanning GitHub...")

    prs = await github_service.list_open_pull_requests(
        owner="aktinestechteam",
        repo="github-review-agent",
    )

    print(f"Found {len(prs)} open PR(s)")

    for pr in prs:
        if not workflow_manager.should_start(
        owner="aktinestechteam",
        repo="github-review-agent",
        pr_number=pr.number,
    ):
            
            print(f"Skipping PR #{pr.number}")
            continue
        await workflow.start_review(
    owner="aktinestechteam",
    repo="github-review-agent",
    pr_number=pr.number,
    approver_email="lgogave@gmail.com",
)
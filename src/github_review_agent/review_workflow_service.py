from datetime import datetime, timedelta

from github_review_agent.graph import graph

from github_review_agent.approval import approval_store
from github_review_agent.approval.approval_request import ApprovalRequest
from github_review_agent.approval.token_service import TokenService

from github_review_agent.email.email_service import EmailService
from github_review_agent.email.templates import approval_email


class ReviewWorkflowService:

    async def start_review(
        self,
        owner: str,
        repo: str,
        pr_number: int,
        approver_email: str,
    ):

        thread_id = f"{owner}-{repo}-{pr_number}"

        config = {
            "configurable": {
                "thread_id": thread_id
            }
        }

        result = await graph.ainvoke(
            {
                "owner": owner,
                "repo": repo,
                "pr_number": pr_number,
            },
            config=config,
        )

        #
        # Workflow completed without interruption
        #
        if "__interrupt__" not in result:
            return result

        review = result["__interrupt__"][0].value

        token = TokenService.generate()

        approval_store.save(
            ApprovalRequest(
                token=token,
                thread_id=thread_id,
                owner=owner,
                repo=repo,
                pr_number=pr_number,
                approver_email=approver_email,
                expires_at=datetime.utcnow() + timedelta(hours=24),
            )
        )

        approve_url = (
            f"http://localhost:8000/approve?token={token}"
        )

        reject_url = (
            f"http://localhost:8000/reject?token={token}"
        )

        html = approval_email(
            pr_title=review["title"],
            summary=review["summary"],
            risk=review["risk"],
            approve_url=approve_url,
            reject_url=reject_url,
        )

        EmailService().send(
            to_email=approver_email,
            subject=f"Approval Required - {review['title']}",
            html=html,
        )

        return {
            "status": "EMAIL_SENT",
            "thread_id": thread_id,
        }
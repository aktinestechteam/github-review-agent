from datetime import datetime, timedelta

from github_review_agent.approval import approval_store
from github_review_agent.approval.approval_request import ApprovalRequest
from github_review_agent.approval.token_service import TokenService


class WorkflowManager:

    def should_start(
        self,
        owner: str,
        repo: str,
        pr_number: int,
    ) -> bool:
        """
        Returns True if no active workflow exists for this PR.
        """

        for request in approval_store._store.values():

            if (
                request.owner == owner
                and request.repo == repo
                and request.pr_number == pr_number
                and request.status == "PENDING"
            ):
                return False

        return True
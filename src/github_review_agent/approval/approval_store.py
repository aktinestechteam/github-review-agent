from typing import Dict

from github_review_agent.approval.approval_request import ApprovalRequest


class ApprovalStore:

    def __init__(self):
        self._store: Dict[str, ApprovalRequest] = {}

    def save(self, request: ApprovalRequest) -> None:
        self._store[request.token] = request

    def get(self, token: str) -> ApprovalRequest | None:
        return self._store.get(token)

    def approve(self, token: str) -> None:
        request = self.get(token)
        if request:
            request.status = "APPROVED"

    def reject(self, token: str) -> None:
        request = self.get(token)
        if request:
            request.status = "REJECTED"

    def delete(self, token: str) -> None:
        self._store.pop(token, None)
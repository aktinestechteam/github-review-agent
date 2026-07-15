from fastapi import FastAPI
from datetime import datetime, timedelta
from github_review_agent.graph import graph
from langgraph.types import Command
from github_review_agent.models.review_request import ReviewRequest
from github_review_agent.approval import approval_store
from github_review_agent.approval.approval_request import ApprovalRequest
from github_review_agent.approval.token_service import TokenService

from github_review_agent.email.email_service import EmailService
from github_review_agent.email.templates import approval_email
from contextlib import asynccontextmanager
from github_review_agent.scheduler.review_scheduler import start_scheduler
from github_review_agent.review_workflow_service import (
    ReviewWorkflowService)

workflow = ReviewWorkflowService()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Scheduler...")
    start_scheduler()
    yield
    print("Stopping Scheduler...")

app = FastAPI(
    title="GitHub Review Agent",
    version="1.0.0",
    lifespan=lifespan,
)


@app.post("/review")
async def review(request: ReviewRequest):
    return await workflow.start_review(
        owner=request.owner,
        repo=request.repo,
        pr_number=request.pr_number,
        approver_email=request.approver_email,
    )

@app.get("/approve")
async def approve(token: str):

    approval_request = approval_store.get(token)

    if approval_request is None:
        return {
            "status": "ERROR",
            "message": "Invalid approval token."
        }

    if approval_request.status != "PENDING":
        return {
            "status": "ERROR",
            "message": "This approval request has already been processed."
        }

    if approval_request.expires_at < datetime.utcnow():
        return {
            "status": "ERROR",
            "message": "Approval request has expired."
        }

    config = {
        "configurable": {
            "thread_id": approval_request.thread_id
        }
    }

    result = await graph.ainvoke(
        Command(
            resume={
                "approved": True
            }
        ),
        config=config,
    )

    approval_store.approve(token)

    return {
        "status": "SUCCESS",
        "message": "Pull Request Approved",
        "result": result,
    }

@app.get("/reject")
async def reject(token: str):

    approval_request = approval_store.get(token)

    if approval_request is None:
        return {
            "status": "ERROR",
            "message": "Invalid approval token."
        }

    if approval_request.status != "PENDING":
        return {
            "status": "ERROR",
            "message": "This approval request has already been processed."
        }

    if approval_request.expires_at < datetime.utcnow():
        return {
            "status": "ERROR",
            "message": "Approval request has expired."
        }

    config = {
        "configurable": {
            "thread_id": approval_request.thread_id
        }
    }

    result = await graph.ainvoke(
        Command(
            resume={
                "approved": False
            }
        ),
        config=config,
    )

    approval_store.reject(token)

    return {
        "status": "SUCCESS",
        "message": "Pull Request Rejected",
        "result": result,
    }
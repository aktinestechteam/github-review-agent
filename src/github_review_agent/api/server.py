from fastapi import FastAPI
from github_review_agent.models.review_request import ReviewRequest
app = FastAPI(
    title="Github Review Agent",
    version="1.0.0"
)

@app.get("/")
async def home():
    return {
        "message":"GitHub Review Agent API Running"
    }
@app.post("/review")
async def start_review(request: ReviewRequest):

    return {
        "owner": request.owner,
        "repo": request.repo,
        "pr_number": request.pr_number,
    }
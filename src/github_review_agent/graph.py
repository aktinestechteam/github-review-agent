from langgraph.graph import START, END, StateGraph
from github_review_agent.state import ReviewState
from github_review_agent.nodes.fetch_pr import fetch_pr
from github_review_agent.nodes.review_pr import review_pr
from github_review_agent.nodes.merge_pr import merge_pr
from github_review_agent.nodes.reject_pr import reject_pr
from github_review_agent.nodes.approval import approval
from github_review_agent.router import approval_router
from github_review_agent.memory.checkpointer import checkpointer


builder = StateGraph(ReviewState)
builder.add_node("fetch_pr", fetch_pr)
builder.add_node("review_pr", review_pr)
builder.add_node("approval", approval)
builder.add_node("merge_pr", merge_pr)
builder.add_node("reject_pr", reject_pr)
builder.add_edge(START, "fetch_pr")
builder.add_edge("fetch_pr", "review_pr")
builder.add_edge("review_pr", "approval")
builder.add_conditional_edges(
    "approval",
    approval_router,
)
builder.add_edge("merge_pr", END)
builder.add_edge("reject_pr", END)
graph = builder.compile(checkpointer=checkpointer)
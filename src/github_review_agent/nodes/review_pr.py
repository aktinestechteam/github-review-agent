from github_review_agent.builders.review_context_builder import ReviewContextBuilder
from github_review_agent.services.ai_review_service import AIReviewService
from github_review_agent.state import ReviewState

context_builder = ReviewContextBuilder()
review_service = AIReviewService()


async def review_pr(state: ReviewState) -> dict:
    """
    Review the Pull Request using AI.
    """

    # Build context from GitHub data
    context = await context_builder.build(state)

    # Ask the LLM to review it
    review = await review_service.review(context)

    # Update graph state
    return {
        "review": review,
    }
from langchain_openai import ChatOpenAI
from github_review_agent.models.review import ReviewResult
from github_review_agent.prompts.review_prompt import SYSTEM_PROMPT
from github_review_agent.config import OPENAI_API_KEY

class AIReviewService:

    def __init__(self):

        self.llm = ChatOpenAI(
            api_key=OPENAI_API_KEY, 
            model="nvidia/nemotron-3-super-120b-a12b:free",
            base_url="https://openrouter.ai/api/v1"
    ).with_structured_output(ReviewResult)

    async def review(
        self,
        context: str,
    ) -> ReviewResult:

        messages = [
            (
                "system",
                SYSTEM_PROMPT,
            ),
            (
                "human",
                context,
            ),
        ]

        return await self.llm.ainvoke(messages)
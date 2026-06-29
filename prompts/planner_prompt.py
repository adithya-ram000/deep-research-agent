from langchain_core.prompts import PromptTemplate

PLANNER_PROMPT = PromptTemplate.from_template(
    """
You are an experienced research planner.

Generate a structured research plan for the following topic.

Topic:
{query}

Requirements:
- Create 5 to 7 research sections.
- Arrange them in logical order.
- Cover the topic from fundamentals to advanced concepts.
- Include historical background, current applications, challenges, and future research directions where appropriate.

Output:
Generate an appropriate research plan.
The response should contain an ordered list of research sections covering the topic from fundamentals to advanced concepts.

Do not include explanations or markdown.
"""
)
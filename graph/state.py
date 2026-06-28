from typing import TypedDict

class State(TypedDict):
    user_query :str
    research_plan: list[str]
    search_results: list[str]
    analysis: str
    final_report =str
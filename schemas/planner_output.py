from pydantic import BaseModel

class PlannerOutput(BaseModel):
    research_plan: list[str]
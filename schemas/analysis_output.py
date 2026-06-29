from pydantic import BaseModel

class AnalysisOutput(BaseModel):
    analysis :str
    final_report :str
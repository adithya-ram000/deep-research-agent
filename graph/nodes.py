from prompts.planner_prompt import PLANNER_PROMPT
from prompts.analysis_prompt import ANALYSIS_PROMPT
from llm.gemini import model
from schemas.planner_output import PlannerOutput
from schemas.analysis_output import AnalysisOutput
from search import search_tool

planner_structured_model =model.with_structured_output(
    PlannerOutput
)

analysis_structured_model =model.with_structured_output(
    AnalysisOutput
)

planner_chain =PLANNER_PROMPT | planner_structured_model

analysis_chain =ANALYSIS_PROMPT | analysis_structured_model
def planner(state):
    response = planner_chain.invoke(
        {
            "query": state["user_query"]
        }
    )

    return{
        "research_plan":response.research_plan
    }
    
def researcher(state):
    results ={}
    for section in state["research_plan"]:
        query =f"{state['user_query']} {section}"
        search =search_tool.invoke(query)
        results[section] =search
    return{
        "search_results":results
    }


def analyst(state):
    formatted_string =""
    for section ,results in state["search_results"].items():
        formatted_string +=f"{section}\n"
        formatted_string += "=" *40 +"\n"

        for result in results:
            formatted_string += f"Title: {result['title']}\n"
            formatted_string += f"{result['content']}\n\n"
        formatted_string +="\n"

    response =analysis_chain.invoke(
        {
            "query" : state["user_query"],
            "context" : formatted_string
        }
    )
    return{
        "final_report":response.final_report,
        "analysis":response.analysis
    }


from langgraph.graph import StateGraph
from graph.state import State
from langgraph.graph import START,END
from graph.nodes import planner,researcher,analyst
graph =StateGraph(State)

graph.add_node("planner",planner)
graph.add_node("researcher",researcher)
graph.add_node("analyst",analyst)
graph.add_edge(START,"planner")
graph.add_edge("planner","researcher")
graph.add_edge("researcher","analyst")
graph.add_edge("analyst",END)
app =graph.compile()



from langgraph.graph import END, START, StateGraph
from .nodes import Nodes
from .state import GraphState

class Workflow():
    def __init__(self, llm):
        workflow = StateGraph(GraphState)
        nodes = Nodes(llm)

        workflow.add_node("Determine Requirement", nodes.DetermineUserReq)
        workflow.add_node("Filter Gmail", nodes.FilterGmail)
        workflow.add_node("Provide Feedback", nodes.RespondToQuery)

        workflow.add_edge(START, "Determine Requirement")
        workflow.add_conditional_edges(
            "Determine Requirement", 
            nodes.IsRelateToGmail,
            {
                "YES" : "Filter Gmail",
                "No"  : "Provide Feedback"
            })
        workflow.add_edge("Filter Gmail", "Provide Feedback")
        workflow.add_edge("Provide Feedback", END)

        self.app = workflow.compile()
from langchain_community.tools.gmail.search import GmailSearch
from langchain_community.agent_toolkits import GmailToolkit
from .agents import Agents
from datetime import datetime

class Nodes:
    """
    The graph consists on the following nodes:
    * Determine the user Requirement
    * Filter Gmail (Search Gmail)
    * Answer Question
    """

    def __init__(self, llm):
        """
        Initialize the Nodes class with LLM.

        @param llm: The language model to be used for generating responses.
        """
        self.agent = Agents(llm)
        self.gmail = GmailToolkit()

    
    def DetermineUserReq(self, state):
        query = state["query"]
        result = self.agent.DetermineUserRequirement.invoke({"query": query})
        
        return{
            **state,
            "requirement": result["User Requirement summary"],
            "isGmailReq": result["Is Gmail requirement"],
            "Response": result["Response"],
        }
    
    def IsRelateToGmail(self, state):
        isGmailRequirement = state["isGmailReq"]
        if isGmailRequirement == "YES":
            return "YES"
        else:
            return "No"

    def FilterGmail(self, state):
        userReq = state["requirement"]
        state["time"] = datetime.now()

        results = self.agent.FilterGmail.invoke({"requirement": userReq, "CurrentTime": state["time"]})
        gmailSyntax = results["Gmail search syntax"]

        # Search new emails
        search = GmailSearch(api_resource = self.gmail.api_resource)
        emails = search.invoke(gmailSyntax)
        c = 1
        return{
            **state,
            "gmail_search_syntax": gmailSyntax,
            "emails": emails,
        }

    def RespondToQuery(self, state):
        if state["isGmailReq"] == "YES":
            Answer = self.agent.RespondQuery.invoke({"emails":state["emails"], "requirement":state["requirement"]})
            return {"Response": Answer['answer']}
        elif state["isGmailReq"] == "No":
            return {"Response": state["Response"]}
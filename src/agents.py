from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from .prompts import *

class Agents():
    def __init__(self, llm) -> None:

        # Determine the user Requirement    
        UserReq_prompt = PromptTemplate.from_template(DetermineRequirement_prompt_template)
        
        self.DetermineUserRequirement = (
            {"query":RunnablePassthrough()}
            | UserReq_prompt
            | llm
            | JsonOutputParser()
        )
        
        # Filter Gmail 
        Filter_prompt = PromptTemplate.from_template(GmailSearchingRules_prompt_template)

        self.FilterGmail = (
            {"requirement":RunnablePassthrough(), "CurrentTime":RunnablePassthrough()}
            | Filter_prompt
            | llm
            | JsonOutputParser()
        )

        # Answer Question
        Answer_Prompt = PromptTemplate.from_template(Answer_prompt_template
                    )
        self.RespondQuery = Answer_Prompt | llm | JsonOutputParser()
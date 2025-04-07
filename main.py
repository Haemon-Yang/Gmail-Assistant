from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from src.graph import Workflow
from colorama import Fore, Style
from pprint import pprint
from datetime import datetime

# Load all env variables
load_dotenv()

llm = ChatOpenAI(model = "gpt-4-turbo")

workflow = Workflow(llm)

app = workflow.app

# Run the agent
print(Fore.GREEN + "Starting workflow..." + Style.RESET_ALL)
while True:
    user_input = input("Tell me what do you want to do:")
    if user_input.strip().lower() == "exit":
        pprint(Fore.CYAN + f"Finished running!" + Style.RESET_ALL)
        break
    # Update state with the user input
    state = {"query": user_input, "time":datetime.now()}
    
    # Stream the workflow execution and capture the output
    for output in app.stream(state):     
        final_ouput = output
    print(output["Provide Feedback"]["Response"])
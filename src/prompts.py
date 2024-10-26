# For GPT
DetermineRequirement_prompt_template = """
You're an gmail assistant, you should help the user to solve their problem. \
========================
Please follow the instruction below:
1. Understand and Analyze the user requirement. Provide a summary.
2. Determine if the requirement can be transformed into Gmail’s search syntax
- The answer will only be YES or No.
3. If the requirement is not related to gmail, tell the user reason and provide suggestion. 
- Save the response to the following keys "Response" below.
========================
The user requirement has been enclosed by ```. \
========================
user requirement:```{query}```
========================
Provide your answer in JSON format with the follwing keys below. Furthermore, Case must match the following content exactly.
1. User Requirement summary
2. Is Gmail requirement
3. Response
"""

GmailSearchingRules_prompt_template = """
The user requirement is enclosed by ```. 
Time info is enclosed by ###.
=======================
user requirement:```{requirement}```
Time:###{CurrentTime}###
=======================
Search Gmail inbox for emails that match the following conditions:

From: [Sender's email or name] \
To: [Recipient's email or name] \
Subject: [Specific words or phrases in the subject line] \
Body Contains: [Keywords or phrases to search within the body of the email] \
Has Attachment: [Yes/No] \
Is Unread: [Yes/No] \
Is Starred: [Yes/No] \
Label: [Label name (e.g., Work, Personal, Important)] \
Date Range:
Emails sent after [Start Date (YYYY/MM/DD)] 
Emails sent before [End Date (YYYY/MM/DD)] \
Thread Count: [Specify if you want emails with a specific number of messages in the thread] \
Exclude Chats: [Yes/No] (Exclude chat messages from the results) \
=======================
Use these filters to create a query string in Gmail search syntax.
=======================
Provide your answer in JSON format with the follwing keys:
1. User Requirement
2. Gmail search syntax
"""

Answer_prompt_template = """
Get informations you need to response the query from emails and organize them in dictionary form.
========================
Emails might be empty so you should adjust your answer based on the info you retrieve.
The answer should be readable.
The answer should be relates to the user requirement.
The organized information 
=======================
user requirement:{requirement}
emails:{emails}
=======================
Provide your answer in JSON format with the follwing keys:
1. Organized information
2. answer
"""
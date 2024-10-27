# Gmail Assistant

## Description

This project aims to enhance the efficiency of Gmail usage by utilizing LangGraph to create an intelligent agent that assists users with their daily inquiries related to Gmail. The agent can analyze user requirement, transform them into Gmail search syntax and retrieve relevant emails based on specified criteria.

## Features

- The agent can determine if a user’s request is related to Gmail and provide appropriate responses or suggestions.
- It can filter Gmail inboxes based on various parameters such as sender, recipient, subject, body content, attachments, and date ranges.

## Architecture

The project is structured around a workflow that integrates user input with a language model to provide responses. The main components include:

- **LangChain**: For managing the workflow.
- **OpenAI GPT-4**: For generating responses based on user input.
- **Colorama**: For colored terminal output.

## Graph for Workflow

[![alt text](stategraph.png)]

## How to Run

### Prerequest

- Python 3.10 or later
- OpenAI API key
- Google API key
- Gmail API credentials
- Python libraries (see requirements.txt)

### Set up

1. Clone the repository:

   ```bash
   git clone https://github.com/Haemon-Yang/Gmail-Assistant.git
   ```

2. Navigate to the project directory:

   ```bash
   cd yourproject
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables by creating a `.env` file and adding the necessary keys.

```env
OPENAI_API_KEY = your_openai_api_key
LANGCHAIN_API_KEY = your_langchain_api_key
TAVILY_API_KEY = your_tavily_api_key
```

4.1 Ensure Gmail API credentials are set up.

Follow [this guide](https://developers.google.com/gmail/api/quickstart/python) to set up Gmail API credentials.

Make sure it generates a `credentials.json` file.

5. Run the application:

   ```bash
   python main.py
   ```

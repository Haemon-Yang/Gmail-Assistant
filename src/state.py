from typing_extensions import TypedDict
from typing import List
from datetime import datetime

### Our graph state
class GraphState(TypedDict):
    query: str
    requirement: str
    isGmailReq: str
    gmail_search_syntax: str
    Response: str
    emails: List[dict]
    time: datetime
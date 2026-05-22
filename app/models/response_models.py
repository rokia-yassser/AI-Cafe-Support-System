from pydantic import BaseModel
from typing import Optional


class ChatResponse(BaseModel):
    final_response: str

    sentiment: Optional[str] = None
    escalation_needed: bool = False
    knowledge_result: Optional[str] = None
    action_result: Optional[str] = None

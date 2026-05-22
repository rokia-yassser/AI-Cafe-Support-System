
from typing import TypedDict


class SupportState(TypedDict):

    user_message: str

    knowledge_result: str

    sentiment: str

    action_result: str

    escalation_needed: bool

    final_response: str
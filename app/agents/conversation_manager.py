from app.core.llm import llm
from app.core.prompts import (
    FINAL_RESPONSE_PROMPT
)

def conversation_node(state):

    user_message = state["user_message"]

    knowledge = state.get(
        "knowledge_result",
        ""
    )

    sentiment = state.get(
        "sentiment",
        "calm"
    )

    action_result = state.get(
        "action_result",
        ""
    )

    escalation_needed = state.get(
        "escalation_needed",
        False
    )

    prompt = FINAL_RESPONSE_PROMPT.format(
        message=user_message,
        knowledge=knowledge,
        sentiment=sentiment,
        action_result=action_result,
        escalation_needed=escalation_needed
    )

    response = llm.invoke(prompt)

    state["final_response"] = (
        response.content
    )

    return state
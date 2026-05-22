from pydantic import BaseModel
from app.core.llm import llm
from app.core.prompts import  ACTION_AGENT_PROMPT



class ActionDecision(BaseModel):

    action: str
    details: str
    response: str



def action_node(state):

    message = state["user_message"]

    prompt = ACTION_AGENT_PROMPT.format(
        message=message
    )

    structured_llm = llm.with_structured_output(
        ActionDecision
    )

    result = structured_llm.invoke(prompt)

    state["action_result"] = {
        "action": result.action,
        "details": result.details
    }

    current_response = state.get(
        "final_response",
        ""
    )

    state["final_response"] = (
        current_response
        + "\n\n"
        + result.response
    )

    return state
# app/agents/escalation_agent.py

from pydantic import BaseModel

from app.core.llm import llm

from app.core.prompts import (
    ESCALATION_DECIDER_PROMPT
)


# =========================================================
# STRUCTURED OUTPUT
# =========================================================

class EscalationDecision(BaseModel):

    escalate: bool

    reason: str

    priority: str


# =========================================================
# ESCALATION NODE
# =========================================================

def escalation_node(state):

    user_message = state["user_message"]

    sentiment = state.get(
        "sentiment",
        "calm"
    )

    prompt = ESCALATION_DECIDER_PROMPT.format(
        message=user_message,
        sentiment=sentiment
    )

    structured_llm = llm.with_structured_output(
        EscalationDecision
    )

    result = structured_llm.invoke(prompt)

    state["escalation_needed"] = (
        result.escalate
    )

    if result.escalate:

        escalation_message = f"""

Your issue needs help from a cafe staff member.

Priority:
{result.priority}

Reason:
{result.reason}

Please wait while we connect you with the team.
"""

        current_response = state.get(
            "final_response",
            ""
        )

        state["final_response"] = (
            current_response
            + escalation_message
        )

    return state
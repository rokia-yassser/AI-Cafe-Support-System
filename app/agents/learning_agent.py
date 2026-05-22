from datetime import datetime


LEARNING_MEMORY = []


def learning_node(state):

    learning_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_message": state["user_message"],
        "sentiment": state.get("sentiment"),
        "escalation_needed": state.get(
            "escalation_needed",
            False
        ),
        "final_response": state.get(
            "final_response",
            ""
        )
    }

    LEARNING_MEMORY.append(
        learning_entry
    )

    return state
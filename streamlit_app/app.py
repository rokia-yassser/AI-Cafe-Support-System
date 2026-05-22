import streamlit as st
import requests
from datetime import datetime


st.set_page_config(
    page_title="AI Cafe Support",
    page_icon="☕",
    layout="wide"
)


st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.stChatMessage {
    border-radius: 12px;
    padding: 10px;
}

.user-message {
    background-color: #1e293b;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}

.assistant-message {
    background-color: #334155;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}

.metric-card {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}

.sidebar-content {
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# ============================================
# SESSION STATE
# ============================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_started" not in st.session_state:
    st.session_state.chat_started = False

if "api_status" not in st.session_state:
    st.session_state.api_status = "Unknown"


with st.sidebar:

    st.title("☕ AI Cafe Support")

    st.markdown("---")

    st.subheader("System Status")
    order_id = st.sidebar.text_input(
    "Order ID",
    value="ORD-1001"
)
    try:
        health = requests.get(
            "http://localhost:8000/docs",
            timeout=3
        )

        if health.status_code == 200:
            st.success("Backend Online")
            st.session_state.api_status = "Online"
        else:
            st.error("Backend Offline")
            st.session_state.api_status = "Offline"

    except:
        st.error("Backend Offline")
        st.session_state.api_status = "Offline"

    st.markdown("---")

    st.subheader("Quick Questions")

    quick_questions = [
        "What time do you close?",
        "Do you have vegan options?",
        "Where is my order?",
        "I want a refund",
        "Can I reserve a table?",
        "What desserts are available?"
    ]

    for question in quick_questions:

        if st.button(
            question,
            use_container_width=True
        ):

            current_time = datetime.now().strftime(
                "%H:%M"
            )

            # Add user message
            st.session_state.messages.append({
                "role": "user",
                "content": question,
                "time": current_time
            })

            # =================================================
            # CALL FASTAPI
            # =================================================

            try:

                response = requests.post(
                    "http://localhost:8000/chat/",
                    json={
                        "order_id": "ORD-1001",
                        "message": question
                    },
                    timeout=60
                )

                if response.status_code == 200:

                    data = response.json()

                    final_response = data.get(
                        "final_response",
                        "No response returned."
                    )

                    # Add assistant response
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": final_response,
                        "time": datetime.now().strftime(
                            "%H:%M"
                        )
                    })

                else:

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": (
                            f"API Error: "
                            f"{response.status_code}"
                        ),
                        "time": datetime.now().strftime(
                            "%H:%M"
                        )
                    })

            except Exception as e:

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"Error: {str(e)}",
                    "time": datetime.now().strftime(
                        "%H:%M"
                    )
                })

            st.rerun()

st.title("☕ AI Customer Support Assistant")

st.markdown("""
Welcome to the AI-powered cafe support system.

You can ask about:

- Menu items
- Refunds
- Reservations
- Order tracking
- Cafe policies
- Vegan options
- Opening hours
""")


chat_container = st.container()

with chat_container:

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            if "time" in message:
                st.caption(message["time"])


user_input = st.chat_input(
    "Ask about menu, orders, refunds, reservations..."
)


if user_input:

    current_time = datetime.now().strftime("%H:%M")

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "time": current_time
    })

    # Display user message immediately
    with st.chat_message("user"):
        st.markdown(user_input)
        st.caption(current_time)

    # Assistant response
    with st.chat_message("assistant"):

        thinking_placeholder = st.empty()

        thinking_placeholder.markdown(
            "⏳ Thinking..."
        )

        try:

            response = requests.post(
                "http://localhost:8000/chat/",
                json={
                    "order_id": order_id,
                    "message": user_input
                },
                timeout=60
            )

            if response.status_code == 200:

                data = response.json()

                final_response = data.get(
                    "final_response",
                    "No response returned."
                )

                sentiment = data.get(
                    "sentiment",
                    "unknown"
                )

                escalation = data.get(
                    "escalation_needed",
                    False
                )

                knowledge = data.get(
                    "knowledge_result",
                    ""
                )

                action_result = data.get(
                    "action_result",
                    ""
                )

                thinking_placeholder.empty()

                st.markdown(final_response)

                # Optional expandable details
                with st.expander("Agent Details"):

                    st.write(
                        f"**Sentiment:** {sentiment}"
                    )

                    st.write(
                        f"**Escalation Needed:** {escalation}"
                    )

                    st.write(
                        f"**Action Result:** {action_result}"
                    )

                    if knowledge:
                        st.write("**Knowledge Base Context:**")
                        st.write(knowledge[:1000])

                # Save assistant message
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": final_response,
                    "time": datetime.now().strftime("%H:%M")
                })

            else:

                thinking_placeholder.error(
                    f"API Error: {response.status_code}"
                )

        except requests.exceptions.ConnectionError:

            thinking_placeholder.error(
                "Cannot connect to FastAPI backend."
            )

        except requests.exceptions.Timeout:

            thinking_placeholder.error(
                "Request timeout."
            )

        except Exception as e:

            thinking_placeholder.error(
                f"Unexpected error: {str(e)}"
            )


st.markdown("---")

st.caption(
    "AI Cafe Support System • Streamlit + FastAPI + LangGraph"
)
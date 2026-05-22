from langgraph.graph import   StateGraph,END
from app.models.state import  SupportState
from app.agents.knowledge_agent import    knowledge_node
from app.agents.sentiment_agent import   sentiment_node
from app.agents.action_agent import   action_node

from app.agents.escalation_agent import escalation_node
from app.agents.conversation_manager import  conversation_node
from app.agents.learning_agent import  learning_node




builder = StateGraph(
    SupportState
)


builder.add_node(
    "knowledge",
    knowledge_node
)

builder.add_node(
    "sentiment",
    sentiment_node
)

builder.add_node(
    "action",
    action_node
)

builder.add_node(
    "escalation",
    escalation_node
)

builder.add_node(
    "conversation",
    conversation_node
)

builder.add_node(
    "learning",
    learning_node
)

# FLOW

builder.set_entry_point(
    "knowledge"
)

builder.add_edge(
    "knowledge",
    "sentiment"
)

builder.add_edge(
    "sentiment",
    "action"
)

builder.add_edge(
    "action",
    "escalation"
)

builder.add_edge(
    "escalation",
    "conversation"
)

builder.add_edge(
    "conversation",
    "learning"
)

builder.add_edge(
    "learning",
    END
)


support_graph = builder.compile()
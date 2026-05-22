
from app.db.vector_store import retriever
from app.core.llm import llm
from app.core.prompts import  KNOWLEDGE_BASE_PROMPT




def knowledge_node(state):

    query = state["user_message"]

    if retriever is None:

        state["knowledge_result"] = (
            "Knowledge base unavailable."
        )
        return state


    docs = retriever.invoke(query)

    context = "\n\n".join([
        doc.page_content
        for doc in docs
    ])

    state["knowledge_result"] = context

    prompt = KNOWLEDGE_BASE_PROMPT.format(
        context=context,
        question=query
    )


    response = llm.invoke
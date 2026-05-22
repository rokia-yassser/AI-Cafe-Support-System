from pydantic import BaseModel

from app.core.llm import llm

from app.core.prompts import (
    SENTIMENT_ANALYZER_PROMPT
)


class SentimentResult(BaseModel):

    sentiment: str


def sentiment_node(state):

    message = state["user_message"]

    prompt = SENTIMENT_ANALYZER_PROMPT.format(
        message=message
    )

    structured_llm = llm.with_structured_output(
        SentimentResult
    )

    result = structured_llm.invoke(prompt)

    state["sentiment"] = result.sentiment

    return state
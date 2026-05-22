from langchain_openai import ChatOpenAI
from app.core.config import settings


llm = ChatOpenAI(

    model=settings.OPENROUTER_MODEL,
    api_key=settings.OPENROUTER_API_KEY,
    base_url=settings.OPENROUTER_BASE_URL,
    temperature=0.5,
    max_tokens=200,
    timeout=60
)
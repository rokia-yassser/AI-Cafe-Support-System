from dotenv import load_dotenv
import os

from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings

# Load .env
load_dotenv()

# Environment variables
VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")


embeddings = CohereEmbeddings(
    cohere_api_key=COHERE_API_KEY,
    model=EMBEDDING_MODEL
)

vector_store = FAISS.load_local(
    VECTOR_STORE_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)


retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)
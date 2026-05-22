from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings


load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")
VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)


embeddings = CohereEmbeddings(
    cohere_api_key=COHERE_API_KEY,
    model=EMBEDDING_MODEL
)


vector_store = FAISS.from_documents(chunks, embeddings)

print(VECTOR_STORE_PATH)
vector_store.save_local(VECTOR_STORE_PATH)
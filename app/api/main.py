from fastapi import FastAPI

from app.db.database import engine
from app.db.models import Base

from app.api.routes.chat import  router as chat_router



Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Cafe Support"
)

app.include_router(chat_router)
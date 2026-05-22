from pydantic import BaseModel

class ChatRequest(BaseModel):
    
    order_id: str
    message: str
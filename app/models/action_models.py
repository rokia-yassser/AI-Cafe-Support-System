
from pydantic import BaseModel


class ActionDecision(BaseModel):
    action: str

    details: str

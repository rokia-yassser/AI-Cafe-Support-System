from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.request_models import    ChatRequest

from app.agents.graph import support_graph
from app.db.database import get_db
from app.db.crud import  create_order_conversation



router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/")
async def chat(
    req: ChatRequest,
    db: Session = Depends(get_db)
):

    result = support_graph.invoke({

        "user_message": req.message,

        "knowledge_result": "",

        "sentiment": "",

        "action_result": "",

        "escalation_needed": False,

        "final_response": ""

    })

    create_order_conversation(

        db=db,

        order_id=req.order_id,

        order_text=req.message,

        conversation_summary=result[
            "final_response"
        ],

        sentiment=result["sentiment"],

        escalation_needed=result[
            "escalation_needed"
        ],

        final_response=result[
            "final_response"
        ]
    )

    return result
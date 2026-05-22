from sqlalchemy.orm import Session
from app.db.models import OrderConversation



def create_order_conversation(
    db: Session,
    order_id: str,
    order_text: str,
    conversation_summary: str,
    sentiment: str,
    escalation_needed: bool,
    final_response: str
):

    existing_order = db.query(
        OrderConversation
    ).filter(
        OrderConversation.order_id == order_id
    ).first()

    if existing_order:
        return None

    new_order = OrderConversation(
        order_id=order_id,
        order_text=order_text,
        conversation_summary=conversation_summary,
        sentiment=sentiment,
        escalation_needed=escalation_needed,
        final_response=final_response
    )

    db.add(new_order)

    db.commit()

    db.refresh(new_order)

    return new_order
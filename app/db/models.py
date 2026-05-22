from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import Boolean

from datetime import datetime
from app.db.database import Base


class OrderConversation(Base):

    __tablename__ = "order_conversations"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    order_id = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    order_text = Column(
        Text,
        nullable=False
    )

 
    conversation_summary = Column(
        Text,
        nullable=True
    )


    sentiment = Column(
        String,
        nullable=True
    )

    escalation_needed = Column(
        Boolean,
        default=False
    )

    final_response = Column(
        Text,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


    def __repr__(self):

        return (
            f"<OrderConversation("
            f"order_id='{self.order_id}', "
            f"sentiment='{self.sentiment}'"
            f")>"
        )
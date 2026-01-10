from sqlalchemy import Column, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from src.database.base import Base

class ChatSummary(Base):
    __tablename__ = "chat_summaries"
    __table_args__ = (
        UniqueConstraint("session_id", name="uq_session_summary"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(
        UUID(as_uuid=True),
        ForeignKey("chat_sessions.id", ondelete="CASCADE"),
        nullable=False
    )

    summary = Column(String, nullable=False)
    model_name = Column(String)
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

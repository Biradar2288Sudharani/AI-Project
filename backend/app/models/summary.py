from sqlalchemy import Column, Integer, Text, String, DateTime, ForeignKey
from datetime import datetime

from app.databases.base import Base


class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(String(50), nullable=False)

    summary_text = Column(Text)

    status = Column(String(50), default="Draft")

    created_at = Column(DateTime, default=datetime.utcnow)
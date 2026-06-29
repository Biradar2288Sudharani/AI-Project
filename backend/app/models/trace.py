from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.databases.base import Base


class Trace(Base):
    __tablename__ = "traces"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(String(50), nullable=False)

    step_number = Column(Integer)

    reasoning = Column(Text)

    action = Column(Text)

    result = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
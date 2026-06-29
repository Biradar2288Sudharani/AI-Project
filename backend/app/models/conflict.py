from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.databases.base import Base


class Conflict(Base):
    __tablename__ = "conflicts"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(String(50), nullable=False)

    conflict_type = Column(String(100))

    description = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
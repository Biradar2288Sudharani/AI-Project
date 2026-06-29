from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.databases.base import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(String(50), unique=True, nullable=False)

    patient_name = Column(String(255))

    admission_date = Column(String(50))

    discharge_date = Column(String(50))

    created_at = Column(DateTime, default=datetime.utcnow)
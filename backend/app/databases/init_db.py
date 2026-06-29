from app.databases.db import engine
from app.databases.base import Base

from app.models.patient import Patient
from app.models.summary import Summary
from app.models.conflict import Conflict
from app.models.trace import Trace

Base.metadata.create_all(bind=engine)

print("✅ All Tables Created Successfully!")
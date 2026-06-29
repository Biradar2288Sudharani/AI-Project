from app.services.database_service import (
    DatabaseService
)

patient_id = DatabaseService.save_patient(
    {
        "patient_id": "P001",
        "patient_name": "Sudha Test",
        "admission_date": "2026-06-01",
        "discharge_date": "2026-06-03"
    }
)

print(
    "Saved Patient ID:",
    patient_id
)
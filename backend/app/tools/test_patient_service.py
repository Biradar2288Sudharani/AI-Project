from app.services.patient_service import PatientProcessor

result = PatientProcessor.process(
    r"uploads/patient 1.pdf"
)

print(result)
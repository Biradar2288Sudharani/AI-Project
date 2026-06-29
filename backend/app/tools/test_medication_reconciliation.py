from app.tools.medication_checker import MedicationReconciliation

admission = [
    "Paracetamol",
    "Aspirin"
]

discharge = [
    "Paracetamol",
    "Metformin"
]

result = MedicationReconciliation.compare(
    admission,
    discharge
)

print(result)
from app.services.discharge_summary_service import DischargeSummaryService


sample_data = {
    "patient_name": "MISSING",
    "admission_date": "MISSING",
    "discharge_date": "MISSING",
    "principal_diagnosis":
        "1) ACUTE GASTROENTERITIS WITH DEHYDRATION",

    "secondary_diagnosis":
        "2) URINARY TRACT INFECTION",

    "hospital_course":
        "Patient treated with IV fluids and antibiotics.",

    "procedures":
        "MISSING",

    "allergies":
        "MISSING",

    "follow_up":
        "Review on 09.03.2026",

    "pending_results":
        ["Report Awaited"],

    "discharge_condition":
        "Hemodynamically stable"
}


summary = DischargeSummaryService.generate(
    sample_data
)

print(summary)
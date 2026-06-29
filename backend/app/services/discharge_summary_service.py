class DischargeSummaryService:

    @staticmethod
    def generate(data):

        summary = f"""
==============================
DISCHARGE SUMMARY
==============================

Patient Name:
{data.get("patient_name", "MISSING")}

Admission Date:
{data.get("admission_date", "MISSING")}

Discharge Date:
{data.get("discharge_date", "MISSING")}

Principal Diagnosis:
{data.get("principal_diagnosis", "MISSING")}

Secondary Diagnosis:
{data.get("secondary_diagnosis", "MISSING")}

Hospital Course:
{data.get("hospital_course", "MISSING")}

Procedures:
{data.get("procedures", "MISSING")}

Allergies:
{data.get("allergies", "MISSING")}

Discharge Condition:
{data.get("discharge_condition", "MISSING")}

Pending Results:
{", ".join(data.get("pending_results", [])) if data.get("pending_results") else "None"}

Follow Up:
{data.get("follow_up", "MISSING")}

==============================
DRAFT FOR CLINICIAN REVIEW
==============================
"""

        return summary
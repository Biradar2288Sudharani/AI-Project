class SummaryService:

    @staticmethod
    def generate(data):

        medications = data.get(
            "discharge_medications"
        )

        if not medications:
            medications = "NOT FOUND"

        pending = data.get(
            "pending_results"
        )

        if pending:
            pending = ", ".join(pending)
        else:
            pending = "None"

        return f"""
DISCHARGE SUMMARY DRAFT

Patient Name:
{data.get('patient_name') or 'NOT FOUND IN DOCUMENT'}

Admission Date:
{data.get('admission_date') or 'NOT FOUND IN DOCUMENT'}

Discharge Date:
{data.get('discharge_date') or 'NOT FOUND IN DOCUMENT'}

Principal Diagnosis:
{data.get('principal_diagnosis') or 'NOT FOUND'}

Secondary Diagnoses:
{data.get('secondary_diagnosis') or 'NOT FOUND'}

Hospital Course:
{data.get('hospital_course') or 'NOT FOUND'}

Procedures:
{data.get('procedures') or 'NOT FOUND'}

Allergies:
{data.get('allergies') or 'NOT FOUND'}

Discharge Medications:
{medications}

Medication Changes:
{data.get('medication_changes') or 'REVIEW REQUIRED'}

Follow Up Instructions:
{data.get('follow_up') or 'NOT FOUND'}

Discharge Condition:
{data.get('discharge_condition') or 'NOT FOUND'}

Pending Results:
{pending}

*** DRAFT FOR CLINICIAN REVIEW ***
"""
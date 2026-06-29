class SummaryGenerator:

    @staticmethod
    def generate(data):

        return f"""
DISCHARGE SUMMARY DRAFT

Patient Name:
{data.get('patient_name', 'MISSING')}

Admission Date:
{data.get('admission_date', 'MISSING')}

Discharge Date:
{data.get('discharge_date', 'MISSING')}

Principal Diagnosis:
{data.get('principal_diagnosis', 'MISSING')}

Secondary Diagnoses:
{data.get('secondary_diagnosis', 'MISSING')}

Hospital Course:
{data.get('hospital_course', 'MISSING')}

Procedures:
{data.get('procedures', 'MISSING')}

Allergies:
{data.get('allergies', 'MISSING')

}

Pending Results:
{data.get('pending_results', 'MISSING')}

Discharge Condition:
{data.get('discharge_condition', 'MISSING')}

*** DRAFT FOR CLINICIAN REVIEW ***
"""
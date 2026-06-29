import re


class ClinicalExtractor:

    @staticmethod
    def extract(text: str):

        data = {
            "patient_name": "MISSING",
            "admission_date": "MISSING",
            "discharge_date": "MISSING",
            "principal_diagnosis": "MISSING",
            "secondary_diagnosis": "MISSING",
            "hospital_course": "MISSING",
            "procedures": "MISSING",
            "allergies": "MISSING",
            "follow_up": "MISSING",
            "pending_results": []
        }

        # Diagnosis

        diagnosis_match = re.search(
            r"DIAGNOSIS:(.*?)(HISTORY:)",
            text,
            re.DOTALL | re.IGNORECASE
        )

        if diagnosis_match:
            diagnosis_text = diagnosis_match.group(1).strip()

            diagnoses = [
                line.strip()
                for line in diagnosis_text.split("\n")
                if line.strip()
            ]

            if len(diagnoses) > 0:
                data["principal_diagnosis"] = diagnoses[0]

            if len(diagnoses) > 1:
                data["secondary_diagnosis"] = ", ".join(
                    diagnoses[1:]
                )

        # Hospital Course

        course_match = re.search(
            r"COURSE IN THE HOSPITAL:(.*?)(CONDITION AT DISCHARGE:)",
            text,
            re.DOTALL | re.IGNORECASE
        )

        if course_match:
            data["hospital_course"] = (
                course_match.group(1).strip()
            )

        # Discharge Condition

        condition_match = re.search(
            r"CONDITION AT DISCHARGE:(.*?)(ADVICE ON DISCHARGE:)",
            text,
            re.DOTALL | re.IGNORECASE
        )

        if condition_match:
            data["discharge_condition"] = (
                condition_match.group(1).strip()
            )

        # Follow Up

        follow_up_match = re.search(
            r"FOLLOW-UP INSTRUCTIONS:(.*?)(ER OBSERVATION CHART|NURSING DOCUMENTATION|INVESTIGATION CHECKLIST|$)",
            text,
            re.DOTALL | re.IGNORECASE
        )

        if follow_up_match:
            data["follow_up"] = follow_up_match.group(1).strip()
        else:
            data["follow_up"] = "MISSING"

        # Pending Results

        if "report awaited" in text.lower():
            data["pending_results"].append(
                "Report Awaited"
            )

        return data
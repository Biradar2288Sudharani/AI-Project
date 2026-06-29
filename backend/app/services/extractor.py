import re


class Extractor:

    @staticmethod
    def _search(patterns, text, group=1):
        """
        Search multiple regex patterns and return
        the first valid match.
        """

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE | re.DOTALL
            )

            if match:

                value = match.group(group).strip()

                value = re.sub(
                    r"\s+",
                    " ",
                    value
                )

                if value:
                    return value

        return None

    @staticmethod
    def _clean_patient_name(name):

        if not name:
            return None

        invalid_values = [

            "frequency duration",
            "frequency",
            "duration",
            "patient details",
            "patient detail",
            "full name",
            "name",
            "date of admission",
            "date of discharge",
            "diagnosis",
            "mrn",
            "male",
            "female",
            "bed",
            "ward"

        ]

        if name.lower() in invalid_values:
            return None

        if len(name) < 3:
            return None

        if len(name) > 60:
            return None

        return name

    @staticmethod
    def extract(text):

        clean_text = text.replace("\r", "\n")

        data = {

            "patient_name": None,
            "admission_date": None,
            "discharge_date": None,

            "principal_diagnosis": None,
            "secondary_diagnosis": None,

            "hospital_course": None,
            "procedures": None,

            "allergies": None,

            "discharge_medications": [],

            "follow_up": None,

            "discharge_condition": None,

            "pending_results": []

        }

        # ============================================
        # PATIENT NAME
        # ============================================

        patient_name_patterns = [

            r"Patient Name\s*:\s*(.+)",

            r"Full Name\s*:\s*(.+)",

            r"Name\s*:\s*(.+)"

        ]

        patient_name = Extractor._search(
            patient_name_patterns,
            clean_text
        )

        patient_name = (
            Extractor._clean_patient_name(
                patient_name
            )
        )

        data["patient_name"] = patient_name

        # ============================================
        # ADMISSION DATE
        # ============================================

        admission_patterns = [

            r"Admission Date\s*:\s*(.+)",

            r"Date of Admission\s*:\s*(.+)"

        ]

        data["admission_date"] = (
            Extractor._search(
                admission_patterns,
                clean_text
            )
        )

        # ============================================
        # DISCHARGE DATE
        # ============================================

        discharge_patterns = [

            r"Discharge Date\s*:\s*(.+)",

            r"Date of Discharge\s*:\s*(.+)"

        ]

        data["discharge_date"] = (
            Extractor._search(
                discharge_patterns,
                clean_text
            )
        )

        # ============================================
        # PRIMARY DIAGNOSIS
        # ============================================

        diagnosis_patterns = [

            r"Primary Diagnosis\s*:\s*(.+)",

            r"Principal Diagnosis\s*:\s*(.+)",

            r"Diagnosis\s*:\s*(.+)"

        ]

        data["principal_diagnosis"] = (
            Extractor._search(
                diagnosis_patterns,
                clean_text
            )
        )

        # ============================================
        # SECONDARY DIAGNOSIS
        # ============================================

        secondary_patterns = [

            r"Secondary Diagnosis\s*:\s*(.+)",

            r"Secondary Diagnoses\s*:\s*(.+)"

        ]

        data["secondary_diagnosis"] = (
            Extractor._search(
                secondary_patterns,
                clean_text
            )
        )

        # ============================================
        # ALLERGIES
        # ============================================

        allergy_patterns = [

            r"Allergies\s*:\s*(.+)",

            r"Drug Allergies\s*:\s*(.+)",

            r"Known Drug Allergies\s*:\s*(.+)"

        ]

        data["allergies"] = (
            Extractor._search(
                allergy_patterns,
                clean_text
            )
        )

        # ============================================
        # PART-2 STARTS FROM HERE
                # ============================================
        # HOSPITAL COURSE
        # ============================================

        course_patterns = [

            r"Hospital Course\s*(.*?)(Consultation Notes|Procedures|Discharge Medications|Follow[- ]?Up|Discharge Condition)",

            r"Course in the Hospital\s*(.*?)(Condition at Discharge|Advice on Discharge)",

            r"Clinical Course\s*(.*?)(Procedures|Follow[- ]?Up|Discharge)"

        ]

        hospital_course = Extractor._search(
            course_patterns,
            clean_text
        )

        if hospital_course:
            hospital_course = hospital_course[:1200]

        data["hospital_course"] = hospital_course

        # ============================================
        # PROCEDURES
        # ============================================

        procedure_patterns = [

            r"Procedures\s*(.*?)(Discharge Medications|Follow[- ]?Up|Discharge Condition)",

            r"Procedure Performed\s*(.*?)(Follow[- ]?Up|Discharge)",

            r"Operation\s*(.*?)(Discharge)"

        ]

        procedures = Extractor._search(
            procedure_patterns,
            clean_text
        )

        if procedures:
            procedures = procedures[:600]

        data["procedures"] = procedures

        # ============================================
        # DISCHARGE MEDICATIONS
        # ============================================

        medication_patterns = [

            r"Discharge Medications\s*(.*?)(Follow[- ]?Up|Discharge Condition)",

            r"Medications\s*(.*?)(Follow[- ]?Up|Pending Results)",

            r"Prescription\s*(.*?)(Follow[- ]?Up)"

        ]

        medicines = Extractor._search(
            medication_patterns,
            clean_text
        )

        if medicines:

            medicine_list = []

            for line in medicines.split("\n"):

                line = line.strip()

                if len(line) > 2:

                    medicine_list.append(line)

            if medicine_list:

                data["discharge_medications"] = medicine_list

        # ============================================
        # FOLLOW UP
        # ============================================

        follow_patterns = [

            r"Follow[- ]?Up Instructions\s*(.*?)(Discharge Condition|Pending Results|$)",

            r"Advice on Discharge\s*(.*?)(Pending Results|$)",

            r"Follow[- ]?Up\s*(.*?)(Pending Results|$)"

        ]

        follow_up = Extractor._search(
            follow_patterns,
            clean_text
        )

        if follow_up:

            follow_up = follow_up[:700]

        data["follow_up"] = follow_up

        # ============================================
        # DISCHARGE CONDITION
        # ============================================

        discharge_patterns = [

            r"Discharge Condition\s*:\s*(.+)",

            r"Condition at Discharge\s*:\s*(.+)",

            r"Discharge Status\s*:\s*(.+)"

        ]

        data["discharge_condition"] = Extractor._search(
            discharge_patterns,
            clean_text
        )

        # ============================================
        # PENDING RESULTS
        # ============================================

        pending_patterns = [

            r"Pending Results\s*:\s*(.+)",

            r"Pending Investigation\s*:\s*(.+)",

            r"Report Awaited\s*:\s*(.+)"

        ]

        pending = Extractor._search(
            pending_patterns,
            clean_text
        )

        if pending:

            data["pending_results"].append(
                pending
            )

        if "report awaited" in clean_text.lower():

            if "Report Awaited" not in data["pending_results"]:

                data["pending_results"].append(
                    "Report Awaited"
                )

        if "urine culture" in clean_text.lower():

            data["pending_results"].append(
                "Urine Culture Report"
            )

        if "histopathology" in clean_text.lower():

            data["pending_results"].append(
                "Histopathology Report"
            )

        if "biopsy report" in clean_text.lower():

            data["pending_results"].append(
                "Biopsy Report"
            )

        # ============================================
        # REMOVE DUPLICATES
        # ============================================

        data["pending_results"] = list(
            dict.fromkeys(
                data["pending_results"]
            )
        )

        if data["discharge_medications"]:

            data["discharge_medications"] = list(
                dict.fromkeys(
                    data["discharge_medications"]
                )
            )

        return data
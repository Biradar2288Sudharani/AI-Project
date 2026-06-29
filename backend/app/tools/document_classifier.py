import re

class DocumentClassifier:
    @staticmethod
    def classify(document_text: str) -> str:

        text = document_text.lower()

        # Discharge Summary
        if any(keyword in text for keyword in [
            "discharge summary",
            "discharge condition",
            "date of discharge",
            "follow-up instructions",
            "advice on discharge",
            "condition at discharge"
        ]):
            return "discharge_summary"

        # Admission Note
        if any(keyword in text for keyword in [
            "history",
            "physical examination",
            "chief complaints",
            "history of present illness",
            "admission date",
            "admitted under"
        ]):
            return "admission_note"

        # Nursing Notes
        if any(keyword in text for keyword in [
            "nurses notes",
            "nursing documentation",
            "nursing assessment",
            "nursing initial assessment"
        ]):
            return "nursing_document"

        # Observation Charts
        if any(keyword in text for keyword in [
            "observation chart",
            "vital parameters",
            "triage category",
            "gcs",
            "temperature",
            "pulse",
            "spo2"
        ]):
            return "observation_chart"

        # Procedure Records
        if any(keyword in text for keyword in [
            "procedure chart",
            "procedure performed",
            "iv cannulation",
            "blood transfusion",
            "oxygen",
            "ventilator"
        ]):
            return "procedure_document"

        # Lab Results
        if any(keyword in text for keyword in [
            "investigations",
            "laboratory",
            "cbc",
            "creatinine",
            "hemoglobin",
            "sodium",
            "potassium",
            "urine culture",
            "biochemical investigations"
        ]):
            return "lab_results"

        # Medication Record
        if any(keyword in text for keyword in [
            "medication",
            "medication administration",
            "drug",
            "dosage",
            "frequency",
            "tablet",
            "tab.",
            "capsule",
            "inj."
        ]):
            return "medication_record"

        return "unknown"
    
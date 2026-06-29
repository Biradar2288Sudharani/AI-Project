from app.tools.pdf_reader import PDFReader
from app.tools.document_classifier import DocumentClassifier

from app.services.extractor import Extractor
from app.services.missing_data_checker import MissingDataChecker
from app.services.summary_service import SummaryService

from app.tools.medication_checker import MedicationReconciliation
from app.tools.conflict_detector import ConflictDetector
from app.tools.drug_interaction_tool import DrugInteractionTool
from app.tools.escalation_tool import EscalationTool

class DischargeAgent:

    MAX_STEPS = 10

    def run(self, file_path):

        print(f"\nAGENT RECEIVED FILE PATH: {file_path}")

        trace = []

        current_step = 0

        text = ""
        document_type = ""

        extracted_data = {}
        validation = {}
        summary = ""

        while current_step < self.MAX_STEPS:

            current_step += 1

            # STEP 1 - READ PDF
            if current_step == 1:

                text = PDFReader.extract_text(
                    file_path
                )

                print(
                    "\n===== EXTRACTED TEXT ====="
                )

                print(
                    text[:5000]
                )

                trace.append(
                    {
                        "reasoning": "Read PDF",
                        "action": "PDFReader",
                        "result": "Success"
                    }
                )

            # STEP 2 - CLASSIFY DOCUMENT
            elif current_step == 2:

                document_type = (
                    DocumentClassifier.classify(
                        text
                    )
                )

                print(
                    "\nDOCUMENT TYPE DETECTED:"
                )

                print(
                    document_type
                )

                trace.append(
                    {
                        "reasoning": "Classify Document",
                        "action": "DocumentClassifier",
                        "result": document_type
                    }
                )

            # STEP 3 - EXTRACT DATA
            elif current_step == 3:

                extracted_data = (
                    Extractor.extract(
                        text
                    )
                )

                print(
                    "\n===== EXTRACTED DATA ====="
                )

                print(
                    extracted_data
                )

                trace.append(
                    {
                        "reasoning": "Extract Clinical Data",
                        "action": "Extractor",
                        "result": "Success"
                    }
                )

            # STEP 4 - CHECK MISSING DATA
            elif current_step == 4:

                validation = (
                    MissingDataChecker.check(
                        extracted_data
                    )
                )

                print(
                    "\n===== VALIDATION ====="
                )

                print(
                    validation
                )

                trace.append(
                    {
                        "reasoning": "Check Missing Data",
                        "action": "MissingDataChecker",
                        "result": str(validation)
                    }
                )

            # STEP 5 - MEDICATION RECONCILIATION
            elif current_step == 5:

                medication_changes = (
                    MedicationReconciliation.compare(
                        [],
                        []
                    )
                )

                trace.append(
                    {
                        "reasoning": "Medication Reconciliation",
                        "action": "MedicationReconciliation",
                        "result": str(
                            medication_changes
                        )
                    }
                )

            # STEP 6 - CONFLICT DETECTION
            elif current_step == 6:

                conflicts = (
                    ConflictDetector.detect(
                        "",
                        ""
                    )
                )

                trace.append(
                    {
                        "reasoning": "Conflict Detection",
                        "action": "ConflictDetector",
                        "result": str(conflicts)
                    }
                )

            # STEP 7 - DRUG INTERACTION CHECK
            elif current_step == 7:

                interactions = (
                    DrugInteractionTool.check(
                        []
                    )
                )

                trace.append(
                    {
                        "reasoning": "Drug Interaction Check",
                        "action": "DrugInteractionTool",
                        "result": str(
                            interactions
                        )
                    }
                )

            # STEP 8 - ESCALATION REVIEW
            elif current_step == 8:

                escalation = (
                    EscalationTool.escalate(
                        "Pending Results Found"
                    )
                )

                trace.append(
                    {
                        "reasoning": "Escalation Review",
                        "action": "EscalationTool",
                        "result": str(
                            escalation
                        )
                    }
                )

            # STEP 9 - GENERATE SUMMARY
            elif current_step == 9:

                summary = (
                    SummaryService.generate(
                        extracted_data
                    )
                )

                print(
                    "\n===== GENERATED SUMMARY ====="
                )

                print(
                    summary
                )

                trace.append(
                    {
                        "reasoning": "Generate Summary",
                        "action": "SummaryService",
                        "result": "Success"
                    }
                )

            # STEP 10 - STOP
            elif current_step == 10:

                trace.append(
                    {
                        "reasoning": "Reached Max Steps",
                        "action": "AgentStop",
                        "result": "Finished"
                    }
                )

                break

        return {
            "summary": summary,
            "trace": trace,
            "validation": validation
        }
    

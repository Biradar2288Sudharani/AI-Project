from app.services.pdf_export_service import PDFExportService

summary = """
DISCHARGE SUMMARY

Patient Name:
Sudha Test

Admission Date:
2026-06-01

Discharge Date:
2026-06-03

Principal Diagnosis:
Acute Gastroenteritis

Discharge Condition:
Stable

Pending Results:
Report Awaited

Follow Up:
Review after 1 week
"""

pdf_file = PDFExportService.generate_pdf(
    summary,
    "discharge_summary.pdf"
)

print("PDF Generated:", pdf_file)
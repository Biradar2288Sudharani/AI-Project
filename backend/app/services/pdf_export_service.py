from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


class PDFExportService:

    @staticmethod
    def generate_pdf(summary_text, output_path):

        doc = SimpleDocTemplate(output_path)

        styles = getSampleStyleSheet()

        content = []

        for line in summary_text.split("\n"):

            if line.strip():

                content.append(
                    Paragraph(line, styles["Normal"])
                )

                content.append(
                    Spacer(1, 5)
                )

        doc.build(content)

        return output_path
from app.tools.pdf_reader import PDFReader

from app.services.extractor import Extractor
from app.services.summary_service import SummaryService
from app.services.missing_data_checker import (
    MissingDataChecker
)

from app.services.trace_service import (
    TraceService
)


class PatientProcessor:

    @staticmethod
    def process(pdf_path):

        trace = TraceService.create_trace()

        text = PDFReader.extract_text(pdf_path)

        TraceService.add_trace(
            trace,
            "Read PDF",
            "PDFReader",
            "Success"
        )

        data = Extractor.extract(text)

        TraceService.add_trace(
            trace,
            "Extract Clinical Data",
            "Extractor",
            "Success"
        )

        validation = (
            MissingDataChecker.check(data)
        )

        TraceService.add_trace(
            trace,
            "Check Missing Data",
            "MissingDataChecker",
            str(validation)
        )

        summary = (
            SummaryService.generate(data)
        )

        TraceService.add_trace(
            trace,
            "Generate Summary",
            "SummaryService",
            "Success"
        )

        return {
            "summary": summary,
            "trace": trace,
            "validation": validation
        }
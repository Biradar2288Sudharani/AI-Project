from app.tools.pdf_reader import PDFReader
from app.tools.clinical_extractor import ClinicalExtractor


pdf_path = r"uploads/patient 1.pdf"

text = PDFReader.extract_text(
    pdf_path
)

result = ClinicalExtractor.extract(
    text
)

print(result)
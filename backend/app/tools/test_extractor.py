from app.tools.pdf_reader import PDFReader
from app.tools.extractor import InformationExtractor

pdf_path = r"uploads/admission_note.pdf"

text = PDFReader.extract_text(pdf_path)

data = InformationExtractor.extract(text)

print(data)
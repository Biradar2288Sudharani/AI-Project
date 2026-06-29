from app.tools.pdf_reader import PDFReader
from app.tools.document_classifier import DocumentClassifier


pdf_path = r"C:\Users\ADMIN\Desktop\AI Project\backend\uploads\admission_note.pdf"

text = PDFReader.extract_text(pdf_path)

document_type = DocumentClassifier.classify(text)

print("\n===== DOCUMENT TYPE =====")
print(document_type)